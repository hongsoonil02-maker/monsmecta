# -*- coding: utf-8 -*-
"""
Generate 30ml labels for the 3 main products (몬스멕타, 몬스멕타 헤파맥스, 몬스멕타 레날 디톡스)
with 8mm blank adhesive wings (접착 공간) on both left and right sides:
- Printed center label: 85mm x 40mm (unchanged 1:1 scale)
- Left blank adhesive wing: 8mm x 40mm
- Right blank adhesive wing: 8mm x 40mm
- Total cut sticker dimension: 101mm x 40mm (8mm + 85mm + 8mm)
Generates:
1. Updated HTML files
2. 1-up A4 1:1 scale PDFs
3. 3-up A4 1:1 scale PDFs (3 stickers per A4 sheet)
"""
import os
import sys
import shutil
from playwright.sync_api import sync_playwright
import pypdf

scripts_dir = os.path.dirname(os.path.abspath(__file__))
if scripts_dir not in sys.path:
    sys.path.insert(0, scripts_dir)

from generate_all_30ml_labels import PRODUCTS
from rebuild_all_30ml_labels_with_a4_scale import render_unified_30ml_label_html

out_dir = r"c:\Users\master\monsmecta_landing\public\assets\labels"
desktop_dir = r"C:\Users\master\Desktop\몬스멕타_인쇄소전달용_85x40mm"
os.makedirs(out_dir, exist_ok=True)
os.makedirs(desktop_dir, exist_ok=True)

TARGET_IDS = ["monsmecta", "hepamax", "urinary"]

def inject_8mm_wings_into_html(html_str: str) -> str:
    """
    Transforms the 85x40mm crop-marks-box into a 101x40mm (8mm + 85mm + 8mm)
    sticker container with blank white 8mm adhesive wings on left and right,
    with outer crop marks and subtle outer cutting guideline border.
    """
    wing_css = """<style>
        /* --- 좌우 8mm 접착 날개 (총 101mm x 40mm 스티커 규격) --- */
        .sticker-wing-container {
            display: flex !important;
            flex-direction: row !important;
            align-items: stretch !important;
            width: 101mm !important;
            height: 40mm !important;
            background: #ffffff !important;
            border: 0.20mm solid #94a3b8 !important;
            box-sizing: border-box !important;
            margin: 0 auto !important;
        }
        .adhesive-wing {
            width: 8mm !important;
            height: 100% !important;
            background: #ffffff !important;
            flex-shrink: 0 !important;
        }
        .sticker-wing-container .label-sheet {
            width: 85mm !important;
            height: 100% !important;
            margin: 0 !important;
            border-top: none !important;
            border-bottom: none !important;
            transform: none !important;
            box-shadow: none !important;
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
                height: 40mm !important;
            }
            body.paper-roll,
            body.paper-roll .labels-stage,
            body.paper-roll .crop-marks-box {
                width: 101mm !important;
                height: 40mm !important;
            }
            .sticker-wing-container {
                transform: none !important;
                box-shadow: none !important;
                margin: 0 auto !important;
            }
        }
    </style></head>"""

    html_mod = html_str.replace("</head>", wing_css, 1)

    # Wrap <div class="label-sheet">...</div> inside .sticker-wing-container with left/right 8mm .adhesive-wing
    old_open = '<div class="label-sheet">'
    new_open = '<div class="sticker-wing-container"><div class="adhesive-wing"></div><div class="label-sheet">'
    html_mod = html_mod.replace(old_open, new_open)

    # Close .sticker-wing-container right before </div><!-- end crop-marks-box -->
    target_close = """                    </div>
                </div>
            </div>
        </div>
    </div>"""
    replacement_close = """                    </div>
                </div>
            </div><div class="adhesive-wing"></div></div>
        </div>
    </div>"""
    html_mod = html_mod.replace(target_close, replacement_close)

    # Update header and cut instruction text to mention 8mm adhesive wings (total 101mm x 40mm)
    html_mod = html_mod.replace(
        "용기 라벨 (85mm × 40mm)",
        "용기 라벨 (인쇄 85×40mm + 좌우 접착여백 각 8mm = 총 101×40mm)"
    )
    html_mod = html_mod.replace(
        "정확히 <strong>85mm × 40mm 정품 라벨</strong>이 완성됩니다.",
        "좌우 <strong>8mm 빈 접착 공간이 포함된 101mm × 40mm (중심 라벨 85mm × 40mm)</strong> 스티커가 완성됩니다."
    )
    html_mod = html_mod.replace("@page { size: 85mm 40mm; margin: 0; }", "@page { size: 101mm 40mm; margin: 0; }")

    return html_mod


