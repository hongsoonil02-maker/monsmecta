# -*- coding: utf-8 -*-
import asyncio
from playwright.async_api import async_playwright
import os

FILES = [
    ("02", "hepamax"), ("03", "renal"), ("04", "cancercare"), ("05", "coldzero"),
    ("06", "skincare"), ("07", "heartcare"), ("08", "jointcare"), ("09", "powerase"),
    ("10", "probiotics"), ("11", "vitaplus"),
]

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1400, "height": 1000}, device_scale_factor=2)
        errors = []
        page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)

        for num, key in FILES:
            for size in ("100", "30"):
                base = "file:///" + os.path.abspath(
                    "public/assets/labels/%s_monsmecta_%s_youth.html" % (num, key)).replace("\\", "/")
                await page.goto(base + "?size=" + size)
                await page.wait_for_load_state("networkidle")
                await page.wait_for_timeout(800)
                sticker = page.locator(".sticker")
                out = "public/assets/labels/preview_youth_%s_%s_%sml.png" % (num, key, size)
                await sticker.screenshot(path=out)
                print("captured", out)

        if errors:
            print("CONSOLE ERRORS:", errors[:10])
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
