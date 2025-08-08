#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import hashlib
from datetime import datetime, timezone
from typing import List, Dict, Any, Set
from collections import OrderedDict

def calculate_file_md5(file_path: str) -> str:
    """计算文件的MD5哈希值"""
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        print(f"  ❌ 计算MD5失败 {file_path}: {str(e)}")
        return ""

def load_jsonc_file(file_path: str) -> List[Dict[str, Any]]:
    """加载JSONC文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"读取文件失败 {file_path}: {str(e)}")
        return []

def save_jsonc_file(file_path: str, data: List[Dict[str, Any]]) -> bool:
    """保存JSONC文件"""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print(f"保存文件失败 {file_path}: {str(e)}")
        return False

def update_md5_field_in_item(item: Dict[str, Any], new_md5_value: str) -> Dict[str, Any]:
    """更新数据项中的md5字段值，保持字段顺序"""
    # 创建有序字典来保持字段顺序
    ordered_item = OrderedDict()
    
    for key, value in item.items():
        if key == 'md5':
            ordered_item[key] = new_md5_value
        else:
            ordered_item[key] = value
    
    # 如果没有md5字段，在hsh字段前添加
    if 'md5' not in item:
        new_ordered_item = OrderedDict()
        for key, value in ordered_item.items():
            if key == 'hsh':
                new_ordered_item['md5'] = new_md5_value
            new_ordered_item[key] = value
        # 如果没有hsh字段，在最后添加md5字段
        if 'hsh' not in item:
            new_ordered_item['md5'] = new_md5_value
        ordered_item = new_ordered_item
    
    return dict(ordered_item)

def process_country_images(country: str, images_dir: str, processed_md5s: Set[str], global_md5_mapping: Dict[str, str]) -> tuple:
    """处理指定国家的图片去重"""
    jsonc_file = f"../jsonc/{country}/bing.jsonc"
    
    if not os.path.exists(jsonc_file):
        print(f"  文件不存在: {jsonc_file}")
        return 0, 0, 0, 0
    
    print(f"\n📁 开始处理 {country.upper()} 的图片去重...")
    
    # 加载数据
    wallpapers = load_jsonc_file(jsonc_file)
    if not wallpapers:
        print(f"  没有找到 {country} 的壁纸数据")
        return 0, 0, 0, 0
    
    processed_count = 0
    renamed_count = 0
    deleted_count = 0
    updated_count = 0
    
    for i, item in enumerate(wallpapers):
        if 'md5' not in item:
            print(f"  跳过无md5字段的项目: {i}")
            continue
        
        old_md5 = item['md5']
        old_image_path = os.path.join(images_dir, f"{old_md5}.jpg")
        
        # 检查图片文件是否存在
        if not os.path.exists(old_image_path):
            # 检查是否已经被重命名过
            if old_md5 in global_md5_mapping:
                real_md5 = global_md5_mapping[old_md5]
                print(f"  🔄 使用已知映射: {old_md5} -> {real_md5}")
            else:
                print(f"  ⚠️  图片文件不存在: {old_md5}.jpg")
                continue
        else:
            # 计算图片文件的真实MD5值
            real_md5 = calculate_file_md5(old_image_path)
            if not real_md5:
                continue
            
            # 记录映射关系
            global_md5_mapping[old_md5] = real_md5
            
            new_image_path = os.path.join(images_dir, f"{real_md5}.jpg")
            
            # 如果真实MD5与当前文件名不同，需要重命名或删除
            if real_md5 != old_md5:
                if real_md5 in processed_md5s or os.path.exists(new_image_path):
                    # 图片重复，删除当前图片
                    try:
                        os.remove(old_image_path)
                        print(f"  🗑️  删除重复图片: {old_md5}.jpg -> {real_md5}.jpg")
                        deleted_count += 1
                    except Exception as e:
                        print(f"  ❌ 删除文件失败 {old_image_path}: {str(e)}")
                        continue
                else:
                    # 重命名图片文件
                    try:
                        os.rename(old_image_path, new_image_path)
                        print(f"  📝 重命名图片: {old_md5}.jpg -> {real_md5}.jpg")
                        renamed_count += 1
                    except Exception as e:
                        print(f"  ❌ 重命名文件失败 {old_image_path}: {str(e)}")
                        continue
            else:
                print(f"  ✅ 图片MD5正确: {real_md5}.jpg")
            
            processed_md5s.add(real_md5)
        
        # 更新JSON数据中的md5字段
        if item['md5'] != real_md5:
            wallpapers[i] = update_md5_field_in_item(item, real_md5)
            updated_count += 1
            print(f"  🔄 更新MD5字段: {old_md5} -> {real_md5}")
        
        processed_count += 1
    
    # 保存更新后的数据
    if save_jsonc_file(jsonc_file, wallpapers):
        print(f"  ✓ 已更新 {country.upper()} 的JSON文件")
    else:
        print(f"  ✗ 保存 {country.upper()} 的JSON文件失败")
    
    print(f"  📊 {country.upper()} 处理完成: 处理 {processed_count} 张图片，重命名 {renamed_count} 张，删除 {deleted_count} 张，更新 {updated_count} 条记录")
    return processed_count, renamed_count, deleted_count, updated_count

def get_all_countries() -> List[str]:
    """获取所有国家目录"""
    jsonc_dir = "../jsonc"
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

def get_initial_image_count(images_dir: str) -> int:
    """获取初始图片数量"""
    if not os.path.exists(images_dir):
        return 0
    return len([f for f in os.listdir(images_dir) if f.endswith('.jpg')])

def verify_all_countries_updated(countries: List[str]) -> tuple:
    """验证所有国家的JSON文件是否都已更新"""
    total_items = 0
    updated_items = 0
    
    print("\n🔍 验证所有国家的JSON文件更新状态...")
    
    for country in countries:
        jsonc_file = f"../jsonc/{country}/bing.jsonc"
        wallpapers = load_jsonc_file(jsonc_file)
        
        country_total = 0
        country_updated = 0
        
        for item in wallpapers:
            if 'md5' in item:
                country_total += 1
                total_items += 1
                
                # 检查对应的图片文件是否存在
                md5_value = item['md5']
                image_path = f"../images/{md5_value}.jpg"
                if os.path.exists(image_path):
                    country_updated += 1
                    updated_items += 1
        
        if country_total > 0:
            success_rate = (country_updated / country_total) * 100
            print(f"  {country.upper()}: {country_updated}/{country_total} ({success_rate:.1f}%)")
    
    overall_success_rate = (updated_items / total_items) * 100 if total_items > 0 else 0
    print(f"\n📊 总体验证结果: {updated_items}/{total_items} ({overall_success_rate:.1f}%)")
    
    return total_items, updated_items

def main():
    """主函数"""
    print("🔄 Bing壁纸完整去重工具")
    print("=" * 60)
    print(f"⏰ 开始时间: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")
    
    # 确保images目录存在
    images_dir = "../images"
    if not os.path.exists(images_dir):
        print("❌ images目录不存在")
        return
    
    # 获取初始图片数量
    initial_count = get_initial_image_count(images_dir)
    print(f"📂 初始图片数量: {initial_count}")
    
    # 获取所有国家
    countries = get_all_countries()
    if not countries:
        print("❌ 没有找到任何国家的数据文件")
        return
    
    print(f"🌍 找到 {len(countries)} 个国家: {', '.join(countries)}")
    
    total_processed = 0
    total_renamed = 0
    total_deleted = 0
    total_updated = 0
    success_countries = []
    failed_countries = []
    processed_md5s = set()  # 用于跟踪已处理的MD5值，避免重复
    global_md5_mapping = {}  # 全局MD5映射，用于处理已重命名的文件
    
    # 处理每个国家的数据
    for country in countries:
        try:
            processed, renamed, deleted, updated = process_country_images(
                country, images_dir, processed_md5s, global_md5_mapping
            )
            total_processed += processed
            total_renamed += renamed
            total_deleted += deleted
            total_updated += updated
            success_countries.append(country)
        except Exception as e:
            print(f"❌ 处理 {country.upper()} 时出错: {str(e)}")
            failed_countries.append(country)
            continue
    
    # 获取最终图片数量
    final_count = get_initial_image_count(images_dir)
    saved_space = initial_count - final_count
    
    # 验证所有国家的更新状态
    total_items, updated_items = verify_all_countries_updated(countries)
    
    print("\n" + "=" * 60)
    print("📈 完整图片去重完成!")
    print(f"✅ 成功处理: {len(success_countries)} 个国家")
    if failed_countries:
        print(f"❌ 处理失败: {len(failed_countries)} 个国家 ({', '.join(failed_countries)})")
    print(f"🖼️  总共处理: {total_processed} 张图片")
    print(f"📝 重命名图片: {total_renamed} 张")
    print(f"🗑️  删除重复: {total_deleted} 张")
    print(f"🔄 更新记录: {total_updated} 条")
    print(f"📂 初始图片: {initial_count} 张")
    print(f"📂 最终图片: {final_count} 张")
    print(f"💾 节省空间: {saved_space} 张图片")
    print(f"🎯 验证结果: {updated_items}/{total_items} 条记录已正确更新")
    print(f"⏰ 结束时间: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")
    
    if saved_space > 0:
        print(f"🎉 成功去除了 {saved_space} 张重复图片!")
    
    if updated_items == total_items:
        print("✅ 所有国家的JSON文件都已正确更新!")
    else:
        missing_items = total_items - updated_items
        print(f"⚠️  还有 {missing_items} 条记录需要处理")

if __name__ == "__main__":
    main()