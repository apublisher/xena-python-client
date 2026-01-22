#!/usr/bin/env python3
"""
Xena API Documentation Explorer

Usage:
    python doc.py                           # List all available packages
    python doc.py partner                   # List all methods in partner package
    python doc.py partner get               # Show details for partner GET method
    python doc.py --url <url>               # Parse and show docs for a specific URL
    python doc.py --refresh                 # Force refresh swagger cache

Examples:
    python doc.py --url "https://my.xena.biz/Api/Fiscal/103145/Partner/123"
"""

import json
import sys
import os
import re
from pathlib import Path
from datetime import datetime, timedelta
from urllib.request import urlopen, Request
from urllib.error import URLError
from urllib.parse import urlparse, parse_qs

# Configuration
SWAGGER_URL = "https://my.xena.biz/api/swagger/docs/v1"
CACHE_FILE = Path(__file__).parent / "docs" / "v1.json"
CACHE_MAX_AGE_DAYS = 10

# ANSI color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def colored(text, color):
    """Add color to text if terminal supports it"""
    if os.getenv('NO_COLOR') or not sys.stdout.isatty():
        return text
    return f"{color}{text}{Colors.END}"

def print_error(message):
    """Print error message"""
    print(colored(f"Error: {message}", Colors.RED), file=sys.stderr)

def print_success(message):
    """Print success message"""
    print(colored(message, Colors.GREEN))

def print_header(text):
    """Print section header"""
    print(colored(f"\n{text}", Colors.BOLD + Colors.BLUE))
    print(colored("=" * len(text), Colors.BLUE))

def print_subheader(text):
    """Print subsection header"""
    print(colored(f"\n{text}:", Colors.CYAN))

def cache_exists():
    """Check if cache file exists"""
    return CACHE_FILE.exists()

def cache_age():
    """Get age of cache file in days"""
    if not cache_exists():
        return float('inf')
    mtime = datetime.fromtimestamp(CACHE_FILE.stat().st_mtime)
    age = datetime.now() - mtime
    return age.days

def is_cache_valid():
    """Check if cache is valid (exists and not too old)"""
    return cache_exists() and cache_age() < CACHE_MAX_AGE_DAYS

def download_swagger():
    """Download swagger spec from API"""
    print(f"Downloading Swagger spec from {SWAGGER_URL}...")
    try:
        req = Request(SWAGGER_URL, headers={'User-Agent': 'XenaDocTool/1.0'})
        with urlopen(req, timeout=30) as response:
            data = response.read()
        
        # Ensure docs directory exists
        CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
        
        # Save to cache
        CACHE_FILE.write_bytes(data)
        print_success(f"✓ Swagger spec cached to {CACHE_FILE}")
        return json.loads(data)
    except URLError as e:
        print_error(f"Failed to download swagger spec: {e}")
        if cache_exists():
            print("Using cached version...")
            return load_swagger()
        sys.exit(1)
    except Exception as e:
        print_error(f"Unexpected error: {e}")
        sys.exit(1)

def load_swagger(force_refresh=False):
    """Load swagger spec from cache or download if needed"""
    if force_refresh or not is_cache_valid():
        if not force_refresh and cache_exists():
            print(f"Cache is {cache_age()} days old (max: {CACHE_MAX_AGE_DAYS} days)")
        return download_swagger()
    
    # Load from cache
    try:
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print_error(f"Failed to load cache: {e}")
        return download_swagger()

def extract_packages(swagger_data):
    """Extract package information from swagger spec"""
    packages = {}
    
    for path, methods in swagger_data.get('paths', {}).items():
        for method, details in methods.items():
            if method.lower() not in ['get', 'post', 'put', 'delete', 'patch']:
                continue
            
            tags = details.get('tags', [])
            if not tags:
                continue
            
            # Parse tag format: "PackageName - ClassName"
            tag = tags[0]
            if ' - ' in tag:
                package_name, class_name = tag.split(' - ', 1)
                package_key = package_name.strip('()').lower().replace(' ', '_')
                
                if package_key not in packages:
                    packages[package_key] = {
                        'name': package_name,
                        'classes': {}
                    }
                
                if class_name not in packages[package_key]['classes']:
                    packages[package_key]['classes'][class_name] = []
                
                operation_id = details.get('operationId', f"{method}_{path}")
                packages[package_key]['classes'][class_name].append({
                    'method': method.upper(),
                    'path': path,
                    'operation_id': operation_id,
                    'summary': details.get('summary', ''),
                    'description': details.get('description', ''),
                    'parameters': details.get('parameters', []),
                    'responses': details.get('responses', {}),
                    'consumes': details.get('consumes', []),
                    'produces': details.get('produces', [])
                })
    
    return packages

