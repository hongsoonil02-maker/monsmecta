import os
import shutil
from playwright.sync_api import sync_playwright

LABEL_ITEMS = [
    {
        "html": "public/assets/labels/monsmecta_hepamax_label.html",
        "png": "monsmecta_hepamax_30ml_label_hd.png",
        "pdf": "몬스멕타_헤파맥스_30ml_라벨_인쇄용(85x40mm)_최종.pdf",
        "png_ko": "몬스멕타_헤파맥스_30ml_라벨_고해상도(85x40mm).png"
    },
    {
        "html": "public/assets/labels/monsmecta_renal_label.html",
        "png": "monsmecta_renal_30ml_label_hd.png",
        "pdf": "몬스멕타_레날디톡스_30ml_라벨_인쇄용(85x40mm)_최종.pdf",
        "png_ko": "몬스멕타_레날디톡스_30ml_라벨_고해상도(85x40mm).png"
    },
    {
        "html": "public/assets/labels/monsmecta_probiotics_label.html",
        "png": "monsmecta_probiotics_30ml_label_hd.png",
        "pdf": "몬스멕타_프로바이오틱스_30ml_라벨_인쇄용(85x40mm)_최종.pdf",
        "png_ko": "몬스멕타_프로바이오틱스_30ml_라벨_고해상도(85x40mm).png"
    },
    {
        "html": "public/assets/labels/monsmecta_cancercare_label.html",
        "png": "monsmecta_cancercare_30ml_label_hd.png",
        "pdf": "몬스멕타_캔서케어_30ml_라벨_인쇄용(85x40mm)_최종.pdf",
        "png_ko": "몬스멕타_캔서케어_30ml_라벨_고해상도(85x40mm).png"
    },
    {
        "html": "public/assets/labels/monsmecta_coldzero_label.html",
        "png": "monsmecta_coldzero_30ml_label_hd.png",
        "pdf": "몬스멕타_콜드제로_30ml_라벨_인쇄용(85x40mm)_최종.pdf",
        "png_ko": "몬스멕타_콜드제로_30ml_라벨_고해상도(85x40mm).png"
    },
    {
        "html": "public/assets/labels/monsmecta_skincare_label.html",
        "png": "monsmecta_skincare_30ml_label_hd.png",
        "pdf": "몬스멕타_스킨케어_30ml_라벨_인쇄용(85x40mm)_최종.pdf",
        "png_ko": "몬스멕타_스킨케어_30ml_라벨_고해상도(85x40mm).png"
    },
    {
        "html": "public/assets/labels/monsmecta_heartcare_label.html",
        "png": "monsmecta_heartcare_30ml_label_hd.png",
        "pdf": "몬스멕타_하트케어_30ml_라벨_인쇄용(85x40mm)_최종.pdf",
        "png_ko": "몬스멕타_하트케어_30ml_라벨_고해상도(85x40mm).png"
    },
    {
        "html": "public/assets/labels/monsmecta_jointcare_label.html",
        "png": "monsmecta_jointcare_30ml_label_hd.png",
        "pdf": "몬스멕타_조인트케어_30ml_라벨_인쇄용(85x40mm)_최종.pdf",
        "png_ko": "몬스멕타_조인트케어_30ml_라벨_고해상도(85x40mm).png"
    },
    {
        "html": "public/assets/labels/monsmecta_powerase_label.html",
        "png": "monsmecta_powerase_30ml_label_hd.png",
        "pdf": "몬스멕타_파워라제_30ml_라벨_인쇄용(85x40mm)_최종.pdf",
        "png_ko": "몬스멕타_파워라제_30ml_라벨_고해상도(85x40mm).png"
    },
    {
        "html": "public/assets/labels/monsmecta_vitaplus_label.html",
        "png": "monsmecta_vitaplus_30ml_label_hd.png",
        "pdf": "몬스멕타_비타플러스_30ml_라벨_인쇄용(85x40mm)_최종.pdf",
        "png_ko": "몬스멕타_비타플러스_30ml_라벨_고해상도(85x40mm).png"
    },
    {
        "html": "public/assets/labels/monsmecta_original_30ml_label.html",
        "png": "monsmecta_original_30ml_label_hd.png",
        "pdf": "몬스멕타_오리지널_30ml_라벨_인쇄용(85x40mm)_최종.pdf",
        "png_ko": "몬스멕타_오리지널_30ml_라벨_고해상도(85x40mm).png"
    }
]

def render_label(p, html_file, png_name, pdf_name):
    html_path = os.path.abspath(html_file)
    file_url = 'file:///' + html_path.replace('\\', '/')
    
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 1920, 'height': 1200}, device_scale_factor=2)
    page.goto(file_url)
    page.wait_for_timeout(1000)
    
    label = page.locator('.label-sheet')
    png_out = os.path.abspath(f'public/assets/labels/{png_name}')
    label.screenshot(path=png_out)
    print('Saved PNG:', png_out)
    
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

def main():
    with sync_playwright() as p:
        for item in LABEL_ITEMS:
            print(f"Rendering: {item['html']}...")
            render_label(p, item['html'], item['png'], item['pdf'])
            
            src_png = os.path.abspath(f"public/assets/labels/{item['png']}")
            dst_png = os.path.abspath(f"public/assets/labels/{item['png_ko']}")
            shutil.copyfile(src_png, dst_png)

    # Sync to dist if exists
    if os.path.exists('dist/assets/labels'):
        for item in LABEL_ITEMS:
            for f in [item['html'].split('/')[-1], item['png'], item['pdf'], item['png_ko']]:
                src = os.path.join('public/assets/labels', f)
                dst = os.path.join('dist/assets/labels', f)
                if os.path.exists(src):
                    shutil.copyfile(src, dst)
        print('Synced all label assets to dist/assets/labels')

    print('All rendering complete.')

if __name__ == "__main__":
    main()
