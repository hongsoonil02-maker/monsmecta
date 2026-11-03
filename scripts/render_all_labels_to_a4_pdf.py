# -*- coding: utf-8 -*-
"""
Render all 11 30ml labels to genuine A4 (210mm x 297mm) 1:1 scale print PDFs.
Includes:
- 85mm x 40mm exact 1:1 scale label in center
- Corner crop marks (재단선) for cutting
- 50mm calibration verification ruler (실측 확인용 50mm 눈금자)
- Korean Intellectual Property Office registration: 제40-2026-0140274호 (05류/31류)
- US USPTO registration: App No. 50/041,096
- Fixed manufacture date: 2026. 10. 20.
"""
from playwright.sync_api import sync_playwright
import os
import shutil
import pypdf

PRODUCTS = [
    ("monsmecta_original_label.html", "01_몬스멕타_30ml_라벨_A4실측인쇄용(85x40mm).pdf", "01_몬스멕타_85x40mm.pdf"),
    ("monsmecta_hepamax_label.html", "02_몬스멕타_헤파맥스_30ml_라벨_A4실측인쇄용(85x40mm).pdf", "02_몬스멕타_헤파맥스_85x40mm.pdf"),
    ("monsmecta_renal_label.html", "03_몬스멕타_레날_디톡스_30ml_라벨_A4실측인쇄용(85x40mm).pdf", "03_몬스멕타_레날디톡스_85x40mm.pdf"),
    ("monsmecta_cancercare_label.html", "04_몬스멕타_캔서케어_30ml_라벨_A4실측인쇄용(85x40mm).pdf", "04_몬스멕타_캔서케어_85x40mm.pdf"),
    ("monsmecta_coldzero_label.html", "05_몬스멕타_콜드제로_30ml_라벨_A4실측인쇄용(85x40mm).pdf", "05_몬스멕타_콜드제로_85x40mm.pdf"),
    ("monsmecta_skincare_label.html", "06_몬스멕타_스킨케어_30ml_라벨_A4실측인쇄용(85x40mm).pdf", "06_몬스멕타_스킨케어_85x40mm.pdf"),
    ("monsmecta_heartcare_label.html", "07_몬스멕타_하트케어_30ml_라벨_A4실측인쇄용(85x40mm).pdf", "07_몬스멕타_하트케어_85x40mm.pdf"),
    ("monsmecta_jointcare_label.html", "08_몬스멕타_조인트케어_30ml_라벨_A4실측인쇄용(85x40mm).pdf", "08_몬스멕타_조인트케어_85x40mm.pdf"),
    ("monsmecta_powerase_label.html", "09_몬스멕타_파워라제_30ml_라벨_A4실측인쇄용(85x40mm).pdf", "09_몬스멕타_파워라제_85x40mm.pdf"),
    ("monsmecta_probiotics_label.html", "10_몬스멕타_프로바이오틱스_30ml_라벨_A4실측인쇄용(85x40mm).pdf", "10_몬스멕타_프로바이오틱스_85x40mm.pdf"),
    ("monsmecta_vitaplus_label.html", "11_몬스멕타_비타플러스_30ml_라벨_A4실측인쇄용(85x40mm).pdf", "11_몬스멕타_비타플러스_85x40mm.pdf"),
]

workspace_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
labels_dir = os.path.join(workspace_dir, "public", "assets", "labels")
desktop_dir = r"C:\Users\master\Desktop\몬스멕타_인쇄소전달용_85x40mm"
os.makedirs(desktop_dir, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    for html_name, a4_pdf_name, desktop_pdf_name in PRODUCTS:
        page = browser.new_page()
        file_path = os.path.join(labels_dir, html_name)
        url = "file:///" + file_path.replace("\\", "/") + "?mode=white&paper=a4"
        page.goto(url)
        page.evaluate("""() => {
            document.body.className = 'paper-a4 print-white';
        }""")
        page.wait_for_timeout(800)
        
        target_a4_pdf = os.path.join(labels_dir, a4_pdf_name)
        page.pdf(
            path=target_a4_pdf,
            format="A4",
            print_background=True,
            margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"}
        )
        page.close()
        
        # Verify PDF dimensions & contents
        reader = pypdf.PdfReader(target_a4_pdf)
        box = reader.pages[0].mediabox
        w_mm = float(box.width) * 25.4 / 72
        h_mm = float(box.height) * 25.4 / 72
        text = reader.pages[0].extract_text()
        has_tm = "0140274" in text
        has_uspto = "50/041,096" in text
        print(f"Rendered {a4_pdf_name}: {w_mm:.1f}x{h_mm:.1f}mm | Text: {len(text)} chars | TM KR: {has_tm} | USPTO: {has_uspto}")
        
        # Copy to Desktop folder (both clean short name and descriptive name)
        for dst in [os.path.join(desktop_dir, desktop_pdf_name), os.path.join(desktop_dir, a4_pdf_name)]:
            try:
                shutil.copyfile(target_a4_pdf, dst)
            except PermissionError:
                alt_dst = dst.replace(".pdf", "_최신수정본.pdf")
                shutil.copyfile(target_a4_pdf, alt_dst)

    browser.close()

# Update main default 30ml PDF
orig_pdf = os.path.join(labels_dir, "01_몬스멕타_30ml_라벨_A4실측인쇄용(85x40mm).pdf")
for extra_dst in [
    os.path.join(labels_dir, "몬스멕타_30ml_라벨_인쇄용(85x40mm)_최종.pdf"),
    os.path.join(labels_dir, "몬스멕타_30ml_라벨_화이트뒷면(85x40mm).pdf"),
    os.path.join(desktop_dir, "몬스멕타_30ml_라벨_인쇄용(85x40mm)_최종.pdf"),
]:
    try:
        shutil.copyfile(orig_pdf, extra_dst)
    except PermissionError:
        shutil.copyfile(orig_pdf, extra_dst.replace(".pdf", "_최신수정본.pdf"))
print("Done! All 11 labels rendered as true A4 1:1 scale PDFs with crop marks and calibration ruler.")

