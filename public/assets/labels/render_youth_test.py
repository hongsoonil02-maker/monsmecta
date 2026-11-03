# -*- coding: utf-8 -*-
import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1400, "height": 1000}, device_scale_factor=2)

        base = "file:///" + os.path.abspath("public/assets/labels/01_monsmecta_original_youth.html").replace("\\", "/")

        # 1. 100ml
        await page.goto(base + "?size=100")
        await page.wait_for_load_state("networkidle")
        await page.wait_for_timeout(1200)
        sticker = page.locator(".sticker")
        await sticker.screenshot(path="public/assets/labels/preview_youth_01_100ml.png")
        print("Captured youth 100ml")

        # 2. 30ml
        await page.goto(base + "?size=30")
        await page.wait_for_load_state("networkidle")
        await page.wait_for_timeout(1200)
        sticker = page.locator(".sticker")
        await sticker.screenshot(path="public/assets/labels/preview_youth_01_30ml.png")
        print("Captured youth 30ml")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
