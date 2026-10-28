# Bing 壁纸数据爬虫与文档生成器

- [English Documentation](README.md)
- [中文文档](README_CN.md)

这是一个自动化的 Bing 壁纸数据收集和文档生成项目，支持多国家/地区的每日壁纸数据抓取、高清图片下载和 Markdown 文档生成。

## 🌟 主要功能

### 📊 数据抓取
- **多国家支持**：支持 34+ 个国家和地区的 Bing 壁纸数据
- **每日自动更新**：通过 GitHub Actions 每天 23:01 UTC 自动运行
- **数据完整性**：保存完整的壁纸元数据，包括标题、版权信息、描述等

### 🖼️ 图片下载
- **高清壁纸**：自动下载 UHD 超高清版本壁纸
- **智能去重**：基于 MD5 哈希值自动检测和删除重复图片
- **增量下载**：只下载新增的壁纸，避免重复下载
- **文件管理**：使用 MD5 值作为文件名，便于管理和去重

### 📝 文档生成
- **自动化文档**：为每个国家生成专门的 Markdown 文档
- **响应式布局**：3列网格布局，适配不同屏幕尺寸
- **多时间维度**：支持今日壁纸、最近30天、按年月归档浏览
- **多语言支持**：支持多种语言的界面文本

## 🗂️ 项目结构

```
项目根目录/
├── .github/workflows/          # GitHub Actions 工作流
│   └── python-app.yml         # 自动化任务配置
├── crawl/                     # 爬虫脚本目录
│   ├── bing_data.py          # 数据抓取脚本
│   ├── download_wallpapers_action.py  # 壁纸下载脚本（Actions版）
│   ├── download_wallpapers.py # 壁纸下载脚本（本地版）
│   ├── generate_markdown.py  # Markdown文档生成脚本
│   ├── generate_readme.py    # README生成脚本
│   └── deduplicate_images.py # 图片去重工具
├── jsonc/                     # 壁纸数据存储
│   ├── us/bing.jsonc         # 美国壁纸数据
│   ├── cn/bing.jsonc         # 中国壁纸数据
│   └── ...                   # 其他国家数据
├── images/                    # 下载的壁纸图片
│   ├── {md5}.jpg             # 以MD5命名的图片文件
│   └── ...
├── markdown/                  # 生成的文档
│   ├── wallpaper-list-us.md  # 美国壁纸文档
│   ├── wallpaper-list-cn.md  # 中国壁纸文档
│   └── ...                   # 其他国家文档
├── messages/                  # 国际化文本
│   ├── us.json               # 英文界面文本
│   ├── cn.json               # 中文界面文本
│   └── ...
├── templates/                 # README模板文件
│   ├── README_template.md    # 英文README模板
│   └── README_CN_template.md # 中文README模板
├── README.md                  # 项目说明文档（自动生成）
└── README_CN.md              # 中文说明文档（自动生成）
```

## 🚀 核心脚本说明

### `bing_data.py` - 数据抓取脚本
- **功能**：从 Bing API 抓取每日壁纸数据
- **输出**：保存到 `jsonc/{country}/bing.jsonc`
- **特性**：
  - 支持 34+ 个国家和地区
  - 自动处理 API 响应和错误
  - 保持数据的时间顺序（最新在前）
  - 增量更新，避免重复数据

### `download_wallpapers_action.py` - 壁纸下载脚本
- **功能**：下载高清壁纸图片并管理文件
- **特性**：
  - **智能跳过**：检查 JSON 中的 `md5` 字段，已下载的跳过
  - **URL构建**：`https://www.bing.com{urlbase}_UHD.jpg`
  - **MD5管理**：计算图片MD5值，用作文件名和去重标识
  - **自动去重**：相同MD5的图片自动删除重复文件
  - **数据更新**：将MD5值写回JSON数据中

