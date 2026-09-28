"""Opt-in token lifecycle with application-owned persistence."""

import math
import threading
import time
from typing import Callable, Optional
from urllib.parse import urlsplit

import requests

from .oauth import OAuthError, OAuthLoginRequired, OAuthTokens, XenaOAuth


class OAuthStorageError(OAuthError):
    """The application's token storage failed; no API request was sent."""


_NO_PENDING_SAVE = object()


class OAuthTokenManager:
    """Manage one user's Xena authorization, shared by its client instances.

    load_tokens returns OAuthTokens or None; save_tokens replaces the entire
    record, or deletes it for None. Both callbacks run under the same lock as
    refresh. The default lock serializes threads using this manager. Applications
    sharing a record across managers/processes must supply a shared lock context
    manager, also used by their login/logout handlers.
    """

    def __init__(self, oauth: XenaOAuth, *,
                 load_tokens: Callable[[], Optional[OAuthTokens]],
                 save_tokens: Callable[[Optional[OAuthTokens]], None],
                 refresh_leeway: float = 60, lock=None):
        if isinstance(refresh_leeway, bool) or not math.isfinite(refresh_leeway) or refresh_leeway < 0:
            raise ValueError('refresh_leeway must be finite and non-negative')
        if not callable(load_tokens) or not callable(save_tokens):
            raise ValueError('load_tokens and save_tokens must be callable')
        self.oauth = oauth
        self._load_tokens = load_tokens
        self._save_tokens = save_tokens
        self._refresh_leeway = refresh_leeway
        self._lock = lock if lock is not None else threading.RLock()
        self._pending_save = _NO_PENDING_SAVE

    def store_tokens(self, tokens: Optional[OAuthTokens]) -> None:
        """Save a login result, or clear this authorization with None (logout)."""
        if tokens is not None and not isinstance(tokens, OAuthTokens):
            raise ValueError('Expected OAuthTokens or None')
        with self._lock:
            self._persist(tokens)

    def _persist(self, tokens: Optional[OAuthTokens]) -> None:
        # Retain a rotated token if storage fails. On this manager's next call,
        # retry persistence before loading/refreshing any older stored token.
        self._pending_save = tokens
        try:
            self._save_tokens(tokens)
        except Exception:
            raise OAuthStorageError('Could not save OAuth tokens; retry storage on this manager') from None
        self._pending_save = _NO_PENDING_SAVE

    def _load(self) -> OAuthTokens:
        if self._pending_save is not _NO_PENDING_SAVE:
            self._persist(self._pending_save)
        try:
            tokens = self._load_tokens()
        except Exception:
            raise OAuthStorageError('Could not load OAuth tokens') from None
        if tokens is None:
            raise OAuthLoginRequired('No OAuth tokens stored; start a new login')
        if not isinstance(tokens, OAuthTokens):
            raise OAuthStorageError('Token storage must return OAuthTokens or None')
        return tokens

    def _refresh(self, tokens: OAuthTokens) -> OAuthTokens:
        try:
            updated = self.oauth.refresh_tokens(tokens)
        except OAuthLoginRequired:
            self._persist(None)
            raise
        self._persist(updated)
        return updated

    def get_access_token(self) -> str:
        """Return an access token, refreshing just before expiry when possible."""
        with self._lock:
            tokens = self._load()
            now = time.time()
            if tokens.expires_at is not None and tokens.expires_at <= now + self._refresh_leeway:
                if tokens.refresh_token:
                    tokens = self._refresh(tokens)
                elif tokens.expires_at <= now:
                    raise OAuthLoginRequired('Access token expired and cannot be refreshed; start a new login')
            if tokens.expires_at is not None and tokens.expires_at <= time.time():
                raise OAuthError('Xena returned an already expired access token')
            return tokens.access_token

    def refresh(self) -> OAuthTokens:
        """Explicitly refresh once, for example when no expiry was supplied.

        Does not retry or replay any API request. Normal requests should use
        get_access_token(), which rechecks storage under the lock first.
        """
        with self._lock:
            return self._refresh(self._load())


class OAuthTokenAuth(requests.auth.AuthBase):
    """Attach managed tokens only to the client's configured HTTPS API origin."""

    def __init__(self, manager: OAuthTokenManager, base_url: str):
        self._manager = manager
        uri = urlsplit(base_url)
        if uri.scheme != 'https' or not uri.hostname or uri.username or uri.password:
            raise ValueError('Managed OAuth requires an HTTPS API base URL')
        self._origin = (uri.scheme, uri.hostname, uri.port or 443)

    def __call__(self, request):
        uri = urlsplit(request.url)
        if ((uri.scheme, uri.hostname, uri.port or 443) != self._origin
                or uri.username is not None or uri.password is not None):
            raise OAuthError('Refusing to send OAuth credentials outside the configured API origin')
        request.headers.pop('XenaAPIKey', None)
        request.headers['Authorization'] = 'Bearer ' + self._manager.get_access_token()
        return request
