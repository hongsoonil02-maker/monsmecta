# -*- coding: utf-8 -*-
"""
Generate a comparison prototype for 30ml Monsmecta label:
- Left outer wing: 3mm
- Left front panel: 39.5mm x 40mm
- Center blank adhesive gap: 10mm
- Right legal panel: 44.5mm x 40mm
- Right outer wing: 3mm
Total sticker width: 100mm x 40mm
"""
import os
import sys
import shutil
import re
from playwright.sync_api import sync_playwright

scripts_dir = r"c:\Users\master\monsmecta_landing\scripts"
if scripts_dir not in sys.path:
    sys.path.insert(0, scripts_dir)

from generate_all_30ml_labels import PRODUCTS
from rebuild_all_30ml_labels_with_a4_scale import render_unified_30ml_label_html

out_dir = r"c:\Users\master\monsmecta_landing\public\assets\labels"
desktop_dir = r"C:\Users\master\Desktop\몬스멕타_인쇄소전달용_85x40mm"
os.makedirs(out_dir, exist_ok=True)
os.makedirs(desktop_dir, exist_ok=True)

def generate_variant_html():
    prod = next(x for x in PRODUCTS if x["id"] == "monsmecta")
    base_html = render_unified_30ml_label_html(prod)

    # 1. Inject custom CSS for 100x40mm sticker (3mm left + 94mm body + 3mm right)
    custom_css = """<style>
        /* --- [비교 테스트용 규격] 중앙 10mm 분리 여백 + 좌우 3mm 접착 날개 (총 100mm x 40mm) --- */
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
            border: 0.20mm solid #94a3b8 !important;
            box-sizing: border-box !important;
            margin: 0 auto !important;
        }

        .adhesive-wing-3mm {
            width: 3mm !important;
            height: 100% !important;
            background: #ffffff !important;
            flex-shrink: 0 !important;
            position: relative !important;
        }
        .wing-3mm-left {
            border-right: 0.12mm dashed #cbd5e1 !important;
        }
        .wing-3mm-right {
            border-left: 0.12mm dashed #cbd5e1 !important;
        }

        .sticker-wing-container .label-sheet {
            width: 94mm !important;
            height: 100% !important;
            margin: 0 !important;
            border: none !important;
            transform: none !important;
            box-shadow: none !important;
            background: transparent !important;
            display: flex !important;
            flex-direction: row !important;
            overflow: hidden !important;
        }

        .sticker-wing-container .content-wrap {
            width: 94mm !important;
            height: 100% !important;
            padding: 0 !important;
            display: flex !important;
            flex-direction: row !important;
            justify-content: flex-start !important;
        }

        /* 좌측 전면 메인 (39.5mm) */
        .col-left-wrap {
            width: 39.5mm !important;
            height: 100% !important;
            position: relative !important;
            flex-shrink: 0 !important;
            overflow: hidden !important;
            background: #09090b !important;
            border-right: 0.15mm solid #10b981 !important;
            box-sizing: border-box !important;
        }
        .col-left-wrap .col-left {
            width: 100% !important;
            height: 100% !important;
            padding: 0.20mm 0.30mm !important;
            box-sizing: border-box !important;
            position: relative !important;
            z-index: 2 !important;
        }

        /* 중앙 10mm 접착 여백 */
        .center-gap-10mm {
            width: 10mm !important;
            height: 100% !important;
            background: #ffffff !important;
            flex-shrink: 0 !important;
            display: flex !important;
            flex-direction: column !important;
            align-items: center !important;
            justify-content: center !important;
            border-right: 0.15mm solid #cbd5e1 !important;
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
            letter-spacing: 0.6mm !important;
            opacity: 0.7 !important;
            user-select: none !important;
            white-space: nowrap !important;
        }

        /* 우측 법정 패널 (44.5mm) */
        .col-right-wrap {
            width: 44.5mm !important;
            height: 100% !important;
            position: relative !important;
            flex-shrink: 0 !important;
            overflow: hidden !important;
            box-sizing: border-box !important;
        }
        #card-white .col-right-wrap {
            background: #ffffff !important;
        }
        #card-dark .col-right-wrap {
            background: #09090b !important;
        }
        .col-right-wrap .col-right {
            width: 100% !important;
            height: 100% !important;
            padding: 0.20mm 0.30mm !important;
            box-sizing: border-box !important;
            position: relative !important;
            z-index: 2 !important;
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
                transform: none !important;
                box-shadow: none !important;
                margin: 0 auto !important;
            }
        }
    </style></head>"""

    html = base_html.replace("</head>", custom_css, 1)

    # 2. Update cut instruction and headers
    html = html.replace(
        "용기 라벨 (85mm × 40mm)",
        "용기 라벨 [테스트형] (중앙 10mm 분리여백 + 좌우 3mm 접착날개 = 총 100×40mm)"
    )
    html = html.replace(
        "정확히 <strong>85mm × 40mm 정품 라벨</strong>이 완성됩니다.",
        "중앙 <strong>10mm 분리 접착여백과 좌우 3mm 날개가 포함된 100mm × 40mm</strong> 스티커가 완성됩니다."
    )
    html = html.replace("@page { size: 85mm 40mm; margin: 0; }", "@page { size: 100mm 40mm; margin: 0; }")

    # 3. Replace card structure
    # Match card-dark and card-white
    def transform_card(card_html):
        # col-left
        c = card_html.replace(
            '<div class="col-left">',
            '<div class="col-left-wrap"><div class="grid-overlay"></div><div class="top-accent-bar"></div><div class="col-left">'
        )
        # divider replacement
        c = re.sub(
            r'</div>\s*<!-- CENTER DIVIDER -->\s*<div class="divider-col">.*?</div>\s*<!-- RIGHT COLUMN[^>]*-->\s*<div class="col-right">',
            '</div></div><!-- 10mm CENTER GAP --><div class="center-gap-10mm"><div class="center-gap-text">접착여백 10mm</div></div><!-- RIGHT COLUMN --><div class="col-right-wrap"><div class="col-right">',
            c,
            flags=re.DOTALL
        )
        # close col-right
        c = re.sub(
            r'(<div class="col-right-wrap"><div class="col-right">.*?</div>\s*</div>\s*</div>\s*</div>\s*</div>)',
            lambda m: m.group(0).replace('</div>\n                </div>\n            </div>', '</div></div></div></div>'),
            c,
            flags=re.DOTALL
        )
        # Wrap .label-sheet in .sticker-wing-container
        c = c.replace(
            '<div class="label-sheet">',
            '<div class="sticker-wing-container"><div class="adhesive-wing-3mm wing-3mm-left"></div><div class="label-sheet">'
        )
        # Close .sticker-wing-container
        c = c.replace(
            '</div>\n        </div>\n    </div>',
            '<div class="adhesive-wing-3mm wing-3mm-right"></div></div>\n        </div>\n    </div>'
        )
        return c

    # Apply to whole document
    html = transform_card(html)

    return html

