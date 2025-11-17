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

[![The trails' call](https://www.bing.com/th?id=OHR.ShenandoahTrail_EN-US8964689271_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251118)

**The trails' call**

National Take a Hike Day is more than a date—it's an invitation to step away from screens and into the rhythm of nature. Created by the American Hiking Society, this day celebrates the simple act of walking under open skies and reminds us that health and happiness often begin with a single stride. Across 60,000 miles of US trails, hikers rediscover the quiet magic of forests, the strength in their own breath, and the promise of unspoiled landscapes.

*© Michael Ver Sprill/Getty Images (Bing United States)*

---

## Recent 30 Days

| | | |
|:---:|:---:|:---:|
| [![The trails' call](https://www.bing.com/th?id=OHR.ShenandoahTrail_EN-US8964689271_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251118) | [![Passages with a past](https://www.bing.com/th?id=OHR.LyonTraboules_EN-US9432784340_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251117) | [![Bend it like Nikko](https://www.bing.com/th?id=OHR.IrohazakaAutumn_EN-US9137140715_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251116) | 
| **[The trails' call](https://bing.codexun.com/us/detail/20251118)**<br>Fall colors in Shenandoah National Park, Virginia<br>*2025-11-18* | **[Passages with a past](https://bing.codexun.com/us/detail/20251117)**<br>A traboule in Lyon, France<br>*2025-11-17* | **[Bend it like Nikko](https://bing.codexun.com/us/detail/20251116)**<br>Irohazaka Road in fall, Nikko, Tochigi, Japan<br>*2025-11-16* | 
| [![A slow reminder for a fast world](https://www.bing.com/th?id=OHR.ManateeBaby_EN-US5594953777_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251115) | [![Quivering under starlight](https://www.bing.com/th?id=OHR.AloeDichotoma_EN-US6966316373_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251114) | [![All roads lead to Rome](https://www.bing.com/th?id=OHR.ColosseumRome_EN-US6932882124_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251113) | 
| **[A slow reminder for a fast world](https://bing.codexun.com/us/detail/20251115)**<br>Mother manatee and calf, Crystal River, Florida<br>*2025-11-15* | **[Quivering under starlight](https://bing.codexun.com/us/detail/20251114)**<br>Quiver trees under the Milky Way, Keetmanshoop, Namibia<br>*2025-11-14* | **[All roads lead to Rome](https://bing.codexun.com/us/detail/20251113)**<br>Aerial view of the Colosseum, Rome, Italy<br>*2025-11-13* | 
| [![Honoring their service](https://www.bing.com/th?id=OHR.MarineMemorial_EN-US6899836690_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251112) | [![Life hidden beneath the prairie](https://www.bing.com/th?id=OHR.PrairieDogTown_EN-US6854295076_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251111) | [![Once upon a star](https://www.bing.com/th?id=OHR.LagoonNebula_EN-US7186308623_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251110) | 
| **[Honoring their service](https://bing.codexun.com/us/detail/20251112)**<br>Marine Corps War Memorial, Arlington, Virginia<br>*2025-11-12* | **[Life hidden beneath the prairie](https://bing.codexun.com/us/detail/20251111)**<br>Black-tailed prairie dogs at Roberts Prairie Dog Town, Badlands National Park, South Dakota<br>*2025-11-11* | **[Once upon a star](https://bing.codexun.com/us/detail/20251110)**<br>Interstellar clouds in the Lagoon Nebula, captured by the Hubble Space Telescope<br>*2025-11-10* | 
| [![Rock stars of Bandon](https://www.bing.com/th?id=OHR.BandonBeach_EN-US7099626478_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251109) | [![Week of the white bear](https://www.bing.com/th?id=OHR.WillowBear_EN-US6995170630_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251108) | [![Sky full of wishes](https://www.bing.com/th?id=OHR.LanternsThailand_EN-US6955074347_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251107) | 
| **[Rock stars of Bandon](https://bing.codexun.com/us/detail/20251109)**<br>Sea stacks of Bandon Beach in Bandon, Oregon<br>*2025-11-09* | **[Week of the white bear](https://bing.codexun.com/us/detail/20251108)**<br>Polar bear in Churchill, Manitoba, Canada<br>*2025-11-08* | **[Sky full of wishes](https://bing.codexun.com/us/detail/20251107)**<br>Colorful lanterns at the temple of Wat Phra That Hariphunchai, Lamphun, Thailand<br>*2025-11-07* | 
| [![Orange you glad it's fall?](https://www.bing.com/th?id=OHR.MoncayoAutumn_EN-US1753631441_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251106) | [![Mind the gap—this one opens](https://www.bing.com/th?id=OHR.TowerBridgeUK_EN-US6871236865_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251105) | [![Just jellin'](https://www.bing.com/th?id=OHR.MexicoJelly_EN-US6803524310_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251104) | 
| **[Orange you glad it's fall?](https://bing.codexun.com/us/detail/20251106)**<br>Peña Roya beech forest, Moncayo Natural Park, Zaragoza, Aragon, Spain<br>*2025-11-06* | **[Mind the gap—this one opens](https://bing.codexun.com/us/detail/20251105)**<br>Tower Bridge, London, England<br>*2025-11-05* | **[Just jellin'](https://bing.codexun.com/us/detail/20251104)**<br>Jellyfish swimming in the Pacific, Guerrero, Mexico<br>*2025-11-04* | 
| [![Where bamboo breathes and maples blaze](https://www.bing.com/th?id=OHR.KyotoMaple_EN-US6732403492_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251103) | [![Herds of heritage](https://www.bing.com/th?id=OHR.BisonSprings_EN-US6080228013_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251102) | [![Under the Halloween spell](https://www.bing.com/th?id=OHR.BranCastle_EN-US5914201029_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251101) | 
| **[Where bamboo breathes and maples blaze](https://bing.codexun.com/us/detail/20251103)**<br>Colorful maple leaves and bamboo forest in Arashiyama, Kyoto, Japan<br>*2025-11-03* | **[Herds of heritage](https://bing.codexun.com/us/detail/20251102)**<br>Bison grazing at thermal hot springs, Yellowstone National Park, Wyoming<br>*2025-11-02* | **[Under the Halloween spell](https://bing.codexun.com/us/detail/20251101)**<br>Entrance of Bran Castle in Bran, Brașov, Romania<br>*2025-11-01* | 
| [![Hooves, hues, and heritage](https://www.bing.com/th?id=OHR.PushkarFair_EN-US4430814252_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251031) | [![Rooted in time](https://www.bing.com/th?id=OHR.FanalForest_EN-US4405104404_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251030) | [![A gateway to stone wonders](https://www.bing.com/th?id=OHR.TepliceRocks_EN-US4098225022_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251029) | 
| **[Hooves, hues, and heritage](https://bing.codexun.com/us/detail/20251031)**<br>Camels at Jaisalmer, Rajasthan, India<br>*2025-10-31* | **[Rooted in time](https://bing.codexun.com/us/detail/20251030)**<br>Ancient til trees in Fanal Forest, island of Madeira, Portugal<br>*2025-10-30* | **[A gateway to stone wonders](https://bing.codexun.com/us/detail/20251029)**<br>The Gothic Gate in the Adršpach-Teplice Rocks, Czechia<br>*2025-10-29* | 
| [![Bigger, bolder, beakier](https://www.bing.com/th?id=OHR.AfricanRaven_EN-US4057369898_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251028) | [![Oh my gourd, it's today!](https://www.bing.com/th?id=OHR.PumpkinFarm_EN-US3773448576_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251027) | [![Finland's living peatland](https://www.bing.com/th?id=OHR.MartimoaapaFinland_EN-US3685817058_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251026) | 
| **[Bigger, bolder, beakier](https://bing.codexun.com/us/detail/20251028)**<br>Thick-billed raven, Simien Mountains, Ethiopia<br>*2025-10-28* | **[Oh my gourd, it's today!](https://bing.codexun.com/us/detail/20251027)**<br>Pumpkin farm in North Carolina<br>*2025-10-27* | **[Finland's living peatland](https://bing.codexun.com/us/detail/20251026)**<br>Aerial view of peatland in Martimoaapa Mire Reserve, Finland<br>*2025-10-26* | 
| [![From 'Grey Ghost' to ghost stories](https://www.bing.com/th?id=OHR.QueenMary_EN-US3331250680_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251025) | [![Snow much love](https://www.bing.com/th?id=OHR.SnowLeopard_EN-US3294064537_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251024) | [![Set in stone](https://www.bing.com/th?id=OHR.BulgariaRocks_EN-US3184562282_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251023) | 
| **[From 'Grey Ghost' to ghost stories](https://bing.codexun.com/us/detail/20251025)**<br>Night view of the RMS Queen Mary, Long Beach, California<br>*2025-10-25* | **[Snow much love](https://bing.codexun.com/us/detail/20251024)**<br>Snow leopard with her cubs, Spiti Valley, Cold Desert Biosphere Reserve, India<br>*2025-10-24* | **[Set in stone](https://bing.codexun.com/us/detail/20251023)**<br>Belogradchik Rocks, Bulgaria<br>*2025-10-23* | 
| [![Glowing traditions](https://www.bing.com/th?id=OHR.DiyaDiwali_EN-US3108369974_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251022) | [![Life in the slow lane](https://www.bing.com/th?id=OHR.HoffmansSloth_EN-US3030106938_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251021) | [![Sweet on science](https://www.bing.com/th?id=OHR.AppleHarvest_EN-US2977882687_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251020) | 
| **[Glowing traditions](https://bing.codexun.com/us/detail/20251022)**<br>A diya at the Golden Temple during Diwali, Amritsar, India<br>*2025-10-22* | **[Life in the slow lane](https://bing.codexun.com/us/detail/20251021)**<br>A Hoffmann's two-toed sloth in Ecuador<br>*2025-10-21* | **[Sweet on science](https://bing.codexun.com/us/detail/20251020)**<br>Apples ready for harvest, Minnesota<br>*2025-10-20* | 


---

## Wallpaper Archive by Year

### 2025
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 6px; margin: 12px 0;">
<a href="https://bing.codexun.com/us/archive/202511" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f3f4f6; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease; font-weight: 500;">202511</a>
<a href="https://bing.codexun.com/us/archive/202510" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202510</a>
<a href="https://bing.codexun.com/us/archive/202509" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202509</a>
<a href="https://bing.codexun.com/us/archive/202508" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202508</a>
<a href="https://bing.codexun.com/us/archive/202507" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202507</a>
<a href="https://bing.codexun.com/us/archive/202506" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202506</a>
</div>



---