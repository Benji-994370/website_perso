---
name: visual-test
description: Test the website visually using Playwright browser automation. Use when user wants to verify UI changes, test responsiveness, or create demo videos.
allowed-tools: Bash(*), Read, Write
---

# Visual Test Skill

Use Playwright MCP or Chrome extension to visually test the website.

## When to Use

- After making UI changes
- Before deploying
- To verify responsive design
- To create demo videos/screenshots for PRs

## Prerequisites

### Option 1: Playwright MCP (Recommended)

Playwright MCP should already be configured. If not:

```bash
# Install Playwright
npm init -y
npm install playwright
npx playwright install chromium
```

### Option 2: Claude in Chrome Extension

Use the `mcp__claude-in-chrome__*` tools if the extension is connected.

## Test Workflow

### 1. Start Local Server

```bash
python3 -m http.server 8000
```

### 2. Visual Tests to Run

| Test | What to Check |
|------|---------------|
| **Homepage load** | Hero section renders, animations work |
| **Navigation** | All links scroll to correct sections |
| **Projects** | Cards display correctly, hover effects work |
| **Testimonials** | Carousel scrolls, pauses on hover |
| **Contact** | Links work (email, LinkedIn, WhatsApp) |
| **Mobile view** | Resize to 375px, check responsive layout |
| **Tablet view** | Resize to 768px, check layout transitions |

### 3. Responsive Breakpoints to Test

```javascript
// Viewport sizes to test
const viewports = [
  { width: 375, height: 667, name: 'iPhone SE' },
  { width: 390, height: 844, name: 'iPhone 12' },
  { width: 768, height: 1024, name: 'iPad' },
  { width: 1024, height: 768, name: 'iPad Landscape' },
  { width: 1440, height: 900, name: 'Desktop' },
];
```

### 4. Screenshots for PR

When creating a pull request, capture:
- Before/after screenshots of changed components
- Mobile and desktop views
- Any new features or interactions

## Example Playwright Test Commands

```javascript
// Navigate to site
await page.goto('http://localhost:8000');

// Screenshot full page
await page.screenshot({ path: 'screenshot.png', fullPage: true });

// Test mobile view
await page.setViewportSize({ width: 375, height: 667 });
await page.screenshot({ path: 'mobile.png' });

// Test navigation
await page.click('a[href="#work"]');
await page.waitForTimeout(1000);

// Record video of interaction
// (configured in playwright.config.js)
```

## Common Issues

| Issue | Solution |
|-------|----------|
| Server not running | Start with `python3 -m http.server 8000` |
| Playwright not found | Run `npx playwright install` |
| Screenshots blank | Wait for animations with `waitForTimeout` |
| Mobile menu not working | Check viewport size is set before clicking |
