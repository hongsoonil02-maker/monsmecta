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
from rebuild_all_30ml_labels_with_a4_scale import render_unified_30ml_label_html

out_dir = r"c:\Users\master\monsmecta_landing\public\assets\labels"
desktop_dir = r"C:\Users\master\Desktop\몬스멕타_인쇄소전달용_85x40mm"
brain_dir = r"C:\Users\master\.gemini\antigravity\brain\cacb210e-6377-4186-9128-20025d75e8f6"
os.makedirs(out_dir, exist_ok=True)
os.makedirs(desktop_dir, exist_ok=True)

def generate_variant_html():
    prod = PRODUCTS[0] # monsmecta
    base_html = render_unified_30ml_label_html(prod)

    # 1. Custom CSS for 101mm x 42mm sticker (7mm left wing + 39.5mm front + 7mm center gap + 44.5mm right + 3mm right wing)
    custom_css = """<style>
        /* 101mm x 42mm Test Sticker Style (좌 7mm + 중 7mm + 우 3mm, 세로 42mm 여유형) */
        .crop-marks-box {
            width: 101mm !important;
            height: 42mm !important;
        }

        .sticker-wing-container {
            display: flex !important;
            flex-direction: row !important;
            align-items: stretch !important;
            width: 101mm !important;
            height: 42mm !important;
            background: #ffffff !important;
            border: 0.20mm solid #cbd5e1 !important;
            box-sizing: border-box !important;
            margin: 0 auto !important;
            position: relative !important;
        }

        /* 좌측 7mm 접착 날개 */
        .adhesive-wing-left {
            width: 7.0mm !important;
            height: 100% !important;
            background: #ffffff !important;
            flex-shrink: 0 !important;
            box-sizing: border-box !important;
            position: relative !important;
            z-index: 10 !important;
            border-right: 0.15mm dashed #cbd5e1 !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
        }
        .wing-text-left {
            writing-mode: vertical-rl !important;
            text-orientation: mixed !important;
            font-size: 1.4mm !important;
            color: #94a3b8 !important;
            font-weight: 800 !important;
            letter-spacing: 0.5mm !important;
            opacity: 0.7 !important;
            user-select: none !important;
            white-space: nowrap !important;
        }

        /* 우측 3mm 접착 날개 */
        .adhesive-wing-right {
            width: 3.0mm !important;
            height: 100% !important;
            background: #ffffff !important;
            flex-shrink: 0 !important;
            box-sizing: border-box !important;
            position: relative !important;
            z-index: 10 !important;
            border-left: 0.15mm dashed #cbd5e1 !important;
        }

        .sticker-wing-container .label-sheet,
        body.paper-a4 #card-white .label-sheet,
        body.paper-a4 #card-dark .label-sheet {
            width: 91.0mm !important;
            max-width: 91.0mm !important;
            min-width: 91.0mm !important;
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
        }

        /* 상단 및 하단 연두색 네온 액센트 바 (각 0.45mm 완벽 일치) */
        .top-accent-bar,
        .bottom-accent-bar {
            height: 0.45mm !important;
            min-height: 0.45mm !important;
            background: linear-gradient(90deg, #059669, #10b981, #6ee7b7, #059669) !important;
            box-shadow: 0 0 1.2mm #10b981E6 !important;
            z-index: 10 !important;
            flex-shrink: 0 !important;
            width: 100% !important;
        }

        .sticker-wing-container .content-wrap {
            width: 91.0mm !important;
            flex: 1 1 auto !important;
            height: calc(100% - 0.90mm) !important;
            padding: 0 !important;
            display: flex !important;
            flex-direction: row !important;
            justify-content: flex-start !important;
            box-sizing: border-box !important;
            overflow: hidden !important;
        }

        /* 좌측 전면 메인: 39.5mm (상하 넉넉한 여백 + 좌우 0.18mm 네온선 프레임) */
        .col-left {
            width: 39.5mm !important;
            height: 100% !important;
            padding: 0.60mm 0.30mm 0.60mm 0.30mm !important;
            box-sizing: border-box !important;
            position: relative !important;
            flex-shrink: 0 !important;
            border-left: 0.18mm solid #10b981 !important;
            border-right: 0.18mm solid #10b981 !important;
            display: flex !important;
            flex-direction: column !important;
            justify-content: space-between !important;
        }

        .col-left .brand-badge {
            margin-top: 0.20mm !important;
        }
        .col-left .hero-section {
            margin-top: 0.15mm !important;
            margin-bottom: 0.15mm !important;
        }
        .col-left .core-effects-box {
            margin-top: -0.60mm !important;
            margin-bottom: 0.50mm !important;
            padding-top: 1.70mm !important;   /* 핵심효능 박스 내부 텍스트 상하 완벽 정중앙 배치 */
            padding-bottom: 0.55mm !important;
        }
        .effects-row:not(:last-child) {
            margin-bottom: 0.22mm !important;
        }
        .col-left .tech-box-ing {
            margin-top: 0.20mm !important;
            margin-bottom: 0.30mm !important;
        }
        .col-left .col-left-bottom-bar {
            margin-bottom: 0.20mm !important;
        }

        /* 중앙 7mm 분리 접착 공간 */
        .center-gap-7mm {
            width: 7.0mm !important;
            height: 100% !important;
            background: #ffffff !important;
            flex-shrink: 0 !important;
            display: flex !important;
            flex-direction: column !important;
            align-items: center !important;
            justify-content: center !important;
            border-right: 0.18mm solid #cbd5e1 !important;
            box-sizing: border-box !important;
            position: relative !important;
            z-index: 5 !important;
        }
        .center-gap-text {
            writing-mode: vertical-rl !important;
            text-orientation: mixed !important;
            font-size: 1.4mm !important;
            color: #94a3b8 !important;
            font-weight: 800 !important;
            letter-spacing: 0.5mm !important;
            opacity: 0.7 !important;
            user-select: none !important;
            white-space: nowrap !important;
        }

        /* 우측 법정 패널: 44.5mm (상하 넉넉한 여백) */
        .col-right {
            width: 44.5mm !important;
            height: 100% !important;
            padding: 0.40mm 0.30mm 0.40mm 0.30mm !important;
            box-sizing: border-box !important;
            position: relative !important;
            flex-shrink: 0 !important;
        }

        #card-white .legal-panel {
            height: 100% !important;
            box-sizing: border-box !important;
            padding: 0.35mm 0.50mm 0.35mm 0.50mm !important;
            display: flex !important;
            flex-direction: column !important;
            justify-content: space-between !important;
        }

        /* ========================================================
           [수정 포인트 1] 하단 S&J VET FORMULA 바 내부 글씨 상하 정중앙 정렬
           ======================================================== */
        .col-left-bottom-bar,
        #card-white .col-left-bottom-bar,
        #card-dark .col-left-bottom-bar {
            display: flex !important;
            align-items: center !important;
            justify-content: space-between !important;
            height: 2.50mm !important;
            min-height: 2.50mm !important;
            max-height: 2.50mm !important;
            padding: 0 0.80mm !important;
            box-sizing: border-box !important;
            line-height: 1 !important;
        }
        .left-btm-brand {
            display: inline-flex !important;
            align-items: center !important;
            line-height: 1 !important;
            font-size: 1.02mm !important;
            transform: translateY(0.12mm) !important; /* 상하 완벽한 시각적 중심 보정 */
        }
        .left-btm-brand strong {
            line-height: 1 !important;
        }
        .left-btm-target {
            display: inline-flex !important;
            align-items: center !important;
            justify-content: center !important;
            height: 1.80mm !important;
            padding: 0 0.70mm !important;
            line-height: 1 !important;
            font-size: 0.98mm !important;
            box-sizing: border-box !important;
            transform: translateY(0.06mm) !important; /* 상하 완벽한 시각적 중심 보정 */
        }

        /* ========================================================
           [수정 포인트 2] 상표등록 번호 상단 점선과 시원한 간격 확보 및 정렬
           ======================================================== */
        .tm-dual-grid,
        #card-white .tm-dual-grid,
        #card-dark .tm-dual-grid {
            display: flex !important;
            flex-direction: column !important;
            gap: 0.28mm !important;
            border-top: 0.18mm dashed #94a3b8 !important;
            padding-top: 0.75mm !important;   /* 점선 아래로 충분한 여백 확보 (기존 0.10mm -> 0.75mm) */
            padding-bottom: 0.35mm !important;
            margin-top: 0.50mm !important;   /* 상단 성분등록번호와의 간격 */
            margin-bottom: 0.40mm !important;
            box-sizing: border-box !important;
        }
        .tm-line {
            display: flex !important;
            justify-content: space-between !important;
            align-items: center !important;
            font-size: 0.96mm !important;
            line-height: 1.15 !important;
        }

        /* ========================================================
           [수정 포인트 3] 용법 및 용량 박스 내부 글씨 상하 정중앙 정렬
           ======================================================== */
        .dose-box-single,
        #card-white .dose-box-single,
        #card-dark .dose-box-single {
            display: flex !important;
            align-items: center !important;
            justify-content: flex-start !important;
            height: 2.70mm !important;
            min-height: 2.70mm !important;
            max-height: 2.70mm !important;
            padding: 0 0.80mm !important;
            box-sizing: border-box !important;
            gap: 0.35mm !important;
            margin-top: 0.40mm !important;
            margin-bottom: 0.40mm !important;
        }
        .dose-box-single .title,
        .dose-box-single .desc,
        .dose-box-single .sub {
            display: inline-flex !important;
            align-items: center !important;
            line-height: 1 !important;
            margin: 0 !important;
            padding: 0 !important;
            transform: translateY(0.12mm) !important; /* 상하 완벽한 시각적 중심 보정 */
        }

        @media screen {
            .sticker-wing-container {
                box-shadow: 0 25px 60px rgba(0, 0, 0, 0.95) !important;
                transform: scale(2.0) !important;
                transform-origin: top center !important;
                margin-bottom: 45mm !important;
            }
        }

        @media print {
            body.paper-a4 .crop-marks-box {
                width: 101mm !important;
                height: 42mm !important;
            }
            body.paper-roll,
            body.paper-roll .labels-stage,
            body.paper-roll .crop-marks-box {
                width: 101mm !important;
                height: 42mm !important;
            }
            .sticker-wing-container {
                width: 101mm !important;
                height: 42mm !important;
                transform: none !important;
                box-shadow: none !important;
                margin: 0 auto !important;
            }
            .sticker-wing-container .label-sheet,
            body.paper-a4 #card-white .label-sheet,
            body.paper-a4 #card-dark .label-sheet {
                border: none !important;
                width: 91mm !important;
                max-width: 91mm !important;
                min-width: 91mm !important;
                height: 100% !important;
                max-height: 100% !important;
            }
        }
    </style></head>"""

    html = base_html.replace("</head>", custom_css, 1)

    # 2. Update divider column to center 7mm adhesive gap
    old_divider = """                    <!-- CENTER DIVIDER -->
                    <div class="divider-col">
                        <div class="divider-line"></div>
                        <div class="divider-diamond"></div>
                    </div>"""
    new_divider = """                    <!-- CENTER 7mm ADHESIVE GAP -->
                    <div class="center-gap-7mm">
                        <div class="center-gap-text">접착여백 7mm</div>
                    </div>"""
    html = html.replace(old_divider, new_divider)

    # 3. Wrap .label-sheet in .sticker-wing-container with left 7mm and right 3mm wings
    html = html.replace(
        '<div class="label-sheet">',
        '<div class="sticker-wing-container"><div class="adhesive-wing-left"><div class="wing-text-left">접착 7mm</div></div><div class="label-sheet">'
    )
    # Target closing: insert bottom-accent-bar and close sticker-wing-container
    target_close = """                    </div>
                </div>
            </div>
        </div>
    </div>"""
    replacement_close = """                    </div>
                </div>
                <div class="bottom-accent-bar"></div>
            </div><div class="adhesive-wing-right"></div></div>
        </div>
    </div>"""
    html = html.replace(target_close, replacement_close)

    # 4. Update texts and page size
    html = html.replace(
        "용기 라벨 (85mm × 40mm)",
        "용기 라벨 [실물 테스트형] (좌측 7mm + 중간 7mm + 우측 3mm 접착 = 총 101×42mm)"
    )
    html = html.replace(
        "정확히 <strong>85mm × 40mm 정품 라벨</strong>이 완성됩니다.",
        "좌측 7mm, 중간 7mm, 우측 3mm 접착 여백이 포함된 <strong>총 101mm × 42mm 실측 스티커</strong>가 완성됩니다."
    )
    html = html.replace("@page { size: 85mm 40mm; margin: 0; }", "@page { size: 101mm 42mm; margin: 0; }")

    return html

