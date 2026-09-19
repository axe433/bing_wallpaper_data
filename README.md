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

[![Through the heart of the pass](https://www.bing.com/th?id=OHR.WinnatsPassPeak_EN-US6112068451_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260919)

**Through the heart of the pass**

A long, winding road cuts through rocks more than 300 million years old in England's Peak District. As if that geological timescale were not remarkable enough, the road passes through Winnats Pass, a narrow limestone gorge whose towering cliffs reveal the ancient seas that once covered this part of Britain.

*© Daniel_Kay/Getty Images (Bing United States)*

---

## Recent 30 Days

| | | |
|:---:|:---:|:---:|
| [![Through the heart of the pass](https://www.bing.com/th?id=OHR.WinnatsPassPeak_EN-US6112068451_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260919) | [![A toast to the harvest](https://www.bing.com/th?id=OHR.Santenay_EN-US5299702509_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260918) | [![The Arctic's new explorers](https://www.bing.com/th?id=OHR.IcyCubs_EN-US5222104616_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260917) | 
| **[Through the heart of the pass](https://bing.codexun.com/us/detail/20260919)**<br>Winnats Pass, Peak District National Park, England<br>*2026-09-19* | **[A toast to the harvest](https://bing.codexun.com/us/detail/20260918)**<br>Sorine windmill and vineyards, Santenay wine region, Côte de Beaune, Burgundy, France<br>*2026-09-18* | **[The Arctic's new explorers](https://bing.codexun.com/us/detail/20260917)**<br>Polar bear cubs playing in Svalbard, Norway<br>*2026-09-17* | 
| [![A crossroad of cultures](https://www.bing.com/th?id=OHR.FortUnion_EN-US5138724452_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260916) | [![Where toughness takes root](https://www.bing.com/th?id=OHR.KochiaChina_EN-US5037126636_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260915) | [![A reef above its station](https://www.bing.com/th?id=OHR.MisurinaPeak_EN-US4897144498_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260914) | 
| **[A crossroad of cultures](https://bing.codexun.com/us/detail/20260916)**<br>Fort Union National Monument, New Mexico<br>*2026-09-16* | **[Where toughness takes root](https://bing.codexun.com/us/detail/20260915)**<br>Field of kochia plants, China<br>*2026-09-15* | **[A reef above its station](https://bing.codexun.com/us/detail/20260914)**<br>Cadini di Misurina, Dolomites, Veneto, Italy<br>*2026-09-14* | 
| [![Masters of the surf and shore](https://www.bing.com/th?id=OHR.SardineBait_EN-US4802395270_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260913) | [![A legacy of heroism](https://www.bing.com/th?id=OHR.Flight93_EN-US5966783443_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260912) | [![A patchwork from above](https://www.bing.com/th?id=OHR.Olvera_EN-US4712443253_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260911) | 
| **[Masters of the surf and shore](https://bing.codexun.com/us/detail/20260913)**<br>California sea lions hunting a sardine bait ball, offshore Mexico, Pacific Ocean<br>*2026-09-13* | **[A legacy of heroism](https://bing.codexun.com/us/detail/20260912)**<br>The Flight 93 National Memorial Visitor Center near Shanksville, Pennsylvania<br>*2026-09-12* | **[A patchwork from above](https://bing.codexun.com/us/detail/20260911)**<br>Aerial view of Olvera, Andalusia, Spain<br>*2026-09-11* | 
| [![Life on India's west coast](https://www.bing.com/th?id=OHR.GabitKeni_EN-US4620523183_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260910) | [![Fields of gold](https://www.bing.com/th?id=OHR.BeechEngland_EN-US4535769514_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260909) | [![Labor's legacy](https://www.bing.com/th?id=OHR.RalphStackpole_EN-US4463800234_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260908) | 
| **[Life on India's west coast](https://bing.codexun.com/us/detail/20260910)**<br>Gabit Keni Beach near Ankola, Karnataka, India<br>*2026-09-10* | **[Fields of gold](https://bing.codexun.com/us/detail/20260909)**<br>Beech tree in a cereal field, East Meon, South Downs National Park, Hampshire, England<br>*2026-09-09* | **[Labor's legacy](https://bing.codexun.com/us/detail/20260908)**<br>'Industries of California' mural by Ralph Stackpole at Coit Tower, San Francisco, California<br>*2026-09-08* | 
| [![A reservoir of reflections](https://www.bing.com/th?id=OHR.LakeFyans_EN-US4295341714_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260907) | [![Small birds, big impact](https://www.bing.com/th?id=OHR.GreenCrowned_EN-US3119017947_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260906) | [![Red and white on the horizon](https://www.bing.com/th?id=OHR.Westerheversand_EN-US3028839945_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260905) | 
| **[A reservoir of reflections](https://bing.codexun.com/us/detail/20260907)**<br>Lake Fyans, Grampians National Park, Victoria, Australia<br>*2026-09-07* | **[Small birds, big impact](https://bing.codexun.com/us/detail/20260906)**<br>Green-crowned brilliant hummingbirds feeding on lobster-claw flowers, Costa Rica<br>*2026-09-06* | **[Red and white on the horizon](https://bing.codexun.com/us/detail/20260905)**<br>Westerheversand Lighthouse in Westerhever, Schleswig-Holstein, Germany<br>*2026-09-05* | 
| [![An act of wilderness](https://www.bing.com/th?id=OHR.AZWilderness_EN-US4070936347_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260904) | [![Painted along the shore](https://www.bing.com/th?id=OHR.SuffolkHuts_EN-US3987062531_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260903) | [![A world beneath your feet](https://www.bing.com/th?id=OHR.HorseHairShroom_EN-US3885857486_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260902) | 
| **[An act of wilderness](https://bing.codexun.com/us/detail/20260904)**<br>Coyote Buttes, Vermilion Cliffs National Monument, Arizona<br>*2026-09-04* | **[Painted along the shore](https://bing.codexun.com/us/detail/20260903)**<br>Traditional beach huts, Southwold, Suffolk Heritage Coast, England<br>*2026-09-03* | **[A world beneath your feet](https://bing.codexun.com/us/detail/20260902)**<br>Horsehair parachute fungus, Belarus<br>*2026-09-02* | 
| [![A master class in pattern](https://www.bing.com/th?id=OHR.SamarkandCeiling_EN-US3761829748_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260901) | [![The fish that outgrew its name](https://www.bing.com/th?id=OHR.YellowShark_EN-US3678567058_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260831) | [![Reading between the waves](https://www.bing.com/th?id=OHR.SantaCatarina_EN-US3600536393_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260830) | 
| **[A master class in pattern](https://bing.codexun.com/us/detail/20260901)**<br>Building detail of Registan Square, Samarkand, Uzbekistan<br>*2026-09-01* | **[The fish that outgrew its name](https://bing.codexun.com/us/detail/20260831)**<br>Whale shark and golden trevally, Cenderawasih Bay, West Papua, Indonesia<br>*2026-08-31* | **[Reading between the waves](https://bing.codexun.com/us/detail/20260830)**<br>Aerial view of surfers, Santa Catarina, Brazil<br>*2026-08-30* | 
| [![Where tides shape a legend](https://www.bing.com/th?id=OHR.MichelSunset_EN-US3527235033_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260829) | [![Water, wildlife, and wonder](https://www.bing.com/th?id=OHR.LakeMagadi_EN-US3401664434_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260828) | [![A sky alive with color](https://www.bing.com/th?id=OHR.AurorasIceland_EN-US3293282785_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260827) | 
| **[Where tides shape a legend](https://bing.codexun.com/us/detail/20260829)**<br>Mont-Saint-Michel during high tide, Manche, Normandy, France<br>*2026-08-29* | **[Water, wildlife, and wonder](https://bing.codexun.com/us/detail/20260828)**<br>Lesser flamingo flock at sunrise, Lake Magadi, Kenya<br>*2026-08-28* | **[A sky alive with color](https://bing.codexun.com/us/detail/20260827)**<br>Auroras over Kirkjufell, Iceland<br>*2026-08-27* | 
| [![Protecting America's treasures](https://www.bing.com/th?id=OHR.RedwoodPark_EN-US3199427613_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260826) | [![Crossing into history](https://www.bing.com/th?id=OHR.BKBridge_EN-US2923468858_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260825) | [![Meet Katmai's fishing giants](https://www.bing.com/th?id=OHR.KatmaiBear_EN-US2844742219_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260824) | 
| **[Protecting America's treasures](https://bing.codexun.com/us/detail/20260826)**<br>Sunrise in Redwood National and State Parks, California<br>*2026-08-26* | **[Crossing into history](https://bing.codexun.com/us/detail/20260825)**<br>Brooklyn Bridge, New York City<br>*2026-08-25* | **[Meet Katmai's fishing giants](https://bing.codexun.com/us/detail/20260824)**<br>Brown bear fishing in river, Katmai National Park, Alaska<br>*2026-08-24* | 
| [![Sky tinted wings](https://www.bing.com/th?id=OHR.CommonBlue_EN-US2760688799_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260823) | [![The climb is calling](https://www.bing.com/th?id=OHR.JulierPass_EN-US2643379571_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260822) | [![Voices of the pod](https://www.bing.com/th?id=OHR.LynnCanalOrca_EN-US0537229184_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20260821) | 
| **[Sky tinted wings](https://bing.codexun.com/us/detail/20260823)**<br>Common blue butterfly, Devon, England<br>*2026-08-23* | **[The climb is calling](https://bing.codexun.com/us/detail/20260822)**<br>Winding road of Julier Pass, Switzerland<br>*2026-08-22* | **[Voices of the pod](https://bing.codexun.com/us/detail/20260821)**<br>An orca surfaces in Lynn Canal near the Chilkat Mountains, Alaska<br>*2026-08-21* | 


---

## Wallpaper Archive by Year

### 2026
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 6px; margin: 12px 0;">
<a href="https://bing.codexun.com/us/archive/202609" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f3f4f6; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease; font-weight: 500;">202609</a>
<a href="https://bing.codexun.com/us/archive/202608" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202608</a>
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