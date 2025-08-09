#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
from datetime import datetime
from typing import List, Dict, Any

def load_wallpaper_data(country: str) -> List[Dict[str, Any]]:
    """加载指定国家的壁纸数据"""
    file_path = f'./jsonc/{country}/bing.jsonc'
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Warning: {file_path} not found")
        return []

def get_available_countries() -> List[str]:
    """获取所有可用的国家代码"""
    jsonc_dir = "./jsonc"
    countries = []
    
    if not os.path.exists(jsonc_dir):
        print(f"JSONC目录不存在: {jsonc_dir}")
        return countries
    
    for item in os.listdir(jsonc_dir):
        country_dir = os.path.join(jsonc_dir, item)
        if os.path.isdir(country_dir):
            bing_file = os.path.join(country_dir, "bing.jsonc")
            if os.path.exists(bing_file):
                countries.append(item)
    
    return sorted(countries)

def get_country_flag_mapping() -> Dict[str, str]:
    """获取国家或地区代码到国旗emoji的映射"""
    return {
        'ar': '🇦🇷',  # 阿根廷
        'au': '🇦🇺',  # 澳大利亚
        'br': '🇧🇷',  # 巴西
        'ca': '🇨🇦',  # 加拿大
        'cn': '🇨🇳',  # 中国
        'cz': '🇨🇿',  # 捷克
        'de': '🇩🇪',  # 德国
        'dk': '🇩🇰',  # 丹麦
        'es': '🇪🇸',  # 西班牙
        'fi': '🇫🇮',  # 芬兰
        'fr': '🇫🇷',  # 法国
        'gb': '🇬🇧',  # 英国
        'gr': '🇬🇷',  # 希腊
        'hk': '🇭🇰',  # 香港
        'id': '🇮🇩',  # 印度尼西亚
        'in': '🇮🇳',  # 印度
        'it': '🇮🇹',  # 意大利
        'jp': '🇯🇵',  # 日本
        'kr': '🇰🇷',  # 韩国
        'my': '🇲🇾',  # 马来西亚
        'nl': '🇳🇱',  # 荷兰
        'no': '🇳🇴',  # 挪威
        'pl': '🇵🇱',  # 波兰
        'pt': '🇵🇹',  # 葡萄牙
        'ru': '🇷🇺',  # 俄罗斯
        'se': '🇸🇪',  # 瑞典
        'sg': '🇸🇬',  # 新加坡
        'th': '🇹🇭',  # 泰国
        'tr': '🇹🇷',  # 土耳其
        'tw': '🇹🇼',  # 台湾
        'ua': '🇺🇦',  # 乌克兰
        'us': '🇺🇸',  # 美国
        'vn': '🇻🇳',  # 越南
        'za': '🇿🇦'   # 南非
    }

def get_country_name_mapping() -> Dict[str, Dict[str, str]]:
    """获取国家代码到国家名称的映射"""
    return {
        'ar': {'en': 'Argentina', 'cn': '阿根廷'},
        'au': {'en': 'Australia', 'cn': '澳大利亚'},
        'br': {'en': 'Brazil', 'cn': '巴西'},
        'ca': {'en': 'Canada', 'cn': '加拿大'},
        'cn': {'en': 'China', 'cn': '中国'},
        'cz': {'en': 'Czech Republic', 'cn': '捷克'},
        'de': {'en': 'Germany', 'cn': '德国'},
        'dk': {'en': 'Denmark', 'cn': '丹麦'},
        'es': {'en': 'Spain', 'cn': '西班牙'},
        'fi': {'en': 'Finland', 'cn': '芬兰'},
        'fr': {'en': 'France', 'cn': '法国'},
        'gb': {'en': 'United Kingdom', 'cn': '英国'},
        'gr': {'en': 'Greece', 'cn': '希腊'},
        'hk': {'en': 'Hong Kong', 'cn': '香港'},
        'id': {'en': 'Indonesia', 'cn': '印度尼西亚'},
        'in': {'en': 'India', 'cn': '印度'},
        'it': {'en': 'Italy', 'cn': '意大利'},
        'jp': {'en': 'Japan', 'cn': '日本'},
        'kr': {'en': 'South Korea', 'cn': '韩国'},
        'my': {'en': 'Malaysia', 'cn': '马来西亚'},
        'nl': {'en': 'Netherlands', 'cn': '荷兰'},
        'no': {'en': 'Norway', 'cn': '挪威'},
        'pl': {'en': 'Poland', 'cn': '波兰'},
        'pt': {'en': 'Portugal', 'cn': '葡萄牙'},
        'ru': {'en': 'Russia', 'cn': '俄罗斯'},
        'se': {'en': 'Sweden', 'cn': '瑞典'},
        'sg': {'en': 'Singapore', 'cn': '新加坡'},
        'th': {'en': 'Thailand', 'cn': '泰国'},
        'tr': {'en': 'Turkey', 'cn': '土耳其'},
        'tw': {'en': 'Taiwan', 'cn': '台湾'},
        'ua': {'en': 'Ukraine', 'cn': '乌克兰'},
        'us': {'en': 'United States', 'cn': '美国'},
        'vn': {'en': 'Vietnam', 'cn': '越南'},
        'za': {'en': 'South Africa', 'cn': '南非'}
    }