### `generate_markdown.py` - 文档生成脚本
- **功能**：生成美观的 Markdown 壁纸文档
- **输出**：保存到 `markdown/wallpaper-list-{country}.md`
- **特性**：
  - **今日壁纸**：展示当天的特色壁纸
  - **最近30天**：3列网格布局展示最近壁纸
  - **归档导航**：按年月组织的历史壁纸浏览
  - **响应式设计**：适配不同设备的显示效果
  - **多语言支持**：根据国家显示对应语言的界面

### `generate_readme.py` - README生成脚本
- **功能**：自动生成中英文README文档
- **输入**：从 `templates/README_template.md` 和 `templates/README_CN_template.md` 读取模板
- **输出**：更新项目根目录的 `README.md` 和 `README_CN.md`
- **特性**：
  - **基于模板**：使用模板文件避免覆盖基础内容
  - **国家链接**：生成所有国家壁纸文档的链接
  - **今日壁纸**：嵌入今日特色壁纸（英文版显示美国，中文版显示中国）
  - **双语支持**：同时生成英文和中文版本
  - **自动更新**：与其他自动化任务一起每日运行

## ⚙️ 自动化工作流

GitHub Actions 每天自动执行以下步骤：

1. **🔄 检出代码** - 获取最新的项目代码
2. **🐍 设置Python环境** - 配置Python运行环境
3. **📦 安装依赖** - 安装 `requests` 等必要库
4. **📊 抓取数据** - 运行 `bing_data.py` 获取最新壁纸数据
5. **🖼️ 下载图片** - 运行 `download_wallpapers_action.py` 下载新壁纸
6. **📝 生成文档** - 运行 `generate_markdown.py` 更新Markdown文档
7. **📄 生成README** - 运行 `generate_readme.py` 更新项目README文件
8. **💾 提交更改** - 自动提交并推送所有更新

## 🌍 支持的国家和地区

项目支持以下 34 个国家和地区：

| 代码 | 国家/地区 | 代码 | 国家/地区 | 代码 | 国家/地区 |
|------|-----------|------|-----------|------|-----------|
| `ar` | [🇦🇷 阿根廷](markdown/wallpaper-list-ar.md) | `au` | [🇦🇺 澳大利亚](markdown/wallpaper-list-au.md) | `br` | [🇧🇷 巴西](markdown/wallpaper-list-br.md) | 
| `ca` | [🇨🇦 加拿大](markdown/wallpaper-list-ca.md) | `cn` | [🇨🇳 中国](markdown/wallpaper-list-cn.md) | `cz` | [🇨🇿 捷克](markdown/wallpaper-list-cz.md) | 
| `de` | [🇩🇪 德国](markdown/wallpaper-list-de.md) | `dk` | [🇩🇰 丹麦](markdown/wallpaper-list-dk.md) | `es` | [🇪🇸 西班牙](markdown/wallpaper-list-es.md) | 
| `fi` | [🇫🇮 芬兰](markdown/wallpaper-list-fi.md) | `fr` | [🇫🇷 法国](markdown/wallpaper-list-fr.md) | `gb` | [🇬🇧 英国](markdown/wallpaper-list-gb.md) | 
| `gr` | [🇬🇷 希腊](markdown/wallpaper-list-gr.md) | `hk` | [🇭🇰 香港](markdown/wallpaper-list-hk.md) | `id` | [🇮🇩 印度尼西亚](markdown/wallpaper-list-id.md) | 
| `in` | [🇮🇳 印度](markdown/wallpaper-list-in.md) | `it` | [🇮🇹 意大利](markdown/wallpaper-list-it.md) | `jp` | [🇯🇵 日本](markdown/wallpaper-list-jp.md) | 
| `kr` | [🇰🇷 韩国](markdown/wallpaper-list-kr.md) | `my` | [🇲🇾 马来西亚](markdown/wallpaper-list-my.md) | `nl` | [🇳🇱 荷兰](markdown/wallpaper-list-nl.md) | 
| `no` | [🇳🇴 挪威](markdown/wallpaper-list-no.md) | `pl` | [🇵🇱 波兰](markdown/wallpaper-list-pl.md) | `pt` | [🇵🇹 葡萄牙](markdown/wallpaper-list-pt.md) | 
| `ru` | [🇷🇺 俄罗斯](markdown/wallpaper-list-ru.md) | `se` | [🇸🇪 瑞典](markdown/wallpaper-list-se.md) | `sg` | [🇸🇬 新加坡](markdown/wallpaper-list-sg.md) | 
| `th` | [🇹🇭 泰国](markdown/wallpaper-list-th.md) | `tr` | [🇹🇷 土耳其](markdown/wallpaper-list-tr.md) | `tw` | [🇹🇼 台湾](markdown/wallpaper-list-tw.md) | 
| `ua` | [🇺🇦 乌克兰](markdown/wallpaper-list-ua.md) | `us` | [🇺🇸 美国](markdown/wallpaper-list-us.md) | `vn` | [🇻🇳 越南](markdown/wallpaper-list-vn.md) | 
| `za` | [🇿🇦 南非](markdown/wallpaper-list-za.md) |  |  |
## 🛠️ 本地使用

