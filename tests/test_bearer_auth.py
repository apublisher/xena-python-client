"""Exercise actual requests preparation with an offline transport."""
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

import requests

ROOT = Path(__file__).resolve().parents[1]
for package in (ROOT / 'xena').glob('xena-*'):
    sys.path.insert(0, str(package))

from xena_client import XenaClient


class OfflineAdapter(requests.adapters.BaseAdapter):
    def __init__(self, status=200, content=b'{}', redirect=None):
        self.status, self.content, self.redirect = status, content, redirect
        self.requests = []

    def send(self, request, **kwargs):
        self.requests.append(request)
        response = requests.Response()
        response.status_code = self.status
        response._content = self.content
        response.request = request
        response.url = request.url
        if self.redirect and len(self.requests) == 1:
            response.status_code = 302
            response.headers['Location'] = self.redirect
        return response

    def close(self):
        pass


class BearerAuthTests(unittest.TestCase):
    def client(self, **kwargs):
        with patch.object(XenaClient, '_load_config', return_value={}):
            client = XenaClient(**kwargs)
        client.session.trust_env = False
        self.addCleanup(client.session.close)
        return client

    def test_token_without_fiscal_or_refresh_does_not_load_default_key(self):
        with patch.object(XenaClient, '_load_config', side_effect=AssertionError('Unexpected config lookup')):
            client = XenaClient(access_token='initial-token')
        self.addCleanup(client.session.close)
        request = client.session.prepare_request(requests.Request('GET', 'https://my.xena.biz/Api/User/FiscalSetup'))
        self.assertEqual('Bearer initial-token', request.headers['Authorization'])
        self.assertNotIn('XenaAPIKey', request.headers)
        self.assertEqual('', client.fiscal_id)

    def test_api_key_usage_is_preserved(self):
        client = self.client(api_key='key', fiscal_id='123')
        request = client.session.prepare_request(requests.Request('GET', client.BASE_URL))
        self.assertEqual('key', request.headers['XenaAPIKey'])
        self.assertNotIn('Authorization', request.headers)

    def test_explicit_auth_overrides_config_auth(self):
        for explicit, config in [({'access_token': 'token'}, {'api_key': 'key'}),
                                 ({'api_key': 'key'}, {'access_token': 'token'})]:
            with self.subTest(explicit=explicit), patch.object(XenaClient, '_load_config', return_value={**config, 'fiscal_id': '123'}):
                client = XenaClient(config_path='test.json', **explicit)
                self.addCleanup(client.session.close)
                self.assertEqual('123', client.fiscal_id)
                self.assertEqual(bool(explicit.get('access_token')), client.session.auth is not None)

    def test_config_token_and_conflicting_auth(self):
        with patch.object(XenaClient, '_load_config', return_value={'access_token': 'token'}):
            client = XenaClient()
            self.addCleanup(client.session.close)
            self.assertIsNotNone(client.session.auth)
        with self.assertRaises(ValueError):
            self.client(api_key='key', access_token='token')
        with patch.object(XenaClient, '_load_config', return_value={'api_key': 'key', 'access_token': 'token'}):
            with self.assertRaises(ValueError):
                XenaClient()

    def test_token_replacement_reaches_existing_domains(self):
        client = self.client(api_key='key', fiscal_id='123')
        document = client.document
        client.set_access_token('replacement')
        self.assertIs(document.session, client.session)
        for domain in ('order', 'partner', 'finance', 'document', 'core'):
            session = getattr(client, domain).session
            request = session.prepare_request(requests.Request('GET', client.BASE_URL))
            self.assertEqual('Bearer replacement', request.headers['Authorization'])
            self.assertNotIn('XenaAPIKey', request.headers)
        self.assertIsNone(client.api_key)

    def test_invalid_token_does_not_replace_valid_auth(self):
        client = self.client(access_token='valid')
        for invalid in ('', 'Bearer token', 'token\r\nHeader:value', ' token', None, 123):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                client.set_access_token(invalid)
        request = client.session.prepare_request(requests.Request('GET', client.BASE_URL))
        self.assertEqual('Bearer valid', request.headers['Authorization'])
        self.assertNotIn('valid', repr(client.session.auth))

    def test_expired_token_raises_once_without_refresh_or_replay(self):
        client = self.client(access_token='expired', fiscal_id='123')
        adapter = OfflineAdapter(status=401)
        client.session.mount('https://', adapter)
        with self.assertRaises(requests.HTTPError) as error:
            client.partner.api_partner__post_post__api__fiscal_fiscal_id__partner(dto={}, fiscal_id='123')
        self.assertEqual(401, error.exception.response.status_code)
        self.assertEqual(1, len(adapter.requests))
        self.assertEqual('Bearer expired', adapter.requests[0].headers['Authorization'])

    def test_raw_document_bytes_are_available_with_bearer_session(self):
        client = self.client(access_token='token')
        data = b'%PDF-1.7\n\x00\xff\xfe'
        adapter = OfflineAdapter(content=data)
        client.session.mount('https://', adapter)
        response = client.session.get(client.BASE_URL + '/Api/Blob/User/Download/42')
        response.raise_for_status()
        self.assertEqual(data, response.content)
        self.assertEqual('Bearer token', adapter.requests[0].headers['Authorization'])

    def test_redirect_to_other_host_does_not_forward_token(self):
        client = self.client(access_token='token')
        adapter = OfflineAdapter(redirect='https://example.invalid/document.pdf')
        client.session.mount('https://', adapter)
        client.session.get(client.BASE_URL + '/Api/Blob/User/Download/42')
        self.assertEqual(2, len(adapter.requests))
        self.assertNotIn('Authorization', adapter.requests[1].headers)


if __name__ == '__main__':
    unittest.main()
