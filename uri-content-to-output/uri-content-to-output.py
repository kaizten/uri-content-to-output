#!/usr/bin/env python3
"""
Script to fetch and print the content of a given URI to standard output.
"""

import sys
import argparse
import urllib.request
import urllib.error

def main():
    parser = argparse.ArgumentParser(
        description="Fetch and print the content of a given URI to standard output."
    )
    parser.add_argument(
        "--uri",
        required=True,
        help="The URI to fetch content from (http, https, file, etc.)"
    )
    
    args = parser.parse_args()
    uri = args.uri
    
    try:
        # Fetch the content from the URI
        with urllib.request.urlopen(uri) as response:
            content = response.read().decode('utf-8')
            print(content, end='')
    except urllib.error.URLError as e:
        print(f"Error: Failed to fetch URI '{uri}': {e.reason}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.HTTPError as e:
        print(f"Error: HTTP error {e.code} for URI '{uri}'", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
