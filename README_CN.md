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

[![排练中的翅膀](https://www.bing.com/th?id=OHR.SunbitternEcuador_ZH-CN9772788253_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260312)

**排练中的翅膀**

在厄瓜多尔的云雾森林高处，一只幼年日鳽展开翅膀进行早期展示，橙色、黑色和白色的斑纹在透过树叶的绿色光影中闪现。突如其来的色彩对比穿透覆盖苔藓的枝干和叶影下的林下层，呈现出这一物种戏剧性的翅膀斑纹。成年的日鳽通常在防御展示时才会显露这些醒目的斑纹，短暂地将这只原本隐秘的鸟变成引人注目的视觉奇观。

*© Andy Rouse/naturepl.com (Bing China)*

---

## 最近30天

| | | |
|:---:|:---:|:---:|
| [![排练中的翅膀](https://www.bing.com/th?id=OHR.SunbitternEcuador_ZH-CN9772788253_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260312) | [![一个美好的春天](https://www.bing.com/th?id=OHR.PeachBloom_ZH-CN9660251274_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260311) | [![霜下之火](https://www.bing.com/th?id=OHR.SpringIceland_ZH-CN9545282898_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260310) | 
| **[排练中的翅膀](https://bing.codexun.com/cn/detail/20260312)**<br>幼年日鳽在巢穴附近展示求偶行为, 厄瓜多尔<br>*2026-03-12* | **[一个美好的春天](https://bing.codexun.com/cn/detail/20260311)**<br>盛开的桃树, 谢萨, 穆尔西亚, 西班牙<br>*2026-03-11* | **[霜下之火](https://bing.codexun.com/cn/detail/20260310)**<br>赫韦拉韦利尔的布拉赫维尔地热池, 冰岛<br>*2026-03-10* | 
| [![一次恰到好处的午睡](https://www.bing.com/th?id=OHR.NappingSeal_ZH-CN9424683964_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260309) | [![节约日光的艺术](https://www.bing.com/th?id=OHR.UlmClock_ZH-CN9282560066_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260308) | [![治愈、宁静且充满希望](https://www.bing.com/th?id=OHR.BrockenSunrise_ZH-CN4930790850_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260307) | 
| **[一次恰到好处的午睡](https://bing.codexun.com/cn/detail/20260309)**<br>在海滩上睡觉的灰海豹, 奥克尼群岛, 苏格兰<br>*2026-03-09* | **[节约日光的艺术](https://bing.codexun.com/cn/detail/20260308)**<br>乌尔姆市政厅的天文钟, 德国<br>*2026-03-08* | **[治愈、宁静且充满希望](https://bing.codexun.com/cn/detail/20260307)**<br>布罗肯峰的日出, 哈尔茨国家公园, 德国<br>*2026-03-07* | 
| [![混凝土中铸造的波浪](https://www.bing.com/th?id=OHR.WaveDenmark_ZH-CN8825888678_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260306) | [![古老岩石，现代灯光](https://www.bing.com/th?id=OHR.GoremeTwilight_ZH-CN3731931947_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260305) | [![聚光灯下的番红花](https://www.bing.com/th?id=OHR.RilaCrocuses_ZH-CN3650360951_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260304) | 
| **[混凝土中铸造的波浪](https://bing.codexun.com/cn/detail/20260306)**<br>波浪住宅楼, 瓦埃勒, 丹麦<br>*2026-03-06* | **[古老岩石，现代灯光](https://bing.codexun.com/cn/detail/20260305)**<br>格雷梅的傍晚, 卡帕多西亚, 土耳其<br>*2026-03-05* | **[聚光灯下的番红花](https://bing.codexun.com/cn/detail/20260304)**<br>紫番红花, 里拉七湖, 保加利亚<br>*2026-03-04* | 
| [![花灯映月，团圆吉祥](https://www.bing.com/th?id=OHR.LanternFestivalY26_ZH-CN9186685796_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260303) | [![漂浮的传承](https://www.bing.com/th?id=OHR.SamuiThailand_ZH-CN3323790951_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260302) | [![每一步，都是传承](https://www.bing.com/th?id=OHR.BalearesDay_ZH-CN5024902433_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260301) | 
| **[花灯映月，团圆吉祥](https://bing.codexun.com/cn/detail/20260303)**<br>元宵节期间悬挂的宫灯，北京自贡灯会现场，北京，中国<br>*2026-03-03* | **[漂浮的传承](https://bing.codexun.com/cn/detail/20260302)**<br>苏梅岛的港口和长尾船, 泰国<br>*2026-03-02* | **[每一步，都是传承](https://bing.codexun.com/cn/detail/20260301)**<br>伊维萨岛, 巴利阿里群岛, 西班牙<br>*2026-03-01* | 
| [![洋溢着社区氛围](https://www.bing.com/th?id=OHR.OloupenaFalls_ZH-CN2980118660_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260228) | [![薄冰上的生活](https://www.bing.com/th?id=OHR.ArcitcCub_ZH-CN2725049760_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260227) | [![一幅壮丽的景象](https://www.bing.com/th?id=OHR.GrandSunset_ZH-CN1905986519_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260226) | 
| **[洋溢着社区氛围](https://bing.codexun.com/cn/detail/20260228)**<br>奥洛乌佩纳瀑布, 莫洛凯岛, 夏威夷, 美国<br>*2026-02-28* | **[薄冰上的生活](https://bing.codexun.com/cn/detail/20260227)**<br>北极熊幼崽走过浮冰, 北极国家野生动物保护区, 阿拉斯加州, 美国<br>*2026-02-27* | **[一幅壮丽的景象](https://bing.codexun.com/cn/detail/20260226)**<br>大峡谷和科罗拉多河，亚利桑那州，美国<br>*2026-02-26* | 
| [![冰，由内而外透出光芒](https://www.bing.com/th?id=OHR.MendenhallCave_ZH-CN1850649760_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260225) | [![池底的生命律动](https://www.bing.com/th?id=OHR.TulumLilies_ZH-CN0959403613_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260224) | [![雪原之王](https://www.bing.com/th?id=OHR.BavariaEgret_ZH-CN0521643213_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260223) | 
| **[冰，由内而外透出光芒](https://bing.codexun.com/cn/detail/20260225)**<br>门登霍尔冰川的冰洞，阿拉斯加州，美国<br>*2026-02-25* | **[池底的生命律动](https://bing.codexun.com/cn/detail/20260224)**<br>大天坑里的睡莲，图卢姆，墨西哥<br>*2026-02-24* | **[雪原之王](https://bing.codexun.com/cn/detail/20260223)**<br>大白鹭，上巴伐利亚州，德国<br>*2026-02-23* | 
| [![群山的母亲](https://www.bing.com/th?id=OHR.MamTorSunrise_ZH-CN9698497298_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260222) | [![冬日的低语](https://www.bing.com/th?id=OHR.TetonFox_ZH-CN9461948674_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260221) | [![光照之处](https://www.bing.com/th?id=OHR.AdamsFirefall_ZH-CN9409143565_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260220) | 
| **[群山的母亲](https://bing.codexun.com/cn/detail/20260222)**<br>马姆托尔山，德比郡，英格兰<br>*2026-02-22* | **[冬日的低语](https://bing.codexun.com/cn/detail/20260221)**<br>一只红狐狸站在雪地里，大提顿国家公园，怀俄明州，美国<br>*2026-02-21* | **[光照之处](https://bing.codexun.com/cn/detail/20260220)**<br>约塞米蒂国家公园里的火瀑布，加利福尼亚州，美国<br>*2026-02-20* | 
| [![大地凝视着我们](https://www.bing.com/th?id=OHR.DragonsEyeRock_ZH-CN6164478776_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260219) | [![生而自由，永不驯服](https://www.bing.com/th?id=OHR.PrzewalskisHorse_ZH-CN5785609662_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260218) | [![福气满满，马年大吉](https://www.bing.com/th?id=OHR.SpringFestivalY26_ZH-CN0228318064_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260217) | 
| **[大地凝视着我们](https://bing.codexun.com/cn/detail/20260219)**<br>乌塔克莱夫海滩的“龙之眼”岩层，挪威<br>*2026-02-19* | **[生而自由，永不驯服](https://bing.codexun.com/cn/detail/20260218)**<br>普氏野马<br>*2026-02-18* | **[福气满满，马年大吉](https://bing.codexun.com/cn/detail/20260217)**<br>中国春节传统汉字“福”<br>*2026-02-17* | 
| [![祝除夕团圆，新年顺遂！](https://www.bing.com/th?id=OHR.ChineseNewYearEveY26_ZH-CN7770318975_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260216) | [![浪涛下的歌谣](https://www.bing.com/th?id=OHR.MontereyHumpbacks_ZH-CN5426789466_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260215) | [![爱意绽放](https://www.bing.com/th?id=OHR.ValentineHearts_ZH-CN5332774664_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260214) | 
| **[祝除夕团圆，新年顺遂！](https://bing.codexun.com/cn/detail/20260216)**<br>庆祝春节的龙形灯笼，中国西安<br>*2026-02-16* | **[浪涛下的歌谣](https://bing.codexun.com/cn/detail/20260215)**<br>蒙特雷湾的大翅鲸<br>*2026-02-15* | **[爱意绽放](https://bing.codexun.com/cn/detail/20260214)**<br>荷包牡丹<br>*2026-02-14* | 
| [![为拉近距离而建](https://www.bing.com/th?id=OHR.FriendshipBridge_ZH-CN5199165736_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260213) | [![聚焦进化](https://www.bing.com/th?id=OHR.DarwinBooby_ZH-CN4925779873_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260212) | [![对比之谷](https://www.bing.com/th?id=OHR.BadwaterFlats_ZH-CN4713617982_UHD.jpg&pid=hp&w=2560)](https://bing.codexun.com/cn/detail/20260211) | 
| **[为拉近距离而建](https://bing.codexun.com/cn/detail/20260213)**<br>连接老挝和泰国的第三座泰老友谊大桥<br>*2026-02-13* | **[聚焦进化](https://bing.codexun.com/cn/detail/20260212)**<br>蓝脚鲣鸟，加拉帕戈斯群岛, 厄瓜多尔<br>*2026-02-12* | **[对比之谷](https://bing.codexun.com/cn/detail/20260211)**<br>死亡谷国家公园恶水盆地的盐滩, 加利福尼亚州, 美国<br>*2026-02-11* | 


---

## 按年份浏览壁纸档案

### 2026
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 6px; margin: 12px 0;">
<a href="https://bing.codexun.com/cn/archive/202603" style="padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f3f4f6; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease; font-weight: 500;">202603</a>
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