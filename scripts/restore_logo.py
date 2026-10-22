import base64
import os
import shutil

# 1. Read base64 data uri of the real logo
with open('public/assets/labels/sj_logo_thumb.png', 'rb') as f:
    b64_logo = base64.b64encode(f.read()).decode('utf-8')
data_uri = f'data:image/png;base64,{b64_logo}'

# Also copy sj_logo_thumb.png to public/assets
os.makedirs('public/assets', exist_ok=True)
shutil.copyfile('public/assets/labels/sj_logo_thumb.png', 'public/assets/snj_logo.png')
shutil.copyfile('public/assets/labels/sj_logo_thumb.png', 'public/assets/sj_logo.png')

def update_file(path):
    if not os.path.exists(path):
        return
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace CSS for company-logo-circle
    css_target = """.company-logo-circle {
            width: 2.5mm;
            height: 2.5mm;
            border-radius: 50%;
            background: #fff;
            border: 0.15mm solid #ffd700;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            flex-shrink: 0;
            box-shadow: 0 0 0.5mm rgba(255, 215, 0, 0.6);
            margin-top: 0.1mm;
        }"""
    
    css_replacement = """.company-logo-circle {
            width: 3.4mm;
            height: 3.4mm;
            border-radius: 50%;
            background: #fff;
            border: 0.15mm solid #ffd700;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            flex-shrink: 0;
            box-shadow: 0 0 0.6mm rgba(255, 215, 0, 0.6);
            margin-top: 0.05mm;
        }"""
    
    if css_target in content:
        content = content.replace(css_target, css_replacement)
    
    # 2. Replace the img tag
    # Find the start of company-logo-circle
    marker_start = '<div class="company-logo-circle">'
    if marker_start in content:
        start_idx = content.find(marker_start)
        end_idx = content.find('</div>', start_idx) + len('</div>')
        old_block = content[start_idx:end_idx]
        new_block = f'<div class="company-logo-circle">\n                                <img src="{data_uri}" alt="에스앤제이 동물병원">\n                            </div>'
        content = content[:start_idx] + new_block + content[end_idx:]
        print('Successfully replaced logo block in:', path)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

update_file('public/assets/labels/monsmecta_renal_label.html')
update_file('public/assets/labels/monsmecta_hepamax_label.html')

if os.path.exists(r'c:\Users\master\parvogel_landing\public\assets\monsmecta_hepamax_label.html'):
    update_file(r'c:\Users\master\parvogel_landing\public\assets\monsmecta_hepamax_label.html')

print('Logo restoration script finished.')
