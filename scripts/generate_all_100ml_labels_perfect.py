# -*- coding: utf-8 -*-
import os
import sys
import shutil
from playwright.sync_api import sync_playwright
import pymupdf

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

def render_perfect_100ml_html(prod):
    base_html = render_tight_100ml_label_html(prod)
    neon = prod.get("neon", "#10b981")
    top_bar = prod.get("top_bar", f"linear-gradient(90deg, {neon}, #ffffff, {neon})")

    # 1. Add bottom-accent-bar to HTML closing
    base_html = base_html.replace(
        """                </div>
            </div>
        </div>
    </div>""",
        """                </div>
                <div class="bottom-accent-bar"></div>
            </div>
        </div>
    </div>"""
    )

    # 2. Perfect Visual Alignment CSS for 100ml (110x75mm)
    custom_css = f"""<style>
        /* 상하 대칭 테마 네온 액센트 바 (각 0.50mm) */
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

        .content-wrap {{
            height: calc(75mm - 1.00mm) !important;
        }}

        /* 1. 핵심 효능 박스 내부 텍스트 상하 완벽 정중앙 */
        .core-effects-box {{
            padding-top: 2.10mm !important;   /* 배지 아래 글씨 상하 정중앙 배치 */
            padding-bottom: 0.90mm !important;
            margin-top: 0.8mm !important;
            margin-bottom: 2.2mm !important;
        }}
        .effects-row:not(:last-child) {{
            margin-bottom: 0.45mm !important;
        }}

        /* 2. 좌측 하단 브랜드 바 내부 텍스트 상하 완벽 정중앙 */
        .col-left-bottom-bar {{
            display: flex !important;
            align-items: center !important;
            justify-content: space-between !important;
            height: 3.80mm !important;
            min-height: 3.80mm !important;
            max-height: 3.80mm !important;
            padding: 0 1.30mm !important;
            box-sizing: border-box !important;
            line-height: 1 !important;
            margin-bottom: 1.2mm !important;
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

        /* 3. 우측 상단 상표출원 번호 상단 점선과 시원한 간격 확보 */
        .tm-dual-grid {{
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

        /* 4. 우측 중단 용법 및 용량 박스 내부 글씨 상하 정중앙 */
        .dose-box-single {{
            display: flex !important;
            align-items: center !important;
            justify-content: flex-start !important;
            height: 4.20mm !important;
            min-height: 4.20mm !important;
            max-height: 4.20mm !important;
            padding: 0 1.20mm !important;
            box-sizing: border-box !important;
            gap: 0.60mm !important;
            margin: 0.40mm 0 !important;
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
    </style></head>"""

    base_html = base_html.replace("</head>", custom_css, 1)
    return base_html

def build_all_100ml():
    print(f"=== [100ml 전체 11종 라인업 (110mm x 75mm) 일괄 생성 시작 ({len(PRODUCTS)}종)] ===")

    html_tasks = []
    for idx, p in enumerate(PRODUCTS):
        prefix = f"{idx+1:02d}"
        clean_name = p["name_ko"].replace(" ", "_")
        html_filename = f"{prefix}_{clean_name}_100ml_라벨.html"
        html_path = os.path.join(out_dir, html_filename)
        desktop_html = os.path.join(desktop_100ml_dir, html_filename)

        content = render_perfect_100ml_html(p)
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(content)
        with open(desktop_html, "w", encoding="utf-8") as f:
            f.write(content)

        # Update legacy aliases
        pid = p["id"]
        alias_names = [
            f"{pid}_label_print.html",
            f"{pid}_label_print_white.html",
            "monsmecta_original_white_label.html" if pid == "monsmecta" else ("monsmecta_renal_white_label.html" if pid == "urinary" else f"monsmecta_{pid}_white_label.html")
        ]
        for alias in set(alias_names):
            with open(os.path.join(out_dir, alias), "w", encoding="utf-8") as f:
                f.write(content)

        html_tasks.append((prefix, clean_name, pid, html_path))
        print(f"[{prefix}/11] HTML saved: {html_filename}")

    # Playwright PDF rendering
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 950})

        for prefix, clean_name, pid, html_path in html_tasks:
            file_url = f"file:///{os.path.abspath(html_path).replace(os.sep, '/')}"
            page.goto(file_url)

            # (1) A4 실측 인쇄용 PDF (110x75mm 실측 + 50mm 자 + 코너 재단선)
            pdf_a4_name = f"{prefix}_{clean_name}_100ml_정품_A4실측인쇄(110x75mm).pdf"
            pdf_a4_path = os.path.join(out_dir, pdf_a4_name)
            desktop_pdf_a4 = os.path.join(desktop_100ml_dir, pdf_a4_name)

            page.evaluate("() => { setPaperMode('a4'); setViewMode('white'); }")
            page.wait_for_timeout(350)
            page.emulate_media(media="print")
            page.wait_for_timeout(150)

            temp_a4 = os.path.join(out_dir, f"temp_{pid}_100ml_a4.pdf")
            page.pdf(
                path=temp_a4,
                format="A4",
                print_background=True,
                margin={"top": "8mm", "bottom": "0", "left": "0", "right": "0"}
            )
            safe_copy(temp_a4, pdf_a4_path)
            safe_copy(temp_a4, desktop_pdf_a4)

            # (2) 110x75mm 순수 롤 라벨 PDF
            pdf_roll_name = f"{prefix}_{clean_name}_100ml_롤라벨(110x75mm).pdf"
            pdf_roll_path = os.path.join(out_dir, pdf_roll_name)
            desktop_pdf_roll = os.path.join(desktop_100ml_dir, pdf_roll_name)

            page.evaluate("() => { setPaperMode('roll'); }")
            page.wait_for_timeout(300)

            temp_roll = os.path.join(out_dir, f"temp_{pid}_100ml_roll.pdf")
            page.pdf(
                path=temp_roll,
                width="110mm",
                height="75mm",
                print_background=True,
                margin={"top": "0", "bottom": "0", "left": "0", "right": "0"}
            )
            safe_copy(temp_roll, pdf_roll_path)
            safe_copy(temp_roll, desktop_pdf_roll)

            # Clean up temp files
            try:
                if os.path.exists(temp_a4): os.remove(temp_a4)
                if os.path.exists(temp_roll): os.remove(temp_roll)
            except:
                pass

            print(f"[{prefix}/11] Rendered 100ml PDFs: {pdf_a4_name}")

        browser.close()

    print("=== [100ml 전체 11종 라인업 생성 및 데스크톱 배포 완료] ===")

if __name__ == "__main__":
    build_all_100ml()

