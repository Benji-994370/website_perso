# Add a New Testimonial

This guide explains how to add a new testimonial to the carousel on the website.

## Quick Steps

1. Open `index.html`
2. Find the `<div class="testimonial-track">` section
3. Copy an existing testimonial `<article class="testimonial">...</article>`
4. Paste it after the last testimonial (before the closing `</div>` of testimonial-track)
5. Update the content with the new testimonial details

## Testimonial Template

Copy and paste this template inside the `.testimonial-track` div:

```html
<!-- Testimonial: [NAME] -->
<article class="testimonial">
    <div class="testimonial-header">
        <div class="testimonial-author-main">
            <div class="author-image-wrapper">
                <!-- Option A: Use an image -->
                <img src="[FILENAME].jpg" alt="[NAME]" class="author-image">

                <!-- Option B: Use initials (delete the img tag above) -->
                <!-- <div class="author-image author-initials">[INITIALS]</div> -->

                <svg class="author-decoration" width="100" height="100" viewBox="0 0 100 100">
                    <circle cx="50" cy="50" r="48" fill="none" stroke="#BDB76B" stroke-width="1" opacity="0.4"/>
                    <circle cx="50" cy="50" r="40" fill="none" stroke="#BDB76B" stroke-width="1" opacity="0.3" stroke-dasharray="4 4"/>
                </svg>
            </div>
            <div class="author-info-main">
                <div class="author-name">[FULL NAME]</div>
                <div class="author-title">[JOB TITLE]</div>
                <a href="[LINKEDIN_URL]" target="_blank" class="author-linkedin-inline">
                    <svg width="16" height="16" viewBox="0 0 20 20" fill="none">
                        <path d="M18.5 0H1.5C0.675 0 0 0.675 0 1.5V18.5C0 19.325 0.675 20 1.5 20H18.5C19.325 20 20 19.325 20 18.5V1.5C20 0.675 19.325 0 18.5 0ZM6 17H3V7.5H6V17ZM4.5 6.25C3.5 6.25 2.75 5.45 2.75 4.5C2.75 3.55 3.5 2.75 4.5 2.75C5.5 2.75 6.25 3.55 6.25 4.5C6.25 5.45 5.5 6.25 4.5 6.25ZM17 17H14V12.4C14 11.25 14 9.75 12.4 9.75C10.8 9.75 10.5 11 10.5 12.3V17H7.5V7.5H10.4V8.8C10.8 8.1 11.8 7.3 13.3 7.3C16.3 7.3 17 9.2 17 11.7V17Z" fill="currentColor"/>
                    </svg>
                    View Profile
                </a>
            </div>
        </div>
        <div class="testimonial-badges">
            <svg class="badge-icon" width="48" height="48" viewBox="0 0 48 48" fill="none">
                <circle cx="24" cy="24" r="23" stroke="url(#badge-gradient-[UNIQUE_ID])" stroke-width="1"/>
                <path d="M24 8L26.4 18.8L35.6 13.6L30.4 22.8L41.2 25.2L30.4 27.6L35.6 36.8L26.4 31.6L24 42.4L21.6 31.6L12.4 36.8L17.6 27.6L6.8 25.2L17.6 22.8L12.4 13.6L21.6 18.8L24 8Z" fill="url(#badge-gradient-[UNIQUE_ID])" opacity="0.3"/>
                <circle cx="24" cy="25" r="8" fill="none" stroke="url(#badge-gradient-[UNIQUE_ID])" stroke-width="1.5"/>
                <defs>
                    <linearGradient id="badge-gradient-[UNIQUE_ID]" x1="0" y1="0" x2="48" y2="48">
                        <stop offset="0%" stop-color="#BDB76B"/>
                        <stop offset="100%" stop-color="#8B864E"/>
                    </linearGradient>
                </defs>
            </svg>
        </div>
    </div>
    <div class="testimonial-quote">
        <svg class="quote-icon" width="40" height="32" viewBox="0 0 40 32" fill="none">
            <path d="M0 32V16.4C0 10.96 1.28 6.62667 3.84 3.4C6.4 0.133333 10 -1.07288e-06 14.64 0V5.6C12.48 5.76 10.6933 6.62667 9.28 8.2C7.86667 9.73333 7.16 11.76 7.16 14.28H16V32H0ZM24 32V16.4C24 10.96 25.28 6.62667 27.84 3.4C30.4 0.133333 34 -1.07288e-06 38.64 0V5.6C36.48 5.76 34.6933 6.62667 33.28 8.2C31.8667 9.73333 31.16 11.76 31.16 14.28H40V32H24Z" fill="currentColor" opacity="0.1"/>
        </svg>
        <p class="testimonial-text">
            [PARAGRAPH 1 OF TESTIMONIAL]
        </p>
        <p class="testimonial-text">
            [PARAGRAPH 2 OF TESTIMONIAL]
        </p>
        <p class="testimonial-text">
            [PARAGRAPH 3 OF TESTIMONIAL - OPTIONAL]
        </p>
    </div>
    <div class="testimonial-stats">
        <div class="stat-item">
            <svg class="stat-icon" width="24" height="24" viewBox="0 0 24 24" fill="none">
                <path d="M13 10V3L4 14h7v7l9-11h-7z" fill="currentColor"/>
            </svg>
            <span>[SKILL 1]</span>
        </div>
        <div class="stat-item">
            <svg class="stat-icon" width="24" height="24" viewBox="0 0 24 24" fill="none">
                <circle cx="12" cy="12" r="3" fill="currentColor"/>
                <path d="M12 2a2 2 0 00-2 2v1a2 2 0 002 2 2 2 0 002-2V4a2 2 0 00-2-2zM12 17a2 2 0 00-2 2v1a2 2 0 002 2 2 2 0 002-2v-1a2 2 0 00-2-2zM22 10h-1a2 2 0 00-2 2 2 2 0 002 2h1a2 2 0 002-2 2 2 0 00-2-2zM7 10H6a2 2 0 00-2 2 2 2 0 002 2h1a2 2 0 002-2 2 2 0 00-2-2z" fill="currentColor" opacity="0.5"/>
            </svg>
            <span>[SKILL 2]</span>
        </div>
        <div class="stat-item">
            <svg class="stat-icon" width="24" height="24" viewBox="0 0 24 24" fill="none">
                <path d="M20 6L9 17l-5-5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
            </svg>
            <span>[SKILL 3]</span>
        </div>
    </div>
</article>
```

