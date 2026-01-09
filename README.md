# Bing Wallpaper Data Crawler and Markdown Generator

- [English Documentation](README.md)
- [中文文档](README_CN.md)

An automated Bing wallpaper data collection and documentation generation project that supports daily wallpaper data crawling, high-definition image downloading, and Markdown document generation for 34+ countries and regions.

## 🌟 Key Features

### 📊 Data Crawling
- **Multi-Country Support**: Supports 34+ countries and regions for Bing wallpaper data
- **Daily Auto-Update**: Automatically runs daily at 23:01 UTC via GitHub Actions
- **Data Integrity**: Saves complete wallpaper metadata including titles, copyright info, descriptions, etc.

### 🖼️ Image Download
- **High-Definition Wallpapers**: Automatically downloads UHD ultra-high-definition wallpapers
- **Smart Deduplication**: Automatically detects and removes duplicate images based on MD5 hash
- **Incremental Download**: Only downloads new wallpapers, avoiding duplicates
- **File Management**: Uses MD5 values as filenames for easy management and deduplication

### 📝 Document Generation
- **Automated Documentation**: Generates dedicated Markdown documents for each country
- **Responsive Layout**: 3-column grid layout that adapts to different screen sizes
- **Multi-Time Dimensions**: Supports today's wallpaper, recent 30 days, and archive browsing by year/month
- **Multilingual Support**: Supports interface text in multiple languages

## 🗂️ Project Structure

```
Project Root/
├── .github/workflows/          # GitHub Actions workflows
│   └── python-app.yml         # Automation task configuration
├── crawl/                     # Crawler scripts directory
│   ├── bing_data.py          # Data crawling script
│   ├── download_wallpapers_action.py  # Wallpaper download script (Actions version)
│   ├── download_wallpapers.py # Wallpaper download script (Local version)
│   ├── generate_markdown.py  # Markdown document generation script
│   ├── generate_readme.py    # README generation script
│   └── deduplicate_images.py # Image deduplication tool
├── jsonc/                     # Wallpaper data storage
│   ├── us/bing.jsonc         # US wallpaper data
│   ├── cn/bing.jsonc         # China wallpaper data
│   └── ...                   # Other country data
├── images/                    # Downloaded wallpaper images
│   ├── {md5}.jpg             # Image files named with MD5
│   └── ...
├── markdown/                  # Generated documents
│   ├── wallpaper-list-us.md  # US wallpaper document
│   ├── wallpaper-list-cn.md  # China wallpaper document
│   └── ...                   # Other country documents
├── messages/                  # Internationalization text
│   ├── us.json               # English interface text
│   ├── cn.json               # Chinese interface text
│   └── ...
├── templates/                 # README template files
│   ├── README_template.md    # English README template
│   └── README_CN_template.md # Chinese README template
├── README.md                  # Project documentation (auto-generated)
└── README_CN.md              # Chinese documentation (auto-generated)
```

## 🚀 Core Scripts

### `bing_data.py` - Data Crawling Script
- **Function**: Crawls daily wallpaper data from Bing API
- **Output**: Saves to `jsonc/{country}/bing.jsonc`
- **Features**:
  - Supports 34+ countries and regions
  - Automatic API response and error handling
  - Maintains chronological order (newest first)
  - Incremental updates, avoiding duplicate data

### `download_wallpapers_action.py` - Wallpaper Download Script
- **Function**: Downloads high-definition wallpaper images and manages files
- **Features**:
  - **Smart Skip**: Checks `md5` field in JSON, skips already downloaded items
  - **URL Construction**: `https://www.bing.com{urlbase}_UHD.jpg`
  - **MD5 Management**: Calculates image MD5 value, used as filename and deduplication identifier
  - **Auto Deduplication**: Automatically deletes duplicate files with same MD5
  - **Data Update**: Writes MD5 value back to JSON data

### `generate_markdown.py` - Document Generation Script
- **Function**: Generates beautiful Markdown wallpaper documents
- **Output**: Saves to `markdown/wallpaper-list-{country}.md`
- **Features**:
  - **Today's Wallpaper**: Showcases the featured wallpaper of the day
  - **Recent 30 Days**: 3-column grid layout showing recent wallpapers
  - **Archive Navigation**: Historical wallpaper browsing organized by year/month
  - **Responsive Design**: Display effects adapted to different devices
  - **Multilingual Support**: Displays interface in corresponding language based on country

