#!/usr/bin/env python3
"""
Link Checker Tool

Validates all links in HTML files.

Usage:
    python tools/check_links.py index.html
    python tools/check_links.py index.html --external-only
    python tools/check_links.py index.html --timeout 10

Requirements (optional, for external link checking):
    pip install requests
"""

import argparse
import re
import sys
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, urljoin

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False


class LinkExtractor(HTMLParser):
    """Extract all links from HTML."""

    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        if tag == 'a' and 'href' in attrs_dict:
            self.links.append({
                'type': 'anchor',
                'url': attrs_dict['href'],
                'target': attrs_dict.get('target', '')
            })
        elif tag == 'img' and 'src' in attrs_dict:
            self.links.append({
                'type': 'image',
                'url': attrs_dict['src']
            })
        elif tag == 'link' and 'href' in attrs_dict:
            # Skip preconnect and dns-prefetch hints (not navigable resources)
            rel = attrs_dict.get('rel', '')
            if rel in ('preconnect', 'dns-prefetch'):
                return
            self.links.append({
                'type': 'link',
                'url': attrs_dict['href']
            })
        elif tag == 'script' and 'src' in attrs_dict:
            self.links.append({
                'type': 'script',
                'url': attrs_dict['src']
            })


def extract_links(filepath: Path) -> list:
    """Extract all links from an HTML file."""
    content = filepath.read_text(encoding='utf-8')
    extractor = LinkExtractor()
    extractor.feed(content)
    return extractor.links


def categorize_link(url: str) -> str:
    """Categorize a link as internal, external, anchor, mailto, tel, or other."""
    if not url:
        return 'empty'
    if url.startswith('#'):
        return 'anchor'
    if url.startswith('data:'):
        return 'data'
    if url.startswith('mailto:'):
        return 'mailto'
    if url.startswith('tel:'):
        return 'tel'
    if url.startswith('javascript:'):
        return 'javascript'
    if url.startswith(('http://', 'https://', '//')):
        return 'external'
    return 'internal'


def check_internal_link(url: str, base_path: Path) -> dict:
    """Check if an internal link/file exists."""
    # Handle relative paths
    if url.startswith('/'):
        # Absolute path from root - would need server context
        # For local files, treat as relative
        url = url[1:]

    # Remove query string and fragment
    url = url.split('?')[0].split('#')[0]

    if not url:
        return {'status': 'ok', 'message': 'Same page reference'}

    target_path = base_path.parent / url

    if target_path.exists():
        return {'status': 'ok', 'message': 'File exists'}
    else:
        return {'status': 'error', 'message': f'File not found: {url}'}


def check_external_link(url: str, timeout: int = 5) -> dict:
    """Check if an external link is reachable."""
    if not REQUESTS_AVAILABLE:
        return {'status': 'skipped', 'message': 'requests library not installed'}

    # Normalize URL
    if url.startswith('//'):
        url = 'https:' + url

    try:
        response = requests.head(
            url,
            timeout=timeout,
            allow_redirects=True,
            headers={'User-Agent': 'Mozilla/5.0 (Link Checker)'}
        )

        if response.status_code < 400:
            return {'status': 'ok', 'message': f'HTTP {response.status_code}'}
        elif response.status_code in (403, 405):
            # Many sites block automated HEAD requests — treat as warning
            return {'status': 'warning', 'message': f'HTTP {response.status_code} (likely bot protection)'}
        else:
            return {'status': 'error', 'message': f'HTTP {response.status_code}'}

    except requests.Timeout:
        return {'status': 'warning', 'message': 'Timeout'}
    except requests.RequestException as e:
        return {'status': 'error', 'message': str(e)[:50]}


def check_anchor(anchor: str, content: str) -> dict:
    """Check if an anchor target exists in the document."""
    anchor_id = anchor[1:]  # Remove # prefix

    # Look for id="anchor" or name="anchor"
    if re.search(rf'id=["\']?{re.escape(anchor_id)}["\']?', content):
        return {'status': 'ok', 'message': 'Anchor found'}
    if re.search(rf'name=["\']?{re.escape(anchor_id)}["\']?', content):
        return {'status': 'ok', 'message': 'Anchor found (name attribute)'}

    return {'status': 'error', 'message': f'Anchor not found: {anchor_id}'}


