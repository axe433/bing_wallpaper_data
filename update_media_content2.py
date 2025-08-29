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


def fetch_and_update():
    """
    主函数，遍历所有国家，获取数据并执行更新。
    """
    for country, lang in countries.items():
        print(f"Processing country: {country.upper()}")

        # 定义 API URL
        api_url = f"https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=8&mkt={lang}"
        # api_description = f"https://www.bing.com/hp/api/v1/imagegallery?format=json&mkt={lang}"
        api_description = f"https://www.bing.com/hp/api/model?toWww=1&mkt={lang}"

        try:
            # 获取数据
            response = requests.get(api_url)
            response.raise_for_status()
            response_description = requests.get(api_description)
            response_description.raise_for_status()

            images_data = response.json()
            description_data = response_description.json()

            # 提取需要合并的数据 (与 bing_data.py 第174行逻辑相同)
            images_info = images_data.get('images', [])
            description_map = {item['Ssd']: item for item in description_data.get('MediaContents', [])}

            # 将描述数据合并到图片数据中
            for image in images_info:
                desc_item = description_map.get(image['startdate'])
                if desc_item:
                    image['MediaContent'] = desc_item


            # 定义与语言代码相关的文件路径
            file_path_current = f'./jsonc/{country}/bing.jsonc'

            # 函数读写数据
            def read_json(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        return json.load(file)
                except FileNotFoundError:
                    return []

            def write_json(file_path, data):
                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)


            # 读取现有数据
            old_data = read_json(file_path_current)

            # 执行新的合并逻辑
            merged_data = merge_images_with_update(old_data, images_info)

            # 写回文件
            # 将更新后的数据写回到本地JSON文件
            write_json(file_path_current, merged_data)

            print(f"Successfully updated data for {country.upper()}.\n")

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for {country.upper()}: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON for {country.upper()}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred for {country.upper()}: {e}")


if __name__ == "__main__":
    fetch_and_update()