### `generate_readme.py` - README Generation Script
- **Function**: Automatically generates bilingual README documents
- **Input**: Reads from `templates/README_template.md` and `templates/README_CN_template.md`
- **Output**: Updates `README.md` and `README_CN.md` in project root
- **Features**:
  - **Template-Based**: Uses template files to avoid overwriting base content
  - **Country Links**: Generates links to all country wallpaper documents
  - **Today's Wallpaper**: Embeds today's featured wallpaper (US for English, CN for Chinese)
  - **Bilingual Support**: Generates both English and Chinese versions
  - **Auto-Update**: Runs daily with other automation tasks

## ⚙️ Automated Workflow

GitHub Actions automatically executes the following steps daily:

1. **🔄 Checkout Code** - Get the latest project code
2. **🐍 Setup Python Environment** - Configure Python runtime environment
3. **📦 Install Dependencies** - Install necessary libraries like `requests`
4. **📊 Crawl Data** - Run `bing_data.py` to get latest wallpaper data
5. **🖼️ Download Images** - Run `download_wallpapers_action.py` to download new wallpapers
6. **📝 Generate Documents** - Run `generate_markdown.py` to update Markdown documents
7. **📄 Generate README** - Run `generate_readme.py` to update project README files
8. **💾 Commit Changes** - Automatically commit and push all updates

## 🌍 Supported Countries and Regions

The project supports the following 34 countries and regions:

| Code | Country/Region | Code | Country/Region | Code | Country/Region |
|------|----------------|------|----------------|------|----------------|
| `ar` | [🇦🇷 Argentina](markdown/wallpaper-list-ar.md) | `au` | [🇦🇺 Australia](markdown/wallpaper-list-au.md) | `br` | [🇧🇷 Brazil](markdown/wallpaper-list-br.md) | 
| `ca` | [🇨🇦 Canada](markdown/wallpaper-list-ca.md) | `cn` | [🇨🇳 China](markdown/wallpaper-list-cn.md) | `cz` | [🇨🇿 Czech Republic](markdown/wallpaper-list-cz.md) | 
| `de` | [🇩🇪 Germany](markdown/wallpaper-list-de.md) | `dk` | [🇩🇰 Denmark](markdown/wallpaper-list-dk.md) | `es` | [🇪🇸 Spain](markdown/wallpaper-list-es.md) | 
| `fi` | [🇫🇮 Finland](markdown/wallpaper-list-fi.md) | `fr` | [🇫🇷 France](markdown/wallpaper-list-fr.md) | `gb` | [🇬🇧 United Kingdom](markdown/wallpaper-list-gb.md) | 
| `gr` | [🇬🇷 Greece](markdown/wallpaper-list-gr.md) | `hk` | [🇭🇰 Hong Kong](markdown/wallpaper-list-hk.md) | `id` | [🇮🇩 Indonesia](markdown/wallpaper-list-id.md) | 
| `in` | [🇮🇳 India](markdown/wallpaper-list-in.md) | `it` | [🇮🇹 Italy](markdown/wallpaper-list-it.md) | `jp` | [🇯🇵 Japan](markdown/wallpaper-list-jp.md) | 
| `kr` | [🇰🇷 South Korea](markdown/wallpaper-list-kr.md) | `my` | [🇲🇾 Malaysia](markdown/wallpaper-list-my.md) | `nl` | [🇳🇱 Netherlands](markdown/wallpaper-list-nl.md) | 
| `no` | [🇳🇴 Norway](markdown/wallpaper-list-no.md) | `pl` | [🇵🇱 Poland](markdown/wallpaper-list-pl.md) | `pt` | [🇵🇹 Portugal](markdown/wallpaper-list-pt.md) | 
| `ru` | [🇷🇺 Russia](markdown/wallpaper-list-ru.md) | `se` | [🇸🇪 Sweden](markdown/wallpaper-list-se.md) | `sg` | [🇸🇬 Singapore](markdown/wallpaper-list-sg.md) | 
| `th` | [🇹🇭 Thailand](markdown/wallpaper-list-th.md) | `tr` | [🇹🇷 Turkey](markdown/wallpaper-list-tr.md) | `tw` | [🇹🇼 Taiwan](markdown/wallpaper-list-tw.md) | 
| `ua` | [🇺🇦 Ukraine](markdown/wallpaper-list-ua.md) | `us` | [🇺🇸 United States](markdown/wallpaper-list-us.md) | `vn` | [🇻🇳 Vietnam](markdown/wallpaper-list-vn.md) | 
| `za` | [🇿🇦 South Africa](markdown/wallpaper-list-za.md) |  |  |
## 🛠️ Local Usage

