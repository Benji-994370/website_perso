# Workflows

Standard Operating Procedures (SOPs) for managing the portfolio website.

## Available Workflows

| Workflow | Purpose |
|----------|---------|
| [update_content.md](update_content.md) | Update website text content (hero, about, projects, etc.) |
| [add_project.md](add_project.md) | Add a new project card to the portfolio |
| [manage_images.md](manage_images.md) | Add, optimize, and update images |
| [deploy.md](deploy.md) | Deploy website to hosting platforms |

## How to Use

1. Identify which workflow matches your task
2. Open the relevant `.md` file
3. Follow the steps in order
4. Use the referenced tools when specified
5. Update the workflow if you discover improvements

## Related Tools

All tools are located in `../tools/`:

- `validate_html.py` - Check HTML validity and accessibility
- `optimize_images.py` - Resize and compress images
- `check_links.py` - Verify all links work

## Framework Reference

This project follows the WAT (Workflows, Agents, Tools) architecture:
- **Workflows**: These SOPs (you're reading one now)
- **Agents**: Claude Code handles reasoning and orchestration
- **Tools**: Python scripts in `tools/` handle execution
