import requests
import json
import os
from datetime import datetime, timezone
import urllib.parse

print("Starts time: ", datetime.now(timezone.utc))
# 定义国家和语言代码列表
country_to_lang = {
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

# 确保所有目标文件夹存在
for country, lang in country_to_lang.items():
    directory = f'./jsonc/{country}'
    if not os.path.exists(directory):
        os.makedirs(directory)

#  date_field='enddate', unique_field='fullstartdate'
def merge_images(existing_images, new_images, date_field, unique_field=None):
    existing_dates = {image[date_field] for image in existing_images if date_field in image}
    if unique_field:
        # 创建一个集合来快速查找已存在的唯一标识
        existing_ids = {image[unique_field] for image in existing_images if unique_field in image}
    else:
        existing_ids = set()

    added_count = 0
    skipped_count = 0

    for image_info in new_images:
        # 只处理包含 fullstartdate 的数据
        if unique_field and unique_field in image_info:
            #  TODO 使用 fullstartdate 对比
            unique_id = image_info[unique_field]
            if unique_id not in existing_ids:
                # 如果不存在，添加新数据
                existing_images.append(image_info)
                existing_ids.add(unique_id)
                added_count += 1
                print(f"  ➕ 添加新数据: {unique_id}")
            else:
                # 如果已存在，完全跳过，保留旧数据不变
                skipped_count += 1
                print(f"  ⏭️  跳过已存在数据: {unique_id}")
        # 处理不包含 fullstartdate 的数据，仍然使用 date 进行判断
        elif image_info[date_field] not in existing_dates:
            #  TODO 使用 enddate 进行对比
            existing_images.append(image_info)
            existing_dates.add(image_info[date_field])
            added_count += 1
            print(f"  ➕ 添加新数据 (按日期): {image_info[date_field]}")
        else:
            skipped_count += 1
            print(f"  ⏭️  跳过已存在数据 (按日期): {image_info[date_field]}")

    # 按日期倒序排序
    existing_images.sort(key=lambda x: datetime.strptime(x[date_field], '%Y%m%d'), reverse=True)

    print(f"  📊 数据统计: 新增 {added_count} 条，跳过 {skipped_count} 条")
    return existing_images


# 遍历每种语言
for country, lang in country_to_lang.items():
    # 定义API URL，使用不同的语言代码
    api_url = f"https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=8&mkt={lang}"
    api_description = f"https://www.bing.com/hp/api/model?toWww=1&mkt={lang}"
    # api_url = f"https://www.bing.com/HPImageArchive.aspx?format=js&idx=8&n=8&mkt={lang}" # old
    # 语言不支持，会使用通用 ROW 数据
    if (lang == "hu-HU"): lang = "ROW"

    # 发起请求获取数据
    response = requests.get(api_url)
    response_description = requests.get(api_description)

    # Save the response data
    response_dir = f"response/{country}"
    os.makedirs(response_dir, exist_ok=True)

    # 获取当前日期并格式化
    current_date = datetime.now().strftime('%Y%m%d')

    with open(os.path.join(response_dir, f'{current_date}_data_image.json'), 'w', encoding='utf-8') as f:
        f.write(response.text)

    with open(os.path.join(response_dir, f'{current_date}_data_description.json'), 'w', encoding='utf-8') as f:
        f.write(response_description.text)
    
    data = response.json()
    data_description = response_description.json()

    # 提取所需数据并格式化
    images_info = []
    for image in data['images']:
        # image_info = {
        #     'startdate': datetime.strptime(image['startdate'], '%Y%m%d').strftime('%Y%m%d'),
        #     'fullstartdate': image['fullstartdate'],
        #     'enddate': datetime.strptime(image['enddate'], '%Y%m%d').strftime('%Y%m%d'),
        #     'url': image['url'],
        #     'urlbase': image['urlbase'],
        #     'copyright': image['copyright'],
        #     'copyrightlink': image['copyrightlink'],
        #     'title': image['title'],
        #     'quiz': image['quiz'],
        #     'hsh': image['hsh'],
        #     'drk': image['drk'],
        #     'top': image['top'],
        #     'bot': image['bot'],
        #     # 'tag': [name, id] # such as "tag": ["DugiOtokCroatia","EN-CA6561432536"]
        # }
        image_info = image
        images_info.append(image_info)
    
    for image2 in data_description['MediaContents']:
        fullstartdate = image2['Ssd'].replace('_', '')
        # description = image2['ImageContent']['Description']
        # 找到对应 fullstartdate 的 image_info，并添加 description
        for image_info in images_info:
            if image_info['fullstartdate'] == fullstartdate or image_info['startdate'] == fullstartdate:
                image_info['MediaContent'] = image2
                break  # 找到匹配项后跳出循环


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
    existing_images_info_current = read_json(file_path_current)

    # 过滤并合并新数据
    existing_images_info_current = merge_images(existing_images_info_current, images_info, date_field='enddate', unique_field='fullstartdate')

    # 将更新后的数据写回到本地JSON文件
    write_json(file_path_current, existing_images_info_current)
    print(f"Bing Daily Image data has been saved to '{file_path_current}'")

print("Bing Image of the Day data is saved for all languages.")
print("Ends time: ", datetime.now(timezone.utc))
