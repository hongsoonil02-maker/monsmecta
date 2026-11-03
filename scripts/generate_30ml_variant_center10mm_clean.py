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

    # 1. Add custom CSS for 100mm sticker (3mm wing + 39.5mm front + 10mm center gap + 44.5mm right + 3mm wing)
    custom_css = """<style>
        /* 100mm x 40mm Test Sticker Style */
        .crop-marks-box {
            width: 100mm !important;
            height: 40mm !important;
        }

        .sticker-wing-container {
            display: flex !important;
            flex-direction: row !important;
            align-items: stretch !important;
            width: 100mm !important;
            height: 40mm !important;
            background: #ffffff !important;
            border: 0.20mm solid #cbd5e1 !important;
            box-sizing: border-box !important;
            margin: 0 auto !important;
            position: relative !important;
            overflow: hidden !important;
        }

        .adhesive-wing-3mm {
            width: 3.0mm !important;
            height: 100% !important;
            background: #ffffff !important;
            flex-shrink: 0 !important;
            box-sizing: border-box !important;
            position: relative !important;
            z-index: 10 !important;
        }
        .wing-3mm-left {
            border-right: 0.15mm dashed #cbd5e1 !important;
        }
        .wing-3mm-right {
            border-left: 0.15mm dashed #cbd5e1 !important;
        }

        .sticker-wing-container .label-sheet,
        body.paper-a4 #card-white .label-sheet,
        body.paper-a4 #card-dark .label-sheet {
            width: 94.0mm !important;
            max-width: 94.0mm !important;
            min-width: 94.0mm !important;
            height: 40.0mm !important;
            max-height: 40.0mm !important;
            margin: 0 !important;
            border: none !important;
            transform: none !important;
            box-shadow: none !important;
            display: flex !important;
            flex-direction: column !important;
            overflow: hidden !important;
            position: relative !important;
        }

        .sticker-wing-container .content-wrap {
            width: 94.0mm !important;
            height: 100% !important;
            padding: 0 !important;
            display: flex !important;
            flex-direction: row !important;
            justify-content: flex-start !important;
        }

        /* 좌측 전면 메인: 39.5mm */
        .col-left {
            width: 39.5mm !important;
            height: 100% !important;
            padding: 0.20mm 0.30mm !important;
            box-sizing: border-box !important;
            position: relative !important;
            flex-shrink: 0 !important;
            border-right: 0.18mm solid #10b981 !important;
        }

        /* 중앙 10mm 분리 접착 공간 */
        .center-gap-10mm {
            width: 10.0mm !important;
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
            font-size: 1.5mm !important;
            color: #94a3b8 !important;
            font-weight: 800 !important;
            letter-spacing: 0.8mm !important;
            opacity: 0.7 !important;
            user-select: none !important;
            white-space: nowrap !important;
        }

        /* 우측 법정 패널: 44.5mm */
        .col-right {
            width: 44.5mm !important;
            height: 100% !important;
            padding: 0.20mm 0.30mm !important;
            box-sizing: border-box !important;
            position: relative !important;
            flex-shrink: 0 !important;
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
                width: 100mm !important;
                height: 40mm !important;
            }
            body.paper-roll,
            body.paper-roll .labels-stage,
            body.paper-roll .crop-marks-box {
                width: 100mm !important;
                height: 40mm !important;
            }
            .sticker-wing-container {
                width: 100mm !important;
                height: 40mm !important;
                transform: none !important;
                box-shadow: none !important;
                margin: 0 auto !important;
            }
            .sticker-wing-container .label-sheet,
            body.paper-a4 #card-white .label-sheet,
            body.paper-a4 #card-dark .label-sheet {
                border: none !important;
                width: 94mm !important;
                max-width: 94mm !important;
                min-width: 94mm !important;
                height: 40mm !important;
            }
        }
    </style></head>"""

    html = base_html.replace("</head>", custom_css, 1)

    # 2. Update divider column to center 10mm adhesive gap
    old_divider = """                    <!-- CENTER DIVIDER -->
                    <div class="divider-col">
                        <div class="divider-line"></div>
                        <div class="divider-diamond"></div>
                    </div>"""
    new_divider = """                    <!-- CENTER 10mm ADHESIVE GAP -->
                    <div class="center-gap-10mm">
                        <div class="center-gap-text">접착여백 10mm</div>
                    </div>"""
    html = html.replace(old_divider, new_divider)

    # 3. Wrap .label-sheet in .sticker-wing-container with left/right 3mm wings
    html = html.replace(
        '<div class="label-sheet">',
        '<div class="sticker-wing-container"><div class="adhesive-wing-3mm wing-3mm-left"></div><div class="label-sheet">'
    )
    # Target closing
    target_close = """                    </div>
                </div>
            </div>
        </div>
    </div>"""
    replacement_close = """                    </div>
                </div>
            </div><div class="adhesive-wing-3mm wing-3mm-right"></div></div>
        </div>
    </div>"""
    html = html.replace(target_close, replacement_close)

    # 4. Update texts and page size
    html = html.replace(
        "용기 라벨 (85mm × 40mm)",
        "용기 라벨 [실물 테스트형] (좌·우 3mm + 중앙 10mm 분리접착 = 총 100×40mm)"
    )
    html = html.replace(
        "정확히 <strong>85mm × 40mm 정품 라벨</strong>이 완성됩니다.",
        "좌우 3mm 및 중앙 10mm 접착 공간이 포함된 <strong>총 100mm × 40mm 실측 스티커</strong>가 완성됩니다."
    )
    html = html.replace("@page { size: 85mm 40mm; margin: 0; }", "@page { size: 100mm 40mm; margin: 0; }")

    return html

