import base64
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import parse_qs, urlencode, urlsplit

import requests

ROOT = Path(__file__).resolve().parents[1]
for package in (ROOT / 'xena').glob('xena-*'):
    sys.path.insert(0, str(package))
from xena_client import OAuthConfig, OAuthError, XenaOAuth


class TokenAdapter(requests.adapters.BaseAdapter):
    def __init__(self, payload, status):
        self.payload, self.status, self.calls = payload, status, []

    def send(self, request, **kwargs):
        self.calls.append((request, kwargs))
        response = requests.Response()
        response.status_code = self.status
        response._content = json.dumps(self.payload).encode()
        response.request = request
        response.url = request.url
        return response

    def close(self):
        pass


class OAuthFlowTests(unittest.TestCase):
    def flow(self, **kwargs):
        return XenaOAuth(OAuthConfig('example.xena.biz', 'http://127.0.0.1:8765/callback', **kwargs))

    def callback(self, flow, **kwargs):
        query = parse_qs(urlsplit(flow.authorization_url()).query)
        return flow.config.redirect_uri + '?' + urlencode({'code': 'authorization-code', 'state': query['state'][0], **kwargs}), query

    def exchange(self, flow, callback, payload=None, status=200):
        session = requests.Session()
        session.trust_env = False
        adapter = TokenAdapter(payload if payload is not None else {'access_token': 'access-token', 'token_type': 'Bearer'}, status)
        session.mount('https://', adapter)
        self.last_adapter = adapter
        with patch('xena_client.oauth.requests.Session', return_value=session):
            return flow.exchange_callback(callback)

    def test_pkce_url_and_exchange_without_refresh(self):
        flow = self.flow()
        callback, query = self.callback(flow)
        self.assertEqual(['code'], query['response_type'])
        self.assertEqual(['query'], query['response_mode'])
        self.assertEqual(['testapi'], query['scope'])
        self.assertEqual(['S256'], query['code_challenge_method'])
        self.assertNotIn('code_verifier', query)
        tokens = self.exchange(flow, callback)
        request, options = self.last_adapter.calls[0]
        body = parse_qs(request.body)
        verifier = body['code_verifier'][0]
        self.assertTrue(43 <= len(verifier) <= 128)
        challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).rstrip(b'=').decode()
        self.assertEqual(query['code_challenge'][0], challenge)
        self.assertEqual(['authorization_code'], body['grant_type'])
        self.assertEqual([flow.config.redirect_uri], body['redirect_uri'])
        self.assertEqual([flow.config.client_id], body['client_id'])
        self.assertNotIn('Authorization', request.headers)
        self.assertEqual(30, options['timeout'])
        self.assertIsNone(tokens.refresh_token)
        self.assertIsNone(tokens.expires_at)
        self.assertEqual('access-token', tokens.access_token)
        with self.assertRaises(OAuthError):
            flow.exchange_callback(callback)

    def test_secret_auth_methods(self):
        for method in ('auto', 'client_secret_basic', 'client_secret_post'):
            with self.subTest(method=method):
                flow = self.flow(client_secret='secret: +', token_endpoint_auth_method=method)
                callback, query = self.callback(flow)
                self.assertNotIn('client_secret', query)
                self.exchange(flow, callback)
                request, _ = self.last_adapter.calls[0]
                body = parse_qs(request.body)
                if method == 'client_secret_post':
                    self.assertEqual(['secret: +'], body['client_secret'])
                    self.assertNotIn('Authorization', request.headers)
                else:
                    self.assertEqual('example.xena.biz:secret%3A+%2B', base64.b64decode(request.headers['Authorization'].split()[1]).decode())
                    self.assertNotIn('client_secret', body)
                self.assertNotIn('secret: +', repr(flow.config))

    def test_optional_refresh_and_expiry_are_returned(self):
        flow = self.flow(scopes=('testapi', 'offline_access'))
        callback, query = self.callback(flow)
        self.assertIn('offline_access', query['scope'][0])
        with patch('xena_client.oauth.time.time', return_value=1000):
            tokens = self.exchange(flow, callback, {'access_token': 'private-access', 'token_type': 'bearer', 'refresh_token': 'private-refresh', 'expires_in': 3600})
        self.assertEqual(4600, tokens.expires_at)
        self.assertEqual('private-refresh', tokens.refresh_token)
        self.assertNotIn('private', repr(tokens))

    def test_invalid_callbacks_never_call_token_endpoint(self):
        for alteration in ('state', 'host', 'fragment', 'duplicate', 'issuer'):
            with self.subTest(alteration=alteration):
                flow = self.flow()
                callback, _ = self.callback(flow)
                if alteration == 'state': callback = callback.replace('state=', 'wrong=')
                if alteration == 'host': callback = callback.replace('127.0.0.1', 'localhost')
                if alteration == 'fragment': callback += '#access_token=secret'
                if alteration == 'duplicate': callback += '&code=other-code'
                if alteration == 'issuer': callback += '&iss=https://other.invalid'
                with patch('xena_client.oauth.requests.Session') as session, self.assertRaises(OAuthError):
                    flow.exchange_callback(callback)
                session.assert_not_called()

    def test_expired_and_replaced_login(self):
        flow = self.flow()
        with patch('xena_client.oauth.time.monotonic', return_value=0):
            callback, _ = self.callback(flow)
        with patch('xena_client.oauth.time.monotonic', return_value=600), self.assertRaises(OAuthError):
            flow.exchange_callback(callback)
        old, _ = self.callback(flow)
        flow.authorization_url()
        with self.assertRaises(OAuthError): flow.exchange_callback(old)

    def test_denied_login_and_exchange_errors_do_not_leak_or_retry(self):
        flow = self.flow()
        callback, _ = self.callback(flow, error='access_denied', error_description='private-value')
        with self.assertRaises(OAuthError) as error: flow.exchange_callback(callback)
        self.assertNotIn('private-value', str(error.exception))
        for status in (400, 302, 500):
            flow = self.flow()
            callback, _ = self.callback(flow)
            with self.assertRaises(OAuthError): self.exchange(flow, callback, {'error_description': 'private-value'}, status)
            self.assertEqual(1, len(self.last_adapter.calls))
            with self.assertRaises(OAuthError): flow.exchange_callback(callback)

    def test_invalid_token_responses(self):
        for update in ({'token_type': 'MAC'}, {'access_token': ''}, {'expires_in': -1}, {'expires_in': 'nan'}, {'expires_in': True}, {'refresh_token': ''}, {'scope': []}):
            flow = self.flow(); callback, _ = self.callback(flow)
            with self.subTest(update=update), self.assertRaises(OAuthError):
                self.exchange(flow, callback, {'access_token': 'token', 'token_type': 'Bearer', **update})

    def test_config_from_file_and_validation(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / 'config.json'
            file.write_text(json.dumps({'oauth': {'client_id': 'id', 'redirect_uri': 'https://app.example/callback', 'scopes': ['testapi']}}))
            config = OAuthConfig.from_file(str(file), client_secret='secret')
        self.assertEqual(('testapi',), config.scopes)
        self.assertEqual('secret', config.client_secret)
        for uri in ('http://app.example/callback', 'https://user:pass@app.example', 'https://app.example/callback#fragment', 'https://app.example/callback?query=1'):
            with self.subTest(uri=uri), self.assertRaises(ValueError): OAuthConfig('id', uri)
        with self.assertRaises(ValueError): self.flow(token_endpoint_auth_method='client_secret_basic')
        with self.assertRaises(ValueError): self.flow(scopes='testapi')


if __name__ == '__main__':
    unittest.main()
