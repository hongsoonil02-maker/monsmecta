import os
import shutil
from playwright.sync_api import sync_playwright

TASKS = [
    {
        "id": "monsmecta",
        "html": "public/assets/labels/monsmecta_original_label.html",
        "png": "monsmecta_original_30ml_label_hd.png",
        "png_ko": "몬스멕타_오리지널_30ml_라벨_고해상도(85x40mm).png",
        "pdf": "몬스멕타_오리지널_30ml_라벨_인쇄용(85x40mm)_최종.pdf"
    },
    {
        "id": "hepamax",
        "html": "public/assets/labels/monsmecta_hepamax_label.html",
        "png": "monsmecta_hepamax_30ml_label_hd.png",
        "png_ko": "몬스멕타_헤파맥스_30ml_라벨_고해상도(85x40mm).png",
        "pdf": "몬스멕타_헤파맥스_30ml_라벨_인쇄용(85x40mm)_최종.pdf"
    },
    {
        "id": "urinary",
        "html": "public/assets/labels/monsmecta_renal_label.html",
        "png": "monsmecta_renal_30ml_label_hd.png",
        "png_ko": "몬스멕타_레날디톡스_30ml_라벨_고해상도(85x40mm).png",
        "pdf": "몬스멕타_레날디톡스_30ml_라벨_인쇄용(85x40mm)_최종.pdf"
    },
    {
        "id": "cancercare",
        "html": "public/assets/labels/monsmecta_cancercare_label.html",
        "png": "monsmecta_cancercare_30ml_label_hd.png",
        "png_ko": "몬스멕타_캔서케어_30ml_라벨_고해상도(85x40mm).png",
        "pdf": "몬스멕타_캔서케어_30ml_라벨_인쇄용(85x40mm)_최종.pdf"
    },
    {
        "id": "coldzero",
        "html": "public/assets/labels/monsmecta_coldzero_label.html",
        "png": "monsmecta_coldzero_30ml_label_hd.png",
        "png_ko": "몬스멕타_콜드제로_30ml_라벨_고해상도(85x40mm).png",
        "pdf": "몬스멕타_콜드제로_30ml_라벨_인쇄용(85x40mm)_최종.pdf"
    },
    {
        "id": "skincare",
        "html": "public/assets/labels/monsmecta_skincare_label.html",
        "png": "monsmecta_skincare_30ml_label_hd.png",
        "png_ko": "몬스멕타_스킨케어_30ml_라벨_고해상도(85x40mm).png",
        "pdf": "몬스멕타_스킨케어_30ml_라벨_인쇄용(85x40mm)_최종.pdf"
    },
    {
        "id": "heartcare",
        "html": "public/assets/labels/monsmecta_heartcare_label.html",
        "png": "monsmecta_heartcare_30ml_label_hd.png",
        "png_ko": "몬스멕타_하트케어_30ml_라벨_고해상도(85x40mm).png",
        "pdf": "몬스멕타_하트케어_30ml_라벨_인쇄용(85x40mm)_최종.pdf"
    },
    {
        "id": "jointcare",
        "html": "public/assets/labels/monsmecta_jointcare_label.html",
        "png": "monsmecta_jointcare_30ml_label_hd.png",
        "png_ko": "몬스멕타_조인트케어_30ml_라벨_고해상도(85x40mm).png",
        "pdf": "몬스멕타_조인트케어_30ml_라벨_인쇄용(85x40mm)_최종.pdf"
    },
    {
        "id": "powerase",
        "html": "public/assets/labels/monsmecta_powerase_label.html",
        "png": "monsmecta_powerase_30ml_label_hd.png",
        "png_ko": "몬스멕타_파워라제_30ml_라벨_고해상도(85x40mm).png",
        "pdf": "몬스멕타_파워라제_30ml_라벨_인쇄용(85x40mm)_최종.pdf"
    },
    {
        "id": "probiotics",
        "html": "public/assets/labels/monsmecta_probiotics_label.html",
        "png": "monsmecta_probiotics_30ml_label_hd.png",
        "png_ko": "몬스멕타_프로바이오틱스_30ml_라벨_고해상도(85x40mm).png",
        "pdf": "몬스멕타_프로바이오틱스_30ml_라벨_인쇄용(85x40mm)_최종.pdf"
    },
    {
        "id": "vitaplus",
        "html": "public/assets/labels/monsmecta_vitaplus_label.html",
        "png": "monsmecta_vitaplus_30ml_label_hd.png",
        "png_ko": "몬스멕타_비타플러스_30ml_라벨_고해상도(85x40mm).png",
        "pdf": "몬스멕타_비타플러스_30ml_라벨_인쇄용(85x40mm)_최종.pdf"
    }
]

def render_all():
    print(f"Starting render of {len(TASKS)} labels...")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1200},
            device_scale_factor=2
        )
        
        for task in TASKS:
            html_path = os.path.abspath(task["html"])
            file_url = 'file:///' + html_path.replace('\\', '/')
            
            page = context.new_page()
            page.goto(file_url)
            page.wait_for_timeout(800)
            
            label = page.locator('.label-sheet')
            png_out = os.path.abspath(f'public/assets/labels/{task["png"]}')
            label.screenshot(path=png_out)
            
            # also copy to Korean filename
            png_ko_out = os.path.abspath(f'public/assets/labels/{task["png_ko"]}')
            shutil.copyfile(png_out, png_ko_out)
            
            # Print PDF (85mm x 40mm)
            pdf_out = os.path.abspath(f'public/assets/labels/{task["pdf"]}')
            page.pdf(
                path=pdf_out,
                width='85mm',
                height='40mm',
                margin={'top': '0mm', 'bottom': '0mm', 'left': '0mm', 'right': '0mm'},
                print_background=True
            )
            print(f"[{task['id']}] Rendered PNG & PDF successfully.")
            page.close()
            
        browser.close()

    # Sync to dist if exists
    dist_labels_dir = 'dist/assets/labels'
    if os.path.exists(dist_labels_dir):
        for task in TASKS:
            for f in [task["png"], task["png_ko"], task["pdf"], os.path.basename(task["html"])]:
                src = os.path.join('public/assets/labels', f)
                dst = os.path.join(dist_labels_dir, f)
                if os.path.exists(src):
                    shutil.copyfile(src, dst)
        print("All assets synchronized to dist/assets/labels!")

    print(f"ALL {len(TASKS)} LABELS RENDERED AND VERIFIED!")

if __name__ == '__main__':
    render_all()
