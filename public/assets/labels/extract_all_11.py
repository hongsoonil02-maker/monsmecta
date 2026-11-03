import glob
import os
import re

files = [
    '01_monsmecta_original_label_claude.html',
    '02_monsmecta_hepamax_label_claude.html',
    '03_monsmecta_renal_label_claude.html',
    '04_monsmecta_cancercare_label_claude.html',
    '05_monsmecta_coldzero_label_claude.html',
    '06_monsmecta_skincare_label_claude.html',
    '07_monsmecta_heartcare_label_claude.html',
    '08_monsmecta_jointcare_label_claude.html',
    '09_monsmecta_powerase_label_claude.html',
    '10_monsmecta_probiotics_label_claude.html',
    '11_monsmecta_vitaplus_label_claude.html',
]

base_dir = r'C:\Users\master\monsmecta_landing\public\assets\labels'

for fname in files:
    fpath = os.path.join(base_dir, fname)
    if not os.path.exists(fpath):
        print(f"Missing: {fname}")
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Extract CSS root variables
    root_match = re.search(r':root\s*\{([^}]+)\}', html)
    root_css = root_match.group(1) if root_match else ''
    deep_color = re.search(r'--deep:\s*([^;]+);', root_css)
    emerald_color = re.search(r'--emerald:\s*([^;]+);', root_css)
    lime_color = re.search(r'--lime:\s*([^;]+);', root_css)
    mint_color = re.search(r'--mint:\s*([^;]+);', root_css)
    
    # Extract title, en, tagline
    tagline_match = re.search(r'<div class="tagline">(.*?)</div>', html, re.DOTALL)
    title_match = re.search(r'<div class="title">(.*?)</div>', html, re.DOTALL)
    en_match = re.search(r'<div class="en">(.*?)</div>', html, re.DOTALL)
    
    # Extract effects
    effects = re.findall(r'<li><span class="ck"></span>\s*(.*?)\s*</li>', html, re.DOTALL)
    
    # Extract ingredients (ing)
    ing_title = re.search(r'<h3>(.*?)</h3>', html)
    ing_items = re.findall(r'<li>\s*<span class="no">(\d+)</span>\s*<div class="t">\s*<div class="m">(.*?)</div>\s*<div class="s">(.*?)</div>\s*</div>\s*</li>', html, re.DOTALL)
    
    # Extract registration no
    reg_no = re.search(r'<span class="v">(.*?)</span>', html)
    
    print(f"=== {fname} ===")
    print(f"Colors: deep={deep_color.group(1) if deep_color else ''}, emerald={emerald_color.group(1) if emerald_color else ''}, lime={lime_color.group(1) if lime_color else ''}, mint={mint_color.group(1) if mint_color else ''}")
    print(f"Tagline: {re.sub('<[^<]+?>', '', tagline_match.group(1)).strip() if tagline_match else ''}")
    print(f"Title: {re.sub('<[^<]+?>', '', title_match.group(1)).strip() if title_match else ''}")
    print(f"EN: {re.sub('<[^<]+?>', '', en_match.group(1)).strip() if en_match else ''}")
    print(f"Effects: {[re.sub('<[^<]+?>', '', e).strip() for e in effects]}")
    print(f"Ing Title: {ing_title.group(1) if ing_title else ''}")
    print(f"Ing Count: {len(ing_items)}")
    for no, m, s in ing_items[:2]:
        print(f"  {no}. {re.sub('<[^<]+?>', '', m).strip()} // {re.sub('<[^<]+?>', '', s).strip()}")
    print(f"Reg No: {reg_no.group(1) if reg_no else ''}")
    print("-" * 50)

