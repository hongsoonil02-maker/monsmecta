import os
import shutil
from playwright.sync_api import sync_playwright

def render_label(html_file, png_name, pdf_name):
    html_path = os.path.abspath(html_file)
    file_url = 'file:///' + html_path.replace('\\', '/')
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        # High-res screenshot (device_scale_factor=2)
        page = browser.new_page(viewport={'width': 1920, 'height': 1200}, device_scale_factor=2)
        page.goto(file_url)
        page.wait_for_timeout(1000)
        
        label = page.locator('.label-sheet')
        png_out = os.path.abspath(f'public/assets/labels/{png_name}')
        label.screenshot(path=png_out)
        print('Saved PNG:', png_out)
        
        # Print PDF
        pdf_out = os.path.abspath(f'public/assets/labels/{pdf_name}')
        page.pdf(
            path=pdf_out,
            width='85mm',
            height='40mm',
            margin={'top': '0mm', 'bottom': '0mm', 'left': '0mm', 'right': '0mm'},
            print_background=True
        )
        print('Saved PDF:', pdf_out)
        browser.close()

# 1. Render Renal Detox
render_label(
    'public/assets/labels/monsmecta_renal_label.html',
    'monsmecta_renal_30ml_label_hd.png',
    '몬스멕타_레날디톡스_30ml_라벨_인쇄용(85x40mm)_최종.pdf'
)
shutil.copyfile(
    'public/assets/labels/monsmecta_renal_30ml_label_hd.png',
    'public/assets/labels/몬스멕타_레날디톡스_30ml_라벨_고해상도(85x40mm).png'
)

# 2. Render Hepamax
render_label(
    'public/assets/labels/monsmecta_hepamax_label.html',
    'monsmecta_hepamax_30ml_label_hd.png',
    '몬스멕타_헤파맥스_30ml_라벨_인쇄용(85x40mm)_최종.pdf'
)
shutil.copyfile(
    'public/assets/labels/monsmecta_hepamax_30ml_label_hd.png',
    'public/assets/labels/몬스멕타_헤파맥스_30ml_라벨_고해상도(85x40mm).png'
)

# 3. Sync to dist if exists
if os.path.exists('dist/assets/labels'):
    for f in [
        'monsmecta_renal_label.html', 'monsmecta_renal_30ml_label_hd.png',
        '몬스멕타_레날디톡스_30ml_라벨_인쇄용(85x40mm)_최종.pdf', '몬스멕타_레날디톡스_30ml_라벨_고해상도(85x40mm).png',
        'monsmecta_hepamax_label.html', 'monsmecta_hepamax_30ml_label_hd.png',
        '몬스멕타_헤파맥스_30ml_라벨_인쇄용(85x40mm)_최종.pdf', '몬스멕타_헤파맥스_30ml_라벨_고해상도(85x40mm).png',
        'sj_logo_thumb.png'
    ]:
        src = os.path.join('public/assets/labels', f)
        dst = os.path.join('dist/assets/labels', f)
        if os.path.exists(src):
            shutil.copyfile(src, dst)
    print('Synced all label assets to dist/assets/labels')

print('All rendering complete.')
