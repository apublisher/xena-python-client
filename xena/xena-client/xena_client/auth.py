"""Bearer access-token authentication without an assumed refresh capability."""

import requests


class BearerTokenAuth(requests.auth.AuthBase):
    """Attach an existing OAuth access token. This does not log in or refresh."""

    def __init__(self, access_token: str) -> None:
        if (not isinstance(access_token, str) or not access_token
                or not access_token.isascii() or any(c.isspace() for c in access_token)):
            raise ValueError("access_token must be a non-empty token without whitespace; omit the Bearer prefix")
        self._access_token = access_token

    def __call__(self, request):
        request.headers.pop('XenaAPIKey', None)
        request.headers['Authorization'] = 'Bearer ' + self._access_token
        return request
