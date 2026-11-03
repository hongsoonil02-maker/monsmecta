# -*- coding: utf-8 -*-
import os
import sys
import shutil
from playwright.sync_api import sync_playwright
import pymupdf
from PIL import Image

scripts_dir = os.path.dirname(os.path.abspath(__file__))
if scripts_dir not in sys.path:
    sys.path.insert(0, scripts_dir)

from generate_all_30ml_labels import PRODUCTS
from build_all_100ml_tight_labels import render_tight_100ml_label_html

out_dir = r"c:\Users\master\monsmecta_landing\public\assets\labels"
desktop_100ml_dir = r"C:\Users\master\Desktop\몬스멕타_100ml_인쇄용_110x75mm"
brain_dir = r"C:\Users\master\.gemini\antigravity\brain\cacb210e-6377-4186-9128-20025d75e8f6"
os.makedirs(out_dir, exist_ok=True)
os.makedirs(desktop_100ml_dir, exist_ok=True)

def safe_copy(src, dst):
    try:
        shutil.copyfile(src, dst)
        return dst
    except PermissionError:
        base, ext = os.path.splitext(dst)
        fallback = f"{base}_최신수정본{ext}"
        shutil.copyfile(src, fallback)
        print(f"Warning: {dst} locked, saved as fallback: {fallback}")
        return fallback

