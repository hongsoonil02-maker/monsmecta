# -*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright
import os

base_dir = r"C:\Users\master\monsmecta_landing\public\assets\labels"
viewer_path = os.path.join(base_dir, "monsmecta_labels_viewer.html")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1400, "height": 1100})
    page.goto(f"file:///{viewer_path.replace(os.sep, '/')}", wait_until="networkidle")
    page.wait_for_timeout(1000)
    page.screenshot(path=os.path.join(base_dir, "preview_viewer_modern_all.png"))
    
    # 2번 헤파맥스 탭 클릭 테스트
    page.locator(".tab-btn").nth(1).click()
    page.wait_for_timeout(800)
    page.screenshot(path=os.path.join(base_dir, "preview_viewer_hepamax.png"))

    # 30ml 버튼 클릭 테스트
    page.locator("#size-30").click()
    page.wait_for_timeout(800)
    page.screenshot(path=os.path.join(base_dir, "preview_viewer_hepamax_30ml.png"))

    browser.close()

print("Viewer test completed successfully!")

