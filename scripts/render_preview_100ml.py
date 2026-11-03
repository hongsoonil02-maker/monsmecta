import asyncio
import os
from playwright.async_api import async_playwright

async def render_preview():
    html_path = os.path.abspath(r"c:\Users\master\monsmecta_landing\public\assets\labels\test_100ml_tight_original.html")
    file_url = f"file:///{html_path.replace(os.sep, '/')}"
    
    preview_png = r"c:\Users\master\monsmecta_landing\public\assets\labels\test_100ml_tight_white.png"
    preview_pdf = r"c:\Users\master\monsmecta_landing\public\assets\labels\test_100ml_tight_white.pdf"
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1280, "height": 900}, device_scale_factor=2)
        await page.goto(file_url, wait_until="networkidle")
        
        # Click White back view
        await page.evaluate("setViewMode('white')")
        await page.wait_for_timeout(500)
        
        # Take screenshot of the white card
        white_card = await page.query_selector("#card-white .label-sheet")
        if white_card:
            await white_card.screenshot(path=preview_png)
            print(f"Card Screenshot saved: {preview_png}")
            
        # Also print A4 PDF
        await page.pdf(
            path=preview_pdf,
            format="A4",
            print_background=True,
            margin={"top": "8mm", "bottom": "0", "left": "0", "right": "0"}
        )
        print(f"PDF saved: {preview_pdf}")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(render_preview())

