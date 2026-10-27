import os
import sys

scripts_dir = os.path.dirname(os.path.abspath(__file__))
if scripts_dir not in sys.path:
    sys.path.insert(0, scripts_dir)

out_dir = r"c:\Users\master\monsmecta_landing\public\assets\labels"
os.makedirs(out_dir, exist_ok=True)

with open(os.path.join(scripts_dir, "extracted_logo_b64.txt"), encoding="utf-8") as f:
    raw_logo = f.read().strip()
    LOGO_SRC = raw_logo if raw_logo.startswith("data:") else f"data:image/png;base64,{raw_logo}"

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

    # 상표출원 ™ 표시 처리 (출원인: (주)한국아그로 / 특허청 상표출원 제40-2026-0140274호, 제40-2026-0140275호)
    tm_badge = '<span class="tm-mark">™</span>'
    name_ko_display = p["name_ko"].replace("몬스멕타", f"몬스멕타{tm_badge}")
    name_en_display = p["name_en"].replace("MONSMECTA", f"MONSMECTA{tm_badge}")

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
        stat_eff_html.append(f'<li><span class="roman">{r}</span><span>{eff}</span></li>')
    stat_eff_joined = "\n                                ".join(stat_eff_html)

    # 5. Dosage
    dosage_desc = p.get("dosage_desc", "1일 1~2ml / 체중 5kg")
    dosage_sub = p.get("dosage_sub", "( 1 펌프 = 약 1ml ) - 증상에 따라 조절 가능")

    # 6. Normalize feed_type format
    feed_type_clean = p["feed_type"].replace("l액상l", "(액상)/").replace("l", "/")

    html = f'''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>{p["name_en"]} Label (110mm x 75mm) - 균형 잡힌 고가독성 100ml 정품 규격 1:1 실측 인쇄</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@500;700;800;900&family=Orbitron:wght@700;900&display=swap" rel="stylesheet">
    
    <!-- 동적 용지 설정 스타일: A4 일반 프린터 vs 110x75mm 라벨 롤 프린터 -->
    <style id="page-style">
        @page {{
            size: A4 portrait;
            margin: 8mm auto 0 auto;
        }}
    </style>

    <style>
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
            background: #09090b;
        }}

        .orbitron {{
            font-family: 'Orbitron', sans-serif;
        }}

        @media screen {{
            html, body {{
                width: 100% !important;
                min-height: 100vh !important;
                display: flex !important;
                flex-direction: column !important;
                align-items: center !important;
                justify-content: flex-start !important;
                padding: 85px 20px 60px 20px !important;
                overflow-x: auto !important;
            }}

            .a4-calibration-header, .a4-cut-instructions, .crop-line {{
                display: none !important;
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

        @media print {{
            html, body {{
                background: #ffffff !important;
                color: #000000 !important;
                margin: 0 !important;
                padding: 0 !important;
            }}

            .no-print {{
                display: none !important;
            }}

            body.paper-a4 {{
                width: 210mm !important;
                margin: 0 auto !important;
            }}

            body.paper-a4 .labels-stage {{
                display: flex !important;
                flex-direction: column !important;
                align-items: center !important;
                width: 210mm !important;
                margin: 0 auto !important;
                padding-top: 4mm !important;
            }}

            body.paper-a4 .a4-calibration-header {{
                display: flex !important;
                flex-direction: column !important;
                align-items: center !important;
                width: 100% !important;
                margin-bottom: 6mm !important;
            }}

            body.paper-a4 .crop-marks-box {{
                position: relative !important;
                width: 110mm !important;
                height: 75mm !important;
                margin: 0 auto !important;
            }}

            body.paper-a4 .crop-line {{
                display: block !important;
                position: absolute !important;
                background: #0f172a !important;
                z-index: 9999 !important;
            }}
            body.paper-a4 .crop-tl-h {{ top: 0; left: -5mm; width: 4mm; height: 0.3mm; }}
            body.paper-a4 .crop-tl-v {{ top: -5mm; left: 0; width: 0.3mm; height: 4mm; }}
            body.paper-a4 .crop-tr-h {{ top: 0; right: -5mm; width: 4mm; height: 0.3mm; }}
            body.paper-a4 .crop-tr-v {{ top: -5mm; right: 0; width: 0.3mm; height: 4mm; }}
            body.paper-a4 .crop-bl-h {{ bottom: 0; left: -5mm; width: 4mm; height: 0.3mm; }}
            body.paper-a4 .crop-bl-v {{ bottom: -5mm; left: 0; width: 0.3mm; height: 4mm; }}
            body.paper-a4 .crop-br-h {{ bottom: 0; right: -5mm; width: 4mm; height: 0.3mm; }}
            body.paper-a4 .crop-br-v {{ bottom: -5mm; right: 0; width: 0.3mm; height: 4mm; }}

            body.paper-a4 .a4-cut-instructions {{
                display: block !important;
                margin-top: 6mm !important;
                font-size: 8.5pt !important;
                color: #334155 !important;
                text-align: center !important;
                font-weight: 700 !important;
            }}

            body.paper-roll {{
                width: 110mm !important;
                height: 75mm !important;
                margin: 0 !important;
                padding: 0 !important;
                overflow: hidden !important;
            }}
            body.paper-roll .a4-calibration-header,
            body.paper-roll .a4-cut-instructions,
            body.paper-roll .crop-line {{
                display: none !important;
            }}
            body.paper-roll .labels-stage {{
                display: block !important;
                padding: 0 !important;
                margin: 0 !important;
                width: 110mm !important;
                height: 75mm !important;
            }}
            body.paper-roll .crop-marks-box {{
                position: static !important;
                width: 110mm !important;
                height: 75mm !important;
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
                border: 0.25mm solid {border} !important;
                width: 110mm !important;
                height: 75mm !important;
                max-width: 110mm !important;
                max-height: 75mm !important;
                transform: none !important;
                box-shadow: none !important;
                margin: 0 auto !important;
            }}
        }}

        /* ========================================================================= */
        /* 라벨 캔버스: 110mm x 75mm                                                 */
        /* ========================================================================= */
        .label-sheet {{
            width: 110mm;
            height: 75mm;
            background: {bg_gradient};
            color: #f8fafc;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            border: 0.25mm solid {border};
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

        .top-accent-bar {{
            height: 0.80mm;
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
            height: calc(75mm - 0.80mm);
            width: 110mm;
            padding: 1.2mm 1.6mm;
            justify-content: space-between;
        }}

        /* 좌측: 전면 메인 노출부 (너비 52.2mm)
           -> 각 블록 간 여유 있는 breathing space 분배
        */
        .col-left {{
            width: 52.2mm;
            height: 100%;
            display: flex;
            flex-direction: column;
        }}

        /* 중앙 디바이더 (2.2mm) */
        .divider-col {{
            width: 2.2mm;
            height: 100%;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .divider-line {{
            width: 0.25mm;
            height: 98%;
            background: linear-gradient(180deg, transparent, {neon}, transparent);
            opacity: 0.7;
        }}
        .divider-diamond {{
            position: absolute;
            width: 1.5mm;
            height: 1.5mm;
            background: #000;
            border: 0.25mm solid {neon};
            transform: rotate(45deg);
        }}

        /* 우측: 법정 고시사항 패널 (너비 52.2mm) */
        .col-right {{
            width: 52.2mm;
            height: 100%;
            display: flex;
            flex-direction: column;
        }}

        /* ---------------- [좌측 전면 메인 타이포그래피] ---------------- */
        .tm-mark {{
            font-size: 0.52em;
            vertical-align: super;
            line-height: 1;
            font-weight: 800;
            margin-left: 0.3mm;
        }}

        .brand-badge {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 1.2mm;
            background: rgba(0, 0, 0, 0.75);
            border: 0.25mm solid {neon};
            border-radius: 999px;
            padding: 0.55mm 2.2mm;
            line-height: 1;
            box-sizing: border-box;
            margin-bottom: 1.6mm;
        }}
        .brand-badge .emoji {{
            font-size: 3.4mm;
            line-height: 1;
            display: inline-flex;
            align-items: center;
        }}
        .brand-badge .text {{
            font-size: 2.05mm;
            font-weight: 900;
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
            padding: 0;
            margin-bottom: 2.2mm;
        }}
        .sub-desc {{
            font-size: 1.85mm;
            font-weight: 800;
            color: {neon_pale};
            letter-spacing: -0.01em;
            line-height: 1.2;
            margin-bottom: 0.6mm;
        }}
        .main-title {{
            font-size: 5.8mm;
            font-weight: 900;
            color: #ffffff;
            letter-spacing: -0.03em;
            line-height: 1.05;
            text-shadow: 0 0 2.5mm rgba({hex_to_rgb(neon)}, 0.7);
            margin-bottom: 0.5mm;
        }}
        .en-title {{
            font-size: 2.65mm;
            font-weight: 900;
            color: {neon};
            letter-spacing: 0.07em;
            line-height: 1;
            text-shadow: 0 0 1.5mm {neon}AA;
        }}

        /* 핵심 효능 박스 */
        .core-effects-box {{
            background: rgba(0, 0, 0, 0.65);
            border: 0.25mm solid {neon};
            border-radius: 1.0mm;
            padding: 1.1mm 1.6mm 1.0mm 1.6mm;
            position: relative;
            margin-bottom: 5.2mm; /* 주요 성분 데이터 박스를 아래로 충분히 내리기 위한 여유 공간 */
        }}
        .box-tag-label {{
            position: absolute;
            top: -1.3mm;
            left: 2.2mm;
            background: {neon};
            color: #000000;
            font-size: 1.50mm;
            font-weight: 900;
            padding: 0.2mm 1.2mm;
            border-radius: 0.4mm;
            line-height: 1;
        }}
        .effects-row {{
            display: flex;
            align-items: center;
            font-size: 1.80mm;
            font-weight: 800;
            color: #f8fafc;
            line-height: 1.35;
        }}
        .effects-row:not(:last-child) {{
            margin-bottom: 0.5mm;
        }}
        .eff-item {{
            display: inline-flex;
            align-items: center;
            gap: 0.8mm;
        }}
        .eff-dot {{
            width: 1.2mm;
            height: 1.2mm;
            border-radius: 50%;
            background: {neon};
            box-shadow: 0 0 1.0mm {neon};
            flex-shrink: 0;
        }}
        .eff-note {{
            font-size: 1.40mm;
            color: {neon_sub};
            font-weight: 700;
            margin-left: auto;
        }}

        /* 주요 성분 데이터 표: 사용자의 요청대로 행간을 절반으로 줄여 컴팩트하게 배치하고 아래로 충분히 내림 */
        .ingredients-table-box {{
            background: rgba(0, 0, 0, 0.65);
            border: 0.25mm solid rgba(255, 255, 255, 0.25);
            border-radius: 1.0mm;
            padding: 1.0mm 1.5mm;
            position: relative;
            margin-bottom: 1.5mm;
            display: flex;
            flex-direction: column;
        }}
        .table-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 0.20mm solid rgba(255, 255, 255, 0.25);
            padding-bottom: 0.5mm;
            margin-bottom: 0.4mm;
        }}
        .table-title {{
            font-size: 1.85mm;
            font-weight: 900;
            color: #ffffff;
            display: flex;
            align-items: center;
            gap: 0.8mm;
        }}
        .table-title::before {{
            content: "";
            width: 1.2mm;
            height: 1.2mm;
            background: {neon};
            display: inline-block;
        }}
        .table-badge {{
            font-size: 1.40mm;
            font-weight: 800;
            color: {neon};
            background: rgba({hex_to_rgb(neon)}, 0.15);
            border: 0.20mm solid {neon};
            padding: 0.15mm 1.0mm;
            border-radius: 0.4mm;
        }}
        .ingredients-list {{
            display: flex;
            flex-direction: column;
        }}
        .ing-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 1.65mm;
            line-height: 1.2;
            border-bottom: 0.15mm solid rgba(255, 255, 255, 0.10);
            padding: 0.35mm 0; /* 기존의 절반 */
        }}
        .ing-row:last-child {{
            border-bottom: none;
            padding-bottom: 0;
        }}
        .ing-name {{
            font-weight: 800;
            color: #f1f5f9;
        }}
        .ing-val {{
            font-weight: 900;
            color: {neon};
            font-family: 'Orbitron', sans-serif;
            font-size: 1.60mm;
            letter-spacing: 0.02em;
        }}

        /* 좌측 하단 바 */
        .col-left-bottom-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(0, 0, 0, 0.8);
            border: 0.25mm solid {neon};
            border-radius: 0.8mm;
            padding: 0.8mm 1.5mm;
            margin-top: auto;
        }}
        .left-btm-brand {{
            font-size: 1.50mm;
            font-weight: 800;
            color: #e2e8f0;
            display: flex;
            align-items: center;
            gap: 1.0mm;
            white-space: nowrap;
        }}
        .left-btm-brand strong {{
            color: {neon};
            font-weight: 900;
        }}
        .left-btm-target {{
            font-size: 1.50mm;
            font-weight: 900;
            color: #000000;
            background: {neon};
            padding: 0.25mm 1.2mm;
            border-radius: 0.4mm;
            white-space: nowrap;
        }}

        /* ---------------- [우측 법정 고시사항 패널 공통 타이포그래피] ---------------- */
        .legal-panel {{
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 100%;
            padding: 0.8mm 1.3mm;
            border-radius: 1.0mm;
            font-size: 1.58mm;
            line-height: 1.38;
        }}

        .top-reg-grid {{
            display: flex;
            flex-direction: column;
            gap: 0.45mm;
            border-bottom: 0.25mm solid #cbd5e1;
            padding-bottom: 0.55mm;
        }}
        .reg-num-line {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-weight: 900;
            font-size: 1.80mm;
        }}
        .tm-dual-grid {{
            display: flex;
            flex-direction: column;
            gap: 0.3mm;
            border-top: 0.20mm dashed #cbd5e1;
            padding-top: 0.35mm;
            margin-top: 0.15mm;
        }}
        .tm-line {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 1.40mm;
            line-height: 1.25;
        }}
        .tm-lbl {{
            font-weight: 800;
        }}
        .tm-num {{
            font-weight: 800;
            letter-spacing: 0.01em;
        }}
        .tm-flag {{
            display: inline-block;
            font-size: 1.05mm;
            font-weight: 900;
            padding: 0.1mm 0.8mm;
            border-radius: 0.3mm;
            background: #0f172a;
            color: #ffffff;
            margin-right: 0.6mm;
            vertical-align: middle;
            line-height: 1.1;
        }}
        #card-dark .tm-flag {{
            background: {neon};
            color: #000000;
        }}
        .feed-type-line {{
            font-size: 1.48mm;
            line-height: 1.35;
            word-break: break-all;
        }}

        .sec-block {{
            margin-top: 0.45mm;
        }}
        .sec-line {{
            display: flex;
            align-items: baseline;
            gap: 0.8mm;
            line-height: 1.3;
        }}
        .sec-lbl {{
            font-size: 1.70mm;
            font-weight: 900;
            flex-shrink: 0;
        }}
        .sec-val {{
            font-size: 1.58mm;
            line-height: 1.3;
        }}

        .materials-val-box {{
            font-size: 1.55mm;
            line-height: 1.35;
            margin-top: 0.25mm;
            padding-left: 0.4mm;
        }}

        .effects-sub-list {{
            list-style: none;
            padding-left: 0.4mm;
            margin-top: 0.25mm;
            display: flex;
            flex-direction: column;
            gap: 0.45mm;
        }}
        .effects-sub-list li {{
            font-size: 1.55mm;
            line-height: 1.35;
            display: flex;
            align-items: baseline;
            gap: 0.8mm;
        }}
        .effects-sub-list .roman {{
            font-weight: 900;
            font-size: 1.45mm;
            flex-shrink: 0;
        }}

        .dose-box-single {{
            margin-top: 0.65mm;
            border-radius: 0.8mm;
            padding: 0.65mm 1.3mm;
            display: flex;
            flex-direction: column;
            gap: 0.3mm;
            line-height: 1.3;
        }}
        .dose-title-line {{
            display: flex;
            align-items: baseline;
            gap: 1.4mm;
        }}
        .dose-box-single .title {{
            font-weight: 900;
            font-size: 1.72mm;
            white-space: nowrap;
        }}
        .dose-box-single .desc {{
            font-weight: 800;
            font-size: 1.70mm;
            white-space: nowrap;
        }}
        .dose-box-single .sub {{
            font-size: 1.38mm;
            font-weight: 700;
            line-height: 1.25;
            padding-left: 0.4mm;
        }}

        .warn-grid {{
            margin-top: 0.45mm;
            display: flex;
            flex-direction: column;
            gap: 0.35mm;
            font-size: 1.45mm;
            line-height: 1.35;
        }}
        .warn-header {{
            font-weight: 900;
            font-size: 1.62mm;
            display: flex;
            align-items: center;
            gap: 0.4mm;
        }}
        .warn-item-orig {{
            display: flex;
            gap: 0.4mm;
        }}

        .meta-bottom-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 0.55mm;
            border-top: 0.25mm solid #cbd5e1;
            padding-top: 0.55mm;
            font-size: 1.55mm;
            font-weight: 800;
        }}
        .mfg-date-row {{
            display: flex;
            align-items: center;
            gap: 0.8mm;
        }}
        .mfg-date-row .lbl {{
            font-weight: 900;
        }}
        .recycle-wrap {{
            display: flex;
            align-items: center;
            gap: 0.6mm;
            font-size: 1.35mm;
            font-weight: 900;
        }}
        .recycle-triangle {{
            width: 3.6mm;
            height: 3.6mm;
            border: 0.28mm solid currentColor;
            transform: rotate(45deg);
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 0.4mm;
        }}
        .recycle-triangle span {{
            transform: rotate(-45deg);
            font-size: 0.95mm;
            font-weight: 900;
            line-height: 1;
        }}

        /* 하단 푸터: 사용자 요청에 따라 글씨 크기를 대폭 늘리고 선명하게 배치 */
        .original-footer {{
            margin-top: 0.7mm;
            border-top: 0.25mm solid #cbd5e1;
            padding-top: 0.7mm;
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            gap: 1.0mm;
        }}
        .footer-seller {{
            display: flex;
            align-items: flex-start;
            gap: 1.0mm;
            flex: 1.08;
        }}
        .footer-maker {{
            flex: 1.0;
            border-left: 0.25mm solid #cbd5e1;
            padding-left: 1.2mm;
        }}
        .co-logo-circle {{
            width: 7.2mm;
            height: 7.2mm;
            border-radius: 50%;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            background: #ffffff;
            border: 0.25mm solid #cbd5e1;
            margin-top: 0.3mm;
        }}
        .co-logo-img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}
        .co-text-col {{
            display: flex;
            flex-direction: column;
            gap: 0.3mm;
            line-height: 1.25;
            min-width: 0;
        }}
        .co-line-main {{
            font-size: 1.70mm; /* 대폭 확대 */
            font-weight: 900;
            white-space: nowrap;
            letter-spacing: -0.02em;
        }}
        .co-line-sub {{
            font-size: 1.48mm; /* 대폭 확대 */
            font-weight: 700;
            line-height: 1.3;
            letter-spacing: -0.02em;
            word-break: keep-all;
        }}
        .co-tel-line {{
            font-size: 1.45mm;
            font-weight: 800;
            white-space: nowrap;
            letter-spacing: -0.01em;
            margin-top: 0.1mm;
        }}

        /* ========================================================================= */
        /* [TYPE A: 원본 올 다크 스타일] */
        /* ========================================================================= */
        #card-dark .legal-panel {{
            background: rgba(0, 0, 0, 0.45);
            border: 0.25mm solid rgba(255, 255, 255, 0.2);
            color: #e2e8f0;
        }}
        #card-dark .top-reg-grid {{
            border-bottom: 0.25mm solid rgba(255, 255, 255, 0.2);
        }}
        #card-dark .tm-dual-grid {{
            border-top: 0.20mm dashed rgba(255, 255, 255, 0.25);
        }}
        #card-dark .tm-line .tm-lbl {{ color: {neon}; font-weight: 800; }}
        #card-dark .tm-line .tm-num {{ color: #fef08a; font-weight: 900; }}
        #card-dark .reg-num-label {{ color: {neon}; font-weight: 900; }}
        #card-dark .reg-num-val {{ color: #ffffff; font-weight: 900; }}
        #card-dark .feed-type-line {{ color: #cbd5e1; font-weight: 700; }}
        #card-dark .feed-type-line .lbl {{ color: {neon}; font-weight: 900; }}

        #card-dark .sec-lbl {{ color: {neon}; font-weight: 900; }}
        #card-dark .sec-val {{ color: #ffffff; font-weight: 800; }}
        #card-dark .materials-val-box {{ color: #cbd5e1; font-weight: 700; }}
        #card-dark .effects-sub-list li {{ color: #f1f5f9; font-weight: 700; }}
        #card-dark .effects-sub-list .roman {{ color: {neon}; font-weight: 900; }}

        #card-dark .dose-box-single {{
            background: rgba({hex_to_rgb(neon)}, 0.12);
            border: 0.25mm solid {neon};
        }}
        #card-dark .dose-box-single .title {{ color: {neon}; font-weight: 900; }}
        #card-dark .dose-box-single .desc {{ color: #ffffff; font-weight: 900; }}
        #card-dark .dose-box-single .sub {{ color: {neon}; font-weight: 800; }}

        #card-dark .warn-header {{ color: #f87171; font-weight: 900; }}
        #card-dark .warn-item-orig {{ color: #f1f5f9; font-weight: 700; }}
        #card-dark .warn-item-orig .hl-shake {{
            color: #fef08a;
            font-weight: 900;
            text-decoration: underline;
        }}

        #card-dark .meta-bottom-row {{
            border-top: 0.25mm solid rgba(255, 255, 255, 0.2);
        }}
        #card-dark .mfg-date-row .lbl {{ color: {neon}; font-weight: 900; }}
        #card-dark .mfg-date-row .val {{ color: #ffffff; font-weight: 800; }}
        #card-dark .recycle-wrap {{ color: {neon}; }}
        #card-dark .recycle-other {{ color: #ffffff; font-weight: 900; }}

        #card-dark .original-footer {{
            border-top: 0.25mm solid rgba(255, 255, 255, 0.2);
        }}
        #card-dark .footer-maker {{
            border-left: 0.25mm solid rgba(255, 255, 255, 0.2);
            padding-left: 1.2mm;
        }}
        #card-dark .co-logo-circle {{
            border: 0.25mm solid {neon};
            box-shadow: 0 0 1.0mm rgba({hex_to_rgb(neon)}, 0.4);
        }}
        #card-dark .co-line-main {{ color: #ffffff; font-weight: 900; }}
        #card-dark .co-line-sub {{ color: #94a3b8; font-weight: 700; }}

        /* ========================================================================= */
        /* [TYPE B: 화이트 뒷면 가독성 특화 스타일] */
        /* ========================================================================= */
        #card-white .col-right {{
            background: #ffffff !important;
            border-radius: 0 0.8mm 0.8mm 0;
            box-shadow: inset 0 0 2.5mm rgba(0, 0, 0, 0.08);
        }}
        #card-white .legal-panel {{
            background: #ffffff !important;
            color: #000000 !important;
        }}
        #card-white .top-reg-grid {{
            border-bottom: 0.25mm solid #94a3b8 !important;
        }}
        #card-white .tm-dual-grid {{
            border-top: 0.20mm dashed #94a3b8 !important;
        }}
        #card-white .tm-line .tm-lbl {{ color: #000000 !important; font-weight: 900 !important; }}
        #card-white .tm-line .tm-num {{ color: #000000 !important; font-weight: 900 !important; }}

        #card-white .reg-num-label {{ color: #000000 !important; font-weight: 900 !important; }}
        #card-white .reg-num-val {{ color: #000000 !important; font-weight: 900 !important; }}
        #card-white .feed-type-line {{ color: #000000 !important; font-weight: 700 !important; }}
        #card-white .feed-type-line .lbl {{ color: #000000 !important; font-weight: 900 !important; }}

        #card-white .sec-lbl {{ color: #000000 !important; font-weight: 900 !important; }}
        #card-white .sec-val {{ color: #000000 !important; font-weight: 800 !important; }}
        #card-white .materials-val-box {{ color: #000000 !important; font-weight: 700 !important; }}
        #card-white .effects-sub-list li {{ color: #000000 !important; font-weight: 700 !important; }}
        #card-white .effects-sub-list .roman {{ color: #000000 !important; font-weight: 900 !important; }}

        #card-white .dose-box-single {{
            background: #f1f5f9 !important;
            border: 0.30mm solid #000000 !important;
        }}
        #card-white .dose-box-single .title {{ color: #000000 !important; font-weight: 900 !important; }}
        #card-white .dose-box-single .desc {{ color: #000000 !important; font-weight: 900 !important; }}
        #card-white .dose-box-single .sub {{ color: #1e293b !important; font-weight: 800 !important; }}

        #card-white .warn-header {{ color: #dc2626 !important; font-weight: 900 !important; }}
        #card-white .warn-item-orig {{ color: #000000 !important; font-weight: 700 !important; }}
        #card-white .warn-item-orig .hl-shake {{
            color: #b91c1c !important;
            font-weight: 900 !important;
            text-decoration: underline !important;
        }}

        #card-white .meta-bottom-row {{
            border-top: 0.25mm solid #94a3b8 !important;
        }}
        #card-white .mfg-date-row .lbl {{ color: #000000 !important; font-weight: 900 !important; }}
        #card-white .mfg-date-row .val {{ color: #000000 !important; font-weight: 800 !important; }}
        #card-white .recycle-wrap {{ color: #000000 !important; }}
        #card-white .recycle-other {{ color: #000000 !important; font-weight: 900 !important; }}

        #card-white .original-footer {{
            border-top: 0.25mm solid #94a3b8 !important;
        }}
        #card-white .footer-maker {{
            border-left: 0.25mm solid #94a3b8 !important;
            padding-left: 1.2mm;
        }}
        #card-white .co-logo-circle {{
            border: 0.25mm solid #cbd5e1 !important;
            box-shadow: 0 0 0.8mm rgba(0,0,0,0.2);
        }}
        #card-white .co-line-main {{ color: #000000 !important; font-weight: 900 !important; }}
        #card-white .co-line-sub {{ color: #0f172a !important; font-weight: 700 !important; }}

        #card-white .divider-line {{
            background: linear-gradient(180deg, transparent, {border}, transparent) !important;
        }}
        #card-white .divider-diamond {{
            background: #fff !important;
            border-color: {border} !important;
        }}
    </style>
</head>
<body class="mode-white print-white paper-a4">

<!-- 상단 실시간 인쇄/뷰어 인터랙티브 툴바 (화면 표시 전용) -->
<div class="no-print" style="position:fixed; top:10px; left:50%; transform:translateX(-50%); z-index:99999; background:rgba(15,23,42,0.96); border:1px solid {neon}; padding:10px 20px; border-radius:14px; display:flex; align-items:center; gap:12px; box-shadow:0 12px 35px rgba(0,0,0,0.85); backdrop-filter:blur(10px); font-family:sans-serif; max-width:98vw; overflow-x:auto;">
    <div style="color:#ffffff; font-size:13px; font-weight:700; display:flex; align-items:center; gap:8px; white-space:nowrap;">
        <span style="color:{neon}; font-size:16px;">★</span>
        <span style="color:{neon}; font-weight:900;">{p["name_ko"]} 100ml</span>
        <span style="color:#38bdf8; font-size:11px; background:rgba(56,189,248,0.12); padding:3px 8px; border-radius:6px; border:1px solid rgba(56,189,248,0.3); font-weight:800;">110mm × 75mm (1:1 실측)</span>
        <span style="color:#fde047; font-size:11px; background:rgba(253,224,71,0.15); padding:3px 8px; border-radius:6px; border:1px solid rgba(253,224,71,0.35); font-weight:800;">특허청 상표출원 완료</span>
    </div>

    <div style="height:20px; width:1px; background:rgba(255,255,255,0.2);"></div>

    <!-- 인쇄 용지 규격 선택 (A4 vs 롤 라벨) -->
    <div style="display:flex; align-items:center; gap:6px; background:rgba(0,0,0,0.5); padding:3px 6px; border-radius:8px; border:1px solid rgba(255,255,255,0.15);">
        <span style="color:#94a3b8; font-size:11px; font-weight:700; margin-right:4px;">인쇄 규격:</span>
        <button id="btn-paper-a4" onclick="setPaperMode('a4')" style="background:#0284c7; color:#ffffff; border:1px solid #38bdf8; padding:5px 12px; border-radius:6px; font-size:12px; font-weight:800; cursor:pointer; transition:all 0.2s; white-space:nowrap;">
            📄 A4 실측 (자르기 가이드)
        </button>
        <button id="btn-paper-roll" onclick="setPaperMode('roll')" style="background:rgba(30,41,59,0.8); color:#94a3b8; border:1px solid #475569; padding:5px 12px; border-radius:6px; font-size:12px; font-weight:800; cursor:pointer; transition:all 0.2s; white-space:nowrap;">
            🏷️ 롤 라벨지 (110x75mm)
        </button>
    </div>

    <div style="height:20px; width:1px; background:rgba(255,255,255,0.2);"></div>

    <!-- 라벨 디자인 탭 전환 (화이트 뒷면 vs 올 다크) -->
    <div style="display:flex; align-items:center; gap:6px; background:rgba(0,0,0,0.5); padding:3px 6px; border-radius:8px; border:1px solid rgba(255,255,255,0.15);">
        <span style="color:#94a3b8; font-size:11px; font-weight:700; margin-right:4px;">디자인:</span>
        <button id="btn-white-label" onclick="setViewMode('white')" style="background:linear-gradient(135deg, {neon}, {neon_sub}); color:#000000; border:1px solid {neon}; padding:5px 12px; border-radius:6px; font-size:12px; font-weight:900; cursor:pointer; transition:all 0.2s; white-space:nowrap; box-shadow:0 0 10px rgba({hex_to_rgb(neon)},0.4);">
            ☀️ 화이트 뒷면 (가독성 특화)
        </button>
        <button id="btn-dark-label" onclick="setViewMode('dark')" style="background:rgba(30,41,59,0.8); color:#94a3b8; border:1px solid #475569; padding:5px 12px; border-radius:6px; font-size:12px; font-weight:800; cursor:pointer; transition:all 0.2s; white-space:nowrap;">
            🌙 오리지널 다크
        </button>
        <button id="btn-compare-label" onclick="setViewMode('compare')" style="background:rgba(30,41,59,0.8); color:#94a3b8; border:1px solid #475569; padding:5px 10px; border-radius:6px; font-size:12px; font-weight:700; cursor:pointer; transition:all 0.2s; white-space:nowrap;">
            👀 둘 다 비교
        </button>
    </div>

    <!-- 인쇄 실행 버튼 -->
    <button onclick="doPrint()" style="background:#10b981; color:#ffffff; border:none; padding:6px 16px; border-radius:8px; font-size:13px; font-weight:900; cursor:pointer; display:flex; align-items:center; gap:6px; box-shadow:0 0 12px rgba(16,185,129,0.5); white-space:nowrap;">
        <span>🖨️ 인쇄 (Ctrl+P)</span>
    </button>
</div>

<div class="labels-stage">

    <!-- [A4 인쇄 전용 헤더: 50mm 실측 캘리브레이션 자] -->
    <div class="a4-calibration-header">
        <div style="font-size:11pt; font-weight:900; color:#0f172a; margin-bottom:2mm;">
            [100ml 정품 규격] 몬스멕타™ {p["name_ko"].replace("몬스멕타 ", "")} 용기 라벨 (110mm × 75mm)
        </div>
        <div style="font-size:8.5pt; color:#475569; margin-bottom:3mm;">
            ※ 인쇄 설정 시 반드시 <strong>[배율: 맞춤(100%)]</strong> 또는 <strong>[실제 크기(Actual Size)]</strong>로 지정하십시오.
        </div>
        <div style="display:flex; align-items:center; gap:3mm; font-size:8pt; font-family:monospace; color:#334155;">
            <span>실측 확인용 눈금자:</span>
            <div style="width:50mm; height:5mm; border:0.3mm solid #0f172a; border-top:none; display:flex; justify-content:space-between; position:relative;">
                <div style="position:absolute; top:0; left:0; width:0.3mm; height:3mm; background:#0f172a;"></div>
                <div style="position:absolute; top:0; left:10mm; width:0.3mm; height:2mm; background:#0f172a;"></div>
                <div style="position:absolute; top:0; left:20mm; width:0.3mm; height:2mm; background:#0f172a;"></div>
                <div style="position:absolute; top:0; left:30mm; width:0.3mm; height:2mm; background:#0f172a;"></div>
                <div style="position:absolute; top:0; left:40mm; width:0.3mm; height:2mm; background:#0f172a;"></div>
                <div style="position:absolute; top:0; right:0; width:0.3mm; height:3mm; background:#0f172a;"></div>
                <span style="position:absolute; bottom:0.5mm; left:1mm; font-size:6.5pt;">0</span>
                <span style="position:absolute; bottom:0.5mm; right:1mm; font-size:6.5pt;">50mm (5cm)</span>
            </div>
            <span style="font-size:7.5pt; color:#64748b;">(자로 재었을 때 정확히 5cm여야 합니다)</span>
        </div>
    </div>

    <!-- [CARD 1: 화이트 뒷면 라벨 (Type B) - 기본 권장] -->
    <div class="label-card-wrapper" id="card-white">
        <div class="label-type-tag tag-white no-print">
            <span>☀️ 화이트 뒷면 (인쇄 권장 규격)</span>
            <span style="font-weight:600; color:#475569;">| 법정 고시사항 100% 선명 흑백 대비 (110mm × 75mm / 100ml)</span>
        </div>
        <div class="crop-marks-box">
            <div class="crop-line crop-tl-h"></div>
            <div class="crop-line crop-tl-v"></div>
            <div class="crop-line crop-tr-h"></div>
            <div class="crop-line crop-tr-v"></div>
            <div class="crop-line crop-bl-h"></div>
            <div class="crop-line crop-bl-v"></div>
            <div class="crop-line crop-br-h"></div>
            <div class="crop-line crop-br-v"></div>

            <div class="label-sheet">
                <div class="grid-overlay"></div>
                <div class="top-accent-bar"></div>

                <div class="content-wrap">
                    <!-- LEFT COLUMN -->
                    <div class="col-left">
                        <div class="brand-badge">
                            <span class="emoji">🐶</span>
                            <span class="text"><span class="accent">S&J</span>&nbsp;ADVANCED VET FORMULA</span>
                            <span class="emoji">🐱</span>
                        </div>

                        <div class="hero-section">
                            <div class="sub-desc">{p["sub_desc"]}</div>
                            <h1 class="main-title">{name_ko_display}</h1>
                            <h2 class="en-title orbitron">{name_en_display}</h2>
                        </div>

                        <div class="core-effects-box">
                            <div class="box-tag-label">핵심 효능</div>
                            <div class="effects-row" style="margin-top: 0.6mm;">
                                {row1_html}
                            </div>
                            <div class="effects-row">
                                {row2_joined}
                            </div>
                        </div>

                        <div class="ingredients-table-box">
                            <div class="table-header">
                                <span class="table-title">주요 성분 데이터</span>
                                <span class="table-badge">100ml 정품 규격</span>
                            </div>
                            <div class="ingredients-list">
                                {ing_joined}
                            </div>
                        </div>

                        <div class="col-left-bottom-bar">
                            <div class="left-btm-brand">
                                <strong>S&J VET FORMULA</strong>&nbsp;· 동물병원 처방
                            </div>
                            <div class="left-btm-target">반려견·반려묘 (100ml)</div>
                        </div>
                    </div>

                    <!-- CENTER DIVIDER -->
                    <div class="divider-col">
                        <div class="divider-line"></div>
                        <div class="divider-diamond"></div>
                    </div>

                    <!-- RIGHT COLUMN -->
                    <div class="col-right">
                        <div class="legal-panel">
                            <div class="top-reg-grid">
                                <div class="reg-num-line">
                                    <span class="reg-num-label">성분등록번호</span>
                                    <span class="reg-num-val">{p["reg_no"]}</span>
                                </div>
                                <div class="tm-dual-grid">
                                    <div class="tm-line">
                                        <span class="tm-lbl">🇰🇷 특허청 상표출원</span>
                                        <span class="tm-num">제40-2026-0140274호 (05류/31류)</span>
                                    </div>
                                    <div class="tm-line">
                                        <span class="tm-lbl">🇺🇸 미국 USPTO 출원</span>
                                        <span class="tm-num orbitron">App No. 50/041,096</span>
                                    </div>
                                </div>
                                <div class="feed-type-line">
                                    <span class="lbl">사료의 명칭 및 형태 :</span>
                                    <span>{feed_type_clean}</span>
                                </div>
                                <div class="feed-type-line">
                                    <span class="lbl">등록성분량 :</span>
                                    <span>{p["reg_ing"]}</span>
                                </div>
                            </div>

                            <div class="sec-block">
                                <div class="sec-line">
                                    <span class="sec-lbl">사용원료 :</span>
                                </div>
                                <div class="materials-val-box">
                                    {raw_mat_html}
                                </div>
                            </div>

                            <div class="sec-block">
                                <div class="sec-line">
                                    <span class="sec-lbl">효능 및 효과 :</span>
                                </div>
                                <ul class="effects-sub-list">
                                    {stat_eff_joined}
                                </ul>
                            </div>

                            <div class="dose-box-single">
                                <div class="dose-title-line">
                                    <span class="title">급여방법 :</span>
                                    <span class="desc">{dosage_desc}</span>
                                </div>
                                <div class="sub">{dosage_sub}</div>
                            </div>

                            <div class="warn-grid">
                                <div class="warn-header">
                                    <span>주의사항</span>
                                </div>
                                <div class="warn-item-orig">
                                    <span>1) 직사광선을 피하여 건조하고 서늘한 곳에 보관하십시오.</span>
                                </div>
                                <div class="warn-item-orig">
                                    <span>2) 제품 특성상 가라앉는 성분이 있으므로 <span class="hl-shake">흔들어서 사용</span>하십시오.</span>
                                </div>
                                <div class="warn-item-orig">
                                    <span>3) 제품에 대하여 문의하실 경우 제조원 또는 판매원으로 연락하여 주시기 바랍니다.</span>
                                </div>
                            </div>

                            <div class="meta-bottom-row">
                                <div style="display:flex; align-items:baseline; gap:0.8mm;">
                                    <span>중량 :</span>
                                    <strong style="font-size:1.75mm; color:#000000;">100ml</strong>
                                </div>
                                <div class="mfg-date-row">
                                    <span class="lbl">제조일자 :</span>
                                    <span class="val">별도표기</span>
                                </div>
                                <div>유통기한 : 18개월</div>
                                <div class="recycle-wrap">
                                    <div class="recycle-triangle">
                                        <span>플라스틱</span>
                                    </div>
                                    <span class="recycle-other">OTHER</span>
                                </div>
                            </div>

                                                        <div class="original-footer">
                                <div class="footer-seller">
                                    <div class="co-logo-circle">
                                        <img src="{LOGO_SRC}" class="co-logo-img" alt="S&J">
                                    </div>
                                    <div class="co-text-col">
                                        <div class="co-line-main">위탁제조판매원 : 에스앤제이 동물병원</div>
                                        <div class="co-line-sub">경기도 용인시 처인구<br>포곡읍 선장1로 98-8</div>
                                        <div class="co-tel-line"><span style="font-weight:900;">TEL</span> 031-321-6562</div>
                                    </div>
                                </div>
                                <div class="footer-maker">
                                    <div class="co-text-col">
                                        <div class="co-line-main">제조원 : 엠오 바이오</div>
                                        <div class="co-line-sub">화성시 팔탄면<br>석포로 74번길 10-25</div>
                                        <div class="co-tel-line"><span style="font-weight:900;">TEL</span> 031-458-1240</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- [CARD 2: 오리지널 올 다크 라벨 (Type A)] -->
    <div class="label-card-wrapper" id="card-dark" style="display:none;">
        <div class="label-type-tag tag-dark no-print">
            <span>🌙 오리지널 풀 네온 다크</span>
            <span style="font-weight:600; color:#94a3b8;">| 딥 블랙 배경 & 네온 발광 테마 (110mm × 75mm / 100ml)</span>
        </div>
        <div class="crop-marks-box">
            <div class="crop-line crop-tl-h"></div>
            <div class="crop-line crop-tl-v"></div>
            <div class="crop-line crop-tr-h"></div>
            <div class="crop-line crop-tr-v"></div>
            <div class="crop-line crop-bl-h"></div>
            <div class="crop-line crop-bl-v"></div>
            <div class="crop-line crop-br-h"></div>
            <div class="crop-line crop-br-v"></div>

            <div class="label-sheet">
                <div class="grid-overlay"></div>
                <div class="top-accent-bar"></div>

                <div class="content-wrap">
                    <!-- LEFT COLUMN -->
                    <div class="col-left">
                        <div class="brand-badge">
                            <span class="emoji">🐶</span>
                            <span class="text"><span class="accent">S&J</span>&nbsp;ADVANCED VET FORMULA</span>
                            <span class="emoji">🐱</span>
                        </div>

                        <div class="hero-section">
                            <div class="sub-desc">{p["sub_desc"]}</div>
                            <h1 class="main-title">{name_ko_display}</h1>
                            <h2 class="en-title orbitron">{name_en_display}</h2>
                        </div>

                        <div class="core-effects-box">
                            <div class="box-tag-label">핵심 효능</div>
                            <div class="effects-row" style="margin-top: 0.6mm;">
                                {row1_html}
                            </div>
                            <div class="effects-row">
                                {row2_joined}
                            </div>
                        </div>

                        <div class="ingredients-table-box">
                            <div class="table-header">
                                <span class="table-title">주요 성분 데이터</span>
                                <span class="table-badge">100ml 정품 규격</span>
                            </div>
                            <div class="ingredients-list">
                                {ing_joined}
                            </div>
                        </div>

                        <div class="col-left-bottom-bar">
                            <div class="left-btm-brand">
                                <strong>S&J VET FORMULA</strong>&nbsp;· 동물병원 처방
                            </div>
                            <div class="left-btm-target">반려견·반려묘 (100ml)</div>
                        </div>
                    </div>

                    <!-- CENTER DIVIDER -->
                    <div class="divider-col">
                        <div class="divider-line"></div>
                        <div class="divider-diamond"></div>
                    </div>

                    <!-- RIGHT COLUMN -->
                    <div class="col-right">
                        <div class="legal-panel">
                            <div class="top-reg-grid">
                                <div class="reg-num-line">
                                    <span class="reg-num-label">성분등록번호</span>
                                    <span class="reg-num-val">{p["reg_no"]}</span>
                                </div>
                                <div class="tm-dual-grid">
                                    <div class="tm-line">
                                        <span class="tm-lbl">🇰🇷 특허청 상표출원</span>
                                        <span class="tm-num">제40-2026-0140274호 (05류/31류)</span>
                                    </div>
                                    <div class="tm-line">
                                        <span class="tm-lbl">🇺🇸 미국 USPTO 출원</span>
                                        <span class="tm-num orbitron">App No. 50/041,096</span>
                                    </div>
                                </div>
                                <div class="feed-type-line">
                                    <span class="lbl">사료의 명칭 및 형태 :</span>
                                    <span>{feed_type_clean}</span>
                                </div>
                                <div class="feed-type-line">
                                    <span class="lbl">등록성분량 :</span>
                                    <span>{p["reg_ing"]}</span>
                                </div>
                            </div>

                            <div class="sec-block">
                                <div class="sec-line">
                                    <span class="sec-lbl">사용원료 :</span>
                                </div>
                                <div class="materials-val-box">
                                    {raw_mat_html}
                                </div>
                            </div>

                            <div class="sec-block">
                                <div class="sec-line">
                                    <span class="sec-lbl">효능 및 효과 :</span>
                                </div>
                                <ul class="effects-sub-list">
                                    {stat_eff_joined}
                                </ul>
                            </div>

                            <div class="dose-box-single">
                                <div class="dose-title-line">
                                    <span class="title">급여방법 :</span>
                                    <span class="desc">{dosage_desc}</span>
                                </div>
                                <div class="sub">{dosage_sub}</div>
                            </div>

                            <div class="warn-grid">
                                <div class="warn-header">
                                    <span>주의사항</span>
                                </div>
                                <div class="warn-item-orig">
                                    <span>1) 직사광선을 피하여 건조하고 서늘한 곳에 보관하십시오.</span>
                                </div>
                                <div class="warn-item-orig">
                                    <span>2) 제품 특성상 가라앉는 성분이 있으므로 <span class="hl-shake">흔들어서 사용</span>하십시오.</span>
                                </div>
                                <div class="warn-item-orig">
                                    <span>3) 제품에 대하여 문의하실 경우 제조원 또는 판매원으로 연락하여 주시기 바랍니다.</span>
                                </div>
                            </div>

                            <div class="meta-bottom-row">
                                <div style="display:flex; align-items:baseline; gap:0.8mm;">
                                    <span>중량 :</span>
                                    <strong style="font-size:1.75mm; color:#ffffff;">100ml</strong>
                                </div>
                                <div class="mfg-date-row">
                                    <span class="lbl">제조일자 :</span>
                                    <span class="val">별도표기</span>
                                </div>
                                <div>유통기한 : 18개월</div>
                                <div class="recycle-wrap">
                                    <div class="recycle-triangle">
                                        <span>플라스틱</span>
                                    </div>
                                    <span class="recycle-other">OTHER</span>
                                </div>
                            </div>

                                                        <div class="original-footer">
                                <div class="footer-seller">
                                    <div class="co-logo-circle">
                                        <img src="{LOGO_SRC}" class="co-logo-img" alt="S&J">
                                    </div>
                                    <div class="co-text-col">
                                        <div class="co-line-main">위탁제조판매원 : 에스앤제이 동물병원</div>
                                        <div class="co-line-sub">경기도 용인시 처인구<br>포곡읍 선장1로 98-8</div>
                                        <div class="co-tel-line"><span style="font-weight:900;">TEL</span> 031-321-6562</div>
                                    </div>
                                </div>
                                <div class="footer-maker">
                                    <div class="co-text-col">
                                        <div class="co-line-main">제조원 : 엠오 바이오</div>
                                        <div class="co-line-sub">화성시 팔탄면<br>석포로 74번길 10-25</div>
                                        <div class="co-tel-line"><span style="font-weight:900;">TEL</span> 031-458-1240</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- [A4 인쇄 안내 문구] -->
    <div class="a4-cut-instructions">
        ✂️ 검정색 테두리 코너 재단선(Crop Marks)을 따라 칼이나 가위로 자르면 정확히 <strong>110mm × 75mm 정품 라벨</strong>이 완성됩니다.
    </div>

</div>

<!-- 인터랙티브 스위처 자바스크립트 -->
<script>
    let currentPaper = 'a4';
    let currentDesign = 'white';

    function setPaperMode(mode) {{
        currentPaper = mode;
        const pageStyle = document.getElementById('page-style');
        const btnA4 = document.getElementById('btn-paper-a4');
        const btnRoll = document.getElementById('btn-paper-roll');

        if (mode === 'a4') {{
            document.body.classList.remove('paper-roll');
            document.body.classList.add('paper-a4');
            pageStyle.innerHTML = '@page {{ size: A4 portrait; margin: 8mm auto 0 auto; }}';
            btnA4.style.background = '#0284c7';
            btnA4.style.color = '#ffffff';
            btnA4.style.borderColor = '#38bdf8';
            btnRoll.style.background = 'rgba(30,41,59,0.8)';
            btnRoll.style.color = '#94a3b8';
            btnRoll.style.borderColor = '#475569';
        }} else {{
            document.body.classList.remove('paper-a4');
            document.body.classList.add('paper-roll');
            pageStyle.innerHTML = '@page {{ size: 110mm 75mm; margin: 0; }}';
            btnRoll.style.background = '#0284c7';
            btnRoll.style.color = '#ffffff';
            btnRoll.style.borderColor = '#38bdf8';
            btnA4.style.background = 'rgba(30,41,59,0.8)';
            btnA4.style.color = '#94a3b8';
            btnA4.style.borderColor = '#475569';
        }}
    }}

    function setViewMode(mode) {{
        currentDesign = mode;
        const cardDark = document.getElementById('card-dark');
        const cardWhite = document.getElementById('card-white');
        const btnDark = document.getElementById('btn-dark-label');
        const btnWhite = document.getElementById('btn-white-label');
        const btnCompare = document.getElementById('btn-compare-label');

        [btnDark, btnWhite, btnCompare].forEach(b => {{
            b.style.background = 'rgba(30,41,59,0.8)';
            b.style.color = '#94a3b8';
            b.style.borderColor = '#475569';
            b.style.boxShadow = 'none';
        }});

        document.body.classList.remove('print-dark', 'print-white', 'mode-dark', 'mode-white', 'mode-compare');

        if (mode === 'dark') {{
            cardDark.style.display = 'flex';
            cardWhite.style.display = 'none';
            btnDark.style.background = 'linear-gradient(135deg, #1e293b, #0f172a)';
            btnDark.style.color = '{neon}';
            btnDark.style.borderColor = '{neon}';
            btnDark.style.boxShadow = '0 0 10px rgba({hex_to_rgb(neon)},0.3)';
            document.body.classList.add('mode-dark', 'print-dark');
        }} else if (mode === 'white') {{
            cardDark.style.display = 'none';
            cardWhite.style.display = 'flex';
            btnWhite.style.background = 'linear-gradient(135deg, {neon}, {neon_sub})';
            btnWhite.style.color = '#000000';
            btnWhite.style.borderColor = '{neon}';
            btnWhite.style.boxShadow = '0 0 10px rgba({hex_to_rgb(neon)},0.4)';
            document.body.classList.add('mode-white', 'print-white');
        }} else {{
            cardDark.style.display = 'flex';
            cardWhite.style.display = 'flex';
            btnCompare.style.background = '#2563eb';
            btnCompare.style.color = '#ffffff';
            btnCompare.style.borderColor = '#60a5fa';
            document.body.classList.add('mode-compare', 'print-white');
        }}
    }}

    function doPrint() {{
        if (currentDesign === 'dark') {{
            document.body.classList.remove('print-white');
            document.body.classList.add('print-dark');
        }} else {{
            document.body.classList.remove('print-dark');
            document.body.classList.add('print-white');
        }}
        window.print();
    }}

    const urlParams = new URLSearchParams(window.location.search);
    const initialMode = urlParams.get('mode') || 'white';
    const initialPaper = urlParams.get('paper') || 'a4';
    setPaperMode(initialPaper);
    setViewMode(initialMode);
</script>

</body>
</html>
'''
    return html

