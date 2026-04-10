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

[![Plotting paws](https://www.bing.com/th?id=OHR.FoxSiblings_EN-US7533678992_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260411)

**Plotting paws**

Ever caught siblings plotting? In Karula National Park, Estonia, it looks as though these two red fox kits froze mid-conspiracy, their expressions mirrored in curiosity and caution. They're not just springtime fluff; they're apprentices in survival. Born in litters averaging four to six kits, foxes grow quickly, their underground den becoming their wrestling ring, classroom, and testing ground. Older kits often help feed, guard, and teach the younger ones, turning play into practice and mischief into muscle memory. In their families, siblings are not background—they're backup.

*© Sven Zacek/Nature Picture Library (Bing United States)*

---

## Recent 30 Days

| | | |
|:---:|:---:|:---:|
| [![Plotting paws](https://www.bing.com/th?id=OHR.FoxSiblings_EN-US7533678992_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260411) | [![Veil of light](https://www.bing.com/th?id=OHR.WalesWaterfall_EN-US7187055503_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260410) | [![The Emerald City](https://www.bing.com/th?id=OHR.SeattleSunrise_EN-US6729754002_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260409) | 
| **[Plotting paws](https://bing.codexun.com/us/detail/20260411)**<br>Two young red foxes at Karula National Park, Estonia<br>*2026-04-11* | **[Veil of light](https://bing.codexun.com/us/detail/20260410)**<br>Sgwd yr Eira waterfall, Bannau Brycheiniog National Park, Wales<br>*2026-04-10* | **[The Emerald City](https://bing.codexun.com/us/detail/20260409)**<br>Seattle, Washington<br>*2026-04-09* | 
| [![One stick at a time](https://www.bing.com/th?id=OHR.BeaverPortrait_EN-US6459336252_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260408) | [![Where power resides](https://www.bing.com/th?id=OHR.CastleBlossoms_EN-US6202844131_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260407) | [![Hello, Easter Sunday](https://www.bing.com/th?id=OHR.LithuaniaEggs_EN-US5074250791_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260406) | 
| **[One stick at a time](https://bing.codexun.com/us/detail/20260408)**<br>Beaver, Germany<br>*2026-04-08* | **[Where power resides](https://bing.codexun.com/us/detail/20260407)**<br>Hirosaki Castle with cherry blossoms, Hirosaki, Japan<br>*2026-04-07* | **[Hello, Easter Sunday](https://bing.codexun.com/us/detail/20260406)**<br>Colorful handmade wooden Easter eggs, Vilnius, Lithuania<br>*2026-04-06* | 
| [![The lek side story](https://www.bing.com/th?id=OHR.GrouseGuff_EN-US4212457538_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260405) | [![Bridging the gap, one arm at a time](https://www.bing.com/th?id=OHR.ArmbrugBridge_EN-US3302230248_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260404) | [![Patterns of spring](https://www.bing.com/th?id=OHR.WildflowerValley_EN-US6579657743_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260403) | 
| **[The lek side story](https://bing.codexun.com/us/detail/20260405)**<br>Black grouse males facing off on a lekking site, Estonia<br>*2026-04-05* | **[Bridging the gap, one arm at a time](https://bing.codexun.com/us/detail/20260404)**<br>Armbrug bridge, Amsterdam, Netherlands<br>*2026-04-04* | **[Patterns of spring](https://bing.codexun.com/us/detail/20260403)**<br>Wildflower bloom, Central Valley, California<br>*2026-04-03* | 
| [![Hopping into April](https://www.bing.com/th?id=OHR.JapaneseTreeFrog_EN-US6527297660_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260402) | [![Underground paradise](https://www.bing.com/th?id=OHR.ParadiseCave_EN-US6470755729_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260401) | [![Elegance in motion](https://www.bing.com/th?id=OHR.IndiaCranes_EN-US6414900321_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260331) | 
| **[Hopping into April](https://bing.codexun.com/us/detail/20260402)**<br>Japanese tree frog in a pink morning glory<br>*2026-04-02* | **[Underground paradise](https://bing.codexun.com/us/detail/20260401)**<br>Paradise Cave, Phong Nha-Ke Bang National Park, Vietnam<br>*2026-04-01* | **[Elegance in motion](https://bing.codexun.com/us/detail/20260331)**<br>Demoiselle cranes, India<br>*2026-03-31* | 
| [![Serenity by the sea](https://www.bing.com/th?id=OHR.PeggysLighthouse_EN-US6365734559_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260330) | [![The untamed spirit](https://www.bing.com/th?id=OHR.CapeBuffalo_EN-US6304011521_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260329) | [![Still burning bright](https://www.bing.com/th?id=OHR.RadioCityHall_EN-US6218301556_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260328) | 
| **[Serenity by the sea](https://bing.codexun.com/us/detail/20260330)**<br>Peggy's Point Lighthouse, Atlantic Coast, Nova Scotia, Canada<br>*2026-03-30* | **[The untamed spirit](https://bing.codexun.com/us/detail/20260329)**<br>African buffalo, Ngorongoro Crater, Tanzania<br>*2026-03-29* | **[Still burning bright](https://bing.codexun.com/us/detail/20260328)**<br>Radio City Music Hall in New York City<br>*2026-03-28* | 
| [![A step above the wild](https://www.bing.com/th?id=OHR.LoganCreek_EN-US6075548781_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260327) | [![The secret life of manatees](https://www.bing.com/th?id=OHR.ManateeSpring_EN-US1203685327_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260326) | [![The shape of spring](https://www.bing.com/th?id=OHR.WuhanCherryBlossom_EN-US5963967452_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260325) | 
| **[A step above the wild](https://bing.codexun.com/us/detail/20260327)**<br>Logan Creek Suspension Bridge, West Coast Trail, Canada<br>*2026-03-27* | **[The secret life of manatees](https://bing.codexun.com/us/detail/20260326)**<br>Juvenile manatees in a freshwater spring, Crystal River, Florida<br>*2026-03-26* | **[The shape of spring](https://bing.codexun.com/us/detail/20260325)**<br>Cherry blossoms at East Lake Cherry Blossom Park, Wuhan, China<br>*2026-03-25* | 
| [![Guided by the weather](https://www.bing.com/th?id=OHR.SonoranStorm_EN-US5792303901_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260324) | [![When water draws the line](https://www.bing.com/th?id=OHR.TanganyikaWater_EN-US5685685365_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260323) | [![Where roots run wild](https://www.bing.com/th?id=OHR.LeteaForest_EN-US5404369914_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260322) | 
| **[Guided by the weather](https://bing.codexun.com/us/detail/20260324)**<br>Lightning storm over saguaro cacti, Sonoran Desert, Arizona<br>*2026-03-24* | **[When water draws the line](https://bing.codexun.com/us/detail/20260323)**<br>Lake Tanganyika, Africa<br>*2026-03-23* | **[Where roots run wild](https://bing.codexun.com/us/detail/20260322)**<br>Letea Forest, Danube Delta, Romania<br>*2026-03-22* | 
| [![The quiet bloom of change](https://www.bing.com/th?id=OHR.SpringSnowdrops_EN-US5032204696_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260321) | [![Spike your curiosity](https://www.bing.com/th?id=OHR.EchidnaAustralia_EN-US7660451296_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260320) | [![Urban blooms](https://www.bing.com/th?id=OHR.PortlandBlossoms_EN-US7604107803_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260319) | 
| **[The quiet bloom of change](https://bing.codexun.com/us/detail/20260321)**<br>Snowdrops in spring<br>*2026-03-21* | **[Spike your curiosity](https://bing.codexun.com/us/detail/20260320)**<br>Short-beaked echidna, Adelaide Hills, Australia<br>*2026-03-20* | **[Urban blooms](https://bing.codexun.com/us/detail/20260319)**<br>Cherry blossoms at Tom McCall Waterfront Park, Portland, Oregon<br>*2026-03-19* | 
| [![Ireland's spiritual crossroads](https://www.bing.com/th?id=OHR.DonegalFort_EN-US7529893132_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260318) | [![Into the Pandaverse](https://www.bing.com/th?id=OHR.PandaForest_EN-US7436757535_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260317) | [![Passing through, making waves](https://www.bing.com/th?id=OHR.PacificRimNP_EN-US7242831009_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260316) | 
| **[Ireland's spiritual crossroads](https://bing.codexun.com/us/detail/20260318)**<br>Grianan of Aileach ring fort, Donegal, Ireland<br>*2026-03-18* | **[Into the Pandaverse](https://bing.codexun.com/us/detail/20260317)**<br>Giant panda eating bamboo, China<br>*2026-03-17* | **[Passing through, making waves](https://bing.codexun.com/us/detail/20260316)**<br>Pacific Rim National Park Reserve, Vancouver Island, Canada<br>*2026-03-16* | 
| [![An ancient angle on Pi](https://www.bing.com/th?id=OHR.CornwallDolmen_EN-US7192709883_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260315) | [![A quiet masterpiece in stone](https://www.bing.com/th?id=OHR.VendeeVaults_EN-US7120114878_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260314) | [![Wings in rehearsal](https://www.bing.com/th?id=OHR.SunbitternEcuador_EN-US7059069378_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260313) | 
| **[An ancient angle on Pi](https://bing.codexun.com/us/detail/20260315)**<br>Lanyon Quoit, a Neolithic dolmen in Cornwall, England<br>*2026-03-15* | **[A quiet masterpiece in stone](https://bing.codexun.com/us/detail/20260314)**<br>Vaults of the Church of Notre Dame de Bon-Port, Les Sables-d'Olonne, France<br>*2026-03-14* | **[Wings in rehearsal](https://bing.codexun.com/us/detail/20260313)**<br>Juvenile sunbittern displaying at nest, Ecuador<br>*2026-03-13* | 


---

## Wallpaper Archive by Year

### 2026
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 6px; margin: 12px 0;">
<a href="https://bing.codexun.com/us/archive/202604" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f3f4f6; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease; font-weight: 500;">202604</a>
<a href="https://bing.codexun.com/us/archive/202603" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202603</a>
<a href="https://bing.codexun.com/us/archive/202602" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202602</a>
<a href="https://bing.codexun.com/us/archive/202601" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202601</a>
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