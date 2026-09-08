"""Experimental OAuth code + PKCE helper; not yet verified against a Xena app."""

import base64
from dataclasses import dataclass, field
import hashlib
import hmac
import json
import math
import secrets
import time
from typing import Optional, Tuple
from urllib.parse import parse_qs, quote_plus, urlencode, urlsplit

import requests

from .auth import BearerTokenAuth

AUTHORIZATION_ENDPOINT = 'https://login.xena.biz/connect/authorize'
TOKEN_ENDPOINT = 'https://login.xena.biz/connect/token'


class OAuthError(ValueError):
    """Login or token exchange failed. Messages exclude callback/token payloads."""


@dataclass(frozen=True)
class OAuthConfig:
    client_id: str
    redirect_uri: str
    scopes: Tuple[str, ...] = ('testapi',)
    client_secret: Optional[str] = field(default=None, repr=False)
    token_endpoint_auth_method: str = 'auto'

    def __post_init__(self):
        if not isinstance(self.client_id, str) or not self.client_id.strip():
            raise ValueError('client_id is required')
        uri = urlsplit(self.redirect_uri)
        if (not uri.hostname or uri.username is not None or uri.password is not None
                or uri.query or uri.fragment or any(c.isspace() for c in self.redirect_uri)
                or not (uri.scheme == 'https' or (uri.scheme == 'http' and
                        uri.hostname in ('localhost', '127.0.0.1', '::1')))):
            raise ValueError('redirect_uri must be HTTPS (or HTTP loopback), without credentials, query or fragment')
        if isinstance(self.scopes, str) or not self.scopes or any(
                not isinstance(s, str) or not s or any(ord(c) < 33 or ord(c) > 126 or c in '\\"' for c in s)
                for s in self.scopes):
            raise ValueError('scopes must be a non-empty sequence of OAuth scope names')
        object.__setattr__(self, 'scopes', tuple(self.scopes))
        if self.client_secret is not None and (not isinstance(self.client_secret, str) or not self.client_secret):
            raise ValueError('client_secret must be a non-empty string when supplied')
        if self.token_endpoint_auth_method not in ('auto', 'none', 'client_secret_basic', 'client_secret_post'):
            raise ValueError('Unsupported token endpoint authentication method')
        if self.token_endpoint_auth_method.startswith('client_secret_') and not self.client_secret:
            raise ValueError('Selected authentication method requires client_secret')
        if self.token_endpoint_auth_method == 'none' and self.client_secret:
            raise ValueError('Do not supply client_secret with authentication method none')

    @classmethod
    def from_file(cls, path: str, **overrides):
        """Load the oauth section of JSON configuration; overrides can supply a secret."""
        with open(path, encoding='utf-8') as source:
            values = json.load(source)['oauth']
        return cls(**{**values, **overrides})


@dataclass(frozen=True)
class OAuthTokens:
    access_token: str = field(repr=False)
    token_type: str = 'Bearer'
    expires_at: Optional[float] = None
    refresh_token: Optional[str] = field(default=None, repr=False)
    scope: Optional[str] = None


