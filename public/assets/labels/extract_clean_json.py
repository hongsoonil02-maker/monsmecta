import glob
import os
import re
import json

base_dir = r'C:\Users\master\monsmecta_landing\public\assets\labels'
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

def clean_html(text):
    if not text: return ""
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

products_data = []

for fname in files:
    fpath = os.path.join(base_dir, fname)
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    # CSS colors
    root_match = re.search(r':root\s*\{([^}]+)\}', html)
    root_css = root_match.group(1) if root_match else ''
    
    def get_var(var_name, default=''):
        m = re.search(rf'--{var_name}:\s*([^;]+);', root_css)
        return m.group(1).strip() if m else default

    colors = {
        'deep': get_var('deep', '#06402f'),
        'deep_2': get_var('deep-2', '#0b5a42'),
        'deep_3': get_var('deep-3', '#04291f'),
        'emerald': get_var('emerald', '#0e9f6e'),
        'mint': get_var('mint', '#bff0d6'),
        'lime': get_var('lime', '#d8f46a'),
        'cream': get_var('cream', '#fff6e3'),
        'peach': get_var('peach', '#ffc9a3'),
        'coral': get_var('coral', '#e8553b'),
        'ink': get_var('ink', '#0b2a20'),
    }

    # Front content
    tagline_m = re.search(r'<div class="tagline">(.*?)</div>', html, re.DOTALL)
    title_m = re.search(r'<h1 class="title">(.*?)</h1>', html, re.DOTALL)
    en_m = re.search(r'<h2 class="en">(.*?)</h2>', html, re.DOTALL)
    
    tagline = clean_html(tagline_m.group(1)) if tagline_m else ''
    title = clean_html(title_m.group(1)) if title_m else ''
    en = clean_html(en_m.group(1)) if en_m else ''
    
    # Clean title / en if ™ is attached
    title_clean = title.replace('™', '').strip()
    en_clean = en.replace('™', '').strip()

    # Effects
    eff_m = re.search(r'<div class="effects">(.*?)</div>\s*<div class="ing">', html, re.DOTALL)
    effects = []
    if eff_m:
        lis = re.findall(r'<li>(.*?)</li>', eff_m.group(1), re.DOTALL)
        for li in lis:
            effects.append(clean_html(li))

    # Ingredients
    ing_sec_m = re.search(r'<div class="ing">(.*?)</div>\s*<div class="f-bottom">', html, re.DOTALL)
    ing_title = "성분(5가지 복합체)"
    ing_items = []
    if ing_sec_m:
        ing_h3 = re.search(r'<h3>(.*?)</h3>', ing_sec_m.group(1))
        if ing_h3: ing_title = clean_html(ing_h3.group(1))
        lis = re.findall(r'<li>\s*<span class="no">(\d+)</span>\s*<div>(.*?)</div>\s*</li>', ing_sec_m.group(1), re.DOTALL)
        for num, content in lis:
            # clean inner
            m_part = re.search(r'<div class="m">(.*?)</div>', content, re.DOTALL)
            s_part = re.search(r'<div class="s">(.*?)</div>', content, re.DOTALL)
            main_txt = clean_html(m_part.group(1)) if m_part else clean_html(content)
            sub_txt = clean_html(s_part.group(1)) if s_part else ""
            ing_items.append({'num': num, 'main': main_txt, 'sub': sub_txt})

    # Back content
    reg_no_m = re.search(r'<div class="b-reg">.*?<span class="v">(.*?)</span>', html, re.DOTALL)
    reg_no = clean_html(reg_no_m.group(1)) if reg_no_m else '제 XX9UY0145호'

    # Trademark numbers
    b_tm_m = re.search(r'<div class="b-tm">(.*?)</div>', html, re.DOTALL)
    kr_tm = "제40-2026-0140274호 (05류/31류)"
    us_tm = "App No. 50/041,096"
    if b_tm_m:
        tms = re.findall(r'<span class="n">(.*?)</span>', b_tm_m.group(1))
        if len(tms) >= 1: kr_tm = clean_html(tms[0])
        if len(tms) >= 2: us_tm = clean_html(tms[1])

    # Info paragraphs
    b_info_m = re.search(r'<div class="b-info">(.*?)</div>\s*<div class="b-dose">', html, re.DOTALL)
    b_info_html = b_info_m.group(1) if b_info_m else ''
    
    feed_type_m = re.search(r'사료의 종류와 명칭[^:]*:\s*</b>\s*(.*?)</p>', b_info_html, re.DOTALL)
    feed_type = clean_html(feed_type_m.group(1)) if feed_type_m else '보조사료/미생물제/바실러스 서브틸리스(액상)/반려동물'

    feed_qty_m = re.search(r'등록성분량[^:]*:\s*</b>\s*(.*?)</p>', b_info_html, re.DOTALL)
    feed_qty = clean_html(feed_qty_m.group(1)) if feed_qty_m else '바실러스 서브틸리스 1.0 x 10⁶ cfu/g 이상, 부형제( 정제수 )'

    feed_mat_m = re.search(r'사용한 원료의 명칭[^:]*:\s*</b>\s*(.*?)</p>', b_info_html, re.DOTALL)
    feed_mat = clean_html(feed_mat_m.group(1)) if feed_mat_m else '바실러스 서브틸리스, 비타민A, 아세트산 나트륨, 프로피온산 나트륨, 포도당, 몬모릴로나이트, 정제수'

    feed_target_m = re.search(r'대상[^:]*:\s*</b>\s*(.*?)</p>', b_info_html, re.DOTALL)
    feed_target = clean_html(feed_target_m.group(1)) if feed_target_m else '반려견, 반려묘'

    b_eff_lis = re.findall(r'<li><span class="r">.*?</span><span>(.*?)</span></li>', b_info_html, re.DOTALL)
    back_effects = [clean_html(x) for x in b_eff_lis]

    # Dosage
    dose_m = re.search(r'<div class="b-dose">.*?<div class="t">용법 및 용량\s*:\s*<span>(.*?)</span></div>.*?<div class="s">(.*?)</div>', html, re.DOTALL)
    dose_t = clean_html(dose_m.group(1)) if dose_m else '1일 1~2ml / 체중 5kg'
    dose_s = clean_html(dose_m.group(2)) if dose_m else '( 1 펌프 = 약 1ml ) - 증상에 따라 조절 가능'

    # Warnings
    warn_m = re.search(r'<div class="b-warn">.*?<ul>(.*?)</ul>', html, re.DOTALL)
    warnings = []
    if warn_m:
        w_lis = re.findall(r'<li>(.*?)</li>', warn_m.group(1), re.DOTALL)
        for w in w_lis:
            warnings.append(clean_html(w))

    pdata = {
        'file': fname,
        'colors': colors,
        'tagline': tagline,
        'title': title_clean,
        'en': en_clean,
        'effects': effects,
        'ing_title': ing_title,
        'ing_items': ing_items,
        'reg_no': reg_no,
        'kr_tm': kr_tm,
        'us_tm': us_tm,
        'feed_type': feed_type,
        'feed_qty': feed_qty,
        'feed_mat': feed_mat,
        'feed_target': feed_target,
        'back_effects': back_effects,
        'dose_t': dose_t,
        'dose_s': dose_s,
        'warnings': warnings,
    }
    products_data.append(pdata)

out_json = os.path.join(base_dir, 'all_11_products_data.json')
with open(out_json, 'w', encoding='utf-8') as f:
    json.dump(products_data, f, ensure_ascii=False, indent=2)

print(f"Extracted {len(products_data)} products to {out_json}")
for p in products_data:
    print(f"- {p['file']}: {p['title']} ({p['en']}) | colors={p['colors']['deep']}, {p['colors']['lime']}")

