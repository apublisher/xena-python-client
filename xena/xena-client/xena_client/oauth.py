"""Xena authorization-code/PKCE and refresh-token operations."""

import base64
from dataclasses import dataclass, field
import hashlib
import hmac
import json
import math
import re
import secrets
import time
from typing import Mapping, Optional, Tuple
from urllib.parse import parse_qs, quote_plus, urlencode, urlsplit

import requests

from .auth import BearerTokenAuth

AUTHORIZATION_ENDPOINT = 'https://login.xena.biz/connect/authorize'
TOKEN_ENDPOINT = 'https://login.xena.biz/connect/token'


class OAuthError(ValueError):
    """Login or token exchange failed. Messages exclude callback/token payloads."""


class OAuthLoginRequired(OAuthError):
    """The application must obtain a new authorization from the user."""


@dataclass(frozen=True)
class OAuthConfig:
    client_id: str
    redirect_uri: str
    scopes: Tuple[str, ...] = ('testapi',)
    client_secret: Optional[str] = field(default=None, repr=False)
    token_endpoint_auth_method: str = 'auto'
    response_type: str = 'code'
    response_mode: str = 'query'
    callback_app_id: Optional[str] = None

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
        if self.response_type not in ('code', 'code id_token', 'code token', 'code id_token token'):
            raise ValueError('response_type must include code in a supported code or hybrid flow')
        if self.response_mode not in ('query', 'form_post'):
            raise ValueError('response_mode must be query or form_post')
        if self.response_type != 'code' and self.response_mode != 'form_post':
            raise ValueError('Hybrid responses require form_post')
        if 'id_token' in self.response_type.split() and 'openid' not in self.scopes:
            raise ValueError('A response containing id_token requires the openid scope')
        if self.callback_app_id is not None and (
                not isinstance(self.callback_app_id, str) or not re.fullmatch(
                    r'[a-z](?:[a-z0-9-]{0,61}[a-z0-9])?', self.callback_app_id)):
            raise ValueError('callback_app_id must be 1-63 lowercase letters, digits or hyphens, starting with a letter and ending with a letter or digit')

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

    def __post_init__(self):
        BearerTokenAuth(self.access_token)
        if not isinstance(self.token_type, str) or self.token_type.lower() != 'bearer':
            raise ValueError('Expected Bearer token_type')
        if self.expires_at is not None and (
                isinstance(self.expires_at, bool) or not isinstance(self.expires_at, (float, int))
                or not math.isfinite(self.expires_at)):
            raise ValueError('expires_at must be a finite Unix timestamp or None')
        if self.refresh_token is not None and (not isinstance(self.refresh_token, str) or not self.refresh_token):
            raise ValueError('refresh_token must be a non-empty string or None')
        if self.scope is not None and not isinstance(self.scope, str):
            raise ValueError('scope must be a string or None')


