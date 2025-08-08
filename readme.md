# Bing Wallpaper Data Crawler and Markdown Generator

This directory contains scripts for automatically crawling Bing wallpaper data and generating markdown documentation.

## Files

### `bing_data.py`
- **Purpose**: Crawls daily Bing wallpaper data from multiple countries
- **Function**: Fetches wallpaper metadata and saves to `jsonc/{country}/bing.jsonc`
- **Countries**: Supports 25+ countries including US, UK, Germany, France, China, Japan, etc.
- **Schedule**: Runs daily at 23:01 UTC via GitHub Actions

### `generate_markdown.py`
- **Purpose**: Generates markdown documentation for wallpaper collections
- **Function**: Creates country-specific wallpaper list files (e.g., `us-wallpaper-list.md`)
- **Features**:
  - Today's featured wallpaper
  - Recent 30 days wallpaper grid (3 per row)
  - Archive navigation by year/month
  - Responsive markdown table format
  - Multilingual support for section titles
- **Output**: Creates `{country}-wallpaper-list.md` files in project root

## Workflow

The automated process runs daily via GitHub Actions:

1. **Data Crawling** (`bing_data.py`)
   - Fetches latest wallpaper data from Bing API
   - Updates existing JSON files with new entries
   - Maintains chronological order (newest first)

2. **Markdown Generation** (`generate_markdown.py`)
   - Reads updated JSON data
   - Generates formatted markdown documents
   - Creates responsive tables for GitHub display

3. **Git Commit**
   - Commits updated data and markdown files
   - Pushes changes to repository

## Generated Markdown Features

Each generated markdown file includes:

- **Header**: Country-specific title
- **Today's Wallpaper**: Featured image with description
- **Recent 30 Days Grid**: 3-column responsive table showing wallpapers from the last 30 days
- **Archive Navigation**: Year/month links for browsing
- **Footer**: Usage information

### Recent Improvements

- **Fixed Table Formatting**: Resolved markdown table separator issue where multiple separator rows were being generated. Now uses proper markdown table format with a single separator row after the header.
- **Improved Layout**: Enhanced 3-column grid layout for better visual presentation of wallpaper collections.
- **Recent 30 Days View**: Changed from current month view to recent 30 days view for more flexible time-based wallpaper browsing. Supports multilingual titles (English, German, French, Chinese, Japanese).

## Usage

### Manual Execution

```bash
# Crawl wallpaper data
python crawl/bing_data.py

# Generate markdown files
python crawl/generate_markdown.py
```

### Automatic Execution

The workflow runs automatically via GitHub Actions:
- **Schedule**: Daily at 23:01 UTC
- **Trigger**: Can also be manually triggered
- **Output**: Updated JSON data and markdown files

## Configuration

### Supported Countries

The scripts support the following countries:

- `us` - United States
- `gb` - United Kingdom  
- `de` - Germany
- `fr` - France
- `cn` - China
- `jp` - Japan
- And 20+ more...

### File Structure

```
jsonc/
├── us/bing.jsonc          # US wallpaper data
├── gb/bing.jsonc          # UK wallpaper data
└── ...

messages/
├── us.json                # US localization
├── gb.json                # UK localization
└── ...

Generated files:
├── us-wallpaper-list.md   # US wallpaper markdown
├── gb-wallpaper-list.md   # UK wallpaper markdown
└── ...
```

## Dependencies

- `requests` - For HTTP API calls
- `json` - For data processing
- `datetime` - For date handling

## GitHub Actions Integration

The workflow is defined in `.github/workflows/python-app.yml`:

```yaml
- name: run bingjson
  run: python crawl/bing_data.py

- name: Generate markdown documents  
  run: python crawl/generate_markdown.py

- name: Commit and Push
  run: |
    git add .
    git commit -m "Update wallpaper data and markdown at $(date)"
    git push
```

This ensures that both data collection and documentation generation happen automatically every day.