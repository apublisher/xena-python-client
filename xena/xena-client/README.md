# xena-client

Unified client for Xena API - provides easy access to all Xena domains.

## OAuth access tokens (0.2.0)

Use an access token obtained through your application's login flow. A refresh
token, client registration or client secret is not required by this client to
send an already-issued token. Xena still determines the token's permissions.

```python
from xena_client import XenaClient

client = XenaClient(access_token=access_token, fiscal_id=fiscal_id)
# After a new login, or refresh handled by your application:
client.set_access_token(new_access_token)
```

Pass the token without `Bearer `. All domains share the authenticated session.
`fiscal_id` may be omitted for user-level endpoints. API-key authentication
continues to work through `api_key`; do not supply both authentication types.
An explicit credential overrides authentication in config.json. Explicit OAuth
does not implicitly read a default config file; pass config_path if needed.
Config files may alternatively contain `access_token` instead of `api_key`.

The client does not perform interactive login, token exchange, automatic refresh,
expiry prediction, or token persistence. If Xena rejects the token, generated
API methods raise `requests.HTTPError` (inspect `error.response.status_code`).
There is no automatic retry or fallback to an API key. Obtain a new token and
call `set_access_token` before making further calls. Existing domain instances
use the new token. Coordinate token changes with in-flight calls yourself.

### PDF, images and other binary documents

The generated methods return JSON or text. For original file bytes, use the
same authenticated session directly and read `response.content`:

```python
with client.session.get(
    f"{client.BASE_URL}/Api/Blob/User/Download/{int(version_id)}",
    headers={"Accept": "*/*"},
    timeout=60,
) as response:
    response.raise_for_status()
    document_bytes = response.content
```

Use the appropriate fiscal or user download endpoint for your document. This
example uses the user-level version-ID endpoint. Whether API-key access is
accepted on a particular media endpoint must be verified against Xena.

## Installation

```bash
pip install xena-client
```

This will install the main client plus all 18 domain packages.

## Quick Start

### 1. Create config.json

```json
{
  "api_key": "your-api-key-here",
  "fiscal_id": "your-fiscal-id"
}
```

### 2. Use the Client

```python
from xena_client import XenaClient

# Initialize (loads config.json automatically)
client = XenaClient()

# Access any domain API
partners = client.partner.api_partner__get_get__api__fiscal_fiscal_id__partner(
    fiscal_id=client.fiscal_id,
    list_options_page_size=10
)

# All domains available:
# client.partner, client.order, client.finance, client.article
# client.accountant, client.bank, client.chart, client.core
# client.developer, client.document, client.price, client.project
# client.provider, client.reporting, client.scheduling, client.subscription
# client.appstore, client.archive
```

### 3. Alternative: Pass credentials directly

```python
client = XenaClient(
    api_key="your-api-key",
    fiscal_id="your-fiscal-id"
)
```

## Features

- ✓ Automatic authentication with XenaAPIKey header
- ✓ Hardcoded base URL (https://my.xena.biz)
- ✓ Lazy loading of API clients (only loads what you use)
- ✓ Access to all 18 Xena API domains
- ✓ Shared session across all API calls
- ✓ Simple configuration via config.json

## Requirements

- Python 3.8+
- requests>=2.25.0
- All xena-* domain packages

## License

MIT
