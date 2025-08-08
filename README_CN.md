# Bing 壁纸数据爬虫与文档生成器

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
| `ar` | 🇦🇷 阿根廷 | `au` | 🇦🇺 澳大利亚 | `br` | 🇧🇷 巴西 | 
| `ca` | 🇨🇦 加拿大 | `cn` | 🇨🇳 中国 | `cz` | 🇨🇿 捷克 | 
| `de` | 🇩🇪 德国 | `dk` | 🇩🇰 丹麦 | `es` | 🇪🇸 西班牙 | 
| `fi` | 🇫🇮 芬兰 | `fr` | 🇫🇷 法国 | `gb` | 🇬🇧 英国 | 
| `gr` | 🇬🇷 希腊 | `hk` | 🇭🇰 香港 | `id` | 🇮🇩 印度尼西亚 | 
| `in` | 🇮🇳 印度 | `it` | 🇮🇹 意大利 | `jp` | 🇯🇵 日本 | 
| `kr` | 🇰🇷 韩国 | `my` | 🇲🇾 马来西亚 | `nl` | 🇳🇱 荷兰 | 
| `no` | 🇳🇴 挪威 | `pl` | 🇵🇱 波兰 | `pt` | 🇵🇹 葡萄牙 | 
| `ru` | 🇷🇺 俄罗斯 | `se` | 🇸🇪 瑞典 | `sg` | 🇸🇬 新加坡 | 
| `th` | 🇹🇭 泰国 | `tr` | 🇹🇷 土耳其 | `tw` | 🇹🇼 台湾 | 
| `ua` | 🇺🇦 乌克兰 | `us` | 🇺🇸 美国 | `vn` | 🇻🇳 越南 | 
| `za` | 🇿🇦 南非 |  |  |
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

## 🌍 各国壁纸文档链接

点击下方链接查看各国的壁纸文档：

| [🇦🇷 阿根廷](markdown/wallpaper-list-ar.md) | [🇦🇺 澳大利亚](markdown/wallpaper-list-au.md) | [🇧🇷 巴西](markdown/wallpaper-list-br.md) | 
|:---:|:---:|:---:|
| [🇨🇦 加拿大](markdown/wallpaper-list-ca.md) | [🇨🇳 中国](markdown/wallpaper-list-cn.md) | [🇨🇿 捷克](markdown/wallpaper-list-cz.md) | 
| [🇩🇪 德国](markdown/wallpaper-list-de.md) | [🇩🇰 丹麦](markdown/wallpaper-list-dk.md) | [🇪🇸 西班牙](markdown/wallpaper-list-es.md) | 
| [🇫🇮 芬兰](markdown/wallpaper-list-fi.md) | [🇫🇷 法国](markdown/wallpaper-list-fr.md) | [🇬🇧 英国](markdown/wallpaper-list-gb.md) | 
| [🇬🇷 希腊](markdown/wallpaper-list-gr.md) | [🇭🇰 香港](markdown/wallpaper-list-hk.md) | [🇮🇩 印度尼西亚](markdown/wallpaper-list-id.md) | 
| [🇮🇳 印度](markdown/wallpaper-list-in.md) | [🇮🇹 意大利](markdown/wallpaper-list-it.md) | [🇯🇵 日本](markdown/wallpaper-list-jp.md) | 
| [🇰🇷 韩国](markdown/wallpaper-list-kr.md) | [🇲🇾 马来西亚](markdown/wallpaper-list-my.md) | [🇳🇱 荷兰](markdown/wallpaper-list-nl.md) | 
| [🇳🇴 挪威](markdown/wallpaper-list-no.md) | [🇵🇱 波兰](markdown/wallpaper-list-pl.md) | [🇵🇹 葡萄牙](markdown/wallpaper-list-pt.md) | 
| [🇷🇺 俄罗斯](markdown/wallpaper-list-ru.md) | [🇸🇪 瑞典](markdown/wallpaper-list-se.md) | [🇸🇬 新加坡](markdown/wallpaper-list-sg.md) | 
| [🇹🇭 泰国](markdown/wallpaper-list-th.md) | [🇹🇷 土耳其](markdown/wallpaper-list-tr.md) | [🇹🇼 台湾](markdown/wallpaper-list-tw.md) | 
| [🇺🇦 乌克兰](markdown/wallpaper-list-ua.md) | [🇺🇸 美国](markdown/wallpaper-list-us.md) | [🇻🇳 越南](markdown/wallpaper-list-vn.md) | 
| [🇿🇦 南非](markdown/wallpaper-list-za.md) |  |  | 


## 今日壁纸

