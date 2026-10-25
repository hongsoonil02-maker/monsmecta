import glob
import os
import re

files = glob.glob(r'public/assets/labels/*_label_print.html')
for f in sorted(files):
    name = os.path.basename(f)
    with open(f, encoding='utf-8') as fp:
        c = fp.read()
    title_m = re.search(r'<h1[^>]*>(.*?)</h1>', c)
    en_m = re.search(r'<h2[^>]*>(.*?)</h2>', c)
    sub_m = re.search(r'<p[^>]*class="[^"]*text-gray-400[^"]*"[^>]*>(.*?)</p>', c)
    reg_m = re.search(r'사료 성분등록번호.*?<div[^>]*>(.*?)</div>', c, re.S)
    type_m = re.search(r'사료의 종류 및 명칭.*?<div[^>]*>(.*?)</div>', c, re.S)
    print(f'=== {name} ===')
    print('Title:', title_m.group(1).strip() if title_m else 'N/A')
    print('EN:', en_m.group(1).strip() if en_m else 'N/A')
    print('Sub:', sub_m.group(1).strip() if sub_m else 'N/A')
    print('Reg:', reg_m.group(1).strip() if reg_m else 'N/A')
    print('Type:', type_m.group(1).strip() if type_m else 'N/A')
