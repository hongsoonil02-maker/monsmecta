# -*- coding: utf-8 -*-
import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1400, "height": 1000}, device_scale_factor=2)

        # 1. 100ml 캡처
        url_100 = "file:///" + os.path.abspath("public/assets/labels/monsmecta_100ml_modern.html").replace("\\", "/")
        await page.goto(url_100)
        await page.wait_for_load_state("networkidle")
        await page.wait_for_timeout(1000)

        # 전체 A4 가이드 래퍼
        a4_wrapper = page.locator(".a4-guide-wrapper")
        if await a4_wrapper.count() > 0:
            await a4_wrapper.screenshot(path="public/assets/labels/preview_modern_monsmecta_100ml_a4.png")
            print("Captured 100ml A4 view")

        # 스티커 본체
        sticker = page.locator(".sticker")
        if await sticker.count() > 0:
            await sticker.screenshot(path="public/assets/labels/preview_modern_monsmecta_100ml_sticker.png")
            print("Captured 100ml Sticker view")

        # 2. 30ml 캡처
        url_30 = "file:///" + os.path.abspath("public/assets/labels/monsmecta_30ml_modern.html").replace("\\", "/")
        await page.goto(url_30)
        await page.wait_for_load_state("networkidle")
        await page.wait_for_timeout(1000)

        a4_wrapper_30 = page.locator(".a4-guide-wrapper")
        if await a4_wrapper_30.count() > 0:
            await a4_wrapper_30.screenshot(path="public/assets/labels/preview_modern_monsmecta_30ml_a4.png")
            print("Captured 30ml A4 view")

        sticker_30 = page.locator(".sticker")
        if await sticker_30.count() > 0:
            await sticker_30.screenshot(path="public/assets/labels/preview_modern_monsmecta_30ml_sticker.png")
            print("Captured 30ml Sticker view")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())

