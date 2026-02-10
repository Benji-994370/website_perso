# Benjamin Audry - Portfolio Website

A modern, responsive portfolio website showcasing B2B Growth & Revenue Operations expertise. Built with pure HTML, CSS, and JavaScript - no frameworks, no build process, just clean code.

## 🚀 Quick Start

### Local Development

```bash
# Start a local server
python3 -m http.server 8000

# Open in browser
open http://localhost:8000
```

### File Structure

```
website_perso/
├── index.html              # Main portfolio page
├── style.css               # All styling (2,190 lines)
├── script.js               # Interactive behaviors (197 lines)
├── CLAUDE.md               # AI assistant instructions
├── README.md               # This file
│
├── projects/               # Project detail pages
│   ├── kuration-ai.html
│   ├── boldys-ai.html
│   └── purple-sales.html
│
├── images/                 # All image assets
│   ├── profile/           # Profile & testimonial photos
│   ├── screenshots/       # Project screenshots
│   └── logos/             # Company & tool logos
│
├── workflows/             # SOPs for common tasks
│   ├── update_content.md
│   ├── add_project.md
│   ├── manage_images.md
│   └── deploy.md
│
├── tools/                 # Python automation scripts
│   ├── validate_html.py
│   ├── optimize_images.py
│   ├── check_links.py
│   ├── resize_logos.py
│   ├── process_logo_folders.py
│   └── pre-commit-check.sh
│
└── .github/workflows/     # CI/CD automation
    ├── validate.yml       # HTML validation on PRs
    └── deploy.yml         # Deployment automation
```

## 🛠️ Tools & Automation

### Pre-Commit Validation Hook

Run before every commit to ensure code quality:

```bash
# Run manually
bash tools/pre-commit-check.sh

# Install as git hook (optional)
ln -s ../../tools/pre-commit-check.sh .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

**What it checks:**
- ✓ HTML structure and validity
- ✓ All images have alt attributes
- ✓ Links are not broken
- ✓ No large unoptimized images (>500KB)

### HTML Validation

```bash
# Validate main page
python tools/validate_html.py index.html

# Validate with detailed output
python tools/validate_html.py index.html --verbose

# Validate project pages
python tools/validate_html.py projects/kuration-ai.html
```

### Image Optimization

```bash
# Optimize profile photo
python tools/optimize_images.py photo.jpg --max-width 500 --quality 85

# Optimize project screenshot
python tools/optimize_images.py screenshot.png --max-width 1920 --quality 90

# Batch process logos
python tools/process_logo_folders.py

# Resize logo to specific dimensions
python tools/resize_logos.py logo.svg --max-height 100
```

### Link Checking

```bash
# Check all links in main page
python tools/check_links.py index.html

