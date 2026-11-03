# -*- coding: utf-8 -*-
import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1500, "height": 1100}, device_scale_factor=1)

        base = "file:///" + os.path.abspath("public/assets/labels/monsmecta_labels_viewer.html").replace("\\", "/")
        await page.goto(base)
        await page.wait_for_load_state("networkidle")
        await page.wait_for_timeout(1500)

        # 유스 테스트 버튼 클릭
        await page.click("#style-youth")
        await page.wait_for_timeout(2000)
        await page.screenshot(path="public/assets/labels/preview_viewer_youth.png")
        print("Captured viewer youth mode")

        # 30ml 전환
        await page.click("#size-30")
        await page.wait_for_timeout(2000)
        await page.screenshot(path="public/assets/labels/preview_viewer_youth_30.png")
        print("Captured viewer youth 30ml")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
