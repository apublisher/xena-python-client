"""
Simple HTTP client to test Xena API communication.

This tests the basic HTTP layer - sending requests and receiving responses.
Then tests the generated API packages.

Configuration:
    Edit config.json with your credentials before running.
"""

import json
import requests
from pathlib import Path
from typing import Optional, Dict, Any

# Import API packages
from xena_partner import PartnerApi
from xena_order import OrderApi


def load_config(config_path: str = 'config.json') -> Dict[str, str]:
    """Load configuration from config.json file."""
    config_file = Path(__file__).parent / config_path
    
    if not config_file.exists():
        print(f"Config file not found: {config_file}")
        print("Creating default config.json - please edit with your credentials")
        default_config = {
            "base_url": "https://my.xena.biz",
            "api_key": "YOUR_API_KEY_HERE",
            "fiscal_id": "YOUR_FISCAL_ID_HERE"
        }
        with open(config_file, 'w') as f:
            json.dump(default_config, f, indent=2)
        return default_config
    
    with open(config_file, 'r') as f:
        config = json.load(f)
    
    return config


class XenaHttpClient:
    """Basic HTTP client for Xena API - handles requests/responses only."""
    
    def __init__(self, base_url: str, api_key: Optional[str] = None) -> None:
        """Initialize the HTTP client."""
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.api_key = api_key
        
        # Set up authentication if API key provided
        if api_key:
            self.session.headers.update({
                'XenaAPIKey': api_key,
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            })
    
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> requests.Response:
        """Send a GET request."""
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, params=params)
        return response
    
    def post(self, endpoint: str, data: Optional[Any] = None, json: Optional[Dict[str, Any]] = None) -> requests.Response:
        """Send a POST request."""
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, data=data, json=json)
        return response
    
    def test_connection(self) -> Optional[requests.Response]:
        """Test basic HTTP connection to the API."""
        print(f"Testing connection to: {self.base_url}")
        try:
            # Just try to connect to the base URL
            response = self.session.get(self.base_url, timeout=10)
            print(f"  Status: {response.status_code}")
            print(f"  Response size: {len(response.content)} bytes")
            return response
        except requests.exceptions.RequestException as e:
            print(f"  Error: {e}")
            return None


def main():
    """Test basic HTTP communication with Xena API."""
    
    print("="*60)
    print("Xena HTTP Client Test")
    print("="*60)
    
    # Load configuration from config.json
    print("\nLoading configuration from config.json...")
    config = load_config()
    
    BASE_URL = config.get('base_url', 'https://my.xena.biz')
    API_KEY = config.get('api_key', '')
    FISCAL_ID = config.get('fiscal_id', '')
    
    # Check if config has been set up
    if API_KEY == 'YOUR_API_KEY_HERE' or not API_KEY:
        print("\n⚠ WARNING: Please edit config.json with your actual credentials!")
        print(f"   Config file location: {Path(__file__).parent / 'config.json'}")
        print("\nExiting...")
        return
    
    print("\nConfiguration loaded:")
    print(f"  Base URL: {BASE_URL}")
    print(f"  API Key: ***{API_KEY[-4:] if len(API_KEY) > 4 else 'Invalid'}")
    print(f"  Fiscal ID: {FISCAL_ID}")
    
    # Create HTTP client
    print("\n" + "="*60)
    print("Step 1: Creating HTTP Client")
    print("="*60)
    
    client = XenaHttpClient(base_url=BASE_URL, api_key=API_KEY)
    print("  ✓ HTTP client created")
    print(f"  ✓ Base URL: {client.base_url}")
    print(f"  ✓ Authentication: Configured with API key")
    
    # Test basic connection
    print("\n" + "="*60)
    print("Step 2: Testing HTTP Connection")
    print("="*60)
    
    response = client.test_connection()
    
    if response:
        print("\n  Connection successful!")
        print(f"  Status Code: {response.status_code}")
        print(f"  Headers received: {dict(list(response.headers.items())[:3])}")
    
    # Test with API packages
    print("\n" + "="*60)
    print("Step 3: Testing API Packages")
    print("="*60)
    
    print("\n  Creating API instances with authenticated session...")
    partner_api = PartnerApi(base_url=BASE_URL, session=client.session)
    order_api = OrderApi(base_url=BASE_URL, session=client.session)
    
    print("  ✓ PartnerApi created")
    print("  ✓ OrderApi created")
    print("\n  These API instances will use the authenticated session")
    print("  with the XenaAPIKey header automatically included in all requests")
    
    # Make a real API call
    print("\n" + "="*60)
    print("Step 4: Testing Real API Call - List Partners")
    print("="*60)
    
    print(f"\n  Calling: partner_api.api_partner__get_get__api__fiscal_fiscal_id__partner()")
    print(f"  Endpoint: GET /Api/Fiscal/{FISCAL_ID}/Partner")
    
    try:
        result = partner_api.api_partner__get_get__api__fiscal_fiscal_id__partner(
            fiscal_id=FISCAL_ID,
            list_options_page_size=5  # Limit to 5 results for testing
        )
        
        print("\n  ✓ API call successful!")
        print(f"  Response type: {type(result)}")
        
        # Display the partner data
        if isinstance(result, dict):
            count = result.get('Count', 0)
            entities = result.get('Entities', [])
            
            print(f"\n  Total partners: {count}")
            print(f"  Partners returned: {len(entities)}")
            
            if entities:
                print("\n  Partner List:")
                print("  " + "="*58)
                for i, partner in enumerate(entities, 1):
                    print(f"\n  Partner {i}:")
                    # Show key fields
                    if isinstance(partner, dict):
                        for key in ['Id', 'Name', 'AccountNumber', 'Email', 'PhoneNumber', 'City']:
                            if key in partner:
                                print(f"    {key}: {partner[key]}")
                print("  " + "="*58)
        elif isinstance(result, list):
            print(f"\n  Number of partners: {len(result)}")
            if len(result) > 0:
                print("\n  Partner List:")
                print("  " + "="*58)
                for i, partner in enumerate(result[:5], 1):  # Show first 5
                    print(f"\n  Partner {i}:")
                    if isinstance(partner, dict):
                        for key, value in list(partner.items())[:6]:
                            print(f"    {key}: {value}")
                print("  " + "="*58)
        else:
            print(f"\n  Response: {str(result)[:500]}")
        
    except requests.exceptions.HTTPError as e:
        print(f"\n  ✗ HTTP Error: {e}")
        print(f"  Status Code: {e.response.status_code}")
        print(f"  Response: {e.response.text[:500]}")
    except Exception as e:
        print(f"\n  ✗ Error: {type(e).__name__}: {e}")
    
    print("\n" + "="*60)
    print("Test Complete!")
    print("="*60)


if __name__ == "__main__":
    main()
