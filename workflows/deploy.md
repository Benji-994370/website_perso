# Deploy Website

Deploy the portfolio website to a hosting platform.

## Objective
Make the website publicly accessible on the internet.

## Pre-Deployment Checklist

Run these checks before deploying:

```bash
# 1. Validate HTML
python tools/validate_html.py index.html

# 2. Check all links
python tools/check_links.py index.html

# 3. Preview locally
python3 -m http.server 8000
# Visit http://localhost:8000 and verify everything works
```

**Manual checks:**
- [ ] All content is up to date
- [ ] Contact links are correct
- [ ] Images load properly (or have fallbacks)
- [ ] Site looks good on mobile (test with browser dev tools)
- [ ] No console errors in browser

## Deployment Options

### Option 1: GitHub Pages (Recommended)

**Setup (first time):**

1. Initialize git repository:
   ```bash
   cd "/Users/boldysai/Desktop/Claude Code/website_perso"
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. Create GitHub repository at github.com/new

3. Push to GitHub:
   ```bash
   git remote add origin https://github.com/USERNAME/REPO.git
   git push -u origin main
   ```

4. Enable GitHub Pages:
   - Go to repo Settings > Pages
   - Source: Deploy from branch
   - Branch: main, folder: / (root)
   - Save

**Subsequent deploys:**
```bash
git add .
git commit -m "Update: description of changes"
git push
```

Site URL: `https://USERNAME.github.io/REPO/`

---

### Option 2: Netlify

**Setup (first time):**

1. Go to netlify.com and sign in
2. Click "Add new site" > "Deploy manually"
3. Drag the entire `website_perso` folder to upload

**Subsequent deploys:**
- Drag folder again to update
- Or connect to GitHub for automatic deploys

Site URL: `https://random-name.netlify.app` (customizable)

---

### Option 3: Vercel

**Setup (first time):**

1. Install Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Deploy:
   ```bash
   cd "/Users/boldysai/Desktop/Claude Code/website_perso"
   vercel
   ```

3. Follow prompts to configure

**Subsequent deploys:**
```bash
vercel --prod
```

Site URL: `https://project-name.vercel.app`

---

### Option 4: Custom Domain

After deploying to any platform:

1. Purchase domain (Namecheap, Google Domains, etc.)
2. Add custom domain in hosting platform settings
3. Update DNS records:
   - For GitHub Pages: CNAME record pointing to `USERNAME.github.io`
   - For Netlify/Vercel: Follow their DNS instructions

## Post-Deployment

1. **Test the live site**:
   - Visit the URL
   - Check all pages/sections
   - Test contact links
   - Verify on mobile

2. **Update CLAUDE.md** with:
   - Live URL
   - Hosting platform used

3. **Set up monitoring** (optional):
   - Google Search Console for SEO
   - Simple analytics if needed

## Rollback

If something goes wrong:

**GitHub Pages:**
```bash
git revert HEAD
git push
```

**Netlify/Vercel:**
- Use their dashboard to rollback to previous deploy

## Edge Cases

- **Large files**: Hosting platforms have limits (usually 100MB total for free tiers)
- **CORS issues**: If using external APIs, may need configuration
- **Mixed content**: Ensure all resources use HTTPS
