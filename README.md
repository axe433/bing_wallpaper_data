# Bing Wallpaper Data Crawler and Markdown Generator

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

## 📖 Documentation

- [中文文档 (Chinese Documentation)](README_CN.md)
- [English Documentation](README.md)

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

[![All for falls and falls for all](https://www.bing.com/th?id=OHR.IguazuArgentina_EN-US5953375078_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250809)

**All for falls and falls for all**

No voice is loud enough to drown out the roar of Iguazú Falls. But it's not just the sound. The sheer presence of this natural wonder is overwhelming as it straddles the border between Argentina and Brazil. This vast waterfall system stretches nearly 2 miles and features more than 270 individual cascades, each offering a unique display of tumbling water and shimmering mist.

*© Mark Meredith/Getty Images (Bing United States)*

---

## Recent 30 Days

| | | |
|:---:|:---:|:---:|
| [![All for falls and falls for all](https://www.bing.com/th?id=OHR.IguazuArgentina_EN-US5953375078_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250809) | [![Code of the coastline](https://www.bing.com/th?id=OHR.GasparillaLight_EN-US0554204214_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250808) | [![Off the grid](https://www.bing.com/th?id=OHR.NaPaliKauai_EN-US7451684312_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250807) | 
| **[All for falls and falls for all](https://bing.codexun.com/us/detail/20250809)**<br>Three Musketeers Falls at Iguazú Falls, Argentina<br>*2025-08-09* | **[Code of the coastline](https://bing.codexun.com/us/detail/20250808)**<br>Gasparilla Island Rear Range Light, Boca Grande, Florida<br>*2025-08-08* | **[Off the grid](https://bing.codexun.com/us/detail/20250807)**<br>Kalalau Beach on the Nā Pali Coast, Kauai, Hawaii<br>*2025-08-07* | 
| [![Tide and seek](https://www.bing.com/th?id=OHR.CaliforniaTidepool_EN-US9089576317_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250806) | [![Whooo's home?](https://www.bing.com/th?id=OHR.LaplandOwl_EN-US8965493818_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250805) | [![Hello yellow!](https://www.bing.com/th?id=OHR.HappySunflower_EN-US8791544241_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250804) | 
| **[Tide and seek](https://bing.codexun.com/us/detail/20250806)**<br>Tide pools in La Jolla, California<br>*2025-08-06* | **[Whooo's home?](https://bing.codexun.com/us/detail/20250805)**<br>Great gray owls in their nest, Finland<br>*2025-08-05* | **[Hello yellow!](https://bing.codexun.com/us/detail/20250804)**<br>Sunflowers in a field in summer<br>*2025-08-04* | 
| [![Age-old storyboard](https://www.bing.com/th?id=OHR.FruitaPetroglyphs_EN-US8712481828_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250803) | [![Expect the unexpected](https://www.bing.com/th?id=OHR.EdinburghFringe_EN-US5923216873_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250802) | [![Madagascar native](https://www.bing.com/th?id=OHR.BabyLemur_EN-US9264861498_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250801) | 
| **[Age-old storyboard](https://bing.codexun.com/us/detail/20250803)**<br>Petroglyphs near Fruita in Capitol Reef National Park, Utah<br>*2025-08-03* | **[Expect the unexpected](https://bing.codexun.com/us/detail/20250802)**<br>Royal Mile, Edinburgh, Scotland<br>*2025-08-02* | **[Madagascar native](https://bing.codexun.com/us/detail/20250801)**<br>Ring-tailed lemur infant playing with its own tail, Madagascar<br>*2025-08-01* | 
| [![Friendship without borders](https://www.bing.com/th?id=OHR.SaypeDubai_EN-US5078679271_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250731) | [![The jungle queen](https://www.bing.com/th?id=OHR.TigerDay_EN-US5038876410_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250730) | [![A steppe ahead](https://www.bing.com/th?id=OHR.MongoliaYurts_EN-US1803457525_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250729) | 
| **[Friendship without borders](https://bing.codexun.com/us/detail/20250731)**<br>'Beyond Walls' land-art installation by Saype at Expo 2020 Dubai, United Arab Emirates<br>*2025-07-31* | **[The jungle queen](https://bing.codexun.com/us/detail/20250730)**<br>Female Bengal tiger, Kanha National Park, India<br>*2025-07-30* | **[A steppe ahead](https://bing.codexun.com/us/detail/20250729)**<br>Yurts in the grasslands of Mongolia<br>*2025-07-29* | 
| [![Shimmer in sync](https://www.bing.com/th?id=OHR.BlackfinBarracuda_EN-US1227116811_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250728) | [![Sentinels of the tide](https://www.bing.com/th?id=OHR.MangroveTwilight_EN-US0646432423_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250727) | [![Canvas of life](https://www.bing.com/th?id=OHR.LasPalmas_EN-US0568727017_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250726) | 
| **[Shimmer in sync](https://bing.codexun.com/us/detail/20250728)**<br>School of blackfin barracuda, Shark Reef, Ras Mohammed National Park, Sinai Peninsula, Egypt<br>*2025-07-28* | **[Sentinels of the tide](https://bing.codexun.com/us/detail/20250727)**<br>Mangrove trees at twilight, Walakiri Beach, island of Sumba, Indonesia<br>*2025-07-27* | **[Canvas of life](https://bing.codexun.com/us/detail/20250726)**<br>Aerial view of colorful houses, Las Palmas de Gran Canaria, Spain<br>*2025-07-26* | 
| [![Sticking together](https://www.bing.com/th?id=OHR.AshyWoodswallow_EN-US7005770998_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250725) | [![A country within a city](https://www.bing.com/th?id=OHR.VaticanCity_EN-US5915643866_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250724) | [![Epic sunsets and ancient secrets](https://www.bing.com/th?id=OHR.BadlandsSunset_EN-US5821746223_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250723) | 
| **[Sticking together](https://bing.codexun.com/us/detail/20250725)**<br>Family of ashy woodswallows perched on a branch in Thailand<br>*2025-07-25* | **[A country within a city](https://bing.codexun.com/us/detail/20250724)**<br>Vatican City with St. Peter's Basilica<br>*2025-07-24* | **[Epic sunsets and ancient secrets](https://bing.codexun.com/us/detail/20250723)**<br>Sunset over Badlands National Park, South Dakota<br>*2025-07-23* | 
| [![Rainforests of the sea](https://www.bing.com/th?id=OHR.AcroporaReef_EN-US5567789372_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250722) | [![Dancing in the moonlight](https://www.bing.com/th?id=OHR.BigMoon_EN-US5436003142_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250721) | [![Moth-ers day](https://www.bing.com/th?id=OHR.MothWeek_EN-US5360572836_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250720) | 
| **[Rainforests of the sea](https://bing.codexun.com/us/detail/20250722)**<br>Staghorn coral off the island of Bonaire, Caribbean Netherlands<br>*2025-07-22* | **[Dancing in the moonlight](https://bing.codexun.com/us/detail/20250721)**<br>The moon's surface photographed through a telescope<br>*2025-07-21* | **[Moth-ers day](https://bing.codexun.com/us/detail/20250720)**<br>Luna moth resting on cedar elm, New Braunfels, Texas, USA<br>*2025-07-20* | 
| [![Gulf Islands glow](https://www.bing.com/th?id=OHR.FloridaSeashore_EN-US9038929616_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250719) | [![Fragrant horizons](https://www.bing.com/th?id=OHR.FranceLavender_EN-US5224253118_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250718) | [![Illuminated by Isis](https://www.bing.com/th?id=OHR.TemplePhilae_EN-US5062419351_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250717) | 
| **[Gulf Islands glow](https://bing.codexun.com/us/detail/20250719)**<br>Beach at sunrise, Gulf Islands National Seashore, Florida<br>*2025-07-19* | **[Fragrant horizons](https://bing.codexun.com/us/detail/20250718)**<br>Lavender fields in Plateau de Valensole, France<br>*2025-07-18* | **[Illuminated by Isis](https://bing.codexun.com/us/detail/20250717)**<br>Temple of Philae<br>*2025-07-17* | 
| [![Timeless glow](https://www.bing.com/th?id=OHR.PerseidsPine_EN-US4826682211_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250716) | [![Chasing waves](https://www.bing.com/th?id=OHR.YoungShark_EN-US4689572794_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250715) | [![Rockin' those layers](https://www.bing.com/th?id=OHR.BasaltColumns_EN-US4476950150_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250714) | 
| **[Timeless glow](https://bing.codexun.com/us/detail/20250716)**<br>Perseid meteor shower and an ancient bristlecone pine, Great Basin National Park, Nevada<br>*2025-07-16* | **[Chasing waves](https://bing.codexun.com/us/detail/20250715)**<br>Young blue shark swimming off the coast of Galicia, Spain<br>*2025-07-15* | **[Rockin' those layers](https://bing.codexun.com/us/detail/20250714)**<br>Basalt columns at Kálfshamarsvík, Skagi Peninsula, Iceland<br>*2025-07-14* | 
| [![Following mom's lead](https://www.bing.com/th?id=OHR.ThomsonGazelle_EN-US4354285846_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250713) | [![Counting us all in](https://www.bing.com/th?id=OHR.TokyoSunrise_EN-US4269783992_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250712) | [![To the waves of freedom](https://www.bing.com/th?id=OHR.BahamaBlues_EN-US1367794856_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250711) | 
| **[Following mom's lead](https://bing.codexun.com/us/detail/20250713)**<br>Thomson's gazelle mother and fawn, Maasai Mara, Kenya<br>*2025-07-13* | **[Counting us all in](https://bing.codexun.com/us/detail/20250712)**<br>Tokyo at sunrise<br>*2025-07-12* | **[To the waves of freedom](https://bing.codexun.com/us/detail/20250711)**<br>Turquoise waters of the Bahamas<br>*2025-07-11* | 


---

## Wallpaper Archive by Year

### 2025
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 6px; margin: 12px 0;">
<a href="https://bing.codexun.com/us/archive/202508" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f3f4f6; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease; font-weight: 500;">202508</a>
<a href="https://bing.codexun.com/us/archive/202507" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202507</a>
<a href="https://bing.codexun.com/us/archive/202506" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202506</a>
</div>



---