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

[![A taste of Pienza](https://www.bing.com/th?id=OHR.PienzaItaly_EN-US8831227247_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250929)

**A taste of Pienza**

Some towns evolve slowly over centuries. Pienza? It received a full rebrand in the 1400s from a pope who wanted to prove a point—and maybe show off a little. This tiny Italian town is perched above the Val d'Orcia, surrounded by rolling hills that look exactly like you think Tuscany should: cypress trees, winding dirt roads, the occasional sheep. It's peaceful. And then you step inside the town walls, and it gets clever.

*© zpagistock/Getty Images (Bing United States)*

---

## Recent 30 Days

| | | |
|:---:|:---:|:---:|
| [![A taste of Pienza](https://www.bing.com/th?id=OHR.PienzaItaly_EN-US8831227247_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250929) | [![Weeding and wishing](https://www.bing.com/th?id=OHR.TankLakes_EN-US9278332978_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250928) | [![The fast and the furriest](https://www.bing.com/th?id=OHR.AutumnChipmunk_EN-US9248365602_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250927) | 
| **[A taste of Pienza](https://bing.codexun.com/us/detail/20250929)**<br>Town of Pienza in Tuscany, Italy<br>*2025-09-29* | **[Weeding and wishing](https://bing.codexun.com/us/detail/20250928)**<br>Tank Lakes, Alpine Lakes Wilderness, Washington<br>*2025-09-28* | **[The fast and the furriest](https://bing.codexun.com/us/detail/20250927)**<br>Least chipmunk, Kootenai National Forest, Montana<br>*2025-09-27* | 
| [![Carved stones of courage](https://www.bing.com/th?id=OHR.FortChittorgarh_EN-US9184486139_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250926) | [![The lonely giant](https://www.bing.com/th?id=OHR.BearLodge_EN-US9061134971_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250925) | [![Beak-side story](https://www.bing.com/th?id=OHR.ToucanForest_EN-US8319635845_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250924) | 
| **[Carved stones of courage](https://bing.codexun.com/us/detail/20250926)**<br>Chittorgarh Fort, Rajasthan, India<br>*2025-09-26* | **[The lonely giant](https://bing.codexun.com/us/detail/20250925)**<br>Devils Tower National Monument, Wyoming<br>*2025-09-25* | **[Beak-side story](https://bing.codexun.com/us/detail/20250924)**<br>Keel-billed toucan in Costa Rica<br>*2025-09-24* | 
| [![Midway to winter](https://www.bing.com/th?id=OHR.AspenEquinox_EN-US8237887036_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250923) | [![Otterly cool](https://www.bing.com/th?id=OHR.IceOtters_EN-US7982442590_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250922) | [![A tale of brews and views](https://www.bing.com/th?id=OHR.OktoberfestSwing_EN-US7916182497_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250921) | 
| **[Midway to winter](https://bing.codexun.com/us/detail/20250923)**<br>Aspen trees during fall, Fishlake National Forest, Utah<br>*2025-09-23* | **[Otterly cool](https://bing.codexun.com/us/detail/20250922)**<br>Sea otters, Prince William Sound, Alaska<br>*2025-09-22* | **[A tale of brews and views](https://bing.codexun.com/us/detail/20250921)**<br>Swing carousel at Oktoberfest, Munich, Germany<br>*2025-09-21* | 
| [![A thousand reasons to visit](https://www.bing.com/th?id=OHR.ThousandIslands_EN-US7884567746_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250920) | [![Ireland's western edge](https://www.bing.com/th?id=OHR.DunquinIreland_EN-US9846056364_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250919) | [![A crown in the making](https://www.bing.com/th?id=OHR.YoungMoose_EN-US2991221135_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250918) | 
| **[A thousand reasons to visit](https://bing.codexun.com/us/detail/20250920)**<br>Thousand Islands region, St. Lawrence River, US-Canada border<br>*2025-09-20* | **[Ireland's western edge](https://bing.codexun.com/us/detail/20250919)**<br>Serpentine stairs of Dunquin Pier, County Kerry, Ireland<br>*2025-09-19* | **[A crown in the making](https://bing.codexun.com/us/detail/20250918)**<br>Young bull moose in Denali National Park, Alaska<br>*2025-09-18* | 
| [![A stratospheric success](https://www.bing.com/th?id=OHR.OzoneEarth_EN-US9728527733_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250917) | [![Vibrancy in every brick](https://www.bing.com/th?id=OHR.DallasLegorreta_EN-US9050675226_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250916) | [![Moss and mist](https://www.bing.com/th?id=OHR.HohWaterfall_EN-US9003533736_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250915) | 
| **[A stratospheric success](https://bing.codexun.com/us/detail/20250917)**<br>Nighttime view of the Gulf Coast states from 225 miles above Earth<br>*2025-09-17* | **[Vibrancy in every brick](https://bing.codexun.com/us/detail/20250916)**<br>Latino Cultural Center designed by Ricardo Legorreta, Dallas, Texas<br>*2025-09-16* | **[Moss and mist](https://bing.codexun.com/us/detail/20250915)**<br>A waterfall in Olympic National Park, Washington<br>*2025-09-15* | 
| [![Rugged and wild](https://www.bing.com/th?id=OHR.PointReyesSeashore_EN-US8949381326_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250914) | [![Swim wild, swim free](https://www.bing.com/th?id=OHR.SpinnerDolphins_EN-US8860882818_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250913) | [![In unity and remembrance](https://www.bing.com/th?id=OHR.LibertyManhattan_EN-US8781721086_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250912) | 
| **[Rugged and wild](https://bing.codexun.com/us/detail/20250914)**<br>Chimney Rock, Point Reyes National Seashore, California<br>*2025-09-14* | **[Swim wild, swim free](https://bing.codexun.com/us/detail/20250913)**<br>Spinner dolphin pod in the Red Sea, Marsa Alam, Egypt<br>*2025-09-13* | **[In unity and remembrance](https://bing.codexun.com/us/detail/20250912)**<br>Statue of Liberty and Lower Manhattan, New York City<br>*2025-09-12* | 
| [!['Hay' there!](https://www.bing.com/th?id=OHR.YorkshireHay_EN-US8523120193_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250911) | [![Twig by twig, she prepares](https://www.bing.com/th?id=OHR.SwissSquirrel_EN-US8185093853_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250910) | [![Booked for the day](https://www.bing.com/th?id=OHR.OrchardLibrary_EN-US8095609746_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250909) | 
| **['Hay' there!](https://bing.codexun.com/us/detail/20250911)**<br>Hay bales, North Yorkshire, England<br>*2025-09-11* | **[Twig by twig, she prepares](https://bing.codexun.com/us/detail/20250910)**<br>A female Eurasian red squirrel carrying moss, Switzerland<br>*2025-09-10* | **[Booked for the day](https://bing.codexun.com/us/detail/20250909)**<br>Library@orchard, Singapore<br>*2025-09-09* | 
| [![Pastel dreams and still waters](https://www.bing.com/th?id=OHR.BlueGdansk_EN-US8032283831_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250908) | [![A hum-dinger of a day](https://www.bing.com/th?id=OHR.RufousHummer_EN-US7346003108_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250907) | [![A pier-fect evening](https://www.bing.com/th?id=OHR.SunsetPier_EN-US7261804528_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250906) | 
| **[Pastel dreams and still waters](https://bing.codexun.com/us/detail/20250908)**<br>Gdańsk on the banks of the Motława, Poland<br>*2025-09-08* | **[A hum-dinger of a day](https://bing.codexun.com/us/detail/20250907)**<br>Rufous hummingbird, Golden Gate Park, San Francisco, California<br>*2025-09-07* | **[A pier-fect evening](https://bing.codexun.com/us/detail/20250906)**<br>Pacific Park at Santa Monica State Beach, California<br>*2025-09-06* | 
| [![Bear with us—it's National Wildlife Day](https://www.bing.com/th?id=OHR.WrestlingBears_EN-US4338158114_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250905) | [![Protected stillness](https://www.bing.com/th?id=OHR.MinnesotaWaters_EN-US4282198656_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250904) | [![Ghosts of Deadvlei](https://www.bing.com/th?id=OHR.DeadvleiTrees_EN-US4233800313_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250903) | 
| **[Bear with us—it's National Wildlife Day](https://bing.codexun.com/us/detail/20250905)**<br>Grizzly bears wrestling, Katmai National Park and Preserve, Alaska<br>*2025-09-05* | **[Protected stillness](https://bing.codexun.com/us/detail/20250904)**<br>Boundary Waters Canoe Area Wilderness, Minnesota<br>*2025-09-04* | **[Ghosts of Deadvlei](https://bing.codexun.com/us/detail/20250903)**<br>Camel thorn trees, Deadvlei, Namib-Naukluft Park, Namibia<br>*2025-09-03* | 
| [![Stitched into history](https://www.bing.com/th?id=OHR.LaborDayChicago_EN-US3947410593_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250902) | [![Painted clouds, still cliffs](https://www.bing.com/th?id=OHR.ScottsBluff_EN-US3893566724_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250901) | [![Finned and fabulous](https://www.bing.com/th?id=OHR.MaldivesWhaleShark_EN-US3819740955_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250831) | 
| **[Stitched into history](https://bing.codexun.com/us/detail/20250902)**<br>Amalgamated Clothing Workers of America in a Labor Day parade, May 1915, Chicago<br>*2025-09-02* | **[Painted clouds, still cliffs](https://bing.codexun.com/us/detail/20250901)**<br>Scotts Bluff National Monument in Gering, Nebraska<br>*2025-09-01* | **[Finned and fabulous](https://bing.codexun.com/us/detail/20250831)**<br>Whale shark off the coast of Alifu Dhaalu Atoll, Maldives<br>*2025-08-31* | 


---

## Wallpaper Archive by Year

### 2025
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 6px; margin: 12px 0;">
<a href="https://bing.codexun.com/us/archive/202509" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f3f4f6; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease; font-weight: 500;">202509</a>
<a href="https://bing.codexun.com/us/archive/202508" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202508</a>
<a href="https://bing.codexun.com/us/archive/202507" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202507</a>
<a href="https://bing.codexun.com/us/archive/202506" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202506</a>
</div>



---