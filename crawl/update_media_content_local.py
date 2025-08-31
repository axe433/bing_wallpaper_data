import requests
import json
import os
from datetime import datetime

# 和 bing_data.py 中相同的国家/地区列表
countries = {
    'us': 'en-US',
    'gb': 'en-GB',
    'de': 'de-DE',
    'fr': 'fr-FR',
    'it': 'it-IT',
    'es': 'es-ES',
    'pt': 'pt-PT',
    'pl': 'pl-PL',
    'ua': 'uk-UA',
    'nl': 'nl-NL',
    'se': 'sv-SE',
    'fi': 'fi-FI',
    'no': 'nb-NO',
    'dk': 'da-DK',
    'cz': 'cs-CZ',
    'gr': 'el-GR',
    'ru': 'ru-RU',
    'ca': 'en-CA',
    'au': 'en-AU',
    'cn': 'zh-CN',
    'hk': 'zh-HK',
    'tw': 'zh-TW',
    'sg': 'en-SG',
    'jp': 'ja-JP',
    'kr': 'ko-KR',
    'in': 'hi-IN',
    'id': 'id-ID',
    'th': 'th-TH',
    'vn': 'vi-VN',
    'my': 'ms-MY',
    'br': 'pt-BR',
    'ar': 'es-AR',
    'tr': 'tr-TR',
    'za': 'af-ZA'
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
    correction_start_date = "20250829"
    correction_end_date = "20250830"

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
            descriptions_info = []
            seen_titles = set()
            for filename in os.listdir(response_dir):
                if 'data_description' in filename:
                    file_path = os.path.join(response_dir, filename)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        for item in data.get('MediaContents', []):
                            title = item.get('ImageContent').get('Title')
                            if title and title not in seen_titles:
                                descriptions_info.append(item)
                                seen_titles.add(title)

            # 3. 将描述数据合并到图片数据中 (使用选中的代码逻辑)
            for image in images_info:
                copyright = image.get('copyright')
                if copyright:
                    for desc_item in descriptions_info:
                        if desc_item.get('ImageContent').get('Title') in copyright and desc_item.get('ImageContent').get('Copyright') in copyright:
                            image['MediaContent'] = desc_item
                            break

            # 4. 读取、修正并写回目标文件
            target_file_path = f'./jsonc/{country}/bing.jsonc'
            if not os.path.exists(target_file_path):
                print(f"  Target file not found: {target_file_path}, skipping correction.")
                continue

            with open(target_file_path, 'r', encoding='utf-8') as f:
                target_data = json.load(f)

            update_count = 0
            # 将修正源数据转换为以 startdate 为键的字典，以便快速查找 [将新数据中新条目合并到target 数据中]
            correct_target_map = {item['startdate']: item for item in target_data if 'startdate' in item}
            for item in images_info:
                item_startdate = item.get('startdate')
                if item_startdate and correction_start_date <= item_startdate <= correction_end_date:
                    correct_item = correct_target_map.get(item_startdate)
                    if not correct_item: # 如果没有找到对应的正确数据，说明是新数据，则添加
                        target_data.append(item)
                        update_count += 1
                    elif correct_item.get('MediaContent') != item.get('MediaContent'):
                        correct_item['MediaContent'] = item.get('MediaContent')
                        update_count += 1

            if update_count > 0:
                with open(target_file_path, 'w', encoding='utf-8') as f:
                    # 按日期倒序排序
                    target_data.sort(key=lambda x: datetime.strptime(x['startdate'], '%Y%m%d'), reverse=True)
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
