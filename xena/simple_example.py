"""
Simple example using the unified XenaClient.

Just needs config.json with api_key and fiscal_id.
"""

from xena_client import XenaClient

# That's it! Just create the client - it loads config.json automatically
client = XenaClient()

print("Xena Client Ready!")
print(f"Fiscal ID: {client.fiscal_id}")

# List partners
print("\nFetching partners...")
result = client.partner.api_partner__get_get__api__fiscal_fiscal_id__partner(
    fiscal_id=client.fiscal_id,
    list_options_page_size=3
)

print(f"Total partners: {result['Count']}")
print(f"Showing: {len(result['Entities'])} partners\n")

for i, partner in enumerate(result['Entities'], 1):
    print(f"Partner {i}: {partner.get('Name', 'N/A')} (#{partner.get('AccountNumber', 'N/A')})")
