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

[![刻在石头上](https://www.bing.com/th?id=OHR.BulgariaRocks_ZH-CN0234903972_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251022)

**刻在石头上**

在保加利亚巴尔干山脉西麓，贝洛格拉奇克石林如同一座天然画廊，每一块岩石都诉说着独特的故事。这些砂岩与石灰岩柱经过数百万年的风化与侵蚀，形成了千姿百态的奇特造型，当地人坚信其中有些轮廓酷似人物、动物，甚至完整的场景。因此，这些岩石也被赋予了富有想象力的名字，如"骑手岩"、"女学生岩"、"僧侣岩"等。在这片土地上，辨认岩石形状就像在玩一场大自然版的猜谜游戏，既有趣又充满惊喜。

*© EvaL Miko/Shutterstock (Bing China)*

---

## 最近30天

| | | |
|:---:|:---:|:---:|
| [![刻在石头上](https://www.bing.com/th?id=OHR.BulgariaRocks_ZH-CN0234903972_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251022) | [![鸟喙的故事](https://www.bing.com/th?id=OHR.ToucanForest_ZH-CN0072036253_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251021) | [![慢节奏的生活](https://www.bing.com/th?id=OHR.HoffmansSloth_ZH-CN7563408641_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251020) | 
| **[刻在石头上](https://bing.codexun.com/cn/detail/20251022)**<br>贝洛格拉齐克石林，保加利亚<br>*2025-10-22* | **[鸟喙的故事](https://bing.codexun.com/cn/detail/20251021)**<br>哥斯达黎加的厚嘴巨嘴鸟<br>*2025-10-21* | **[慢节奏的生活](https://bing.codexun.com/cn/detail/20251020)**<br>霍氏树懒，厄瓜多尔<br>*2025-10-20* | 
| [![痴迷科学](https://www.bing.com/th?id=OHR.AppleHarvest_ZH-CN7317228007_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251019) | [![那座铭记往昔的山丘](https://www.bing.com/th?id=OHR.SilburyHill_ZH-CN6666447580_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251018) | [![爱上密歇根](https://www.bing.com/th?id=OHR.RockRiverFalls_ZH-CN6532185546_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251017) | 
| **[痴迷科学](https://bing.codexun.com/cn/detail/20251019)**<br>即将收获的苹果，明尼苏达州，美国<br>*2025-10-19* | **[那座铭记往昔的山丘](https://bing.codexun.com/cn/detail/20251018)**<br>西尔布利山的新石器时代遗址，蒂尔斯黑德，威尔特郡，英国<br>*2025-10-18* | **[爱上密歇根](https://bing.codexun.com/cn/detail/20251017)**<br>罗克河瀑布，上半岛，密歇根州，美国<br>*2025-10-17* | 
| [![幽灵之猫](https://www.bing.com/th?id=OHR.SiberianLynx_ZH-CN0749166653_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251016) | [![孢子奇遇记](https://www.bing.com/th?id=OHR.AmethystLaccaria_ZH-CN0643667280_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251015) | [![蓝与白的梦境](https://www.bing.com/th?id=OHR.OiaSantorini_ZH-CN0531650189_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251014) | 
| **[幽灵之猫](https://bing.codexun.com/cn/detail/20251016)**<br>欧亚猞猁，西伯利亚<br>*2025-10-16* | **[孢子奇遇记](https://bing.codexun.com/cn/detail/20251015)**<br>紫蜡蘑，西贝克，华盛顿州，美国<br>*2025-10-15* | **[蓝与白的梦境](https://bing.codexun.com/cn/detail/20251014)**<br>伊亚镇，圣托里尼岛，希腊<br>*2025-10-14* | 
| [![水声低语](https://www.bing.com/th?id=OHR.HinterseeWaterfall_ZH-CN0432994081_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251013) | [![爱上萨拉纳克](https://www.bing.com/th?id=OHR.SaranacLake_ZH-CN0224689397_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251012) | [![下一站：墨西哥！](https://www.bing.com/th?id=OHR.WoodDuckHen_ZH-CN9558916773_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251011) | 
| **[水声低语](https://bing.codexun.com/cn/detail/20251013)**<br>温巴赫峡谷瀑布，巴伐利亚州，德国<br>*2025-10-13* | **[爱上萨拉纳克](https://bing.codexun.com/cn/detail/20251012)**<br>萨拉纳克湖村，阿迪朗达克山脉，纽约州，美国<br>*2025-10-12* | **[下一站：墨西哥！](https://bing.codexun.com/cn/detail/20251011)**<br>林鸳鸯，美国<br>*2025-10-11* | 
| [![思绪之礁](https://www.bing.com/th?id=OHR.MonurikiFiji_ZH-CN9178115886_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251010) | [![宇宙在绽放](https://www.bing.com/th?id=OHR.WebbPillars_ZH-CN9054137596_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251009) | [![动态伪装](https://www.bing.com/th?id=OHR.OctopusCyanea_ZH-CN8948609460_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251008) | 
| **[思绪之礁](https://bing.codexun.com/cn/detail/20251010)**<br>莫努里基岛周边的珊瑚礁，玛玛努卡群岛，斐济<br>*2025-10-10* | **[宇宙在绽放](https://bing.codexun.com/cn/detail/20251009)**<br>‌詹姆斯·韦伯太空望远镜观测的创生之柱<br>*2025-10-09* | **[动态伪装](https://bing.codexun.com/cn/detail/20251008)**<br>白日章鱼, 毛伊岛, 夏威夷, 美国<br>*2025-10-08* | 
| [![金色的秋日余晖](https://www.bing.com/th?id=OHR.RidgwayAspens_ZH-CN8735375502_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251007) | [![千里共婵娟](https://www.bing.com/th?id=OHR.AnshunBridge_ZH-CN8392458102_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251006) | [![庆祝智慧！](https://www.bing.com/th?id=OHR.TeacherOwl_ZH-CN8289875605_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251005) | 
| **[金色的秋日余晖](https://bing.codexun.com/cn/detail/20251007)**<br>里奇韦附近斯内弗尔斯山脚下的秋色, 科罗拉多州, 美国<br>*2025-10-07* | **[千里共婵娟](https://bing.codexun.com/cn/detail/20251006)**<br>安顺桥中秋灯展，成都，中国<br>*2025-10-06* | **[庆祝智慧！](https://bing.codexun.com/cn/detail/20251005)**<br>中欧森林里的鬼鸮<br>*2025-10-05* | 
| [![使命必达](https://www.bing.com/th?id=OHR.DragonEndeavour_ZH-CN8160066040_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251004) | [![雾中遐想](https://www.bing.com/th?id=OHR.SkyeHeather_ZH-CN2820283990_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251003) | [![法定自然区](https://www.bing.com/th?id=OHR.OxbowBend_ZH-CN7211791969_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251002) | 
| **[使命必达](https://bing.codexun.com/cn/detail/20251004)**<br>从SpaceX载人龙飞船“奋进号”视角看到的国际空间站主太阳能电池阵列<br>*2025-10-04* | **[雾中遐想](https://bing.codexun.com/cn/detail/20251003)**<br>布里特尔峡谷里生长的帚石楠花, 斯凯岛, 苏格兰<br>*2025-10-03* | **[法定自然区](https://bing.codexun.com/cn/detail/20251002)**<br>蛇河上的牛轭湖, 大提顿国家公园, 怀俄明州, 美国<br>*2025-10-02* | 
| [![克拉克山脉的回声](https://www.bing.com/th?id=OHR.YosemiteClark_ZH-CN7179533292_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20251001) | [![坚持重要的事情](https://www.bing.com/th?id=OHR.EucalyptusKoala_ZH-CN6942451940_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250930) | [![彩虹骑行与宁静氛围](https://www.bing.com/th?id=OHR.HoutenHouses_ZH-CN6776452438_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250929) | 
| **[克拉克山脉的回声](https://bing.codexun.com/cn/detail/20251001)**<br>克拉克山脉, 内华达山脉, 约塞米蒂国家公园, 加利福尼亚州, 美国<br>*2025-10-01* | **[坚持重要的事情](https://bing.codexun.com/cn/detail/20250930)**<br>桉树上的考拉, 大奥特维国家公园, 澳大利亚<br>*2025-09-30* | **[彩虹骑行与宁静氛围](https://bing.codexun.com/cn/detail/20250929)**<br>豪滕镇的彩虹屋, 荷兰<br>*2025-09-29* | 
| [![品味皮恩扎](https://www.bing.com/th?id=OHR.PienzaItaly_ZH-CN6564335348_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250928) | [![美丽的星空](https://www.bing.com/th?id=OHR.TankLakes_ZH-CN6402368934_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250927) | [![速度与毛茸茸](https://www.bing.com/th?id=OHR.AutumnChipmunk_ZH-CN6224482683_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250926) | 
| **[品味皮恩扎](https://bing.codexun.com/cn/detail/20250928)**<br>托斯卡纳的皮恩扎镇, 意大利<br>*2025-09-28* | **[美丽的星空](https://bing.codexun.com/cn/detail/20250927)**<br>坦克湖<br>*2025-09-27* | **[速度与毛茸茸](https://bing.codexun.com/cn/detail/20250926)**<br>最小花栗鼠, 库特奈国家公园, 蒙大拿州, 美国<br>*2025-09-26* | 
| [![忠勇的雕刻石](https://www.bing.com/th?id=OHR.FortChittorgarh_ZH-CN5999553283_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250925) | [![孤独的巨人](https://www.bing.com/th?id=OHR.BearLodge_ZH-CN5880511888_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250924) | [![树树皆秋色](https://www.bing.com/th?id=OHR.AutumnalEquinoxY25_ZH-CN5692548297_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20250923) | 
| **[忠勇的雕刻石](https://bing.codexun.com/cn/detail/20250925)**<br>奇陶尔加尔堡, 拉贾斯坦邦, 印度<br>*2025-09-25* | **[孤独的巨人](https://bing.codexun.com/cn/detail/20250924)**<br>魔鬼塔国家纪念碑, 怀俄明州，美国<br>*2025-09-24* | **[树树皆秋色](https://bing.codexun.com/cn/detail/20250923)**<br>航拍中国江苏省常州翠竹公园<br>*2025-09-23* | 


---

## 按年份浏览壁纸档案

### 2025
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 6px; margin: 12px 0;">
<a href="https://bing.codexun.com/cn/archive/202510" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f3f4f6; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease; font-weight: 500;">202510</a>
<a href="https://bing.codexun.com/cn/archive/202509" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202509</a>
<a href="https://bing.codexun.com/cn/archive/202508" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202508</a>
<a href="https://bing.codexun.com/cn/archive/202507" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202507</a>
<a href="https://bing.codexun.com/cn/archive/202506" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;">202506</a>
</div>



---