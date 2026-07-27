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

[![仰望芝城，流光溢彩](https://www.bing.com/th?id=OHR.ChicagoTiffany_ZH-CN9860688834_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260727)

**仰望芝城，流光溢彩**

步入位于美国，伊利诺伊州，芝加哥文化中心的建筑内部，目光瞬间会被上方绚丽夺目的彩色顶棚——蒂芙尼穹顶所吸引。这座艺术杰作悬挂在普雷斯顿·布拉德利大厅上方，直径约38英尺，由约30,000片法夫里尔玻璃组成，每片玻璃都呈鱼鳞状。阳光透过其半透明的表面，在错综复杂的图案中映射出变幻莫测的蓝色与金色。

*© Felix Lipov/Shutterstock (Bing China)*

---

## 最近30天

| | | |
|:---:|:---:|:---:|
| [![仰望芝城，流光溢彩](https://www.bing.com/th?id=OHR.ChicagoTiffany_ZH-CN9860688834_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260727) | [![海陆际会，生机肇始](https://www.bing.com/th?id=OHR.RedMangroveSunrise_ZH-CN7940335392_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260726) | [![加境幽廊](https://www.bing.com/th?id=OHR.GaliciaBeach_ZH-CN1246611659_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260725) | 
| **[仰望芝城，流光溢彩](https://bing.codexun.com/cn/detail/20260727)**<br>蒂芙尼穹顶，芝加哥文化中心，伊利诺伊州，美国<br>*2026-07-27* | **[海陆际会，生机肇始](https://bing.codexun.com/cn/detail/20260726)**<br>红树上的日出在小猪群岛，洪都拉斯<br>*2026-07-26* | **[加境幽廊](https://bing.codexun.com/cn/detail/20260725)**<br>大教堂海滩，加利西亚，西班牙<br>*2026-07-25* | 
| [![缤纷多彩的一家人](https://www.bing.com/th?id=OHR.GalapagosFlamingos_ZH-CN1152519387_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260724) | [![瓣叠交响](https://www.bing.com/th?id=OHR.PinkDahlia_ZH-CN2259107800_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260723) | [![细微之举，影响深远](https://www.bing.com/th?id=OHR.CoralAwareness_ZH-CN1621627126_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260722) | 
| **[缤纷多彩的一家人](https://bing.codexun.com/cn/detail/20260724)**<br>美洲红鹳群在伊莎贝拉岛，加拉帕戈斯群岛，厄瓜多尔<br>*2026-07-24* | **[瓣叠交响](https://bing.codexun.com/cn/detail/20260723)**<br>粉红色大丽花<br>*2026-07-23* | **[细微之举，影响深远](https://bing.codexun.com/cn/detail/20260722)**<br>珊瑚礁与海滩在拉贾安帕特，印度尼西亚<br>*2026-07-22* | 
| [![拱影寻踪](https://www.bing.com/th?id=OHR.SantaCatalina_ZH-CN6223370790_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260721) | [![月瞰寰宇](https://www.bing.com/th?id=OHR.Artemis_ZH-CN3540365575_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260720) | [![敛羽栖时](https://www.bing.com/th?id=OHR.HirundoRustica_ZH-CN2798518247_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260719) | 
| **[拱影寻踪](https://bing.codexun.com/cn/detail/20260721)**<br>圣卡塔琳娜拱门，安提瓜，危地马拉<br>*2026-07-21* | **[月瞰寰宇](https://bing.codexun.com/cn/detail/20260720)**<br>月球与地球由阿耳忒弥斯2号机组人员拍摄<br>*2026-07-20* | **[敛羽栖时](https://bing.codexun.com/cn/detail/20260719)**<br>不同亚种的家燕聚在一起休息<br>*2026-07-19* | 
| [![环影圆成](https://www.bing.com/th?id=OHR.DevilsBridge_ZH-CN2164982440_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260718) | [![希腊式的逃离](https://www.bing.com/th?id=OHR.VaiUmbrellas_ZH-CN1271422272_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260717) | [![滨水变色龙](https://www.bing.com/th?id=OHR.NavyPier_ZH-CN4649271588_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260716) | 
| **[环影圆成](https://bing.codexun.com/cn/detail/20260718)**<br>恶魔桥在克罗姆劳杜鹃花公园，萨克森州，德国<br>*2026-07-18* | **[希腊式的逃离](https://bing.codexun.com/cn/detail/20260717)**<br>瓦伊海滩上的日光浴躺椅，克里特岛，希腊<br>*2026-07-17* | **[滨水变色龙](https://bing.codexun.com/cn/detail/20260716)**<br>海军码头，芝加哥，伊利诺伊州，美国<br>*2026-07-16* | 
| [![攀登后的奖励](https://www.bing.com/th?id=OHR.MarieLake_ZH-CN4927917413_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260715) | [![奇妙的真相](https://www.bing.com/th?id=OHR.LemonShark_ZH-CN4650331008_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260714) | [![为摇滚而生](https://www.bing.com/th?id=OHR.NavajoSandstone_ZH-CN5009673011_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260713) | 
| **[攀登后的奖励](https://bing.codexun.com/cn/detail/20260715)**<br>玛丽湖，约翰·缪尔荒野（毕晓普附近），加利福尼亚州，美国<br>*2026-07-15* | **[奇妙的真相](https://bing.codexun.com/cn/detail/20260714)**<br>柠檬鲨幼崽在红树林中，伊柳塞拉岛，巴哈马<br>*2026-07-14* | **[为摇滚而生](https://bing.codexun.com/cn/detail/20260713)**<br>羚羊峡谷，纳瓦霍族保留地，亚利桑那州，美国<br>*2026-07-13* | 
| [![缅因州的狂野一面](https://www.bing.com/th?id=OHR.KatahdinWWNM_ZH-CN5496444375_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260712) | [![布列塔尼的潮汐之约](https://www.bing.com/th?id=OHR.AurayBrittany_ZH-CN5549157888_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260711) | [![陆地与海洋的鸟瞰图](https://www.bing.com/th?id=OHR.VictoriaBeach_ZH-CN8892195426_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260710) | 
| **[缅因州的狂野一面](https://bing.codexun.com/cn/detail/20260712)**<br>卡塔丁森林和水域国家纪念地，缅因州，美国<br>*2026-07-12* | **[布列塔尼的潮汐之约](https://bing.codexun.com/cn/detail/20260711)**<br>圣古斯坦港, 欧赖, 布列塔尼, 法国<br>*2026-07-11* | **[陆地与海洋的鸟瞰图](https://bing.codexun.com/cn/detail/20260710)**<br>陆地与海洋的鸟瞰图，维多利亚州，澳大利亚<br>*2026-07-10* | 
| [![步步传承](https://www.bing.com/th?id=OHR.SapaVietnam_ZH-CN2178893672_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260709) | [![远古火山的回响](https://www.bing.com/th?id=OHR.LakeAtitlan_ZH-CN1920221893_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260708) | [![林冠华彩](https://www.bing.com/th?id=OHR.MountainToucanOrchids_ZH-CN1400221431_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260707) | 
| **[步步传承](https://bing.codexun.com/cn/detail/20260709)**<br>在沙巴的水稻田，老街，越南<br>*2026-07-09* | **[远古火山的回响](https://bing.codexun.com/cn/detail/20260708)**<br>阿蒂特兰湖的日出，危地马拉<br>*2026-07-08* | **[林冠华彩](https://bing.codexun.com/cn/detail/20260707)**<br>板嘴山巨嘴鸟与兰花，厄瓜多尔<br>*2026-07-07* | 
| [![百代镌刻之城](https://www.bing.com/th?id=OHR.SyracuseItaly_ZH-CN1001695972_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260706) | [![紫色花海](https://www.bing.com/th?id=OHR.LavenderRows_ZH-CN0676810895_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260705) | [![此行，不虚绕道](https://www.bing.com/th?id=OHR.KaysersbergVillage_ZH-CN0445080679_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260704) | 
| **[百代镌刻之城](https://bing.codexun.com/cn/detail/20260706)**<br>锡拉库萨的日落，西西里岛，意大利<br>*2026-07-06* | **[紫色花海](https://bing.codexun.com/cn/detail/20260705)**<br>瓦朗索勒高原的薰衣草行，普罗旺斯，法国<br>*2026-07-05* | **[此行，不虚绕道](https://bing.codexun.com/cn/detail/20260704)**<br>凯泽斯堡，阿尔萨斯，法国<br>*2026-07-04* | 
| [![流光之诗](https://www.bing.com/th?id=OHR.FirefliesJapan_ZH-CN0071253415_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260703) | [![走进埃斯纳神圣的世界](https://www.bing.com/th?id=OHR.TempleEsna_ZH-CN9834689523_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260702) | [![大西洋雕琢而成的加拿大](https://www.bing.com/th?id=OHR.DungeonPark_ZH-CN9544093701_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260701) | 
| **[流光之诗](https://bing.codexun.com/cn/detail/20260703)**<br>小溪上方的萤火虫，冈山县，日本<br>*2026-07-03* | **[走进埃斯纳神圣的世界](https://bing.codexun.com/cn/detail/20260702)**<br>埃斯纳神庙穹顶天花板, 埃及<br>*2026-07-02* | **[大西洋雕琢而成的加拿大](https://bing.codexun.com/cn/detail/20260701)**<br>地牢省立公园, 纽芬兰和拉布拉多省, 加拿大<br>*2026-07-01* | 
| [![阴影被拉得修长之处](https://www.bing.com/th?id=OHR.MasaiGiraffe_ZH-CN1665123897_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260630) | [![生于烈火，拥于碧水](https://www.bing.com/th?id=OHR.BoraBoraLagoon_ZH-CN9234363590_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260629) | [![看起来很精神](https://www.bing.com/th?id=OHR.SaguaroSun_ZH-CN5820504732_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260628) | 
| **[阴影被拉得修长之处](https://bing.codexun.com/cn/detail/20260630)**<br>马赛马拉国家保护区日落时分的长颈鹿, 肯尼亚<br>*2026-06-30* | **[生于烈火，拥于碧水](https://bing.codexun.com/cn/detail/20260629)**<br>波拉波拉岛及其泻湖, 南太平洋, 法属波利尼西亚<br>*2026-06-29* | **[看起来很精神](https://bing.codexun.com/cn/detail/20260628)**<br>温德盖特山口附近的巨柱仙人掌, 麦克道尔山脉, 亚利桑那州, 美国<br>*2026-06-28* | 


---

## 按年份浏览壁纸档案

### 2026
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 6px; margin: 12px 0;">
<a href="https://bing.codexun.com/cn/archive/202607" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f3f4f6; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease; font-weight: 500;">202607</a>
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