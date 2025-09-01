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

[![Stitched into history](https://www.bing.com/th?id=OHR.LaborDayChicago_EN-US3947410593_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250902)

**Stitched into history**

May 1915: Chicago buzzes with energy. Streetcars pass brick buildings, shop signs catch the morning light, and the city moves with purpose. But today, something different takes over the streets. The Amalgamated Clothing Workers of America, just months old, march in rows as sharp as the suits they craft. This isn't a quiet debut—it's a statement.

*© Chicago Sun-Times/Chicago Daily News collection/Chicago History Museum/Getty Images (Bing United States)*

---

## Recent 30 Days

| | | |
|:---:|:---:|:---:|
| [![Stitched into history](https://www.bing.com/th?id=OHR.LaborDayChicago_EN-US3947410593_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250902) | [![Painted clouds, still cliffs](https://www.bing.com/th?id=OHR.ScottsBluff_EN-US3893566724_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250901) | [![Finned and fabulous](https://www.bing.com/th?id=OHR.MaldivesWhaleShark_EN-US3819740955_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250831) | 
| **[Stitched into history](https://bing.codexun.com/us/detail/20250902)**<br>Amalgamated Clothing Workers of America in a Labor Day parade, May 1915, Chicago<br>*2025-09-02* | **[Painted clouds, still cliffs](https://bing.codexun.com/us/detail/20250901)**<br>Scotts Bluff National Monument in Gering, Nebraska<br>*2025-09-01* | **[Finned and fabulous](https://bing.codexun.com/us/detail/20250831)**<br>Whale shark off the coast of Alifu Dhaalu Atoll, Maldives<br>*2025-08-31* | 
| [![The heart of the grid](https://www.bing.com/th?id=OHR.PlazaMayor_EN-US3692727880_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250830) | [![This egret has no regrets](https://www.bing.com/th?id=OHR.WhiteEgret_EN-US3605994040_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250829) | [![A lake above the ocean](https://www.bing.com/th?id=OHR.FaroeLake_EN-US3557234950_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250828) | 
| **[The heart of the grid](https://bing.codexun.com/us/detail/20250830)**<br>Aerial view of Plaza Mayor, Madrid, Spain<br>*2025-08-30* | **[This egret has no regrets](https://bing.codexun.com/us/detail/20250829)**<br>Great white egret, Hungary<br>*2025-08-29* | **[A lake above the ocean](https://bing.codexun.com/us/detail/20250828)**<br>Sørvágsvatn lake, island of Vágar, Faroe Islands, Denmark<br>*2025-08-28* | 
| [![A 'trulli' remarkable town](https://www.bing.com/th?id=OHR.TrulliHouses_EN-US3489439665_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250827) | [![From volcanic roots to river routes](https://www.bing.com/th?id=OHR.YellowstoneRiver_EN-US3380364726_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250826) | [!['Fallow' us](https://www.bing.com/th?id=OHR.CervusDama_EN-US3217647015_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250825) | 
| **[A 'trulli' remarkable town](https://bing.codexun.com/us/detail/20250827)**<br>Trullo buildings in Alberobello, Apulia, Italy<br>*2025-08-27* | **[From volcanic roots to river routes](https://bing.codexun.com/us/detail/20250826)**<br>Calcite Springs Overlook and Yellowstone River, Yellowstone National Park, Wyoming<br>*2025-08-26* | **['Fallow' us](https://bing.codexun.com/us/detail/20250825)**<br>European fallow deer, England<br>*2025-08-25* | 
| [![Gothic majesty](https://www.bing.com/th?id=OHR.SaintBarbaras_EN-US3076115197_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250824) | [![Nature's green quilt](https://www.bing.com/th?id=OHR.PalouseWA_EN-US2419102005_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250823) | [![Perched and poised](https://www.bing.com/th?id=OHR.WheatearBird_EN-US2132045619_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250822) | 
| **[Gothic majesty](https://bing.codexun.com/us/detail/20250824)**<br>St. Barbara's Cathedral, Kutná Hora, Czechia<br>*2025-08-24* | **[Nature's green quilt](https://bing.codexun.com/us/detail/20250823)**<br>Rolling hills of the Palouse, Washington<br>*2025-08-23* | **[Perched and poised](https://bing.codexun.com/us/detail/20250822)**<br>Wheatear and flowering heather, Peak District National Park, England<br>*2025-08-22* | 
| [![Built to last](https://www.bing.com/th?id=OHR.CitadelBonifacio_EN-US2046177235_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250821) | [![Powered by the sun](https://www.bing.com/th?id=OHR.SolarAviation_EN-US1940905760_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250820) | [![Stream a little dream](https://www.bing.com/th?id=OHR.AvalancheLake_EN-US1814683119_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250819) | 
| **[Built to last](https://bing.codexun.com/us/detail/20250821)**<br>The citadel in Bonifacio, Southern Corsica, France<br>*2025-08-21* | **[Powered by the sun](https://bing.codexun.com/us/detail/20250820)**<br>Solar Impulse 2 at Kalaeloa Airport, Honolulu, Hawaii<br>*2025-08-20* | **[Stream a little dream](https://bing.codexun.com/us/detail/20250819)**<br>Avalanche Lake Trail at Adirondack High Peaks, New York<br>*2025-08-19* | 
| [![One tall way to spot the sea](https://www.bing.com/th?id=OHR.LyngvigLighthouse_EN-US1600601632_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250818) | [![Bee the change](https://www.bing.com/th?id=OHR.ColorfulBeehives_EN-US1476944743_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250817) | [![Winging it underwater](https://www.bing.com/th?id=OHR.SpottedEagleRay_EN-US9227600044_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250816) | 
| **[One tall way to spot the sea](https://bing.codexun.com/us/detail/20250818)**<br>Lyngvig Lighthouse, Hvide Sande, Denmark<br>*2025-08-18* | **[Bee the change](https://bing.codexun.com/us/detail/20250817)**<br>Colorful beehives in Italy<br>*2025-08-17* | **[Winging it underwater](https://bing.codexun.com/us/detail/20250816)**<br>Spotted eagle rays, San Cristóbal Island, Galápagos Islands, Ecuador<br>*2025-08-16* | 
| [![Taking it from the top](https://www.bing.com/th?id=OHR.PizNairPeak_EN-US9097547756_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250815) | [![Earth's open secret](https://www.bing.com/th?id=OHR.CoronaArch_EN-US8928406175_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250814) | [![Wild, wise, and wonderful](https://www.bing.com/th?id=OHR.KenyaElephants_EN-US8723347309_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250813) | 
| **[Taking it from the top](https://bing.codexun.com/us/detail/20250815)**<br>Cable car station on Piz Nair mountain, Graubünden, Switzerland<br>*2025-08-15* | **[Earth's open secret](https://bing.codexun.com/us/detail/20250814)**<br>A man rappels off Corona Arch near Moab, Utah<br>*2025-08-14* | **[Wild, wise, and wonderful](https://bing.codexun.com/us/detail/20250813)**<br>African elephant herd, Amboseli National Park, Kenya<br>*2025-08-13* | 
| [![Postcard from the peaks](https://www.bing.com/th?id=OHR.SantaMaddalena_EN-US8546897995_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250812) | [![Roar for a cause](https://www.bing.com/th?id=OHR.LionessKenya_EN-US8440386444_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250811) | [![Honoring Indigenous voices](https://www.bing.com/th?id=OHR.MaoriRock_EN-US6499689741_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250810) | 
| **[Postcard from the peaks](https://bing.codexun.com/us/detail/20250812)**<br>Village of Santa Maddalena, Dolomites, Italy<br>*2025-08-12* | **[Roar for a cause](https://bing.codexun.com/us/detail/20250811)**<br>Lioness in Maasai Mara National Reserve, Kenya<br>*2025-08-11* | **[Honoring Indigenous voices](https://bing.codexun.com/us/detail/20250810)**<br>Ngātoroirangi Mine Bay Māori Rock Carvings on Lake Taupō, New Zealand<br>*2025-08-10* | 
| [![All for falls and falls for all](https://www.bing.com/th?id=OHR.IguazuArgentina_EN-US5953375078_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250809) | [![Code of the coastline](https://www.bing.com/th?id=OHR.GasparillaLight_EN-US0554204214_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250808) | [![Off the grid](https://www.bing.com/th?id=OHR.NaPaliKauai_EN-US7451684312_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250807) | 
| **[All for falls and falls for all](https://bing.codexun.com/us/detail/20250809)**<br>Three Musketeers Falls at Iguazú Falls, Argentina<br>*2025-08-09* | **[Code of the coastline](https://bing.codexun.com/us/detail/20250808)**<br>Gasparilla Island Rear Range Light, Boca Grande, Florida<br>*2025-08-08* | **[Off the grid](https://bing.codexun.com/us/detail/20250807)**<br>Kalalau Beach on the Nā Pali Coast, Kauai, Hawaii<br>*2025-08-07* | 
| [![Tide and seek](https://www.bing.com/th?id=OHR.CaliforniaTidepool_EN-US9089576317_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250806) | [![Whooo's home?](https://www.bing.com/th?id=OHR.LaplandOwl_EN-US8965493818_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250805) | [![Hello yellow!](https://www.bing.com/th?id=OHR.HappySunflower_EN-US8791544241_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20250804) | 
| **[Tide and seek](https://bing.codexun.com/us/detail/20250806)**<br>Tide pools in La Jolla, California<br>*2025-08-06* | **[Whooo's home?](https://bing.codexun.com/us/detail/20250805)**<br>Great gray owls in their nest, Finland<br>*2025-08-05* | **[Hello yellow!](https://bing.codexun.com/us/detail/20250804)**<br>Sunflowers in a field in summer<br>*2025-08-04* | 


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