def main():
    print("[1/3] Generating all 11 product 100ml labels with balanced typography & trademark filing (110mm x 75mm)...")
    for p in PRODUCTS:
        if p.get("ingredients_header_ref") == "100ml / 30ml 공용":
            p["ingredients_header_ref"] = "100ml 정품 규격"

    for p in PRODUCTS:
        html = render_100ml_label_html(p)
        key = p["id"]
        
        # 1. monsmecta_{key}_label.html (기본 화이트+다크 듀얼)
        target_name = p["file_name"]
        target_path = os.path.join(out_dir, target_name)
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated {target_name}")

        # 2. monsmecta_{key}_white_label.html (화이트 라벨 전용)
        if key == "monsmecta":
            white_name = "monsmecta_original_white_label.html"
        elif key == "urinary":
            white_name = "monsmecta_renal_white_label.html"
        else:
            white_name = f"monsmecta_{key}_white_label.html"

        white_path = os.path.join(out_dir, white_name)
        with open(white_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated {white_name}")

    print("\n[2/3] Updating legacy aliases to balanced 100ml 110x75mm...")
    legacy_mappings = [
        ("monsmecta_original_30ml_94x45.html", "monsmecta"),
        ("monsmecta_renal_30ml_94x45.html", "urinary"),
        ("monsmecta_hepamax_30ml_94x45.html", "hepamax"),
        ("monsmecta_hepamax_25ml_label.html", "hepamax"),
        ("hepamax_25ml_label_print.html", "hepamax")
    ]
    for filename, pid in legacy_mappings:
        prod = next((item for item in PRODUCTS if item["id"] == pid), None)
        if prod:
            legacy_path = os.path.join(out_dir, filename)
            with open(legacy_path, "w", encoding="utf-8") as f:
                f.write(render_100ml_label_html(prod))
            print(f"Updated legacy alias {filename}")

    print("\n[3/3] Updating all *_label_print.html and *_label_print_white.html to balanced 110x75mm...")
    for p in PRODUCTS:
        pid = p["id"]
        print_name = f"{pid}_label_print.html"
        print_white_name = f"{pid}_label_print_white.html"
        
        html = render_100ml_label_html(p)
        with open(os.path.join(out_dir, print_name), "w", encoding="utf-8") as f:
            f.write(html)
        with open(os.path.join(out_dir, print_white_name), "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Updated {print_name} & {print_white_name}")

    print("\n[ALL COMPLETE] All labels successfully regenerated with perfectly balanced typography, trademark marks, and zero empty voids!")

if __name__ == "__main__":
    main()
