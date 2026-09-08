# Xena Python API Client

Python client libraries for the Xena accounting system API. Provides easy access to all Xena API domains through standalone packages.

## API update 0.2.0

The unified client also accepts an existing OAuth access token without requiring
refresh support: `XenaClient(access_token=token, fiscal_id=fiscal_id)`.
After another login, use `client.set_access_token(new_token)`. See the
[OAuth and binary download guide](xena/xena-client/README.md#oauth-access-tokens-020).
Login and refresh remain the application's responsibility. The current wrapper
still requires API-key credentials; this change adds OAuth to the client itself.

`xena-client`, `xena-order`, `xena-finance`, and `xena-subscription` are version
0.2.0. Other domain packages remain at 0.1.0. See [CHANGELOG.md](CHANGELOG.md)
for the nine added operations and two optional filters.

To install or upgrade all packages together from a checkout in PowerShell:

```powershell
# Run from the repository root, in your application's Python environment.
$packages = @(Get-ChildItem ./xena -Directory -Filter 'xena-*' | ForEach-Object { $_.FullName })
python -m pip install --upgrade $packages
```

Passing all local packages together lets pip resolve the domain dependencies
without requiring them to be published on PyPI. The wrapper itself does not
need an update to keep using its existing methods.

The source Swagger snapshot is committed under `specs/`. Run offline contract
tests (requires `requests`) from the repository root:

```bash
python -m unittest discover -s tests -v
```

These tests verify endpoint coverage and request construction, not live Xena
behavior. `Document/Inbox.query_string` remains supported for compatibility,
although it is absent from the current Swagger snapshot.

## 📦 Packages

This repository contains 19 Python packages for working with the Xena API:

### Unified Client
- **xena-client** - Unified client that provides access to all domains

### Domain Packages
- **xena-accountant** - Accountant domain API
- **xena-appstore** - AppStore domain API
- **xena-archive** - Archive domain API
- **xena-article** - Article/Product management API
- **xena-bank** - Bank integration API
- **xena-chart** - Chart of accounts API
- **xena-core** - Core functionality API
- **xena-developer** - Developer tools API
- **xena-document** - Document management API
- **xena-finance** - Finance/Accounting API
- **xena-order** - Order processing API
- **xena-partner** - Customer/Supplier management API
- **xena-price** - Price management API
- **xena-project** - Project management API
- **xena-provider** - Provider integration API
- **xena-reporting** - Reporting API
- **xena-scheduling** - Scheduling API
- **xena-subscription** - Subscription management API

## 🚀 Quick Start

### Installation (For Your Projects)

**Option 1: Install unified client (easy, includes all domains)**

```bash
# In your project directory
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install unified client with all domains
pip install git+https://github.com/apublisher/xena-python-client.git#subdirectory=xena/xena-client
```

**Option 2: Install only specific packages (if you only need a few)**

```bash
# Install individual packages
pip install git+https://github.com/apublisher/xena-python-client.git#subdirectory=xena/xena-partner
pip install git+https://github.com/apublisher/xena-python-client.git#subdirectory=xena/xena-order
```

**Requirements:** Git must be installed on your system for pip to download from GitHub.

**Authentication (Private Repository):**
- **SSH:** Set up your SSH key with GitHub (recommended)
- **Token:** `pip install git+https://<token>@github.com/apublisher/xena-python-client.git#subdirectory=xena/xena-client`

**Note:** This copies the packages into your virtual environment. No need to keep the repository around.

### Configuration

Create a `config.json` file:
```json
{
  "api_key": "your-api-key-here",
  "fiscal_id": "your-fiscal-id"
}
```

### Usage

**With unified client:**

```python
from xena_client import XenaClient

# Initialize (loads config.json automatically)
client = XenaClient()

# Access any domain API
partners = client.partner.api_partner__get_get__api__fiscal_fiscal_id__partner(
    fiscal_id=client.fiscal_id,
    list_options_page_size=10
)

print(f"Found {partners['Count']} partners")
for partner in partners['Entities']:
    print(f"- {partner['Name']}")
```

**With individual packages:**

```python
from xena_partner import PartnerApi
import requests
import json

# Load config
with open('config.json') as f:
    config = json.load(f)

# Create authenticated session
session = requests.Session()
session.headers['XenaAPIKey'] = config['api_key']

# Use the API
partner_api = PartnerApi(base_url="https://my.xena.biz", session=session)
partners = partner_api.api_partner__get_get__api__fiscal_fiscal_id__partner(
    fiscal_id=config['fiscal_id'],
    list_options_page_size=10
)

print(f"Found {partners['Count']} partners")
```

## 📖 Features

- ✅ **Modular Design** - Install only the packages you need
- ✅ **Automatic Authentication** - API key configured once, used everywhere
- ✅ **Type Hints** - Full type annotations for better IDE support
- ✅ **Simple Configuration** - Just create config.json
- ✅ **All Xena Domains** - Complete coverage of Xena API
- ✅ **Session Management** - Efficient connection pooling

## 🔧 Development

### Modifying the Packages (Editable Mode)

Use this setup **only** when you want to modify the xena-python-client package code itself:

```bash
# Clone the repository
git clone https://github.com/apublisher/xena-python-client.git
cd xena-python-client/xena

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install packages in editable mode (-e flag)
pip install -e xena-client -e xena-partner -e xena-order
# ... (install other packages as needed)
```

**What is `-e` (editable mode)?**
- Creates a **link** to your source code (doesn't copy files)
- Changes to the package code are immediately active
- **Do NOT delete** the repository - packages need it!
- Use this when working on the package code itself, not when using packages in other projects

**Workflow:**
1. Make changes to the package code
2. Test immediately (no reinstall needed)
3. Commit and push to GitHub
4. Other projects get updates with `pip install --upgrade git+...`

### Testing

```bash
# Create config.json with your credentials
# Run the test client
python test_client.py
```

## 📝 Documentation

Each package includes:
- Auto-generated API methods from Xena API
- Type hints for all parameters
- Docstrings with endpoint information

### Finding Methods

Use your IDE's autocomplete or search the package files:
```python
# List all methods
dir(client.partner)

# Find methods containing 'get'
[m for m in dir(client.partner) if 'get' in m.lower()]
```

## 🔑 Authentication

The packages use the `XenaAPIKey` header for authentication. Configure your API key in `config.json` or pass it directly:

```python
client = XenaClient(api_key="your-key", fiscal_id="your-fiscal-id")
```

## 📋 Requirements

- Python 3.8+
- requests >= 2.25.0

## 🤝 Contributing

Contributions are welcome! This is an auto-generated client library based on the Xena API.

## 📄 License

MIT License - see LICENSE file for details

## 🔗 Resources

- [Xena Website](https://xena.biz)
- [Xena API Documentation](https://my.xena.biz)

## ⚠️ Note

These packages are auto-generated from the Xena API. The base URL is hardcoded to `https://my.xena.biz`.
