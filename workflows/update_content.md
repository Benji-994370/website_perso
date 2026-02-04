# Update Website Content

Update text content across the portfolio website.

## Objective
Modify existing text content in any section of the website while maintaining consistency and formatting.

## Required Inputs
- **Section**: Which section to update (hero, about, work, testimonials, contact)
- **New content**: The updated text

## Sections Reference

### Hero Section (lines ~58-103 in index.html)
- Main headline: `<h1>` inside `.hero-content`
- Subtitle/tagline: `<p class="hero-subtitle">`
- Stats: `.hero-stats` badges
- CTA buttons: `.hero-ctas` links

### About Section (lines ~199-270 in index.html)
- Main bio: `<p>` tags inside `.about-text`
- Skills grid: `.skills-grid` with two columns
  - Core Expertise: First `.skills-column`
  - Tools & Tech: Second `.skills-column`

### Work Section (lines ~105-197 in index.html)
- Section intro: `<p class="section-intro">`
- Individual projects: See `add_project.md` for structure

### Testimonials Section (lines ~272-315 in index.html)
- Quote text: `<p class="testimonial-quote">`
- Author name: `<span class="author-name">`
- Author title: `<span class="author-title">`
- Stats: `.testimonial-stats` items

### Contact Section (lines ~317-350 in index.html)
- Headline: `<h2>` inside `.contact-content`
- Description: `<p>` after the headline
- Email: Link with `mailto:`
- LinkedIn: Link with LinkedIn URL
- Calendly: Link with Calendly URL

## Steps

1. **Identify the section** in `index.html` using the line references above
2. **Locate the specific element** to update
3. **Edit the content** preserving HTML structure and classes
4. **Validate changes**:
   ```bash
   python tools/validate_html.py index.html
   ```
5. **Preview locally**:
   ```bash
   python3 -m http.server 8000
   # Visit http://localhost:8000
   ```

## Edge Cases

- **Long text**: Keep paragraphs concise for readability
- **Special characters**: Use HTML entities (`&amp;`, `&quot;`, etc.)
- **Links**: Update both the `href` and visible text
- **Stats/numbers**: Ensure consistency (don't mix formats like "3" vs "three")

## Contact Information

Current contact details (update all instances):
- Email: `benjamin.audry.pro@gmail.com`
- LinkedIn: `linkedin.com/in/ben-audry`
- Calendly: `calendly.com/benjamin-boldys/linkedin`
