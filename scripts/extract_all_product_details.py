import glob
import os
import re
import json

products_data = {}

files = glob.glob(r'public/assets/labels/*_label_print.html')
for f in sorted(files):
    name = os.path.basename(f)
    prod_id = name.replace('_label_print.html', '')
    with open(f, encoding='utf-8') as fp:
        c = fp.read()
    
    # Title & English
    title_m = re.search(r'<h1[^>]*>(.*?)</h1>', c)
    en_m = re.search(r'<h2[^>]*>(.*?)</h2>', c)
    sub_m = re.search(r'<p[^>]*class="[^"]*text-gray-400[^"]*"[^>]*>(.*?)</p>', c)
    
    # Effects (li inside ul in 핵심 효능)
    eff_section = re.search(r'핵심 효능.*?<ul[^>]*>(.*?)</ul>', c, re.S)
    effects = []
    if eff_section:
        effects = [re.sub(r'<[^>]+>', '', x).strip() for x in re.findall(r'<li[^>]*>(.*?)</li>', eff_section.group(1), re.S)]
    
    # Ingredients list
    ing_section = re.search(r'주요 성분 데이터.*?<ul[^>]*>(.*?)</ul>', c, re.S)
    ingredients = []
    if ing_section:
        for li in re.findall(r'<li[^>]*>(.*?)</li>', ing_section.group(1), re.S):
            divs = re.findall(r'<div[^>]*>(.*?)</div>', li, re.S)
            if len(divs) >= 2:
                k = re.sub(r'<[^>]+>', '', divs[0]).strip()
                v = re.sub(r'<[^>]+>', '', divs[1]).strip()
                ingredients.append((k, v))
    
    # Legal notices
    reg_no = ""
    reg_m = re.search(r'사료 성분등록번호.*?<div[^>]*>(.*?)</div>', c, re.S)
    if reg_m: reg_no = re.sub(r'<[^>]+>', '', reg_m.group(1)).strip()
    
    feed_type = ""
    type_m = re.search(r'사료의 종류 및 명칭.*?<div[^>]*>(.*?)</div>', c, re.S)
    if type_m: feed_type = re.sub(r'<[^>]+>', '', type_m.group(1)).strip()
    
    reg_ing = ""
    reg_ing_m = re.search(r'등록성분량.*?<div[^>]*>(.*?)</div>', c, re.S)
    if reg_ing_m: reg_ing = re.sub(r'<[^>]+>', '', reg_ing_m.group(1)).strip()
    
    raw_mat = ""
    raw_m = re.search(r'사용한 원료의 명칭.*?<div[^>]*>(.*?)</div>', c, re.S)
    if raw_m: raw_mat = re.sub(r'<[^>]+>', '', raw_m.group(1)).strip()
    
    target = "반려견 · 반려묘"
    target_m = re.search(r'대상축종.*?<div[^>]*>(.*?)</div>', c, re.S)
    if target_m: target = re.sub(r'<[^>]+>', '', target_m.group(1)).strip()
    
    dosage = ""
    dose_m = re.search(r'용법 및 용량.*?<div[^>]*>(.*?)</div>', c, re.S)
    if dose_m: dosage = re.sub(r'<[^>]+>', '', dose_m.group(1)).strip()
    
    products_data[prod_id] = {
        "prod_id": prod_id,
        "title": title_m.group(1).strip() if title_m else "",
        "name_en": en_m.group(1).strip() if en_m else "",
        "sub_desc": sub_m.group(1).strip() if sub_m else "",
        "effects": effects,
        "ingredients": ingredients,
        "reg_no": reg_no,
        "feed_type": feed_type,
        "reg_ing": reg_ing,
        "raw_mat": raw_mat,
        "target": target,
        "dosage": dosage
    }

with open(r'scripts/extracted_products.json', 'w', encoding='utf-8') as fp:
    json.dump(products_data, fp, ensure_ascii=False, indent=2)

print("Extracted", len(products_data), "products successfully.")
