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

[![A lush kingdom](https://www.bing.com/th?id=OHR.QuinaultFerns_EN-US6436576493_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260623)

**A lush kingdom**

June 22 is World Rainforest Day, a global moment and a year-round call to protect the world's remaining rainforests. These ecosystems aren't just dots on the map. They thrive across the tropics and beyond yet cover only about 6% of Earth's surface. Think of the Amazon in South America, the Congo Basin in Africa, and the forests of Southeast Asia.

*© Chris Moore/Tandem Stills + Motion (Bing United States)*

---

## Recent 30 Days

| | | |
|:---:|:---:|:---:|
| [![A lush kingdom](https://www.bing.com/th?id=OHR.QuinaultFerns_EN-US6436576493_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260623) | [![Feathered fathers](https://www.bing.com/th?id=OHR.EggDad_EN-US6390221455_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260622) | [![An ocean's frozen cathedral](https://www.bing.com/th?id=OHR.ArchedIceberg_EN-US6345786269_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260621) | 
| **[A lush kingdom](https://bing.codexun.com/us/detail/20260623)**<br>Quinault rainforest, Olympic National Park, Washington state<br>*2026-06-23* | **[Feathered fathers](https://bing.codexun.com/us/detail/20260622)**<br>King penguin father checking egg<br>*2026-06-22* | **[An ocean's frozen cathedral](https://bing.codexun.com/us/detail/20260621)**<br>Arched iceberg floating off the western Antarctic Peninsula, Southern Ocean<br>*2026-06-21* | 
| [![A story rising in bronze](https://www.bing.com/th?id=OHR.JuneteenthNMAAHC_EN-US6306942628_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260620) | [![A rock-solid marvel](https://www.bing.com/th?id=OHR.Saqsaywaman_EN-US6250260694_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260619) | [![Twist your way up](https://www.bing.com/th?id=OHR.TremolaRoad_EN-US6212254886_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260618) | 
| **[A story rising in bronze](https://bing.codexun.com/us/detail/20260620)**<br>National Museum of African American History and Culture, Washington, DC<br>*2026-06-20* | **[A rock-solid marvel](https://bing.codexun.com/us/detail/20260619)**<br>Aerial view of the ruins of Sacsayhuamán, Cusco, Peru<br>*2026-06-19* | **[Twist your way up](https://bing.codexun.com/us/detail/20260618)**<br>Tremola Road on the Saint Gotthard Pass in Airolo, Switzerland<br>*2026-06-18* | 
| [![Nature's reef keepers](https://www.bing.com/th?id=OHR.SevenMileTurtle_EN-US6164934763_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260617) | [![Aged to scenic perfection](https://www.bing.com/th?id=OHR.ParkEstd_EN-US6114949122_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260616) | [![History flies high](https://www.bing.com/th?id=OHR.FlagsMonument_EN-US6034154869_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260615) | 
| **[Nature's reef keepers](https://bing.codexun.com/us/detail/20260617)**<br>Hawksbill sea turtle pair near Seven Mile Beach, Grand Cayman, Cayman Islands<br>*2026-06-17* | **[Aged to scenic perfection](https://bing.codexun.com/us/detail/20260616)**<br>Great Smoky Mountains National Park, Tennessee<br>*2026-06-16* | **[History flies high](https://bing.codexun.com/us/detail/20260615)**<br>US flags surrounding the Washington Monument, Washington, DC<br>*2026-06-15* | 
| [![Layers of change](https://www.bing.com/th?id=OHR.BadSunset_EN-US5981956630_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260614) | [![A flash in flight](https://www.bing.com/th?id=OHR.SpainBeeEater_EN-US5920719155_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260613) | [![Quiet strength](https://www.bing.com/th?id=OHR.Limpets_EN-US1055673545_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260612) | 
| **[Layers of change](https://bing.codexun.com/us/detail/20260614)**<br>Sunset in Badlands National Park, South Dakota, USA<br>*2026-06-14* | **[A flash in flight](https://bing.codexun.com/us/detail/20260613)**<br>European bee-eater, Sierra de Grazalema Natural Park, Cádiz, Spain<br>*2026-06-13* | **[Quiet strength](https://bing.codexun.com/us/detail/20260612)**<br>Limpets exposed at low tide on the coast of Praia da Ursa, Portugal<br>*2026-06-12* | 
| [![A splash of blue](https://www.bing.com/th?id=OHR.Hnausapollur_EN-US2080493040_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260611) | [![Taste the sunset](https://www.bing.com/th?id=OHR.CTNPVernazza_EN-US1571456265_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260610) | [![Drift with the current](https://www.bing.com/th?id=OHR.Cyanea_EN-US1146473249_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260609) | 
| **[A splash of blue](https://bing.codexun.com/us/detail/20260611)**<br>Hnausapollur volcanic crater lake, Fjallabak Nature Reserve, Landmannalaugar, Iceland<br>*2026-06-11* | **[Taste the sunset](https://bing.codexun.com/us/detail/20260610)**<br>Vernazza, Cinque Terre, Liguria, Italy<br>*2026-06-10* | **[Drift with the current](https://bing.codexun.com/us/detail/20260609)**<br>Lion's mane jellyfish swimming in the ocean<br>*2026-06-09* | 
| [![Plant your kingdom](https://www.bing.com/th?id=OHR.GardenAtlanta_EN-US2319128074_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260608) | [![Wander often, wonder more](https://www.bing.com/th?id=OHR.HikingNatchez_EN-US0663065299_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260607) | [![The quiet power of an unclaimed world](https://www.bing.com/th?id=OHR.WedLapland_EN-US9813120088_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260606) | 
| **[Plant your kingdom](https://bing.codexun.com/us/detail/20260608)**<br>Atlanta Botanical Garden, Atlanta, Georgia<br>*2026-06-08* | **[Wander often, wonder more](https://bing.codexun.com/us/detail/20260607)**<br>Natchez Trace Parkway, Tupelo, Mississippi, USA<br>*2026-06-07* | **[The quiet power of an unclaimed world](https://bing.codexun.com/us/detail/20260606)**<br>View from Skierffe Mountain over the Rapadalen river delta, Sarek National Park, Laponia, Lapland, Sweden<br>*2026-06-06* | 
| [![Fancy feathers](https://www.bing.com/th?id=OHR.PreeningEgret_EN-US9350488148_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260605) | [![Where the road stops, the ride begins](https://www.bing.com/th?id=OHR.BardenasReales_EN-US9044910730_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260604) | [![Between the blues](https://www.bing.com/th?id=OHR.Qinghai_EN-US8807254633_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260603) | 
| **[Fancy feathers](https://bing.codexun.com/us/detail/20260605)**<br>Snowy egret preening, central Florida, USA<br>*2026-06-05* | **[Where the road stops, the ride begins](https://bing.codexun.com/us/detail/20260604)**<br>Cyclist in Bardenas Reales Natural Park and Biosphere Reserve, Navarra, Spain<br>*2026-06-04* | **[Between the blues](https://bing.codexun.com/us/detail/20260603)**<br>Highway through Xitai Jinaier Lake, Qinghai Province, China<br>*2026-06-03* | 
| [![Pride in plain sight](https://www.bing.com/th?id=OHR.RockefellerPride_EN-US1087499810_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260602) | [![Follow the flow](https://www.bing.com/th?id=OHR.EvergladesWetlands_EN-US8572465847_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260601) | [![Reading between the lines](https://www.bing.com/th?id=OHR.EquusQuagga_EN-US8240577582_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260531) | 
| **[Pride in plain sight](https://bing.codexun.com/us/detail/20260602)**<br>Rainbow flags at Rockefeller Center on June 28, 2020, New York City<br>*2026-06-02* | **[Follow the flow](https://bing.codexun.com/us/detail/20260601)**<br>Aerial view of Everglades National Park, Florida<br>*2026-06-01* | **[Reading between the lines](https://bing.codexun.com/us/detail/20260531)**<br>Plains zebra foal in Etosha National Park, Namibia<br>*2026-05-31* | 
| [![A 'peak' into history](https://www.bing.com/th?id=OHR.SummitEverest_EN-US0552794971_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260530) | [![Design meets discipline](https://www.bing.com/th?id=OHR.HwaesongFortress_EN-US1012626869_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260529) | [![No 'otter' like them](https://www.bing.com/th?id=OHR.OtterDay_EN-US0973120905_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260528) | 
| **[A 'peak' into history](https://bing.codexun.com/us/detail/20260530)**<br>Mount Everest summit, Sagarmatha National Park, Nepal<br>*2026-05-30* | **[Design meets discipline](https://bing.codexun.com/us/detail/20260529)**<br>Old city wall of Hwaseong Fortress, Suwon, South Korea<br>*2026-05-29* | **[No 'otter' like them](https://bing.codexun.com/us/detail/20260528)**<br>Sea otter, Kachemak Bay, Homer, Alaska<br>*2026-05-28* | 
| [![A season written in lupine](https://www.bing.com/th?id=OHR.LupineBloom_EN-US0920778137_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260527) | [![Where silence bears names](https://www.bing.com/th?id=OHR.ArlingtonAmphitheater_EN-US0872772906_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260526) | [![Preserving Europe's wild places](https://www.bing.com/th?id=OHR.DolomitesPark_EN-US0828472809_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260525) | 
| **[A season written in lupine](https://bing.codexun.com/us/detail/20260527)**<br>Lupine flowers in bloom, Northern California<br>*2026-05-27* | **[Where silence bears names](https://bing.codexun.com/us/detail/20260526)**<br>Memorial Amphitheater at Arlington National Cemetery, Arlington, Virginia<br>*2026-05-26* | **[Preserving Europe's wild places](https://bing.codexun.com/us/detail/20260525)**<br>Tre Cime Nature Park, South Tyrol, Italy<br>*2026-05-25* | 


---

## Wallpaper Archive by Year

### 2026
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 6px; margin: 12px 0;">
<a href="https://bing.codexun.com/us/archive/202606" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f3f4f6; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease; font-weight: 500;">202606</a>
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