def generate_100ml_variant_html(prod, title_ko):
    base_html = render_tight_100ml_label_html(prod)
    neon = prod.get("neon", "#10b981")
    border = prod.get("border", "#059669")
    top_bar = prod.get("top_bar", f"linear-gradient(90deg, {border}, {neon}, #ffffff, {border})")

    # 1. Custom CSS for 100ml with Left 7mm + Mid 7mm + Right 3mm wings
    # Total width: 7mm + 50mm + 7mm + 56mm + 3mm = 123mm
    # Height: 75mm
    custom_css = f"""<style>
        /* 123mm x 75mm 100ml Sticker Style (좌 7mm + 전면 50mm + 중 7mm + 후면 56mm + 우 3mm) */
        .crop-marks-box {{
            width: 123mm !important;
            height: 75mm !important;
        }}

        .sticker-wing-container {{
            display: flex !important;
            flex-direction: row !important;
            align-items: stretch !important;
            width: 123mm !important;
            height: 75mm !important;
            background: #ffffff !important;
            border: 0.25mm solid #cbd5e1 !important;
            box-sizing: border-box !important;
            margin: 0 auto !important;
            position: relative !important;
        }}

        /* 좌측 7mm 접착 날개 */
        .adhesive-wing-left {{
            width: 7.0mm !important;
            height: 100% !important;
            background: #ffffff !important;
            flex-shrink: 0 !important;
            box-sizing: border-box !important;
            position: relative !important;
            z-index: 10 !important;
            border-right: 0.20mm dashed #cbd5e1 !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
        }}
        .wing-text-left {{
            writing-mode: vertical-rl !important;
            text-orientation: mixed !important;
            font-size: 2.2mm !important;
            color: #94a3b8 !important;
            font-weight: 800 !important;
            letter-spacing: 1.0mm !important;
            opacity: 0.7 !important;
            user-select: none !important;
            white-space: nowrap !important;
        }}

        /* 우측 3mm 접착 날개 */
        .adhesive-wing-right {{
            width: 3.0mm !important;
            height: 100% !important;
            background: #ffffff !important;
            flex-shrink: 0 !important;
            box-sizing: border-box !important;
            position: relative !important;
            z-index: 10 !important;
            border-left: 0.20mm dashed #cbd5e1 !important;
        }}

        /* 본체 시트: 113mm (50mm + 7mm + 56mm) */
        .sticker-wing-container .label-sheet,
        body.paper-a4 #card-white .label-sheet,
        body.paper-a4 #card-dark .label-sheet {{
            width: 113.0mm !important;
            max-width: 113.0mm !important;
            min-width: 113.0mm !important;
            height: 100% !important;
            max-height: 100% !important;
            margin: 0 !important;
            border: none !important;
            transform: none !important;
            box-shadow: none !important;
            display: flex !important;
            flex-direction: column !important;
            position: relative !important;
            box-sizing: border-box !important;
        }}

        /* 상단 및 하단 테마 네온 액센트 바 (각 0.50mm 완벽 일치) */
        .top-accent-bar,
        .bottom-accent-bar {{
            height: 0.50mm !important;
            min-height: 0.50mm !important;
            background: {top_bar} !important;
            box-shadow: 0 0 1.5mm {neon}E6 !important;
            z-index: 10 !important;
            flex-shrink: 0 !important;
            width: 100% !important;
        }}

        .sticker-wing-container .content-wrap {{
            width: 113.0mm !important;
            flex: 1 1 auto !important;
            height: calc(100% - 1.00mm) !important;
            padding: 0 !important;
            display: flex !important;
            flex-direction: row !important;
            justify-content: flex-start !important;
            box-sizing: border-box !important;
            overflow: hidden !important;
        }}

        /* 좌측 전면 메인: 50.0mm (상하 넉넉한 여백 + 테마 네온 프레임) */
        .col-left {{
            width: 50.0mm !important;
            height: 100% !important;
            padding: 0.80mm 0.60mm 0.80mm 0.60mm !important;
            box-sizing: border-box !important;
            position: relative !important;
            flex-shrink: 0 !important;
            border-left: 0.20mm solid {neon} !important;
            border-right: 0.20mm solid {neon} !important;
            display: flex !important;
            flex-direction: column !important;
            justify-content: space-between !important;
        }}

        /* 중앙 7mm 분리 접착 공간 */
        .center-gap-7mm {{
            width: 7.0mm !important;
            height: 100% !important;
            background: #ffffff !important;
            flex-shrink: 0 !important;
            display: flex !important;
            flex-direction: column !important;
            align-items: center !important;
            justify-content: center !important;
            border-right: 0.20mm solid #cbd5e1 !important;
            box-sizing: border-box !important;
            position: relative !important;
            z-index: 5 !important;
        }}
        .center-gap-text {{
            writing-mode: vertical-rl !important;
            text-orientation: mixed !important;
            font-size: 2.2mm !important;
            color: #94a3b8 !important;
            font-weight: 800 !important;
            letter-spacing: 1.0mm !important;
            opacity: 0.7 !important;
            user-select: none !important;
            white-space: nowrap !important;
        }}

        /* 우측 법정 패널: 56.0mm */
        .col-right {{
            width: 56.0mm !important;
            height: 100% !important;
            padding: 0.60mm 0.80mm 0.60mm 0.80mm !important;
            box-sizing: border-box !important;
            position: relative !important;
            flex-shrink: 0 !important;
        }}

        #card-white .legal-panel {{
            height: 100% !important;
            box-sizing: border-box !important;
            padding: 0.80mm 1.0mm 0.80mm 1.0mm !important;
            display: flex !important;
            flex-direction: column !important;
            justify-content: space-between !important;
        }}

        /* ========================================================
           [수정 포인트 1] 핵심 효능 박스 내부 텍스트 상하 완벽 정중앙 정렬
           ======================================================== */
        .core-effects-box {{
            padding-top: 2.10mm !important;   /* 배지 아래 글씨 상하 정중앙 배치 */
            padding-bottom: 0.90mm !important;
            margin-top: 0.6mm !important;
            margin-bottom: 1.8mm !important;
        }}
        .effects-row:not(:last-child) {{
            margin-bottom: 0.45mm !important;
        }}

        /* ========================================================
           [수정 포인트 2] 하단 S&J VET FORMULA 바 내부 글씨 상하 정중앙 정렬
           ======================================================== */
        .col-left-bottom-bar,
        #card-white .col-left-bottom-bar,
        #card-dark .col-left-bottom-bar {{
            display: flex !important;
            align-items: center !important;
            justify-content: space-between !important;
            height: 3.80mm !important;
            min-height: 3.80mm !important;
            max-height: 3.80mm !important;
            padding: 0 1.30mm !important;
            box-sizing: border-box !important;
            line-height: 1 !important;
            margin-bottom: 0.6mm !important;
        }}
        .left-btm-brand {{
            display: inline-flex !important;
            align-items: center !important;
            line-height: 1 !important;
            transform: translateY(0.18mm) !important;
        }}
        .left-btm-brand strong {{
            line-height: 1 !important;
        }}
        .left-btm-target {{
            display: inline-flex !important;
            align-items: center !important;
            justify-content: center !important;
            height: 2.70mm !important;
            padding: 0 1.10mm !important;
            line-height: 1 !important;
            box-sizing: border-box !important;
            transform: translateY(0.10mm) !important;
        }}

        /* ========================================================
           [수정 포인트 3] 상표등록 번호 상단 점선과 시원한 간격 확보 및 정렬
           ======================================================== */
        .tm-dual-grid,
        #card-white .tm-dual-grid,
        #card-dark .tm-dual-grid {{
            display: flex !important;
            flex-direction: column !important;
            gap: 0.28mm !important;
            border-top: 0.20mm dashed #94a3b8 !important;
            padding-top: 0.85mm !important;   /* 점선 아래 여유 공간 확보 */
            padding-bottom: 0.40mm !important;
            margin-top: 0.50mm !important;
            margin-bottom: 0.40mm !important;
            box-sizing: border-box !important;
        }}
        .tm-line {{
            display: flex !important;
            justify-content: space-between !important;
            align-items: center !important;
            line-height: 1.2 !important;
        }}

        /* ========================================================
           [수정 포인트 4] 용법 및 용량 박스 내부 글씨 상하 정중앙 정렬
           ======================================================== */
        .dose-box-single,
        #card-white .dose-box-single,
        #card-dark .dose-box-single {{
            display: flex !important;
            align-items: center !important;
            justify-content: flex-start !important;
            height: 4.20mm !important;
            min-height: 4.20mm !important;
            max-height: 4.20mm !important;
            padding: 0 1.20mm !important;
            box-sizing: border-box !important;
            gap: 0.60mm !important;
            margin: 0.30mm 0 !important;
        }}
        .dose-box-single .title,
        .dose-box-single .desc,
        .dose-box-single .sub {{
            display: inline-flex !important;
            align-items: center !important;
            line-height: 1 !important;
            margin: 0 !important;
            padding: 0 !important;
            transform: translateY(0.18mm) !important;
        }}

        @media screen {{
            .sticker-wing-container {{
                box-shadow: 0 25px 60px rgba(0, 0, 0, 0.95) !important;
                transform: scale(1.6) !important;
                transform-origin: top center !important;
                margin-bottom: 50mm !important;
            }}
        }}

        @media print {{
            body.paper-a4 .crop-marks-box {{
                width: 123mm !important;
                height: 75mm !important;
            }}
            body.paper-roll,
            body.paper-roll .labels-stage,
            body.paper-roll .crop-marks-box {{
                width: 123mm !important;
                height: 75mm !important;
            }}
            .sticker-wing-container {{
                width: 123mm !important;
                height: 75mm !important;
                transform: none !important;
                box-shadow: none !important;
                margin: 0 auto !important;
            }}
            .sticker-wing-container .label-sheet,
            body.paper-a4 #card-white .label-sheet,
            body.paper-a4 #card-dark .label-sheet {{
                border: none !important;
                width: 113mm !important;
                max-width: 113mm !important;
                min-width: 113mm !important;
                height: 100% !important;
                max-height: 100% !important;
            }}
        }}
    </style></head>"""

    html = base_html.replace("</head>", custom_css, 1)

    # 2. Update divider column to center 7mm adhesive gap (using regex to avoid whitespace issues)
    import re
    divider_pattern = re.compile(
        r'<div class="divider-col">\s*<div class="divider-line"></div>\s*<div class="divider-diamond"></div>\s*</div>',
        re.MULTILINE
    )
    new_divider = """<!-- CENTER 7mm ADHESIVE GAP -->
                    <div class="center-gap-7mm">
                        <div class="center-gap-text">접착여백 7mm</div>
                    </div>"""
    html = divider_pattern.sub(new_divider, html)

    # 3. Wrap .label-sheet in .sticker-wing-container with left 7mm and right 3mm wings
    html = html.replace(
        '<div class="label-sheet">',
        '<div class="sticker-wing-container"><div class="adhesive-wing-left"><div class="wing-text-left">접착 7mm</div></div><div class="label-sheet">'
    )
    
    # Close label-sheet, add bottom accent bar, and add right 3mm wing
    end_pattern = re.compile(
        r'(<div><span class="co-addr">주소 : 경기도 화성시 팔탄면 석포로 74번길 10-25</span></div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>)\s*</div>',
        re.MULTILINE
    )
    replacement_end = r'\1\n                <div class="bottom-accent-bar"></div>\n            </div><div class="adhesive-wing-right"></div></div>'
    html = end_pattern.sub(replacement_end, html)

    # 4. Update texts and page size
    import re
    html = re.sub(
        r'\[100ml 정품 규격\][^\n<]+용기 라벨 \(110mm × 75mm\)',
        f'[100ml 정품 규격] {title_ko} 용기 라벨 [실물 테스트형] (좌측 7mm + 중간 7mm + 우측 3mm 접착 = 총 123×75mm)',
        html
    )
    html = html.replace(
        "정확히 110mm × 75mm 정품 라벨이 완성됩니다.",
        "좌측 7mm, 중간 7mm, 우측 3mm 접착 여백이 포함된 <strong>총 123mm × 75mm 실측 스티커</strong>가 완성됩니다."
    )
    html = html.replace(
        "정확히 <strong>110mm × 75mm 정품 라벨</strong>이 완성됩니다.",
        "좌측 7mm, 중간 7mm, 우측 3mm 접착 여백이 포함된 <strong>총 123mm × 75mm 실측 스티커</strong>가 완성됩니다."
    )
    html = html.replace("@page { size: 110mm 75mm; margin: 0; }", "@page { size: 123mm 75mm; margin: 0; }")

    return html

