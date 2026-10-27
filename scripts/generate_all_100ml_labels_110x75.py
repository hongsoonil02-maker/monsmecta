import os
import json
import sys

scripts_dir = os.path.dirname(os.path.abspath(__file__))
if scripts_dir not in sys.path:
    sys.path.insert(0, scripts_dir)

out_dir = r"c:\Users\master\monsmecta_landing\public\assets\labels"
os.makedirs(out_dir, exist_ok=True)

with open(os.path.join(scripts_dir, "extracted_logo_b64.txt"), encoding="utf-8") as f:
    LOGO_B64 = f.read().strip()

from generate_all_30ml_labels import PRODUCTS

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    if len(hex_str) == 3:
        hex_str = ''.join([c*2 for c in hex_str])
    r = int(hex_str[0:2], 16)
    g = int(hex_str[2:4], 16)
    b = int(hex_str[4:6], 16)
    return f"{r}, {g}, {b}"

def render_100ml_label_html(p):
    neon = p["neon"]
    neon_sub = p.get("neon_sub", neon)
    neon_pale = p.get("neon_pale", "#ffffff")
    border = p["border"]
    bg_gradient = p["bg_gradient"]
    top_bar = p["top_bar"]

    # 1. Front effects
    row1 = p["front_effects"][0]
    row2 = p["front_effects"][1]
    
    note_html = f'<span class="eff-note">{row2[2]}</span>' if len(row2) > 2 and row2[2] else ""
    row1_html = f'''<span class="eff-item"><span class="eff-dot"></span>{row1[0]}</span>
                                <span class="eff-item" style="margin-left:auto;"><span class="eff-dot"></span>{row1[1]}</span>'''
    
    row2_items = []
    if row2[0]: row2_items.append(f'<span class="eff-item"><span class="eff-dot"></span>{row2[0]}</span>')
    if row2[1]: row2_items.append(f'<span class="eff-item" style="margin-left:3.0mm;"><span class="eff-dot"></span>{row2[1]}</span>')
    row2_joined = "\n                                ".join(row2_items)
    if note_html:
        row2_joined += f"\n                                {note_html}"
    
    # 2. Ingredients table
    ing_rows = []
    for name, val in p["ingredients"]:
        ing_rows.append(f'<div class="ing-row"><span class="ing-name">{name}</span><span class="ing-val">{val}</span></div>')
    ing_joined = "\n                        ".join(ing_rows)

    # 3. Raw materials lines
    raw_mat_lines = p["raw_mat_lines"]
    raw_mat_html = "\n                                    ".join([f"<div>{line}</div>" for line in raw_mat_lines])

    # 4. Statutory effects list
    stat_eff_html = []
    romans = ["I.", "II.", "III.", "IV."]
    for idx, eff in enumerate(p["statutory_effects"]):
        r = romans[idx] if idx < len(romans) else "•"
        stat_eff_html.append(f'<li><span class="roman">{r}</span>{eff}</li>')
    stat_eff_joined = "\n                                ".join(stat_eff_html)

    # Dosage
    dosage_desc = p.get("dosage_desc", "1일 1~2ml / 체중 5kg")
    dosage_sub = p.get("dosage_sub", "( 1 펌프 = 약 1ml ) - 증상에 따라 조절 가능")

    html = f'''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>{p["name_en"]} Label (110mm x 75mm) - 100ml 정품 규격</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;800;900&family=Orbitron:wght@700;900&display=swap" rel="stylesheet">
    <style>
        @page {{
            size: 110mm 75mm;
            margin: 0mm;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
            word-break: keep-all;
            overflow-wrap: break-word;
        }}

        html, body {{
            margin: 0;
            padding: 0;
            font-family: 'Noto Sans KR', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }}

        .orbitron {{
            font-family: 'Orbitron', sans-serif;
        }}

        /* 화면 뷰어 모드 */
        @media screen {{
            html, body {{
                width: 100% !important;
                min-height: 100vh !important;
                background: #09090b !important;
                display: flex !important;
                flex-direction: column !important;
                align-items: center !important;
                justify-content: flex-start !important;
                padding: 75px 20px 60px 20px !important;
                overflow-x: auto !important;
            }}

            .labels-stage {{
                display: flex;
                flex-direction: column;
                align-items: center;
                gap: 50px;
                padding: 15px 0;
            }}

            .label-card-wrapper {{
                display: flex;
                flex-direction: column;
                align-items: center;
                gap: 14px;
            }}

            .label-type-tag {{
                font-size: 13px;
                font-weight: 800;
                padding: 6px 18px;
                border-radius: 999px;
                display: inline-flex;
                align-items: center;
                gap: 8px;
            }}

            .tag-dark {{
                background: rgba(30, 41, 59, 0.95);
                border: 1px solid rgba({hex_to_rgb(neon)}, 0.5);
                color: {neon};
                box-shadow: 0 4px 15px rgba(0,0,0,0.6);
            }}

            .tag-white {{
                background: #ffffff;
                border: 1px solid #cbd5e1;
                color: #0f172a;
                box-shadow: 0 4px 15px rgba(0,0,0,0.4);
            }}

            .label-sheet {{
                box-shadow: 0 25px 60px rgba(0, 0, 0, 0.95), 0 0 35px rgba({hex_to_rgb(neon)}, 0.25);
                transform: scale(1.6);
                transform-origin: top center;
                margin-bottom: 50mm;
            }}
        }}

        /* 인쇄 전용 (110mm x 75mm 1:1) */
        @media print {{
            html, body {{
                width: 110mm !important;
                height: 75mm !important;
                margin: 0 !important;
                padding: 0 !important;
                background: transparent !important;
                overflow: hidden !important;
            }}

            .no-print {{
                display: none !important;
            }}

            .labels-stage {{
                display: block !important;
                padding: 0 !important;
                margin: 0 !important;
            }}

            .label-card-wrapper {{
                display: none !important;
                padding: 0 !important;
                margin: 0 !important;
            }}

            body.print-white #card-white,
            body.print-dark #card-dark {{
                display: block !important;
            }}

            body:not(.print-dark):not(.print-white) #card-white {{
                display: block !important;
            }}

            .label-sheet {{
                border: none !important;
                width: 110mm !important;
                height: 75mm !important;
                transform: none !important;
                box-shadow: none !important;
                margin: 0 !important;
            }}
        }}

        /* 라벨 전체 규격: 110mm x 75mm (100ml 정품 규격) */
        .label-sheet {{
            width: 110mm;
            height: 75mm;
            background: {bg_gradient};
            color: #f8fafc;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            border: 0.20mm solid {border};
            flex-shrink: 0;
        }}

        .grid-overlay {{
            position: absolute;
            inset: 0;
            opacity: 0.08;
            background-image: 
                linear-gradient({neon} 1px, transparent 1px),
                linear-gradient(90deg, {neon} 1px, transparent 1px);
            background-size: 3.5mm 3.5mm;
            pointer-events: none;
            z-index: 1;
        }}

        /* 상단 액센트 바 (0.60mm) */
        .top-accent-bar {{
            height: 0.60mm;
            background: {top_bar};
            box-shadow: 0 0 1.5mm {neon}E6;
            z-index: 2;
            flex-shrink: 0;
        }}

        /* 콘텐츠 랩 */
        .content-wrap {{
            position: relative;
            z-index: 2;
            display: flex;
            height: calc(75mm - 0.60mm);
            width: 110mm;
            padding: 0.8mm 1.2mm 0.8mm 1.2mm;
            justify-content: space-between;
        }}

        /* 좌측: 전면 메인 노출부 (52.6mm) */
        .col-left {{
            width: 52.6mm;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}

        /* 중앙 디바이더 (2.4mm) */
        .divider-col {{
            width: 2.4mm;
            height: 100%;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .divider-line {{
            width: 0.20mm;
            height: 98%;
            background: linear-gradient(180deg, transparent, {neon}, transparent);
            opacity: 0.7;
        }}
        .divider-diamond {{
            position: absolute;
            width: 1.2mm;
            height: 1.2mm;
            background: #000;
            border: 0.20mm solid {neon};
            transform: rotate(45deg);
        }}

        /* 우측: 법정 고시사항 패널 (52.6mm) */
        .col-right {{
            width: 52.6mm;
            height: 100%;
            display: flex;
            flex-direction: column;
        }}

        /* ---------------- 좌측 전면 메인 스타일 ---------------- */
        .brand-badge {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 1.0mm;
            background: rgba(0, 0, 0, 0.65);
            border: 0.20mm solid {neon};
            border-radius: 999px;
            padding: 0.3mm 2.0mm;
            line-height: 1;
            box-sizing: border-box;
        }}
        .brand-badge .emoji {{
            font-size: 3.0mm;
            line-height: 1;
            display: inline-flex;
            align-items: center;
        }}
        .brand-badge .text {{
            font-size: 1.70mm;
            font-weight: 800;
            letter-spacing: 0.04em;
            color: #ffffff;
            line-height: 1;
            display: inline-flex;
            align-items: center;
        }}
        .brand-badge .accent {{
            color: {neon};
            font-weight: 900;
        }}

        .hero-section {{
            text-align: center;
            padding: 0.5mm 0;
            margin: 0;
        }}
        .sub-desc {{
            font-size: 2.0mm;
            font-weight: 700;
            color: #f1f5f9;
            line-height: 1.15;
            margin-bottom: 0.4mm;
            text-shadow: 0 0 0.8mm rgba(0,0,0,0.8);
        }}
        .main-title {{
            font-size: 5.6mm;
            font-weight: 900;
            color: #ffffff;
            line-height: 1.05;
            letter-spacing: -0.02em;
            text-shadow: 0 0 1.5mm rgba(255, 255, 255, 0.5), 0 1px 2px #000;
            margin-bottom: 0.4mm;
        }}
        .en-title {{
            font-size: 2.3mm;
            font-weight: 900;
            color: {neon};
            letter-spacing: 0.06em;
            line-height: 1;
        }}

        .effects-box-wrapper {{
            position: relative;
            padding-top: 1.4mm;
            margin: 0.4mm 0;
        }}
        .effects-badge-top {{
            position: absolute;
            top: 0;
            left: 1.8mm;
            z-index: 3;
            background: {neon};
            color: #000;
            border: 0.15mm solid #000;
            border-radius: 0.3mm;
            padding: 0.15mm 1.0mm;
            font-size: 1.55mm;
            font-weight: 900;
            line-height: 1;
            box-shadow: 0 0.3mm 0.6mm rgba(0, 0, 0, 0.9);
            display: inline-flex;
            align-items: center;
            justify-content: center;
        }}
        .effects-card {{
            background: rgba(0, 0, 0, 0.60);
            border: 0.22mm solid {neon};
            border-radius: 0.5mm;
            padding: 1.6mm 1.0mm 1.0mm 1.0mm;
            display: flex;
            flex-direction: column;
            gap: 0.6mm;
        }}
        .effects-row {{
            display: flex;
            align-items: center;
            gap: 0.8mm;
            line-height: 1.15;
            white-space: nowrap;
        }}
        .eff-item {{
            font-size: 1.70mm;
            font-weight: 800;
            color: #ffffff;
            display: inline-flex;
            align-items: center;
            gap: 0.4mm;
            letter-spacing: -0.01em;
        }}
        .eff-dot {{
            width: 0.65mm;
            height: 0.65mm;
            background: {neon};
            border-radius: 50%;
            display: inline-block;
            flex-shrink: 0;
        }}
        .eff-note {{
            font-size: 1.25mm;
            color: #cbd5e1;
            font-weight: 500;
            margin-left: auto;
        }}

        .tech-box-ing {{
            background: rgba(0, 0, 0, 0.55);
            border: 0.20mm solid rgba({hex_to_rgb(neon)}, 0.45);
            border-radius: 0.5mm;
            padding: 0.8mm 1.2mm;
            display: flex;
            flex-direction: column;
            gap: 0.25mm;
        }}
        .ing-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 0.15mm solid {neon}55;
            padding-bottom: 0.4mm;
            margin-bottom: 0.3mm;
        }}
        .ing-header .title {{
            font-size: 1.65mm;
            font-weight: 800;
            color: {neon};
            line-height: 1;
        }}
        .ing-header .ref {{
            font-size: 1.35mm;
            color: {neon_pale};
            font-weight: 600;
            line-height: 1;
        }}
        .ing-row {{
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            font-size: 1.52mm;
            line-height: 1.35;
        }}
        .ing-name {{
            color: #e2e8f0;
            font-weight: 600;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            max-width: 38mm;
        }}
        .ing-val {{
            color: #ffffff;
            font-weight: 800;
            white-space: nowrap;
            flex-shrink: 0;
            margin-left: 0.6mm;
        }}

        .pack-tag {{
            align-self: center;
            background: rgba(0, 0, 0, 0.65);
            border: 0.22mm solid {neon};
            border-radius: 999px;
            padding: 0.35mm 2.2mm;
            font-size: 1.80mm;
            font-weight: 800;
            display: flex;
            gap: 0.8mm;
            align-items: center;
            justify-content: center;
            line-height: 1;
            box-sizing: border-box;
            color: #ffffff;
        }}
        .pack-tag .val {{
            color: {neon};
            font-weight: 900;
        }}

        /* ---------------- 우측 법정 고시 패널 공통 레이아웃 ---------------- */
        .legal-panel {{
            height: 100%;
            padding: 0.4mm 0.8mm 0.4mm 0.8mm;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}

        /* 헤더 */
        .legal-header {{
            display: flex;
            flex-direction: column;
            gap: 0.3mm;
            padding-bottom: 0.3mm;
        }}
        .reg-num-line {{
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            line-height: 1.15;
        }}
        .reg-num-label {{
            font-size: 1.55mm;
            font-weight: 800;
            line-height: 1;
        }}
        .reg-num-val {{
            font-size: 1.80mm;
            font-weight: 900;
            line-height: 1;
        }}
        .feed-type-line {{
            font-size: 1.35mm;
            font-weight: 700;
            line-height: 1.25;
            white-space: nowrap;
        }}
        .feed-type-line .lbl {{
            font-weight: 800;
        }}

        /* 본문 내용 */
        .sec-content {{
            display: flex;
            flex-direction: column;
            gap: 0.35mm;
            margin: 0.2mm 0;
            text-align: left;
        }}
        .info-row {{
            display: flex;
            align-items: baseline;
            font-size: 1.55mm;
            line-height: 1.30;
            text-align: left;
        }}
        .sec-lbl {{
            font-weight: 800;
            margin-right: 0.4mm;
            white-space: nowrap;
            flex-shrink: 0;
        }}
        .sec-val {{
            font-weight: 700;
            flex: 1;
        }}

        .materials-val-box {{
            display: flex;
            flex-direction: column;
            gap: 0.15mm;
            flex: 1;
            font-weight: 600;
            line-height: 1.30;
        }}

        .effects-sub-list {{
            list-style: none;
            padding-left: 0.4mm;
            display: flex;
            flex-direction: column;
            gap: 0.2mm;
            margin: 0.1mm 0;
        }}
        .effects-sub-list li {{
            font-size: 1.50mm;
            font-weight: 600;
            line-height: 1.30;
            display: flex;
            align-items: baseline;
            gap: 0.4mm;
        }}
        .effects-sub-list .roman {{
            font-weight: 800;
            font-size: 1.45mm;
            flex-shrink: 0;
        }}

        /* 용법 및 용량 */
        .dose-box-single {{
            border-radius: 0.45mm;
            padding: 0.45mm 0.9mm;
            display: flex;
            align-items: center;
            justify-content: flex-start;
            gap: 0.6mm;
            line-height: 1.15;
            white-space: nowrap;
        }}
        .dose-box-single .title {{
            font-size: 1.60mm;
            font-weight: 900;
        }}
        .dose-box-single .desc {{
            font-size: 1.60mm;
            font-weight: 800;
        }}
        .dose-box-single .sub {{
            font-size: 1.35mm;
            font-weight: 600;
            margin-left: 0.3mm;
        }}

        /* 주의사항 */
        .warn-box-orig {{
            border: 0.20mm solid #ef4444;
            border-radius: 0.45mm;
            padding: 0.45mm 0.8mm;
            display: flex;
            flex-direction: column;
            gap: 0.15mm;
        }}
        .warn-title-orig {{
            font-size: 1.45mm;
            font-weight: 800;
            color: #ef4444;
            line-height: 1;
        }}
        .warn-list-orig {{
            list-style: none;
            padding: 0;
            margin: 0;
            display: flex;
            flex-direction: column;
            gap: 0.12mm;
        }}
        .warn-item-orig {{
            font-size: 1.35mm;
            line-height: 1.25;
            display: flex;
            align-items: baseline;
            gap: 0.3mm;
        }}
        .hl-shake {{
            font-weight: 800;
        }}

        /* 제조일자/유통기한/재활용 */
        .mfg-date-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0.2mm 0.4mm;
            font-size: 1.45mm;
            line-height: 1;
            white-space: nowrap;
        }}
        .mfg-date-row .lbl {{
            font-weight: 800;
            margin-right: 0.2mm;
        }}
        .mfg-date-row .val {{
            font-weight: 800;
        }}
        .recycle-wrap {{
            display: flex;
            align-items: center;
            gap: 0.35mm;
            flex-shrink: 0;
        }}
        .recycle-other {{
            font-size: 1.35mm;
            font-weight: 900;
            letter-spacing: -0.01em;
        }}

        /* 제조원 / 위탁제조판매원 풋터 */
        .original-footer {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 0.8mm;
            padding-top: 0.4mm;
            line-height: 1.25;
        }}
        .footer-seller {{
            display: flex;
            align-items: center;
            gap: 0.6mm;
            flex: 1.15;
            min-width: 0;
        }}
        .footer-maker {{
            flex: 0.85;
            min-width: 0;
        }}
        .co-logo-circle {{
            width: 4.8mm;
            height: 4.8mm;
            border-radius: 50%;
            background: #ffffff;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            flex-shrink: 0;
        }}
        .co-logo-img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}
        .co-text-col {{
            display: flex;
            flex-direction: column;
            gap: 0.05mm;
            font-size: 1.15mm;
            white-space: nowrap;
        }}
        .co-line-main {{
            font-weight: 800;
        }}
        .co-line-sub {{
            font-weight: 600;
        }}

        /* ========================================================================= */
        /* [TYPE A: 원본 다크 스타일] */
        /* ========================================================================= */
        #card-dark .legal-panel {{
            background: transparent;
        }}
        #card-dark .reg-num-label {{ color: {neon}; }}
        #card-dark .reg-num-val {{ color: #ffffff; }}
        #card-dark .feed-type-line {{ color: #ffffff; }}
        #card-dark .feed-type-line .lbl {{ color: {neon}; }}

        #card-dark .sec-lbl {{ color: {neon}; }}
        #card-dark .sec-val {{ color: #ffffff; }}
        #card-dark .materials-val-box {{ color: #ffffff; }}
        #card-dark .effects-sub-list li {{ color: #ffffff; }}
        #card-dark .effects-sub-list .roman {{ color: {neon}; }}

        #card-dark .dose-box-single {{
            background: rgba({hex_to_rgb(neon)}, 0.12);
            border: 0.20mm solid {neon};
        }}
        #card-dark .dose-box-single .title {{ color: {neon}; }}
        #card-dark .dose-box-single .desc {{ color: #ffffff; }}
        #card-dark .dose-box-single .sub {{ color: {neon}; }}

        #card-dark .warn-item-orig {{ color: #f1f5f9; }}
        #card-dark .warn-item-orig .hl-shake {{
            color: #fef08a;
            font-weight: 800;
            text-decoration: underline;
        }}

        #card-dark .mfg-date-row .lbl {{ color: {neon}; }}
        #card-dark .mfg-date-row .val {{ color: #ffffff; }}
        #card-dark .recycle-wrap {{ color: {neon}; }}
        #card-dark .recycle-other {{ color: #ffffff; }}

        #card-dark .original-footer {{
            border-top: 0.15mm solid rgba(255, 255, 255, 0.15);
        }}
        #card-dark .footer-maker {{
            border-left: 0.15mm solid rgba(255, 255, 255, 0.15);
            padding-left: 0.8mm;
        }}
        #card-dark .co-logo-circle {{
            border: 0.20mm solid {neon};
        }}
        #card-dark .co-line-main {{ color: #ffffff; }}
        #card-dark .co-line-sub {{ color: #94a3b8; }}

        /* ========================================================================= */
        /* [TYPE B: 화이트 뒷면 가독성 특화 스타일] */
        /* ========================================================================= */
        #card-white .col-right {{
            background: #ffffff !important;
            border-radius: 0 0.4mm 0.4mm 0;
            box-shadow: inset 0 0 1.5mm rgba(0, 0, 0, 0.08);
        }}
        #card-white .legal-panel {{
            background: #ffffff !important;
            color: #000000 !important;
        }}

        #card-white .reg-num-label {{ color: #000000 !important; font-weight: 900 !important; }}
        #card-white .reg-num-val {{ color: #000000 !important; font-weight: 900 !important; }}
        #card-white .feed-type-line {{ color: #000000 !important; }}
        #card-white .feed-type-line .lbl {{ color: #000000 !important; font-weight: 900 !important; }}

        #card-white .sec-lbl {{ color: #000000 !important; font-weight: 900 !important; }}
        #card-white .sec-val {{ color: #000000 !important; font-weight: 700 !important; }}
        #card-white .materials-val-box {{ color: #000000 !important; font-weight: 600 !important; }}
        #card-white .effects-sub-list li {{ color: #000000 !important; font-weight: 600 !important; }}
        #card-white .effects-sub-list .roman {{ color: #000000 !important; font-weight: 900 !important; }}

        #card-white .dose-box-single {{
            background: #f1f5f9 !important;
            border: 0.20mm solid #0f172a !important;
        }}
        #card-white .dose-box-single .title {{ color: #000000 !important; font-weight: 900 !important; }}
        #card-white .dose-box-single .desc {{ color: #000000 !important; font-weight: 800 !important; }}
        #card-white .dose-box-single .sub {{ color: #334155 !important; font-weight: 700 !important; }}

        #card-white .warn-box-orig {{
            border: 0.20mm solid #dc2626 !important;
            background: #fff1f2 !important;
        }}
        #card-white .warn-title-orig {{ color: #dc2626 !important; font-weight: 900 !important; }}
        #card-white .warn-item-orig {{ color: #000000 !important; font-weight: 600 !important; }}
        #card-white .warn-item-orig .hl-shake {{
            color: #b45309 !important;
            font-weight: 900 !important;
            background: #fef08a !important;
            padding: 0 0.3mm !important;
            border-radius: 0.25mm !important;
            text-decoration: none !important;
        }}

        #card-white .mfg-date-row .lbl {{ color: #000000 !important; font-weight: 900 !important; }}
        #card-white .mfg-date-row .val {{ color: #000000 !important; font-weight: 800 !important; }}
        #card-white .recycle-wrap {{ color: #000000 !important; }}
        #card-white .recycle-other {{ color: #000000 !important; }}

        #card-white .original-footer {{
            border-top: 0.15mm solid #cbd5e1 !important;
        }}
        #card-white .footer-maker {{
            border-left: 0.15mm solid #cbd5e1 !important;
            padding-left: 0.8mm;
        }}
        #card-white .co-logo-circle {{
            border: 0.20mm solid #cbd5e1 !important;
            box-shadow: 0 0 0.4mm rgba(0,0,0,0.15);
        }}
        #card-white .co-line-main {{ color: #000000 !important; font-weight: 900 !important; }}
        #card-white .co-line-sub {{ color: #1e293b !important; font-weight: 700 !important; }}

        #card-white .divider-line {{
            background: linear-gradient(180deg, transparent, {border}, transparent) !important;
        }}
        #card-white .divider-diamond {{
            background: #fff !important;
            border-color: {border} !important;
        }}
    </style>
</head>
<body class="mode-compare print-white">

<!-- 상단 실시간 비교/인쇄 툴바 -->
<div class="no-print" style="position:fixed; top:12px; left:50%; transform:translateX(-50%); z-index:99999; background:rgba(15,23,42,0.96); border:1px solid {neon}; padding:10px 22px; border-radius:14px; display:flex; align-items:center; gap:14px; box-shadow:0 12px 35px rgba(0,0,0,0.85); backdrop-filter:blur(10px); font-family:sans-serif;">
    <div style="color:#ffffff; font-size:13px; font-weight:700; display:flex; align-items:center; gap:8px;">
        <span style="color:{neon}; font-size:15px;">★</span>
        <span style="color:{neon}; font-weight:800;">{p["name_ko"]} 100ml</span>
        <span style="color:#94a3b8; font-size:12px; background:rgba(255,255,255,0.08); padding:3px 8px; border-radius:6px; border:1px solid rgba(255,255,255,0.15);">정밀 규격 110mm × 75mm (100ml 정품)</span>
    </div>

    <div style="height:18px; width:1px; background:rgba(255,255,255,0.2);"></div>

    <!-- 비교 모드 선택 버튼군 -->
    <div style="display:flex; gap:6px;">
        <button id="btn-dark" onclick="setViewMode('dark')" style="background:rgba(30,41,59,0.8); color:{neon}; border:1px solid rgba({hex_to_rgb(neon)},0.4); font-weight:700; font-size:12px; padding:6px 13px; border-radius:8px; cursor:pointer; transition:all 0.15s ease;">
            🌙 원본 올 다크 (Original)
        </button>
        <button id="btn-white" onclick="setViewMode('white')" style="background:linear-gradient(135deg, {neon}, {neon_sub}); color:#000; border:1px solid {neon}; font-weight:900; font-size:12px; padding:6px 13px; border-radius:8px; cursor:pointer; box-shadow:0 0 10px rgba({hex_to_rgb(neon)},0.3); transition:all 0.15s ease;">
            ☀️ 화이트 뒷면 (White Back)
        </button>
        <button id="btn-compare" onclick="setViewMode('compare')" style="background:#2563eb; color:#fff; border:1px solid #60a5fa; font-weight:800; font-size:12px; padding:6px 13px; border-radius:8px; cursor:pointer; transition:all 0.15s ease;">
            ⚖️ 상하 동시 비교
        </button>
    </div>

    <div style="height:18px; width:1px; background:rgba(255,255,255,0.2);"></div>

    <!-- 인쇄 타겟 선택 및 인쇄 실행 -->
    <div style="display:flex; align-items:center; gap:6px;">
        <select id="print-target" onchange="updatePrintTarget(this.value)" style="background:#1e293b; color:#e2e8f0; border:1px solid #475569; font-size:12px; font-weight:700; padding:5px 8px; border-radius:6px; cursor:pointer; outline:none;">
            <option value="white" selected>인쇄: 화이트 뒷면 (Type B)</option>
            <option value="dark">인쇄: 원본 올 다크 (Type A)</option>
        </select>
        <button onclick="window.print()" style="background:linear-gradient(135deg, #10b981, #059669); color:#fff; font-weight:800; font-size:12px; padding:6px 15px; border:none; border-radius:8px; cursor:pointer; box-shadow:0 3px 10px rgba(16,185,129,0.4); display:flex; align-items:center; gap:5px;">
            <span>🖨️ 인쇄 (Ctrl+P)</span>
        </button>
    </div>
</div>

<div class="labels-stage">

    <!-- [CARD 1] 원본 올 다크 라벨 -->
    <div class="label-card-wrapper" id="card-dark">
        <div class="label-type-tag tag-dark no-print">
            <span>🌙 원본 라벨 (올 다크 테마)</span>
            <span style="font-weight:400; opacity:0.85;">| 고유 아이덴티티 네온 다크 (110mm × 75mm / 100ml)</span>
        </div>
        <div class="label-sheet">
            <div class="grid-overlay"></div>
            <div class="top-accent-bar"></div>

            <div class="content-wrap">
                <!-- LEFT COLUMN (전면 메인) -->
                <div class="col-left">
                    <div class="brand-badge">
                        <span class="emoji">🐶</span>
                        <span class="text"><span class="accent">S&J</span>&nbsp;ADVANCED VET FORMULA</span>
                        <span class="emoji">🐱</span>
                    </div>

                    <div class="hero-section">
                        <div class="sub-desc">{p["sub_desc"]}</div>
                        <h1 class="main-title">{p["name_ko"]}</h1>
                        <h2 class="en-title orbitron">{p["name_en"]}</h2>
                    </div>

                    <div class="effects-box-wrapper">
                        <div class="effects-badge-top">핵심 효능</div>
                        <div class="effects-card">
                            <div class="effects-row">
                                {row1_html}
                            </div>
                            <div class="effects-row">
                                {row2_joined}
                            </div>
                        </div>
                    </div>

                    <div class="tech-box-ing">
                        <div class="ing-header">
                            <span class="title">주요 성분량</span>
                            <span class="ref">{p.get("ingredients_header_ref", "100ml 정품 기준")}</span>
                        </div>
                        {ing_joined}
                    </div>

                    <div class="pack-tag">
                        <span>포장 단위 :</span>
                        <span class="val">100ml / 병</span>
                    </div>
                </div>

                <!-- CENTER DIVIDER -->
                <div class="divider-col">
                    <div class="divider-line"></div>
                    <div class="divider-diamond"></div>
                </div>

                <!-- RIGHT COLUMN (원본 올 다크 법정 패널) -->
                <div class="col-right">
                    <div class="legal-panel">
                        <div class="legal-header">
                            <div class="reg-num-line">
                                <span class="reg-num-label">사료의 성분등록번호 :</span>
                                <span class="reg-num-val">{p["reg_no"]}</span>
                            </div>
                            <div class="feed-type-line">
                                <span class="lbl">사료의 종류와 명칭 / 형태 / 용도 :</span> {p["feed_type"]}
                            </div>
                        </div>

                        <div class="sec-content">
                            <div class="info-row">
                                <span class="sec-lbl">등록성분량 :</span>
                                <span class="sec-val">{p["reg_ing"]}</span>
                            </div>
                            <div class="info-row">
                                <span class="sec-lbl">사용한 원료의 명칭 :</span>
                                <div class="materials-val-box">
                                    {raw_mat_html}
                                </div>
                            </div>
                            <div class="info-row">
                                <span class="sec-lbl">대상축종 :</span>
                                <span class="sec-val" style="color:{neon}; font-weight:800;">{p["target"]}</span>
                            </div>
                            <div class="info-row" style="align-items:flex-start;">
                                <span class="sec-lbl">효과 :</span>
                                <ul class="effects-sub-list">
                                {stat_eff_joined}
                                </ul>
                            </div>
                        </div>

                        <div class="dose-box-single">
                            <span class="title">용법 및 용량 :</span>
                            <span class="desc">{dosage_desc}</span>
                            <span class="sub">{dosage_sub}</span>
                        </div>

                        <div class="warn-box-orig">
                            <span class="warn-title-orig">⚠️ 주의사항</span>
                            <ul class="warn-list-orig">
                                <li class="warn-item-orig">• 직사광선을 피하여 <strong>건조하고 서늘한 곳에 보관</strong>하십시오.</li>
                                <li class="warn-item-orig">• 제품 특성 상 침전물이 생길 수 있으니 <span class="hl-shake">흔들어서 사용</span>하십시오.</li>
                                <li class="warn-item-orig">• 문의사항은 제조원 또는 판매원으로 연락해 주시기 바랍니다.</li>
                            </ul>
                        </div>

                        <div class="mfg-date-row">
                            <div><span class="lbl">제조일자 :</span><span class="val">별도표기</span></div>
                            <div><span class="lbl">유통기한 :</span><span class="val">제조일로부터 18개월</span></div>
                            <div><span class="lbl">포장 :</span><span class="val" style="color:{neon};">100ml</span></div>
                            <div class="recycle-wrap">
                                <svg width="3.8mm" height="3.8mm" viewBox="0 0 100 115" style="fill:none; stroke:currentColor; stroke-width:7;">
                                    <path d="M50 8 L90 74 L10 74 Z" stroke-linejoin="round" stroke-linecap="round"/>
                                    <path d="M50 8 L61 19 M90 74 L75 74 M10 74 L21 59" stroke-linecap="round"/>
                                    <text x="50" y="52" text-anchor="middle" dominant-baseline="central" fill="currentColor" font-size="20" font-weight="900" font-family="'Noto Sans KR', sans-serif">플라스틱</text>
                                </svg>
                                <span class="recycle-other orbitron">OTHER</span>
                            </div>
                        </div>

                        <!-- 풋터 원본 일치 (에스앤제이 용인 / 엠오바이오 화성) -->
                        <div class="original-footer">
                            <div class="footer-seller">
                                <div class="co-logo-circle">
                                    <img src="data:image/png;base64,{LOGO_B64}" class="co-logo-img" alt="S&J">
                                </div>
                                <div class="co-text-col">
                                    <div class="co-line-main">위탁제조판매원 : 에스앤제이 동물병원</div>
                                    <div class="co-line-sub">경기도 용인시 처인구 포곡읍 선장1로 98-8</div>
                                    <div class="co-line-sub"><span style="color:{neon}; font-weight:800;">TEL</span> 031-321-6562</div>
                                </div>
                            </div>
                            <div class="footer-maker">
                                <div class="co-text-col">
                                    <div class="co-line-main">제조원 : 엠오 바이오</div>
                                    <div class="co-line-sub">화성시 팔탄면 석포로 74번길 10-25</div>
                                    <div class="co-line-sub"><span style="color:{neon}; font-weight:800;">TEL</span> 031-458-1240</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- [CARD 2] 화이트 뒷면 가독성 특화 라벨 -->
    <div class="label-card-wrapper" id="card-white">
        <div class="label-type-tag tag-white no-print">
            <span>☀️ 화이트 뒷면 라벨 (Type B / 약사·수의사 권장 가독성)</span>
            <span style="font-weight:600; color:#475569;">| 원본 표기사항 100% 동일, 우측 배경 화이트 및 텍스트 블랙 (110mm × 75mm / 100ml)</span>
        </div>
        <div class="label-sheet">
            <div class="grid-overlay"></div>
            <div class="top-accent-bar"></div>

            <div class="content-wrap">
                <!-- LEFT COLUMN (전면 메인은 고유 네온 다크 유지) -->
                <div class="col-left">
                    <div class="brand-badge">
                        <span class="emoji">🐶</span>
                        <span class="text"><span class="accent">S&J</span>&nbsp;ADVANCED VET FORMULA</span>
                        <span class="emoji">🐱</span>
                    </div>

                    <div class="hero-section">
                        <div class="sub-desc">{p["sub_desc"]}</div>
                        <h1 class="main-title">{p["name_ko"]}</h1>
                        <h2 class="en-title orbitron">{p["name_en"]}</h2>
                    </div>

                    <div class="effects-box-wrapper">
                        <div class="effects-badge-top">핵심 효능</div>
                        <div class="effects-card">
                            <div class="effects-row">
                                {row1_html}
                            </div>
                            <div class="effects-row">
                                {row2_joined}
                            </div>
                        </div>
                    </div>

                    <div class="tech-box-ing">
                        <div class="ing-header">
                            <span class="title">주요 성분량</span>
                            <span class="ref">{p.get("ingredients_header_ref", "100ml 정품 기준")}</span>
                        </div>
                        {ing_joined}
                    </div>

                    <div class="pack-tag">
                        <span>포장 단위 :</span>
                        <span class="val">100ml / 병</span>
                    </div>
                </div>

                <!-- CENTER DIVIDER -->
                <div class="divider-col">
                    <div class="divider-line"></div>
                    <div class="divider-diamond"></div>
                </div>

                <!-- RIGHT COLUMN (화이트 배경 + 고대비 블랙 텍스트 법정 패널) -->
                <div class="col-right">
                    <div class="legal-panel">
                        <div class="legal-header">
                            <div class="reg-num-line">
                                <span class="reg-num-label">사료의 성분등록번호 :</span>
                                <span class="reg-num-val">{p["reg_no"]}</span>
                            </div>
                            <div class="feed-type-line">
                                <span class="lbl">사료의 종류와 명칭 / 형태 / 용도 :</span> {p["feed_type"]}
                            </div>
                        </div>

                        <div class="sec-content">
                            <div class="info-row">
                                <span class="sec-lbl">등록성분량 :</span>
                                <span class="sec-val">{p["reg_ing"]}</span>
                            </div>
                            <div class="info-row">
                                <span class="sec-lbl">사용한 원료의 명칭 :</span>
                                <div class="materials-val-box">
                                    {raw_mat_html}
                                </div>
                            </div>
                            <div class="info-row">
                                <span class="sec-lbl">대상축종 :</span>
                                <span class="sec-val" style="color:#0f172a; font-weight:800;">{p["target"]}</span>
                            </div>
                            <div class="info-row" style="align-items:flex-start;">
                                <span class="sec-lbl">효과 :</span>
                                <ul class="effects-sub-list">
                                {stat_eff_joined}
                                </ul>
                            </div>
                        </div>

                        <div class="dose-box-single">
                            <span class="title">용법 및 용량 :</span>
                            <span class="desc">{dosage_desc}</span>
                            <span class="sub">{dosage_sub}</span>
                        </div>

                        <div class="warn-box-orig">
                            <span class="warn-title-orig">⚠️ 주의사항</span>
                            <ul class="warn-list-orig">
                                <li class="warn-item-orig">• 직사광선을 피하여 <strong>건조하고 서늘한 곳에 보관</strong>하십시오.</li>
                                <li class="warn-item-orig">• 제품 특성 상 침전물이 생길 수 있으니 <span class="hl-shake">흔들어서 사용</span>하십시오.</li>
                                <li class="warn-item-orig">• 문의사항은 제조원 또는 판매원으로 연락해 주시기 바랍니다.</li>
                            </ul>
                        </div>

                        <div class="mfg-date-row">
                            <div><span class="lbl">제조일자 :</span><span class="val">별도표기</span></div>
                            <div><span class="lbl">유통기한 :</span><span class="val">제조일로부터 18개월</span></div>
                            <div><span class="lbl">포장 :</span><span class="val" style="color:#0f172a;">100ml</span></div>
                            <div class="recycle-wrap">
                                <svg width="3.8mm" height="3.8mm" viewBox="0 0 100 115" style="fill:none; stroke:#000000; stroke-width:7;">
                                    <path d="M50 8 L90 74 L10 74 Z" stroke-linejoin="round" stroke-linecap="round"/>
                                    <path d="M50 8 L61 19 M90 74 L75 74 M10 74 L21 59" stroke-linecap="round"/>
                                    <text x="50" y="52" text-anchor="middle" dominant-baseline="central" fill="#000000" font-size="20" font-weight="900" font-family="'Noto Sans KR', sans-serif">플라스틱</text>
                                </svg>
                                <span class="recycle-other orbitron">OTHER</span>
                            </div>
                        </div>

                        <!-- 풋터 화이트 버전 -->
                        <div class="original-footer">
                            <div class="footer-seller">
                                <div class="co-logo-circle">
                                    <img src="data:image/png;base64,{LOGO_B64}" class="co-logo-img" alt="S&J">
                                </div>
                                <div class="co-text-col">
                                    <div class="co-line-main">위탁제조판매원 : 에스앤제이 동물병원</div>
                                    <div class="co-line-sub">경기도 용인시 처인구 포곡읍 선장1로 98-8</div>
                                    <div class="co-line-sub"><span style="color:#000000; font-weight:800;">TEL</span> 031-321-6562</div>
                                </div>
                            </div>
                            <div class="footer-maker">
                                <div class="co-text-col">
                                    <div class="co-line-main">제조원 : 엠오 바이오</div>
                                    <div class="co-line-sub">화성시 팔탄면 석포로 74번길 10-25</div>
                                    <div class="co-line-sub"><span style="color:#000000; font-weight:800;">TEL</span> 031-458-1240</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</div>

<script>
    function setViewMode(mode) {{
        const cardDark = document.getElementById('card-dark');
        const cardWhite = document.getElementById('card-white');
        const btnDark = document.getElementById('btn-dark');
        const btnWhite = document.getElementById('btn-white');
        const btnCompare = document.getElementById('btn-compare');
        const printSelect = document.getElementById('print-target');

        [btnDark, btnWhite, btnCompare].forEach(b => {{
            b.style.background = 'rgba(30,41,59,0.8)';
            b.style.color = '#94a3b8';
            b.style.boxShadow = 'none';
        }});

        if (mode === 'dark') {{
            cardDark.style.display = 'flex';
            cardWhite.style.display = 'none';
            btnDark.style.background = 'linear-gradient(135deg, #1e293b, #0f172a)';
            btnDark.style.color = '{neon}';
            btnDark.style.boxShadow = '0 0 10px rgba({hex_to_rgb(neon)},0.3)';
            printSelect.value = 'dark';
            document.body.className = 'mode-dark print-dark';
        }} else if (mode === 'white') {{
            cardDark.style.display = 'none';
            cardWhite.style.display = 'flex';
            btnWhite.style.background = 'linear-gradient(135deg, {neon}, {neon_sub})';
            btnWhite.style.color = '#000000';
            btnWhite.style.boxShadow = '0 0 10px rgba({hex_to_rgb(neon)},0.4)';
            printSelect.value = 'white';
            document.body.className = 'mode-white print-white';
        }} else {{
            cardDark.style.display = 'flex';
            cardWhite.style.display = 'flex';
            btnCompare.style.background = '#2563eb';
            btnCompare.style.color = '#ffffff';
            btnCompare.style.boxShadow = '0 0 10px rgba(37,99,235,0.4)';
            document.body.className = 'mode-compare ' + (printSelect.value === 'dark' ? 'print-dark' : 'print-white');
        }}
    }}

    function updatePrintTarget(target) {{
        document.body.classList.remove('print-dark', 'print-white');
        document.body.classList.add('print-' + target);
    }}

    const urlParams = new URLSearchParams(window.location.search);
    const initialMode = urlParams.get('mode') || 'compare';
    setViewMode(initialMode);
</script>

</body>
</html>
'''
    return html

