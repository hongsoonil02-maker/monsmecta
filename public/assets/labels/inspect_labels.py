import glob
import os
import re

files = glob.glob(r'C:\Users\master\monsmecta_landing\public\assets\labels\*_label_claude.html')
for f in sorted(files):
    name = os.path.basename(f)
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    # Extract some key details
    title = re.search(r'<div class="brand-title[^"]*">(.*?)</div>', content)
    eng_title = re.search(r'<div class="brand-eng[^"]*">(.*?)</div>', content)
    tagline = re.search(r'<div class="brand-tagline[^"]*">(.*?)</div>', content)
    
    print(f"=== {name} ===")
    if title: print("Title:", title.group(1).strip()[:50])
    if eng_title: print("Eng:", eng_title.group(1).strip()[:50])
    if tagline: print("Tagline:", tagline.group(1).strip()[:50])

