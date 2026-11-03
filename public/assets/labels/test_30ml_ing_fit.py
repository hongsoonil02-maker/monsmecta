# -*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright

test_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: #1e1645; display: flex; justify-content: center; padding: 20px; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans KR", sans-serif; }

.col-left { width: 38.3mm; background: #1e1645; color: #fff; padding: 1mm; }

.ing { background: #e0e7ff; color: #1e1645; border-radius: 1.8mm; padding: 0.7mm 1.0mm; }
.ing-h { display: flex; align-items: center; justify-content: space-between; padding-bottom: 0.3mm; margin-bottom: 0.35mm; border-bottom: 0.18mm dashed #a5b4fc; }
.ing-h .ti { font-size: 1.2mm; font-weight: 900; }
.ing-h .ref { font-size: 0.95mm; font-weight: 800; color: #fff; background: #6366f1; border-radius: 999px; padding: 0.2mm 0.8mm; }

.row { display: flex; align-items: flex-start; gap: 0.6mm; margin-bottom: 0.3mm; }
.row:last-child { margin-bottom: 0; }
.no { width: 1.35mm; height: 1.35mm; border-radius: 50%; background: #1e1645; color: #fff; font-size: 0.9mm; font-weight: 900; display: flex; align-items: center; justify-content: center; flex: 0 0 1.35mm; }
.rb { flex: 1; min-width: 0; }
.rm { font-size: 0.98mm; font-weight: 800; line-height: 1.15; letter-spacing: -0.04em; white-space: nowrap; overflow: hidden; text-overflow: clip; }
</style>
</head>
<body>
<div class="col-left">
  <div class="ing">
    <div class="ing-h">
      <span class="ti">주요 성분량(5대 복합)</span>
      <span class="ref">30ml 정품 규격</span>
    </div>
    <div class="row"><span class="no">1</span><div class="rb"><div class="rm">Montmorillonite (몬모릴로나이트) - 고함량</div></div></div>
    <div class="row"><span class="no">2</span><div class="rb"><div class="rm">Bifidobacterium longum - 1.0 x 10¹¹ cfu</div></div></div>
    <div class="row"><span class="no">3</span><div class="rb"><div class="rm">비타민 A (Vitamin A) - 400,000 IU</div></div></div>
    <div class="row"><span class="no">4</span><div class="rb"><div class="rm">비타민 D3 (Vitamin D3) - 80,000 IU</div></div></div>
    <div class="row"><span class="no">5</span><div class="rb"><div class="rm">비타민 E (Vitamin E) - 200 IU</div></div></div>
  </div>
</div>
</body>
</html>
"""

with open(r"C:\Users\master\monsmecta_landing\public\assets\labels\test_ing.html", "w", encoding="utf-8") as f:
    f.write(test_html)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 400, "height": 300})
    page.goto(r"file:///C:/Users/master/monsmecta_landing/public\assets\labels\test_ing.html")
    page.locator(".ing").screenshot(path=r"C:\Users\master\monsmecta_landing\public\assets\labels\test_ing.png")
    browser.close()

print("Ing test rendered successfully!")

