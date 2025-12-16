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

[![皮毛、霜冻和盛宴](https://www.bing.com/th?id=OHR.FrostySquirrel_ZH-CN4613360783_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251217)

**皮毛、霜冻和盛宴**

谁能抗拒这张软乎乎的小脸？一只欧亚红松鼠栖息在积雪覆盖的松枝上，前爪紧紧抓着松果，仿佛那是世上最后的美食。这些灵巧的小家伙全年忙碌：夏季采集坚果、种子和菌类，冬季则靠储存的松果维持生活。

*© Michael_Conrad/Getty Images (Bing China)*

---

## 最近30天

| | | |
|:---:|:---:|:---:|
| [![皮毛、霜冻和盛宴](https://www.bing.com/th?id=OHR.FrostySquirrel_ZH-CN4613360783_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251217) | [![小帽子，大能量](https://www.bing.com/th?id=OHR.ChristmasGnomes_ZH-CN4405839101_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251216) | [![静谧水波，闪耀灯影](https://www.bing.com/th?id=OHR.AmsterdamLights_ZH-CN4288146509_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251215) | 
| **[皮毛、霜冻和盛宴](https://bing.codexun.com/cn/detail/20251217)**<br>在诺森伯兰郡的欧亚红松鼠, 英格兰<br>*2025-12-17* | **[小帽子，大能量](https://bing.codexun.com/cn/detail/20251216)**<br>圣诞市场上的手工小矮人<br>*2025-12-16* | **[静谧水波，闪耀灯影](https://bing.codexun.com/cn/detail/20251215)**<br>斯皮格尔运河上的灯光装饰, 阿姆斯特丹, 荷兰<br>*2025-12-15* | 
| [![假日鸟类大比拼](https://www.bing.com/th?id=OHR.TuftedTitmouse_ZH-CN4154825372_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251214) | [![冰封的倒影](https://www.bing.com/th?id=OHR.YosemiteWinter_ZH-CN3824387818_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251213) | [![点亮节日的红色植物](https://www.bing.com/th?id=OHR.SpeckledPoinsettia_ZH-CN3726763235_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251212) | 
| **[假日鸟类大比拼](https://bing.codexun.com/cn/detail/20251214)**<br>簇山雀栖息在松枝上, 马萨诸塞州, 美国<br>*2025-12-14* | **[冰封的倒影](https://bing.codexun.com/cn/detail/20251213)**<br>默塞德河, 优胜美地国家公园, 加利福尼亚, 美国<br>*2025-12-13* | **[点亮节日的红色植物](https://bing.codexun.com/cn/detail/20251212)**<br>有斑点的一品红<br>*2025-12-12* | 
| [![天地相接之处](https://www.bing.com/th?id=OHR.EverestGlow_ZH-CN4985720231_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251211) | [![文化交汇之地](https://www.bing.com/th?id=OHR.CordobaCathedral_ZH-CN4603063077_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251210) | [![说“茄子”……或者“青草”](https://www.bing.com/th?id=OHR.LlamaDay_ZH-CN2646855786_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251209) | 
| **[天地相接之处](https://bing.codexun.com/cn/detail/20251211)**<br>从伦佐拉山口眺望珠穆朗玛峰日落时分的峰顶，尼泊尔<br>*2025-12-11* | **[文化交汇之地](https://bing.codexun.com/cn/detail/20251210)**<br>科尔多瓦清真寺大教堂的内部，安达卢西亚，西班牙<br>*2025-12-10* | **[说“茄子”……或者“青草”](https://bing.codexun.com/cn/detail/20251209)**<br>原驼，北角，瓦尔德斯半岛, 阿根廷<br>*2025-12-09* | 
| [![一切安详，一切明亮](https://www.bing.com/th?id=OHR.ComoChristmas_ZH-CN2565627033_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251208) | [![雪落下的声音](https://www.bing.com/th?id=OHR.TheGreatSnowY25_ZH-CN2448918230_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251207) | [![佛罗里达州的生命湿地](https://www.bing.com/th?id=OHR.EvergladesSunrise_ZH-CN2298606730_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251206) | 
| **[一切安详，一切明亮](https://bing.codexun.com/cn/detail/20251208)**<br>多马索的建筑上的圣诞彩灯，科莫湖，意大利<br>*2025-12-08* | **[雪落下的声音](https://bing.codexun.com/cn/detail/20251207)**<br>雪中的故宫，中国北京<br>*2025-12-07* | **[佛罗里达州的生命湿地](https://bing.codexun.com/cn/detail/20251206)**<br>大沼泽地国家公园的蜘蛛网，佛罗里达州，美国<br>*2025-12-06* | 
| [![绘制星图的城市](https://www.bing.com/th?id=OHR.CopanRuins_ZH-CN2157795324_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251205) | [![为生存而疾驰](https://www.bing.com/th?id=OHR.CheetahMound_ZH-CN1970221812_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251204) | [![曙光中的鹤影](https://www.bing.com/th?id=OHR.BosqueCranes_ZH-CN1838488224_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251203) | 
| **[绘制星图的城市](https://bing.codexun.com/cn/detail/20251205)**<br>科潘的玛雅遗址，洪都拉斯<br>*2025-12-05* | **[为生存而疾驰](https://bing.codexun.com/cn/detail/20251204)**<br>马赛马拉国家保护区的猎豹, 纳罗克, 肯尼亚<br>*2025-12-04* | **[曙光中的鹤影](https://bing.codexun.com/cn/detail/20251203)**<br>日出时的沙丘鹤, ‌阿帕奇森林国家野生动物保护区, 新墨西哥州, 美国<br>*2025-12-03* | 
| [![一景胜千言](https://www.bing.com/th?id=OHR.WillowLake_ZH-CN9798614021_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251202) | [![冰雪凝息之处](https://www.bing.com/th?id=OHR.AntarcticArch_ZH-CN1622701432_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251201) | [![一路闪耀](https://www.bing.com/th?id=OHR.LeipzigMarket_ZH-CN1517513161_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251130) | 
| **[一景胜千言](https://bing.codexun.com/cn/detail/20251202)**<br>柳树湖与布莱克本山, 兰格尔－圣伊利亚斯国家公园暨保护区, 阿拉斯加州, 美国<br>*2025-12-02* | **[冰雪凝息之处](https://bing.codexun.com/cn/detail/20251201)**<br>冰山上天然形成的拱门, 南极洲<br>*2025-12-01* | **[一路闪耀](https://bing.codexun.com/cn/detail/20251130)**<br>莱比锡圣诞集市, 德国<br>*2025-11-30* | 
| [![哎呀，好冷啊！](https://www.bing.com/th?id=OHR.DeerVeluwe_ZH-CN1438758687_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251129) | [![白色回响](https://www.bing.com/th?id=OHR.InvernoItalia_ZH-CN1329490862_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251128) | [![潮起潮落的坚守](https://www.bing.com/th?id=OHR.PierOfEastbourne2025_ZH-CN7178301269_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251127) | 
| **[哎呀，好冷啊！](https://bing.codexun.com/cn/detail/20251129)**<br>荷兰梵高国家森林公园的马鹿雄鹿, 荷兰<br>*2025-11-29* | **[白色回响](https://bing.codexun.com/cn/detail/20251128)**<br>瓦尔·布兰德特, 布雷西亚, 伦巴第大区, 意大利<br>*2025-11-28* | **[潮起潮落的坚守](https://bing.codexun.com/cn/detail/20251127)**<br>伊斯特本码头, 东萨塞克斯郡, 英格兰<br>*2025-11-27* | 
| [![让树叶诉说历史](https://www.bing.com/th?id=OHR.OliveGrove_ZH-CN7054006944_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251126) | [![爱情、幸运与硬币](https://www.bing.com/th?id=OHR.TreviFountain_ZH-CN6892299520_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251125) | [![岩石中的秘密](https://www.bing.com/th?id=OHR.GwailorFort_ZH-CN6731607002_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251124) | 
| **[让树叶诉说历史](https://bing.codexun.com/cn/detail/20251126)**<br>特拉蒙塔纳山脉的橄榄园, 马略卡岛, 巴利阿里群岛, 西班牙<br>*2025-11-26* | **[爱情、幸运与硬币](https://bing.codexun.com/cn/detail/20251125)**<br>罗马的特雷维喷泉, 意大利<br>*2025-11-25* | **[岩石中的秘密](https://bing.codexun.com/cn/detail/20251124)**<br>瓜廖尔堡, ‌中央邦, 印度<br>*2025-11-24* | 
| [![大自然的秘密代码](https://www.bing.com/th?id=OHR.MadgascarAmmonite_ZH-CN6497276091_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251123) | [![守护江河的佛像](https://www.bing.com/th?id=OHR.LeshanBuddha_ZH-CN2804271540_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251122) | [![带着“你好”的问候](https://www.bing.com/th?id=OHR.SealWaving_ZH-CN2467723602_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251121) | 
| **[大自然的秘密代码](https://bing.codexun.com/cn/detail/20251123)**<br>马达加斯加菊石化石<br>*2025-11-23* | **[守护江河的佛像](https://bing.codexun.com/cn/detail/20251122)**<br>乐山大佛, 四川, 中国<br>*2025-11-22* | **[带着“你好”的问候](https://bing.codexun.com/cn/detail/20251121)**<br>罗伯特·摩西州立公园的港海豹, 长岛, 纽约, 美国<br>*2025-11-21* | 
| [![颂扬保护与美](https://www.bing.com/th?id=OHR.PondCave_ZH-CN2304770650_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251120) | [![石头与符号，诉说一个民族的故事](https://www.bing.com/th?id=OHR.BudapestParliament_ZH-CN1607028780_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251119) | [![秋日里的羽翼明星](https://www.bing.com/th?id=OHR.AutumnMerganser_ZH-CN1320438449_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251118) | 
| **[颂扬保护与美](https://bing.codexun.com/cn/detail/20251120)**<br>查帕达迪亚曼蒂纳国家公园，巴伊亚州，巴西<br>*2025-11-20* | **[石头与符号，诉说一个民族的故事](https://bing.codexun.com/cn/detail/20251119)**<br>匈牙利国会大厦，布达佩斯，匈牙利<br>*2025-11-19* | **[秋日里的羽翼明星](https://bing.codexun.com/cn/detail/20251118)**<br>雄性棕胁秋沙鸭，俄勒冈州，美国<br>*2025-11-18* | 


---

## 按年份浏览壁纸档案

### 2025
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 6px; margin: 12px 0;">
<a href="https://bing.codexun.com/cn/archive/202512" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f3f4f6; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease; font-weight: 500;">202512</a>
<a href="https://bing.codexun.com/cn/archive/202511" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202511</a>
<a href="https://bing.codexun.com/cn/archive/202510" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202510</a>
<a href="https://bing.codexun.com/cn/archive/202509" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202509</a>
<a href="https://bing.codexun.com/cn/archive/202508" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202508</a>
<a href="https://bing.codexun.com/cn/archive/202507" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202507</a>
<a href="https://bing.codexun.com/cn/archive/202506" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202506</a>
</div>



---