class XenaOAuth:
    """One pending login per instance. Keep the instance in the initiating user's
    server-side session, not globally shared between users. Login attempts expire
    after ten minutes. The application hosts the callback and stores tokens.
    """

    def __init__(self, config: OAuthConfig, *, timeout: float = 30):
        if not math.isfinite(timeout) or timeout <= 0:
            raise ValueError('timeout must be finite and positive')
        self.config = config
        self.timeout = timeout
        self._pending = None

    def authorization_url(self) -> str:
        """Begin a login, replacing any prior pending attempt. Open URL in browser."""
        state = (secrets.token_hex(32) + '-' + self.config.callback_app_id
                 if self.config.callback_app_id is not None else secrets.token_urlsafe(32))
        verifier = secrets.token_urlsafe(64)
        challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode('ascii')).digest()).rstrip(b'=').decode('ascii')
        self._pending = (state, verifier, time.monotonic() + 600)
        params = {
            'client_id': self.config.client_id,
            'redirect_uri': self.config.redirect_uri,
            'response_type': self.config.response_type,
            'response_mode': self.config.response_mode,
            'scope': ' '.join(self.config.scopes),
            'state': state,
            'code_challenge': challenge,
            'code_challenge_method': 'S256',
        }
        if 'openid' in self.config.scopes:
            params['nonce'] = secrets.token_urlsafe(32)
        if 'offline_access' in self.config.scopes:
            params['prompt'] = 'consent'
        return AUTHORIZATION_ENDPOINT + '?' + urlencode(params)

    def export_pending_login(self) -> dict:
        """Export sensitive state for storage in the user's server-side session.

        Do not send this dictionary to the browser. The application must consume
        its stored copy once, atomically, when handling the callback.
        """
        state, verifier, deadline = self._pending_login()
        return {'state': state, 'code_verifier': verifier,
                'expires_at': time.time() + (deadline - time.monotonic()),
                'client_id': self.config.client_id, 'redirect_uri': self.config.redirect_uri,
                'callback_app_id': self.config.callback_app_id}

    def restore_pending_login(self, pending: Mapping) -> None:
        """Restore an attempt from trusted server-side storage on another worker."""
        try:
            state, verifier, expiry = pending['state'], pending['code_verifier'], pending['expires_at']
            allowed = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~'
            if (pending['client_id'] != self.config.client_id or pending['redirect_uri'] != self.config.redirect_uri
                    or pending.get('callback_app_id') != self.config.callback_app_id
                    or not isinstance(state, str) or not 32 <= len(state) <= 128
                    or any(c not in allowed for c in state)
                    or (self.config.callback_app_id is not None and not re.fullmatch(
                        r'[0-9a-f]{64}-' + re.escape(self.config.callback_app_id), state))
                    or not isinstance(verifier, str) or not 43 <= len(verifier) <= 128
                    or any(c not in allowed for c in verifier)
                    or isinstance(expiry, bool) or not isinstance(expiry, (float, int)) or not math.isfinite(expiry)):
                raise ValueError()
            remaining = expiry - time.time()
            if remaining <= 0 or remaining > 600:
                raise ValueError()
        except (KeyError, TypeError, ValueError):
            raise OAuthError('Invalid or expired stored login attempt') from None
        self._pending = (state, verifier, time.monotonic() + remaining)

    def _pending_login(self):
        if self._pending is None:
            raise OAuthError('No pending login; start authorization again')
        if time.monotonic() >= self._pending[2]:
            self._pending = None
            raise OAuthError('Login attempt expired; start authorization again')
        return self._pending

    def exchange_callback(self, callback_url: str) -> OAuthTokens:
        """Validate the full callback URL and exchange its code once for tokens.

        Callback handling must be serialized per instance. After a valid callback,
        including a denied login or failed token exchange, start a fresh login to
        retry. A token response without refresh_token is a successful response.
        """
        uri = urlsplit(callback_url)
        target = urlsplit(self.config.redirect_uri)
        if (uri.scheme, uri.netloc, uri.path) != (target.scheme, target.netloc, target.path) or uri.fragment:
            raise OAuthError('Callback does not match redirect_uri')
        return self.exchange_callback_params(parse_qs(uri.query, keep_blank_values=True))

    def exchange_callback_params(self, parameters: Mapping) -> OAuthTokens:
        """Exchange a parsed form_post (or query) callback.

        Accepts strings or single-value lists/tuples. Pass a multidict unchanged
        if it has lists(); otherwise preserve duplicates when parsing the body.
        Front-channel access/ID tokens are ignored: only the code is exchanged.
        This is API authorization, not an OpenID Connect identity validator.
        """
        state, verifier, _ = self._pending_login()
        params = {}
        if not isinstance(parameters, Mapping):
            raise OAuthError('Invalid callback parameters')
        items = parameters.lists() if hasattr(parameters, 'lists') else parameters.items()
        for key, value in items:
            if isinstance(value, (list, tuple)):
                if len(value) != 1:
                    raise OAuthError('Duplicate callback parameters')
                value = value[0]
            if not isinstance(key, str) or not isinstance(value, str):
                raise OAuthError('Invalid callback parameters')
            params[key] = value
        received_state = params.get('state', '')
        if not received_state or not hmac.compare_digest(received_state.encode('utf-8'), state.encode('ascii')):
            raise OAuthError('Invalid OAuth state')
        if 'iss' in params and params['iss'] != 'https://login.xena.biz':
            raise OAuthError('Unexpected authorization issuer')
        self._pending = None
        if 'error' in params:
            raise OAuthError('Xena did not authorize the request; start a new login')
        code = params.get('code', '')
        if not code:
            raise OAuthError('Callback contains no authorization code')
        data = {'grant_type': 'authorization_code', 'code': code,
                'redirect_uri': self.config.redirect_uri, 'code_verifier': verifier}
        return self._token_request(data)

    def refresh_tokens(self, tokens: OAuthTokens) -> OAuthTokens:
        """Refresh once; keep the old refresh token if Xena does not replace it.

        May be called after access-token expiry. A refresh token's lifetime is
        controlled by Xena; expires_at describes only the access token.
        The caller must persist the result before using it for subsequent calls.
        """
        if not tokens.refresh_token:
            raise OAuthLoginRequired('No refresh token available; start a new login')
        return self._token_request({'grant_type': 'refresh_token',
                                    'refresh_token': tokens.refresh_token}, previous=tokens)

    def _token_request(self, data: dict, previous: Optional[OAuthTokens] = None) -> OAuthTokens:
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
                    if response.status_code == 400:
                        try:
                            error_payload = response.json()
                        except ValueError:
                            error_payload = None
                        if previous is not None and isinstance(error_payload, dict) and error_payload.get('error') == 'invalid_grant':
                            raise OAuthLoginRequired('Refresh token is no longer valid; start a new login')
                    if response.status_code != 200:
                        raise OAuthError('Token exchange rejected (HTTP %s); verify OAuth app configuration' % response.status_code)
                    payload = response.json()
        except requests.RequestException:
            raise OAuthError('Token request failed; no automatic retry was attempted') from None
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
        refresh = payload.get('refresh_token', previous.refresh_token if previous is not None else None)
        if 'refresh_token' in payload and refresh is None:
            raise OAuthError('Invalid refresh token in response')
        if refresh is not None and (not isinstance(refresh, str) or not refresh):
            raise OAuthError('Invalid refresh token in response')
        expires_at = None
        if 'expires_in' in payload:
            try:
                duration = float(payload['expires_in'])
                if isinstance(payload['expires_in'], bool) or not math.isfinite(duration) or duration < 0:
                    raise ValueError()
                expires_at = time.time() + duration
                if not math.isfinite(expires_at):
                    raise ValueError()
            except (ValueError, TypeError, OverflowError):
                raise OAuthError('Invalid token expiry') from None
        scope = payload.get('scope', previous.scope if previous is not None else None)
        if scope is not None and not isinstance(scope, str):
            raise OAuthError('Invalid token scope')
        return OAuthTokens(token, payload['token_type'], expires_at, refresh, scope)