def list_packages(packages):
    """List all available packages"""
    print_header("Available Xena API Packages")
    
    sorted_packages = sorted(packages.items())
    for package_key, package_data in sorted_packages:
        class_count = len(package_data['classes'])
        method_count = sum(len(methods) for methods in package_data['classes'].values())
        print(f"  {colored(package_key, Colors.BOLD):<20} "
              f"({class_count} classes, {method_count} methods)")
    
    print(f"\n{colored('Usage:', Colors.YELLOW)} python doc.py <package_name>")
    print(f"{colored('Example:', Colors.YELLOW)} python doc.py partner")

def list_package_methods(package_key, packages):
    """List all methods in a package"""
    if package_key not in packages:
        print_error(f"Package '{package_key}' not found")
        print(f"\nAvailable packages: {', '.join(sorted(packages.keys()))}")
        sys.exit(1)
    
    package = packages[package_key]
    print_header(f"{package['name']} Package")
    
    for class_name, methods in sorted(package['classes'].items()):
        print_subheader(class_name)
        
        for method_info in sorted(methods, key=lambda m: (m['method'], m['path'])):
            method_tag = colored(f"{method_info['method']:<6}", Colors.GREEN)
            path = colored(method_info['path'], Colors.CYAN)
            operation = method_info['operation_id']
            
            print(f"  {method_tag} {path}")
            print(f"         → {operation}")
            if method_info.get('summary'):
                print(f"         {method_info['summary']}")
    
    print(f"\n{colored('Usage:', Colors.YELLOW)} python doc.py {package_key} <method>")
    print(f"{colored('Example:', Colors.YELLOW)} python doc.py {package_key} get")

def show_method_details(package_key, method_filter, packages):
    """Show detailed information for a specific method"""
    if package_key not in packages:
        print_error(f"Package '{package_key}' not found")
        sys.exit(1)
    
    package = packages[package_key]
    method_filter_lower = method_filter.lower()
    
    # Find matching methods
    matches = []
    for class_name, methods in package['classes'].items():
        for method_info in methods:
            if (method_filter_lower in method_info['method'].lower() or
                method_filter_lower in method_info['operation_id'].lower() or
                method_filter_lower in method_info['path'].lower()):
                matches.append((class_name, method_info))
    
    if not matches:
        print_error(f"No methods found matching '{method_filter}'")
        sys.exit(1)
    
    # Show all matches
    for class_name, method_info in matches:
        print_header(f"{method_info['method']} {method_info['path']}")
        
        print(f"\n{colored('Package:', Colors.BOLD)} {package['name']}")
        print(f"{colored('Class:', Colors.BOLD)} {class_name}")
        print(f"{colored('Operation ID:', Colors.BOLD)} {method_info['operation_id']}")
        
        if method_info.get('summary'):
            print(f"{colored('Summary:', Colors.BOLD)} {method_info['summary']}")
        
        if method_info.get('description'):
            print_subheader("Description")
            print(f"  {method_info['description']}")
        
        # Parameters
        if method_info['parameters']:
            print_subheader("Parameters")
            for param in method_info['parameters']:
                param_name = colored(param['name'], Colors.YELLOW)
                param_type = param.get('type', param.get('schema', {}).get('type', 'object'))
                required = colored('required', Colors.RED) if param.get('required') else colored('optional', Colors.GREEN)
                location = param.get('in', 'unknown')
                
                print(f"  • {param_name} ({param_type}) - {required}")
                print(f"    Location: {location}")
                if param.get('description'):
                    print(f"    {param['description']}")
                if param.get('format'):
                    print(f"    Format: {param['format']}")
        
        # Request body
        consumes = method_info.get('consumes', [])
        if consumes:
            print_subheader("Consumes")
            for content_type in consumes:
                print(f"  • {content_type}")
        
        # Response formats
        produces = method_info.get('produces', [])
        if produces:
            print_subheader("Produces")
            for content_type in produces:
                print(f"  • {content_type}")
        
        # Responses
        if method_info['responses']:
            print_subheader("Responses")
            for status_code, response_info in sorted(method_info['responses'].items()):
                status_color = Colors.GREEN if status_code.startswith('2') else Colors.YELLOW
                status = colored(status_code, status_color)
                description = response_info.get('description', 'No description')
                
                print(f"  {status}: {description}")
                
                if 'schema' in response_info:
                    schema = response_info['schema']
                    if '$ref' in schema:
                        ref = schema['$ref'].split('/')[-1]
                        print(f"    Schema: {colored(ref, Colors.CYAN)}")
                    elif 'type' in schema:
                        print(f"    Type: {schema['type']}")
        
        print()  # Blank line between matches

