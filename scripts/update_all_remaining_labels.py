import os
import re
import glob

# 1. Update _30ml_94x45.html files
files_94x45 = [
    r'public/assets/labels/monsmecta_hepamax_30ml_94x45.html',
    r'public/assets/labels/monsmecta_renal_30ml_94x45.html'
]

for fpath in files_94x45:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Title TM replacement: MONSMECTA HEPAMAX -> MONSMECTA™ HEPAMAX
    # Or in orbitron tag: <h2 class="en-title orbitron">MONSMECTA ...</h2>
    def replace_title_orbitron(match):
        inner = match.group(1)
        if '™' in inner:
            return match.group(0)
        new_inner = inner.replace('MONSMECTA', 'MONSMECTA<span style="font-size:0.65em; vertical-align:super; margin-left:0.3mm;">™</span>')
        return f'<h2 class="en-title orbitron">{new_inner}</h2>'

    content = re.sub(r'<h2 class="en-title orbitron">(.*?)</h2>', replace_title_orbitron, content)

    # Legal header replacement for dark and white cards:
    # Add U.S. TM App: 50/041,096
    old_reg = '''<div class="reg-num-line">
                                <span class="reg-num-label">사료의 성분등록번호 :</span>
                                <span class="reg-num-val">제 XX9UY0145호</span>
                            </div>'''
    new_reg = '''<div class="reg-num-line" style="display:flex; justify-content:space-between; align-items:center;">
                                <div>
                                    <span class="reg-num-label">사료의 성분등록번호 :</span>
                                    <span class="reg-num-val">제 XX9UY0145호</span>
                                </div>
                                <span style="font-size:0.95mm; font-weight:800; white-space:nowrap; opacity:0.9;">U.S. TM App: 50/041,096</span>
                            </div>'''
    
    if old_reg in content:
        content = content.replace(old_reg, new_reg)
    else:
        # regex fallback if spacing differs
        content = re.sub(
            r'<div class="reg-num-line">\s*<span class="reg-num-label">사료의 성분등록번호 :</span>\s*<span class="reg-num-val">제 XX9UY0145호</span>\s*</div>',
            new_reg,
            content
        )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated 94x45 file: {fpath}')


# 2. Update all *_label_print.html in public/assets/labels/
print_files = glob.glob('public/assets/labels/*_label_print.html') + glob.glob('public/assets/labels/*_print.html')

for fpath in print_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Title TM replacement: MONSMECTA -> MONSMECTA™
    if '™' not in content:
        # replace in MONSMECTA headings
        content = re.sub(r'MONSMECTA\b(?!™)', 'MONSMECTA™', content)
        content = re.sub(r'몬스멕타\b(?!™)', '몬스멕타™', content)

    # Patent & U.S. TM App No
    if '50/041,096' not in content:
        # Look for patent or registration number
        content = content.replace(
            '제XX9UY0145호</span>',
            '제XX9UY0145호</span>\n                                </div>\n                                <div class="flex justify-between items-center text-[11px] text-emerald-300 mt-1">\n                                    <span>U.S. Trademark App. No.</span>\n                                    <span class="font-mono font-bold text-orange-300">50/041,096</span>'
        )
        content = content.replace(
            '제 XX9UY0145호</span>',
            '제 XX9UY0145호</span>\n                                </div>\n                                <div class="flex justify-between items-center text-[11px] text-emerald-300 mt-1">\n                                    <span>U.S. Trademark App. No.</span>\n                                    <span class="font-mono font-bold text-orange-300">50/041,096</span>'
        )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated print file: {fpath}')
