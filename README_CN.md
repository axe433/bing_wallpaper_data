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

[![承载过往的篇章](https://www.bing.com/th?id=OHR.LyonTraboules_ZH-CN8476826325_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251116)

**承载过往的篇章**

在法国里昂，你不只是简单地走过街巷，而是像在城市的脉络中轻盈滑行。这里的穿廊，是一条条隐秘的通道，蜿蜒穿梭于庭院与建筑之间，将简单的散步变成一场寻宝之旅。它们曾是最早的捷径，帮助居民避雨、搬运货物，或悄然穿过中世纪街区。如今，这些通道更多承载的是探索的乐趣。它们的历史可追溯至公元四世纪，在文艺复兴时期更显重要——当时丝绸商人利用这些通道，将珍贵织物从作坊安全运送到河边，免受风雨侵扰。二战期间，抵抗运动战士也曾借助这些通道作为秘密逃生路线。走进里昂，你会发现，每一条穿廊都藏着故事，每一次转角都可能遇见历史的回声。

*© TPopova/Getty Images 法国 (Bing China)*

---

## 最近30天

| | | |
|:---:|:---:|:---:|
| [![承载过往的篇章](https://www.bing.com/th?id=OHR.LyonTraboules_ZH-CN8476826325_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251116) | [![像日光那样“弯道飞驰”](https://www.bing.com/th?id=OHR.IrohazakaAutumn_ZH-CN8146412245_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251115) | [![快节奏时代，别忘了慢下来](https://www.bing.com/th?id=OHR.ManateeBaby_ZH-CN7805040281_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251114) | 
| **[承载过往的篇章](https://bing.codexun.com/cn/detail/20251116)**<br>里昂的一条穿廊，法国<br>*2025-11-16* | **[像日光那样“弯道飞驰”](https://bing.codexun.com/cn/detail/20251115)**<br>秋天的伊吕波坂，日光市，栃木县，日本<br>*2025-11-15* | **[快节奏时代，别忘了慢下来](https://bing.codexun.com/cn/detail/20251114)**<br>海牛妈妈和幼崽，水晶河，佛罗里达州，美国<br>*2025-11-14* | 
| [![星光下的颤动之树](https://www.bing.com/th?id=OHR.AloeDichotoma_ZH-CN4432972312_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251113) | [![条条大路通罗马](https://www.bing.com/th?id=OHR.ColosseumRome_ZH-CN4305271578_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251112) | [![传奇之地](https://www.bing.com/th?id=OHR.ExternsteineSunset_ZH-CN4190155102_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251111) | 
| **[星光下的颤动之树](https://bing.codexun.com/cn/detail/20251113)**<br>夜晚的箭袋树与银河，基特曼斯胡普，纳米比亚<br>*2025-11-13* | **[条条大路通罗马](https://bing.codexun.com/cn/detail/20251112)**<br>斗兽场鸟瞰图，罗马，意大利<br>*2025-11-12* | **[传奇之地](https://bing.codexun.com/cn/detail/20251111)**<br>条顿堡森林的伊克斯坦岩石层，德国<br>*2025-11-11* | 
| [![草原之下的生命](https://www.bing.com/th?id=OHR.PrairieDogTown_ZH-CN3989288881_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251110) | [![从前有一颗星星](https://www.bing.com/th?id=OHR.LagoonNebula_ZH-CN3890147543_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251109) | [![班登的明星岩石](https://www.bing.com/th?id=OHR.BandonBeach_ZH-CN3684356649_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251108) | 
| **[草原之下的生命](https://bing.codexun.com/cn/detail/20251110)**<br>土拨鼠镇的黑尾土拨鼠，劣地国家公园，南达科他州，美国<br>*2025-11-10* | **[从前有一颗星星](https://bing.codexun.com/cn/detail/20251109)**<br>礁湖星云中的星际云，由哈勃太空望远镜拍摄<br>*2025-11-09* | **[班登的明星岩石](https://bing.codexun.com/cn/detail/20251108)**<br>班登海滩的海蚀柱，俄勒冈州，美国<br>*2025-11-08* | 
| [![魅力十足的巨型动物](https://www.bing.com/th?id=OHR.WillowBear_ZH-CN3501489210_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251107) | [![满天心愿](https://www.bing.com/th?id=OHR.LanternsThailand_ZH-CN3419382923_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251106) | [![秋天来了，你开心吗？](https://www.bing.com/th?id=OHR.MoncayoAutumn_ZH-CN5187959516_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251105) | 
| **[魅力十足的巨型动物](https://bing.codexun.com/cn/detail/20251107)**<br>丘吉尔的北极熊，曼尼托巴省，加拿大<br>*2025-11-07* | **[满天心愿](https://bing.codexun.com/cn/detail/20251106)**<br>哈里朋柴佛塔寺的彩色灯笼, 南奔府, 泰国<br>*2025-11-06* | **[秋天来了，你开心吗？](https://bing.codexun.com/cn/detail/20251105)**<br>佩尼亚罗亚山毛榉森林, 蒙卡约自然公园, 萨拉戈萨, 阿拉贡, 西班牙<br>*2025-11-05* | 
| [![小心空隙，桥面将开启！](https://www.bing.com/th?id=OHR.TowerBridgeUK_ZH-CN1846533186_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251104) | [![随波轻舞](https://www.bing.com/th?id=OHR.MexicoJelly_ZH-CN5266285518_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251103) | [![竹林吐纳清气，枫叶绚烂如火](https://www.bing.com/th?id=OHR.KyotoMaple_ZH-CN4730358356_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251102) | 
| **[小心空隙，桥面将开启！](https://bing.codexun.com/cn/detail/20251104)**<br>塔桥, 伦敦, 英格兰<br>*2025-11-04* | **[随波轻舞](https://bing.codexun.com/cn/detail/20251103)**<br>在太平洋中游泳的水母, 格雷罗, 墨西哥<br>*2025-11-03* | **[竹林吐纳清气，枫叶绚烂如火](https://bing.codexun.com/cn/detail/20251102)**<br>岚山缤纷的枫叶与竹林, 京都, 日本<br>*2025-11-02* | 
| [![古老血脉的兽群](https://www.bing.com/th?id=OHR.BisonSprings_ZH-CN4419733534_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251101) | [![在万圣节的魔咒之下](https://www.bing.com/th?id=OHR.BranCastle_ZH-CN3879660917_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251031) | [![蹄声、色彩与传承](https://www.bing.com/th?id=OHR.PushkarFair_ZH-CN2069143641_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251030) | 
| **[古老血脉的兽群](https://bing.codexun.com/cn/detail/20251101)**<br>野牛在温泉边吃草,  黄石国家公园, 怀俄明州, 美国<br>*2025-11-01* | **[在万圣节的魔咒之下](https://bing.codexun.com/cn/detail/20251031)**<br>布兰城堡入口, 布拉索夫, 罗马尼亚<br>*2025-10-31* | **[蹄声、色彩与传承](https://bing.codexun.com/cn/detail/20251030)**<br>杰伊瑟尔梅尔的骆驼, 拉贾斯坦邦, 印度<br>*2025-10-30* | 
| [![时光扎根](https://www.bing.com/th?id=OHR.FanalForest_ZH-CN2203572101_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251029) | [![通往石之奇境的大门](https://www.bing.com/th?id=OHR.TepliceRocks_ZH-CN1785316311_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251028) | [![千年秘境](https://www.bing.com/th?id=OHR.AutumnColorY25_ZH-CN1551135398_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251027) | 
| **[时光扎根](https://bing.codexun.com/cn/detail/20251029)**<br>法纳尔森林里的古老月桂树，马德拉群岛，葡萄牙<br>*2025-10-29* | **[通往石之奇境的大门](https://bing.codexun.com/cn/detail/20251028)**<br>安德尔施帕赫-特普利采岩石林的哥特式拱门, 捷克<br>*2025-10-28* | **[千年秘境](https://bing.codexun.com/cn/detail/20251027)**<br>被胡杨树围绕着的湖, 金塔县, 酒泉, 甘肃, 中国<br>*2025-10-27* | 
| [![南瓜日，今日登场！](https://www.bing.com/th?id=OHR.PumpkinFarm_ZH-CN1232784365_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251026) | [![芬兰的活泥炭地](https://www.bing.com/th?id=OHR.MartimoaapaFinland_ZH-CN1066271356_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251025) | [![从“灰色幽灵”到幽灵传说](https://www.bing.com/th?id=OHR.QueenMary_ZH-CN0468294074_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251024) | 
| **[南瓜日，今日登场！](https://bing.codexun.com/cn/detail/20251026)**<br>北卡罗来纳州的南瓜农场, 美国<br>*2025-10-26* | **[芬兰的活泥炭地](https://bing.codexun.com/cn/detail/20251025)**<br>马蒂莫阿帕沼泽保护区泥炭地鸟瞰图, 芬兰<br>*2025-10-25* | **[从“灰色幽灵”到幽灵传说](https://bing.codexun.com/cn/detail/20251024)**<br>玛丽皇后号邮轮的夜景, 长滩, 加利福尼亚州, 美国<br>*2025-10-24* | 
| [![雪中深情](https://www.bing.com/th?id=OHR.SnowLeopard_ZH-CN6644701381_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251023) | [![刻在石头上](https://www.bing.com/th?id=OHR.BulgariaRocks_ZH-CN0234903972_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251022) | [![鸟喙的故事](https://www.bing.com/th?id=OHR.ToucanForest_ZH-CN0072036253_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251021) | 
| **[雪中深情](https://bing.codexun.com/cn/detail/20251023)**<br>雪豹和她的幼崽, 斯皮提谷, 寒冷沙漠生物圈保护区, 印度<br>*2025-10-23* | **[刻在石头上](https://bing.codexun.com/cn/detail/20251022)**<br>贝洛格拉齐克石林，保加利亚<br>*2025-10-22* | **[鸟喙的故事](https://bing.codexun.com/cn/detail/20251021)**<br>哥斯达黎加的厚嘴巨嘴鸟<br>*2025-10-21* | 
| [![慢节奏的生活](https://www.bing.com/th?id=OHR.HoffmansSloth_ZH-CN7563408641_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251020) | [![痴迷科学](https://www.bing.com/th?id=OHR.AppleHarvest_ZH-CN7317228007_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251019) | [![那座铭记往昔的山丘](https://www.bing.com/th?id=OHR.SilburyHill_ZH-CN6666447580_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251018) | 
| **[慢节奏的生活](https://bing.codexun.com/cn/detail/20251020)**<br>霍氏树懒，厄瓜多尔<br>*2025-10-20* | **[痴迷科学](https://bing.codexun.com/cn/detail/20251019)**<br>即将收获的苹果，明尼苏达州，美国<br>*2025-10-19* | **[那座铭记往昔的山丘](https://bing.codexun.com/cn/detail/20251018)**<br>西尔布利山的新石器时代遗址，蒂尔斯黑德，威尔特郡，英国<br>*2025-10-18* | 


---

## 按年份浏览壁纸档案

### 2025
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 6px; margin: 12px 0;">
<a href="https://bing.codexun.com/cn/archive/202511" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f3f4f6; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease; font-weight: 500;">202511</a>
<a href="https://bing.codexun.com/cn/archive/202510" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202510</a>
<a href="https://bing.codexun.com/cn/archive/202509" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202509</a>
<a href="https://bing.codexun.com/cn/archive/202508" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202508</a>
<a href="https://bing.codexun.com/cn/archive/202507" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202507</a>
<a href="https://bing.codexun.com/cn/archive/202506" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202506</a>
</div>



---