def main():
    # 1. Update PRODUCTS references
    for p in PRODUCTS:
        if p.get("ingredients_header_ref") == "100ml / 30ml 공용":
            p["ingredients_header_ref"] = "100ml 정품 규격"

    # 2. Generate all 11 products in 110x75mm
    for p in PRODUCTS:
        html_content = render_100ml_label_html(p)
        target_path = os.path.join(out_dir, p["file_name"])
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Generated {p['name_ko']} (110x75mm, 100ml, Dark+White) -> {target_path}")

    # 3. Sync legacy files
    legacy_mappings = [
        ("monsmecta_original_30ml_94x45.html", "monsmecta"),
        ("monsmecta_renal_30ml_94x45.html", "urinary"),
        ("monsmecta_hepamax_30ml_94x45.html", "hepamax")
    ]

    for filename, pid in legacy_mappings:
        prod = next((item for item in PRODUCTS if item["id"] == pid), None)
        if prod:
            legacy_path = os.path.join(out_dir, filename)
            with open(legacy_path, "w", encoding="utf-8") as f:
                f.write(render_100ml_label_html(prod))
            print(f"Synced legacy file {filename} -> {legacy_path}")

    print("\n[SUCCESS] ALL 11 PRODUCTS GENERATED IN 110mm x 75mm (100ml)!")

if __name__ == "__main__":
    main()
