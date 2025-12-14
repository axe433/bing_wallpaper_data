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

[![The great holiday bird-off](https://www.bing.com/th?id=OHR.TuftedTitmouse_EN-US4835376471_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251215)

**The great holiday bird-off**

Each December, thousands swap wrapping paper for binoculars and step outside for a different kind of holiday tradition: the Audubon Christmas Bird Count. Instead of hunting for bargains, they hunt for birds—with pencils, rather than pellets. Started in 1900 by ornithologist Frank M. Chapman, the count offered a peaceful alternative to the Christmas 'side hunts,' where people competed to shoot the most animals. Chapman had a better idea: count them instead. Over a century later, that simple shift has grown into the world's longest-running citizen-science project.

*© Tim Laman/NPL/Minden Pictures (Bing United States)*

---

## Recent 30 Days

| | | |
|:---:|:---:|:---:|
| [![The great holiday bird-off](https://www.bing.com/th?id=OHR.TuftedTitmouse_EN-US4835376471_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251215) | [![Frozen reflections](https://www.bing.com/th?id=OHR.YosemiteWinter_EN-US4786605896_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251214) | [![The plant that paints the holidays red](https://www.bing.com/th?id=OHR.SpeckledPoinsettia_EN-US4098165068_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251213) | 
| **[The great holiday bird-off](https://bing.codexun.com/us/detail/20251215)**<br>Tufted titmouse perched on pine boughs, Massachusetts<br>*2025-12-15* | **[Frozen reflections](https://bing.codexun.com/us/detail/20251214)**<br>Merced River, Yosemite National Park, California<br>*2025-12-14* | **[The plant that paints the holidays red](https://bing.codexun.com/us/detail/20251213)**<br>Spotted poinsettia<br>*2025-12-13* | 
| [![Where the sky meets Earth](https://www.bing.com/th?id=OHR.EverestGlow_EN-US6131667612_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251212) | [![Where cultures converge](https://www.bing.com/th?id=OHR.CordobaCathedral_EN-US6045311068_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251211) | [![Say 'cheese'… or grass](https://www.bing.com/th?id=OHR.LlamaDay_EN-US5971354659_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251210) | 
| **[Where the sky meets Earth](https://bing.codexun.com/us/detail/20251212)**<br>Summit of Mount Everest at sunset, seen from Renjo La, Nepal<br>*2025-12-12* | **[Where cultures converge](https://bing.codexun.com/us/detail/20251211)**<br>Interior of the Mosque-Cathedral of Córdoba, Andalusia, Spain<br>*2025-12-11* | **[Say 'cheese'… or grass](https://bing.codexun.com/us/detail/20251210)**<br>Guanaco in Punta Norte, Argentina<br>*2025-12-10* | 
| [![All is calm, all is bright](https://www.bing.com/th?id=OHR.ComoChristmas_EN-US5867954466_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251209) | [![Remembering Pearl Harbor](https://www.bing.com/th?id=OHR.PearlHarborDay_EN-US5774515492_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251208) | [![Florida's living wetlands](https://www.bing.com/th?id=OHR.EvergladesSunrise_EN-US5606230133_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251207) | 
| **[All is calm, all is bright](https://bing.codexun.com/us/detail/20251209)**<br>Christmas lights in Domaso, Lake Como, Italy<br>*2025-12-09* | **[Remembering Pearl Harbor](https://bing.codexun.com/us/detail/20251208)**<br>USS Arizona Memorial, Pearl Harbor, Honolulu, Hawaii<br>*2025-12-08* | **[Florida's living wetlands](https://bing.codexun.com/us/detail/20251207)**<br>Spider webs in Everglades National Park, Florida<br>*2025-12-07* | 
| [![The city that mapped the stars](https://www.bing.com/th?id=OHR.CopanRuins_EN-US5517813382_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251206) | [![Sprint for survival](https://www.bing.com/th?id=OHR.CheetahMound_EN-US5447540393_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251205) | [![Dawn of the cranes](https://www.bing.com/th?id=OHR.BosqueCranes_EN-US6752028797_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251204) | 
| **[The city that mapped the stars](https://bing.codexun.com/us/detail/20251206)**<br>Maya site of Copán, Honduras<br>*2025-12-06* | **[Sprint for survival](https://bing.codexun.com/us/detail/20251205)**<br>Cheetah in Maasai Mara National Reserve, Narok, Kenya<br>*2025-12-05* | **[Dawn of the cranes](https://bing.codexun.com/us/detail/20251204)**<br>Sandhill cranes at sunrise, Bosque del Apache National Wildlife Refuge, New Mexico<br>*2025-12-04* | 
| [![A view that speaks volumes](https://www.bing.com/th?id=OHR.WillowLake_EN-US6664756735_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251203) | [![Where ice holds its breath](https://www.bing.com/th?id=OHR.AntarcticArch_EN-US6560308300_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251202) | [![Twinkle all the way](https://www.bing.com/th?id=OHR.LeipzigMarket_EN-US6493622236_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251201) | 
| **[A view that speaks volumes](https://bing.codexun.com/us/detail/20251203)**<br>Willow Lake and Mount Blackburn, Wrangell-St. Elias National Park and Preserve, Alaska<br>*2025-12-03* | **[Where ice holds its breath](https://bing.codexun.com/us/detail/20251202)**<br>Natural arch carved in an iceberg, Antarctica<br>*2025-12-02* | **[Twinkle all the way](https://bing.codexun.com/us/detail/20251201)**<br>Christmas market in Leipzig, Germany<br>*2025-12-01* | 
| [![Oh deer, it's cold!](https://www.bing.com/th?id=OHR.DeerVeluwe_EN-US6795108723_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251130) | [![Wear your heritage](https://www.bing.com/th?id=OHR.ConchaBelt_EN-US6625864424_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251129) | [![The echoes of Plymouth](https://www.bing.com/th?id=OHR.TurkeyDetail_EN-US7401521602_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251128) | 
| **[Oh deer, it's cold!](https://bing.codexun.com/us/detail/20251130)**<br>Red deer stag in De Hoge Veluwe National Park, Netherlands<br>*2025-11-30* | **[Wear your heritage](https://bing.codexun.com/us/detail/20251129)**<br>Collection of silver Native American concho belts, Santa Fe, New Mexico<br>*2025-11-29* | **[The echoes of Plymouth](https://bing.codexun.com/us/detail/20251128)**<br>Male wild turkey plumage, Aransas Natural Wildlife Refuge, Texas<br>*2025-11-28* | 
| [!['Leaf' it to history](https://www.bing.com/th?id=OHR.OliveGrove_EN-US7076835672_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251127) | [![Love, luck, and loose change](https://www.bing.com/th?id=OHR.TreviFountain_EN-US6800145474_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251126) | [![Secrets in stone](https://www.bing.com/th?id=OHR.GwailorFort_EN-US6671653416_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251125) | 
| **['Leaf' it to history](https://bing.codexun.com/us/detail/20251127)**<br>Olive orchard in the Serra de Tramuntana, Mallorca, Balearic Islands, Spain<br>*2025-11-27* | **[Love, luck, and loose change](https://bing.codexun.com/us/detail/20251126)**<br>The Trevi Fountain in Rome, Italy<br>*2025-11-26* | **[Secrets in stone](https://bing.codexun.com/us/detail/20251125)**<br>Gwalior Fort, Madhya Pradesh, India<br>*2025-11-25* | 
| [![Nature's secret code](https://www.bing.com/th?id=OHR.MadgascarAmmonite_EN-US6525238032_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251124) | [![The guardian of the waters](https://www.bing.com/th?id=OHR.LeshanBuddha_EN-US6412307232_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251123) | [![Sealed with a hello](https://www.bing.com/th?id=OHR.SealWaving_EN-US6277930581_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251122) | 
| **[Nature's secret code](https://bing.codexun.com/us/detail/20251124)**<br>Ammonite fossil from Madagascar<br>*2025-11-24* | **[The guardian of the waters](https://bing.codexun.com/us/detail/20251123)**<br>Leshan Giant Buddha, Sichuan, China<br>*2025-11-23* | **[Sealed with a hello](https://bing.codexun.com/us/detail/20251122)**<br>Harbor seals at Robert Moses State Park, Long Island, New York<br>*2025-11-22* | 
| [![Sketched into history](https://www.bing.com/th?id=OHR.SaypeGeneva_EN-US6121087903_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251121) | [![Stone, symbol, and a nation's story](https://www.bing.com/th?id=OHR.BudapestParliament_EN-US5929195878_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251120) | [![Fall's feathered headliner](https://www.bing.com/th?id=OHR.AutumnMerganser_EN-US5860535351_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251119) | 
| **[Sketched into history](https://bing.codexun.com/us/detail/20251121)**<br>Artist Saype poses with his land art painting at UN Headquarters, Geneva, Switzerland<br>*2025-11-21* | **[Stone, symbol, and a nation's story](https://bing.codexun.com/us/detail/20251120)**<br>Hungarian Parliament Building, Budapest, Hungary<br>*2025-11-20* | **[Fall's feathered headliner](https://bing.codexun.com/us/detail/20251119)**<br>Male hooded merganser, Oregon<br>*2025-11-19* | 
| [![The trails' call](https://www.bing.com/th?id=OHR.ShenandoahTrail_EN-US8964689271_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251118) | [![Passages with a past](https://www.bing.com/th?id=OHR.LyonTraboules_EN-US9432784340_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251117) | [![Bend it like Nikko](https://www.bing.com/th?id=OHR.IrohazakaAutumn_EN-US9137140715_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/us/detail/20251116) | 
| **[The trails' call](https://bing.codexun.com/us/detail/20251118)**<br>Fall colors in Shenandoah National Park, Virginia<br>*2025-11-18* | **[Passages with a past](https://bing.codexun.com/us/detail/20251117)**<br>A traboule in Lyon, France<br>*2025-11-17* | **[Bend it like Nikko](https://bing.codexun.com/us/detail/20251116)**<br>Irohazaka Road in fall, Nikko, Tochigi, Japan<br>*2025-11-16* | 


---

## Wallpaper Archive by Year

### 2025
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 6px; margin: 12px 0;">
<a href="https://bing.codexun.com/us/archive/202512" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f3f4f6; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease; font-weight: 500;">202512</a>
<a href="https://bing.codexun.com/us/archive/202511" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202511</a>
<a href="https://bing.codexun.com/us/archive/202510" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202510</a>
<a href="https://bing.codexun.com/us/archive/202509" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202509</a>
<a href="https://bing.codexun.com/us/archive/202508" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202508</a>
<a href="https://bing.codexun.com/us/archive/202507" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202507</a>
<a href="https://bing.codexun.com/us/archive/202506" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202506</a>
</div>



---