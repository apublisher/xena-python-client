"""Offline contract checks. No Xena credentials or network access required."""
import importlib
import inspect
import json
from pathlib import Path
import re
import sys
import unittest
from unittest.mock import Mock
from urllib.parse import parse_qs, urlparse

import requests

ROOT = Path(__file__).resolve().parents[1]
for package in (ROOT / 'xena').glob('xena-*'):
    sys.path.insert(0, str(package))
SPEC = json.loads((ROOT / 'specs/swagger-2026-09-09.json').read_text())


def snake(name):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower().replace('.', '_')


def clients():
    for file in (ROOT / 'xena').glob('xena-*/xena_*/*_api.py'):
        module = importlib.import_module(file.parent.name + '.' + file.stem)
        cls = next(value for name, value in vars(module).items()
                   if inspect.isclass(value) and name.endswith('Api'))
        yield cls


class SwaggerUpdateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.methods = {}
        for api in clients():
            for name, method in inspect.getmembers(api, inspect.isfunction):
                match = re.fullmatch(r'Auto-generated method for (\w+) (\S+)', inspect.getdoc(method) or '')
                if match:
                    key = match.groups()
                    if key in cls.methods:
                        raise AssertionError('Duplicate operation: ' + str(key))
                    cls.methods[key] = (api, name)

    def test_all_swagger_operations_have_methods(self):
        expected = {(verb.upper(), path) for path, methods in SPEC['paths'].items()
                    for verb in methods if verb in ('get', 'put', 'post', 'delete', 'patch', 'head', 'options')}
        self.assertEqual(expected, set(self.methods))
        self.assertEqual(1301, len(expected))

    def invoke(self, key, **kwargs):
        api, name = self.methods[key]
        session = Mock(spec=requests.Session)
        response = Mock(spec=requests.Response)
        response.json.return_value = {'ok': True}
        getattr(session, key[0].lower()).return_value = response
        result = getattr(api('https://example.invalid', session), name)(**kwargs)
        self.assertEqual({'ok': True}, result)
        response.raise_for_status.assert_called_once_with()
        getattr(session, key[0].lower()).assert_called_once()
        call = getattr(session, key[0].lower()).call_args
        return call.args[0], call.kwargs

    def test_new_operations_build_requests_from_swagger(self):
        selected = [(verb.upper(), path) for path, methods in SPEC['paths'].items()
                    for verb in methods if verb in ('get', 'put', 'post', 'delete')
                    and (path in ('/Api/Fiscal/{fiscalId}/OrderTaskBudgetPost', '/Api/Fiscal/{fiscalId}/OrderTaskBudgetPost/{id}', '/Api/Fiscal/{fiscalId}/OrderTask/{orderTaskId}/OrderTaskBudgetPost/Standard') or path.endswith('/OrderTaskLine/DeleteLines')
                         or path.endswith('/ResourcePost/Totals') or (verb == 'post' and path.endswith('/PaymentExportDraft/{contextId}/ByPaymentIds')))]
        self.assertEqual(9, len(selected))
        for key in selected:
            with self.subTest(operation=key):
                parameters = SPEC['paths'][key[1]][key[0].lower()]['parameters']
                values = {p['name']: {'Ids': [11, 12]} if p['in'] == 'body'
                          else [11, 12] if p.get('type') == 'array'
                          else False if p.get('type') == 'boolean'
                          else 11 if p.get('type') == 'integer' else 'sample'
                          for p in parameters}
                url, kwargs = self.invoke(key, **{snake(name): value for name, value in values.items()})
                expected_path = key[1]
                for p in parameters:
                    if p['in'] == 'path':
                        expected_path = expected_path.replace('{' + p['name'] + '}', str(values[p['name']]))
                    elif p['in'] == 'body':
                        self.assertEqual(values[p['name']], kwargs['json'])
                self.assertEqual('https://example.invalid' + expected_path, url)
                self.assertEqual({p['name']: values[p['name']] for p in parameters if p['in'] == 'query'}, kwargs['params'])
                required = {snake(p['name']): values[p['name']] for p in parameters if p['required']}
                _, minimal = self.invoke(key, **required)
                self.assertEqual({p['name']: values[p['name']] for p in parameters if p['in'] == 'query' and p['required']}, minimal['params'])

    def test_resource_ids_use_repeated_query_keys(self):
        key = ('GET', '/Api/Fiscal/{fiscalId}/ResourcePost/Totals')
        url, kwargs = self.invoke(key, fiscal_id='sample', filter_resource_ids=[11, 12])
        prepared = requests.Request('GET', url, params=kwargs['params']).prepare()
        self.assertEqual(['11', '12'], parse_qs(urlparse(prepared.url).query)['filter.resourceIds'])

    def test_new_filters_preserve_false_and_omit_none(self):
        for endpoint, argument, wire in [('LedgerAccount', 'exclude_article_groups_without_number', 'excludeArticleGroupsWithoutNumber'),
                                         ('Subscription', 'is_active', 'isActive')]:
            key = ('GET', '/Api/Fiscal/{fiscalId}/' + endpoint)
            for value in (False, True, None):
                with self.subTest(endpoint=endpoint, value=value):
                    _, kwargs = self.invoke(key, fiscal_id='sample', **{argument: value})
                    if value is None:
                        self.assertNotIn(wire, kwargs['params'])
                    else:
                        self.assertIs(value, kwargs['params'][wire])

    def test_inbox_query_string_remains_supported(self):
        _, kwargs = self.invoke(('GET', '/Api/Fiscal/{fiscalId}/Document/Inbox'), fiscal_id='sample', query_string='invoice')
        self.assertEqual('invoice', kwargs['params']['queryString'])


if __name__ == '__main__':
    unittest.main()