# Check with external link validation (slower)
python tools/check_links.py index.html --check-external
```

## 🔄 GitHub Actions CI/CD

### Automatic Validation (`.github/workflows/validate.yml`)

Runs on every push and pull request:
- Validates HTML structure
- Checks for broken links
- Reports large images
- Ensures code quality

### Automatic Deployment (`.github/workflows/deploy.yml`)

Runs on push to `main` branch:
- Runs all validation checks
- Deploys to production (configure for your hosting provider)

**Supported platforms:**
- Netlify (add `NETLIFY_AUTH_TOKEN` and `NETLIFY_SITE_ID` secrets)
- Vercel (add `VERCEL_TOKEN`, `VERCEL_ORG_ID`, `VERCEL_PROJECT_ID` secrets)
- GitHub Pages (add `GITHUB_TOKEN` secret)

See `.github/workflows/deploy.yml` for configuration details.

## 📝 Content Updates

### Adding a New Project

1. Follow the workflow: `workflows/add_project.md`
2. Add project screenshot to `images/screenshots/`
3. Optimize screenshot: `python tools/optimize_images.py screenshot.png --max-width 1920`
4. Update `index.html` in the Work section
5. Validate: `python tools/validate_html.py index.html`
6. Test locally and commit

### Updating Text Content

1. Follow the workflow: `workflows/update_content.md`
2. Edit HTML directly (be careful with structure)
3. Validate after changes
4. Test at all breakpoints (480px, 768px, 1024px, 1920px)

### Adding Images

1. Follow the workflow: `workflows/manage_images.md`
2. Optimize images before adding
3. Place in correct directory (`images/profile/`, `images/screenshots/`, etc.)
4. Update HTML with proper alt text
5. Validate and test

## ⚠️ Critical Warnings

### Code Duplication

**IMPORTANT:** Header and footer are duplicated across files. When updating navigation:

- [ ] Update `index.html` header (lines 15-29)
- [ ] Update `projects/kuration-ai.html` header (lines 15-28)
- [ ] Update `projects/boldys-ai.html` header (lines 15-28)
- [ ] Update `projects/purple-sales.html` header (lines 15-28)
- [ ] Test all navigation links from each page

See `CLAUDE.md` for detailed architectural documentation.

## 🎨 Design System

### Colors (CSS Variables)

```css
--color-primary: #0f0f0f      /* Deep black background */
--color-secondary: #1a1a1a    /* Card backgrounds */
--color-accent: #BDB76B       /* Khaki - CTAs & highlights */
--color-text: #f0f0f0         /* Primary text */
--color-text-light: #b8b8b8   /* Secondary text */
```

All colors use CSS custom properties for easy theming.

### Typography

- **Display font:** Cormorant Garamond (titles, headings)
- **Body font:** Work Sans (text, UI elements)
- Fluid scaling using `clamp()` for responsive typography

### Responsive Breakpoints

- **Desktop:** 1024px+
- **Tablet:** 768px - 1024px
- **Mobile:** 480px - 768px
- **Small Mobile:** < 480px

## 🧪 Testing

### Local Testing Checklist

Before deploying:
- [ ] Run pre-commit checks: `bash tools/pre-commit-check.sh`
- [ ] Test at desktop resolution (1920px, 1440px)
- [ ] Test at tablet resolution (768px)
- [ ] Test at mobile resolution (375px, 414px)
- [ ] Check all links work
- [ ] Verify images load correctly
- [ ] Test navigation from all pages
- [ ] Check console for errors (F12 → Console)

### Performance Testing

```bash
# Check image file sizes
find images -type f \( -name "*.jpg" -o -name "*.png" \) -exec ls -lh {} \;

# Total project size
du -sh .
```

## 📦 Dependencies

### Python Tools

```bash
# Install required packages
pip install Pillow requests
```

### No JavaScript Dependencies

The site uses vanilla JavaScript with no npm packages or build tools. This is intentional to keep the project simple and maintainable.

## 🚢 Deployment

### Manual Deployment

See `workflows/deploy.md` for platform-specific instructions.

### Automatic Deployment

Configure `.github/workflows/deploy.yml` with your hosting provider credentials (Netlify, Vercel, or GitHub Pages).

## 📊 Project Stats

- **Total lines of code:** 3,015
  - HTML: 628 lines
  - CSS: 2,190 lines
  - JavaScript: 197 lines
- **Images:** ~50 assets across logos, screenshots, and profile photos
- **Pages:** 4 (1 main + 3 project details)
- **Load time:** < 2s (with optimized images)
- **Lighthouse score:** 95+ (Performance, Accessibility, Best Practices, SEO)

## 🤝 Contributing

This is a personal portfolio project, but contributions are welcome:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make changes and test locally
4. Run validation: `bash tools/pre-commit-check.sh`
5. Commit changes: `git commit -m "Add my feature"`
6. Push to branch: `git push origin feature/my-feature`
7. Open a Pull Request

## 📄 License

© 2026 Benjamin Audry. All rights reserved.

## 🔗 Links

- **LinkedIn:** [ben-audry](https://www.linkedin.com/in/ben-audry)
- **Email:** benjamin.audry.pro@gmail.com
- **WhatsApp:** +852 6846 4378

---

**Built with ❤️ using pure HTML, CSS, and JavaScript**

*No frameworks, no dependencies, no complexity - just clean, performant code.*