def generate_supported_countries_section(countries: List[str], lang: str) -> str:
    """生成支持的国家和地区部分"""
    country_mapping = get_country_name_mapping()
    flag_mapping = get_country_flag_mapping()
    
    if lang == 'cn':
        section_title = "## 🌍 支持的国家和地区"
        section_desc = f"项目支持以下 {len(countries)} 个国家和地区："
        table_headers = "| 代码 | 国家/地区 | 代码 | 国家/地区 | 代码 | 国家/地区 |"
        table_separator = "|------|-----------|------|-----------|------|-----------|"
    else:
        section_title = "## 🌍 Supported Countries and Regions"
        section_desc = f"The project supports the following {len(countries)} countries and regions:"
        table_headers = "| Code | Country/Region | Code | Country/Region | Code | Country/Region |"
        table_separator = "|------|----------------|------|----------------|------|----------------|"
    
    content = f"{section_title}\n\n{section_desc}\n\n{table_headers}\n{table_separator}\n"
    
    # 按每行3个分组
    for i in range(0, len(countries), 3):
        row_countries = countries[i:i+3]
        row_content = "| "
        
        for country in row_countries:
            country_name = country_mapping.get(country, {}).get(lang, country.upper())
            country_flag = flag_mapping.get(country, '🏳️')
            country_link = f"[{country_flag} {country_name}](markdown/wallpaper-list-{country}.md)"
            row_content += f"`{country}` | {country_link} | "
        
        # 补齐空列
        while len(row_countries) < 3:
            row_content += " | "
            row_countries.append("")
        
        content += row_content + "\n"
    
    return content

