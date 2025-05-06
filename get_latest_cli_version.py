#!/usr/bin/env python3

import re
import urllib.request

def get_latest_cli_version():
    url = "https://app-updates.agilebits.com/product_history/CLI2"
    
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')
        
    # Look for download URLs which contain the version number
    # Example: https://cache.agilebits.com/dist/1P/op2/pkg/v2.30.3/op_linux_amd64_v2.30.3.zip
    url_pattern = re.compile(r'https://cache\.agilebits\.com/dist/1P/op2/pkg/v(\d+\.\d+\.\d+)/')
    
    # Find all version matches from URLs, excluding beta versions
    matches = url_pattern.findall(html)
    
    # Filter out beta versions if any
    stable_versions = [v for v in matches if '-beta' not in v]
    
    # Return the first match (most recent non-beta version)
    if stable_versions:
        return stable_versions[0]
            
    raise ValueError("No stable version found")

if __name__ == "__main__":
    version = get_latest_cli_version()
    if version:
        print(version)
    else:
        print("Failed to find the latest non-beta version")