[![致敬原住民之声](https://www.bing.com/th?id=OHR.MaoriRock_ZH-CN5614685493_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250809)

**致敬原住民之声**

每年8月9日，联合国都会庆祝“世界土著人民国际日”，这一日是纪念原住民社区坚韧精神、智慧和丰富文化的时刻。在美国，这一天也成为反思美洲原住民部落历史与贡献的契机，同时鼓励人们与全球各地的土著人民携手共进。

*© Joppi/Getty Images (Bing China)*

---

## 最近30天

| | | |
|:---:|:---:|:---:|
| [![致敬原住民之声](https://www.bing.com/th?id=OHR.MaoriRock_ZH-CN5614685493_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250809) | [![奔流不息，为你为我](https://www.bing.com/th?id=OHR.IguazuArgentina_ZH-CN4457051931_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250808) | [![海岸的密码](https://www.bing.com/th?id=OHR.GasparillaLight_ZH-CN6855683859_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250807) | 
| **[致敬原住民之声](https://bing.codexun.com/cn/detail/20250809)**<br>陶波湖上的 Ngātoroirangi 矿湾毛利石刻, 新西兰<br>*2025-08-09* | **[奔流不息，为你为我](https://bing.codexun.com/cn/detail/20250808)**<br>伊瓜苏瀑布的三火枪瀑布, 阿根廷<br>*2025-08-08* | **[海岸的密码](https://bing.codexun.com/cn/detail/20250807)**<br>加斯帕里拉岛灯塔后导标灯, 博卡格兰德, 佛罗里达州, 美国<br>*2025-08-07* | 
| [![马达加斯加原住民](https://www.bing.com/th?id=OHR.BabyLemur_ZH-CN6617977758_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250806) | [![潮起潮落](https://www.bing.com/th?id=OHR.CaliforniaTidepool_ZH-CN6273815361_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250805) | [![这是谁的家？](https://www.bing.com/th?id=OHR.LaplandOwl_ZH-CN6070251232_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250804) | 
| **[马达加斯加原住民](https://bing.codexun.com/cn/detail/20250806)**<br>环尾狐猴幼崽在玩自己的尾巴‌, 马达加斯加<br>*2025-08-06* | **[潮起潮落](https://bing.codexun.com/cn/detail/20250805)**<br>拉霍亚的潮汐池‌, 加利福尼亚州, 美国<br>*2025-08-05* | **[这是谁的家？](https://bing.codexun.com/cn/detail/20250804)**<br>巢中的乌林鸮, 芬兰<br>*2025-08-04* | 
| [![你好，黄色！](https://www.bing.com/th?id=OHR.HappySunflower_ZH-CN5840993161_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250803) | [![古老的岩画](https://www.bing.com/th?id=OHR.FruitaPetroglyphs_ZH-CN5423905955_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250802) | [![惊喜随时上演](https://www.bing.com/th?id=OHR.EdinburghFringe_ZH-CN5243292664_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250801) | 
| **[你好，黄色！](https://bing.codexun.com/cn/detail/20250803)**<br>夏天田野里盛开的向日葵<br>*2025-08-03* | **[古老的岩画](https://bing.codexun.com/cn/detail/20250802)**<br>圆顶礁国家公园弗鲁塔附近的岩画, 犹他州, 美国<br>*2025-08-02* | **[惊喜随时上演](https://bing.codexun.com/cn/detail/20250801)**<br>皇家英里大道, 爱丁堡, 苏格兰<br>*2025-08-01* | 
| [![远离尘嚣](https://www.bing.com/th?id=OHR.NaPaliKauai_ZH-CN5070149838_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250731) | [![理想的世界！](https://www.bing.com/th?id=OHR.RibadesellaSummer_ZH-CN4852547359_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250730) | [![丛林女王](https://www.bing.com/th?id=OHR.TigerDay_ZH-CN4359136631_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250729) | 
| **[远离尘嚣](https://bing.codexun.com/cn/detail/20250731)**<br>纳帕利海岸的卡拉劳海滩, 可爱岛, 夏威夷, 美国<br>*2025-07-31* | **[理想的世界！](https://bing.codexun.com/cn/detail/20250730)**<br>里瓦德塞利亚，阿斯图里亚斯，西班牙<br>*2025-07-30* | **[丛林女王](https://bing.codexun.com/cn/detail/20250729)**<br>雌性孟加拉虎，坎哈国家公园，印度<br>*2025-07-29* | 
| [![领先一步](https://www.bing.com/th?id=OHR.MongoliaYurts_ZH-CN4015475887_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250728) | [![同步闪耀](https://www.bing.com/th?id=OHR.BlackfinBarracuda_ZH-CN3850642551_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250727) | [![潮汐的守护者](https://www.bing.com/th?id=OHR.MangroveTwilight_ZH-CN3596666263_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250726) | 
| **[领先一步](https://bing.codexun.com/cn/detail/20250728)**<br>蒙古草原上的蒙古包<br>*2025-07-28* | **[同步闪耀](https://bing.codexun.com/cn/detail/20250727)**<br>黑鳍梭鱼群，鲨鱼礁，拉斯穆罕默德国家公园，西奈半岛，埃及<br>*2025-07-27* | **[潮汐的守护者](https://bing.codexun.com/cn/detail/20250726)**<br>黄昏时的红树林，瓦拉基里海滩，松巴岛，印度尼西亚<br>*2025-07-26* | 
| [![生活的画卷](https://www.bing.com/th?id=OHR.LasPalmas_ZH-CN5993442425_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250725) | [![物以类聚，鸟以群分](https://www.bing.com/th?id=OHR.AshyWoodswallow_ZH-CN3224168805_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250724) | [![城中之国](https://www.bing.com/th?id=OHR.VaticanCity_ZH-CN3075109504_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250723) | 
| **[生活的画卷](https://bing.codexun.com/cn/detail/20250725)**<br>大加那利岛拉斯帕尔马斯色彩缤纷的房屋鸟瞰图，西班牙<br>*2025-07-25* | **[物以类聚，鸟以群分](https://bing.codexun.com/cn/detail/20250724)**<br>栖息在树枝上的灰燕鵙家族<br>*2025-07-24* | **[城中之国](https://bing.codexun.com/cn/detail/20250723)**<br>梵蒂冈城与圣彼得大教堂，罗马，意大利<br>*2025-07-23* | 
| [![天山上的蓝宝石](https://www.bing.com/th?id=OHR.GreatHeatY25_ZH-CN8252122347_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250722) | [![海洋中的热带雨林](https://www.bing.com/th?id=OHR.AcroporaReef_ZH-CN2622120276_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250721) | [![在月光下起舞](https://www.bing.com/th?id=OHR.BigMoon_ZH-CN2508603883_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250720) | 
| **[天山上的蓝宝石](https://bing.codexun.com/cn/detail/20250722)**<br>夏季的赛里木湖，博尔塔拉蒙古自治州博乐县, 中国新疆维吾尔自治区<br>*2025-07-22* | **[海洋中的热带雨林](https://bing.codexun.com/cn/detail/20250721)**<br>浅海中的鹿角珊瑚<br>*2025-07-21* | **[在月光下起舞](https://bing.codexun.com/cn/detail/20250720)**<br>望远镜下的月球表面照片<br>*2025-07-20* | 
| [![化石、瀑布与林间小径](https://www.bing.com/th?id=OHR.YohoNP_ZH-CN2349599497_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250719) | [![一切准备就绪，等待日落](https://www.bing.com/th?id=OHR.IcelandSolstice_ZH-CN6073168622_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250718) | [![追随香气的地平线](https://www.bing.com/th?id=OHR.FranceLavender_ZH-CN1639602547_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250717) | 
| **[化石、瀑布与林间小径](https://bing.codexun.com/cn/detail/20250719)**<br>幽鹤国家公园的伯吉斯山和翡翠湖, 不列颠哥伦比亚省, 加拿大<br>*2025-07-19* | **[一切准备就绪，等待日落](https://bing.codexun.com/cn/detail/20250718)**<br>塞里雅兰瀑布日落美景，冰岛<br>*2025-07-18* | **[追随香气的地平线](https://bing.codexun.com/cn/detail/20250717)**<br>瓦朗索勒高原的薰衣草田，法国<br>*2025-07-17* | 
| [![伊西斯女神的光辉照耀下](https://www.bing.com/th?id=OHR.TemplePhilae_ZH-CN1232015188_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250716) | [![永恒的光芒](https://www.bing.com/th?id=OHR.PerseidsPine_ZH-CN1081004815_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250715) | [![追逐海浪，掀起潮汐](https://www.bing.com/th?id=OHR.YoungShark_ZH-CN0887374663_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250714) | 
| **[伊西斯女神的光辉照耀下](https://bing.codexun.com/cn/detail/20250716)**<br>菲莱神庙<br>*2025-07-16* | **[永恒的光芒](https://bing.codexun.com/cn/detail/20250715)**<br>英仙座流星雨和一棵古老刺果松，大盆地国家公园，内华达州，美国<br>*2025-07-15* | **[追逐海浪，掀起潮汐](https://bing.codexun.com/cn/detail/20250714)**<br>加利西亚海域游弋的幼年大青鲨，西班牙<br>*2025-07-14* | 
| [![层层叠叠的岩石](https://www.bing.com/th?id=OHR.BasaltColumns_ZH-CN0743036217_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250713) | [![跟随妈妈的脚步](https://www.bing.com/th?id=OHR.ThomsonGazelle_ZH-CN0413171014_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250712) | [![把我们都算上](https://www.bing.com/th?id=OHR.TokyoSunrise_ZH-CN0091906710_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250711) | 
| **[层层叠叠的岩石](https://bing.codexun.com/cn/detail/20250713)**<br>卡尔夫沙马尔斯维克湾玄武岩柱，斯卡吉半岛，冰岛<br>*2025-07-13* | **[跟随妈妈的脚步](https://bing.codexun.com/cn/detail/20250712)**<br>汤氏瞪羚母亲和小鹿，马赛马拉，肯尼亚<br>*2025-07-12* | **[把我们都算上](https://bing.codexun.com/cn/detail/20250711)**<br>日出时的东京，日本<br>*2025-07-11* | 


---

## 按年份浏览壁纸档案

### 2025
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 6px; margin: 12px 0;">
<a href="https://bing.codexun.com/cn/archive/202508" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f3f4f6; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease; font-weight: 500;">202508</a>
<a href="https://bing.codexun.com/cn/archive/202507" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202507</a>
<a href="https://bing.codexun.com/cn/archive/202506" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202506</a>
</div>



---