# Xena Python API Client

Python client libraries for the Xena accounting system API. Provides easy access to all Xena API domains through standalone packages.

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

### Installation

Install the unified client (includes all domains):
```bash
pip install xena-client
```

Or install only the packages you need:
```bash
pip install xena-partner xena-order xena-finance
```

### Configuration

Create a `config.json` file:
```json
{
  "api_key": "your-api-key-here",
  "fiscal_id": "your-fiscal-id"
}
```

### Usage

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

## 📖 Features

- ✅ **Modular Design** - Install only the packages you need
- ✅ **Automatic Authentication** - API key configured once, used everywhere
- ✅ **Type Hints** - Full type annotations for better IDE support
- ✅ **Simple Configuration** - Just create config.json
- ✅ **All Xena Domains** - Complete coverage of Xena API
- ✅ **Session Management** - Efficient connection pooling

## 🔧 Development

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/xena-python-client.git
cd xena-python-client

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install all packages in editable mode
pip install -e xena-client -e xena-partner -e xena-order
# ... (install other packages as needed)
```

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