## Fields to Replace

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `[NAME]` | Person's full name | John Smith |
| `[FILENAME]` | Image filename (without extension) | john-smith |
| `[INITIALS]` | 2-letter initials (if no photo) | JS |
| `[FULL NAME]` | Full display name | John Smith |
| `[JOB TITLE]` | Their role/position | CEO & Founder |
| `[LINKEDIN_URL]` | Full LinkedIn profile URL | https://www.linkedin.com/in/johnsmith/ |
| `[UNIQUE_ID]` | A number (3, 4, 5...) for SVG gradient ID | 3 |
| `[PARAGRAPH 1-3]` | Testimonial text split into paragraphs | "Working with Benjamin was..." |
| `[SKILL 1-3]` | 3 key skills/qualities mentioned | Automation Expert |

## Adding a Profile Photo

1. **Get the image**: Save the person's profile photo (ideally from LinkedIn)
2. **Name it**: Use format `firstname-lastname.jpg` (e.g., `john-smith.jpg`)
3. **Optimize it**: Run `python tools/optimize_images.py [image.jpg] --max-width 200`
4. **Place it**: Put the file in the root website folder
5. **Update HTML**: Set `src="firstname-lastname.jpg"` in the template

## Using Initials Instead

If no photo is available, use the initials avatar:

```html
<!-- Delete the img tag and use this instead: -->
<div class="author-image author-initials">JS</div>
```

## Infinite Scroll Behavior

Testimonials display as an infinite horizontal scroll (very slow, album-style). JavaScript automatically clones all testimonials to create a seamless loop. No dots or navigation arrows — just add your testimonial inside `.testimonial-track` and it will appear in the scroll.

Hovering over any testimonial pauses the scroll so the reader can read it fully.

## Testing

After adding a testimonial:

1. Start the server: `python3 -m http.server 8000`
2. Open http://localhost:8000
3. Wait 10 seconds for fonts and animations to fully load
4. Check that:
   - The new testimonial appears in the horizontal scroll
   - Hovering pauses the scroll completely
   - Moving the mouse away resumes scrolling
   - The testimonial displays properly on mobile

## Troubleshooting

**Carousel not working?**
- Check that the testimonial is inside `.testimonial-track`
- Make sure all HTML tags are properly closed
- Check browser console for JavaScript errors

**Image not showing?**
- Verify the filename matches exactly (case-sensitive)
- Ensure the image is in the root folder
- Check the file extension (.jpg, .png)

**Styling looks wrong?**
- Make sure you copied all the required HTML structure
- Check that class names match exactly
- Ensure the `[UNIQUE_ID]` is different from existing testimonials