def get_base_readme_content(lang: str) -> str:
    """获取基础README内容"""
    if lang == 'cn':
        # 读取中文README模板内容
        try:
            with open('templates/README_CN_template.md', 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print("Warning: templates/README_CN_template.md not found")
            return "# Bing 壁纸数据爬虫与文档生成器\n\n基础中文README内容"
    else:
        # 读取英文README模板内容
        try:
            with open('templates/README_template.md', 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print("Warning: templates/README_template.md not found")
            return "# Bing Wallpaper Data Crawler and Markdown Generator\n\nBase English README content"

def generate_country_links_section(countries: List[str], lang: str) -> str:
    """生成各国壁纸链接部分"""
    country_mapping = get_country_name_mapping()
    flag_mapping = get_country_flag_mapping()
    
    if lang == 'cn':
        section_title = "## 🌍 各国壁纸链接"
        section_desc = "点击下方链接查看各国的壁纸："
    else:
        section_title = "## 🌍 Country Wallpaper Links"
        section_desc = "Click the links below to view wallpaper for each country:"
    
    links_content = f"{section_title}\n\n{section_desc}\n\n"
    
    # 按每行5个分组
    for i in range(0, len(countries), 5):
        row_countries = countries[i:i+5]
        row_content = "| "
        
        for country in row_countries:
            country_name = country_mapping.get(country, {}).get(lang, country.upper())
            country_flag = flag_mapping.get(country, '🏳️')
            link = f"[{country_flag} {country_name}](https://bing.codexun.com/{country})"
            row_content += f"{link} | "
        
        # 补齐空列
        while len(row_countries) < 5:
            row_content += " | "
            row_countries.append("")
        
        links_content += row_content + "\n"
        
        # 添加表格分隔符（只在第一行后添加）
        if i == 0:
            links_content += "|:---:|:---:|:---:|:---:|:---:|\n"
    
    return links_content

def get_wallpaper_list_content(country: str, lang: str) -> str:
    """获取完整的壁纸列表内容（包括今日壁纸、最近30天和按月导航）"""
    wallpaper_file = f"markdown/wallpaper-list-{country}.md"
    
    try:
        with open(wallpaper_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取从第一个 ## 开始到文档结尾的内容
        lines = content.split('\n')
        start_index = 0
        
        # 找到第一个 ## 标题的位置（跳过文档标题）
        for i, line in enumerate(lines):
            if line.startswith('## ') and i > 0:  # 跳过第一行的文档标题
                start_index = i
                break
        
        if start_index > 0:
            # 提取从第一个 ## 开始的所有内容
            wallpaper_content = '\n'.join(lines[start_index:])
            
            # 移除最后的说明文字（"本文档展示了..."这一段）
            if '---\n\n本文档展示了' in wallpaper_content:
                wallpaper_content = wallpaper_content.split('---\n\n本文档展示了')[0] + '---'
            elif '---\n\nThis document showcases' in wallpaper_content:
                wallpaper_content = wallpaper_content.split('---\n\nThis document showcases')[0] + '---'
            
            return wallpaper_content
        else:
            print(f"Warning: 无法找到 {wallpaper_file} 中的壁纸内容")
            return ""
            
    except FileNotFoundError:
        print(f"Warning: {wallpaper_file} 文件不存在")
        return ""
    except Exception as e:
        print(f"Warning: 读取 {wallpaper_file} 时出错: {e}")
        return ""

def generate_readme(lang: str):
    """生成README文档"""
    print(f"正在生成{'中文' if lang == 'cn' else '英文'}README文档...")
    
    # 获取基础内容
    base_content = get_base_readme_content(lang)
    
    # 获取所有国家
    countries = get_available_countries()
    if not countries:
        print("❌ 没有找到任何国家的数据文件")
        return
    
    # 生成支持的国家和地区部分（替换模板中的静态内容）
    supported_countries_section = generate_supported_countries_section(countries, lang)
    
    # 替换模板中的支持国家部分
    if lang == 'cn':
        # 查找并替换中文模板中的支持国家部分
        import re
        pattern = r'## 🌍 支持的国家和地区.*?(?=\n## |\n---|\Z)'
        base_content = re.sub(pattern, supported_countries_section.rstrip(), base_content, flags=re.DOTALL)
    else:
        # 查找并替换英文模板中的支持国家部分
        import re
        pattern = r'## 🌍 Supported Countries and Regions.*?(?=\n## |\n---|\Z)'
        base_content = re.sub(pattern, supported_countries_section.rstrip(), base_content, flags=re.DOTALL)
    
    # 生成各国链接部分
    country_links_section = generate_country_links_section(countries, lang)
    
    # 生成完整壁纸列表内容（包括今日壁纸、最近30天和按月导航）
    wallpaper_country = 'cn' if lang == 'cn' else 'us'
    wallpaper_list_section = get_wallpaper_list_content(wallpaper_country, lang)
    
    # 组合完整内容
    full_content = base_content + "\n\n" + country_links_section + "\n\n" + wallpaper_list_section
    
    # 写入文件
    filename = 'README.md' if lang == 'en' else 'README_CN.md'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    print(f"✅ 生成完成: {filename}")

def main():
    """主函数"""
    print("🚀 开始生成README文档...")
    
    # 生成英文README
    generate_readme('en')
    
    # 生成中文README
    generate_readme('cn')
    
    print("🎉 README文档生成完成！")

if __name__ == "__main__":
    main()