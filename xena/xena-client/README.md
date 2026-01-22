# xena-client

Unified client for Xena API - provides easy access to all Xena domains.

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
