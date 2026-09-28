# OAuth in xena-client 0.3.0

OAuth is opt-in. Existing `XenaClient(api_key=..., fiscal_id=...)`, positional
arguments and API-key config files work unchanged. No OAuth configuration,
callback route, new dependency or token storage is needed for API-key consumers.
An `oauth` section in config.json does not activate OAuth automatically.

The client handles authorization URLs, code exchange with S256 PKCE, bearer
headers and on-demand refresh. The consuming application handles HTTP routes,
browser redirects, association with its own user/session, secret storage,
persistent token storage and asking the user to authorize again when necessary.

## Register and configure the application

Register an OAuth application with Xena and configure its exact callback URI.
`client_id` identifies this registration; it is **not** the `fiscal_id`, which
identifies the accounting organization used by API methods. Scopes, response
type and client authentication must be allowed for that registration.

These settings match the successful PHP experiment on 2026-09-28. Substitute
your own registered credentials and callback:

```python
import os
from xena_client import OAuthConfig, XenaOAuth

config = OAuthConfig(
    client_id=os.environ['XENA_CLIENT_ID'],
    client_secret=os.environ['XENA_CLIENT_SECRET'],
    redirect_uri='https://your-app.example/xena/callback',
    scopes=('openid', 'profile', 'testapi', 'offline_access'),
    response_type='code id_token token',
    response_mode='form_post',
    token_endpoint_auth_method='client_secret_post',
)
oauth = XenaOAuth(config)
```

Existing defaults remain `response_type='code'`, `response_mode='query'`, scopes
`('testapi',)` and authentication `auto`. Choose `code` if the registration allows
it. Hybrid types `code id_token`, `code token`, and `code id_token token` require
`form_post`. Requesting `id_token` requires `openid`. Pure implicit flows without
a code and fragment callbacks are not supported.

`auto` uses `client_secret_basic` with a secret, otherwise `none`.
`client_secret_post` can be selected explicitly. Public-client exchange without a
secret has not been confirmed for Xena. PKCE does not replace a confidential
client's secret. Load an application's JSON `oauth` section with
`OAuthConfig.from_file(path, client_secret=...)` if preferred.

Callbacks must use HTTPS, except HTTP loopback for local apps. Callback URIs
with query strings or fragments are not supported. If a callback is forwarded
through another endpoint, keep the **original registered URI** in `redirect_uri`:
this is also the URI sent during code exchange.

## Login and callback

In the consumer's login handler:

```python
oauth = XenaOAuth(config)  # one pending login per instance
login_url = oauth.authorization_url()
pending = oauth.export_pending_login()
# Store pending in the initiating user's server-side session, then redirect
# the browser to login_url. These operations belong to your web framework.
```

`authorization_url()` creates state and a PKCE verifier, replaces any previous
pending attempt on the instance and expires after ten minutes. It requests
`prompt=consent` with `offline_access`. Building the URL makes no network request.
The exported dictionary is JSON-serializable and contains the **secret verifier**.
Store it on the server, never in a browser-visible cookie or URL. Bind it to the
initiating session and intended Xena connection, and consume the stored record
atomically once. Arrange for that session to be available on a cross-site POST
when using `form_post`, including appropriate browser cookie settings.

In the consumer's callback handler, recover and consume that pending record:

```python
oauth = XenaOAuth(config)
oauth.restore_pending_login(pending)
tokens = oauth.exchange_callback_params(form_parameters)  # form_post
# For response_mode='query', use oauth.exchange_callback(full_callback_url).
token_manager.store_tokens(tokens)
# Redirect the browser to the application's own page.
```

The application supplies `pending`, `form_parameters` and `token_manager`.
Pass parameters as a mapping of strings or single-value lists. Multidicts with
`lists()` are supported; otherwise preserve duplicates when parsing the body so
the helper can reject them. Serve the registered callback and accept the
configured response mode in the application.

Alternatively retain the original helper in a server-side session and call its
exchange method directly. Do not share that instance across users. Serialize
callback handling. After a valid callback is consumed, a denied login or failed
exchange requires a fresh login rather than reusing the code.

Only tokens from the token endpoint are used. Access/ID tokens arriving in a
hybrid callback are ignored. This library does **not** validate ID-token claims
or implement OpenID Connect user identity login. Associate the authorization
with the application's own session; do not treat decoded ID-token claims as
verified identity. State and PKCE bind the code exchange to the attempt.

## Persistent storage and automatic refresh

Configure one token manager for each Xena authorization/connection:

```python
from xena_client import OAuthTokenManager, XenaClient

token_manager = OAuthTokenManager(
    XenaOAuth(config),
    load_tokens=load_tokens,
    save_tokens=save_tokens,
)
client = XenaClient(oauth=token_manager, fiscal_id=fiscal_id)
```

The application supplies two synchronous callbacks:

- `load_tokens()` returns `OAuthTokens` for this connection, or None when there
  is no authorization.
- `save_tokens(tokens)` atomically replaces the **whole** stored record.
  If `tokens is None`, delete/clear it. Return only after durable storage succeeds;
  raise an exception on failure.

`OAuthTokens` contains `access_token`, `token_type`, `expires_at`, `refresh_token`
and `scope`. `expires_at` is an absolute Unix timestamp for the **access token**.
Use `dataclasses.asdict(tokens)` and `OAuthTokens(**record)` to serialize/restore
a private record. Keep tokens and client secrets in protected server storage;
do not log these dictionaries, callback bodies, codes or HTTP payloads. Secret
fields are excluded from dataclass repr, not from serialization.

