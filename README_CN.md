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

[![天际线上的印记](https://www.bing.com/th?id=OHR.Fujisan_ZH-CN7203975085_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260623)

**天际线上的印记**

富士山是日本最高峰，海拔12,389英尺（约3700米），耸立于本州岛，位于东京西南约60英里（约97公里）处。这座近乎完美的锥形山峰是一座火山——自1707年12月最后一次喷发后便一直处于休眠状态，但仍被归类为活火山。那次大规模喷发被称为宝荣喷发，火山灰和其他火山碎屑喷涌而出，席卷日本东部，甚至远至江户（今东京）。除了地质学意义之外，富士山长期以来被视为神圣的景观和朝圣登山的目的地，这体现了日本自然、宗教和日常生活的交融。这种经久不衰的文化魅力也是它于2013年被联合国教科文组织列为世界遗产的原因之一，被誉为“神圣之地和艺术灵感的源泉”。众所周知，在晴朗的日子里，富士山从远处就能清晰可见，但这并非必然——云层可能在几分钟内将其遮蔽。无论您是徒步攀登，还是只是从火车车窗瞥见它，它依然是日本地平线上的标志性景观。

*© phutthiseth thongtae/Getty Images (Bing China)*

---

## 最近30天

| | | |
|:---:|:---:|:---:|
| [![天际线上的印记](https://www.bing.com/th?id=OHR.Fujisan_ZH-CN7203975085_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260623) | [![一个郁郁葱葱的王国](https://www.bing.com/th?id=OHR.QuinaultFerns_ZH-CN6696428927_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260622) | [![鸟类好爸爸](https://www.bing.com/th?id=OHR.EggDad_ZH-CN6045387630_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260621) | 
| **[天际线上的印记](https://bing.codexun.com/cn/detail/20260623)**<br>本州岛上的富士山, 日本<br>*2026-06-23* | **[一个郁郁葱葱的王国](https://bing.codexun.com/cn/detail/20260622)**<br>奎诺尔特雨林, 奥林匹克国家公园, 华盛顿州, 美国<br>*2026-06-22* | **[鸟类好爸爸](https://bing.codexun.com/cn/detail/20260621)**<br>企鹅爸爸正在检查蛋的情况<br>*2026-06-21* | 
| [![海洋中冰封的大教堂](https://www.bing.com/th?id=OHR.ArchedIceberg_ZH-CN2698040371_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260620) | [![龙吟古韵](https://www.bing.com/th?id=OHR.DragonBoatFestivalY26_ZH-CN3070279417_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260619) | [![坚如磐石的奇观](https://www.bing.com/th?id=OHR.Saqsaywaman_ZH-CN2584038469_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260618) | 
| **[海洋中冰封的大教堂](https://bing.codexun.com/cn/detail/20260620)**<br>漂浮在南极半岛西部海域的拱形冰山, 南大洋<br>*2026-06-20* | **[龙吟古韵](https://bing.codexun.com/cn/detail/20260619)**<br>湖中的龙舟，中国<br>*2026-06-19* | **[坚如磐石的奇观](https://bing.codexun.com/cn/detail/20260618)**<br>萨克赛瓦曼遗址俯瞰图，库斯科，秘鲁<br>*2026-06-18* | 
| [![蜿蜒而上](https://www.bing.com/th?id=OHR.TremolaRoad_ZH-CN8810749250_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260617) | [![蔚蓝海礁的守护者](https://www.bing.com/th?id=OHR.SevenMileTurtle_ZH-CN4346512721_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260616) | [![岁月雕琢，风景始成](https://www.bing.com/th?id=OHR.ParkEstd_ZH-CN3419035151_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260615) | 
| **[蜿蜒而上](https://bing.codexun.com/cn/detail/20260617)**<br>特雷莫拉公路在圣哥达山口，艾罗洛，瑞士<br>*2026-06-17* | **[蔚蓝海礁的守护者](https://bing.codexun.com/cn/detail/20260616)**<br>七英里海滩附近的玳瑁海龟伴侣，大开曼岛，开曼群岛<br>*2026-06-16* | **[岁月雕琢，风景始成](https://bing.codexun.com/cn/detail/20260615)**<br>大烟山国家公园，田纳西州，美国<br>*2026-06-15* | 
| [![潜羽探清波](https://www.bing.com/th?id=OHR.DuckPond_ZH-CN1683101997_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260614) | [![岁月的层峦](https://www.bing.com/th?id=OHR.BadSunset_ZH-CN9050997938_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260613) | [![惊鸿一瞥](https://www.bing.com/th?id=OHR.SpainBeeEater_ZH-CN4424052851_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260612) | 
| **[潜羽探清波](https://bing.codexun.com/cn/detail/20260614)**<br>绿头鸭<br>*2026-06-14* | **[岁月的层峦](https://bing.codexun.com/cn/detail/20260613)**<br>落日，恶地国家公园，南达科他州，美国<br>*2026-06-13* | **[惊鸿一瞥](https://bing.codexun.com/cn/detail/20260612)**<br>黄喉蜂虎，格拉萨莱马山自然公园，加的斯，西班牙<br>*2026-06-12* | 
| [![沉静的力量](https://www.bing.com/th?id=OHR.Limpets_ZH-CN4991771513_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260611) | [![一抹蓝色](https://www.bing.com/th?id=OHR.Hnausapollur_ZH-CN4075343976_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260610) | [![品尝日落](https://www.bing.com/th?id=OHR.CTNPVernazza_ZH-CN3971102271_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260609) | 
| **[沉静的力量](https://bing.codexun.com/cn/detail/20260611)**<br>退潮时裸露在乌尔萨海滩海岸上的帽贝, 葡萄牙<br>*2026-06-11* | **[一抹蓝色](https://bing.codexun.com/cn/detail/20260610)**<br>赫瑙萨波鲁尔火山口, 菲亚拉巴克自然保护区, 兰德曼纳劳加尔, 冰岛<br>*2026-06-10* | **[品尝日落](https://bing.codexun.com/cn/detail/20260609)**<br>韦尔纳扎, 五渔村, 利古里亚, 意大利<br>*2026-06-09* | 
| [![随波逐流](https://www.bing.com/th?id=OHR.Cyanea_ZH-CN3858079050_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260608) | [![最后一堵墙矗立着](https://www.bing.com/th?id=OHR.DunseverickCastle2026_ZH-CN3036266326_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260607) | [![多走走，多思考](https://www.bing.com/th?id=OHR.HikingNatchez_ZH-CN2495512699_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260606) | 
| **[随波逐流](https://bing.codexun.com/cn/detail/20260608)**<br>在海洋中游动的狮鬃水母<br>*2026-06-08* | **[最后一堵墙矗立着](https://bing.codexun.com/cn/detail/20260607)**<br>邓塞弗里克城堡遗址, 安特里姆郡, 北爱尔兰<br>*2026-06-07* | **[多走走，多思考](https://bing.codexun.com/cn/detail/20260606)**<br>纳奇兹小径公园大道, 图珀洛, 密西西比州, 美国<br>*2026-06-06* | 
| [![无人问津之地的静默力量](https://www.bing.com/th?id=OHR.WedLapland_ZH-CN2365942547_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260605) | [![优雅羽饰](https://www.bing.com/th?id=OHR.PreeningEgret_ZH-CN2216012708_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260604) | [![路之所止，行之所启](https://www.bing.com/th?id=OHR.BardenasReales_ZH-CN0480548935_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260603) | 
| **[无人问津之地的静默力量](https://bing.codexun.com/cn/detail/20260605)**<br>从斯基尔夫山俯瞰拉帕达伦河三角洲, 萨雷克国家公园, 拉波尼亚, 瑞典拉普兰<br>*2026-06-05* | **[优雅羽饰](https://bing.codexun.com/cn/detail/20260604)**<br>梳理羽毛的雪鹭，佛罗里达州中部，美国<br>*2026-06-04* | **[路之所止，行之所启](https://bing.codexun.com/cn/detail/20260603)**<br>骑行者，巴德纳斯雷亚莱斯自然公园与生物圈保护区，纳瓦拉，西班牙<br>*2026-06-03* | 
| [![穿行于蓝色之间](https://www.bing.com/th?id=OHR.Qinghai_ZH-CN9899656327_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260602) | [![历史的况味](https://www.bing.com/th?id=OHR.OlivaPalermo_ZH-CN9639920195_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260601) | [![顺流而行](https://www.bing.com/th?id=OHR.EvergladesWetlands_ZH-CN9515366484_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260531) | 
| **[穿行于蓝色之间](https://bing.codexun.com/cn/detail/20260602)**<br>穿越西台吉乃尔湖的公路，青海省，中国<br>*2026-06-02* | **[历史的况味](https://bing.codexun.com/cn/detail/20260601)**<br>巴勒莫暮色下的天际线，西西里岛，意大利<br>*2026-06-01* | **[顺流而行](https://bing.codexun.com/cn/detail/20260531)**<br>大沼泽地国家公园航拍景观，佛罗里达州，美国<br>*2026-05-31* | 
| [![读懂黑白之间](https://www.bing.com/th?id=OHR.EquusQuagga_ZH-CN9323988132_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260530) | [![巅峰历史时刻](https://www.bing.com/th?id=OHR.SummitEverest_ZH-CN9252833251_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260529) | [![设计与秩序相结合](https://www.bing.com/th?id=OHR.HwaesongFortress_ZH-CN8225341972_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260528) | 
| **[读懂黑白之间](https://bing.codexun.com/cn/detail/20260530)**<br>平原斑马幼崽，埃托沙国家公园，纳米比亚<br>*2026-05-30* | **[巅峰历史时刻](https://bing.codexun.com/cn/detail/20260529)**<br>珠穆朗玛峰峰顶，萨加玛塔国家公园，尼泊尔<br>*2026-05-29* | **[设计与秩序相结合](https://bing.codexun.com/cn/detail/20260528)**<br>华城堡的古城墙，水原，韩国<br>*2026-05-28* | 
| [![它们“獭”独一无二](https://www.bing.com/th?id=OHR.OtterDay_ZH-CN7735013625_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260527) | [![羽扇豆书写的季节](https://www.bing.com/th?id=OHR.LupineBloom_ZH-CN7639721663_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260526) | [![石间的清风](https://www.bing.com/th?id=OHR.HawaMahal2026_ZH-CN7233246545_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260525) | 
| **[它们“獭”独一无二](https://bing.codexun.com/cn/detail/20260527)**<br>海獭，霍默卡奇马克湾，阿拉斯加州，美国<br>*2026-05-27* | **[羽扇豆书写的季节](https://bing.codexun.com/cn/detail/20260526)**<br>盛开的羽扇豆，北加利福尼亚州，美国<br>*2026-05-26* | **[石间的清风](https://bing.codexun.com/cn/detail/20260525)**<br>从风之宫殿俯瞰斋浦尔市景，拉贾斯坦邦，印度<br>*2026-05-25* | 


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