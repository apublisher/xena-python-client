"""Optional router state, complete state validation and unchanged direct OAuth."""
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit

import requests

ROOT = Path(__file__).resolve().parents[1]
for package in (ROOT / 'xena').glob('xena-*'):
    sys.path.insert(0, str(package))
from xena_client import OAuthConfig, OAuthError, XenaOAuth
from test_oauth_flow import TokenAdapter


class CallbackRouterTests(unittest.TestCase):
    def config(self, app_id=None):
        return OAuthConfig('registered-client', 'https://router.example/',
                           callback_app_id=app_id, response_mode='form_post')

    def test_unique_prefix_with_hyphenated_app_id(self):
        flow = XenaOAuth(self.config('audit-manager'))
        values = [parse_qs(urlsplit(flow.authorization_url()).query)['state'][0]
                  for _ in range(20)]
        self.assertEqual(len(values), len(set(values)))
        for state in values:
            self.assertRegex(state, r'^[0-9a-f]{64}-audit-manager$')
            self.assertEqual('audit-manager', state.split('-', 1)[1])

    def test_restore_and_exchange_keep_registered_redirect_uri(self):
        flow = XenaOAuth(self.config('audit-manager'))
        state = parse_qs(urlsplit(flow.authorization_url()).query)['state'][0]
        pending = flow.export_pending_login()
        receiver = XenaOAuth(self.config('audit-manager'))
        receiver.restore_pending_login(pending)
        session = requests.Session()
        session.trust_env = False
        adapter = TokenAdapter({'access_token': 'synthetic-token', 'token_type': 'Bearer'}, 200)
        session.mount('https://', adapter)
        with patch('xena_client.oauth.requests.Session', return_value=session):
            receiver.exchange_callback_params({'state': state, 'code': 'synthetic-code'})
        self.assertEqual(['https://router.example/'], parse_qs(adapter.calls[0][0].body)['redirect_uri'])
        with self.assertRaises(OAuthError):
            receiver.exchange_callback_params({'state': state, 'code': 'synthetic-code'})

    def test_tampered_prefix_or_app_id_rejected_before_network(self):
        flow = XenaOAuth(self.config('audit-manager'))
        state = parse_qs(urlsplit(flow.authorization_url()).query)['state'][0]
        for changed in (state[:65] + 'another-app', 'f' * 64 + '-audit-manager'):
            with patch('xena_client.oauth.requests.Session') as network, self.assertRaises(OAuthError):
                flow.exchange_callback_params({'state': changed, 'code': 'code'})
            network.assert_not_called()

    def test_pending_attempt_cannot_move_between_router_apps(self):
        flow = XenaOAuth(self.config('audit-manager'))
        flow.authorization_url()
        pending = flow.export_pending_login()
        for app_id in ('other-app', None):
            with self.assertRaises(OAuthError):
                XenaOAuth(self.config(app_id)).restore_pending_login(pending)
        pending['state'] = 'a' * 64 + '-other-app'
        with self.assertRaises(OAuthError):
            XenaOAuth(self.config('audit-manager')).restore_pending_login(pending)

    def test_id_limits_and_config_validation(self):
        for app_id in ('a', 'a-1', 'a' * 63):
            flow = XenaOAuth(self.config(app_id))
            flow.authorization_url()
            XenaOAuth(self.config(app_id)).restore_pending_login(flow.export_pending_login())
        for app_id in ('', 'A', '1app', '-app', 'app-', 'a' * 64, 'app.id', 'app\n', [], 42):
            with self.subTest(app_id=app_id), self.assertRaises(ValueError):
                self.config(app_id)

    def test_direct_state_and_old_pending_records_are_unchanged(self):
        flow = XenaOAuth(self.config())
        with patch('xena_client.oauth.secrets.token_urlsafe', return_value='x' * 64), \
                patch('xena_client.oauth.secrets.token_hex') as routed_random:
            state = parse_qs(urlsplit(flow.authorization_url()).query)['state'][0]
        self.assertEqual('x' * 64, state)
        routed_random.assert_not_called()
        pending = flow.export_pending_login()
        del pending['callback_app_id']  # Pending record from before router support.
        XenaOAuth(self.config()).restore_pending_login(pending)


if __name__ == '__main__':
    unittest.main()
