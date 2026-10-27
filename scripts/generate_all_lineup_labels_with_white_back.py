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

def render_lineup_label_html(p):
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
    if row2[1]: row2_items.append(f'<span class="eff-item" style="margin-left:2.5mm;"><span class="eff-dot"></span>{row2[1]}</span>')
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
    <title>{p["name_en"]} Label (85mm x 40mm) - Dark / White Comparison</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;800;900&family=Orbitron:wght@700;900&display=swap" rel="stylesheet">
    <style>
        @page {{
            size: 85mm 40mm;
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
                gap: 45px;
                padding: 15px 0;
            }}

            .label-card-wrapper {{
                display: flex;
                flex-direction: column;
                align-items: center;
                gap: 12px;
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
                transform: scale(2.4);
                transform-origin: top center;
                margin-bottom: 60mm;
            }}
        }}

        /* 인쇄 전용 (85mm x 40mm 1:1) */
        @media print {{
            html, body {{
                width: 85mm !important;
                height: 40mm !important;
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
                width: 85mm !important;
                height: 40mm !important;
                transform: none !important;
                box-shadow: none !important;
                margin: 0 !important;
            }}
        }}

        /* 라벨 전체 규격: 85mm x 40mm */
        .label-sheet {{
            width: 85mm;
            height: 40mm;
            background: {bg_gradient};
            color: #f8fafc;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            border: 0.15mm solid {border};
            flex-shrink: 0;
        }}

        .grid-overlay {{
            position: absolute;
            inset: 0;
            opacity: 0.08;
            background-image: 
                linear-gradient({neon} 1px, transparent 1px),
                linear-gradient(90deg, {neon} 1px, transparent 1px);
            background-size: 2.5mm 2.5mm;
            pointer-events: none;
            z-index: 1;
        }}

        /* 상단 액센트 바 (0.35mm) */
        .top-accent-bar {{
            height: 0.35mm;
            background: {top_bar};
            box-shadow: 0 0 1.2mm {neon}E6;
            z-index: 2;
            flex-shrink: 0;
        }}

        /* 콘텐츠 랩 */
        .content-wrap {{
            position: relative;
            z-index: 2;
            display: flex;
            height: calc(40mm - 0.35mm);
            width: 85mm;
            padding: 0.20mm 0.30mm 0.20mm 0.30mm;
            justify-content: space-between;
        }}

        /* 좌측: 전면 메인 노출부 (39.5mm) */
        .col-left {{
            width: 39.5mm;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}

        /* 중앙 디바이더 (1.8mm) */
        .divider-col {{
            width: 1.8mm;
            height: 100%;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .divider-line {{
            width: 0.15mm;
            height: 98%;
            background: linear-gradient(180deg, transparent, {neon}, transparent);
            opacity: 0.7;
        }}
        .divider-diamond {{
            position: absolute;
            width: 0.8mm;
            height: 0.8mm;
            background: #000;
            border: 0.15mm solid {neon};
            transform: rotate(45deg);
        }}

        /* 우측: 법정 고시사항 패널 (43.1mm) */
        .col-right {{
            width: 43.1mm;
            height: 100%;
            display: flex;
            flex-direction: column;
        }}

        /* ---------------- 좌측 전면 메인 스타일 ---------------- */
        .brand-badge {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.6mm;
            background: rgba(0, 0, 0, 0.65);
            border: 0.15mm solid {neon};
            border-radius: 999px;
            padding: 0.12mm 1.0mm;
            line-height: 1;
            box-sizing: border-box;
        }}
        .brand-badge .emoji {{
            font-size: 2.2mm;
            line-height: 1;
            display: inline-flex;
            align-items: center;
        }}
        .brand-badge .text {{
            font-size: 1.28mm;
            font-weight: 800;
            letter-spacing: 0.02em;
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
            padding: 0;
            margin: 0;
        }}
        .sub-desc {{
            font-size: 1.45mm;
            font-weight: 700;
            color: #f1f5f9;
            line-height: 1.05;
            margin-bottom: 0.04mm;
            text-shadow: 0 0 0.6mm rgba(0,0,0,0.8);
        }}
        .main-title {{
            font-size: 3.95mm;
            font-weight: 900;
            color: #ffffff;
            line-height: 1.0;
            letter-spacing: -0.03em;
            text-shadow: 0 0 1.2mm rgba(255, 255, 255, 0.5), 0 1px 2px #000;
            margin-bottom: 0.04mm;
        }}
        .en-title {{
            font-size: 1.62mm;
            font-weight: 900;
            color: {neon};
            letter-spacing: 0.05em;
            line-height: 1;
        }}

        .effects-box-wrapper {{
            position: relative;
            padding-top: 0.95mm;
            margin: 0.06mm 0;
        }}
        .effects-badge-top {{
            position: absolute;
            top: 0;
            left: 1.2mm;
            z-index: 3;
            background: {neon};
            color: #000;
            border: 0.12mm solid #000;
            border-radius: 0.25mm;
            padding: 0.05mm 0.65mm 0.23mm 0.65mm;
            font-size: 1.15mm;
            font-weight: 900;
            line-height: 1;
            box-shadow: 0 0.2mm 0.4mm rgba(0, 0, 0, 0.9);
            display: inline-flex;
            align-items: center;
            justify-content: center;
        }}
        .effects-card {{
            background: rgba(0, 0, 0, 0.60);
            border: 0.18mm solid {neon};
            border-radius: 0.4mm;
            padding: 0.85mm 0.50mm 0.25mm 0.50mm;
            display: flex;
            flex-direction: column;
            gap: 0.22mm;
        }}
        .effects-row {{
            display: flex;
            align-items: center;
            gap: 0.5mm;
            line-height: 1.05;
            white-space: nowrap;
        }}
        .eff-item {{
            font-size: 1.24mm;
            font-weight: 800;
            color: #ffffff;
            display: inline-flex;
            align-items: center;
            gap: 0.3mm;
            letter-spacing: -0.01em;
        }}
        .eff-dot {{
            width: 0.45mm;
            height: 0.45mm;
            background: {neon};
            border-radius: 50%;
            display: inline-block;
            flex-shrink: 0;
        }}
        .eff-note {{
            font-size: 0.85mm;
            color: #cbd5e1;
            font-weight: 500;
            margin-left: auto;
        }}

        .tech-box-ing {{
            background: rgba(0, 0, 0, 0.55);
            border: 0.15mm solid rgba({hex_to_rgb(neon)}, 0.45);
            border-radius: 0.4mm;
            padding: 0.18mm 0.40mm;
            display: flex;
            flex-direction: column;
            gap: 0.04mm;
        }}
        .ing-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 0.1mm solid {neon}55;
            padding-bottom: 0.06mm;
            margin-bottom: 0.04mm;
        }}
        .ing-header .title {{
            font-size: 1.15mm;
            font-weight: 800;
            color: {neon};
            line-height: 1;
        }}
        .ing-header .ref {{
            font-size: 0.95mm;
            color: {neon_pale};
            font-weight: 600;
            line-height: 1;
        }}
        .ing-row {{
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            font-size: 1.06mm;
            line-height: 1.18;
        }}
        .ing-name {{
            color: #e2e8f0;
            font-weight: 600;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            max-width: 28mm;
        }}
        .ing-val {{
            color: #ffffff;
            font-weight: 800;
            white-space: nowrap;
            flex-shrink: 0;
            margin-left: 0.4mm;
        }}

        .pack-tag {{
            align-self: center;
            background: rgba(0, 0, 0, 0.65);
            border: 0.18mm solid {neon};
            border-radius: 999px;
            padding: 0.14mm 1.4mm;
            font-size: 1.32mm;
            font-weight: 800;
            display: flex;
            gap: 0.5mm;
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
            padding: 0.15mm 0.50mm 0.12mm 0.50mm;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}

        /* 헤더 */
        .legal-header {{
            display: flex;
            flex-direction: column;
            gap: 0.14mm;
            padding-bottom: 0.08mm;
        }}
        .reg-num-line {{
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            line-height: 1.1;
        }}
        .reg-num-label {{
            font-size: 1.15mm;
            font-weight: 800;
            line-height: 1;
        }}
        .reg-num-val {{
            font-size: 1.30mm;
            font-weight: 900;
            line-height: 1;
        }}
        .feed-type-line {{
            font-size: 0.98mm;
            font-weight: 700;
            line-height: 1.15;
            white-space: nowrap;
        }}
        .feed-type-line .lbl {{
            font-weight: 800;
        }}

        /* 본문 내용 */
        .sec-content {{
            display: flex;
            flex-direction: column;
            gap: 0.06mm;
            margin: 0.01mm 0;
            text-align: left;
        }}
        .info-row {{
            display: flex;
            align-items: baseline;
            font-size: 1.15mm;
            line-height: 1.20;
            text-align: left;
        }}
        .sec-lbl {{
            font-weight: 800;
            margin-right: 0.25mm;
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
            gap: 0.02mm;
            flex: 1;
            font-weight: 600;
            line-height: 1.18;
        }}

        .effects-sub-list {{
            list-style: none;
            padding-left: 0.3mm;
            display: flex;
            flex-direction: column;
            gap: 0.03mm;
            margin: 0.01mm 0;
        }}
        .effects-sub-list li {{
            font-size: 1.12mm;
            font-weight: 600;
            line-height: 1.20;
            display: flex;
            align-items: baseline;
            gap: 0.3mm;
        }}
        .effects-sub-list .roman {{
            font-weight: 800;
            font-size: 1.05mm;
            flex-shrink: 0;
        }}

        /* 용법 및 용량 (1줄 수평 정렬) */
        .dose-box-single {{
            border-radius: 0.35mm;
            padding: 0.12mm 0.50mm;
            display: flex;
            align-items: center;
            justify-content: flex-start;
            gap: 0.4mm;
            line-height: 1.1;
            white-space: nowrap;
        }}
        .dose-box-single .title {{
            font-size: 1.15mm;
            font-weight: 900;
        }}
        .dose-box-single .desc {{
            font-size: 1.15mm;
            font-weight: 800;
        }}
        .dose-box-single .sub {{
            font-size: 0.98mm;
            font-weight: 600;
            margin-left: 0.2mm;
        }}

        /* 주의사항 */
        .warn-box-orig {{
            border: 0.15mm solid #ef4444;
            border-radius: 0.35mm;
            padding: 0.08mm 0.40mm;
            display: flex;
            flex-direction: column;
            gap: 0.02mm;
        }}
        .warn-title-orig {{
            font-size: 1.06mm;
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
            gap: 0.02mm;
        }}
        .warn-item-orig {{
            font-size: 0.98mm;
            line-height: 1.16;
            display: flex;
            align-items: baseline;
            gap: 0.2mm;
        }}
        .hl-shake {{
            font-weight: 800;
        }}

        /* 제조일자/유통기한/재활용 */
        .mfg-date-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0.04mm 0.2mm;
            font-size: 1.04mm;
            line-height: 1;
            white-space: nowrap;
        }}
        .mfg-date-row .lbl {{
            font-weight: 800;
            margin-right: 0.15mm;
        }}
        .mfg-date-row .val {{
            font-weight: 800;
        }}
        .recycle-wrap {{
            display: flex;
            align-items: center;
            gap: 0.25mm;
            flex-shrink: 0;
        }}
        .recycle-other {{
            font-size: 0.95mm;
            font-weight: 900;
            letter-spacing: -0.01em;
        }}

        /* 제조원 / 위탁제조판매원 풋터 (원본 일치: 용인 에스앤제이 / 화성 엠오바이오) */
        .original-footer {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 0.5mm;
            padding-top: 0.06mm;
            line-height: 1.15;
        }}
        .footer-seller {{
            display: flex;
            align-items: center;
            gap: 0.4mm;
            flex: 1.15;
            min-width: 0;
        }}
        .footer-maker {{
            flex: 0.85;
            min-width: 0;
        }}
        .co-logo-circle {{
            width: 3.6mm;
            height: 3.6mm;
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
            gap: 0.01mm;
            font-size: 0.82mm;
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
            border: 0.15mm solid {neon};
        }}
        #card-dark .dose-box-single .title {{ color: {neon}; }}
        #card-dark .dose-box-single .desc {{ color: #ffffff; }}
        #card-dark .dose-box-single .sub {{ color: {neon}; }}

        #card-dark .warn-box-orig {{
            background: rgba(239, 68, 68, 0.08);
            border-color: #ef4444;
        }}
        #card-dark .warn-item-orig {{ color: #ffffff; }}
        #card-dark .warn-item-orig .hl-shake {{ color: {neon}; text-decoration: underline; }}

        #card-dark .mfg-date-row .lbl {{ color: {neon}; }}
        #card-dark .mfg-date-row .val {{ color: #ffffff; }}
        #card-dark .recycle-wrap {{ color: {neon}; }}

        #card-dark .co-logo-circle {{
            border: 0.18mm solid {neon};
            box-shadow: 0 0 0.4mm rgba({hex_to_rgb(neon)}, 0.6);
        }}
        #card-dark .co-line-main {{ color: {neon}; }}
        #card-dark .co-line-sub {{ color: {neon}; }}

        /* ========================================================================= */
        /* [TYPE B: 화이트 뒷면 - 원본 내용 100% 동일, 배경만 화이트 + 텍스트 블랙] */
        /* ========================================================================= */
        #card-white .legal-panel {{
            background: #ffffff !important;
            border: 0.18mm solid #cbd5e1 !important;
            border-radius: 0.4mm;
            box-shadow: 0 0 1.2mm rgba(0,0,0,0.12);
        }}
        #card-white .reg-num-label {{ color: #000000 !important; font-weight: 900 !important; }}
        #card-white .reg-num-val {{ color: #000000 !important; font-weight: 900 !important; }}
        #card-white .feed-type-line {{ color: #000000 !important; font-weight: 700 !important; }}
        #card-white .feed-type-line .lbl {{ color: #000000 !important; font-weight: 900 !important; }}

        #card-white .sec-lbl {{ color: #000000 !important; font-weight: 900 !important; }}
        #card-white .sec-val {{ color: #000000 !important; font-weight: 700 !important; }}
        #card-white .materials-val-box {{ color: #000000 !important; font-weight: 600 !important; }}
        #card-white .effects-sub-list li {{ color: #000000 !important; font-weight: 600 !important; }}
        #card-white .effects-sub-list .roman {{ color: #000000 !important; font-weight: 900 !important; }}

        #card-white .dose-box-single {{
            background: #f8fafc !important;
            border: 0.18mm solid #cbd5e1 !important;
        }}
        #card-white .dose-box-single .title {{ color: #000000 !important; font-weight: 900 !important; }}
        #card-white .dose-box-single .desc {{ color: #000000 !important; font-weight: 800 !important; }}
        #card-white .dose-box-single .sub {{ color: #334155 !important; font-weight: 700 !important; }}

        #card-white .warn-box-orig {{
            background: #fef2f2 !important;
            border-color: #ef4444 !important;
        }}
        #card-white .warn-title-orig {{ color: #dc2626 !important; font-weight: 900 !important; }}
        #card-white .warn-item-orig {{ color: #000000 !important; font-weight: 600 !important; }}
        #card-white .warn-item-orig .hl-shake {{
            color: #b45309 !important;
            font-weight: 900 !important;
            background: #fef08a !important;
            padding: 0 0.25mm !important;
            border-radius: 0.2mm !important;
            text-decoration: none !important;
        }}

        #card-white .mfg-date-row .lbl {{ color: #000000 !important; font-weight: 900 !important; }}
        #card-white .mfg-date-row .val {{ color: #000000 !important; font-weight: 800 !important; }}
        #card-white .recycle-wrap {{ color: #000000 !important; }}
        #card-white .recycle-other {{ color: #000000 !important; }}

        #card-white .co-logo-circle {{
            border: 0.15mm solid #cbd5e1 !important;
            box-shadow: 0 0 0.3mm rgba(0,0,0,0.15);
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
        <span style="color:{neon}; font-weight:800;">{p["name_ko"]} 30ml</span>
        <span style="color:#94a3b8; font-size:12px; background:rgba(255,255,255,0.08); padding:3px 8px; border-radius:6px; border:1px solid rgba(255,255,255,0.15);">정밀 규격 85mm × 40mm</span>
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
            <span style="font-weight:400; opacity:0.85;">| 고유 아이덴티티 네온 다크 (85mm × 40mm)</span>
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
                            <span class="ref">{p.get("ingredients_header_ref", "1L 기준")}</span>
                        </div>
                        {ing_joined}
                    </div>

                    <div class="pack-tag">
                        <span>포장 단위 :</span>
                        <span class="val">30ml / 병</span>
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
                                <span class="sec-lbl">대상 :</span>
                                <span class="sec-val">{p["target"]}</span>
                            </div>
                            <div class="info-row">
                                <span class="sec-lbl">효과 :</span>
                            </div>
                            <ul class="effects-sub-list">
                                {stat_eff_joined}
                            </ul>
                        </div>

                        <!-- 1줄 수평 용법 및 용량 -->
                        <div class="dose-box-single">
                            <span class="title">용법 및 용량 :</span>
                            <span class="desc">{dosage_desc}</span>
                            <span class="sub">{dosage_sub}</span>
                        </div>

                        <!-- 주의사항 -->
                        <div class="warn-box-orig">
                            <div class="warn-title-orig">▲ 주의사항 :</div>
                            <ul class="warn-list-orig">
                                <li class="warn-item-orig"><span>1) 직사광선을 피하여 서늘한 곳에 보관하십시오.</span></li>
                                <li class="warn-item-orig"><span>2) 제품특성상 가라앉는 성분들이 있어서 <span class="hl-shake">흔들어서 사용</span> 하십시오.</span></li>
                                <li class="warn-item-orig"><span>3) 제품에 대하여 문의하실 경우 제조원 또는 판매원으로 연락하여 주시기 바랍니다</span></li>
                            </ul>
                        </div>

                        <!-- 포장/제조/유통 + 재활용 -->
                        <div class="mfg-date-row">
                            <span><span class="lbl">포장 단위 :</span> <span class="val">30ml</span></span>
                            <span><span class="lbl">제조일자 :</span> <span class="val">2026.09.15</span></span>
                            <span><span class="lbl">유통기한 :</span> <span class="val">제조일로부터 18개월</span></span>
                            <div class="recycle-wrap">
                                <svg width="2.4mm" height="2.4mm" viewBox="0 0 100 100">
                                    <path d="M50 12 L90 82 L10 82 Z" fill="none" stroke="currentColor" stroke-width="7" stroke-linejoin="round"/>
                                    <text x="50" y="65" font-size="28" font-weight="900" text-anchor="middle" fill="currentColor">플라스틱</text>
                                </svg>
                                <span class="recycle-other">OTHER</span>
                            </div>
                        </div>

                        <!-- 제조원 / 위탁제조판매원 (원본 내용 100% 동일) -->
                        <div class="original-footer">
                            <div class="footer-seller">
                                <div class="co-logo-circle">
                                    <img src="{LOGO_B64}" class="co-logo-img">
                                </div>
                                <div class="co-text-col">
                                    <div class="co-line-main">위탁제조판매원 : 에스앤제이 동물병원</div>
                                    <div class="co-line-sub">주소 : 경기도 용인시 포곡읍 선장1로 98-8</div>
                                    <div class="co-line-sub">전화번호 : 031-321-6562</div>
                                </div>
                            </div>
                            <div class="footer-maker">
                                <div class="co-text-col">
                                    <div class="co-line-main">제조원: 엠오바이오</div>
                                    <div class="co-line-sub">주소 : 경기도 화성시 팔탄면 석포로 74번길 10-25</div>
                                    <div class="co-line-sub">전화번호 : 031-458-1240</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- [CARD 2] 화이트 뒷면 라벨 (원본 내용 100% 보존, 배경만 화이트 + 글씨만 블랙) -->
    <div class="label-card-wrapper" id="card-white">
        <div class="label-type-tag tag-white no-print">
            <span>☀️ 화이트 뒷면 라벨 (우측 화이트 배경 + 블랙 텍스트)</span>
            <span style="font-weight:600; color:#475569;">| 원본 표기사항 100% 동일, 우측 배경만 화이트 및 텍스트 블랙 적용 (85mm × 40mm)</span>
        </div>
        <div class="label-sheet">
            <div class="grid-overlay"></div>
            <div class="top-accent-bar"></div>

            <div class="content-wrap">
                <!-- LEFT COLUMN (전면 메인 - 동일한 고유 컬러 다크 테마) -->
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
                            <span class="ref">{p.get("ingredients_header_ref", "1L 기준")}</span>
                        </div>
                        {ing_joined}
                    </div>

                    <div class="pack-tag">
                        <span>포장 단위 :</span>
                        <span class="val">30ml / 병</span>
                    </div>
                </div>

                <!-- CENTER DIVIDER -->
                <div class="divider-col">
                    <div class="divider-line"></div>
                    <div class="divider-diamond"></div>
                </div>

                <!-- RIGHT COLUMN (화이트 배경 + 검은 글씨 법정 패널) -->
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
                                <span class="sec-lbl">대상 :</span>
                                <span class="sec-val">{p["target"]}</span>
                            </div>
                            <div class="info-row">
                                <span class="sec-lbl">효과 :</span>
                            </div>
                            <ul class="effects-sub-list">
                                {stat_eff_joined}
                            </ul>
                        </div>

                        <!-- 1줄 수평 용법 및 용량 -->
                        <div class="dose-box-single">
                            <span class="title">용법 및 용량 :</span>
                            <span class="desc">{dosage_desc}</span>
                            <span class="sub">{dosage_sub}</span>
                        </div>

                        <!-- 주의사항 -->
                        <div class="warn-box-orig">
                            <div class="warn-title-orig">▲ 주의사항 :</div>
                            <ul class="warn-list-orig">
                                <li class="warn-item-orig"><span>1) 직사광선을 피하여 서늘한 곳에 보관하십시오.</span></li>
                                <li class="warn-item-orig"><span>2) 제품특성상 가라앉는 성분들이 있어서 <span class="hl-shake">흔들어서 사용</span> 하십시오.</span></li>
                                <li class="warn-item-orig"><span>3) 제품에 대하여 문의하실 경우 제조원 또는 판매원으로 연락하여 주시기 바랍니다</span></li>
                            </ul>
                        </div>

                        <!-- 포장/제조/유통 + 재활용 -->
                        <div class="mfg-date-row">
                            <span><span class="lbl">포장 단위 :</span> <span class="val">30ml</span></span>
                            <span><span class="lbl">제조일자 :</span> <span class="val">2026.09.15</span></span>
                            <span><span class="lbl">유통기한 :</span> <span class="val">제조일로부터 18개월</span></span>
                            <div class="recycle-wrap">
                                <svg width="2.4mm" height="2.4mm" viewBox="0 0 100 100">
                                    <path d="M50 12 L90 82 L10 82 Z" fill="none" stroke="currentColor" stroke-width="7" stroke-linejoin="round"/>
                                    <text x="50" y="65" font-size="28" font-weight="900" text-anchor="middle" fill="currentColor">플라스틱</text>
                                </svg>
                                <span class="recycle-other">OTHER</span>
                            </div>
                        </div>

                        <!-- 제조원 / 위탁제조판매원 (원본 내용 100% 동일, 글씨만 검은색) -->
                        <div class="original-footer">
                            <div class="footer-seller">
                                <div class="co-logo-circle">
                                    <img src="{LOGO_B64}" class="co-logo-img">
                                </div>
                                <div class="co-text-col">
                                    <div class="co-line-main">위탁제조판매원 : 에스앤제이 동물병원</div>
                                    <div class="co-line-sub">주소 : 경기도 용인시 포곡읍 선장1로 98-8</div>
                                    <div class="co-line-sub">전화번호 : 031-321-6562</div>
                                </div>
                            </div>
                            <div class="footer-maker">
                                <div class="co-text-col">
                                    <div class="co-line-main">제조원: 엠오바이오</div>
                                    <div class="co-line-sub">주소 : 경기도 화성시 팔탄면 석포로 74번길 10-25</div>
                                    <div class="co-line-sub">전화번호 : 031-458-1240</div>
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

        btnDark.style.background = 'rgba(30,41,59,0.8)';
        btnDark.style.color = '{neon}';
        btnDark.style.boxShadow = 'none';

        btnWhite.style.background = 'rgba(30,41,59,0.8)';
        btnWhite.style.color = '#ffffff';
        btnWhite.style.boxShadow = 'none';

        btnCompare.style.background = 'rgba(30,41,59,0.8)';
        btnCompare.style.color = '#ffffff';
        btnCompare.style.boxShadow = 'none';

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

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    if len(hex_str) == 3:
        hex_str = ''.join([c*2 for c in hex_str])
    r = int(hex_str[0:2], 16)
    g = int(hex_str[2:4], 16)
    b = int(hex_str[4:6], 16)
    return f"{r}, {g}, {b}"

# Generate all 11 products
for p in PRODUCTS:
    html_content = render_lineup_label_html(p)
    target_path = os.path.join(out_dir, p["file_name"])
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated {p['name_ko']} (85x40mm, Dark+White) -> {target_path}")

# Also update legacy/open documents:
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
            f.write(render_lineup_label_html(prod))
        print(f"Synced legacy file {filename} -> {legacy_path}")

print("ALL 11 PRODUCTS + LEGACY FILES GENERATED WITH EXACT ORIGINAL CONTENT + WHITE BACK TOGGLE!")