def safe_copy(src, dst):
    try:
        shutil.copyfile(src, dst)
        return dst
    except PermissionError:
        base, ext = os.path.splitext(dst)
        fallback = f"{base}_수정본{ext}"
        shutil.copyfile(src, fallback)
        print(f"Warning: {dst} locked, saved as fallback: {fallback}")
        return fallback

def main():
    html_content = generate_variant_html()
    variant_html_path = os.path.join(out_dir, "monsmecta_original_30ml_left7_mid7_right3mm.html")
    with open(variant_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Saved clean variant HTML:", variant_html_path)

    temp_1up = os.path.join(out_dir, "temp_1up.pdf")
    temp_3up = os.path.join(out_dir, "temp_3up.pdf")

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        url = "file:///" + variant_html_path.replace("\\", "/") + "?mode=white&paper=a4"

        # 1-up A4 PDF
        page = browser.new_page(viewport={"width": 1280, "height": 950})
        page.goto(url)
        page.evaluate("() => { document.body.className = 'paper-a4 print-white'; }")
        page.wait_for_timeout(400)
        page.emulate_media(media="print")
        page.wait_for_timeout(200)

        page.pdf(
            path=temp_1up,
            format="A4",
            print_background=True,
            margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"}
        )
        page.close()

        pdf_1up_name = "01_몬스멕타_30ml_테스트_좌7_중간7_우3mm(1구_A4실측).pdf"
        target_1up = os.path.join(out_dir, pdf_1up_name)
        safe_1up = safe_copy(temp_1up, target_1up)
        safe_copy(temp_1up, os.path.join(desktop_dir, pdf_1up_name))
        print("Generated 1-up PDF:", safe_1up)

        # 3-up A4 PDF
        page3 = browser.new_page(viewport={"width": 1280, "height": 1200})
        page3.goto(url)
        page3.wait_for_timeout(400)
        page3.evaluate("""() => {
            document.body.className = 'paper-a4 print-white';
            const titleEl = document.querySelector('.a4-calibration-header > div:first-child');
            if (titleEl) {
                titleEl.textContent = '[30ml 실물 테스트용] 몬스멕타™ 3구 실측 라벨 (좌측 7mm + 중간 7mm + 우측 3mm 접착 = 총 101×42mm × 3개)';
            }
            const cardWhite = document.getElementById('card-white');
            if (!cardWhite) return;
            const originalCropBox = cardWhite.querySelector('.crop-marks-box');
            if (!originalCropBox) return;

            const container = document.createElement('div');
            container.className = 'multi-label-print-container';
            container.style.display = 'flex';
            container.style.flexDirection = 'column';
            container.style.alignItems = 'center';
            container.style.gap = '12mm';
            container.style.marginTop = '2mm';
            container.style.width = '100%';

            for (let i = 1; i <= 3; i++) {
                const clone = originalCropBox.cloneNode(true);
                clone.style.margin = '0 auto';

                const numTag = document.createElement('div');
                numTag.style.textAlign = 'center';
                numTag.style.fontSize = '7.5pt';
                numTag.style.fontWeight = '700';
                numTag.style.color = '#64748b';
                numTag.style.marginBottom = '2mm';
                numTag.textContent = '▼ 테스트 라벨 #' + i + ' (좌측 7mm + 중간 7mm + 우측 3mm 접착 = 총 101×42mm)';

                const wrapper = document.createElement('div');
                wrapper.style.display = 'flex';
                wrapper.style.flexDirection = 'column';
                wrapper.style.alignItems = 'center';
                wrapper.appendChild(numTag);
                wrapper.appendChild(clone);
                container.appendChild(wrapper);
            }

            originalCropBox.parentNode.replaceChild(container, originalCropBox);

            const header = document.querySelector('.a4-calibration-header');
            if (header) {
                header.style.marginBottom = '4mm';
                header.style.paddingTop = '2mm';
            }
        }""")
        page3.wait_for_timeout(300)
        page3.emulate_media(media="print")
        page3.wait_for_timeout(200)

        page3.pdf(
            path=temp_3up,
            format="A4",
            print_background=True,
            margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"}
        )
        page3.close()

        pdf_3up_name = "01_몬스멕타_30ml_테스트_좌7_중간7_우3mm(3구_A4실측).pdf"
        target_3up = os.path.join(out_dir, pdf_3up_name)
        safe_3up = safe_copy(temp_3up, target_3up)
        safe_copy(temp_3up, os.path.join(desktop_dir, pdf_3up_name))
        print("Generated 3-up PDF:", safe_3up)

        browser.close()

    # Clean up temp pdfs if possible
    try:
        if os.path.exists(temp_1up): os.remove(temp_1up)
        if os.path.exists(temp_3up): os.remove(temp_3up)
    except:
        pass

    # Render preview PNGs via PyMuPDF (DPI 250 for crisp inspection)
    doc_1up = pymupdf.open(safe_1up)
    page_0 = doc_1up[0]
    pix_1up = page_0.get_pixmap(dpi=250)
    prev_1up = os.path.join(brain_dir, "preview_left7_mid7_right3mm_1up.png")
    pix_1up.save(prev_1up)
    print("Saved preview 1up:", prev_1up)

    # Also render full 3up preview
    doc_3up = pymupdf.open(safe_3up)
    pix_3up = doc_3up[0].get_pixmap(dpi=150)
    prev_3up = os.path.join(brain_dir, "preview_left7_mid7_right3mm_3up.png")
    pix_3up.save(prev_3up)
    print("Saved preview 3up:", prev_3up)

if __name__ == "__main__":
    main()
