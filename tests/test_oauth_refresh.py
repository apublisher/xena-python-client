"""Exercise opt-in OAuth, persistence and API-key compatibility without Xena calls."""
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
from dataclasses import asdict
import json
from pathlib import Path
import sys
import tempfile
import threading
import unittest
from unittest.mock import Mock, patch
from urllib.parse import parse_qs, urlsplit

import requests

ROOT = Path(__file__).resolve().parents[1]
for package in (ROOT / 'xena').glob('xena-*'):
    sys.path.insert(0, str(package))

from xena_client import (OAuthConfig, OAuthError, OAuthLoginRequired,
                         OAuthStorageError, OAuthTokenManager, OAuthTokens,
                         XenaClient, XenaOAuth)
from test_bearer_auth import OfflineAdapter
from test_oauth_flow import TokenAdapter


class MemoryStore:
    def __init__(self, tokens):
        self.tokens = tokens
        self.saved = []

    def load(self):
        return self.tokens

    def save(self, tokens):
        self.tokens = tokens
        self.saved.append(tokens)


class OAuthRefreshTests(unittest.TestCase):
    def flow(self, **kwargs):
        return XenaOAuth(OAuthConfig('registered-app', 'https://app.example/callback', **kwargs))

    @contextmanager
    def endpoint(self, payload=None, status=200):
        session = requests.Session()
        session.trust_env = False
        adapter = TokenAdapter(payload if payload is not None else {
            'access_token': 'new-access', 'refresh_token': 'new-refresh',
            'token_type': 'Bearer', 'expires_in': 3600,
        }, status)
        session.mount('https://', adapter)
        with patch('xena_client.oauth.requests.Session', return_value=session):
            yield adapter

    def manager(self, tokens, **kwargs):
        store = MemoryStore(tokens)
        flow = self.flow(client_secret='private-secret', token_endpoint_auth_method='client_secret_post')
        manager = OAuthTokenManager(flow, load_tokens=store.load, save_tokens=store.save, **kwargs)
        return manager, store

    def client(self, manager, **kwargs):
        client = XenaClient(oauth=manager, **kwargs)
        client.session.trust_env = False
        adapter = OfflineAdapter()
        client.session.mount('https://', adapter)
        self.addCleanup(client.session.close)
        return client, adapter

    def test_hybrid_form_post_uses_code_pkce_and_token_endpoint_result(self):
        flow = self.flow(scopes=('openid', 'profile', 'testapi', 'offline_access'),
                         response_type='code id_token token', response_mode='form_post',
                         client_secret='private-secret', token_endpoint_auth_method='client_secret_post')
        query = parse_qs(urlsplit(flow.authorization_url()).query)
        self.assertEqual(['code id_token token'], query['response_type'])
        self.assertEqual(['form_post'], query['response_mode'])
        self.assertEqual(['consent'], query['prompt'])
        self.assertTrue(query['nonce'][0])
        with self.endpoint() as adapter:
            tokens = flow.exchange_callback_params({'state': query['state'], 'code': ['the-code'],
                                                    'access_token': 'browser-token', 'id_token': 'ignored'})
        body = parse_qs(adapter.calls[0][0].body)
        self.assertEqual(['the-code'], body['code'])
        self.assertIn('code_verifier', body)
        self.assertEqual([flow.config.redirect_uri], body['redirect_uri'])
        self.assertEqual('new-access', tokens.access_token)
        self.assertEqual('new-refresh', tokens.refresh_token)
        self.assertNotIn('browser-token', adapter.calls[0][0].body)

    def test_form_post_rejects_state_duplicates_errors_and_missing_code(self):
        for update in ({'state': 'wrong'}, {'code': ['a', 'b']}, {'state': []},
                       {'error': 'access_denied'}, {'code': ''}, {'code': 123},
                       {'iss': 'https://other.example'}):
            with self.subTest(update=update):
                flow = self.flow(response_mode='form_post')
                state = parse_qs(urlsplit(flow.authorization_url()).query)['state'][0]
                with patch('xena_client.oauth.requests.Session') as session:
                    with self.assertRaises(OAuthError):
                        flow.exchange_callback_params({'state': state, 'code': 'code', **update})
                session.assert_not_called()

    def test_multidict_duplicates_are_not_flattened(self):
        class MultiDict(dict):
            def lists(self):
                return [('state', [self['state']]), ('code', ['first', 'second'])]
        flow = self.flow()
        state = parse_qs(urlsplit(flow.authorization_url()).query)['state'][0]
        with self.assertRaisesRegex(OAuthError, 'Duplicate'):
            flow.exchange_callback_params(MultiDict(state=state, code='first'))

    def test_pending_login_roundtrip_between_workers_and_expiry(self):
        flow = self.flow()
        query = parse_qs(urlsplit(flow.authorization_url()).query)
        with patch('xena_client.oauth.time.time', return_value=1000):
            stored = json.loads(json.dumps(flow.export_pending_login()))
        other_worker = self.flow()
        with patch('xena_client.oauth.time.time', return_value=1200):
            other_worker.restore_pending_login(stored)
        with self.endpoint() as adapter:
            other_worker.exchange_callback_params({'state': query['state'], 'code': 'code'})
        self.assertEqual([stored['code_verifier']], parse_qs(adapter.calls[0][0].body)['code_verifier'])
        with self.assertRaises(OAuthError):
            other_worker.exchange_callback_params({'state': query['state'], 'code': 'code'})
        for update in ({'expires_at': 1200}, {'client_id': 'another-app'},
                       {'redirect_uri': 'https://other.example'}, {'code_verifier': 'short'},
                       {'expires_at': float('nan')}, {'state': 'bad\nstate'}):
            with self.subTest(update=update), patch('xena_client.oauth.time.time', return_value=1200):
                with self.assertRaises(OAuthError):
                    self.flow().restore_pending_login({**stored, **update})

    def test_refresh_preserves_or_rotates_and_never_invents_expiry(self):
        original = OAuthTokens('old-access', expires_at=0, refresh_token='old-refresh', scope='testapi')
        for replacement in ({}, {'refresh_token': 'rotated', 'scope': 'testapi profile', 'expires_in': 3600}):
            with self.subTest(replacement=replacement), self.endpoint({
                    'access_token': 'new-access', 'token_type': 'Bearer', **replacement}) as adapter:
                with patch('xena_client.oauth.time.time', return_value=1000):
                    refreshed = self.flow().refresh_tokens(original)
                body = parse_qs(adapter.calls[0][0].body)
            self.assertEqual(['refresh_token'], body['grant_type'])
            self.assertEqual(['old-refresh'], body['refresh_token'])
            for field in ('code', 'redirect_uri', 'code_verifier', 'scope'):
                self.assertNotIn(field, body)
            self.assertEqual(replacement.get('refresh_token', 'old-refresh'), refreshed.refresh_token)
            self.assertEqual(replacement.get('scope', 'testapi'), refreshed.scope)
            self.assertEqual(4600 if replacement else None, refreshed.expires_at)
            self.assertEqual('old-refresh', original.refresh_token)

    def test_refresh_auth_methods_and_missing_refresh(self):
        for method in ('auto', 'client_secret_basic', 'client_secret_post', 'none'):
            secret = None if method == 'none' else 'private-secret'
            with self.subTest(method=method), self.endpoint() as adapter:
                self.flow(client_secret=secret, token_endpoint_auth_method=method).refresh_tokens(
                    OAuthTokens('old', refresh_token='refresh'))
            request, options = adapter.calls[0]
            body = parse_qs(request.body)
            self.assertEqual(30, options['timeout'])
            self.assertNotIn('XenaAPIKey', request.headers)
            if method in ('auto', 'client_secret_basic'):
                self.assertTrue(request.headers['Authorization'].startswith('Basic '))
                self.assertNotIn('client_secret', body)
            else:
                self.assertNotIn('Authorization', request.headers)
                self.assertEqual(['registered-app'], body['client_id'])
                self.assertEqual(['private-secret'] if secret else None, body.get('client_secret'))
        with patch('xena_client.oauth.requests.Session') as session, self.assertRaises(OAuthLoginRequired):
            self.flow().refresh_tokens(OAuthTokens('access'))
        session.assert_not_called()

    def test_invalid_grant_requires_login_other_failures_are_not_misclassified(self):
        tokens = OAuthTokens('access', refresh_token='refresh')
        for status, error in ((400, 'invalid_grant'), (400, 'unauthorized_client'),
                              (401, 'invalid_client'), (500, 'server_error'), (302, 'redirect')):
            with self.subTest(status=status, error=error):
                with self.endpoint({'error': error, 'error_description': 'private-detail'}, status) as adapter:
                    with self.assertRaises(OAuthError) as caught:
                        self.flow().refresh_tokens(tokens)
                self.assertEqual(error == 'invalid_grant', isinstance(caught.exception, OAuthLoginRequired))
                self.assertNotIn('private-detail', str(caught.exception))
                self.assertEqual(1, len(adapter.calls))

    def test_refresh_network_failure_and_invalid_payloads_do_not_leak(self):
        flow = self.flow()
        tokens = OAuthTokens('old', refresh_token='refresh')
        with patch('xena_client.oauth.requests.Session') as session:
            session.return_value.__enter__.return_value.post.side_effect = requests.Timeout('private-detail')
            with self.assertRaises(OAuthError) as caught:
                flow.refresh_tokens(tokens)
            self.assertNotIn('private-detail', str(caught.exception))
            self.assertEqual(1, session.return_value.__enter__.return_value.post.call_count)
        for update in ({'refresh_token': None}, {'refresh_token': ''}, {'token_type': 'MAC'},
                       {'expires_in': -1}, {'expires_in': float('inf')}, {'access_token': 'bad\r\nheader'}):
            with self.subTest(update=update), self.endpoint({'access_token': 'new', 'token_type': 'Bearer', **update}):
                with self.assertRaises(OAuthError):
                    flow.refresh_tokens(tokens)

    def test_api_call_after_a_month_refreshes_and_saves_before_sending(self):
        manager, store = self.manager(OAuthTokens('old', expires_at=3600, refresh_token='old-refresh'))
        with patch.object(XenaClient, '_load_config', side_effect=AssertionError('Config should not load')):
            client, api = self.client(manager)
        old_domain = client.partner
        with patch('xena_client.token_manager.time.time', return_value=30 * 24 * 3600), self.endpoint() as token_endpoint:
            # Offline API transport checks persistence happened before sending.
            original_send = api.send
            def send(request, **kwargs):
                self.assertEqual('new-refresh', store.tokens.refresh_token)
                return original_send(request, **kwargs)
            api.send = send
            old_domain.api_partner__post_post__api__fiscal_fiscal_id__partner(dto={}, fiscal_id='123')
            client.session.get(client.BASE_URL + '/Api/User/FiscalSetup')
        self.assertEqual(1, len(token_endpoint.calls))
        self.assertEqual(2, len(api.requests))
        for request in api.requests:
            self.assertEqual('Bearer new-access', request.headers['Authorization'])
            self.assertNotIn('XenaAPIKey', request.headers)
        self.assertEqual(1, len(store.saved))

    def test_leeway_missing_refresh_and_unknown_expiry(self):
        for expiry, refresh, expect_refresh, expect_login in (
                (1061, 'refresh', False, False), (1060, 'refresh', True, False),
                (1020, None, False, False), (1000, None, False, True),
                (None, 'refresh', False, False), (None, None, False, False)):
            with self.subTest(expiry=expiry, refresh=refresh):
                manager, _ = self.manager(OAuthTokens('access', expires_at=expiry, refresh_token=refresh))
                with patch('xena_client.token_manager.time.time', return_value=1000), self.endpoint() as adapter:
                    if expect_login:
                        with self.assertRaises(OAuthLoginRequired): manager.get_access_token()
                    else:
                        self.assertEqual('new-access' if expect_refresh else 'access', manager.get_access_token())
                self.assertEqual(int(expect_refresh), len(adapter.calls))

    def test_401_never_replays_a_write_or_refreshes_after_the_request(self):
        manager, _ = self.manager(OAuthTokens('valid', expires_at=None, refresh_token='refresh'))
        client, api = self.client(manager)
        api.status = 401
        with self.endpoint() as adapter:
            with self.assertRaises(requests.HTTPError):
                client.partner.api_partner__post_post__api__fiscal_fiscal_id__partner(dto={}, fiscal_id='123')
        self.assertEqual(1, len(api.requests))
        self.assertEqual(0, len(adapter.calls))

    def test_revoked_refresh_clears_storage_and_sends_no_api_request(self):
        manager, store = self.manager(OAuthTokens('expired', expires_at=0, refresh_token='revoked'))
        client, api = self.client(manager)
        with self.endpoint({'error': 'invalid_grant'}, 400) as adapter:
            for _ in range(2):
                with self.assertRaises(OAuthLoginRequired): client.session.get(client.BASE_URL)
        self.assertEqual([None], store.saved)
        self.assertEqual(1, len(adapter.calls))
        self.assertEqual([], api.requests)

    def test_token_endpoint_failure_preserves_stored_tokens(self):
        old = OAuthTokens('expired', expires_at=0, refresh_token='refresh')
        manager, store = self.manager(old)
        client, api = self.client(manager)
        with self.endpoint({'error': 'server_error'}, 503):
            with self.assertRaises(OAuthError): client.session.get(client.BASE_URL)
        self.assertIs(old, store.tokens)
        self.assertEqual([], store.saved)
        self.assertEqual([], api.requests)

    def test_persistence_failure_keeps_rotated_token_for_save_retry(self):
        manager, store = self.manager(OAuthTokens('expired', expires_at=0, refresh_token='old-refresh'))
        client, api = self.client(manager)
        manager._save_tokens = Mock(side_effect=RuntimeError('private-db-detail'))
        with self.endpoint() as adapter:
            with self.assertRaises(OAuthStorageError) as caught:
                client.session.get(client.BASE_URL)
            self.assertNotIn('private-db-detail', str(caught.exception))
            self.assertEqual([], api.requests)
            self.assertEqual('old-refresh', store.tokens.refresh_token)
            manager._save_tokens = store.save
            client.session.get(client.BASE_URL)
        self.assertEqual(1, len(adapter.calls))
        self.assertEqual('new-refresh', store.tokens.refresh_token)
        self.assertEqual(1, len(api.requests))

    def test_store_login_logout_and_load_failure(self):
        manager, store = self.manager(None)
        with self.assertRaises(OAuthLoginRequired): manager.get_access_token()
        manager.store_tokens(OAuthTokens('fresh'))
        self.assertEqual('fresh', manager.get_access_token())
        manager.store_tokens(None)
        with self.assertRaises(OAuthLoginRequired): manager.get_access_token()
        for result in ('invalid', RuntimeError('private-storage-detail')):
            manager._load_tokens = Mock(side_effect=result) if isinstance(result, Exception) else Mock(return_value=result)
            with self.assertRaises(OAuthStorageError) as caught: manager.get_access_token()
            self.assertNotIn('private-storage-detail', str(caught.exception))

    def test_shared_lock_serializes_two_managers_and_reloads_rotated_tokens(self):
        old = OAuthTokens('old', expires_at=0, refresh_token='refresh')
        manager, store = self.manager(old)
        lock = threading.RLock()
        manager._lock = lock
        other = OAuthTokenManager(manager.oauth, load_tokens=store.load, save_tokens=store.save, lock=lock)
        barrier = threading.Barrier(8)
        def get(index):
            barrier.wait(timeout=5)
            return (manager if index % 2 else other).get_access_token()
        with self.endpoint() as adapter, ThreadPoolExecutor(max_workers=8) as workers:
            results = list(workers.map(get, range(8)))
        self.assertEqual(['new-access'] * 8, results)
        self.assertEqual(1, len(adapter.calls))
        self.assertEqual(1, len(store.saved))

    def test_persisted_tokens_resume_in_a_new_manager(self):
        manager, store = self.manager(OAuthTokens('old', expires_at=0, refresh_token='old-refresh'))
        with self.endpoint(): manager.refresh()
        restored = OAuthTokens(**json.loads(json.dumps(asdict(store.tokens))))
        new_manager, _ = self.manager(restored)
        with self.endpoint() as adapter:
            self.assertEqual('new-access', new_manager.get_access_token())
        self.assertEqual([], adapter.calls)
        for secret in ('new-access', 'new-refresh'):
            self.assertNotIn(secret, repr(restored))
            self.assertNotIn(secret, repr(new_manager))

    def test_managed_auth_origin_and_cross_host_redirect(self):
        manager, _ = self.manager(OAuthTokens('access'))
        client, api = self.client(manager)
        for url in ('https://other.example', 'http://my.xena.biz', 'https://my.xena.biz:444',
                    'https://user:password@my.xena.biz'):
            with self.subTest(url=url), self.assertRaises(OAuthError): client.session.get(url)
        self.assertEqual([], api.requests)
        api.redirect = 'https://other.example/download'
        client.session.get(client.BASE_URL)
        self.assertEqual('Bearer access', api.requests[0].headers['Authorization'])
        self.assertNotIn('Authorization', api.requests[1].headers)

    def test_auth_conflicts_and_explicit_manager_overrides_file_auth(self):
        manager, _ = self.manager(OAuthTokens('access'))
        for kwargs in ({'api_key': 'key'}, {'access_token': 'token'}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                XenaClient(oauth=manager, **kwargs)
        with patch.object(XenaClient, '_load_config', return_value={'api_key': 'key', 'fiscal_id': '123'}):
            client, _ = self.client(manager, config_path='test.json')
        self.assertEqual('123', client.fiscal_id)
        self.assertNotIn('XenaAPIKey', client.session.headers)
        client.set_access_token('manual')
        with patch.object(manager, 'get_access_token', side_effect=AssertionError('No longer managed')):
            request = client.session.prepare_request(requests.Request('GET', client.BASE_URL))
        self.assertEqual('Bearer manual', request.headers['Authorization'])

    def test_existing_api_key_config_and_positional_constructor_need_no_oauth(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'config.json'
            path.write_text(json.dumps({'api_key': 'file-key', 'fiscal_id': '123',
                                        'oauth': {'intentionally': 'invalid'}}))
            with patch.object(XenaOAuth, '_token_request', side_effect=AssertionError('OAuth must be unused')):
                for client in (XenaClient(str(path)), XenaClient(None, 'explicit-key', '456')):
                    self.addCleanup(client.session.close)
                    self.assertIsNone(client.session.auth)
                    request = client.session.prepare_request(requests.Request('GET', client.BASE_URL))
                    self.assertEqual(client.api_key, request.headers['XenaAPIKey'])
                    self.assertNotIn('Authorization', request.headers)

    def test_new_config_validation(self):
        for kwargs in ({'response_type': 'token'}, {'response_mode': 'fragment'},
                       {'response_type': 'code token'},
                       {'response_type': 'code id_token', 'response_mode': 'form_post'}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError): self.flow(**kwargs)
        for leeway in (-1, float('inf'), float('nan'), True):
            with self.subTest(leeway=leeway), self.assertRaises(ValueError): self.manager(None, refresh_leeway=leeway)


if __name__ == '__main__':
    unittest.main()
