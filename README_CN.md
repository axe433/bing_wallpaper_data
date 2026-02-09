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

[![海妖歌唱之处](https://www.bing.com/th?id=OHR.IbizaIslets_ZH-CN4580106286_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260210)

**海妖歌唱之处**

在西班牙伊维萨岛西南海域，矗立着两座无人居住的小岛——埃斯韦德拉和埃斯韦德拉内尔。它们属于受保护的自然保留区，以独特的生态价值和震撼的视觉效果闻名。埃斯韦德拉几乎垂直从海中升起，高约1300英尺，陡峭的石灰岩峭壁宛如一座孤立的山脉。不远处的埃斯韦德拉内尔轮廓锋利，因形似伏卧的巨龙而被称为“沉睡的巨龙”，与主岛的高峻挺拔相互映衬。

*© L. Apolli/Getty Images (Bing China)*

---

## 最近30天

| | | |
|:---:|:---:|:---:|
| [![海妖歌唱之处](https://www.bing.com/th?id=OHR.IbizaIslets_ZH-CN4580106286_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260210) | [![斑纹流转](https://www.bing.com/th?id=OHR.LeopardCat_ZH-CN4431427444_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260209) | [![从宁静的夜晚到充满冒险的白天](https://www.bing.com/th?id=OHR.CorfuGreece_ZH-CN4305970968_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260208) | 
| **[海妖歌唱之处](https://bing.codexun.com/cn/detail/20260210)**<br>埃斯韦德拉岛和埃斯韦德拉内尔岛，伊维萨岛，西班牙<br>*2026-02-10* | **[斑纹流转](https://bing.codexun.com/cn/detail/20260209)**<br>阿穆尔豹猫，俄罗斯<br>*2026-02-09* | **[从宁静的夜晚到充满冒险的白天](https://bing.codexun.com/cn/detail/20260208)**<br>科孚岛的夜晚, 希腊<br>*2026-02-08* | 
| [![在盐沼与天空之间，万物静谧](https://www.bing.com/th?id=OHR.SalarUyuni_ZH-CN4163237089_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260207) | [![拉古塞拉——奥运赛季的巅峰](https://www.bing.com/th?id=OHR.GiauPass_ZH-CN3901214501_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260206) | [![困在网格里](https://www.bing.com/th?id=OHR.MaltaSalt_ZH-CN7025158187_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260205) | 
| **[在盐沼与天空之间，万物静谧](https://bing.codexun.com/cn/detail/20260207)**<br>玻利维亚乌尤尼盐湖<br>*2026-02-07* | **[拉古塞拉——奥运赛季的巅峰](https://bing.codexun.com/cn/detail/20260206)**<br>贾乌山口的拉古塞拉峰, 在科尔蒂纳丹佩佐附近, 意大利<br>*2026-02-06* | **[困在网格里](https://bing.codexun.com/cn/detail/20260205)**<br>戈佐岛上的盐田, 马耳他<br>*2026-02-05* | 
| [![优雅掠过天际](https://www.bing.com/th?id=OHR.BigGardenBirdwatch2026_ZH-CN6864628198_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260204) | [![太浩湖视觉盛宴](https://www.bing.com/th?id=OHR.FanetteIsland_ZH-CN6466809551_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260203) | [![影子的承诺](https://www.bing.com/th?id=OHR.AlpineMarmots_ZH-CN6323637910_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260202) | 
| **[优雅掠过天际](https://bing.codexun.com/cn/detail/20260204)**<br>雪中​​的红鸢<br>*2026-02-04* | **[太浩湖视觉盛宴](https://bing.codexun.com/cn/detail/20260203)**<br>翡翠湾和范内特岛, 太浩湖, 加利福尼亚州, 美国<br>*2026-02-03* | **[影子的承诺](https://bing.codexun.com/cn/detail/20260202)**<br>阿尔卑斯山土拨鼠, 霍赫陶恩国家公园, 奥地利<br>*2026-02-02* | 
| [![奇迹之墙](https://www.bing.com/th?id=OHR.Olinda_ZH-CN6216385346_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260201) | [![一见钟情](https://www.bing.com/th?id=OHR.EtoshaZebra_ZH-CN6068087794_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260131) | [![海潮退却之处](https://www.bing.com/th?id=OHR.StMichaelsCornwall_ZH-CN5878042411_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260130) | 
| **[奇迹之墙](https://bing.codexun.com/cn/detail/20260201)**<br>奥林达的彩色房子, 巴西<br>*2026-02-01* | **[一见钟情](https://bing.codexun.com/cn/detail/20260131)**<br>平原斑马, 埃托沙国家公园, 纳米比亚<br>*2026-01-31* | **[海潮退却之处](https://bing.codexun.com/cn/detail/20260130)**<br>马拉齐翁的圣迈克尔山, 康沃尔郡, 英格兰<br>*2026-01-30* | 
| [![密尔沃基的传奇故事](https://www.bing.com/th?id=OHR.MilwaukeeHall_ZH-CN5779477975_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260129) | [![随河而行](https://www.bing.com/th?id=OHR.WhanganuiPark_ZH-CN5664518836_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260128) | [![羽翼预告：前方有鹈鹕](https://www.bing.com/th?id=OHR.DalmationPelicans_ZH-CN5252732863_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260127) | 
| **[密尔沃基的传奇故事](https://bing.codexun.com/cn/detail/20260129)**<br>密尔沃基市政厅的八层开放式中庭，威斯康星州，美国<br>*2026-01-29* | **[随河而行](https://bing.codexun.com/cn/detail/20260128)**<br>旺格努伊国家公园，雷塔鲁克，新西兰<br>*2026-01-28* | **[羽翼预告：前方有鹈鹕](https://bing.codexun.com/cn/detail/20260127)**<br>卷羽鹈鹕，凯尔基尼湖，希腊<br>*2026-01-27* | 
| [![巴伐利亚的瑰宝](https://www.bing.com/th?id=OHR.NeuschwansteinWinter_ZH-CN4972014681_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260126) | [![传统熠熠生辉](https://www.bing.com/th?id=OHR.BurnsPark_ZH-CN4442772228_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260125) | [![瑞士山间的短逃离](https://www.bing.com/th?id=OHR.AndermattSwiss_ZH-CN4112824348_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260124) | 
| **[巴伐利亚的瑰宝](https://bing.codexun.com/cn/detail/20260126)**<br>新天鹅堡，巴伐利亚州，德国<br>*2026-01-26* | **[传统熠熠生辉](https://bing.codexun.com/cn/detail/20260125)**<br>伯恩斯国家遗产公园，艾尔，南艾尔郡，苏格兰<br>*2026-01-25* | **[瑞士山间的短逃离](https://bing.codexun.com/cn/detail/20260124)**<br>阿尔卑斯山脉的安德马特小镇，瑞士<br>*2026-01-24* | 
| [![霜雪中的盛宴](https://www.bing.com/th?id=OHR.IcelandSheep_ZH-CN3931993073_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260123) | [![波西米亚温泉故事](https://www.bing.com/th?id=OHR.KarlovyVary_ZH-CN7585938362_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260122) | [![冬日白雪中的一抹红](https://www.bing.com/th?id=OHR.BerrySquirrel_ZH-CN7382553646_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260121) | 
| **[霜雪中的盛宴](https://bing.codexun.com/cn/detail/20260123)**<br>绵羊在雪地里吃草，冰岛<br>*2026-01-23* | **[波西米亚温泉故事](https://bing.codexun.com/cn/detail/20260122)**<br>卡罗维瓦利，波西米亚，捷克共和国<br>*2026-01-22* | **[冬日白雪中的一抹红](https://bing.codexun.com/cn/detail/20260121)**<br>欧亚红松鼠<br>*2026-01-21* | 
| [![冬季里的呆萌小可爱](https://www.bing.com/th?id=OHR.TheGreatColdY25_ZH-CN7239762815_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260120) | [![大自然的波普艺术](https://www.bing.com/th?id=OHR.BubblesAbraham_ZH-CN7203734882_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260119) | [![伪装成沙漠的奇境](https://www.bing.com/th?id=OHR.WhiteSandsNM_ZH-CN7070772772_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260118) | 
| **[冬季里的呆萌小可爱](https://bing.codexun.com/cn/detail/20260120)**<br>栖息在树枝上的北长尾山雀，大庆市，中国黑龙江省<br>*2026-01-20* | **[大自然的波普艺术](https://bing.codexun.com/cn/detail/20260119)**<br>亚伯拉罕湖冰封景象，艾伯塔省，加拿大<br>*2026-01-19* | **[伪装成沙漠的奇境](https://bing.codexun.com/cn/detail/20260118)**<br>白沙国家公园，新墨西哥州，美国<br>*2026-01-18* | 
| [![普雷比希托广场上的穹顶](https://www.bing.com/th?id=OHR.NaplesBasilica_ZH-CN6888150174_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260117) | [![眼神对上了](https://www.bing.com/th?id=OHR.EtoshaLeopard_ZH-CN6654006040_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260116) | [![小村庄，大视野](https://www.bing.com/th?id=OHR.ReineSunrise_ZH-CN6297586399_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260115) | 
| **[普雷比希托广场上的穹顶](https://bing.codexun.com/cn/detail/20260117)**<br>保罗圣方济圣殿，那不勒斯，意大利<br>*2026-01-17* | **[眼神对上了](https://bing.codexun.com/cn/detail/20260116)**<br>埃托沙国家公园的豹子，纳米比亚<br>*2026-01-16* | **[小村庄，大视野](https://bing.codexun.com/cn/detail/20260115)**<br>雷讷渔村, 挪威<br>*2026-01-15* | 
| [![帕拉米蒂的历史之阶](https://www.bing.com/th?id=OHR.PalamidiFortress_ZH-CN5420143053_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260114) | [![苹果韵，旧时光](https://www.bing.com/th?id=OHR.WalesWinter_ZH-CN3692879767_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260113) | [![水獭之国爱沙尼亚](https://www.bing.com/th?id=OHR.SnowOtters_ZH-CN3563991803_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260112) | 
| **[帕拉米蒂的历史之阶](https://bing.codexun.com/cn/detail/20260114)**<br>帕拉米蒂要塞的阶梯, 纳夫普利翁, 希腊<br>*2026-01-14* | **[苹果韵，旧时光](https://bing.codexun.com/cn/detail/20260113)**<br>克卢伊德谷, 威尔士<br>*2026-01-13* | **[水獭之国爱沙尼亚](https://bing.codexun.com/cn/detail/20260112)**<br>欧亚水獭和幼崽, 爱沙尼亚<br>*2026-01-12* | 


---

## 按年份浏览壁纸档案

### 2026
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 6px; margin: 12px 0;">
<a href="https://bing.codexun.com/cn/archive/202602" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f3f4f6; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease; font-weight: 500;">202602</a>
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