def check_all_links(
    filepath: Path,
    check_external: bool = True,
    timeout: int = 5
) -> dict:
    """Check all links in an HTML file."""

    content = filepath.read_text(encoding='utf-8')
    links = extract_links(filepath)

    results = {
        'total': len(links),
        'ok': [],
        'errors': [],
        'warnings': [],
        'skipped': []
    }

    seen = set()  # Track unique URLs

    for link in links:
        url = link['url']

        # Skip duplicates
        if url in seen:
            continue
        seen.add(url)

        category = categorize_link(url)
        result = {'url': url, 'type': link['type'], 'category': category}

        if category == 'empty':
            result['status'] = 'warning'
            result['message'] = 'Empty URL'
            results['warnings'].append(result)

        elif category == 'anchor':
            check = check_anchor(url, content)
            result.update(check)
            if check['status'] == 'ok':
                results['ok'].append(result)
            else:
                results['errors'].append(result)

        elif category == 'mailto' or category == 'tel':
            result['status'] = 'ok'
            result['message'] = f'{category.capitalize()} link'
            results['ok'].append(result)

        elif category == 'javascript' or category == 'data':
            result['status'] = 'skipped'
            result['message'] = f'{category.capitalize()} URI'
            results['skipped'].append(result)

        elif category == 'internal':
            check = check_internal_link(url, filepath)
            result.update(check)
            if check['status'] == 'ok':
                results['ok'].append(result)
            else:
                results['errors'].append(result)

        elif category == 'external':
            if check_external:
                check = check_external_link(url, timeout)
                result.update(check)
                if check['status'] == 'ok':
                    results['ok'].append(result)
                elif check['status'] == 'warning':
                    results['warnings'].append(result)
                elif check['status'] == 'skipped':
                    results['skipped'].append(result)
                else:
                    results['errors'].append(result)
            else:
                result['status'] = 'skipped'
                result['message'] = 'External check disabled'
                results['skipped'].append(result)

    return results


def print_results(results: dict, verbose: bool = False):
    """Print link check results."""

    print(f"\n{'='*60}")
    print("LINK CHECK RESULTS")
    print('='*60)

    # Errors
    if results['errors']:
        print(f"\nERRORS ({len(results['errors'])})")
        print('-'*60)
        for item in results['errors']:
            print(f"  [ERROR] {item['url'][:50]}")
            print(f"          {item['message']}")

    # Warnings
    if results['warnings']:
        print(f"\nWARNINGS ({len(results['warnings'])})")
        print('-'*60)
        for item in results['warnings']:
            print(f"  [WARN]  {item['url'][:50]}")
            print(f"          {item['message']}")

    # OK links (only in verbose mode)
    if verbose and results['ok']:
        print(f"\nOK ({len(results['ok'])})")
        print('-'*60)
        for item in results['ok']:
            print(f"  [OK]    {item['url'][:50]}")

    # Skipped
    if results['skipped']:
        print(f"\nSKIPPED ({len(results['skipped'])})")
        print('-'*60)
        for item in results['skipped']:
            print(f"  [SKIP]  {item['url'][:50]} - {item['message']}")

    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print('='*60)
    print(f"  Total links: {results['total']}")
    print(f"  Unique checked: {len(results['ok']) + len(results['errors']) + len(results['warnings'])}")
    print(f"  OK: {len(results['ok'])}")
    print(f"  Errors: {len(results['errors'])}")
    print(f"  Warnings: {len(results['warnings'])}")
    print(f"  Skipped: {len(results['skipped'])}")

    if not results['errors']:
        print(f"\n  STATUS: PASSED")
    else:
        print(f"\n  STATUS: FAILED")
    print('='*60)


def main():
    parser = argparse.ArgumentParser(
        description='Check all links in an HTML file'
    )
    parser.add_argument('file', type=Path, help='HTML file to check')
    parser.add_argument('--no-external', action='store_true',
                       help='Skip external link checks')
    parser.add_argument('--external-only', action='store_true',
                       help='Only check external links')
    parser.add_argument('--timeout', '-t', type=int, default=5,
                       help='Timeout for external requests (default: 5s)')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Show all links including OK ones')

    args = parser.parse_args()

    if not args.file.exists():
        print(f"ERROR: File not found: {args.file}")
        sys.exit(1)

    print(f"\nChecking links in: {args.file}")

    if not REQUESTS_AVAILABLE and not args.no_external:
        print("\nNote: 'requests' library not installed.")
        print("External links will be skipped.")
        print("Install with: pip install requests")

    results = check_all_links(
        args.file,
        check_external=not args.no_external,
        timeout=args.timeout
    )

    print_results(results, args.verbose)

    # Exit with error code if there are errors
    sys.exit(1 if results['errors'] else 0)


if __name__ == '__main__':
    main()
