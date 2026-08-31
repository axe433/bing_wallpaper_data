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

[![The fish that outgrew its name](https://www.bing.com/th?id=OHR.YellowShark_EN-US3678567058_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260831)

**The fish that outgrew its name**

Today, International Whale Shark Day makes room for the world's largest fish. Despite their name, whale sharks are not whales but fish, reaching lengths of up to 60 feet and weighing around 20 tons. Found in warm tropical seas, they glide through the water with their mouths open, filtering plankton, fish eggs, and other tiny prey. This species' distinctive white-spot patterns are unique to each individual, much like human fingerprints.

*© Pete Oxford/Nature Picture Library (Bing United States)*

---

## Recent 30 Days

| | | |
|:---:|:---:|:---:|
| [![The fish that outgrew its name](https://www.bing.com/th?id=OHR.YellowShark_EN-US3678567058_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260831) | [![Reading between the waves](https://www.bing.com/th?id=OHR.SantaCatarina_EN-US3600536393_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260830) | [![Where tides shape a legend](https://www.bing.com/th?id=OHR.MichelSunset_EN-US3527235033_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260829) | 
| **[The fish that outgrew its name](https://bing.codexun.com/us/detail/20260831)**<br>Whale shark and golden trevally, Cenderawasih Bay, West Papua, Indonesia<br>*2026-08-31* | **[Reading between the waves](https://bing.codexun.com/us/detail/20260830)**<br>Aerial view of surfers, Santa Catarina, Brazil<br>*2026-08-30* | **[Where tides shape a legend](https://bing.codexun.com/us/detail/20260829)**<br>Mont-Saint-Michel during high tide, Manche, Normandy, France<br>*2026-08-29* | 
| [![Water, wildlife, and wonder](https://www.bing.com/th?id=OHR.LakeMagadi_EN-US3401664434_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260828) | [![A sky alive with color](https://www.bing.com/th?id=OHR.AurorasIceland_EN-US3293282785_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260827) | [![Protecting America's treasures](https://www.bing.com/th?id=OHR.RedwoodPark_EN-US3199427613_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260826) | 
| **[Water, wildlife, and wonder](https://bing.codexun.com/us/detail/20260828)**<br>Lesser flamingo flock at sunrise, Lake Magadi, Kenya<br>*2026-08-28* | **[A sky alive with color](https://bing.codexun.com/us/detail/20260827)**<br>Auroras over Kirkjufell, Iceland<br>*2026-08-27* | **[Protecting America's treasures](https://bing.codexun.com/us/detail/20260826)**<br>Sunrise in Redwood National and State Parks, California<br>*2026-08-26* | 
| [![Crossing into history](https://www.bing.com/th?id=OHR.BKBridge_EN-US2923468858_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260825) | [![Meet Katmai's fishing giants](https://www.bing.com/th?id=OHR.KatmaiBear_EN-US2844742219_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260824) | [![Sky tinted wings](https://www.bing.com/th?id=OHR.CommonBlue_EN-US2760688799_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260823) | 
| **[Crossing into history](https://bing.codexun.com/us/detail/20260825)**<br>Brooklyn Bridge, New York City<br>*2026-08-25* | **[Meet Katmai's fishing giants](https://bing.codexun.com/us/detail/20260824)**<br>Brown bear fishing in river, Katmai National Park, Alaska<br>*2026-08-24* | **[Sky tinted wings](https://bing.codexun.com/us/detail/20260823)**<br>Common blue butterfly, Devon, England<br>*2026-08-23* | 
| [![The climb is calling](https://www.bing.com/th?id=OHR.JulierPass_EN-US2643379571_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260822) | [![Voices of the pod](https://www.bing.com/th?id=OHR.LynnCanalOrca_EN-US0537229184_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260821) | [![Testing the future of flight](https://www.bing.com/th?id=OHR.BrewsterXF2A_EN-US0417477370_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260820) | 
| **[The climb is calling](https://bing.codexun.com/us/detail/20260822)**<br>Winding road of Julier Pass, Switzerland<br>*2026-08-22* | **[Voices of the pod](https://bing.codexun.com/us/detail/20260821)**<br>An orca surfaces in Lynn Canal near the Chilkat Mountains, Alaska<br>*2026-08-21* | **[Testing the future of flight](https://bing.codexun.com/us/detail/20260820)**<br>NASA's Langley Research Center mounted the Navy's Brewster XF2A-1 Buffalo in the Full-Scale Tunnel, 1938, Hampton, Virginia<br>*2026-08-20* | 
| [![Geometry of a star city](https://www.bing.com/th?id=OHR.Palmanova_EN-US0340289339_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260819) | [![A prime 'reef' estate](https://www.bing.com/th?id=OHR.CabilaoClowns_EN-US6302440247_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260818) | [![Where swans started a legend](https://www.bing.com/th?id=OHR.RossErrillyRuins_EN-US5729358123_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260817) | 
| **[Geometry of a star city](https://bing.codexun.com/us/detail/20260819)**<br>Aerial view of Palmanova, a fortress city in Friuli, Italy<br>*2026-08-19* | **[A prime 'reef' estate](https://bing.codexun.com/us/detail/20260818)**<br>Three false clownfish in a sea anemone, Cabilao Island, Bohol, Philippines<br>*2026-08-18* | **[Where swans started a legend](https://bing.codexun.com/us/detail/20260817)**<br>Ruins of Ross Errilly Friary, County Galway, Ireland<br>*2026-08-17* | 
| [![The great balancing act](https://www.bing.com/th?id=OHR.ValleyDreams_EN-US5250331985_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260816) | [![Built for paws, not people](https://www.bing.com/th?id=OHR.WildlifeCrossingPoland_EN-US5004733603_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260815) | [![Make a wish](https://www.bing.com/th?id=OHR.PerseidasTenerife_EN-US4798593153_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260814) | 
| **[The great balancing act](https://bing.codexun.com/us/detail/20260816)**<br>Hoodoos in Ah Shi Sle Pah Wilderness in San Juan County, New Mexico<br>*2026-08-16* | **[Built for paws, not people](https://bing.codexun.com/us/detail/20260815)**<br>Aerial view of a wildlife crossing near Zakrzów, Poland<br>*2026-08-15* | **[Make a wish](https://bing.codexun.com/us/detail/20260814)**<br>Perseid meteors over Teide Observatory, Tenerife, Spain<br>*2026-08-14* | 
| [![Giants worth protecting](https://www.bing.com/th?id=OHR.ElephantDay_EN-US4280370948_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260813) | [![Copenhagen in full color](https://www.bing.com/th?id=OHR.ColorfulCop_EN-US3993977654_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260812) | [![Where two deserts collide](https://www.bing.com/th?id=OHR.SandPath_EN-US3759872156_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260811) | 
| **[Giants worth protecting](https://bing.codexun.com/us/detail/20260813)**<br>A group of elephants, Amboseli National Park, Kenya<br>*2026-08-13* | **[Copenhagen in full color](https://bing.codexun.com/us/detail/20260812)**<br>Colorful homes line Nyhavn Canal, Copenhagen, Denmark<br>*2026-08-12* | **[Where two deserts collide](https://bing.codexun.com/us/detail/20260811)**<br>Joshua Tree National Park, California<br>*2026-08-11* | 
| [![Architecture of identity](https://www.bing.com/th?id=OHR.JMTjibaou_EN-US3454380257_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260810) | [![Crossing into infinity](https://www.bing.com/th?id=OHR.StocktonInfinity_EN-US3006724421_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260809) | [![Guiding ships through history](https://www.bing.com/th?id=OHR.LimeKiln_EN-US2748515593_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260808) | 
| **[Architecture of identity](https://bing.codexun.com/us/detail/20260810)**<br>Jean-Marie Tjibaou Cultural Centre, New Caledonia<br>*2026-08-10* | **[Crossing into infinity](https://bing.codexun.com/us/detail/20260809)**<br>Infinity Bridge in Stockton-on-Tees, England<br>*2026-08-09* | **[Guiding ships through history](https://bing.codexun.com/us/detail/20260808)**<br>Lime Kiln Lighthouse on San Juan Island, Washington State<br>*2026-08-08* | 
| [![Where the river tests the brave](https://www.bing.com/th?id=OHR.MaraCrossing_EN-US8682968377_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260807) | [![Gates of a hidden kingdom](https://www.bing.com/th?id=OHR.FezMorocco_EN-US8380353742_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260806) | [![Hoot hoot hooray!](https://www.bing.com/th?id=OHR.AdorableOwlet_EN-US7873975586_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260805) | 
| **[Where the river tests the brave](https://bing.codexun.com/us/detail/20260807)**<br>Migrating wildebeest crossing Mara River in Masai Mara, Kenya<br>*2026-08-07* | **[Gates of a hidden kingdom](https://bing.codexun.com/us/detail/20260806)**<br>Decorated gate of the Royal Palace of Fez, Morocco<br>*2026-08-06* | **[Hoot hoot hooray!](https://bing.codexun.com/us/detail/20260805)**<br>Florida burrowing owlet, Cape Coral, Florida, USA<br>*2026-08-05* | 
| [![Bright boats, timeless traditions](https://www.bing.com/th?id=OHR.BoatsMalta_EN-US5373607495_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260804) | [![Daughter of the Baltic](https://www.bing.com/th?id=OHR.HelsinkiBlue_EN-US4898215906_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260803) | [![The power of Kīlauea](https://www.bing.com/th?id=OHR.HawaiiLava_EN-US4126737972_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260802) | 
| **[Bright boats, timeless traditions](https://bing.codexun.com/us/detail/20260804)**<br>Colorful boats in Marsaxlokk Harbor, Malta<br>*2026-08-04* | **[Daughter of the Baltic](https://bing.codexun.com/us/detail/20260803)**<br>Helsinki's shoreline during blue hour, Uusimaa, Finland<br>*2026-08-03* | **[The power of Kīlauea](https://bing.codexun.com/us/detail/20260802)**<br>A series of lava flows spill into the ocean, Big Island, Hawaii<br>*2026-08-02* | 


---

## Wallpaper Archive by Year

### 2026
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 6px; margin: 12px 0;">
<a href="https://bing.codexun.com/us/archive/202608" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f3f4f6; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease; font-weight: 500;">202608</a>
<a href="https://bing.codexun.com/us/archive/202607" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202607</a>
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