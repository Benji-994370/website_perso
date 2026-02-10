# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal portfolio website for Ben Audry, a B2B Growth & AI Automation specialist. The site is a single-page application built with vanilla HTML, CSS, and JavaScript - no build tools or frameworks required.

**Tech Stack:**
- Pure HTML5, CSS3, and JavaScript (ES6+)
- Google Fonts: Cormorant Garamond (display) and Work Sans (body)
- No dependencies or build process

## WAT Framework

This project uses the WAT (Workflows, Agents, Tools) architecture for organized development.

### Directory Structure
```
website_perso/
├── workflows/     # Markdown SOPs for common tasks
├── tools/         # Python scripts for automation
├── .tmp/          # Temporary processing files (disposable)
└── (website files)
```

### Workflows (SOPs)
Located in `workflows/`:
- `update_content.md` - Update website text in any section
- `add_project.md` - Add a new project card
- `manage_images.md` - Optimize and add images
- `deploy.md` - Deploy to hosting platforms

**How to use:** Open the relevant workflow, follow the steps, and use referenced tools.

### Tools
Located in `tools/`:

```bash
# Validate HTML structure and accessibility
python tools/validate_html.py index.html

# Optimize images for web
python tools/optimize_images.py image.jpg --max-width 800

# Check all links in the site
python tools/check_links.py index.html
```

**Dependencies:**
- `validate_html.py` - No dependencies (uses stdlib)
- `optimize_images.py` - Requires `pip install Pillow`
- `check_links.py` - Optional `pip install requests` for external link checks

### Framework Philosophy
- **Workflows** define what to do (instructions)
- **Claude Code** handles reasoning and orchestration
- **Tools** handle deterministic execution

When making changes, check if a workflow exists first. Update workflows when you discover better methods.

## Development Workflow

**To view the website:**
```bash
# Option 1: Simple HTTP server with Python
python3 -m http.server 8000

# Option 2: If you have Node.js installed
npx serve

# Then open http://localhost:8000 in your browser
```

**To edit:**
- `index.html` - Main structure and content
- `style.css` - All styling and responsive design
- `script.js` - Interactive behaviors and animations

## Architecture & Design System

### Color System (Dark Khaki Theme)
The site uses CSS custom properties defined in `:root` in style.css:
- **Primary Background**: `#0f0f0f` (deep black)
- **Card Background**: `#1a1a1a` (lighter black for surfaces)
- **Accent Color**: `#BDB76B` (khaki) - used for CTAs, highlights, and interactive elements
- **Text**: `#f0f0f0` (primary) and `#b8b8b8` (secondary/body)

All colors are referenced via CSS variables like `var(--color-accent)`.

### Typography Hierarchy
- **Display font** (`--font-display`): Cormorant Garamond - used for large titles and hero text
- **Body font** (`--font-body`): Work Sans - used for all body text, buttons, navigation
- Font sizes use `clamp()` for fluid responsive scaling

### Key Interactive Features

**1. Scroll-Based Animations**
- Intersection Observer API triggers fade-in animations on `.project` and `.testimonial` cards (script.js:19-42)
- Parallax effect on hero background shapes using `requestAnimationFrame` (script.js:44-65)
- Header background changes on scroll (script.js:68-87)

**2. Custom Cursor (Desktop Only)**
- Custom cursor with hover effects enabled only on screens > 1024px (script.js:126-158)
- Dynamically injected styles for cursor behavior

**3. Smooth Scroll Navigation**
- All anchor links scroll smoothly with header offset (script.js:1-17)

### Responsive Breakpoints
- **Desktop**: 1024px+ (full layout, custom cursor, large typography)
- **Tablet**: 768px - 1024px (2-column to 1-column transitions)
- **Mobile**: 480px - 768px (simplified navigation, stacked layouts)
- **Small Mobile**: < 480px (logo text hidden, full-width buttons)

## Content Structure

The portfolio has 5 main sections:

1. **Hero** - Opening with value proposition, dual CTAs, floating workflow card with connected automation nodes
2. **Work** - 3 project cards (Kuration AI, boldys.ai, Purple Sales) — screenshots link to live websites
3. **About** - Personal bio, profile image, skills grid (2 columns: Core Expertise & Tools)
4. **Testimonials** - Infinite horizontal scroll carousel (pauses on hover) with testimonials from Sacha Delcourt and Greg Benadiba
5. **Contact** - Final CTA with email, LinkedIn, WhatsApp links

## Design Principles

**Performance Optimizations:**
- Debounced scroll handlers to reduce repaints (script.js:183-200)
- `requestAnimationFrame` for smooth parallax animations
- Font preloading for Cormorant Garamond and Work Sans (script.js:166-180)
- Minimal JavaScript footprint

