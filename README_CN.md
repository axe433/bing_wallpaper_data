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

[![日落之后，探索仍在继续](https://www.bing.com/th?id=OHR.SunsetKiva_ZH-CN3978606378_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260420)

**日落之后，探索仍在继续**

国家公园周，是你暂别日常、走向自然的最佳契机。这一为期九天的庆祝活动将于4月18日至26日举行，聚焦国家公园体系中400多处自然与文化遗产地。在这里，自然风光与人文历史交织，为人们带来难忘的户外体验。从海岸线与森林，到辽阔的沙漠景观，这些受保护的区域邀请人们走进自然，感受宁静，心怀敬畏。

*© Jason Hatfield/Tandem Stills + Motion (Bing China)*

---

## 最近30天

| | | |
|:---:|:---:|:---:|
| [![日落之后，探索仍在继续](https://www.bing.com/th?id=OHR.SunsetKiva_ZH-CN3978606378_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260420) | [![潮汐留下的印记](https://www.bing.com/th?id=OHR.TranBA_ZH-CN3467060262_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260419) | [![未完成巨像的静默](https://www.bing.com/th?id=OHR.MaoiStatues_ZH-CN3219447748_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260418) | 
| **[日落之后，探索仍在继续](https://bing.codexun.com/cn/detail/20260420)**<br>夕阳下的峡谷地国家公园，莫阿布，犹他州，美国<br>*2026-04-20* | **[潮汐留下的印记](https://bing.codexun.com/cn/detail/20260419)**<br>镜面海滩，塞古罗港，巴伊亚州，巴西<br>*2026-04-19* | **[未完成巨像的静默](https://bing.codexun.com/cn/detail/20260418)**<br>摩艾石像采石场，拉诺拉拉库，复活节岛，智利<br>*2026-04-18* | 
| [![蝙蝠信号：开启](https://www.bing.com/th?id=OHR.FlyingFoxMom_ZH-CN2913012516_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260417) | [![花瓣巡游](https://www.bing.com/th?id=OHR.SkagitTulips_ZH-CN4234324174_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260416) | [![走进这幅鲜活的画布](https://www.bing.com/th?id=OHR.VanGoghFields_ZH-CN3495668941_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260415) | 
| **[蝙蝠信号：开启](https://bing.codexun.com/cn/detail/20260417)**<br>灰头狐蝠母亲携幼崽，雅拉湾国家公园，澳大利亚<br>*2026-04-17* | **[花瓣巡游](https://bing.codexun.com/cn/detail/20260416)**<br>斯卡吉特谷地郁金香花田, 华盛顿, 美国<br>*2026-04-16* | **[走进这幅鲜活的画布](https://bing.codexun.com/cn/detail/20260415)**<br>光之采石场的文森特·梵高展览, 莱博德普罗旺斯, 法国<br>*2026-04-15* | 
| [![珊瑚礁邻居](https://www.bing.com/th?id=OHR.OcellarisClownfish_ZH-CN9362948727_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260414) | [![当灯光熄灭之后](https://www.bing.com/th?id=OHR.BorregoStars_ZH-CN8915519147_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260413) | [![离开地球的第一步](https://www.bing.com/th?id=OHR.SpaceTrails_ZH-CN8377463217_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260412) | 
| **[珊瑚礁邻居](https://bing.codexun.com/cn/detail/20260414)**<br>海葵中的普通小丑鱼, 拉贾安帕特群岛, 印度尼西亚<br>*2026-04-14* | **[当灯光熄灭之后](https://bing.codexun.com/cn/detail/20260413)**<br>安扎-博雷戈沙漠州立公园上空的银河, 加利福尼亚州, 美国<br>*2026-04-13* | **[离开地球的第一步](https://bing.codexun.com/cn/detail/20260412)**<br>城市灯光在下方划过, 拍摄于国际空间站<br>*2026-04-12* | 
| [![火山外衣](https://www.bing.com/th?id=OHR.PlayaPapagayo_ZH-CN7708804019_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260411) | [![算计的小爪子](https://www.bing.com/th?id=OHR.FoxSiblings_ZH-CN8133856518_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260410) | [![光之水帘](https://www.bing.com/th?id=OHR.WalesWaterfall_ZH-CN3175091833_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260409) | 
| **[火山外衣](https://bing.codexun.com/cn/detail/20260411)**<br>帕帕加约海滩, 兰萨罗特, 加那利群岛, 西班牙<br>*2026-04-11* | **[算计的小爪子](https://bing.codexun.com/cn/detail/20260410)**<br>卡鲁拉国家公园的两只幼年赤狐, 爱沙尼亚<br>*2026-04-10* | **[光之水帘](https://bing.codexun.com/cn/detail/20260409)**<br>雪落瀑布，布雷肯比肯斯国家公园，威尔士<br>*2026-04-09* | 
| [![翡翠之城](https://www.bing.com/th?id=OHR.SeattleSunrise_ZH-CN2884575647_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260408) | [![一根树枝，一点工程](https://www.bing.com/th?id=OHR.BeaverPortrait_ZH-CN4700069789_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260407) | [![芬芳四月](https://www.bing.com/th?id=OHR.CastleBlossoms_ZH-CN3064288127_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260406) | 
| **[翡翠之城](https://bing.codexun.com/cn/detail/20260408)**<br>西雅图，华盛顿州，美国<br>*2026-04-08* | **[一根树枝，一点工程](https://bing.codexun.com/cn/detail/20260407)**<br>河狸，德国<br>*2026-04-07* | **[芬芳四月](https://bing.codexun.com/cn/detail/20260406)**<br>樱花盛开的弘前城，弘前，日本<br>*2026-04-06* | 
| [![静静绽放的变化](https://www.bing.com/th?id=OHR.SpringSnowdrops_ZH-CN2933051747_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260405) | [![求偶展示场的故事](https://www.bing.com/th?id=OHR.GrouseGuff_ZH-CN2647001885_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260404) | [![一次挥动桥臂，连接两岸](https://www.bing.com/th?id=OHR.ArmbrugBridge_ZH-CN4600005169_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260403) | 
| **[静静绽放的变化](https://bing.codexun.com/cn/detail/20260405)**<br>春天的雪钟花<br>*2026-04-05* | **[求偶展示场的故事](https://bing.codexun.com/cn/detail/20260404)**<br>求偶展示场上对峙的雄性黑琴鸡，爱沙尼亚<br>*2026-04-04* | **[一次挥动桥臂，连接两岸](https://bing.codexun.com/cn/detail/20260403)**<br>阿姆布鲁大桥，阿姆斯特丹，荷兰<br>*2026-04-03* | 
| [![春天的图案](https://www.bing.com/th?id=OHR.WildflowerValley_ZH-CN7048300331_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260402) | [![跃入四月](https://www.bing.com/th?id=OHR.JapaneseTreeFrog_ZH-CN6467379766_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260401) | [![地下天堂](https://www.bing.com/th?id=OHR.ParadiseCave_ZH-CN6371627729_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260331) | 
| **[春天的图案](https://bing.codexun.com/cn/detail/20260402)**<br>野花绽放, 中央谷地, 加利福尼亚州, 美国<br>*2026-04-02* | **[跃入四月](https://bing.codexun.com/cn/detail/20260401)**<br>粉色牵牛花里的日本树蛙<br>*2026-04-01* | **[地下天堂](https://bing.codexun.com/cn/detail/20260331)**<br>天堂洞, 峰牙-格邦国家公园, 越南<br>*2026-03-31* | 
| [![优雅的动态](https://www.bing.com/th?id=OHR.IndiaCranes_ZH-CN5871338482_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260330) | [![海边的宁静](https://www.bing.com/th?id=OHR.PeggysLighthouse_ZH-CN5730463973_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260329) | [![未驯服的精神](https://www.bing.com/th?id=OHR.CapeBuffalo_ZH-CN5591123662_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260328) | 
| **[优雅的动态](https://bing.codexun.com/cn/detail/20260330)**<br>蓑羽鹤, 印度<br>*2026-03-30* | **[海边的宁静](https://bing.codexun.com/cn/detail/20260329)**<br>佩吉角灯塔, 大西洋海岸, 新斯科舍省, 加拿大<br>*2026-03-29* | **[未驯服的精神](https://bing.codexun.com/cn/detail/20260328)**<br>非洲水牛, 恩戈罗恩戈罗火山口, 坦桑尼亚<br>*2026-03-28* | 
| [![依然明亮地燃烧着](https://www.bing.com/th?id=OHR.RadioCityHall_ZH-CN5492649461_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260327) | [![凌驾荒野之上](https://www.bing.com/th?id=OHR.LoganCreek_ZH-CN5372283365_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260326) | [![海牛的秘密生活](https://www.bing.com/th?id=OHR.ManateeSpring_ZH-CN5252847120_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260325) | 
| **[依然明亮地燃烧着](https://bing.codexun.com/cn/detail/20260327)**<br>纽约市的无线电城音乐厅, 美国<br>*2026-03-27* | **[凌驾荒野之上](https://bing.codexun.com/cn/detail/20260326)**<br>洛根溪吊桥，西海岸步道，加拿大<br>*2026-03-26* | **[海牛的秘密生活](https://bing.codexun.com/cn/detail/20260325)**<br>淡水泉中的幼年海牛，水晶河，佛罗里达州，美国<br>*2026-03-25* | 
| [![春天的形状](https://www.bing.com/th?id=OHR.WuhanCherryBlossom_ZH-CN1031985926_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260324) | [![当水划出界线](https://www.bing.com/th?id=OHR.SonoranStorm_ZH-CN0579792563_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260323) | [![当水划出界线](https://www.bing.com/th?id=OHR.TanganyikaWater_ZH-CN4884850067_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260322) | 
| **[春天的形状](https://bing.codexun.com/cn/detail/20260324)**<br>东湖樱花园的樱花，武汉，中国<br>*2026-03-24* | **[当水划出界线](https://bing.codexun.com/cn/detail/20260323)**<br>坦噶尼喀湖，非洲<br>*2026-03-23* | **[当水划出界线](https://bing.codexun.com/cn/detail/20260322)**<br>坦噶尼喀湖，非洲<br>*2026-03-22* | 


---

## 按年份浏览壁纸档案

### 2026
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 6px; margin: 12px 0;">
<a href="https://bing.codexun.com/cn/archive/202604" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f3f4f6; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease; font-weight: 500;">202604</a>
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