class XenaOAuth:
    """One pending login per instance. Keep the instance in the initiating user's
    server-side session, not globally shared between users. Login attempts expire
    after ten minutes. This helper neither hosts the callback nor refreshes tokens.
    """

    def __init__(self, config: OAuthConfig, *, timeout: float = 30):
        if not math.isfinite(timeout) or timeout <= 0:
            raise ValueError('timeout must be finite and positive')
        self.config = config
        self.timeout = timeout
        self._pending = None

    def authorization_url(self) -> str:
        """Begin a login, replacing any prior pending attempt. Open URL in browser."""
        state = secrets.token_urlsafe(32)
        verifier = secrets.token_urlsafe(64)
        challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode('ascii')).digest()).rstrip(b'=').decode('ascii')
        self._pending = (state, verifier, time.monotonic() + 600)
        return AUTHORIZATION_ENDPOINT + '?' + urlencode({
            'client_id': self.config.client_id,
            'redirect_uri': self.config.redirect_uri,
            'response_type': 'code',
            'response_mode': 'query',
            'scope': ' '.join(self.config.scopes),
            'state': state,
            'code_challenge': challenge,
            'code_challenge_method': 'S256',
        })

    def exchange_callback(self, callback_url: str) -> OAuthTokens:
        """Validate the full callback URL and exchange its code once for tokens.

        Callback handling must be serialized per instance. After a valid callback,
        including a denied login or failed token exchange, start a fresh login to
        retry. A token response without refresh_token is a successful response.
        """
        if self._pending is None:
            raise OAuthError('No pending login; start authorization again')
        state, verifier, deadline = self._pending
        if time.monotonic() >= deadline:
            self._pending = None
            raise OAuthError('Login attempt expired; start authorization again')
        uri = urlsplit(callback_url)
        target = urlsplit(self.config.redirect_uri)
        if (uri.scheme, uri.netloc, uri.path) != (target.scheme, target.netloc, target.path) or uri.fragment:
            raise OAuthError('Callback does not match redirect_uri')
        params = parse_qs(uri.query, keep_blank_values=True)
        if any(len(v) != 1 for v in params.values()):
            raise OAuthError('Duplicate callback parameters')
        received_state = params.get('state', [''])[0]
        if not received_state or not hmac.compare_digest(received_state.encode('utf-8'), state.encode('ascii')):
            raise OAuthError('Invalid OAuth state')
        if 'iss' in params and params['iss'][0] != 'https://login.xena.biz':
            raise OAuthError('Unexpected authorization issuer')
        self._pending = None
        if 'error' in params:
            raise OAuthError('Xena did not authorize the request; start a new login')
        code = params.get('code', [''])[0]
        if not code:
            raise OAuthError('Callback contains no authorization code')
        data = {'grant_type': 'authorization_code', 'code': code,
                'redirect_uri': self.config.redirect_uri, 'code_verifier': verifier}
        method = self.config.token_endpoint_auth_method
        if method == 'auto':
            method = 'client_secret_basic' if self.config.client_secret else 'none'
        # Explicit no-op auth prevents .netrc credentials from being used.
        auth = lambda request: request
        if method == 'client_secret_basic':
            auth = requests.auth.HTTPBasicAuth(quote_plus(self.config.client_id), quote_plus(self.config.client_secret))
        else:
            data['client_id'] = self.config.client_id
            if method == 'client_secret_post':
                data['client_secret'] = self.config.client_secret
        try:
            # Dedicated session: never inherit API-key or bearer authentication.
            with requests.Session() as session:
                response = session.post(TOKEN_ENDPOINT, data=data, auth=auth,
                                        headers={'Accept': 'application/json'},
                                        timeout=self.timeout, allow_redirects=False)
                with response:
                    if response.status_code != 200:
                        raise OAuthError('Token exchange rejected (HTTP %s); verify OAuth app configuration' % response.status_code)
                    payload = response.json()
        except requests.RequestException:
            raise OAuthError('Token exchange failed; start a new login') from None
        except ValueError as error:
            if isinstance(error, OAuthError):
                raise
            raise OAuthError('Invalid token response') from None
        if not isinstance(payload, dict) or 'error' in payload:
            raise OAuthError('Invalid token response')
        token = payload.get('access_token')
        try:
            BearerTokenAuth(token)
        except ValueError:
            raise OAuthError('Token response has no valid access token') from None
        if not isinstance(payload.get('token_type'), str) or payload['token_type'].lower() != 'bearer':
            raise OAuthError('Expected a Bearer token response')
        refresh = payload.get('refresh_token')
        if refresh is not None and (not isinstance(refresh, str) or not refresh):
            raise OAuthError('Invalid refresh token in response')
        expires_at = None
        if 'expires_in' in payload:
            try:
                duration = float(payload['expires_in'])
                if isinstance(payload['expires_in'], bool) or not math.isfinite(duration) or duration < 0:
                    raise ValueError()
                expires_at = time.time() + duration
            except (ValueError, TypeError, OverflowError):
                raise OAuthError('Invalid token expiry') from None
        scope = payload.get('scope')
        if scope is not None and not isinstance(scope, str):
            raise OAuthError('Invalid token scope')
        return OAuthTokens(token, payload['token_type'], expires_at, refresh, scope)
