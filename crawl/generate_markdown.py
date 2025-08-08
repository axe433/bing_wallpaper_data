#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
from datetime import datetime, timedelta
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

def load_messages(country: str) -> Dict[str, Any]:
    """加载国际化文案"""
    file_path = f'./messages/{country}.json'
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Warning: {file_path} not found, using default messages")
        return {
            "home": {
                "page_title": "Bing Wallpaper Archive - Daily Desktop Backgrounds",
                "today_wallpaper": "Today's Wallpaper",
                "archive_title": "Wallpaper Archive by Year"
            }
        }

def get_image_url(urlbase: str) -> str:
    """生成高质量图片URL"""
    return f"https://www.bing.com{urlbase}_UHD.jpg&pid=hp&w=2560"

def get_detail_url(country: str, date: str) -> str:
    """生成详情页面URL"""
    return f"https://bing.codexun.com/{country}/detail/{date}"

def get_archive_url(country: str, year_month: str) -> str:
    """生成归档页面URL"""
    return f"https://bing.codexun.com/{country}/archive/{year_month}"

def format_date(date_str: str) -> str:
    """格式化日期为 YYYY-MM-DD"""
    if len(date_str) == 8:
        return f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
    return date_str

def get_recent_30_days_wallpapers(wallpapers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """获取最近30天的壁纸"""
    if not wallpapers:
        return []
    
    # 获取最新壁纸的日期
    latest_date_str = wallpapers[0]['enddate']
    latest_date = datetime.strptime(latest_date_str, '%Y%m%d')
    
    # 计算30天前的日期（不包含30天前的那一天）
    thirty_days_ago = latest_date - timedelta(days=29)
    
    # 筛选最近30天的壁纸
    recent_wallpapers = []
    for wallpaper in wallpapers:
        wallpaper_date = datetime.strptime(wallpaper['enddate'], '%Y%m%d')
        if wallpaper_date >= thirty_days_ago:
            recent_wallpapers.append(wallpaper)
    
    return recent_wallpapers

def get_available_months(wallpapers: List[Dict[str, Any]]) -> Dict[str, List[str]]:
    """获取所有可用的年月数据"""
    year_months = {}
    
    for wallpaper in wallpapers:
        date = wallpaper['enddate']
        year = date[:4]
        year_month = date[:6]
        
        if year not in year_months:
            year_months[year] = []
        
        if year_month not in year_months[year]:
            year_months[year].append(year_month)
    
    # 对每年的月份进行倒序排序
    for year in year_months:
        year_months[year].sort(reverse=True)
    
    return year_months

def generate_wallpaper_table(wallpapers: List[Dict[str, Any]], country: str) -> str:
    """生成壁纸表格的markdown"""
    if not wallpapers:
        return ""
    
    # 按每行3个分组
    rows = []
    for i in range(0, len(wallpapers), 3):
        row_wallpapers = wallpapers[i:i+3]
        rows.append(row_wallpapers)
    
    markdown = ""
    
    # 添加表头（隐藏的表头，用于分隔符）
    markdown += "| | | |\n"
    markdown += "|:---:|:---:|:---:|\n"
    
    for row_index, row in enumerate(rows):
        # 图片行
        image_row = "| "
        info_row = "| "
        
        for i in range(3):  # 固定3列
            if i < len(row) and row[i]:
                wallpaper = row[i]
                title = wallpaper.get('title', 'Bing Wallpaper')
                image_url = get_image_url(wallpaper['urlbase'])
                detail_url = get_detail_url(country, wallpaper['enddate'])
                
                # 图片
                image_row += f"[![{title}]({image_url})]({detail_url}) | "
                
                # 信息
                copyright_text = wallpaper.get('copyright', '')
                # 提取版权信息中的描述部分（去掉版权标识）
                if '(' in copyright_text:
                    description = copyright_text.split('(')[0].strip()
                else:
                    description = copyright_text
                
                formatted_date = format_date(wallpaper['enddate'])
                info_row += f"**[{title}]({detail_url})**<br>{description}<br>*{formatted_date}* | "
            else:
                # 空列
                image_row += " | "
                info_row += " | "
        
        markdown += image_row + "\n"
        markdown += info_row + "\n"
    
    return markdown

def generate_archive_navigation(year_months: Dict[str, List[str]], country: str, current_month: str) -> str:
    """生成归档导航的markdown"""
    markdown = ""
    
    # 按年份倒序排列
    sorted_years = sorted(year_months.keys(), reverse=True)
    
    for year in sorted_years:
        markdown += f"### {year}\n"
        markdown += '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 6px; margin: 12px 0;">\n'
        
        for year_month in year_months[year]:
            archive_url = get_archive_url(country, year_month)
            
            # 高亮当前月份
            if year_month == current_month:
                style = 'padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f3f4f6; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease; font-weight: 500;'
            else:
                style = 'padding: 6px 12px; font-size: 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); background-color: #f9fafb; color: #374151; text-decoration: none; text-align: center; transition: background-color 0.2s ease;'
            
            markdown += f'<a href="{archive_url}" style="{style}">{year_month}</a>\n'
        
        markdown += '</div>\n\n'
    
    return markdown

def generate_markdown_document(country: str) -> str:
    """生成完整的markdown文档"""
    # 加载数据
    wallpapers = load_wallpaper_data(country)
    messages = load_messages(country)
    
    if not wallpapers:
        print(f"No wallpaper data found for {country}")
        return ""
    
    # 获取最新壁纸
    latest_wallpaper = wallpapers[0]
    
    # 获取最近30天壁纸
    recent_30_days_wallpapers = get_recent_30_days_wallpapers(wallpapers)
    current_month = latest_wallpaper['enddate'][:6]
    
    # 获取可用月份
    year_months = get_available_months(wallpapers)
    
    # 从国际化文件获取国家名称
    country_name = messages['home'].get('country_name', country.upper())
    
    # 获取最新壁纸信息
    latest_title = latest_wallpaper.get('title', 'Today\'s Wallpaper')
    latest_image_url = get_image_url(latest_wallpaper['urlbase'])
    latest_detail_url = get_detail_url(country, latest_wallpaper['enddate'])
    latest_description = ""
    latest_copyright = latest_wallpaper.get('copyright', '')
    
    # 尝试从MediaContent获取描述
    if 'MediaContent' in latest_wallpaper and 'ImageContent' in latest_wallpaper['MediaContent']:
        latest_description = latest_wallpaper['MediaContent']['ImageContent'].get('Description', '')
    
    # 如果没有描述，从版权信息提取
    if not latest_description and '(' in latest_copyright:
        latest_description = latest_copyright.split('(')[0].strip()
    
    # 提取版权信息
    if '©' in latest_copyright:
        copyright_info = latest_copyright.split('©')[1].strip() if '©' in latest_copyright else latest_copyright
        if ')' in copyright_info:
            copyright_info = copyright_info.replace(')', '')
    else:
        copyright_info = latest_copyright
    
    # 从国际化文件获取最近30天标题
    recent_30_days_display = messages['home'].get('recent_30_days', 'Recent 30 Days')
    
    markdown = f"""# Bing Wallpaper Archive - {country_name}

## {messages['home'].get('today_wallpaper', 'Today\'s Wallpaper')}

[![{latest_title}]({latest_image_url})]({latest_detail_url})

**{latest_title}**

{latest_description}

*© {copyright_info} (Bing {country_name})*

---

## {recent_30_days_display}

{generate_wallpaper_table(recent_30_days_wallpapers, country)}

---

## {messages['home'].get('archive_title', 'Wallpaper Archive by Year')}

{generate_archive_navigation(year_months, country, current_month)}

---

{messages['home'].get('footer_description', 'This document showcases the beautiful Bing wallpaper collection from {country_name}. All wallpapers are available in Ultra HD, 2K, and 1080p resolutions. Click on any wallpaper to view details and download options.').format(country_name=country_name)}
"""
    
    return markdown

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

def main():
    """主函数"""
    # 确保markdown目录存在
    markdown_dir = "./markdown"
    if not os.path.exists(markdown_dir):
        os.makedirs(markdown_dir)
        print(f"创建markdown目录: {markdown_dir}")
    
    # 自动获取所有可用的国家列表
    countries = get_available_countries()
    if not countries:
        print("❌ 没有找到任何国家的数据文件")
        return
    
    print(f"🌍 找到 {len(countries)} 个国家: {', '.join(countries)}")
    
    for country in countries:
        print(f"Generating markdown for {country}...")
        
        markdown_content = generate_markdown_document(country)
        
        if markdown_content:
            # 生成文件名（输出到markdown目录，国家代码放到最后）
            output_file = f"{markdown_dir}/wallpaper-list-{country}.md"
            
            # 写入文件
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            print(f"Generated {output_file}")
        else:
            print(f"Failed to generate markdown for {country}")

if __name__ == "__main__":
    main()