def main():
    print(f"=== [100ml 전체 11종 라인업 123x75mm (좌7+중7+우3mm 접착형) 일괄 생성 시작 ({len(PRODUCTS)}종)] ===")

    items = []
    PREFIX_MAP = {
        "monsmecta": ("01_몬스멕타", "몬스멕타™ 오리지널"),
        "hepamax": ("02_몬스멕타_헤파맥스", "몬스멕타™ 헤파맥스"),
        "urinary": ("03_몬스멕타_레날디톡스", "몬스멕타™ 레날디톡스"),
        "cancercare": ("04_몬스멕타_캔서케어", "몬스멕타™ 캔서케어"),
        "coldzero": ("05_몬스멕타_콜드제로", "몬스멕타™ 콜드제로"),
        "skincare": ("06_몬스멕타_스킨케어", "몬스멕타™ 스킨케어"),
        "heartcare": ("07_몬스멕타_하트케어", "몬스멕타™ 하트케어"),
        "jointcare": ("08_몬스멕타_조인트케어", "몬스멕타™ 조인트케어"),
        "powerase": ("09_몬스멕타_파워에이스", "몬스멕타™ 파워에이스"),
        "probiotics": ("10_몬스멕타_프로바이오틱스", "몬스멕타™ 프로바이오틱스"),
        "vitaplus": ("11_몬스멕타_비타플러스", "몬스멕타™ 비타플러스"),
    }

    for p in PRODUCTS:
        pid = p["id"]
        if pid in PREFIX_MAP:
            pfx, tko = PREFIX_MAP[pid]
            html_name = f"{pfx}_100ml_좌7_중간7_우3mm.html"
            html_content = generate_100ml_variant_html(p, tko)
            html_path = os.path.join(out_dir, html_name)
            desktop_html = os.path.join(desktop_100ml_dir, html_name)
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(html_content)
            with open(desktop_html, "w", encoding="utf-8") as f:
                f.write(html_content)
            items.append({
                "prod": p,
                "prefix": pfx,
                "title_ko": tko,
                "html_path": html_path,
                "html_name": html_name
            })
            print(f"[{tko}] Saved HTML: {html_name}")

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 950})

        for item in items:
            pfx = item["prefix"]
            tko = item["title_ko"]
            pid = item["prod"]["id"]
            html_path = item["html_path"]

            file_url = f"file:///{os.path.abspath(html_path).replace(os.sep, '/')}"
            page.goto(file_url)

            # (1) A4 실측 인쇄용 PDF (총 123x75mm 실측 + 50mm 자 + 코너 재단선)
            pdf_a4_name = f"{pfx}_100ml_테스트_좌7_중간7_우3mm(1구_A4실측).pdf"
            pdf_a4_path = os.path.join(out_dir, pdf_a4_name)
            desktop_pdf_a4 = os.path.join(desktop_100ml_dir, pdf_a4_name)

            page.evaluate("() => { setPaperMode('a4'); setViewMode('white'); }")
            page.wait_for_timeout(350)
            page.emulate_media(media="print")
            page.wait_for_timeout(150)

            temp_a4 = os.path.join(out_dir, f"temp_{pid}_100ml_a4_wing.pdf")
            page.pdf(
                path=temp_a4,
                format="A4",
                print_background=True,
                margin={"top": "8mm", "bottom": "0", "left": "0", "right": "0"}
            )
            safe_copy(temp_a4, pdf_a4_path)
            safe_copy(temp_a4, desktop_pdf_a4)

            # (2) 123x75mm 순수 롤 라벨 PDF
            pdf_roll_name = f"{pfx}_100ml_테스트_좌7_중간7_우3mm(롤라벨_123x75mm).pdf"
            pdf_roll_path = os.path.join(out_dir, pdf_roll_name)
            desktop_pdf_roll = os.path.join(desktop_100ml_dir, pdf_roll_name)

            page.evaluate("() => { setPaperMode('roll'); }")
            page.wait_for_timeout(300)

            temp_roll = os.path.join(out_dir, f"temp_{pid}_100ml_roll_wing.pdf")
            page.pdf(
                path=temp_roll,
                width="123mm",
                height="75mm",
                print_background=True,
                margin={"top": "0", "bottom": "0", "left": "0", "right": "0"}
            )
            safe_copy(temp_roll, pdf_roll_path)
            safe_copy(temp_roll, desktop_pdf_roll)

            try:
                if os.path.exists(temp_a4): os.remove(temp_a4)
                if os.path.exists(temp_roll): os.remove(temp_roll)
            except:
                pass

            print(f"[{tko}] Generated 100ml Wing PDFs: {pdf_a4_name}")

        browser.close()

    # Generate preview for Monsmecta 100ml
    doc0 = pymupdf.open(os.path.join(out_dir, "01_몬스멕타_100ml_테스트_좌7_중간7_우3mm(1구_A4실측).pdf"))
    pix0 = doc0[0].get_pixmap(dpi=150)
    prev_path = os.path.join(brain_dir, "preview_100ml_with_wings.png")
    pix0.save(prev_path)
    print("Saved preview:", prev_path)

    print("=== [100ml 전체 11종 좌7+중7+우3mm 접착형 일괄 생성 완료] ===")

if __name__ == "__main__":
    main()