### Requirements
- Python 3.7+
- `requests` library

### Install Dependencies
```bash
pip install requests
```

### Manual Execution

```bash
# 1. Crawl wallpaper data
python crawl/bing_data.py

# 2. Download wallpaper images
python crawl/download_wallpapers_action.py

# 3. Generate Markdown documents
python crawl/generate_markdown.py

# 4. Generate README documents
python crawl/generate_readme.py
```

### Image Deduplication Tool
```bash
# Clean duplicate image files
python crawl/deduplicate_images.py
```

## 📋 Generated Document Features

Each generated Markdown document includes:

### 🎯 Today's Wallpaper
- High-definition wallpaper preview
- Detailed description and copyright information
- Click to view details page link

### 📅 Recent 30 Days
- 3-column responsive grid layout
- Thumbnail and basic information for each wallpaper
- Formatted date display

### 🗃️ Archive Navigation
- Month navigation grouped by year
- Current month highlighting
- Beautiful button-style design

### 🌐 Multilingual Support
- Automatically selects interface language based on country
- Supports English, Chinese, German, French, Japanese, etc.
- Extensible internationalization framework

## 🔧 Configuration

### GitHub Actions Configuration
Workflow configuration file: `.github/workflows/python-app.yml`

```yaml
name: Generate Bing Wallpaper Json Auto
on:
  schedule:
    - cron: '1 23 * * *'  # Execute daily at 23:01 UTC
  workflow_dispatch:      # Support manual trigger

jobs:
  download_and_push:
    runs-on: ubuntu-latest
    steps:
      - name: run bingjson
        run: python crawl/bing_data.py
      - name: Download wallpaper images
        run: python crawl/download_wallpapers_action.py
      - name: Generate markdown documents
        run: python crawl/generate_markdown.py
      - name: Generate README documents
        run: python crawl/generate_readme.py
      - name: Commit and Push
        run: |
          git add .
          git commit -m "Update wallpaper data and markdown at $(date)"
          git push
```

### Data Format
Each wallpaper data item contains the following fields:
- `startdate` / `enddate`: Start and end dates of the wallpaper
- `url` / `urlbase`: URL information of the wallpaper
- `copyright`: Copyright information
- `title`: Wallpaper title
- `md5`: MD5 hash value of the image file (added after download)
- `MediaContent`: Detailed media content information

## 🎨 Featured Capabilities

### Smart Download Management
- ✅ **Incremental Download**: Only downloads new wallpapers without `md5` field
- ✅ **Auto Deduplication**: Avoids duplicate images based on MD5 hash
- ✅ **Error Handling**: Graceful handling of network exceptions without interrupting the process
- ✅ **Detailed Logging**: Provides clear processing progress and result statistics

### Document Generation Optimization
- ✅ **Responsive Design**: Adapts to desktop and mobile devices
- ✅ **SEO Friendly**: Structured titles and metadata
- ✅ **Fast Loading**: Optimized image links and layout
- ✅ **User Experience**: Intuitive navigation and browsing experience

### Automated Operations
- ✅ **Scheduled Execution**: Daily automatic updates without manual intervention
- ✅ **Error Monitoring**: GitHub Actions provides execution status monitoring
- ✅ **Version Control**: All changes have complete Git history records
- ✅ **Scalability**: Easy to add new countries and features

## 📈 Project Statistics

- **Supported Countries**: 34+ countries and regions
- **Data Format**: JSON/JSONC structured storage
- **Image Quality**: UHD ultra-high-definition (usually 3840x2160 or higher)
- **Update Frequency**: Daily automatic updates
- **Document Format**: Markdown, perfectly compatible with GitHub

## 🤝 Contributing

Welcome to submit Issues and Pull Requests to improve this project!

## 📄 License

This project is for learning and research purposes only. All wallpaper copyrights belong to Microsoft Bing and the respective photographers/copyright owners.

---

*Last Updated: August 2025*

## 🌍 Country Wallpaper Links

Click the links below to view wallpaper for each country:

