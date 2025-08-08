# README Templates

This folder contains the template files used to generate the project's README documentation.

## Files

- `README_template.md` - English README template
- `README_CN_template.md` - Chinese README template

## Usage

These template files are used by the `crawl/generate_readme.py` script to generate the final README files in the project root. The script:

1. Reads the base content from these template files
2. Adds dynamically generated content (country links and today's wallpaper)
3. Outputs the final README files to the project root

## Important Notes

- **DO NOT** modify the generated README files in the project root directly
- **DO** modify these template files if you need to update the base README content
- The generated README files are automatically updated daily by GitHub Actions

## Template Structure

Each template contains:
- Project description and features
- Project structure
- Core scripts documentation
- Usage instructions
- Configuration details

The `generate_readme.py` script appends:
- Links to all country wallpaper documents
- Today's featured wallpaper content