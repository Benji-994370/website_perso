---
name: deploy
description: Deploy the portfolio website to production. Use when user wants to publish changes, deploy to hosting, or go live.
allowed-tools: Bash(git *), Bash(npx *), Bash(python *), Read, Write
---

# Deploy Skill

Deploy the portfolio website to production hosting.

## Pre-Deployment Checklist

Before deploying, always run these checks:

```bash
# 1. Validate HTML on all pages
python tools/validate_html.py index.html
python tools/validate_html.py projects/kuration-ai.html
python tools/validate_html.py projects/boldys-ai.html
python tools/validate_html.py projects/purple-sales.html

# 2. Check all links
python tools/check_links.py index.html

# 3. Test locally
python3 -m http.server 8000
# Then manually verify at http://localhost:8000
```

## Deployment Options

### Option 1: Netlify (Recommended)

```bash
# Install Netlify CLI if needed
npm install -g netlify-cli

# Deploy to draft URL first
npx netlify deploy

# Deploy to production
npx netlify deploy --prod
```

### Option 2: Vercel

```bash
# Install Vercel CLI if needed
npm install -g vercel

# Deploy (will prompt for project setup first time)
npx vercel

# Deploy to production
npx vercel --prod
```

### Option 3: GitHub Pages

1. Push to `main` branch
2. GitHub Actions will auto-deploy (if configured)

```bash
git checkout main
git merge dev
git push origin main
```

## Post-Deployment

1. Verify the live site works
2. Test on mobile device
3. Check all navigation links
4. Verify images load correctly

## Rollback

If something goes wrong:

```bash
# Netlify: Rollback to previous deploy in dashboard
# Or redeploy from a previous commit

git log --oneline -5  # Find the commit to rollback to
git checkout <commit-hash>
npx netlify deploy --prod
```
