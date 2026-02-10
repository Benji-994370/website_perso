---
name: content-update
description: Update website content (text, projects, testimonials). Use when user wants to change copy, add new content, or update existing sections.
allowed-tools: Read, Edit, Write, Bash(python *), Grep
---

# Content Update Skill

Safely update content on the portfolio website.

## Content Locations

| Content Type | File | Section |
|--------------|------|---------|
| Hero headline | `index.html` | Lines ~30-50 |
| Hero CTAs | `index.html` | `.hero-actions` |
| Projects | `index.html` | `.projects` grid |
| About bio | `index.html` | `#about` section |
| Skills list | `index.html` | `.skills-grid` |
| Testimonials | `index.html` | `.testimonials` |
| Contact info | `index.html` | `#contact` section |

## Before Making Changes

1. **Read the current content first** - Never edit blind
2. **Backup is automatic** - Git tracks all changes
3. **Validate after** - Run `python tools/validate_html.py index.html`

## Update Patterns

### Update Text Content

```html
<!-- Find the element, update only the text -->
<h1 class="hero-title">New Headline Here</h1>
```

### Add a New Project

Follow this structure:
```html
<article class="project">
  <div class="project-media">
    <a href="https://project-url.com" target="_blank">
      <img src="images/screenshots/project-name.png" alt="Project Name screenshot">
    </a>
  </div>
  <div class="project-content">
    <span class="project-tag">Category</span>
    <h3>Project Name</h3>
    <p>Project description goes here.</p>
  </div>
</article>
```

### Add a Testimonial

```html
<div class="testimonial">
  <div class="testimonial-content">
    <p class="testimonial-quote">"The testimonial quote here."</p>
    <div class="testimonial-author">
      <img src="images/profile/person-name.jpg" alt="Person Name">
      <div>
        <span class="author-name">Person Name</span>
        <span class="author-title">Title, Company</span>
      </div>
    </div>
  </div>
</div>
```

### Update Contact Info

Search and replace these patterns:
- Email: `benjamin.audry@hotmail.com`
- LinkedIn: `linkedin.com/in/ben-audry`
- Calendly: `calendly.com/benjamin-boldys/linkedin`
- WhatsApp: `wa.me/` link

## Multi-Page Updates (CRITICAL)

**Headers and footers are duplicated!** When updating navigation:

Update ALL of these files:
1. `index.html`
2. `projects/kuration-ai.html`
3. `projects/boldys-ai.html`
4. `projects/purple-sales.html`
5. `services/simple-automation.html`
6. `services/complex-automation.html`
7. `services/in-person-consulting.html`
8. `privacy-policy.html`

## Post-Update Checklist

```bash
# Validate HTML
python tools/validate_html.py index.html

# Check links
python tools/check_links.py index.html

# Test locally at different breakpoints
python3 -m http.server 8000
```

## Common Mistakes to Avoid

- Don't break HTML structure (missing closing tags)
- Don't use straight quotes `"` in content - use `&quot;` or curly quotes
- Don't forget `alt` text on images
- Don't use emojis unless specifically requested
- Don't update headers without updating ALL pages
