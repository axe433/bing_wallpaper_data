import requests
import json
import os
from datetime import datetime

# 和 bing_data.py 中相同的国家/地区列表
countries = {
    # 'us': 'en-US',
    # 'gb': 'en-GB',
    # 'de': 'de-DE',
    # 'fr': 'fr-FR',
    # 'it': 'it-IT',
    # 'es': 'es-ES',
    # 'pt': 'pt-PT',
    # 'pl': 'pl-PL',
    # 'ua': 'uk-UA',
    # 'nl': 'nl-NL',
    # 'se': 'sv-SE',
    # 'fi': 'fi-FI',
    # 'no': 'nb-NO',
    # 'dk': 'da-DK',
    # 'cz': 'cs-CZ',
    # 'gr': 'el-GR',
    # 'ru': 'ru-RU',
    # 'ca': 'en-CA',
    # 'au': 'en-AU',
    'cn': 'zh-CN',
    # 'hk': 'zh-HK',
    # 'tw': 'zh-TW',
    # 'sg': 'en-SG',
    # 'jp': 'ja-JP',
    # 'kr': 'ko-KR',
    # 'in': 'hi-IN',
    # 'id': 'id-ID',
    # 'th': 'th-TH',
    # 'vn': 'vi-VN',
    # 'my': 'ms-MY',
    # 'br': 'pt-BR',
    # 'ar': 'es-AR',
    # 'tr': 'tr-TR',
    # 'za': 'af-ZA'
}

def merge_images_with_update(old_images, new_images_data):
    """
    合并新旧数据。
    - 如果新数据是全新的，则添加。
    - 如果新数据已存在于旧数据中，则检查新数据中是否有 'MediaContent' 字段。
      如果有，则用它来更新旧数据中对应的记录。
    """
    # 使用字典以便通过日期快速查找和更新记录
    old_images_map = {img['startdate']: img for img in old_images}

    update_count = 0
    new_count = 0

    for new_image_info in new_images_data:
        startdate = new_image_info.get('startdate')
        if not startdate:
            continue

        # 检查新数据是否存在于旧数据中
        if startdate in old_images_map:
            old_image_record = old_images_map[startdate]

            # 核心逻辑：如果新记录有 MediaContent，则更新旧记录
            if 'MediaContent' in new_image_info:
                # 检查旧记录是否已经有这个字段，或者内容是否不同
                if 'MediaContent' not in old_image_record:
                    old_image_record['MediaContent'] = new_image_info['MediaContent']
                    update_count += 1
        else:
            # 如果是全新的记录，则添加到 map 中
            old_images_map[startdate] = new_image_info
            new_count += 1

    print(f"Updated {update_count} existing records. Added {new_count} new records.")

    # 将字典的值转换回列表
    old_images_merged = list(old_images_map.values())
    # 按日期倒序排序
    old_images_merged.sort(key=lambda x: datetime.strptime(x['enddate'], '%Y%m%d'), reverse=True)

    return old_images_merged


def process_local_files():
    """
    主函数，遍历所有国家，从本地读取文件，合并数据，并用合并后的正确数据修正目标文件。
    """
    # 定义修正的日期范围
    correction_start_date = "20250815"
    correction_end_date = "20250828"

    for country, lang in countries.items():
        print(f"Processing country: {country.upper()}")

        response_dir = f"response/{country}"
        if not os.path.isdir(response_dir):
            print(f"  Directory not found: {response_dir}, skipping.")
            continue

        try:
            # 1. 从 'data_image' 文件读取图片数据并去重
            images_info = []
            seen_startdates = set()
            for filename in os.listdir(response_dir):
                if 'data_image' in filename:
                    file_path = os.path.join(response_dir, filename)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        for image in data.get('images', []):
                            startdate = image.get('startdate')
                            if startdate and startdate not in seen_startdates:
                                images_info.append(image)
                                seen_startdates.add(startdate)

            # 2. 从 'data_description' 文件读取描述数据
            description_map = {}
            for filename in os.listdir(response_dir):
                if 'data_description' in filename:
                    file_path = os.path.join(response_dir, filename)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        for item in data.get('MediaContents', []):
                            ssd = item.get('Ssd')
                            if ssd and ssd not in description_map:
                                description_map[ssd] = item

            # 3. 将描述数据合并到图片数据中 (使用选中的代码逻辑)
            for image in images_info:
                startdate_key = image.get('enddate')
                if startdate_key:
                    desc_item = description_map.get(startdate_key)
                    if desc_item:
                        image['MediaContent'] = desc_item
            
            # 4. 读取、修正并写回目标文件
            target_file_path = f'./jsonc/{country}/bing.jsonc'
            if not os.path.exists(target_file_path):
                print(f"  Target file not found: {target_file_path}, skipping correction.")
                continue

            with open(target_file_path, 'r', encoding='utf-8') as f:
                target_data = json.load(f)

            # 将修正源数据转换为以 startdate 为键的字典，以便快速查找
            correct_data_map = {item['startdate']: item for item in images_info if 'startdate' in item}

            update_count = 0
            for item in target_data:
                item_startdate = item.get('startdate')
                if item_startdate and correction_start_date <= item_startdate <= correction_end_date:
                    correct_item = correct_data_map.get(item_startdate)
                    # 如果找到了对应的正确数据，并且其中包含 MediaContent
                    if correct_item and 'MediaContent' in correct_item:
                        # 只有当 MediaContent 不存在或内容不同时才更新
                        if item.get('MediaContent') != correct_item['MediaContent']:
                            item['MediaContent'] = correct_item['MediaContent']
                            update_count += 1
            
            if update_count > 0:
                with open(target_file_path, 'w', encoding='utf-8') as f:
                    json.dump(target_data, f, ensure_ascii=False, indent=4)
                print(f"  Successfully corrected {update_count} items in '{target_file_path}'.\n")
            else:
                print(f"  No items needed correction in '{target_file_path}'.\n")

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON for {country.upper()}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred for {country.upper()}: {e}")


if __name__ == "__main__":
    process_local_files()
