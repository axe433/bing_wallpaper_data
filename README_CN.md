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

[![完美的夜晚](https://www.bing.com/th?id=OHR.SunsetPier_ZH-CN1202083395_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250905)

**完美的夜晚**

当夕阳西下，洒下橙色、粉色和紫色的光芒时，圣莫尼卡从悠闲的氛围中转为灯火通明。真的！这片海滩拥有超过3英里的沙滩、一座历史悠久的码头，以及风景如画的太平洋海岸公路，不仅仅是一条美丽的海岸线。让我们先从沙滩说起。宽阔、洁净，无论是打排球还是悠闲地读一本好书，这里都是日光浴爱好者和沙堡建造者的理想之地。

*© EXTREME-PHOTOGRAPHER/Getty Images (Bing China)*

---

## 最近30天

| | | |
|:---:|:---:|:---:|
| [![完美的夜晚](https://www.bing.com/th?id=OHR.SunsetPier_ZH-CN1202083395_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250905) | [![力量的角逐](https://www.bing.com/th?id=OHR.WrestlingBears_ZH-CN6430637848_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250904) | [![享受宁静](https://www.bing.com/th?id=OHR.MinnesotaWaters_ZH-CN6078521418_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250903) | 
| **[完美的夜晚](https://bing.codexun.com/cn/detail/20250905)**<br>太平洋公园，圣莫妮卡州立海滩，加利福尼亚州，美国<br>*2025-09-05* | **[力量的角逐](https://bing.codexun.com/cn/detail/20250904)**<br>灰熊摔跤, 卡特迈国家公园及自然保护区, 阿拉斯加, 美国<br>*2025-09-04* | **[享受宁静](https://bing.codexun.com/cn/detail/20250903)**<br>边界水域独木舟区荒野区, 明尼苏达州, 美国<br>*2025-09-03* | 
| [![死谷的幽灵](https://www.bing.com/th?id=OHR.DeadvleiTrees_ZH-CN0967414858_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250902) | [![风景如画的葡萄园](https://www.bing.com/th?id=OHR.FieldKaiserstuhl_ZH-CN0467488834_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250901) | [![彩绘的云，静默的悬崖](https://www.bing.com/th?id=OHR.ScottsBluff_ZH-CN0292735112_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250831) | 
| **[死谷的幽灵](https://bing.codexun.com/cn/detail/20250902)**<br>骆驼刺树, 死亡谷, 纳米布-诺克卢福国家公园, 纳米比亚<br>*2025-09-02* | **[风景如画的葡萄园](https://bing.codexun.com/cn/detail/20250901)**<br>凯撒施图尔，巴登-符腾堡，德国<br>*2025-09-01* | **[彩绘的云，静默的悬崖](https://bing.codexun.com/cn/detail/20250831)**<br>杰灵的斯科茨布拉夫国家纪念碑‌, 内布拉斯加州,美国<br>*2025-08-31* | 
| [![有鳍且惊艳](https://www.bing.com/th?id=OHR.MaldivesWhaleShark_ZH-CN9975504316_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250830) | [![网格的心脏](https://www.bing.com/th?id=OHR.PlazaMayor_ZH-CN4576498488_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250829) | [![这只白鹭毫无遗憾](https://www.bing.com/th?id=OHR.WhiteEgret_ZH-CN4425921150_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250828) | 
| **[有鳍且惊艳](https://bing.codexun.com/cn/detail/20250830)**<br>阿里夫达鲁环礁海岸的鲸鲨, 马尔代夫<br>*2025-08-30* | **[网格的心脏](https://bing.codexun.com/cn/detail/20250829)**<br>马约尔广场鸟瞰图, 马德里, 西班牙<br>*2025-08-29* | **[这只白鹭毫无遗憾](https://bing.codexun.com/cn/detail/20250828)**<br>大白鹭，匈牙利<br>*2025-08-28* | 
| [![海洋上方的湖泊](https://www.bing.com/th?id=OHR.FaroeLake_ZH-CN3977660997_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250827) | [![一座非凡的特鲁洛小镇](https://www.bing.com/th?id=OHR.TrulliHouses_ZH-CN3856452406_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250826) | [![从火山之源到河流之路](https://www.bing.com/th?id=OHR.YellowstoneRiver_ZH-CN3716808579_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250825) | 
| **[海洋上方的湖泊](https://bing.codexun.com/cn/detail/20250827)**<br>瑟沃格湖，瓦加尔岛，法罗群岛<br>*2025-08-27* | **[一座非凡的特鲁洛小镇](https://bing.codexun.com/cn/detail/20250826)**<br>阿尔贝罗贝洛的特鲁洛建筑，普利亚大区，意大利<br>*2025-08-26* | **[从火山之源到河流之路](https://bing.codexun.com/cn/detail/20250825)**<br>方解石温泉区和黄石河，黄石国家公园，怀俄明州，美国<br>*2025-08-25* | 
| [![“跟我来”](https://www.bing.com/th?id=OHR.CervusDama_ZH-CN3603505811_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250824) | [![彩林叠翠间的瀑布](https://www.bing.com/th?id=OHR.ChushuY25_ZH-CN0495086720_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250823) | [![大自然的绿色地毯](https://www.bing.com/th?id=OHR.PalouseWA_ZH-CN2552273820_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250822) | 
| **[“跟我来”](https://bing.codexun.com/cn/detail/20250824)**<br>欧洲黇鹿‌，英格兰<br>*2025-08-24* | **[彩林叠翠间的瀑布](https://bing.codexun.com/cn/detail/20250823)**<br>秋季九寨沟国家公园里的诺日朗瀑布, 四川省, 中国<br>*2025-08-23* | **[大自然的绿色地毯](https://bing.codexun.com/cn/detail/20250822)**<br>帕卢斯连绵起伏的丘陵，华盛顿州，美国<br>*2025-08-22* | 
| [![伫立凝视](https://www.bing.com/th?id=OHR.WheatearBird_ZH-CN2663965839_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250821) | [![永恒的建筑](https://www.bing.com/th?id=OHR.CitadelBonifacio_ZH-CN2130899430_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250820) | [![随海而流的岩石！](https://www.bing.com/th?id=OHR.GipuzcoaSummer_ZH-CN1926924422_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250819) | 
| **[伫立凝视](https://bing.codexun.com/cn/detail/20250821)**<br>穗䳭和盛开的帚石楠，峰区国家公园，英格兰<br>*2025-08-21* | **[永恒的建筑](https://bing.codexun.com/cn/detail/20250820)**<br>博尼法乔城堡，科西嘉岛南部，法国<br>*2025-08-20* | **[随海而流的岩石！](https://bing.codexun.com/cn/detail/20250819)**<br>祖马亚的复理层，巴斯克地区，西班牙<br>*2025-08-19* | 
| [![溪流入梦](https://www.bing.com/th?id=OHR.AvalancheLake_ZH-CN1442576083_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250818) | [![眺望大海的高塔](https://www.bing.com/th?id=OHR.LyngvigLighthouse_ZH-CN0836204503_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250817) | [![成为改变的一“蜂”](https://www.bing.com/th?id=OHR.ColorfulBeehives_ZH-CN0180195770_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250816) | 
| **[溪流入梦](https://bing.codexun.com/cn/detail/20250818)**<br>雪崩湖步道，阿迪朗达克高峰区，纽约州，美国<br>*2025-08-18* | **[眺望大海的高塔](https://bing.codexun.com/cn/detail/20250817)**<br>灵维格灯塔，维泽桑讷，丹麦<br>*2025-08-17* | **[成为改变的一“蜂”](https://bing.codexun.com/cn/detail/20250816)**<br>色彩斑斓的蜂巢, 意大利<br>*2025-08-16* | 
| [![水下翱翔](https://www.bing.com/th?id=OHR.SpottedEagleRay_ZH-CN9894613260_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250815) | [![从山顶俯瞰](https://www.bing.com/th?id=OHR.PizNairPeak_ZH-CN8209144138_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250814) | [![地球的公开秘密](https://www.bing.com/th?id=OHR.CoronaArch_ZH-CN5406267193_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250813) | 
| **[水下翱翔](https://bing.codexun.com/cn/detail/20250815)**<br>斑点鹞鲼，圣克里斯托瓦尔岛‌，‌加拉帕戈斯群岛，厄瓜多尔<br>*2025-08-15* | **[从山顶俯瞰](https://bing.codexun.com/cn/detail/20250814)**<br>皮兹奈尔山缆车站, 格劳宾登州, 瑞士<br>*2025-08-14* | **[地球的公开秘密](https://bing.codexun.com/cn/detail/20250813)**<br>一名男子从摩押附近的科罗纳拱门索降, 美国<br>*2025-08-13* | 
| [![野性、智慧与奇迹](https://www.bing.com/th?id=OHR.KenyaElephants_ZH-CN7587207512_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250812) | [![来自山巅的明信片](https://www.bing.com/th?id=OHR.SantaMaddalena_ZH-CN7421083295_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250811) | [![为正义怒吼](https://www.bing.com/th?id=OHR.LionessKenya_ZH-CN6791029673_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250810) | 
| **[野性、智慧与奇迹](https://bing.codexun.com/cn/detail/20250812)**<br>非洲象群, 安博塞利国家公园, 肯尼亚<br>*2025-08-12* | **[来自山巅的明信片](https://bing.codexun.com/cn/detail/20250811)**<br>圣玛格达莱娜, 多洛米蒂山, 意大利<br>*2025-08-11* | **[为正义怒吼](https://bing.codexun.com/cn/detail/20250810)**<br>马赛马拉国家保护区的雌狮,肯尼亚<br>*2025-08-10* | 
| [![致敬原住民之声](https://www.bing.com/th?id=OHR.MaoriRock_ZH-CN5614685493_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250809) | [![奔流不息，为你为我](https://www.bing.com/th?id=OHR.IguazuArgentina_ZH-CN4457051931_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250808) | [![海岸的密码](https://www.bing.com/th?id=OHR.GasparillaLight_ZH-CN6855683859_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250807) | 
| **[致敬原住民之声](https://bing.codexun.com/cn/detail/20250809)**<br>陶波湖上的 Ngātoroirangi 矿湾毛利石刻, 新西兰<br>*2025-08-09* | **[奔流不息，为你为我](https://bing.codexun.com/cn/detail/20250808)**<br>伊瓜苏瀑布的三火枪瀑布, 阿根廷<br>*2025-08-08* | **[海岸的密码](https://bing.codexun.com/cn/detail/20250807)**<br>加斯帕里拉岛灯塔后导标灯, 博卡格兰德, 佛罗里达州, 美国<br>*2025-08-07* | 


---

## 按年份浏览壁纸档案

### 2025
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 6px; margin: 12px 0;">
<a href="https://bing.codexun.com/cn/archive/202509" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f3f4f6; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease; font-weight: 500;">202509</a>
<a href="https://bing.codexun.com/cn/archive/202508" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202508</a>
<a href="https://bing.codexun.com/cn/archive/202507" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202507</a>
<a href="https://bing.codexun.com/cn/archive/202506" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202506</a>
</div>



---