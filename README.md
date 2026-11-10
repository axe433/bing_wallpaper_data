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

[![Where art finds its rhythm](https://www.bing.com/th?id=OHR.TrianaSpain_EN-US0872031458_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261110)

**Where art finds its rhythm**

Cross the Guadalquivir River in Seville, the capital of Spain's Andalusia region, and the city's rhythm seems to change. On the other side lies Triana, a colorful neighborhood where ceramics, flamenco, and local traditions are woven into everyday life. Since the 19th century, the Isabel II Bridge, also known as the Triana Bridge, has connected the neighborhood to Seville's historic center.

*© Andrzej Rostek/Getty Images (Bing United States)*

---

## Recent 30 Days

| | | |
|:---:|:---:|:---:|
| [![Where art finds its rhythm](https://www.bing.com/th?id=OHR.TrianaSpain_EN-US0872031458_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261110) | [![A celebration that shines](https://www.bing.com/th?id=OHR.DiwaliLamps_EN-US0788074051_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261109) | [![The giant that came back](https://www.bing.com/th?id=OHR.DakotaBison_EN-US0710175615_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261108) | 
| **[Where art finds its rhythm](https://bing.codexun.com/us/detail/20261110)**<br>Historic district of Triana, Seville, Spain<br>*2026-11-10* | **[A celebration that shines](https://bing.codexun.com/us/detail/20261109)**<br>Lanterns for Diwali, Mumbai, Maharashtra, India<br>*2026-11-09* | **[The giant that came back](https://bing.codexun.com/us/detail/20261108)**<br>A bison in the grasslands of Theodore Roosevelt National Park, North Dakota<br>*2026-11-08* | 
| [![A green tunnel through Maui](https://www.bing.com/th?id=OHR.PipiwaiTrail_EN-US0631882545_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261107) | [![One step closer to the summit](https://www.bing.com/th?id=OHR.StileCrossing_EN-US9052435517_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261106) | [![Paddling a painted forest](https://www.bing.com/th?id=OHR.AutumnChina_EN-US0467722422_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261105) | 
| **[A green tunnel through Maui](https://bing.codexun.com/us/detail/20261107)**<br>Bamboo forest, Pīpīwai Trail, Haleakalā National Park, Maui, Hawaii<br>*2026-11-07* | **[One step closer to the summit](https://bing.codexun.com/us/detail/20261106)**<br>Wooden stile at a stone wall, Black Crag, Lake District, England<br>*2026-11-06* | **[Paddling a painted forest](https://bing.codexun.com/us/detail/20261105)**<br>People rowing among colorful bald cypress, Xuancheng, Anhui, China<br>*2026-11-05* | 
| [![Peace among the peaks](https://www.bing.com/th?id=OHR.AlpineBraies_EN-US6636326357_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261104) | [![A future written in ice](https://www.bing.com/th?id=OHR.HudsonBear_EN-US0297833232_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261103) | [![Crafting continuity](https://www.bing.com/th?id=OHR.NativeBaskets_EN-US0205712064_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261102) | 
| **[Peace among the peaks](https://bing.codexun.com/us/detail/20261104)**<br>Lake Braies, Fanes‑Sennes‑Braies Nature Park, Dolomites, Italy<br>*2026-11-04* | **[A future written in ice](https://bing.codexun.com/us/detail/20261103)**<br>Polar bear and cubs by Hudson Bay, Manitoba, Canada<br>*2026-11-03* | **[Crafting continuity](https://bing.codexun.com/us/detail/20261102)**<br>Handmade baskets, Santa Fe, New Mexico<br>*2026-11-02* | 
| [![Ghosts of empires past](https://www.bing.com/th?id=OHR.FrankfurtHalloween_EN-US0115213682_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261101) | [![Time to fly high](https://www.bing.com/th?id=OHR.AutumnCranes_EN-US9795571462_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261031) | [![Where mist meets millennia](https://www.bing.com/th?id=OHR.AveburyStones_EN-US9568662876_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261030) | 
| **[Ghosts of empires past](https://bing.codexun.com/us/detail/20261101)**<br>St. Bartholomew's Cathedral in Frankfurt, Germany<br>*2026-11-01* | **[Time to fly high](https://bing.codexun.com/us/detail/20261031)**<br>Sandhill cranes, Bosque del Apache National Wildlife Refuge, New Mexico, USA<br>*2026-10-31* | **[Where mist meets millennia](https://bing.codexun.com/us/detail/20261030)**<br>Standing stones at Avebury in Wiltshire, England<br>*2026-10-30* | 
| [![Where history stands watch](https://www.bing.com/th?id=OHR.KuneticeCastle_EN-US9492527404_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261029) | [![Nature's golden mirror](https://www.bing.com/th?id=OHR.PondCypress_EN-US0123444779_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261028) | [![Hanging in there](https://www.bing.com/th?id=OHR.HangingBat_EN-US7714746725_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261027) | 
| **[Where history stands watch](https://bing.codexun.com/us/detail/20261029)**<br>Kunětická hora Castle, Bohemia, Czechia<br>*2026-10-29* | **[Nature's golden mirror](https://bing.codexun.com/us/detail/20261028)**<br>A grove of pond cypress trees with fall foliage, Georgia, USA<br>*2026-10-28* | **[Hanging in there](https://bing.codexun.com/us/detail/20261027)**<br>Gray-headed flying fox, Victoria, Australia<br>*2026-10-27* | 
| [![Nature's autumn soundtrack](https://www.bing.com/th?id=OHR.SitovoWaterfall_EN-US7626867890_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261026) | [![Bookishly extravagant](https://www.bing.com/th?id=OHR.PortugueseLibrary_EN-US7519268149_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261025) | [![Partners in the wild](https://www.bing.com/th?id=OHR.YellowstoneWolves_EN-US7105521535_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261024) | 
| **[Nature's autumn soundtrack](https://bing.codexun.com/us/detail/20261026)**<br>Autumn waterfalls near Sitovo, Plovdiv Province, Bulgaria<br>*2026-10-26* | **[Bookishly extravagant](https://bing.codexun.com/us/detail/20261025)**<br>Royal Portuguese Cabinet of Reading, Rio de Janeiro, Brazil<br>*2026-10-25* | **[Partners in the wild](https://bing.codexun.com/us/detail/20261024)**<br>Two gray wolves, Yellowstone National Park, Wyoming<br>*2026-10-24* | 
| [![Still waters, vivid colors](https://www.bing.com/th?id=OHR.NaejangsanNP_EN-US7010419904_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261023) | [![Winging it over the river](https://www.bing.com/th?id=OHR.VietnamBridge_EN-US6907946681_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261022) | [![Life in the slow lane](https://www.bing.com/th?id=OHR.BrownSloth_EN-US6816754257_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261021) | 
| **[Still waters, vivid colors](https://bing.codexun.com/us/detail/20261023)**<br>Autumn in Naejangsan National Park, South Korea<br>*2026-10-23* | **[Winging it over the river](https://bing.codexun.com/us/detail/20261022)**<br>Nguyen Hoang Bridge over the Perfume River, Hue, Vietnam<br>*2026-10-22* | **[Life in the slow lane](https://bing.codexun.com/us/detail/20261021)**<br>Brown-throated sloth, Puerto Viejo de Talamanca, Costa Rica<br>*2026-10-21* | 
| [![The road that runs on water](https://www.bing.com/th?id=OHR.VeniceSunrise_EN-US6714393168_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261020) | [![75 and thriving](https://www.bing.com/th?id=OHR.DolbadarnWales_EN-US6620614213_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261019) | [![The past, unearthed](https://www.bing.com/th?id=OHR.ChauvetPaintingsFrance_EN-US6137200151_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261018) | 
| **[The road that runs on water](https://bing.codexun.com/us/detail/20261020)**<br>Grand Canal in Venice, Italy<br>*2026-10-20* | **[75 and thriving](https://bing.codexun.com/us/detail/20261019)**<br>Dolbadarn Castle, Llanberis, Eryri National Park<br>*2026-10-19* | **[The past, unearthed](https://bing.codexun.com/us/detail/20261018)**<br>Life-size replica of Chauvet  cave art in Vallon-Pont-d'Arc, France<br>*2026-10-18* | 
| [!['Peak' into Colorado](https://www.bing.com/th?id=OHR.SneffelsAutumn_EN-US3953128777_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261017) | [![Bridges, rooftops, and twilight](https://www.bing.com/th?id=OHR.WroclawPoland_EN-US7757698922_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261016) | [![Spirals through time](https://www.bing.com/th?id=OHR.AmmoniteFossils_EN-US6354038755_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261015) | 
| **['Peak' into Colorado](https://bing.codexun.com/us/detail/20261017)**<br>Mount Sneffels in the San Juan Mountains near Ridgway, Colorado<br>*2026-10-17* | **[Bridges, rooftops, and twilight](https://bing.codexun.com/us/detail/20261016)**<br>View of the Wroclaw Market Square from the Witches' Bridge in Wroclaw, Poland<br>*2026-10-16* | **[Spirals through time](https://bing.codexun.com/us/detail/20261015)**<br>Ammonite fossils from the Jurassic Period<br>*2026-10-15* | 
| [![A symphony in blue and green](https://www.bing.com/th?id=OHR.PlitviceAutumn_EN-US6255909048_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261014) | [![A landscape of living history](https://www.bing.com/th?id=OHR.WhiteHouse_EN-US6161912809_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261013) | [![Where autumn turns the wheel](https://www.bing.com/th?id=OHR.BabcockSP_EN-US6068931791_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20261012) | 
| **[A symphony in blue and green](https://bing.codexun.com/us/detail/20261014)**<br>Plitvice Lakes National Park, Croatia<br>*2026-10-14* | **[A landscape of living history](https://bing.codexun.com/us/detail/20261013)**<br>White House Ruin at Canyon de Chelly National Monument in Arizona<br>*2026-10-13* | **[Where autumn turns the wheel](https://bing.codexun.com/us/detail/20261012)**<br>Glade Creek Grist Mill, Babcock State Park, West Virginia<br>*2026-10-12* | 


---

## Wallpaper Archive by Year

### 2026
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 6px; margin: 12px 0;">
<a href="https://bing.codexun.com/us/archive/202611" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f3f4f6; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease; font-weight: 500;">202611</a>
<a href="https://bing.codexun.com/us/archive/202610" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202610</a>
<a href="https://bing.codexun.com/us/archive/202609" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202609</a>
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