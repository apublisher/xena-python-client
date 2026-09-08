# Experimental Xena OAuth setup

**Not verified against a registered Xena application.** Authorization Code with
PKCE, client-secret requirements, redirect acceptance, issued scopes and media
access still need a real integration check. The implementation has offline tests;
these do not establish that a particular Xena app can use this flow. Keep using
API keys or an already-issued bearer token where appropriate until that check.

This helper implements OAuth access-token acquisition, not an OpenID Connect user
login/identity validator. It does not validate or use ID tokens. It does not host
a callback server, open a browser, store tokens, or automatically refresh them.

## Configuration in the consuming application

Add this section to the application's config.json:

```json
{
  "fiscal_id": "YOUR_FISCAL_ID",
  "oauth": {
    "client_id": "YOUR_REGISTERED_CLIENT_ID",
    "redirect_uri": "http://127.0.0.1:8765/oauth/callback",
    "scopes": ["testapi"],
    "token_endpoint_auth_method": "auto"
  }
}
```

Register exactly the same redirect URI in Xena. The address above is an example,
not an address this package starts listening on. Your application must serve it.
HTTPS callbacks are supported, with HTTP allowed only for localhost/loopback.
This helper requires callback addresses without a query string or fragment.

`auto` uses `client_secret_basic` when a secret is supplied, and no client
authentication when it is absent. You can explicitly select `client_secret_basic`,
`client_secret_post` or `none`. **Public-client token exchange without a secret is
not confirmed for Xena:** the observed discovery metadata advertises basic/post
client-secret authentication. PKCE does not remove a confidential client's secret
requirement. The chosen method must match the app registration.

Pass a secret from the consuming application's environment or secret storage:

```python
import os
from xena_client import OAuthConfig, XenaOAuth, XenaClient

config = OAuthConfig.from_file(
    "config.json",
    client_secret=os.environ.get("XENA_CLIENT_SECRET"),
)
oauth = XenaOAuth(config)
login_url = oauth.authorization_url()
```

Direct construction with `OAuthConfig(client_id=..., redirect_uri=...)` also works.
Loading configuration and building the URL perform no network requests.

## Browser and callback lifecycle

1. In the application's login handler, create the helper and call
   `authorization_url()`. Redirect the user's browser to the returned URL.
2. Keep that exact helper instance in the initiating user's **server-side** session
   for the callback. It holds state and the PKCE verifier. Do not share a global
   instance between users or place it in client-visible cookies. Applications
   running multiple workers must arrange for the callback to reach its stored
   instance; this initial helper does not implement distributed session storage.
3. In the callback handler, recover the helper for that same user and pass the full
   callback URL (including its query) to `exchange_callback()`:

```python
# In your callback handler, using the helper retained from step 1:
tokens = oauth.exchange_callback(callback_url)
client = XenaClient(access_token=tokens.access_token, fiscal_id=fiscal_id)
```

The helper checks the callback address and state, then posts the code, PKCE
verifier and redirect URI to Xena. It requests `response_mode=query`; callbacks
using fragments or form_post are not implemented. State and verifier are random,
each attempt expires after ten minutes, and starting another login replaces the
pending attempt. Serialize callbacks per helper instance. Once a valid callback
is consumed, even a failed exchange requires starting a new login. Token POSTs
have a timeout and do not follow redirects or retry automatically.

Do not log callback URLs, authorization codes, token objects converted to dicts,
or token HTTP payloads. Token and client-secret fields are excluded from object
repr, but their values remain accessible to the application when needed.

## Refresh is optional and not required for early milestones

The default scope is only `testapi`. To request offline access, configure
`"scopes": ["testapi", "offline_access"]` **if the registration permits it**.
The response may still omit a refresh token. This is a successful login:

- `tokens.access_token`: required access token.
- `tokens.refresh_token`: optional; `None` when absent.
- `tokens.expires_at`: optional Unix timestamp derived from `expires_in`; `None`
  when the server supplies no duration. No lifetime is invented.
- `tokens.scope`: scope string returned by the server, if supplied.

Refresh execution is intentionally not part of this helper. For the first
milestones, repeat browser login when necessary and replace the client's token:

```python
new_login_url = oauth.authorization_url()
# Open/redirect to new_login_url and receive the next callback in the app.
new_tokens = oauth.exchange_callback(new_callback_url)
client.set_access_token(new_tokens.access_token)
```

OAuth failures raise `OAuthError` without returning raw error payloads. API calls
continue to raise `requests.HTTPError` for server rejections such as HTTP 401.
No failed accounting operation is automatically replayed. Tokens are not persisted
by the package. The wrapper's existing constructor still requires API-key
credentials; this feature is in the client package only.

## What remains to verify with Xena

- Registered app allows `response_type=code` and S256 PKCE.
- Callback address and token endpoint client authentication are accepted.
- `testapi` access is issued and works for the intended document endpoint.
- Whether that document endpoint also works with API-key-only authentication.
- Optional offline access and refresh issuance, when relevant later.

Xena's documentation describes registration and enabling offline access, but a
separate App Store approval requirement for refresh has **not** been established.
The server advertises code/PKCE support generally; that is not proof of permission
for a particular app registration.

Sources used for the implementation:

- [Xena OAuth setup](https://dev.xena.biz/xena-developer/development/get-started/xena-api-using-oauth)
- [Xena discovery metadata](https://login.xena.biz/.well-known/openid-configuration)
- [OAuth 2.0](https://www.rfc-editor.org/rfc/rfc6749.html)
- [PKCE](https://www.rfc-editor.org/rfc/rfc7636.html)

The endpoint addresses match the discovery metadata inspected on 2026-09-09.
Automatic discovery is not implemented. See README.md for original-byte document
downloads through the authenticated session.