def main():
    html_content = generate_variant_html()
    variant_html_path = os.path.join(out_dir, "monsmecta_original_30ml_center10mm_wing3mm.html")
    with open(variant_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Saved variant HTML:", variant_html_path)

    # Render A4 1-up and 3-up PDFs and screenshots
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

        # Copy 1-up to Desktop
        shutil.copyfile(target_1up, os.path.join(desktop_dir, pdf_1up_name))

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

        # Copy 3-up to Desktop
        shutil.copyfile(target_3up, os.path.join(desktop_dir, pdf_3up_name))

        browser.close()

    # Use pymupdf to render high-res PNG previews directly from the PDF
    import pymupdf
    # 3-up A4 preview
    doc_3up = pymupdf.open(target_3up)
    pix_3up = doc_3up[0].get_pixmap(dpi=150)
    preview_3up_path = r"C:\Users\master\.gemini\antigravity\brain\cacb210e-6377-4186-9128-20025d75e8f6\preview_center10mm_wing3mm_3up.png"
    pix_3up.save(preview_3up_path)

    # 1-up sticker zoom preview
    doc_1up = pymupdf.open(target_1up)
    # A4 is 595.28 x 841.89 points. In 1-up, the sticker is roughly in upper-middle area.
    pix_1up = doc_1up[0].get_pixmap(dpi=300)
    preview_1up_path = r"C:\Users\master\.gemini\antigravity\brain\cacb210e-6377-4186-9128-20025d75e8f6\preview_center10mm_wing3mm_1up.png"
    pix_1up.save(preview_1up_path)

    print("Rendered PNG previews via PyMuPDF successfully.")
    print("Successfully generated center 10mm + outer 3mm test variant!")

if __name__ == "__main__":
    main()
