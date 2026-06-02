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

[![穿行于蓝色之间](https://www.bing.com/th?id=OHR.Qinghai_ZH-CN9899656327_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260602)

**穿行于蓝色之间**

在青藏高原北缘、中国西部的荒漠之中，西台吉乃尔湖以一种超现实的姿态横跨在偏远的柴达木盆地。315国道的一段延伸线直接纵贯其浅水区，营造出一种公路悬浮于两个世界之间的视觉错觉。受卤水中矿物质浓度差异的影响，湖水呈现出鲜明的对比：一侧常显深邃的蓝色，另一侧则呈现柔和的绿色。

*© Kaicheng Xu/Getty Images (Bing China)*

---

## 最近30天

| | | |
|:---:|:---:|:---:|
| [![穿行于蓝色之间](https://www.bing.com/th?id=OHR.Qinghai_ZH-CN9899656327_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260602) | [![历史的况味](https://www.bing.com/th?id=OHR.OlivaPalermo_ZH-CN9639920195_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260601) | [![顺流而行](https://www.bing.com/th?id=OHR.EvergladesWetlands_ZH-CN9515366484_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260531) | 
| **[穿行于蓝色之间](https://bing.codexun.com/cn/detail/20260602)**<br>穿越西台吉乃尔湖的公路，青海省，中国<br>*2026-06-02* | **[历史的况味](https://bing.codexun.com/cn/detail/20260601)**<br>巴勒莫暮色下的天际线，西西里岛，意大利<br>*2026-06-01* | **[顺流而行](https://bing.codexun.com/cn/detail/20260531)**<br>大沼泽地国家公园航拍景观，佛罗里达州，美国<br>*2026-05-31* | 
| [![读懂黑白之间](https://www.bing.com/th?id=OHR.EquusQuagga_ZH-CN9323988132_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260530) | [![巅峰历史时刻](https://www.bing.com/th?id=OHR.SummitEverest_ZH-CN9252833251_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260529) | [![设计与秩序相结合](https://www.bing.com/th?id=OHR.HwaesongFortress_ZH-CN8225341972_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260528) | 
| **[读懂黑白之间](https://bing.codexun.com/cn/detail/20260530)**<br>平原斑马幼崽，埃托沙国家公园，纳米比亚<br>*2026-05-30* | **[巅峰历史时刻](https://bing.codexun.com/cn/detail/20260529)**<br>珠穆朗玛峰峰顶，萨加玛塔国家公园，尼泊尔<br>*2026-05-29* | **[设计与秩序相结合](https://bing.codexun.com/cn/detail/20260528)**<br>华城堡的古城墙，水原，韩国<br>*2026-05-28* | 
| [![它们“獭”独一无二](https://www.bing.com/th?id=OHR.OtterDay_ZH-CN7735013625_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260527) | [![羽扇豆书写的季节](https://www.bing.com/th?id=OHR.LupineBloom_ZH-CN7639721663_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260526) | [![石间的清风](https://www.bing.com/th?id=OHR.HawaMahal2026_ZH-CN7233246545_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260525) | 
| **[它们“獭”独一无二](https://bing.codexun.com/cn/detail/20260527)**<br>海獭，霍默卡奇马克湾，阿拉斯加州，美国<br>*2026-05-27* | **[羽扇豆书写的季节](https://bing.codexun.com/cn/detail/20260526)**<br>盛开的羽扇豆，北加利福尼亚州，美国<br>*2026-05-26* | **[石间的清风](https://bing.codexun.com/cn/detail/20260525)**<br>从风之宫殿俯瞰斋浦尔市景，拉贾斯坦邦，印度<br>*2026-05-25* | 
| [![守护欧洲的自然净土](https://www.bing.com/th?id=OHR.DolomitesPark_ZH-CN7134423478_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260524) | [![为龟类喝彩！](https://www.bing.com/th?id=OHR.ThreeTurtlesButterflies_ZH-CN7043849571_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260523) | [![海洋生命的律动](https://www.bing.com/th?id=OHR.KauehiAtollLagoon_ZH-CN9552036080_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260522) | 
| **[守护欧洲的自然净土](https://bing.codexun.com/cn/detail/20260524)**<br>三峰自然公园，南蒂罗尔，意大利<br>*2026-05-24* | **[为龟类喝彩！](https://bing.codexun.com/cn/detail/20260523)**<br>与蝴蝶在一起的乌龟<br>*2026-05-23* | **[海洋生命的律动](https://bing.codexun.com/cn/detail/20260522)**<br>埃希环礁，土阿莫土群岛，法属波利尼西亚<br>*2026-05-22* | 
| [![酿造传承](https://www.bing.com/th?id=OHR.SichuanTea_ZH-CN6703437873_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260521) | [![喧闹从这里开始](https://www.bing.com/th?id=OHR.BumbleBee_ZH-CN6429376340_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260520) | [![马略卡岛的边缘](https://www.bing.com/th?id=OHR.SpainLighthouse_ZH-CN6024263415_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260519) | 
| **[酿造传承](https://bing.codexun.com/cn/detail/20260521)**<br>四川省的茶梯田, 中国<br>*2026-05-21* | **[喧闹从这里开始](https://bing.codexun.com/cn/detail/20260520)**<br>熊蜂在授粉, 伍斯特, 英格兰<br>*2026-05-20* | **[马略卡岛的边缘](https://bing.codexun.com/cn/detail/20260519)**<br>福门托尔灯塔, 马略卡, 巴利阿里群岛, 西班牙<br>*2026-05-19* | 
| [![大厅里的希望](https://www.bing.com/th?id=OHR.MuseumLondon_ZH-CN5602977820_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260518) | [![静谧之巅，喧嚣之景](https://www.bing.com/th?id=OHR.ShenandoahSunset_ZH-CN4399136794_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260517) | [![跌到谷底？这里可不是。](https://www.bing.com/th?id=OHR.SmithRockPark_ZH-CN4210144402_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260516) | 
| **[大厅里的希望](https://bing.codexun.com/cn/detail/20260518)**<br>伦敦自然历史博物馆, 英格兰<br>*2026-05-18* | **[静谧之巅，喧嚣之景](https://bing.codexun.com/cn/detail/20260517)**<br>仙纳度国家公园的玳瑁峰, 弗吉尼亚州, 美国<br>*2026-05-17* | **[跌到谷底？这里可不是。](https://bing.codexun.com/cn/detail/20260516)**<br>史密斯岩州立公园, 俄勒冈州, 美国<br>*2026-05-16* | 
| [![鲸鱼，你会救我吗？](https://www.bing.com/th?id=OHR.EndangeredWhales_ZH-CN4053106967_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260515) | [![一场穿越时空的旅程](https://www.bing.com/th?id=OHR.Pitigliano_ZH-CN1509921892_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260514) | [![银河系，摇滚吧！](https://www.bing.com/th?id=OHR.AlabamaHills_ZH-CN1387018045_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260513) | 
| **[鲸鱼，你会救我吗？](https://bing.codexun.com/cn/detail/20260515)**<br>一群抹香鲸, 印度洋<br>*2026-05-15* | **[一场穿越时空的旅程](https://bing.codexun.com/cn/detail/20260514)**<br>中世纪古镇皮蒂利亚诺, 托斯卡纳, 意大利<br>*2026-05-14* | **[银河系，摇滚吧！](https://bing.codexun.com/cn/detail/20260513)**<br>拱门与银河, 阿拉巴马山, 内华达山脉, 加利福尼亚州, 美国<br>*2026-05-13* | 
| [![振翅, 潜水, 生存](https://www.bing.com/th?id=OHR.Fratercula_ZH-CN1239275412_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260512) | [![水下建筑](https://www.bing.com/th?id=OHR.QueenslandReef_ZH-CN1138150002_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260511) | [![一份经久不衰的羁绊](https://www.bing.com/th?id=OHR.MotherCub_ZH-CN0999123163_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260510) | 
| **[振翅, 潜水, 生存](https://bing.codexun.com/cn/detail/20260512)**<br>北极海鹦, 威尔士<br>*2026-05-12* | **[水下建筑](https://bing.codexun.com/cn/detail/20260511)**<br>从上方俯瞰大堡礁, 昆士兰州, 澳大利亚<br>*2026-05-11* | **[一份经久不衰的羁绊](https://bing.codexun.com/cn/detail/20260510)**<br>北极熊妈妈和幼崽在瓦普斯克国家公园玩耍, 马尼托巴省, 加拿大<br>*2026-05-10* | 
| [![克尔卡的造物主](https://www.bing.com/th?id=OHR.SkradinskiBuk_ZH-CN0882603359_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260509) | [![不仅仅是一声咿呀学语](https://www.bing.com/th?id=OHR.SardinianDonkey_ZH-CN0758031524_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260508) | [![广袤铺展的沙漠](https://www.bing.com/th?id=OHR.Kofa_ZH-CN0584573563_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260507) | 
| **[克尔卡的造物主](https://bing.codexun.com/cn/detail/20260509)**<br>克尔卡国家公园的斯克拉丁斯基布克瀑布, 克罗地亚<br>*2026-05-09* | **[不仅仅是一声咿呀学语](https://bing.codexun.com/cn/detail/20260508)**<br>撒丁岛母驴和幼崽, 法国<br>*2026-05-08* | **[广袤铺展的沙漠](https://bing.codexun.com/cn/detail/20260507)**<br>科法国家野生动物保护区，亚利桑那州，美国<br>*2026-05-07* | 
| [![承受压力之下的平原](https://www.bing.com/th?id=OHR.BulgariaPlains_ZH-CN3853985252_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260506) | [![藕花风起，首夏清和](https://www.bing.com/th?id=OHR.BeginningofSummerY26_ZH-CN7628545617_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260505) | [![科幻源于现实](https://www.bing.com/th?id=OHR.KsarOuledSoltane_ZH-CN3569810663_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260504) | 
| **[承受压力之下的平原](https://bing.codexun.com/cn/detail/20260506)**<br>平原上空的雷暴，保加利亚<br>*2026-05-06* | **[藕花风起，首夏清和](https://bing.codexun.com/cn/detail/20260505)**<br>莲花与莲花植株<br>*2026-05-05* | **[科幻源于现实](https://bing.codexun.com/cn/detail/20260504)**<br>乌莱德·索尔坦克萨尔，塔塔温区，突尼斯南部<br>*2026-05-04* | 


---

## 按年份浏览壁纸档案

### 2026
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 6px; margin: 12px 0;">
<a href="https://bing.codexun.com/cn/archive/202606" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f3f4f6; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease; font-weight: 500;">202606</a>
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