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

[![Snowfield monarch](https://www.bing.com/th?id=OHR.BavariaEgret_EN-US2697995103_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260224)

**Snowfield monarch**

The great egret is a striking large heron, easily recognizable by its pure white plumage, long neck, and sharp yellow bill. Known for its cosmopolitan distribution, it occupies habitats around the world and adapts well to many aquatic environments. Adults measure about 37 to 41 inches in body length, with a wingspan of 4.3 to 4.8 feet, and weigh about 2.2 pounds, giving them a tall, elegant silhouette—roughly chest‑high when compared to a 6‑foot-tall person. As carnivores, they feed primarily on fish but also take amphibians, insects, small mammals, and occasionally reptiles. Their patient hunting style, standing motionless before striking with sudden precision, is one of their most distinctive traits.

*© Konrad Wothe/naturepl.com (Bing United States)*

---

## Recent 30 Days

| | | |
|:---:|:---:|:---:|
| [![Snowfield monarch](https://www.bing.com/th?id=OHR.BavariaEgret_EN-US2697995103_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260224) | [![The mother of hills](https://www.bing.com/th?id=OHR.MamTorSunrise_EN-US2655534073_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260223) | [![Whispers of winter](https://www.bing.com/th?id=OHR.TetonFox_EN-US2616700325_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260222) | 
| **[Snowfield monarch](https://bing.codexun.com/us/detail/20260224)**<br>Great white egret, Upper Bavaria, Germany<br>*2026-02-24* | **[The mother of hills](https://bing.codexun.com/us/detail/20260223)**<br>The hill of Mam Tor, Derbyshire, England<br>*2026-02-23* | **[Whispers of winter](https://bing.codexun.com/us/detail/20260222)**<br>Red fox standing in snowfall, Grand Teton National Park, Wyoming<br>*2026-02-22* | 
| [![Where light falls](https://www.bing.com/th?id=OHR.AdamsFirefall_EN-US2580399078_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260221) | [![Where the land stares back](https://www.bing.com/th?id=OHR.DragonsEyeRock_EN-US6826796617_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260220) | [![Born to stay wild](https://www.bing.com/th?id=OHR.PrzewalskisHorse_EN-US6767229079_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260219) | 
| **[Where light falls](https://bing.codexun.com/us/detail/20260221)**<br>Horsetail Fall in Yosemite National Park, California<br>*2026-02-21* | **[Where the land stares back](https://bing.codexun.com/us/detail/20260220)**<br>The Dragon's Eye rock formation at Uttakleiv Beach, Norway<br>*2026-02-20* | **[Born to stay wild](https://bing.codexun.com/us/detail/20260219)**<br>Przewalski's horses<br>*2026-02-19* | 
| [![Fifteen days of light](https://www.bing.com/th?id=OHR.NewYearLantern_EN-US6665128229_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260218) | [![Legacies in view](https://www.bing.com/th?id=OHR.PresidentsDay_EN-US6598155144_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260217) | [![Songs beneath the waves](https://www.bing.com/th?id=OHR.MontereyHumpbacks_EN-US6328970690_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260216) | 
| **[Fifteen days of light](https://bing.codexun.com/us/detail/20260218)**<br>Red lanterns celebrating Chinese New Year<br>*2026-02-18* | **[Legacies in view](https://bing.codexun.com/us/detail/20260217)**<br>Lincoln Memorial, Washington, DC<br>*2026-02-17* | **[Songs beneath the waves](https://bing.codexun.com/us/detail/20260216)**<br>Humpback whales in Monterey Bay, California<br>*2026-02-16* | 
| [![Love in bloom](https://www.bing.com/th?id=OHR.ValentineHearts_EN-US6208359150_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260215) | [![Built to bring closer](https://www.bing.com/th?id=OHR.FriendshipBridge_EN-US6136231298_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260214) | [![Evolution in focus](https://www.bing.com/th?id=OHR.DarwinBooby_EN-US4839738451_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260213) | 
| **[Love in bloom](https://bing.codexun.com/us/detail/20260215)**<br>Bleeding hearts<br>*2026-02-15* | **[Built to bring closer](https://bing.codexun.com/us/detail/20260214)**<br>Third Thai-Lao Friendship Bridge connecting Laos and Thailand<br>*2026-02-14* | **[Evolution in focus](https://bing.codexun.com/us/detail/20260213)**<br>Blue-footed booby, Galápagos Islands, Ecuador<br>*2026-02-13* | 
| [![The valley of contrasts](https://www.bing.com/th?id=OHR.BadwaterFlats_EN-US4770719796_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260212) | [![Where the Sirens sing](https://www.bing.com/th?id=OHR.IbizaIslets_EN-US4713963434_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260211) | [![Patterns in motion](https://www.bing.com/th?id=OHR.LeopardCat_EN-US4669057608_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260210) | 
| **[The valley of contrasts](https://bing.codexun.com/us/detail/20260212)**<br>Salt flats in Badwater Basin, Death Valley National Park, California<br>*2026-02-12* | **[Where the Sirens sing](https://bing.codexun.com/us/detail/20260211)**<br>Islets of Es Vedrà and Es Vedranell, Ibiza, Spain<br>*2026-02-11* | **[Patterns in motion](https://bing.codexun.com/us/detail/20260210)**<br>Amur leopard cat, Russia<br>*2026-02-10* | 
| [![From quiet nights to adventurous days](https://www.bing.com/th?id=OHR.CorfuGreece_EN-US4606019833_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260209) | [![Salt, sky, and the stillness between](https://www.bing.com/th?id=OHR.SalarUyuni_EN-US1639129259_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260208) | [![Ra Gusela—peak of the Olympic season](https://www.bing.com/th?id=OHR.GiauPass_EN-US1580552183_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260207) | 
| **[From quiet nights to adventurous days](https://bing.codexun.com/us/detail/20260209)**<br>Corfu at night, Greece<br>*2026-02-09* | **[Salt, sky, and the stillness between](https://bing.codexun.com/us/detail/20260208)**<br>Salar de Uyuni salt flats in Bolivia<br>*2026-02-08* | **[Ra Gusela—peak of the Olympic season](https://bing.codexun.com/us/detail/20260207)**<br>Ra Gusela peak at Giau Pass, near Cortina d'Ampezzo, Italy<br>*2026-02-07* | 
| [![Stuck in a grid](https://www.bing.com/th?id=OHR.MaltaSalt_EN-US0310458987_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260206) | [![The face of change](https://www.bing.com/th?id=OHR.ParksGlass_EN-US0280057691_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260205) | [![Tahoe serving views](https://www.bing.com/th?id=OHR.FanetteIsland_EN-US0236094374_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260204) | 
| **[Stuck in a grid](https://bing.codexun.com/us/detail/20260206)**<br>Salt evaporation ponds on the island of Gozo, Malta<br>*2026-02-06* | **[The face of change](https://bing.codexun.com/us/detail/20260205)**<br>Rosa Parks in stained glass window, Shorter Community African Methodist Episcopal Church, Denver<br>*2026-02-05* | **[Tahoe serving views](https://bing.codexun.com/us/detail/20260204)**<br>Emerald Bay and Fannette Island, Lake Tahoe, California<br>*2026-02-04* | 
| [![A shadow's promise](https://www.bing.com/th?id=OHR.AlpineMarmots_EN-US0200342638_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260203) | [![Celebrate. Reflect. Rise.](https://www.bing.com/th?id=OHR.ArmyNurses_EN-US0165759491_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260202) | [![Love at first stripe](https://www.bing.com/th?id=OHR.EtoshaZebra_EN-US0091145236_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260201) | 
| **[A shadow's promise](https://bing.codexun.com/us/detail/20260203)**<br>Alpine marmots, Hohe Tauern National Park, Austria<br>*2026-02-03* | **[Celebrate. Reflect. Rise.](https://bing.codexun.com/us/detail/20260202)**<br>US Army nurses arrive in Greenock, Scotland, 1944<br>*2026-02-02* | **[Love at first stripe](https://bing.codexun.com/us/detail/20260201)**<br>Plains zebras, Etosha National Park, Namibia<br>*2026-02-01* | 
| [![Where the sea makes way](https://www.bing.com/th?id=OHR.StMichaelsCornwall_EN-US0036057583_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260131) | [![A tall story of Milwaukee](https://www.bing.com/th?id=OHR.MilwaukeeHall_EN-US9990591477_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260130) | [![Flow with it](https://www.bing.com/th?id=OHR.WhanganuiPark_EN-US9741312204_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260129) | 
| **[Where the sea makes way](https://bing.codexun.com/us/detail/20260131)**<br>St. Michael's Mount in Marazion, Cornwall, England<br>*2026-01-31* | **[A tall story of Milwaukee](https://bing.codexun.com/us/detail/20260130)**<br>The eight-story open atrium of Milwaukee City Hall, Wisconsin<br>*2026-01-30* | **[Flow with it](https://bing.codexun.com/us/detail/20260129)**<br>Whanganui National Park, Retaruke, New Zealand<br>*2026-01-29* | 
| [![Feather forecast: pelicans ahead](https://www.bing.com/th?id=OHR.DalmationPelicans_EN-US9458474756_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260128) | [![Bavaria’s gem](https://www.bing.com/th?id=OHR.NeuschwansteinWinter_EN-US9407713688_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260127) | [![Tradition burns bright](https://www.bing.com/th?id=OHR.BurnsPark_EN-US9363066918_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260126) | 
| **[Feather forecast: pelicans ahead](https://bing.codexun.com/us/detail/20260128)**<br>Dalmatian pelicans, Lake Kerkini, Greece<br>*2026-01-28* | **[Bavaria’s gem](https://bing.codexun.com/us/detail/20260127)**<br>Neuschwanstein Castle, Bavaria, Germany<br>*2026-01-27* | **[Tradition burns bright](https://bing.codexun.com/us/detail/20260126)**<br>Burns National Heritage Park, Ayr, Ayrshire, Scotland<br>*2026-01-26* | 


---

## Wallpaper Archive by Year

### 2026
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 6px; margin: 12px 0;">
<a href="https://bing.codexun.com/us/archive/202602" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f3f4f6; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease; font-weight: 500;">202602</a>
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