# Changelog

## 0.3.0 — 2026-09-28

- Add opt-in `XenaClient(oauth=OAuthTokenManager(...))` with on-demand refresh, application-supplied token load/save callbacks and serialized refresh/persistence. Save replacement refresh tokens before API calls; preserve an existing refresh token if the response omits one.
- Add `XenaOAuth.refresh_tokens`, form_post callback parsing, configurable code/hybrid response types and server-side pending-login export/restore. Request consent with offline_access.
- Add `OAuthLoginRequired` and `OAuthStorageError`. Never replay API operations, automatically retry token HTTP requests or fall back to API keys. Retain a pending token update in the manager when storage fails.
- Preserve API-key construction/configuration, manual access_token usage and generated domain APIs. No new runtime dependencies; only the unified xena-client package advances to 0.3.0.
- Verify the Python client against live Xena on 2026-09-28: code exchange through the existing registered callback and HTTP 307 relay, persistent loading in a new process, automatic refresh with replacement refresh-token storage, and HTTP 200 from GET /Api/User/FiscalSetup before and after refresh. Local expiry was advanced for the test; long-term refresh validity is not established.

## 0.2.0 — 2026-09-09

- Add experimental OAuthConfig/XenaOAuth helpers for configurable redirect URI, Authorization Code with S256 PKCE, state checking and a single-use callback exchange. Live Xena compatibility is unconfirmed. Refresh-token issuance is optional; automatic refresh remains out of scope.

- Add existing OAuth bearer-token support to XenaClient through access_token and set_access_token. Refresh tokens are optional at the application level; this client never refreshes or replays rejected requests automatically.
- Preserve API-key authentication, reject ambiguous credentials and document original-byte downloads through the shared authenticated session.

- Update xena-client, xena-order, xena-finance and xena-subscription to 0.2.0. Other domain packages remain at 0.1.0.
- Add six OrderTaskBudgetPost operations, OrderTaskLine/DeleteLines and ResourcePost/Totals to xena-order.
- Add PaymentExportDraft/{contextId}/ByPaymentIds to xena-finance.
- Add optional exclude_article_groups_without_number to LedgerAccount GET and is_active to Subscription GET. New arguments follow all existing positional arguments.
- Preserve existing method names and Document/Inbox.query_string for compatibility; the latter is absent from current Swagger but its runtime support is unverified.
- Track the public Swagger snapshot used for this update under specs/. Source: https://my.xena.biz/api/swagger/docs/v1. SHA-256: 948a617516198ce453cb5e4a00326ea3d6837d22c1ea6a7ab70dc9e19964c9c6.

This update aligns endpoint and parameter coverage. It does not assert that all historical JSON schemas or server behavior are unchanged. HTTPS remains the default.