def main():
    html_content = generate_variant_html()
    variant_html_path = os.path.join(out_dir, "monsmecta_original_30ml_center10mm_wing3mm.html")
    with open(variant_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Saved clean variant HTML:", variant_html_path)

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

        pdf_1up_name = "01_몬스멕타_30ml_테스트_중앙10mm_좌우3mm(1구_A4실측).pdf"
        target_1up = os.path.join(out_dir, pdf_1up_name)
        page.pdf(
            path=target_1up,
            format="A4",
            print_background=True,
            margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"}
        )
        page.close()
        shutil.copyfile(target_1up, os.path.join(desktop_dir, pdf_1up_name))
        print("Generated 1-up PDF:", target_1up)

        # 3-up A4 PDF
        page3 = browser.new_page(viewport={"width": 1280, "height": 1200})
        page3.goto(url)
        page3.wait_for_timeout(400)
        page3.evaluate("""() => {
            document.body.className = 'paper-a4 print-white';
            const titleEl = document.querySelector('.a4-calibration-header > div:first-child');
            if (titleEl) {
                titleEl.textContent = '[30ml 실물 테스트용] 몬스멕타™ 3구 실측 라벨 (중앙 10mm 분리접착 + 좌·우 3mm 접착날개 = 총 100×40mm × 3개)';
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
            container.style.gap = '14mm';
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
                numTag.textContent = '▼ 테스트 라벨 #' + i + ' (중앙 10mm 접착공간 + 좌·우 3mm 접착날개 = 총 100×40mm)';

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

        pdf_3up_name = "01_몬스멕타_30ml_테스트_중앙10mm_좌우3mm(3구_A4실측).pdf"
        target_3up = os.path.join(out_dir, pdf_3up_name)
        page3.pdf(
            path=target_3up,
            format="A4",
            print_background=True,
            margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"}
        )
        page3.close()
        shutil.copyfile(target_3up, os.path.join(desktop_dir, pdf_3up_name))
        print("Generated 3-up PDF:", target_3up)

        browser.close()

    # Render preview PNGs via PyMuPDF
    doc_1up = pymupdf.open(target_1up)
    pix_1up = doc_1up[0].get_pixmap(dpi=200)
    prev_1up = os.path.join(brain_dir, "preview_center10mm_wing3mm_1up.png")
    pix_1up.save(prev_1up)
    print("Saved preview 1up:", prev_1up)

    doc_3up = pymupdf.open(target_3up)
    pix_3up = doc_3up[0].get_pixmap(dpi=150)
    prev_3up = os.path.join(brain_dir, "preview_center10mm_wing3mm_3up.png")
    pix_3up.save(prev_3up)
    print("Saved preview 3up:", prev_3up)

if __name__ == "__main__":
    main()
