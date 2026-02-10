#!/bin/bash
# Pre-commit validation hook
# Run this script before committing to ensure code quality
#
# Usage:
#   bash tools/pre-commit-check.sh
#
# To install as a git hook:
#   ln -s ../../tools/pre-commit-check.sh .git/hooks/pre-commit
#   chmod +x .git/hooks/pre-commit

set -e  # Exit on first error

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$( cd "$SCRIPT_DIR/.." && pwd )"

echo ""
echo "🔍 Running pre-commit validation checks..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Change to project root
cd "$PROJECT_ROOT"

# Track if any checks fail
CHECKS_FAILED=0

# Check 1: Validate main HTML file
echo "📄 Validating index.html..."
if python3 tools/validate_html.py index.html; then
    echo "✓ index.html passed validation"
else
    echo "✗ index.html validation failed"
    CHECKS_FAILED=1
fi
echo ""

# Check 2: Validate project detail pages
echo "📄 Validating project pages..."
for file in projects/*.html; do
    if [ -f "$file" ]; then
        echo "  Checking $(basename $file)..."
        if python3 tools/validate_html.py "$file" > /dev/null 2>&1; then
            echo "  ✓ $(basename $file) passed"
        else
            echo "  ✗ $(basename $file) failed validation"
            CHECKS_FAILED=1
        fi
    fi
done
echo ""

# Check 3: Check for broken links (soft check - many sites block automated requests)
echo "🔗 Checking links..."
if python3 tools/check_links.py index.html > /dev/null 2>&1; then
    echo "✓ All links valid"
else
    echo "⚠️  Warning: Some external links may be inaccessible (LinkedIn, Google Fonts often block automated checks)"
    echo "  Manual verification recommended for external links"
fi
echo ""

# Check 4: Check for large unoptimized images
echo "🖼️  Checking for large images..."
LARGE_IMAGES=$(find images -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" \) -size +500k 2>/dev/null || true)
if [ -n "$LARGE_IMAGES" ]; then
    echo "⚠️  Warning: Found large images (>500KB):"
    echo "$LARGE_IMAGES" | while read img; do
        SIZE=$(du -h "$img" | cut -f1)
        echo "    - $img ($SIZE)"
    done
    echo ""
    echo "  Consider optimizing with:"
    echo "  python tools/optimize_images.py <image_path> --max-width 1920"
    echo ""
else
    echo "✓ No large images found"
fi
echo ""

# Summary
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if [ $CHECKS_FAILED -eq 0 ]; then
    echo "✅ All checks passed! Safe to commit."
    echo ""
    exit 0
else
    echo "❌ Some checks failed. Please fix issues before committing."
    echo ""
    exit 1
fi