Before preparing each API request, the manager reloads the record. If the access
token expires within 60 seconds and a refresh token exists, it refreshes, saves
the response, then supplies the bearer token. Set `refresh_leeway=...` to change
the margin. All domain APIs and downloads through `client.session` share this
behavior. Constructing the client does not load tokens or call Xena. Managed
credentials are restricted to the HTTPS API origin; cross-host redirects do not
forward the bearer token.

A new refresh token replaces the old one. If the response omits it, the old one
is retained. An omitted scope also retains the previous scope. An omitted
`expires_in` means the new access-token expiry is unknown; no lifetime is
invented. Call `token_manager.refresh()` explicitly if needed in that case.
`oauth.refresh_tokens(tokens)` is available when the application wants to manage
refresh and persistence itself.

Refresh happens when the application needs a token and can happen after access
expiry, so no scheduled keepalive is required. A month of inactivity works
**only if Xena still accepts the refresh token**. Its lifetime and inactivity
policy are controlled by Xena; a one-hour access-token duration does not establish
a refresh-token lifetime.

### Concurrency and failures

The manager serializes load/refresh/save with a thread lock. Share it between
clients for the same authorization. `requests.Session` itself should not be
mutated concurrently; separate client sessions may share one manager.

For separate managers/processes using the same record, pass `lock=` with a
reusable shared/distributed lock context manager for that connection. Use it
for every refresh and login/logout update. Callbacks must read the latest
committed record after acquiring the lock. Default locking cannot coordinate
different workers; racing refreshes can lose rotated tokens.

- `OAuthLoginRequired`: no stored tokens, expired access without refresh, or
  refresh rejected with `invalid_grant`. Start authorization again. A rejected
  refresh clears the stored record.
- `OAuthStorageError`: loading/saving failed; no API request is sent. The manager
  retains a failed pending save and retries saving it on its next call before
  reading an older token. Keep that manager alive during recovery. If it is lost
  after rotation, a new login may be needed. Multiple-worker applications must
  coordinate storage-failure recovery as well as normal refreshes.
- Other `OAuthError`: token HTTP failure, invalid response or configuration
  mismatch. Remote error payload details are omitted. Another login may not fix
  the underlying problem.
- `requests.HTTPError`: API rejection, including HTTP 401. The library never
  automatically replays the operation. Decide how to recover before making
  another call, especially after a write. Do not blindly retry accounting writes.

Token HTTP requests have a timeout (30 seconds by default), do not follow
redirects and do not retry automatically. A timeout can occur after Xena processed
a refresh, so rotation may already have happened. Persistent failure may require
a new login. There is no fallback to API-key authentication.

`token_manager.store_tokens(None)` clears local authorization; it does not revoke
tokens at Xena. `client.set_access_token(token)` switches to manual-token mode
and stops using the token manager.

## Existing manual bearer mode and wrapper

`XenaClient(access_token=token, fiscal_id=...)` still sends an already-issued
token without login, expiry tracking, persistence or refresh. Replace it with
`client.set_access_token(new_token)`. Select only one of `api_key`, `access_token`
or `oauth`. Explicit authentication overrides file authentication. Explicit
OAuth does not read a default config file; an explicit `config_path` may still
supply `fiscal_id`.

The existing wrapper's API-key constructor continues to work unchanged. This
release adds managed OAuth to **xena-client**; a wrapper OAuth entry point must
accept/inject this authenticated client or manager without requiring a dummy API
key. Callback hosting, registration and storage remain consumer responsibilities.
The library does not host a server or configure databases.

## Verification and sources

A live Python test passed on 2026-09-28 at 15:29:53 UTC, using client code at
commit `4b2ce6bf24a6643260543b2a74c6745c486d8782`, Python 3.10.12 and requests
2.25.1. The configuration was `code id_token token`, `form_post`, S256 PKCE,
`client_secret_post` and `openid profile testapi offline_access`. The registered
legacy callback forwarded the POST with HTTP 307 to the private test application.

- Code exchange returned access and refresh tokens, with a 3600-second access lifetime.
- Tokens were persisted and loaded by a new Python process.
- The real generated `GET /Api/User/FiscalSetup` method returned HTTP 200 and JSON.
- After the test advanced only the stored access-token expiry, the next API call
  triggered automatic refresh. The replacement refresh token was saved and that
  API call also returned HTTP 200 and JSON, without another login.
- The refresh-token value changed. The access-token value remained the same in
  this immediate refresh; the test does not require a distinct access-token string.

The [masked report](../../docs/oauth-live-test-2026-09-28.json) contains status and
timing only. No token values, codes, application credentials or organization data
are published. The local expiry adjustment exercises refresh immediately; it is
not a real one-hour expiry or month-long inactivity test. Other API resources,
registrations and consuming applications' session/storage arrangements need
their own integration checks. Offline tests also cover error handling,
concurrency and API-key compatibility.

- [Xena OAuth setup](https://dev.xena.biz/xena-developer/development/get-started/xena-api-using-oauth)
- [Xena discovery metadata](https://login.xena.biz/.well-known/openid-configuration)
- [OAuth 2.0 refresh](https://www.rfc-editor.org/rfc/rfc6749.html#section-6)
- [PKCE](https://www.rfc-editor.org/rfc/rfc7636.html)

Authorization and token endpoint addresses are fixed to login.xena.biz.
Automatic discovery is not implemented. See README.md for downloading original
document bytes through the authenticated session.