### 环境要求
- Python 3.7+
- `requests` 库

### 安装依赖
```bash
pip install requests
```

### 手动执行

```bash
# 1. 抓取壁纸数据
python crawl/bing_data.py

# 2. 下载壁纸图片
python crawl/download_wallpapers_action.py

# 3. 生成Markdown文档
python crawl/generate_markdown.py

# 4. 生成README文档
python crawl/generate_readme.py
```

### 图片去重工具
```bash
# 清理重复的图片文件
python crawl/deduplicate_images.py
```

## 📋 生成的文档特性

每个生成的 Markdown 文档包含：

### 🎯 今日壁纸
- 高清壁纸预览图
- 详细描述和版权信息
- 点击查看详情页面链接

### 📅 最近30天
- 3列响应式网格布局
- 每张壁纸的缩略图和基本信息
- 格式化的日期显示

### 🗃️ 归档导航
- 按年份分组的月份导航
- 当前月份高亮显示
- 美观的按钮样式设计

### 🌐 多语言支持
- 根据国家自动选择界面语言
- 支持英文、中文、德文、法文、日文等
- 可扩展的国际化框架

## 🔧 配置说明

### GitHub Actions 配置
工作流配置文件：`.github/workflows/python-app.yml`

```yaml
name: Generate Bing Wallpaper Json Auto
on:
  schedule:
    - cron: '1 23 * * *'  # 每天23:01 UTC执行
  workflow_dispatch:      # 支持手动触发

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

### 数据格式
每个壁纸数据项包含以下字段：
- `startdate` / `enddate`：壁纸的开始和结束日期
- `url` / `urlbase`：壁纸的URL信息
- `copyright`：版权信息
- `title`：壁纸标题
- `md5`：图片文件的MD5哈希值（下载后添加）
- `MediaContent`：媒体内容详细信息

## 🎨 特色功能

### 智能下载管理
- ✅ **增量下载**：只下载没有 `md5` 字段的新壁纸
- ✅ **自动去重**：基于MD5哈希避免重复图片
- ✅ **错误处理**：网络异常时优雅处理，不中断流程
- ✅ **详细日志**：提供清晰的处理进度和结果统计

### 文档生成优化
- ✅ **响应式设计**：适配桌面和移动设备
- ✅ **SEO友好**：结构化的标题和元数据
- ✅ **快速加载**：优化的图片链接和布局
- ✅ **用户体验**：直观的导航和浏览体验

### 自动化运维
- ✅ **定时执行**：每日自动更新，无需人工干预
- ✅ **错误监控**：GitHub Actions 提供执行状态监控
- ✅ **版本控制**：所有更改都有完整的Git历史记录
- ✅ **可扩展性**：易于添加新的国家和功能

## 📈 项目统计

- **支持国家**：34+ 个国家和地区
- **数据格式**：JSON/JSONC 结构化存储
- **图片质量**：UHD 超高清（通常 3840x2160 或更高）
- **更新频率**：每日自动更新
- **文档格式**：Markdown，GitHub 完美兼容

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request 来改进这个项目！

## 📄 许可证

本项目仅用于学习和研究目的。所有壁纸版权归 Microsoft Bing 和相应的摄影师/版权所有者所有。

---

*最后更新：2025年8月*

## 🌍 各国壁纸链接

点击下方链接查看各国的壁纸：

| [🇦🇷 阿根廷](https://bing.codexun.com/ar) | [🇦🇺 澳大利亚](https://bing.codexun.com/au) | [🇧🇷 巴西](https://bing.codexun.com/br) | [🇨🇦 加拿大](https://bing.codexun.com/ca) | [🇨🇳 中国](https://bing.codexun.com/cn) | 
|:---:|:---:|:---:|:---:|:---:|
| [🇨🇿 捷克](https://bing.codexun.com/cz) | [🇩🇪 德国](https://bing.codexun.com/de) | [🇩🇰 丹麦](https://bing.codexun.com/dk) | [🇪🇸 西班牙](https://bing.codexun.com/es) | [🇫🇮 芬兰](https://bing.codexun.com/fi) | 
| [🇫🇷 法国](https://bing.codexun.com/fr) | [🇬🇧 英国](https://bing.codexun.com/gb) | [🇬🇷 希腊](https://bing.codexun.com/gr) | [🇭🇰 香港](https://bing.codexun.com/hk) | [🇮🇩 印度尼西亚](https://bing.codexun.com/id) | 
| [🇮🇳 印度](https://bing.codexun.com/in) | [🇮🇹 意大利](https://bing.codexun.com/it) | [🇯🇵 日本](https://bing.codexun.com/jp) | [🇰🇷 韩国](https://bing.codexun.com/kr) | [🇲🇾 马来西亚](https://bing.codexun.com/my) | 
| [🇳🇱 荷兰](https://bing.codexun.com/nl) | [🇳🇴 挪威](https://bing.codexun.com/no) | [🇵🇱 波兰](https://bing.codexun.com/pl) | [🇵🇹 葡萄牙](https://bing.codexun.com/pt) | [🇷🇺 俄罗斯](https://bing.codexun.com/ru) | 
| [🇸🇪 瑞典](https://bing.codexun.com/se) | [🇸🇬 新加坡](https://bing.codexun.com/sg) | [🇹🇭 泰国](https://bing.codexun.com/th) | [🇹🇷 土耳其](https://bing.codexun.com/tr) | [🇹🇼 台湾](https://bing.codexun.com/tw) | 
| [🇺🇦 乌克兰](https://bing.codexun.com/ua) | [🇺🇸 美国](https://bing.codexun.com/us) | [🇻🇳 越南](https://bing.codexun.com/vn) | [🇿🇦 南非](https://bing.codexun.com/za) |  | 


## 今日壁纸

[![历史守望之地](https://www.bing.com/th?id=OHR.KuneticeCastle_ZH-CN8895858920_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20261028)

**历史守望之地**

这些城墙会讲述怎样的故事？库涅季采山城堡高踞于捷克波希米亚东部，见证了数百年的历史。城堡的历史可追溯至14世纪末，后来逐渐发展为一座宏伟的要塞和贵族宅邸。它地势高耸，可俯瞰周围乡野，也因此成为一处重要据点。

*© Marek Saroch/Alamy (Bing China)*

---

## 最近30天

| | | |
|:---:|:---:|:---:|
| [![历史守望之地](https://www.bing.com/th?id=OHR.KuneticeCastle_ZH-CN8895858920_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20261028) | [![大自然的金色明镜](https://www.bing.com/th?id=OHR.PondCypress_ZH-CN9472607734_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20261027) | [![大自然的秋日乐章](https://www.bing.com/th?id=OHR.SitovoWaterfall_ZH-CN8495214046_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20261026) | 
| **[历史守望之地](https://bing.codexun.com/cn/detail/20261028)**<br>库涅季采山城堡，波希米亚，捷克<br>*2026-10-28* | **[大自然的金色明镜](https://bing.codexun.com/cn/detail/20261027)**<br>秋叶缤纷的池杉林，乔治亚州，美国<br>*2026-10-27* | **[大自然的秋日乐章](https://bing.codexun.com/cn/detail/20261026)**<br>秋日瀑布，西托沃附近，普罗夫迪夫州，保加利亚<br>*2026-10-26* | 
| [![群峰与宁静相遇之地](https://www.bing.com/th?id=OHR.MaligneFest_ZH-CN8343066766_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20261025) | [![书香里的极致华美](https://www.bing.com/th?id=OHR.PortugueseLibrary_ZH-CN7096893027_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20261024) | [![荒野伙伴](https://www.bing.com/th?id=OHR.YellowstoneWolves_ZH-CN6767268961_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20261023) | 
| **[群峰与宁静相遇之地](https://bing.codexun.com/cn/detail/20261025)**<br>玛琳湖，贾斯珀国家公园，艾伯塔省，加拿大<br>*2026-10-25* | **[书香里的极致华美](https://bing.codexun.com/cn/detail/20261024)**<br>皇家葡萄牙语阅览室，里约热内卢，巴西<br>*2026-10-24* | **[荒野伙伴](https://bing.codexun.com/cn/detail/20261023)**<br>两只灰狼，黄石国家公园，怀俄明州，美国<br>*2026-10-23* | 
| [![静水映斑斓](https://www.bing.com/th?id=OHR.NaejangsanNP_ZH-CN6538893004_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20261022) | [![飞掠河面](https://www.bing.com/th?id=OHR.VietnamBridge_ZH-CN6134321119_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20261021) | [![慢节奏生活](https://www.bing.com/th?id=OHR.BrownSloth_ZH-CN5776383136_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20261020) | 
| **[静水映斑斓](https://bing.codexun.com/cn/detail/20261022)**<br>内藏山国立公园的秋景，韩国<br>*2026-10-22* | **[飞掠河面](https://bing.codexun.com/cn/detail/20261021)**<br>香江上的阮潢桥，顺化，越南<br>*2026-10-21* | **[慢节奏生活](https://bing.codexun.com/cn/detail/20261020)**<br>褐喉三趾树懒，塔拉曼卡旧港，哥斯达黎加<br>*2026-10-20* | 
| [![水上通衢](https://www.bing.com/th?id=OHR.VeniceSunrise_ZH-CN5251815339_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20261019) | [![75载，风华正茂](https://www.bing.com/th?id=OHR.DolbadarnWales_ZH-CN3649667806_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20261018) | [![发掘尘封的过去](https://www.bing.com/th?id=OHR.ChauvetPaintingsFrance_ZH-CN3150703955_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20261017) | 
| **[水上通衢](https://bing.codexun.com/cn/detail/20261019)**<br>大运河，威尼斯，意大利<br>*2026-10-19* | **[75载，风华正茂](https://bing.codexun.com/cn/detail/20261018)**<br>多巴达恩城堡，兰贝里斯，斯诺登尼亚国家公园，威尔士<br>*2026-10-18* | **[发掘尘封的过去](https://bing.codexun.com/cn/detail/20261017)**<br>肖维岩洞艺术作品等比例复制品，瓦隆蓬达尔克，法国<br>*2026-10-17* | 
| [![一窥科罗拉多群峰](https://www.bing.com/th?id=OHR.SneffelsAutumn_ZH-CN3002661429_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20261016) | [![桥梁、屋顶与暮色](https://www.bing.com/th?id=OHR.WroclawPoland_ZH-CN6042428292_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20261015) | [![穿越时间的螺旋](https://www.bing.com/th?id=OHR.AmmoniteFossils_ZH-CN5825251327_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20261014) | 
| **[一窥科罗拉多群峰](https://bing.codexun.com/cn/detail/20261016)**<br>斯奈费尔斯山，里奇韦附近的圣胡安山脉，科罗拉多州，美国<br>*2026-10-16* | **[桥梁、屋顶与暮色](https://bing.codexun.com/cn/detail/20261015)**<br>弗罗茨瓦夫集市广场景观，摄自女巫桥，弗罗茨瓦夫，波兰<br>*2026-10-15* | **[穿越时间的螺旋](https://bing.codexun.com/cn/detail/20261014)**<br>侏罗纪时期的菊石化石<br>*2026-10-14* | 
| [![蓝与绿的交响曲](https://www.bing.com/th?id=OHR.PlitviceAutumn_ZH-CN5646237897_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20261013) | [![从铁轨到潮汐](https://www.bing.com/th?id=OHR.MumblesSwansea2026_ZH-CN5419531039_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20261012) | [![秋色中转动的水轮](https://www.bing.com/th?id=OHR.BabcockSP_ZH-CN5266848536_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20261011) | 
| **[蓝与绿的交响曲](https://bing.codexun.com/cn/detail/20261013)**<br>普利特维采湖群国家公园，克罗地亚<br>*2026-10-13* | **[从铁轨到潮汐](https://bing.codexun.com/cn/detail/20261012)**<br>曼布尔斯码头，斯旺西，威尔士<br>*2026-10-12* | **[秋色中转动的水轮](https://bing.codexun.com/cn/detail/20261011)**<br>格莱德溪磨坊，巴布科克州立公园，西弗吉尼亚州，美国<br>*2026-10-11* | 
| [![迁飞路线上的生命](https://www.bing.com/th?id=OHR.CormorantsFlight_ZH-CN0770863330_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20261010) | [![科西嘉岛的岩石前哨](https://www.bing.com/th?id=OHR.IlesSanguinaires_ZH-CN3149346035_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20261009) | [![现在你“海”能看见我……](https://www.bing.com/th?id=OHR.MayotteOctopus_ZH-CN2837659998_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20261008) | 
| **[迁飞路线上的生命](https://bing.codexun.com/cn/detail/20261010)**<br>蒙特雷湾上空的双冠鸬鹚，加利福尼亚州，美国<br>*2026-10-10* | **[科西嘉岛的岩石前哨](https://bing.codexun.com/cn/detail/20261009)**<br>桑吉奈尔群岛景观，摄自科西嘉岛，法国<br>*2026-10-09* | **[现在你“海”能看见我……](https://bing.codexun.com/cn/detail/20261008)**<br>印度洋马约特岛，一只呈防御姿态的章鱼<br>*2026-10-08* | 
| [![迷惑不解？沿着小径走](https://www.bing.com/th?id=OHR.ForestofDean_ZH-CN2654753621_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20261007) | [![条纹中的地球故事](https://www.bing.com/th?id=OHR.DanxiaLandform_ZH-CN2386060246_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20261006) | [![纵身一跃，一次一课](https://www.bing.com/th?id=OHR.AdelieTeacher_ZH-CN2201820679_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20261005) | 
| **[迷惑不解？沿着小径走](https://bing.codexun.com/cn/detail/20261007)**<br>覆满苔藓的岩石，英国格洛斯特郡谜林，迪恩森林，格洛斯特郡，英格兰<br>*2026-10-07* | **[条纹中的地球故事](https://bing.codexun.com/cn/detail/20261006)**<br>丹霞地貌，张掖国家地质公园，甘肃省，中国<br>*2026-10-06* | **[纵身一跃，一次一课](https://bing.codexun.com/cn/detail/20261005)**<br>南极洲的阿德利企鹅<br>*2026-10-05* | 
| [![宇宙在召唤](https://www.bing.com/th?id=OHR.ArtemisRocket_ZH-CN1768541365_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20261004) | [![捕捉、进食、重复](https://www.bing.com/th?id=OHR.GrizzlySwim_ZH-CN1005455737_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20261003) | [![一条值得保护的河流](https://www.bing.com/th?id=OHR.ChattoogaRiver_ZH-CN9453791496_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20261002) | 
| **[宇宙在召唤](https://bing.codexun.com/cn/detail/20261004)**<br>阿尔忒弥斯1号月球火箭，39B发射台，肯尼迪航天中心，佛罗里达州，2022年6月15日<br>*2026-10-04* | **[捕捉、进食、重复](https://bing.codexun.com/cn/detail/20261003)**<br>美国阿拉斯加州克拉克湖国家公园和自然保护区银鲑溪中的棕熊<br>*2026-10-03* | **[一条值得保护的河流](https://bing.codexun.com/cn/detail/20261002)**<br>查图加河，阿巴拉契亚山脉，北卡罗来纳州，美国<br>*2026-10-02* | 
| [![在花岗岩中读懂时间](https://www.bing.com/th?id=OHR.OlmstedPoint_ZH-CN4182671075_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20261001) | [![一张令人过目难忘的脸](https://www.bing.com/th?id=OHR.BeardReedling_ZH-CN2750632320_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260930) | [![冰川孕育之河](https://www.bing.com/th?id=OHR.KasilofRiver_ZH-CN2394091052_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260929) | 
| **[在花岗岩中读懂时间](https://bing.codexun.com/cn/detail/20261001)**<br>奥姆斯特德观景点的日落，优胜美地国家公园，加利福尼亚州，美国<br>*2026-10-01* | **[一张令人过目难忘的脸](https://bing.codexun.com/cn/detail/20260930)**<br>雄性文须雀，诺福克郡，英格兰<br>*2026-09-30* | **[冰川孕育之河](https://bing.codexun.com/cn/detail/20260929)**<br>卡西洛夫河冰川融水滋养的湛蓝河水，阿拉斯加州，美国<br>*2026-09-29* | 


---

## 按年份浏览壁纸档案

### 2026
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 6px; margin: 12px 0;">
<a href="https://bing.codexun.com/cn/archive/202610" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f3f4f6; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease; font-weight: 500;">202610</a>
<a href="https://bing.codexun.com/cn/archive/202609" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202609</a>
<a href="https://bing.codexun.com/cn/archive/202608" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202608</a>
<a href="https://bing.codexun.com/cn/archive/202607" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202607</a>
<a href="https://bing.codexun.com/cn/archive/202606" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202606</a>
<a href="https://bing.codexun.com/cn/archive/202605" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202605</a>
<a href="https://bing.codexun.com/cn/archive/202604" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202604</a>
<a href="https://bing.codexun.com/cn/archive/202603" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202603</a>
<a href="https://bing.codexun.com/cn/archive/202602" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202602</a>
<a href="https://bing.codexun.com/cn/archive/202601" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202601</a>
</div>

### 2025
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 6px; margin: 12px 0;">
<a href="https://bing.codexun.com/cn/archive/202512" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202512</a>
<a href="https://bing.codexun.com/cn/archive/202511" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202511</a>
<a href="https://bing.codexun.com/cn/archive/202510" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202510</a>
<a href="https://bing.codexun.com/cn/archive/202509" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202509</a>
<a href="https://bing.codexun.com/cn/archive/202508" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202508</a>
<a href="https://bing.codexun.com/cn/archive/202507" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202507</a>
<a href="https://bing.codexun.com/cn/archive/202506" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202506</a>
</div>



---