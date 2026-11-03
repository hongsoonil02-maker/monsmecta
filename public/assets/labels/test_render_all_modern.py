# -*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright
import os

base_dir = r"C:\Users\master\monsmecta_landing\public\assets\labels"

test_items = [
    ("01_monsmecta_original_modern.html", "preview_modern_01_original_100ml.png", "100"),
    ("01_monsmecta_original_modern.html", "preview_modern_01_original_30ml.png", "30"),
    ("02_monsmecta_hepamax_modern.html", "preview_modern_02_hepamax_100ml.png", "100"),
    ("03_monsmecta_renal_modern.html", "preview_modern_03_renal_100ml.png", "100"),
    ("04_monsmecta_cancercare_modern.html", "preview_modern_04_cancercare_100ml.png", "100"),
    ("05_monsmecta_coldzero_modern.html", "preview_modern_05_coldzero_100ml.png", "100"),
    ("06_monsmecta_skincare_modern.html", "preview_modern_06_skincare_100ml.png", "100"),
    ("07_monsmecta_heartcare_modern.html", "preview_modern_07_heartcare_100ml.png", "100"),
    ("08_monsmecta_jointcare_modern.html", "preview_modern_08_jointcare_100ml.png", "100"),
    ("09_monsmecta_powerase_modern.html", "preview_modern_09_powerase_100ml.png", "100"),
    ("10_monsmecta_probiotics_modern.html", "preview_modern_10_probiotics_100ml.png", "100"),
    ("11_monsmecta_vitaplus_modern.html", "preview_modern_11_vitaplus_100ml.png", "100"),
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1280, "height": 950})

    for fname, out_img, size in test_items:
        fpath = os.path.join(base_dir, fname)
        file_url = f"file:///{fpath.replace(os.sep, '/')}?size={size}"
        page.goto(file_url, wait_until="networkidle")
        page.wait_for_timeout(300)
        
        # 스티커 요소만 스크린샷
        sticker_elem = page.locator(".sticker")
        out_path = os.path.join(base_dir, out_img)
        sticker_elem.screenshot(path=out_path)
        print(f"Captured: {out_img}")

    browser.close()

print("All screenshots captured successfully!")

