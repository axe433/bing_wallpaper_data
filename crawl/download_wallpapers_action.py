#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bing壁纸下载脚本 - GitHub Actions版本
专门为GitHub Actions环境优化的壁纸下载工具
"""

import json
import os
import hashlib
import urllib.request
import urllib.error
import re
from datetime import datetime, timezone
from typing import List, Dict, Any
import time
from collections import OrderedDict

def get_file_md5(file_path: str) -> str:
    """计算文件的MD5哈希值"""
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        print(f"  ✗ 计算MD5失败: {str(e)}")
        return ""

def build_download_url(urlbase: str) -> str:
    """根据urlbase构建下载URL"""
    return f"https://www.bing.com{urlbase}_UHD.jpg"

def download_image(url: str, file_path: str) -> bool:
    """下载图片到指定路径"""
    try:
        print(f"  正在下载: {os.path.basename(file_path)}")
        
        # 创建请求对象，添加User-Agent头
        req = urllib.request.Request(
            url,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
        )
        
        with urllib.request.urlopen(req, timeout=30) as response:
            with open(file_path, 'wb') as f:
                f.write(response.read())
        
        print(f"  ✓ 下载成功: {os.path.basename(file_path)}")
        return True
        
    except Exception as e:
        print(f"  ✗ 下载失败: {str(e)}")
        return False

def load_jsonc_file(file_path: str) -> List[Dict[str, Any]]:
    """加载JSONC文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"读取文件失败 {file_path}: {str(e)}")
        return []

def save_jsonc_file(file_path: str, data: List[Dict[str, Any]]) -> bool:
    """保存JSONC文件，保持字段顺序"""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print(f"保存文件失败 {file_path}: {str(e)}")
        return False

def add_md5_field_to_item(item: Dict[str, Any], md5_value: str) -> Dict[str, Any]:
    """为数据项添加md5字段，放在hsh字段上面"""
    # 创建有序字典来保持字段顺序
    ordered_item = OrderedDict()
    
    for key, value in item.items():
        if key == 'hsh':
            # 在hsh字段前插入md5字段
            ordered_item['md5'] = md5_value
        ordered_item[key] = value
    
    # 如果没有hsh字段，在最后添加md5字段
    if 'hsh' not in item:
        ordered_item['md5'] = md5_value
    
    return dict(ordered_item)

def process_country_wallpapers(country: str, images_dir: str) -> tuple:
    """处理指定国家的壁纸数据"""
    jsonc_file = f"jsonc/{country}/bing.jsonc"
    
    if not os.path.exists(jsonc_file):
        print(f"  文件不存在: {jsonc_file}")
        return 0, 0
    
    print(f"\n📁 开始处理 {country.upper()} 的壁纸数据...")
    
    # 加载数据
    wallpapers = load_jsonc_file(jsonc_file)
    if not wallpapers:
        print(f"  没有找到 {country} 的壁纸数据")
        return 0, 0
    
    downloaded_count = 0
    updated_count = 0
    
    for i, item in enumerate(wallpapers):
        if 'urlbase' not in item:
            print(f"  跳过无urlbase的项目: {i}")
            continue
        
        # 如果已经有md5字段，说明已经处理过，跳过
        if 'md5' in item and item['md5']:
            print(f"  ⏭️  已有md5字段，跳过: {item.get('startdate', 'unknown')}")
            continue
        
        urlbase = item['urlbase']
        
        # 构建下载URL
        download_url = build_download_url(urlbase)
        
        # 创建临时文件名
        temp_filename = f"temp_{int(time.time())}_{i}.jpg"
        temp_path = os.path.join(images_dir, temp_filename)
        
        # 下载图片
        if not download_image(download_url, temp_path):
            print(f"  下载失败，跳过: {download_url}")
            continue
        
        # 计算下载图片的MD5
        file_md5 = get_file_md5(temp_path)
        if not file_md5:
            print(f"  计算MD5失败，删除临时文件")
            if os.path.exists(temp_path):
                os.remove(temp_path)
            continue
        
        # 使用MD5重命名文件
        final_filename = f"{file_md5}.jpg"
        final_path = os.path.join(images_dir, final_filename)
        
        # 检查是否已存在相同MD5的文件
        if os.path.exists(final_path):
            print(f"  🔄 发现重复图片，删除: {final_filename}")
            os.remove(temp_path)
        else:
            # 重命名文件
            os.rename(temp_path, final_path)
            print(f"  ✅ 保存图片: {final_filename}")
            downloaded_count += 1
        
        # 更新JSON数据，添加md5字段
        wallpapers[i] = add_md5_field_to_item(item, file_md5)
        updated_count += 1
        
        # 添加短暂延迟，避免请求过于频繁
        time.sleep(0.5)
    
    # 保存更新后的数据
    if updated_count > 0:
        if save_jsonc_file(jsonc_file, wallpapers):
            print(f"  ✓ 已更新 {country.upper()} 的JSON文件，添加了 {updated_count} 个md5字段")
        else:
            print(f"  ✗ 保存 {country.upper()} 的JSON文件失败")
    
    print(f"  📊 {country.upper()} 处理完成: 下载 {downloaded_count} 张图片，更新 {updated_count} 条记录")
    return downloaded_count, updated_count

def get_all_countries() -> List[str]:
    """获取所有国家目录"""
    jsonc_dir = "jsonc"
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
    print("🎨 Bing壁纸批量下载工具 - GitHub Actions版")
    print("=" * 60)
    print(f"⏰ 开始时间: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")
    
    # 确保images目录存在
    images_dir = "images"
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)
        print(f"📁 创建images目录: {images_dir}")
    
    # 获取所有国家
    countries = get_all_countries()
    if not countries:
        print("❌ 没有找到任何国家的数据文件")
        return
    
    print(f"🌍 找到 {len(countries)} 个国家: {', '.join(countries)}")
    
    total_downloaded = 0
    total_updated = 0
    success_countries = []
    failed_countries = []
    
    # 处理每个国家的数据
    for country in countries:
        try:
            downloaded, updated = process_country_wallpapers(country, images_dir)
            total_downloaded += downloaded
            total_updated += updated
            success_countries.append(country)
        except Exception as e:
            print(f"❌ 处理 {country.upper()} 时出错: {str(e)}")
            failed_countries.append(country)
            continue
    
    print("\n" + "=" * 60)
    print("📈 批量处理完成!")
    print(f"✅ 成功处理: {len(success_countries)} 个国家")
    if failed_countries:
        print(f"❌ 处理失败: {len(failed_countries)} 个国家 ({', '.join(failed_countries)})")
    print(f"🖼️  总共下载: {total_downloaded} 张壁纸")
    print(f"📝 总共更新: {total_updated} 条记录")
    print(f"⏰ 结束时间: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")
    
    # 显示images目录统计
    if os.path.exists(images_dir):
        image_files = [f for f in os.listdir(images_dir) if f.endswith('.jpg')]
        print(f"📂 images目录现有: {len(image_files)} 张图片")

if __name__ == "__main__":
    main()