| [🇦🇷 Argentina](https://bing.codexun.com/ar) | [🇦🇺 Australia](https://bing.codexun.com/au) | [🇧🇷 Brazil](https://bing.codexun.com/br) | [🇨🇦 Canada](https://bing.codexun.com/ca) | [🇨🇳 China](https://bing.codexun.com/cn) | 
|:---:|:---:|:---:|:---:|:---:|
| [🇨🇿 Czech Republic](https://bing.codexun.com/cz) | [🇩🇪 Germany](https://bing.codexun.com/de) | [🇩🇰 Denmark](https://bing.codexun.com/dk) | [🇪🇸 Spain](https://bing.codexun.com/es) | [🇫🇮 Finland](https://bing.codexun.com/fi) | 
| [🇫🇷 France](https://bing.codexun.com/fr) | [🇬🇧 United Kingdom](https://bing.codexun.com/gb) | [🇬🇷 Greece](https://bing.codexun.com/gr) | [🇭🇰 Hong Kong](https://bing.codexun.com/hk) | [🇮🇩 Indonesia](https://bing.codexun.com/id) | 
| [🇮🇳 India](https://bing.codexun.com/in) | [🇮🇹 Italy](https://bing.codexun.com/it) | [🇯🇵 Japan](https://bing.codexun.com/jp) | [🇰🇷 South Korea](https://bing.codexun.com/kr) | [🇲🇾 Malaysia](https://bing.codexun.com/my) | 
| [🇳🇱 Netherlands](https://bing.codexun.com/nl) | [🇳🇴 Norway](https://bing.codexun.com/no) | [🇵🇱 Poland](https://bing.codexun.com/pl) | [🇵🇹 Portugal](https://bing.codexun.com/pt) | [🇷🇺 Russia](https://bing.codexun.com/ru) | 
| [🇸🇪 Sweden](https://bing.codexun.com/se) | [🇸🇬 Singapore](https://bing.codexun.com/sg) | [🇹🇭 Thailand](https://bing.codexun.com/th) | [🇹🇷 Turkey](https://bing.codexun.com/tr) | [🇹🇼 Taiwan](https://bing.codexun.com/tw) | 
| [🇺🇦 Ukraine](https://bing.codexun.com/ua) | [🇺🇸 United States](https://bing.codexun.com/us) | [🇻🇳 Vietnam](https://bing.codexun.com/vn) | [🇿🇦 South Africa](https://bing.codexun.com/za) |  | 


## Today's Wallpaper

[![Where time grows tall](https://www.bing.com/th?id=OHR.MuirWoodsMonument_EN-US9831416144_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260110)

**Where time grows tall**

Step into the realm of giants. Try embracing a BFG (Big Friendly Giant) as you wrap your arms around a thousand years of wisdom in a single tree trunk. Welcome to Muir Woods National Monument—established on this day in 1908—a majestic hall of coastal redwoods just north of San Francisco. These towering redwoods are the tallest trees on Earth—one here stretches about 258 feet, roughly the height of 43 people stacked head to toe. Most are 600–800 years old, and some have stood for over a millennium, yet they're still considered 'young' for a species that can live for 2,000 years.

*© photo by canderson/Getty Images (Bing United States)*

---

## Recent 30 Days

| | | |
|:---:|:---:|:---:|
| [![Where time grows tall](https://www.bing.com/th?id=OHR.MuirWoodsMonument_EN-US9831416144_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260110) | [![Rust meets rush](https://www.bing.com/th?id=OHR.StarlingBrighton2025_EN-US6998438769_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260109) | [![Rock legends](https://www.bing.com/th?id=OHR.OldRockArch_EN-US2422589534_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260108) | 
| **[Where time grows tall](https://bing.codexun.com/us/detail/20260110)**<br>Giant redwood trees in Muir Woods National Monument, California<br>*2026-01-10* | **[Rust meets rush](https://bing.codexun.com/us/detail/20260109)**<br>Starling murmuration over the ruins of Brighton's West Pier, England<br>*2026-01-09* | **[Rock legends](https://bing.codexun.com/us/detail/20260108)**<br>Turret Arch framed by North Window in Arches National Park, Utah<br>*2026-01-08* | 
| [![Chillin' in Nuuk](https://www.bing.com/th?id=OHR.NuukGreenland_EN-US6879869782_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260107) | [![Herd on high alert](https://www.bing.com/th?id=OHR.ImpalaRooibok_EN-US6797453661_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260106) | [![A royal view](https://www.bing.com/th?id=OHR.KingMountain_EN-US6730743729_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260105) | 
| **[Chillin' in Nuuk](https://bing.codexun.com/us/detail/20260107)**<br>Nuuk, Greenland<br>*2026-01-07* | **[Herd on high alert](https://bing.codexun.com/us/detail/20260106)**<br>A herd of impalas, Londolozi Game Reserve, South Africa<br>*2026-01-06* | **[A royal view](https://bing.codexun.com/us/detail/20260105)**<br>Kings Mountain, Chugach Mountains, Alaska<br>*2026-01-05* | 
| [![The steps before the saga](https://www.bing.com/th?id=OHR.LauterbrunnenValley_EN-US6594933852_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260104) | [![The soul of Venice](https://www.bing.com/th?id=OHR.VeniceView_EN-US3244163136_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260103) | [![Stretch into the New Year](https://www.bing.com/th?id=OHR.NewYearFox_EN-US6422915878_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260102) | 
| **[The steps before the saga](https://bing.codexun.com/us/detail/20260104)**<br>Staubbach Falls at Lauterbrunnen, Canton of Bern, Switzerland<br>*2026-01-04* | **[The soul of Venice](https://bing.codexun.com/us/detail/20260103)**<br>Aerial view of Venice, Italy<br>*2026-01-03* | **[Stretch into the New Year](https://bing.codexun.com/us/detail/20260102)**<br>Arctic fox sleeping<br>*2026-01-02* | 
| [![Where Berlin bridges the New Year](https://www.bing.com/th?id=OHR.GermanyNewYear_EN-US6344260060_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260101) | [![Whoop, there they fly](https://www.bing.com/th?id=OHR.JapanSwans_EN-US6228421340_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251231) | [![The church that outlived a city](https://www.bing.com/th?id=OHR.AniTurkey_EN-US6168768263_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251230) | 
| **[Where Berlin bridges the New Year](https://bing.codexun.com/us/detail/20260101)**<br>New Year's Eve, Oberbaum Bridge, Berlin, Germany<br>*2026-01-01* | **[Whoop, there they fly](https://bing.codexun.com/us/detail/20251231)**<br>Whooper swans, Kotoku Pond, Japan<br>*2025-12-31* | **[The church that outlived a city](https://bing.codexun.com/us/detail/20251230)**<br>St. Gregory Church in Ani Ruins, Kars, Türkiye<br>*2025-12-30* | 
| [![What remains wild](https://www.bing.com/th?id=OHR.RuffedLemur_EN-US6014028083_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251229) | [![Shards of winter](https://www.bing.com/th?id=OHR.SuperiorIceMN_EN-US5952266924_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251228) | [![Unboxed traditions](https://www.bing.com/th?id=OHR.WiltshireDawn_EN-US5663179833_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251227) | 
| **[What remains wild](https://bing.codexun.com/us/detail/20251229)**<br>Black-and-white ruffed lemur in Madagascar<br>*2025-12-29* | **[Shards of winter](https://bing.codexun.com/us/detail/20251228)**<br>Plate ice along Lake Superior, Grand Marais, Minnesota<br>*2025-12-28* | **[Unboxed traditions](https://bing.codexun.com/us/detail/20251227)**<br>Salisbury Cathedral, Wiltshire, England<br>*2025-12-27* | 
| [![Miniature worlds, infinite wonder](https://www.bing.com/th?id=OHR.SantaGlobe_EN-US5819361091_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251226) | [![Traditions that travel](https://www.bing.com/th?id=OHR.ElmauChapel_EN-US5704228113_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251225) | [![Where holiday magic runs on hooves](https://www.bing.com/th?id=OHR.ReindeerFinland_EN-US5636971050_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251224) | 
| **[Miniature worlds, infinite wonder](https://bing.codexun.com/us/detail/20251226)**<br>Snow globes at a Christmas market in Heidelberg, Germany<br>*2025-12-26* | **[Traditions that travel](https://bing.codexun.com/us/detail/20251225)**<br>Snowy chapel with Christmas tree in the Bavarian Alps, Germany<br>*2025-12-25* | **[Where holiday magic runs on hooves](https://bing.codexun.com/us/detail/20251224)**<br>Reindeer during winter snowfall, Lapland, Finland<br>*2025-12-24* | 
| [![From Hoffmann's pages to global stages](https://www.bing.com/th?id=OHR.NutcrackerAnkara_EN-US5537620581_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251223) | [![Birth of the new sun](https://www.bing.com/th?id=OHR.SwedenSolstice_EN-US5470044971_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251222) | [![Twinkle, twinkle, paper stars](https://www.bing.com/th?id=OHR.StarLanterns_EN-US5419993556_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251221) | 
| **[From Hoffmann's pages to global stages](https://bing.codexun.com/us/detail/20251223)**<br>'The Nutcracker' performed by the Turkish State Opera and Ballet in Ankara, Türkiye<br>*2025-12-23* | **[Birth of the new sun](https://bing.codexun.com/us/detail/20251222)**<br>Dawn light through frosty trees, Sweden<br>*2025-12-22* | **[Twinkle, twinkle, paper stars](https://bing.codexun.com/us/detail/20251221)**<br>Christmas star lanterns, Germany<br>*2025-12-21* | 
| [![High mountains, deep history](https://www.bing.com/th?id=OHR.BormioItaly_EN-US5324526286_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251220) | [![Layers of time in Utah](https://www.bing.com/th?id=OHR.CathedralValley_EN-US5270905846_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251219) | [![Fur, frost, and feast](https://www.bing.com/th?id=OHR.FrostySquirrel_EN-US5169660143_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251218) | 
| **[High mountains, deep history](https://bing.codexun.com/us/detail/20251220)**<br>Snow-covered landscape at Bormio, Lombardy, Italy<br>*2025-12-20* | **[Layers of time in Utah](https://bing.codexun.com/us/detail/20251219)**<br>Temple of the Sun, Capitol Reef National Park, Utah<br>*2025-12-19* | **[Fur, frost, and feast](https://bing.codexun.com/us/detail/20251218)**<br>Eurasian red squirrel in Northumberland, England<br>*2025-12-18* | 
| [![Tiny hats, big spirits](https://www.bing.com/th?id=OHR.ChristmasGnomes_EN-US5094302697_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251217) | [![Still waters, bright lights](https://www.bing.com/th?id=OHR.AmsterdamLights_EN-US4980559514_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251216) | [![The great holiday bird-off](https://www.bing.com/th?id=OHR.TuftedTitmouse_EN-US4835376471_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251215) | 
| **[Tiny hats, big spirits](https://bing.codexun.com/us/detail/20251217)**<br>Handmade gnomes at a Christmas market<br>*2025-12-17* | **[Still waters, bright lights](https://bing.codexun.com/us/detail/20251216)**<br>Lights on Spiegelgracht canal, Amsterdam, Netherlands<br>*2025-12-16* | **[The great holiday bird-off](https://bing.codexun.com/us/detail/20251215)**<br>Tufted titmouse perched on pine boughs, Massachusetts<br>*2025-12-15* | 
| [![Frozen reflections](https://www.bing.com/th?id=OHR.YosemiteWinter_EN-US4786605896_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251214) | [![The plant that paints the holidays red](https://www.bing.com/th?id=OHR.SpeckledPoinsettia_EN-US4098165068_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251213) | [![Where the sky meets Earth](https://www.bing.com/th?id=OHR.EverestGlow_EN-US6131667612_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251212) | 
| **[Frozen reflections](https://bing.codexun.com/us/detail/20251214)**<br>Merced River, Yosemite National Park, California<br>*2025-12-14* | **[The plant that paints the holidays red](https://bing.codexun.com/us/detail/20251213)**<br>Spotted poinsettia<br>*2025-12-13* | **[Where the sky meets Earth](https://bing.codexun.com/us/detail/20251212)**<br>Summit of Mount Everest at sunset, seen from Renjo La, Nepal<br>*2025-12-12* | 


---

## Wallpaper Archive by Year

### 2026
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 6px; margin: 12px 0;">
<a href="https://bing.codexun.com/us/archive/202601" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f3f4f6; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease; font-weight: 500;">202601</a>
</div>

### 2025
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 6px; margin: 12px 0;">
<a href="https://bing.codexun.com/us/archive/202512" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202512</a>
<a href="https://bing.codexun.com/us/archive/202511" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202511</a>
<a href="https://bing.codexun.com/us/archive/202510" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202510</a>
<a href="https://bing.codexun.com/us/archive/202509" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202509</a>
<a href="https://bing.codexun.com/us/archive/202508" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202508</a>
<a href="https://bing.codexun.com/us/archive/202507" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202507</a>
<a href="https://bing.codexun.com/us/archive/202506" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202506</a>
</div>



---