def main():
    for p in PRODUCTS:
        if p["id"] in TARGET_IDS:
            base_html = render_unified_30ml_label_html(p)
            winged_html = inject_8mm_wings_into_html(base_html)
            html_path = os.path.join(out_dir, p["file_name"])
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(winged_html)
            print(f"Updated HTML with 8mm left/right adhesive wings: {p['file_name']}")

    # Also sync legacy 30ml HTML files for those 3 products
    legacy_map = [
        ("monsmecta_original_30ml_94x45.html", "monsmecta"),
        ("monsmecta_hepamax_30ml_94x45.html", "hepamax"),
        ("monsmecta_renal_30ml_94x45.html", "urinary"),
    ]
    for fname, pid in legacy_map:
        prod = next((x for x in PRODUCTS if x["id"] == pid), None)
        if prod:
            with open(os.path.join(out_dir, fname), "w", encoding="utf-8") as f:
                f.write(inject_8mm_wings_into_html(render_unified_30ml_label_html(prod)))

    # Render 1-up and 3-up A4 PDFs + preview screenshot for the 3 products
    items = [
        ("monsmecta_original_label.html", "01_몬스멕타_30ml_라벨_A4실측인쇄용(85x40mm).pdf", "01_몬스멕타_85x40mm.pdf", "01_몬스멕타_30ml_라벨_A4_3구인쇄(85x40mmx3).pdf", "01_몬스멕타_3구인쇄_85x40mm.pdf", "몬스멕타™"),
        ("monsmecta_hepamax_label.html", "02_몬스멕타_헤파맥스_30ml_라벨_A4실측인쇄용(85x40mm).pdf", "02_몬스멕타_헤파맥스_85x40mm.pdf", "02_몬스멕타_헤파맥스_30ml_라벨_A4_3구인쇄(85x40mmx3).pdf", "02_몬스멕타_헤파맥스_3구인쇄_85x40mm.pdf", "몬스멕타™ 헤파맥스"),
        ("monsmecta_renal_label.html", "03_몬스멕타_레날_디톡스_30ml_라벨_A4실측인쇄용(85x40mm).pdf", "03_몬스멕타_레날디톡스_85x40mm.pdf", "03_몬스멕타_레날_디톡스_30ml_라벨_A4_3구인쇄(85x40mmx3).pdf", "03_몬스멕타_레날디톡스_3구인쇄_85x40mm.pdf", "몬스멕타™ 레날 디톡스"),
    ]

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        for idx, (html_file, a4_1up_name, desk_1up_name, a4_3up_name, desk_3up_name, prod_name) in enumerate(items):
            file_path = os.path.join(out_dir, html_file)
            url = "file:///" + file_path.replace("\\", "/") + "?mode=white&paper=a4"

            # 1) Render 1-up A4 PDF
            page = browser.new_page(viewport={"width": 1280, "height": 950}, device_scale_factor=3)
            page.goto(url)
            page.evaluate("() => { document.body.className = 'paper-a4 print-white'; }")
            page.wait_for_timeout(500)

            if idx == 0:
                # Emulate print media and screenshot the crop-marks-box with surroundings for visual inspection
                page.emulate_media(media="print")
                page.wait_for_timeout(200)
                crop_el = page.query_selector("#card-white .crop-marks-box")
                if crop_el:
                    crop_el.screenshot(path=r"C:\Users\master\.gemini\antigravity\brain\cacb210e-6377-4186-9128-20025d75e8f6\preview_30ml_fixed.png")
                stage_el = page.query_selector(".labels-stage")
                if stage_el:
                    stage_el.screenshot(path=r"C:\Users\master\.gemini\antigravity\brain\cacb210e-6377-4186-9128-20025d75e8f6\preview_30ml_8mm_wings_1up.png")

            target_1up = os.path.join(out_dir, a4_1up_name)
            page.pdf(
                path=target_1up,
                format="A4",
                print_background=True,
                margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"}
            )
            page.close()

            for dst in [
                os.path.join(desktop_dir, desk_1up_name),
                os.path.join(desktop_dir, a4_1up_name),
                os.path.join(desktop_dir, desk_1up_name.replace("85x40mm", "좌우8mm접착포함_101x40mm")),
            ]:
                try:
                    shutil.copyfile(target_1up, dst)
                except PermissionError:
                    shutil.copyfile(target_1up, dst.replace(".pdf", "_최신수정본.pdf"))

            # 2) Render 3-up A4 PDF
            page3 = browser.new_page(viewport={"width": 1280, "height": 1200}, device_scale_factor=2)
            page3.goto(url)
            page3.wait_for_timeout(400)
            page3.evaluate(f"""() => {{
                document.body.className = 'paper-a4 print-white';
                const titleEl = document.querySelector('.a4-calibration-header > div:first-child');
                if (titleEl) {{
                    titleEl.textContent = '[30ml 정품 규격] {prod_name} 3구 실측 라벨 (중심 85×40mm + 좌우 접착공간 각 8mm = 총 101×40mm × 3개)';
                }}
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

                for (let i = 1; i <= 3; i++) {{
                    const clone = originalCropBox.cloneNode(true);
                    clone.style.margin = '0 auto';

                    const numTag = document.createElement('div');
                    numTag.style.textAlign = 'center';
                    numTag.style.fontSize = '7.5pt';
                    numTag.style.fontWeight = '700';
                    numTag.style.color = '#64748b';
                    numTag.style.marginBottom = '2mm';
                    numTag.textContent = '▼ 라벨 #' + i + ' (중심 85×40mm + 좌·우 8mm 접착 날개 = 총 101×40mm)';

                    const wrapper = document.createElement('div');
                    wrapper.style.display = 'flex';
                    wrapper.style.flexDirection = 'column';
                    wrapper.style.alignItems = 'center';
                    wrapper.appendChild(numTag);
                    wrapper.appendChild(clone);
                    container.appendChild(wrapper);
                }}

                originalCropBox.parentNode.replaceChild(container, originalCropBox);

                const header = document.querySelector('.a4-calibration-header');
                if (header) {{
                    header.style.marginBottom = '4mm';
                    header.style.paddingTop = '2mm';
                }}
                const cutInst = document.querySelector('.a4-cut-instructions');
                if (cutInst) {{
                    cutInst.style.marginTop = '4mm';
                    cutInst.style.fontSize = '8pt';
                }}
            }}""")
            page3.wait_for_timeout(400)

            if idx == 0:
                page3.emulate_media(media="print")
                page3.wait_for_timeout(200)
                stage3_el = page3.query_selector(".labels-stage")
                if stage3_el:
                    stage3_el.screenshot(path=r"C:\Users\master\.gemini\antigravity\brain\cacb210e-6377-4186-9128-20025d75e8f6\preview_30ml_8mm_wings_3up.png")

            target_3up = os.path.join(out_dir, a4_3up_name)
            page3.pdf(
                path=target_3up,
                format="A4",
                print_background=True,
                margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"}
            )
            page3.close()

            reader = pypdf.PdfReader(target_3up)
            print(f"Rendered {a4_3up_name}: {len(reader.pages)} page(s)")

            for dst in [
                os.path.join(desktop_dir, desk_3up_name),
                os.path.join(desktop_dir, a4_3up_name),
                os.path.join(desktop_dir, desk_3up_name.replace("85x40mm", "좌우8mm접착포함_101x40mm")),
            ]:
                try:
                    shutil.copyfile(target_3up, dst)
                except PermissionError:
                    shutil.copyfile(target_3up, dst.replace(".pdf", "_최신수정본.pdf"))

        browser.close()

    # Also update default 30ml PDFs
    orig_1up = os.path.join(out_dir, "01_몬스멕타_30ml_라벨_A4실측인쇄용(85x40mm).pdf")
    for extra_dst in [
        os.path.join(out_dir, "몬스멕타_30ml_라벨_인쇄용(85x40mm)_최종.pdf"),
        os.path.join(out_dir, "몬스멕타_30ml_라벨_화이트뒷면(85x40mm).pdf"),
        os.path.join(desktop_dir, "몬스멕타_30ml_라벨_인쇄용(85x40mm)_최종.pdf"),
    ]:
        try:
            shutil.copyfile(orig_1up, extra_dst)
        except PermissionError:
            shutil.copyfile(orig_1up, extra_dst.replace(".pdf", "_최신수정본.pdf"))

    print("Successfully generated 30ml labels with 8mm left/right adhesive wings for all 3 products!")

if __name__ == "__main__":
    main()
