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

[![Small footprint, big impact](https://www.bing.com/th?id=OHR.CoralAwareness_EN-US1824657819_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260723)

**Small footprint, big impact**

Imagine a city built by animals, glowing in the sunlight, and bustling with life beneath the waves. That is a coral reef. During Coral Reef Awareness Week, we celebrate these remarkable ecosystems and the countless species that depend on them.

*© SergeUWPhoto/Shutterstock (Bing United States)*

---

## Recent 30 Days

| | | |
|:---:|:---:|:---:|
| [![Small footprint, big impact](https://www.bing.com/th?id=OHR.CoralAwareness_EN-US1824657819_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260723) | [![Hidden in plain arch](https://www.bing.com/th?id=OHR.SantaCatalina_EN-US1116829215_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260722) | [![The lunar perspective](https://www.bing.com/th?id=OHR.Artemis_EN-US0683925849_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260721) | 
| **[Small footprint, big impact](https://bing.codexun.com/us/detail/20260723)**<br>Coral reef and beach in Raja Ampat, Indonesia<br>*2026-07-23* | **[Hidden in plain arch](https://bing.codexun.com/us/detail/20260722)**<br>Santa Catalina Arch, Antigua, Guatemala<br>*2026-07-22* | **[The lunar perspective](https://bing.codexun.com/us/detail/20260721)**<br>Moon and Earth captured by the Artemis II crew<br>*2026-07-21* | 
| [![Wings at rest](https://www.bing.com/th?id=OHR.HirundoRustica_EN-US3193611104_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260720) | [![Going full circle](https://www.bing.com/th?id=OHR.DevilsBridge_EN-US3505962815_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260719) | [![A Greek escape](https://www.bing.com/th?id=OHR.VaiUmbrellas_EN-US8985051242_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260718) | 
| **[Wings at rest](https://bing.codexun.com/us/detail/20260720)**<br>Barn swallows of different subspecies resting together<br>*2026-07-20* | **[Going full circle](https://bing.codexun.com/us/detail/20260719)**<br>Devil's Bridge in Rhododendron Park Kromlau, Saxony, Germany<br>*2026-07-19* | **[A Greek escape](https://bing.codexun.com/us/detail/20260718)**<br>Sunbeds on the beach at Vai, Crete, Greece<br>*2026-07-18* | 
| [![A waterfront chameleon](https://www.bing.com/th?id=OHR.NavyPier_EN-US1069960047_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260717) | [![The reward after the climb](https://www.bing.com/th?id=OHR.MarieLake_EN-US0365186943_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260716) | [![Fin-tastic truths](https://www.bing.com/th?id=OHR.LemonShark_EN-US9828936448_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260715) | 
| **[A waterfront chameleon](https://bing.codexun.com/us/detail/20260717)**<br>Navy Pier, Chicago, Illinois<br>*2026-07-17* | **[The reward after the climb](https://bing.codexun.com/us/detail/20260716)**<br>Marie Lake, John Muir Wilderness near Bishop, California<br>*2026-07-16* | **[Fin-tastic truths](https://bing.codexun.com/us/detail/20260715)**<br>Lemon shark pup in mangrove forest, Eleuthera, Bahamas<br>*2026-07-15* | 
| [![Born to rock](https://www.bing.com/th?id=OHR.NavajoSandstone_EN-US9496264383_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260714) | [![A wilder side of Maine](https://www.bing.com/th?id=OHR.KatahdinWWNM_EN-US8982810797_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260713) | [![Where Brittany meets the tide](https://www.bing.com/th?id=OHR.AurayBrittany_EN-US7890619884_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260712) | 
| **[Born to rock](https://bing.codexun.com/us/detail/20260714)**<br>Antelope Canyon on the Navajo Nation, east of Page, Arizona<br>*2026-07-14* | **[A wilder side of Maine](https://bing.codexun.com/us/detail/20260713)**<br>Katahdin Woods and Waters National Monument, Maine<br>*2026-07-13* | **[Where Brittany meets the tide](https://bing.codexun.com/us/detail/20260712)**<br>Port de Saint-Goustan, Auray, Brittany, France<br>*2026-07-12* | 
| [![The land of moving shorelines](https://www.bing.com/th?id=OHR.VictoriaBeach_EN-US7607379912_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260711) | [![Tradition in every step](https://www.bing.com/th?id=OHR.SapaVietnam_EN-US4008171614_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260710) | [![Echoes of a volcanic past](https://www.bing.com/th?id=OHR.LakeAtitlan_EN-US3747076006_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260709) | 
| **[The land of moving shorelines](https://bing.codexun.com/us/detail/20260711)**<br>Aerial view of land and ocean, Victoria, Australia<br>*2026-07-11* | **[Tradition in every step](https://bing.codexun.com/us/detail/20260710)**<br>Rice fields at Sapa, Lào Cai, Vietnam<br>*2026-07-10* | **[Echoes of a volcanic past](https://bing.codexun.com/us/detail/20260709)**<br>Sunrise at Lake Atitlán, Guatemala<br>*2026-07-09* | 
| [![Color, craft, and canopy life](https://www.bing.com/th?id=OHR.MountainToucanOrchids_EN-US3433249651_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260708) | [![A city written in centuries](https://www.bing.com/th?id=OHR.SyracuseItaly_EN-US3071727282_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260707) | [![Sea of purple](https://www.bing.com/th?id=OHR.LavenderRows_EN-US2831933520_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260706) | 
| **[Color, craft, and canopy life](https://bing.codexun.com/us/detail/20260708)**<br>Plate-billed mountain toucan with orchids, Ecuador<br>*2026-07-08* | **[A city written in centuries](https://bing.codexun.com/us/detail/20260707)**<br>Syracuse at sunset, Sicily, Italy<br>*2026-07-07* | **[Sea of purple](https://bing.codexun.com/us/detail/20260706)**<br>Lavender rows, Plateau de Valensole, Provence, France<br>*2026-07-06* | 
| [![The story continues](https://www.bing.com/th?id=OHR.LibertyHall_EN-US2562041614_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260705) | [![The poetry of vanishing light](https://www.bing.com/th?id=OHR.FirefliesJapan_EN-US2315956275_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260704) | [![Inside Esna's sacred universe](https://www.bing.com/th?id=OHR.TempleEsna_EN-US1999215513_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260703) | 
| **[The story continues](https://bing.codexun.com/us/detail/20260705)**<br>Liberty Bell and Independence Hall, Independence National Historical Park, Philadelphia, Pennsylvania<br>*2026-07-05* | **[The poetry of vanishing light](https://bing.codexun.com/us/detail/20260704)**<br>Fireflies glowing above a stream, Okayama Prefecture, Japan<br>*2026-07-04* | **[Inside Esna's sacred universe](https://bing.codexun.com/us/detail/20260703)**<br>Ceiling of the Temple of Esna, Egypt<br>*2026-07-03* | 
| [![Canada, carved by the Atlantic](https://www.bing.com/th?id=OHR.DungeonPark_EN-US2499621341_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260702) | [![Where shadows stretch tall](https://www.bing.com/th?id=OHR.MasaiGiraffe_EN-US2240704874_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260701) | [![Born on fire, held by water](https://www.bing.com/th?id=OHR.BoraBoraLagoon_EN-US1491116478_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260630) | 
| **[Canada, carved by the Atlantic](https://bing.codexun.com/us/detail/20260702)**<br>Dungeon Provincial Park, Newfoundland and Labrador, Canada<br>*2026-07-02* | **[Where shadows stretch tall](https://bing.codexun.com/us/detail/20260701)**<br>Giraffes at sunset in the Masai Mara National Reserve, Kenya<br>*2026-07-01* | **[Born on fire, held by water](https://bing.codexun.com/us/detail/20260630)**<br>Bora Bora and its lagoon, South Pacific, French Polynesia<br>*2026-06-30* | 
| [![Looking sharp](https://www.bing.com/th?id=OHR.SaguaroSun_EN-US8982109543_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260629) | [![The trees that lost ground](https://www.bing.com/th?id=OHR.BoneyardBeach_EN-US8247496696_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260628) | [![Current affairs](https://www.bing.com/th?id=OHR.ThamesSummer_EN-US6783349970_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260627) | 
| **[Looking sharp](https://bing.codexun.com/us/detail/20260629)**<br>Saguaro cacti near Windgate Pass, McDowell Range, Arizona, USA<br>*2026-06-29* | **[The trees that lost ground](https://bing.codexun.com/us/detail/20260628)**<br>Driftwood on Boneyard Beach, Hunting Island, South Carolina<br>*2026-06-28* | **[Current affairs](https://bing.codexun.com/us/detail/20260627)**<br>The River Thames, London, England<br>*2026-06-27* | 
| [![Square up to history](https://www.bing.com/th?id=OHR.GrandPlace_EN-US6561229456_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260626) | [![Pollen meets wings](https://www.bing.com/th?id=OHR.BFPollin_EN-US6519187095_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260625) | [![Signature on the horizon](https://www.bing.com/th?id=OHR.Fujisan_EN-US6479372200_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260624) | 
| **[Square up to history](https://bing.codexun.com/us/detail/20260626)**<br>Buildings on Grand-Place Square in Brussels, Belgium<br>*2026-06-26* | **[Pollen meets wings](https://bing.codexun.com/us/detail/20260625)**<br>Butterfly pollinating on yellow flower<br>*2026-06-25* | **[Signature on the horizon](https://bing.codexun.com/us/detail/20260624)**<br>Mount Fuji on Honshu Island, Japan<br>*2026-06-24* | 


---

## Wallpaper Archive by Year

### 2026
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 6px; margin: 12px 0;">
<a href="https://bing.codexun.com/us/archive/202607" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f3f4f6; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease; font-weight: 500;">202607</a>
<a href="https://bing.codexun.com/us/archive/202606" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202606</a>
<a href="https://bing.codexun.com/us/archive/202605" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202605</a>
<a href="https://bing.codexun.com/us/archive/202604" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202604</a>
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