# -*- coding: utf-8 -*-
"""
Generate 3-up A4 multi-label print sheets for:
1. 몬스멕타 (Monsmecta Original)
2. 몬스멕타 헤파맥스 (Monsmecta Hepamax)
3. 몬스멕타 레날 디톡스 (Monsmecta Renal Detox)

Places 3 identical 85mm x 40mm labels on one single A4 page with cutting crop marks
and 50mm calibration verification ruler.
"""
from playwright.sync_api import sync_playwright
import os
import shutil
import pypdf

ITEMS = [
    ("monsmecta_original_label.html", "01_몬스멕타_30ml_라벨_A4_3구인쇄(85x40mmx3).pdf", "01_몬스멕타_3구인쇄_85x40mm.pdf", "몬스멕타"),
    ("monsmecta_hepamax_label.html", "02_몬스멕타_헤파맥스_30ml_라벨_A4_3구인쇄(85x40mmx3).pdf", "02_몬스멕타_헤파맥스_3구인쇄_85x40mm.pdf", "몬스멕타 헤파맥스"),
    ("monsmecta_renal_label.html", "03_몬스멕타_레날_디톡스_30ml_라벨_A4_3구인쇄(85x40mmx3).pdf", "03_몬스멕타_레날디톡스_3구인쇄_85x40mm.pdf", "몬스멕타 레날 디톡스")
]

labels_dir = os.path.abspath("public/assets/labels")
desktop_dir = r"C:\Users\master\Desktop\몬스멕타_인쇄소전달용_85x40mm"
os.makedirs(desktop_dir, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    for html_file, a4_pdf_name, desktop_pdf_name, prod_name in ITEMS:
        page = browser.new_page()
        file_path = os.path.join(labels_dir, html_file)
        url = "file:///" + file_path.replace("\\", "/") + "?mode=white&paper=a4"
        page.goto(url)
        page.wait_for_timeout(600)
        
        # Inject JavaScript to duplicate the crop-marks-box 2 more times (total 3 labels vertically)
        # and adjust page styling for A4 3-up printing
        page.evaluate(f"""() => {{
            document.body.className = 'paper-a4 print-white';
            
            // 1. Update title in calibration header
            const titleEl = document.querySelector('.a4-calibration-header > div:first-child');
            if (titleEl) {{
                titleEl.textContent = '[30ml 정품 규격] {prod_name} 3구 실측 라벨 (85mm × 40mm × 3개)';
            }}
            
            // 2. Find the active white crop-marks-box
            const cardWhite = document.getElementById('card-white');
            if (!cardWhite) return;
            const originalCropBox = cardWhite.querySelector('.crop-marks-box');
            if (!originalCropBox) return;
            
            // 3. Create a multi-label container inside card-white
            const container = document.createElement('div');
            container.className = 'multi-label-print-container';
            container.style.display = 'flex';
            container.style.flexDirection = 'column';
            container.style.alignItems = 'center';
            container.style.gap = '14mm'; // space between 3 labels
            container.style.marginTop = '2mm';
            container.style.width = '100%';
            
            // Clone 3 times with unique cutting guidelines
            for (let i = 1; i <= 3; i++) {{
                const clone = originalCropBox.cloneNode(true);
                clone.style.margin = '0 auto';
                
                // Add a small label numbering tag above each
                const numTag = document.createElement('div');
                numTag.style.textAlign = 'center';
                numTag.style.fontSize = '7.5pt';
                numTag.style.fontWeight = '700';
                numTag.style.color = '#64748b';
                numTag.style.marginBottom = '2mm';
                numTag.textContent = '▼ 라벨 #' + i + ' (85mm × 40mm 정품 실측 크기)';
                
                const wrapper = document.createElement('div');
                wrapper.style.display = 'flex';
                wrapper.style.flexDirection = 'column';
                wrapper.style.alignItems = 'center';
                wrapper.appendChild(numTag);
                wrapper.appendChild(clone);
                
                container.appendChild(wrapper);
            }}
            
            // Replace original box with 3-up container
            originalCropBox.parentNode.replaceChild(container, originalCropBox);
            
            // Adjust A4 header margin to fit 3 labels cleanly on 1 page
            const header = document.querySelector('.a4-calibration-header');
            if (header) {{
                header.style.marginBottom = '4mm';
                header.style.paddingTop = '2mm';
            }}
            
            // Hide bottom cut instruction notice to preserve page space
            const cutInst = document.querySelector('.a4-cut-instructions');
            if (cutInst) {{
                cutInst.style.marginTop = '4mm';
                cutInst.style.fontSize = '8pt';
            }}
        }}""")
        page.wait_for_timeout(500)
        
        target_pdf = os.path.join(labels_dir, a4_pdf_name)
        page.pdf(
            path=target_pdf,
            format="A4",
            print_background=True,
            margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"}
        )
        page.close()
        
        # Verify page count is exactly 1 page
        reader = pypdf.PdfReader(target_pdf)
        num_pages = len(reader.pages)
        box = reader.pages[0].mediabox
        w_mm = float(box.width) * 25.4 / 72
        h_mm = float(box.height) * 25.4 / 72
        txt = reader.pages[0].extract_text()
        print(f"Generated {a4_pdf_name}: {num_pages} page(s) ({w_mm:.1f}x{h_mm:.1f}mm), chars={len(txt)}")
        
        # Deploy to desktop
        for dst in [os.path.join(desktop_dir, a4_pdf_name), os.path.join(desktop_dir, desktop_pdf_name)]:
            try:
                shutil.copyfile(target_pdf, dst)
            except PermissionError:
                shutil.copyfile(target_pdf, dst.replace(".pdf", "_최신수정본.pdf"))

    browser.close()

print("All 3 requested 3-up multi-label PDFs generated and deployed!")

