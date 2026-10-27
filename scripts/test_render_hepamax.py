import os
from playwright.sync_api import sync_playwright

html_file = os.path.abspath("public/assets/labels/monsmecta_hepamax_label.html")
url = "file:///" + html_file.replace("\\", "/")

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(viewport={"width": 1600, "height": 1800}, device_scale_factor=2)
    page = context.new_page()

    # 1. Compare View
    page.goto(url + "?mode=compare")
    page.wait_for_timeout(1000)
    page.screenshot(path="public/assets/labels/hepamax_85x40_comparison_preview.png", full_page=True)
    print("Rendered hepamax_85x40_comparison_preview.png")

    # 2. White Mode Single Label (exact label-sheet screenshot)
    page.goto(url + "?mode=white")
    page.wait_for_timeout(500)
    white_sheet = page.locator("#card-white .label-sheet")
    white_sheet.screenshot(path="public/assets/labels/hepamax_30ml_85x40_white_back_preview.png")
    print("Rendered hepamax_30ml_85x40_white_back_preview.png")

    # 3. Dark Mode Single Label
    page.goto(url + "?mode=dark")
    page.wait_for_timeout(500)
    dark_sheet = page.locator("#card-dark .label-sheet")
    dark_sheet.screenshot(path="public/assets/labels/hepamax_30ml_85x40_dark_back_preview.png")
    print("Rendered hepamax_30ml_85x40_dark_back_preview.png")

    # 4. White Mode PDF Export (85mm x 40mm)
    page.goto(url + "?mode=white")
    page.wait_for_timeout(500)
    page.pdf(
        path="public/assets/labels/몬스멕타_헤파맥스_30ml_라벨_화이트뒷면(85x40mm).pdf",
        width="85mm",
        height="40mm",
        margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"},
        print_background=True
    )
    print("Exported 몬스멕타_헤파맥스_30ml_라벨_화이트뒷면(85x40mm).pdf")

    browser.close()

print("ALL 85x40mm TEST RENDERS COMPLETED SUCCESSFULLY!")
