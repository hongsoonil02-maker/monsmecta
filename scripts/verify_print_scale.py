from playwright.sync_api import sync_playwright
import os

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    url = 'file:///' + os.path.abspath('public/assets/labels/monsmecta_original_white_label.html').replace('\\', '/')
    page.goto(url)
    page.emulate_media(media='print')
    sheet = page.locator('#card-white .label-sheet')
    box = sheet.bounding_box()
    
    px_per_mm = 96.0 / 25.4 # 3.779527559
    width_mm = box['width'] / px_per_mm
    height_mm = box['height'] / px_per_mm
    
    print(f"Rendered dimensions in print mode:")
    print(f"  Width : {box['width']:.2f}px = {width_mm:.2f} mm (Expected: 110.00 mm)")
    print(f"  Height: {box['height']:.2f}px = {height_mm:.2f} mm (Expected: 75.00 mm)")
    
    # Check 50mm ruler
    ruler = page.locator('.a4-calibration-header .no-roll, .a4-calibration-header div[style*="width:50mm"]').first
    ruler_box = ruler.bounding_box()
    if ruler_box:
        ruler_mm = ruler_box['width'] / px_per_mm
        print(f"  50mm Ruler: {ruler_box['width']:.2f}px = {ruler_mm:.2f} mm (Expected: 50.00 mm)")

    # Also render a screenshot of A4 print page
    pdf_path = 'public/assets/labels/test_verified_110x75.pdf'
    page.pdf(path=pdf_path, format='A4', print_background=True)
    print(f"PDF successfully rendered to {pdf_path}")
    browser.close()