def parse_url_and_show_docs(url, swagger_data):
    """Parse a URL and show documentation for the endpoint"""
    try:
        parsed = urlparse(url)
        path = parsed.path
        query_params = parse_qs(parsed.query)
        
        # Remove /Api prefix if present
        if path.startswith('/Api'):
            path = path[4:]
        
        # Extract fiscalId from path
        fiscal_match = re.match(r'/Fiscal/(\d+)(/.*)', path)
        if not fiscal_match:
            print_error("Could not extract fiscal ID from URL")
            return False
        
        fiscal_id = fiscal_match.group(1)
        rest_path = fiscal_match.group(2)
        
        # Build potential paths by replacing numbers with {id}
        potential_paths = [f"/Api/Fiscal/{{fiscalId}}{rest_path}"]
        
        # Also try replacing numeric segments with {id}
        segments = rest_path.split('/')
        for i, segment in enumerate(segments):
            if segment.isdigit():
                test_segments = segments.copy()
                test_segments[i] = '{id}'
                test_path = '/'.join(test_segments)
                potential_paths.append(f"/Api/Fiscal/{{fiscalId}}{test_path}")
        
        # Find matching path in swagger
        for test_path in potential_paths:
            if test_path in swagger_data.get('paths', {}):
                methods = swagger_data['paths'][test_path]
                http_method = 'get'  # Default for browser URLs
                
                if http_method in methods:
                    method_info = methods[http_method]
                    
                    print_header(f"URL Analysis: {url}")
                    print(f"\n{colored('Detected Path:', Colors.BOLD)} {test_path}")
                    print(f"{colored('HTTP Method:', Colors.BOLD)} {http_method.upper()}")
                    print(f"{colored('Fiscal ID:', Colors.BOLD)} {fiscal_id}")
                    
                    if query_params:
                        print_subheader("Query Parameters in URL")
                        for param_name, param_values in query_params.items():
                            print(f"  • {colored(param_name, Colors.YELLOW)}: {', '.join(param_values)}")
                    
                    # Extract package info
                    tags = method_info.get('tags', [])
                    package_key = None
                    class_name_display = None
                    if tags and ' - ' in tags[0]:
                        package_name, class_name_display = tags[0].split(' - ', 1)
                        package_key = package_name.strip('()').lower().replace(' ', '_')
                        print(f"\n{colored('Package:', Colors.BOLD)} {package_name}")
                        print(f"{colored('Class:', Colors.BOLD)} {class_name_display}")
                        
                        # Show Python usage
                        print_subheader("Python Usage")
                        operation_id = method_info.get('operationId', '')
                        # Convert operation ID to method name (e.g., ApiLedgerTag_GetLedgerGroupList -> get_ledger_group_list)
                        if '_' in operation_id:
                            method_name_part = operation_id.split('_', 1)[1] if '_' in operation_id else operation_id
                            # Convert CamelCase to snake_case
                            method_name = re.sub(r'(?<!^)(?=[A-Z])', '_', method_name_part).lower()
                        else:
                            method_name = operation_id.lower()
                        
                        # Collect all parameters for the method signature
                        param_list = []
                        for param in method_info.get('parameters', []):
                            param_name = param['name']
                            # Convert parameter name to Python style (replace dots with underscores)
                            python_param = param_name.replace('.', '_')
                            if param_name == 'fiscalId':
                                param_list.append(f"{python_param}=<fiscal_id>")
                            elif param.get('required'):
                                param_list.append(f"{python_param}=...")
                            else:
                                param_list.append(f"{python_param}=None")
                        
                        print(f"  from xena.{package_key} import {class_name_display}")
                        print(f"  ")
                        print(f"  client = {class_name_display}()")
                        if len(param_list) <= 2:
                            # Short parameter list - single line
                            params_str = ', '.join(param_list)
                            print(f"  result = client.{method_name}({params_str})")
                        else:
                            # Long parameter list - multiple lines
                            print(f"  result = client.{method_name}(")
                            for param in param_list:
                                print(f"      {param},")
                            print(f"  )")
                    
                    print_header(f"{http_method.upper()} {test_path}")
                    print(f"\n{colored('Operation ID:', Colors.BOLD)} {method_info.get('operationId', 'Unknown')}")
                    
                    if method_info.get('summary'):
                        print(f"{colored('Summary:', Colors.BOLD)} {method_info['summary']}")
                    
                    # Parameters
                    if method_info.get('parameters'):
                        print_subheader("Parameters")
                        for param in method_info['parameters']:
                            param_name = colored(param['name'], Colors.YELLOW)
                            param_type = param.get('type', param.get('schema', {}).get('type', 'object'))
                            required = colored('required', Colors.RED) if param.get('required') else colored('optional', Colors.GREEN)
                            location = param.get('in', 'unknown')
                            
                            # Highlight if parameter was in URL
                            in_url = ""
                            if location == 'query' and param['name'] in query_params:
                                in_url = colored(" ✓ (in URL)", Colors.GREEN)
                            elif location == 'path':
                                in_url = colored(" ✓ (in path)", Colors.GREEN)
                            
                            print(f"  • {param_name} ({param_type}) - {required}{in_url}")
                            print(f"    Location: {location}")
                            if param.get('description'):
                                print(f"    {param['description']}")
                    
                    # Produces
                    if method_info.get('produces'):
                        print_subheader("Produces")
                        for content_type in method_info['produces']:
                            print(f"  • {content_type}")
                    
                    # Responses
                    if method_info.get('responses'):
                        print_subheader("Responses")
                        for status_code, response_info in sorted(method_info['responses'].items()):
                            status_color = Colors.GREEN if status_code.startswith('2') else Colors.YELLOW
                            status = colored(status_code, status_color)
                            description = response_info.get('description', 'No description')
                            print(f"  {status}: {description}")
                            
                            if 'schema' in response_info:
                                schema = response_info['schema']
                                if '$ref' in schema:
                                    ref = schema['$ref'].split('/')[-1]
                                    print(f"    Schema: {colored(ref, Colors.CYAN)}")
                    
                    return True
        
        print_error(f"Could not match URL to any known API endpoint")
        print(f"\nExtracted path: {path}")
        return False
        
    except Exception as e:
        print_error(f"Failed to parse URL: {e}")
        import traceback
        traceback.print_exc()
        return False