**Accessibility:**
- WCAG AA compliant text contrast
- Touch-friendly button sizes (44px minimum)
- Semantic HTML structure
- Focus states on all interactive elements

**Visual Effects:**
- Floating workflow card in hero with animated dashed connecting lines and tool nodes
- Grain texture overlay for premium feel (inline SVG in CSS)
- Card hover effects with lift animations and glow shadows
- Gradient backgrounds and border animations on testimonials
- Infinite horizontal scroll on testimonials with hover-pause

## Common Modifications

**To update contact information:**
- Email: Search for `benjamin.audry@hotmail.com` in index.html
- LinkedIn: Search for `linkedin.com/in/ben-audry`
- Calendly: Search for `calendly.com/benjamin-boldys/linkedin`

**To add/modify projects:**
- Edit the `.projects` grid in the Work Section (index.html:105-197)
- Each project follows this structure: `.project` > `.project-media` + `.project-content`
- Featured projects use `.project-featured` class for larger media column

**To update theme colors:**
- Modify CSS custom properties in `:root` (style.css:1-30)
- All colors are referenced via variables, so changes propagate automatically

## ⚠️ Critical Architecture Warnings

### Code Duplication Risk (HIGH PRIORITY)

**IMPORTANT**: Header and footer are duplicated across multiple files. When updating navigation or footer, you MUST update ALL of these files:

1. `index.html` - Main page header
2. `projects/kuration-ai.html` - Project detail header
3. `projects/boldys-ai.html` - Project detail header
4. `projects/purple-sales.html` - Project detail header
5. `services/simple-automation.html` - Service detail header
6. `services/complex-automation.html` - Service detail header
7. `services/in-person-consulting.html` - Service detail header
8. `privacy-policy.html` - Privacy policy header

**Checklist for navigation changes:**
- [ ] Update `index.html` header
- [ ] Update `projects/kuration-ai.html` header
- [ ] Update `projects/boldys-ai.html` header
- [ ] Update `projects/purple-sales.html` header
- [ ] Update `services/simple-automation.html` header
- [ ] Update `services/complex-automation.html` header
- [ ] Update `services/in-person-consulting.html` header
- [ ] Update `privacy-policy.html` header
- [ ] Test all navigation links work from each page
- [ ] Run `python tools/validate_html.py` on all pages

### Content Update Protocol

When updating content (projects, testimonials, stats):
1. **Always** back up the file first
2. Edit HTML carefully to avoid breaking structure
3. Run `python tools/validate_html.py index.html` before committing
4. Test responsiveness at all breakpoints (480px, 768px, 1024px)

### Pre-Deployment Checklist

Before deploying changes:
```bash
# Validate HTML structure
python tools/validate_html.py index.html

# Check all links
python tools/check_links.py index.html

# Optimize any new images
python tools/optimize_images.py path/to/image.jpg --max-width 800

# Test locally
python3 -m http.server 8000
```

## Compound Engineering

This project follows the **Compound Engineering** philosophy: every piece of work should make future work easier.

### The Compound Loop

1. **Plan** → Research codebase patterns, best practices, framework docs before coding
2. **Work** → Execute the plan
3. **Assess** → Review from multiple perspectives (see below)
4. **Compound** → Capture learnings so they apply next time

### Capturing Learnings

When you discover something important (a bug pattern, a better approach, a gotcha):

1. **Quick fix**: Add it directly to this CLAUDE.md file
2. **Detailed learning**: Create a file in `docs/learnings/` with frontmatter for searchability

Example learning file:
```markdown
---
tags: [css, responsive, bug-fix]
date: 2025-01-15
---
# Mobile viewport height issue

On iOS Safari, `100vh` doesn't account for the address bar.
Use `100dvh` (dynamic viewport height) instead.
```

### Review Perspectives

When reviewing changes, consider these angles:

| Perspective | Focus |
|-------------|-------|
| **Security** | XSS, injection, exposed secrets, unsafe links |
| **Simplicity** | Can this be done with less code? Over-engineered? |
| **Accessibility** | Keyboard navigation, screen readers, contrast |
| **Performance** | Image sizes, render blocking, unnecessary JS |
| **Mobile-first** | Does it work on 320px screens? Touch targets 44px+? |

### Compounding Tips

- If Claude makes a mistake, say "add this to CLAUDE.md" so it won't repeat it
- Store architecture decisions in `docs/` for future reference
- When a pattern works well, document it as a skill in `.claude/skills/`
- Review the compound loop after major features

## Notes

- This is a git repository (branch: `dev`, main branch: `main`)
- No package.json or build configuration - intentionally simple
- All styles are in a single CSS file with clear section comments
- The grain texture effect is achieved with an inline SVG filter in CSS
- Network visualization uses native SVG animations (no JavaScript required)
