#!/usr/bin/env python3
"""
HTML Validator Tool

Validates HTML files for:
- Basic HTML5 structure
- Accessibility issues (missing alt tags, heading hierarchy)
- Common problems

Usage:
    python tools/validate_html.py index.html
    python tools/validate_html.py path/to/file.html --verbose
"""

import argparse
import re
import sys
from pathlib import Path
from html.parser import HTMLParser


class HTMLValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.errors = []
        self.warnings = []
        self.info = []

        # Tracking
        self.has_doctype = False
        self.has_html = False
        self.has_head = False
        self.has_title = False
        self.has_body = False
        self.has_lang = False
        self.has_charset = False
        self.has_viewport = False

        self.images = []
        self.links = []
        self.headings = []
        self.current_line = 1

    def handle_decl(self, decl):
        if decl.lower().startswith('doctype'):
            self.has_doctype = True

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        # Track structural elements
        if tag == 'html':
            self.has_html = True
            if 'lang' in attrs_dict:
                self.has_lang = True
            else:
                self.warnings.append("Missing 'lang' attribute on <html> tag")

        elif tag == 'head':
            self.has_head = True

        elif tag == 'title':
            self.has_title = True

        elif tag == 'body':
            self.has_body = True

        elif tag == 'meta':
            if attrs_dict.get('charset'):
                self.has_charset = True
            if attrs_dict.get('name') == 'viewport':
                self.has_viewport = True

        # Check images
        elif tag == 'img':
            src = attrs_dict.get('src', '')
            alt = attrs_dict.get('alt')
            self.images.append({'src': src, 'alt': alt})

            if alt is None:
                self.errors.append(f"Image missing alt attribute: {src}")
            elif alt == '':
                self.info.append(f"Image has empty alt (decorative): {src}")

        # Check links
        elif tag == 'a':
            href = attrs_dict.get('href', '')
            self.links.append(href)

            if not href:
                self.warnings.append("Link with empty or missing href")
            elif href.startswith('http') and 'target' not in attrs_dict:
                self.info.append(f"External link without target='_blank': {href[:50]}")

        # Track headings
        elif tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(tag[1])
            self.headings.append(level)

    def validate(self):
        """Run all validation checks and return results."""

        # Structure checks
        if not self.has_doctype:
            self.errors.append("Missing DOCTYPE declaration")
        if not self.has_html:
            self.errors.append("Missing <html> tag")
        if not self.has_head:
            self.errors.append("Missing <head> tag")
        if not self.has_title:
            self.errors.append("Missing <title> tag")
        if not self.has_body:
            self.errors.append("Missing <body> tag")
        if not self.has_charset:
            self.warnings.append("Missing charset meta tag")
        if not self.has_viewport:
            self.warnings.append("Missing viewport meta tag (important for mobile)")

        # Check heading hierarchy
        if self.headings:
            if self.headings[0] != 1:
                self.warnings.append(f"First heading is h{self.headings[0]}, should be h1")

            for i in range(1, len(self.headings)):
                if self.headings[i] > self.headings[i-1] + 1:
                    self.warnings.append(
                        f"Heading level skipped: h{self.headings[i-1]} to h{self.headings[i]}"
                    )
        else:
            self.warnings.append("No headings found in document")

        return {
            'errors': self.errors,
            'warnings': self.warnings,
            'info': self.info,
            'stats': {
                'images': len(self.images),
                'links': len(self.links),
                'headings': len(self.headings)
            }
        }


def validate_file(filepath: Path, verbose: bool = False) -> dict:
    """Validate an HTML file."""

    if not filepath.exists():
        return {'errors': [f"File not found: {filepath}"], 'warnings': [], 'info': [], 'stats': {}}

    content = filepath.read_text(encoding='utf-8')

    validator = HTMLValidator()
    try:
        validator.feed(content)
    except Exception as e:
        return {'errors': [f"Parse error: {e}"], 'warnings': [], 'info': [], 'stats': {}}

    return validator.validate()


def print_results(results: dict, verbose: bool = False):
    """Print validation results to console."""

    errors = results['errors']
    warnings = results['warnings']
    info = results['info']
    stats = results['stats']

    # Print errors
    if errors:
        print(f"\n{'='*50}")
        print(f"ERRORS ({len(errors)})")
        print('='*50)
        for error in errors:
            print(f"  [ERROR] {error}")

    # Print warnings
    if warnings:
        print(f"\n{'='*50}")
        print(f"WARNINGS ({len(warnings)})")
        print('='*50)
        for warning in warnings:
            print(f"  [WARN]  {warning}")

    # Print info (only in verbose mode)
    if verbose and info:
        print(f"\n{'='*50}")
        print(f"INFO ({len(info)})")
        print('='*50)
        for item in info:
            print(f"  [INFO]  {item}")

    # Print stats
    print(f"\n{'='*50}")
    print("STATS")
    print('='*50)
    print(f"  Images: {stats.get('images', 0)}")
    print(f"  Links:  {stats.get('links', 0)}")
    print(f"  Headings: {stats.get('headings', 0)}")

    # Summary
    print(f"\n{'='*50}")
    if not errors:
        if warnings:
            print(f"PASSED with {len(warnings)} warning(s)")
        else:
            print("PASSED - No issues found")
    else:
        print(f"FAILED - {len(errors)} error(s), {len(warnings)} warning(s)")
    print('='*50)


def main():
    parser = argparse.ArgumentParser(
        description='Validate HTML files for structure and accessibility'
    )
    parser.add_argument('file', type=Path, help='HTML file to validate')
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='Show detailed output including info messages')

    args = parser.parse_args()

    print(f"\nValidating: {args.file}")

    results = validate_file(args.file, args.verbose)
    print_results(results, args.verbose)

    # Exit with error code if there are errors
    sys.exit(1 if results['errors'] else 0)


if __name__ == '__main__':
    main()