def show_help():
    """Show usage information"""
    print(colored(__doc__, Colors.CYAN))

def main():
    """Main entry point"""
    args = sys.argv[1:]
    
    # Handle flags
    force_refresh = '--refresh' in args or '-r' in args
    if force_refresh:
        args = [a for a in args if a not in ['--refresh', '-r']]
    
    show_help_flag = '--help' in args or '-h' in args
    if show_help_flag:
        show_help()
        return
    
    # Handle URL parsing
    if '--url' in args:
        url_idx = args.index('--url')
        if url_idx + 1 < len(args):
            url = args[url_idx + 1]
            swagger_data = load_swagger(force_refresh=force_refresh)
            parse_url_and_show_docs(url, swagger_data)
            return
        else:
            print_error("--url flag requires a URL argument")
            sys.exit(1)
    
    # Load swagger data
    try:
        swagger_data = load_swagger(force_refresh=force_refresh)
    except KeyboardInterrupt:
        print("\nInterrupted by user")
        sys.exit(1)
    
    # Extract package information
    packages = extract_packages(swagger_data)
    
    if not packages:
        print_error("No packages found in swagger spec")
        sys.exit(1)
    
    # Route based on arguments
    if len(args) == 0:
        list_packages(packages)
    elif len(args) == 1:
        list_package_methods(args[0], packages)
    else:
        show_method_details(args[0], args[1], packages)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted by user")
        sys.exit(1)
    except Exception as e:
        print_error(f"Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
