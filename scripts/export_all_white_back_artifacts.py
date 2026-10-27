import os
import sys
from playwright.sync_api import sync_playwright

scripts_dir = os.path.dirname(os.path.abspath(__file__))
if scripts_dir not in sys.path:
    sys.path.insert(0, scripts_dir)

from generate_all_30ml_labels import PRODUCTS

out_dir = r"c:\Users\master\monsmecta_landing\public\assets\labels"

with sync_playwright() as p:
    browser = p.chromium.launch()
    for prod in PRODUCTS:
        html_file = os.path.join(out_dir, prod["file_name"])
        url = "file:///" + html_file.replace("\\", "/") + "?mode=white"
        page = browser.new_page(viewport={"width": 1004, "height": 472})
        page.goto(url)
        page.wait_for_timeout(300)
        
        base_name = prod["name_ko"].replace(" ", "_")
        img_name = f"{base_name}_30ml_라벨_화이트뒷면(85x40mm).png"
        pdf_name = f"{base_name}_30ml_라벨_화이트뒷면(85x40mm).pdf"
        
        el = page.query_selector(".label-box")
        if el:
            el.screenshot(path=os.path.join(out_dir, img_name))
            
        page.pdf(
            path=os.path.join(out_dir, pdf_name),
            width="85mm",
            height="40mm",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"}
        )
        print(f"Exported: {pdf_name} & {img_name}")
        page.close()
    browser.close()

print("ALL 11 PRODUCTS WHITE-BACK PDF & PNG ARTIFACTS CREATED SUCCESSFULLY!")
