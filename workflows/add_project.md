# Add New Project

Add a new project card to the portfolio Work section.

## Objective
Create a new project entry that matches the existing visual style and structure.

## Required Inputs
- **Project name**: Title of the project
- **Description**: 2-3 sentences about the project and your role
- **Tags**: 2-4 category tags (e.g., "AI", "Growth", "B2B")
- **Link**: URL to the project or company website
- **Image** (optional): Screenshot or visual representing the project

## Project Card Structure

```html
<article class="project">
    <div class="project-media">
        <div class="project-image-wrapper">
            <a href="PROJECT_WEBSITE_URL" target="_blank" rel="noopener noreferrer" class="project-image-link">
                <img src="images/PROJECT_IMAGE.png" alt="PROJECT_NAME Homepage" class="project-screenshot">
            </a>
        </div>
    </div>
    <div class="project-content">
        <div class="project-meta">
            <span class="project-year">YEAR</span>
            <span class="project-category">CATEGORY</span>
        </div>
        <h3 class="project-title">PROJECT_NAME</h3>
        <p class="project-description">PROJECT_DESCRIPTION</p>
        <a href="projects/PROJECT_DETAIL_PAGE.html" class="project-link">
            See Details
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                <path d="M4 10H16M16 10L10 4M16 10L10 16" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
            </svg>
        </a>
    </div>
</article>
```

## Featured Project Variant

For highlighted projects, add the `project-featured` class:

```html
<article class="project project-featured">
    <!-- Same structure as above -->
</article>
```

This makes the image larger (60% width vs 45% on desktop).

## Steps

1. **Prepare the image** (if applicable):
   ```bash
   python tools/optimize_images.py input.jpg --output ./
   ```
   Recommended: 800x500px for standard, 1200x700px for featured

2. **Open `index.html`** and locate the Work section (~line 246)

3. **Find the `.projects` grid** (after the section intro)

4. **Add new project card** using the structure above
   - Copy an existing `<article class="project">` as template
   - Replace placeholder values
   - Position based on importance (featured projects first)

5. **Validate HTML**:
   ```bash
   python tools/validate_html.py index.html
   ```

6. **Check links**:
   ```bash
   python tools/check_links.py index.html
   ```

7. **Preview locally** and verify:
   - Card displays correctly on desktop and mobile
   - Image loads properly
   - Link works
   - Tags are visible

## Current Projects (for reference)

1. **Kuration AI** (featured) - AI-powered B2B prospecting → kurationai.com
2. **boldys.ai** - AI automation agency → boldys.ai
3. **Purple Sales** - Outbound marketing campaigns → mypurplesales.com

## Edge Cases

- **No image available**: Use a gradient placeholder (CSS handles this automatically)
- **Long project names**: Keep under 40 characters for best display
- **External links**: Always include `target="_blank" rel="noopener"`
- **Tag overflow**: Limit to 4 tags maximum
