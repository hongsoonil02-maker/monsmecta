import os
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
    <title>{p["name_en"]} Label (110mm x 75mm) - 100ml 정품 규격 1:1 실측 인쇄</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;800;900&family=Orbitron:wght@700;900&display=swap" rel="stylesheet">
    
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

        /* 화면 뷰어 모드 */
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

        /* ========================================================================= */
        /* 인쇄 전용 CSS (1:1 실제 크기 110mm x 75mm 보장)                           */
        /* ========================================================================= */
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

            /* A4 용지 1:1 실측 모드 (일반 프린터 기본값) */
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

            /* 4각 정밀 재단선 */
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

            /* 라벨 프린터 전용 롤 모드 (110x75mm 롤 스티커) */
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

            /* 인쇄 대상 카드만 출력 */
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

            /* 110mm x 75mm 1:1 불변 사이즈 강제 */
            .label-sheet {{
                border: 0.20mm solid {border} !important;
                width: 110mm !important;
                height: 75mm !important;
                max-width: 110mm !important;
                max-height: 75mm !important;
                transform: none !important;
                box-shadow: none !important;
                margin: 0 auto !important;
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
            padding: 0;
            margin: 0.4mm 0 0 0;
        }}
        .sub-desc {{
            font-size: 1.45mm;
            font-weight: 700;
            color: {neon_pale};
            letter-spacing: -0.01em;
            line-height: 1.15;
            margin-bottom: 0.3mm;
        }}
        .main-title {{
            font-size: 4.8mm;
            font-weight: 900;
            color: #ffffff;
            letter-spacing: -0.03em;
            line-height: 1.05;
            text-shadow: 0 0 2.0mm rgba({hex_to_rgb(neon)}, 0.6);
            margin-bottom: 0.2mm;
        }}
        .en-title {{
            font-size: 2.1mm;
            font-weight: 900;
            color: {neon};
            letter-spacing: 0.06em;
            line-height: 1;
            text-shadow: 0 0 1.2mm {neon}AA;
        }}

        .core-effects-box {{
            background: rgba(0, 0, 0, 0.55);
            border: 0.20mm solid {neon};
            border-radius: 0.8mm;
            padding: 0.8mm 1.2mm;
            position: relative;
            margin-top: 0.6mm;
        }}
        .box-tag-label {{
            position: absolute;
            top: -1.2mm;
            left: 2.0mm;
            background: {neon};
            color: #000000;
            font-size: 1.20mm;
            font-weight: 900;
            padding: 0.15mm 1.0mm;
            border-radius: 0.3mm;
            line-height: 1;
        }}
        .effects-row {{
            display: flex;
            align-items: center;
            font-size: 1.30mm;
            font-weight: 800;
            color: #e2e8f0;
            line-height: 1.3;
        }}
        .effects-row:not(:last-child) {{
            margin-bottom: 0.4mm;
        }}
        .eff-item {{
            display: inline-flex;
            align-items: center;
            gap: 0.6mm;
        }}
        .eff-dot {{
            width: 0.8mm;
            height: 0.8mm;
            border-radius: 50%;
            background: {neon};
            box-shadow: 0 0 0.8mm {neon};
            flex-shrink: 0;
        }}
        .eff-note {{
            font-size: 1.10mm;
            color: {neon_sub};
            font-weight: 700;
            margin-left: auto;
        }}

        .ingredients-table-box {{
            background: rgba(0, 0, 0, 0.55);
            border: 0.20mm solid rgba(255, 255, 255, 0.25);
            border-radius: 0.8mm;
            padding: 0.8mm 1.2mm;
            position: relative;
            margin-top: 0.6mm;
            flex-grow: 1;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}
        .table-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 0.15mm solid rgba(255, 255, 255, 0.2);
            padding-bottom: 0.4mm;
            margin-bottom: 0.4mm;
        }}
        .table-title {{
            font-size: 1.35mm;
            font-weight: 900;
            color: #ffffff;
            display: flex;
            align-items: center;
            gap: 0.8mm;
        }}
        .table-title::before {{
            content: "";
            width: 0.9mm;
            height: 0.9mm;
            background: {neon};
            display: inline-block;
        }}
        .table-badge {{
            font-size: 1.05mm;
            font-weight: 800;
            color: {neon};
            background: rgba({hex_to_rgb(neon)}, 0.15);
            border: 0.15mm solid {neon};
            padding: 0.1mm 0.8mm;
            border-radius: 0.3mm;
        }}
        .ingredients-list {{
            display: flex;
            flex-direction: column;
            gap: 0.4mm;
        }}
        .ing-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 1.25mm;
            line-height: 1.2;
            border-bottom: 0.10mm solid rgba(255, 255, 255, 0.08);
            padding-bottom: 0.2mm;
        }}
        .ing-row:last-child {{
            border-bottom: none;
            padding-bottom: 0;
        }}
        .ing-name {{
            font-weight: 700;
            color: #f1f5f9;
        }}
        .ing-val {{
            font-weight: 800;
            color: {neon};
            font-family: 'Orbitron', sans-serif;
            font-size: 1.15mm;
            letter-spacing: 0.02em;
        }}

        .col-left-bottom-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(0, 0, 0, 0.7);
            border: 0.20mm solid {neon};
            border-radius: 0.6mm;
            padding: 0.5mm 1.2mm;
            margin-top: 0.6mm;
        }}
        .left-btm-brand {{
            font-size: 1.25mm;
            font-weight: 800;
            color: #cbd5e1;
            display: flex;
            align-items: center;
            gap: 0.8mm;
        }}
        .left-btm-brand strong {{
            color: {neon};
            font-weight: 900;
        }}
        .left-btm-target {{
            font-size: 1.20mm;
            font-weight: 900;
            color: #000000;
            background: {neon};
            padding: 0.15mm 1.0mm;
            border-radius: 0.3mm;
        }}

        /* ---------------- 우측 법정 고시사항 패널 스타일 ---------------- */
        .legal-panel {{
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 100%;
            padding: 0.6mm 0.8mm;
            border-radius: 0.8mm;
            font-size: 1.20mm;
            line-height: 1.25;
        }}

        .top-reg-grid {{
            display: flex;
            flex-direction: column;
            gap: 0.3mm;
            border-bottom: 0.15mm solid rgba(255, 255, 255, 0.2);
            padding-bottom: 0.4mm;
        }}
        .reg-num-line {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-weight: 800;
            font-size: 1.25mm;
        }}
        .feed-type-line {{
            font-size: 1.10mm;
            line-height: 1.2;
            word-break: break-all;
        }}

        .sec-block {{
            margin-top: 0.4mm;
        }}
        .sec-line {{
            display: flex;
            align-items: baseline;
            gap: 0.8mm;
            line-height: 1.2;
        }}
        .sec-lbl {{
            font-size: 1.20mm;
            font-weight: 900;
            flex-shrink: 0;
        }}
        .sec-val {{
            font-size: 1.15mm;
            line-height: 1.2;
        }}

        .materials-val-box {{
            font-size: 1.08mm;
            line-height: 1.2;
            margin-top: 0.2mm;
            padding-left: 0.4mm;
        }}

        .effects-sub-list {{
            list-style: none;
            padding-left: 0.6mm;
            margin-top: 0.2mm;
            display: flex;
            flex-direction: column;
            gap: 0.25mm;
        }}
        .effects-sub-list li {{
            font-size: 1.10mm;
            line-height: 1.2;
            display: flex;
            align-items: baseline;
            gap: 0.6mm;
        }}
        .effects-sub-list .roman {{
            font-weight: 900;
            font-size: 1.00mm;
            flex-shrink: 0;
        }}

        .dose-box-single {{
            margin-top: 0.4mm;
            border-radius: 0.4mm;
            padding: 0.4mm 0.8mm;
            display: flex;
            align-items: center;
            justify-content: space-between;
            line-height: 1.2;
        }}
        .dose-box-single .title {{
            font-weight: 900;
            font-size: 1.20mm;
        }}
        .dose-box-single .desc {{
            font-weight: 800;
            font-size: 1.18mm;
        }}
        .dose-box-single .sub {{
            font-size: 1.00mm;
            font-weight: 700;
        }}

        .warn-grid {{
            margin-top: 0.4mm;
            display: flex;
            flex-direction: column;
            gap: 0.25mm;
            font-size: 1.05mm;
            line-height: 1.2;
        }}
        .warn-header {{
            font-weight: 900;
            font-size: 1.10mm;
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
            margin-top: 0.4mm;
            border-top: 0.15mm solid rgba(255, 255, 255, 0.2);
            padding-top: 0.3mm;
            font-size: 1.10mm;
            font-weight: 800;
        }}
        .mfg-date-row {{
            display: flex;
            align-items: center;
            gap: 1.0mm;
        }}
        .mfg-date-row .lbl {{
            font-weight: 900;
        }}
        .recycle-wrap {{
            display: flex;
            align-items: center;
            gap: 0.4mm;
            font-size: 0.95mm;
            font-weight: 900;
        }}
        .recycle-triangle {{
            width: 2.2mm;
            height: 2.2mm;
            border: 0.20mm solid currentColor;
            transform: rotate(45deg);
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 0.2mm;
        }}
        .recycle-triangle span {{
            transform: rotate(-45deg);
            font-size: 0.75mm;
            font-weight: 900;
            line-height: 1;
        }}

        .original-footer {{
            margin-top: 0.4mm;
            padding-top: 0.3mm;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}
        .footer-seller {{
            display: flex;
            align-items: center;
            gap: 0.8mm;
            flex: 1;
        }}
        .footer-maker {{
            flex: 1;
            padding-left: 0.8mm;
        }}
        .co-logo-circle {{
            width: 4.8mm;
            height: 4.8mm;
            border-radius: 50%;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            background: #ffffff;
        }}
        .co-logo-img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}
        .co-text-col {{
            display: flex;
            flex-direction: column;
            gap: 0.15mm;
            line-height: 1.15;
        }}
        .co-line-main {{
            font-size: 1.12mm;
            font-weight: 900;
        }}
        .co-line-sub {{
            font-size: 0.98mm;
            font-weight: 600;
        }}

        /* ========================================================================= */
        /* [TYPE A: 원본 올 다크 스타일] */
        /* ========================================================================= */
        #card-dark .legal-panel {{
            background: rgba(0, 0, 0, 0.45);
            border: 0.15mm solid rgba(255, 255, 255, 0.2);
            color: #e2e8f0;
        }}
        #card-dark .reg-num-label {{ color: {neon}; }}
        #card-dark .reg-num-val {{ color: #ffffff; }}
        #card-dark .feed-type-line {{ color: #cbd5e1; }}
        #card-dark .feed-type-line .lbl {{ color: {neon}; font-weight: 800; }}

        #card-dark .sec-lbl {{ color: {neon}; }}
        #card-dark .sec-val {{ color: #ffffff; }}
        #card-dark .materials-val-box {{ color: #cbd5e1; }}
        #card-dark .effects-sub-list li {{ color: #f1f5f9; }}
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
            border: 0.20mm solid #000000 !important;
        }}
        #card-white .dose-box-single .title {{ color: #000000 !important; font-weight: 900 !important; }}
        #card-white .dose-box-single .desc {{ color: #000000 !important; font-weight: 900 !important; }}
        #card-white .dose-box-single .sub {{ color: #334155 !important; font-weight: 800 !important; }}

        #card-white .warn-header {{ color: #dc2626 !important; font-weight: 900 !important; }}
        #card-white .warn-item-orig {{ color: #000000 !important; font-weight: 600 !important; }}
        #card-white .warn-item-orig .hl-shake {{
            color: #b91c1c !important;
            font-weight: 900 !important;
            text-decoration: underline !important;
        }}

        #card-white .meta-bottom-row {{
            border-top: 0.15mm solid #cbd5e1 !important;
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
<body class="mode-white print-white paper-a4">

<!-- 상단 실시간 인쇄/뷰어 인터랙티브 툴바 (화면 표시 전용) -->
<div class="no-print" style="position:fixed; top:10px; left:50%; transform:translateX(-50%); z-index:99999; background:rgba(15,23,42,0.96); border:1px solid {neon}; padding:10px 20px; border-radius:14px; display:flex; align-items:center; gap:12px; box-shadow:0 12px 35px rgba(0,0,0,0.85); backdrop-filter:blur(10px); font-family:sans-serif; max-width:98vw; overflow-x:auto;">
    <div style="color:#ffffff; font-size:13px; font-weight:700; display:flex; align-items:center; gap:8px; white-space:nowrap;">
        <span style="color:{neon}; font-size:16px;">★</span>
        <span style="color:{neon}; font-weight:900;">{p["name_ko"]} 100ml</span>
        <span style="color:#38bdf8; font-size:11px; background:rgba(56,189,248,0.12); padding:3px 8px; border-radius:6px; border:1px solid rgba(56,189,248,0.3); font-weight:800;">110mm × 75mm (1:1 실측)</span>
    </div>

    <div style="height:20px; width:1px; background:rgba(255,255,255,0.2);"></div>

    <!-- 인쇄 용지 규격 선택 (A4 vs 라벨 롤) -->
    <div style="display:flex; align-items:center; gap:5px; white-space:nowrap;">
        <span style="color:#94a3b8; font-size:11px; font-weight:700;">용지:</span>
        <button id="btn-paper-a4" onclick="setPaperMode('a4')" style="background:#2563eb; color:#ffffff; border:1px solid #60a5fa; font-weight:800; font-size:11px; padding:6px 11px; border-radius:7px; cursor:pointer;">
            📄 A4 일반용지 (1:1 실측+재단선)
        </button>
        <button id="btn-paper-roll" onclick="setPaperMode('roll')" style="background:rgba(30,41,59,0.8); color:#94a3b8; border:1px solid #475569; font-weight:700; font-size:11px; padding:6px 11px; border-radius:7px; cursor:pointer;">
            🏷️ 라벨 프린터 (110×75mm 롤)
        </button>
    </div>

    <div style="height:20px; width:1px; background:rgba(255,255,255,0.2);"></div>

    <!-- 라벨 색상 모드 선택 -->
    <div style="display:flex; align-items:center; gap:5px; white-space:nowrap;">
        <span style="color:#94a3b8; font-size:11px; font-weight:700;">디자인:</span>
        <button id="btn-white" onclick="setViewMode('white')" style="background:linear-gradient(135deg, {neon}, {neon_sub}); color:#000; border:1px solid {neon}; font-weight:900; font-size:11px; padding:6px 11px; border-radius:7px; cursor:pointer; box-shadow:0 0 8px rgba({hex_to_rgb(neon)},0.3);">
            ☀️ 화이트 뒷면 (권장)
        </button>
        <button id="btn-dark" onclick="setViewMode('dark')" style="background:rgba(30,41,59,0.8); color:{neon}; border:1px solid rgba({hex_to_rgb(neon)},0.4); font-weight:700; font-size:11px; padding:6px 11px; border-radius:7px; cursor:pointer;">
            🌙 올 다크
        </button>
        <button id="btn-compare" onclick="setViewMode('compare')" style="background:rgba(30,41,59,0.8); color:#94a3b8; border:1px solid #475569; font-weight:700; font-size:11px; padding:6px 11px; border-radius:7px; cursor:pointer;">
            ⚖️ 둘 다 보기
        </button>
    </div>

    <div style="height:20px; width:1px; background:rgba(255,255,255,0.2);"></div>

    <!-- 인쇄 실행 버튼 -->
    <button onclick="doPrint()" style="background:linear-gradient(135deg, #10b981, #059669); color:#fff; font-weight:900; font-size:12px; padding:7px 18px; border:none; border-radius:8px; cursor:pointer; box-shadow:0 4px 15px rgba(16,185,129,0.5); display:flex; align-items:center; gap:6px; white-space:nowrap;">
        <span>🖨️ 1:1 실제 크기 인쇄 (Ctrl+P)</span>
    </button>
</div>

<!-- 인쇄 스테이지 -->
<div class="labels-stage">

    <!-- A4 인쇄 헤더: 제품명 및 실측 확인용 50mm 눈금자 (인쇄 시 자동 출력) -->
    <div class="a4-calibration-header">
        <div style="font-size:13pt; font-weight:900; color:#0f172a; margin-bottom:1.5mm; letter-spacing:-0.02em;">
            MONSMECTA™ {p["name_ko"]} 100ml 처방 라벨 (110mm × 75mm 1:1 정품 규격)
        </div>
        <div style="font-size:8pt; color:#475569; margin-bottom:2.5mm; font-weight:700;">
            ※ 인쇄 창 설정: <strong>[용지: A4]</strong> | <strong>[배율: 100% (실제 크기)]</strong> | <strong>[여백: 없음]</strong> | <strong>[배경 그래픽: 켜기(체크)]</strong>
        </div>
        <div style="display:flex; align-items:center; gap:3mm; margin-bottom:3mm; background:#f8fafc; border:1px dashed #94a3b8; padding:2mm 5mm; border-radius:2mm;">
            <span style="font-size:8pt; font-weight:900; color:#0f172a;">실측 확인용 50mm 자:</span>
            <div style="width:50mm; height:5mm; border-left:1px solid #000; border-right:1px solid #000; border-bottom:1px solid #000; position:relative; box-sizing:border-box;">
                <div style="position:absolute; left:10mm; bottom:0; height:3mm; width:0.5px; background:#000;"></div>
                <div style="position:absolute; left:20mm; bottom:0; height:3mm; width:0.5px; background:#000;"></div>
                <div style="position:absolute; left:30mm; bottom:0; height:3mm; width:0.5px; background:#000;"></div>
                <div style="position:absolute; left:40mm; bottom:0; height:3mm; width:0.5px; background:#000;"></div>
                <div style="position:absolute; top:-3.5mm; left:0; font-size:6pt; font-weight:800; transform:translateX(-50%);">0</div>
                <div style="position:absolute; top:-3.5mm; left:25mm; font-size:6pt; font-weight:800; transform:translateX(-50%);">25mm</div>
                <div style="position:absolute; top:-3.5mm; right:0; font-size:6pt; font-weight:800; transform:translateX(50%);">50mm</div>
            </div>
            <span style="font-size:7.5pt; color:#64748b; font-weight:600;">(출력 후 일반 자를 대어 위 눈금이 정확히 50mm(5cm)이면 100% 실측 정품 크기입니다)</span>
        </div>
    </div>

    <!-- [CARD 1] 원본 올 다크 라벨 -->
    <div class="label-card-wrapper" id="card-dark">
        <div class="label-type-tag tag-dark no-print">
            <span>🌙 원본 라벨 (올 다크 테마)</span>
            <span style="font-weight:400; opacity:0.85;">| 고유 아이덴티티 네온 다크 (110mm × 75mm / 100ml)</span>
        </div>
        <div class="crop-marks-box">
            <!-- 코너 재단선 -->
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
                                <strong>S&J VET FORMULA</strong> · 동물병원 전용 처방
                            </div>
                            <div class="left-btm-target">반려견·반려묘 전용 (100ml)</div>
                        </div>
                    </div>

                    <!-- CENTER DIVIDER -->
                    <div class="divider-col">
                        <div class="divider-line"></div>
                        <div class="divider-diamond"></div>
                    </div>

                    <!-- RIGHT COLUMN (법정 고시사항 원본 일치) -->
                    <div class="col-right">
                        <div class="legal-panel">
                            <div class="top-reg-grid">
                                <div class="reg-num-line">
                                    <span class="reg-num-label">성분등록번호</span>
                                    <span class="reg-num-val">{p["reg_no"]}</span>
                                </div>
                                <div class="feed-type-line">
                                    <span class="lbl">사료의 명칭 및 형태 :</span>
                                    <span>{p["feed_type"]}</span>
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
                                <span class="title">급여방법 :</span>
                                <span class="desc">{dosage_desc}</span>
                                <span class="sub">{dosage_sub}</span>
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
                                <div>중량 : <strong style="font-size:1.15mm;">100ml</strong></div>
                                <div class="mfg-date-row">
                                    <span class="lbl">제조일자 :</span>
                                    <span class="val">별도표기</span>
                                </div>
                                <div>유통기한 : 제조일로부터 18개월</div>
                                <div class="recycle-wrap">
                                    <div class="recycle-triangle">
                                        <span>플라스틱</span>
                                    </div>
                                    <span class="recycle-other">OTHER</span>
                                </div>
                            </div>

                            <!-- 풋터 원본 일치 (에스앤제이 용인 / 엠오 바이오 화성) -->
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
    </div>

    <!-- [CARD 2] 화이트 뒷면 라벨 (Type B) -->
    <div class="label-card-wrapper" id="card-white">
        <div class="label-type-tag tag-white no-print">
            <span>☀️ 화이트 뒷면 (인쇄 권장 규격)</span>
            <span style="font-weight:600; color:#475569;">| 법정 고시사항 100% 선명 흑백 대비 (110mm × 75mm / 100ml)</span>
        </div>
        <div class="crop-marks-box">
            <!-- 코너 재단선 -->
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
                                <strong>S&J VET FORMULA</strong> · 동물병원 전용 처방
                            </div>
                            <div class="left-btm-target">반려견·반려묘 전용 (100ml)</div>
                        </div>
                    </div>

                    <!-- CENTER DIVIDER -->
                    <div class="divider-col">
                        <div class="divider-line"></div>
                        <div class="divider-diamond"></div>
                    </div>

                    <!-- RIGHT COLUMN (화이트 뒷면 고시사항 패널) -->
                    <div class="col-right">
                        <div class="legal-panel">
                            <div class="top-reg-grid">
                                <div class="reg-num-line">
                                    <span class="reg-num-label">성분등록번호</span>
                                    <span class="reg-num-val">{p["reg_no"]}</span>
                                </div>
                                <div class="feed-type-line">
                                    <span class="lbl">사료의 명칭 및 형태 :</span>
                                    <span>{p["feed_type"]}</span>
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
                                <span class="title">급여방법 :</span>
                                <span class="desc">{dosage_desc}</span>
                                <span class="sub">{dosage_sub}</span>
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
                                <div>중량 : <strong style="font-size:1.15mm; color:#000000;">100ml</strong></div>
                                <div class="mfg-date-row">
                                    <span class="lbl">제조일자 :</span>
                                    <span class="val">별도표기</span>
                                </div>
                                <div>유통기한 : 제조일로부터 18개월</div>
                                <div class="recycle-wrap">
                                    <div class="recycle-triangle">
                                        <span>플라스틱</span>
                                    </div>
                                    <span class="recycle-other">OTHER</span>
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

    <!-- A4 하단 재단 가이드 안내문 (인쇄 시 출력) -->
    <div class="a4-cut-instructions">
        <span>✂️ 외곽 4개 모서리 재단선(┌ ┐ └ ┘)을 따라 가위나 칼로 오려낸 후 100ml 용기에 부착하십시오. (정확히 110mm × 75mm)</span>
    </div>

</div>

<script>
    let currentDesign = 'white';
    let currentPaper = 'a4';

    function setPaperMode(paper) {{
        currentPaper = paper;
        const pageStyle = document.getElementById('page-style');
        const btnA4 = document.getElementById('btn-paper-a4');
        const btnRoll = document.getElementById('btn-paper-roll');

        if (paper === 'a4') {{
            document.body.classList.remove('paper-roll');
            document.body.classList.add('paper-a4');
            pageStyle.innerHTML = '@page {{ size: A4 portrait; margin: 8mm auto 0 auto; }}';
            btnA4.style.background = '#2563eb';
            btnA4.style.color = '#ffffff';
            btnA4.style.borderColor = '#60a5fa';
            btnRoll.style.background = 'rgba(30,41,59,0.8)';
            btnRoll.style.color = '#94a3b8';
            btnRoll.style.borderColor = '#475569';
        }} else {{
            document.body.classList.remove('paper-a4');
            document.body.classList.add('paper-roll');
            pageStyle.innerHTML = '@page {{ size: 110mm 75mm; margin: 0mm; }}';
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
        const btnDark = document.getElementById('btn-dark');
        const btnWhite = document.getElementById('btn-white');
        const btnCompare = document.getElementById('btn-compare');

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
        // 인쇄 직전 현재 설정 재확인
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
    print("[1/3] Generating all 11 product 100ml labels (110mm x 75mm 1:1 scale)...")
    for p in PRODUCTS:
        if p.get("ingredients_header_ref") == "100ml / 30ml 공용":
            p["ingredients_header_ref"] = "100ml 정품 규격"

    for p in PRODUCTS:
        html = render_100ml_label_html(p)
        key = p["id"]
        
        # 1. monsmecta_{key}_label.html (다크+화이트 듀얼 탑재, 기본 화이트)
        target_name = p["file_name"]
        target_path = os.path.join(out_dir, target_name)
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated {target_name}")

        # 2. monsmecta_{key}_white_label.html (독립 화이트 라벨)
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

    print("\n[2/3] Updating legacy 30ml aliases to 100ml 110x75mm...")
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

    print("\n[3/3] Updating all *_label_print.html and *_label_print_white.html to 110x75mm 1:1 scale...")
    for p in PRODUCTS:
        pid = p["id"]
        print_name = f"{pid}_label_print.html"
        print_white_name = f"{pid}_label_print_white.html"
        
        # For monsmecta, print_name is monsmecta_label_print.html
        html = render_100ml_label_html(p)
        with open(os.path.join(out_dir, print_name), "w", encoding="utf-8") as f:
            f.write(html)
        with open(os.path.join(out_dir, print_white_name), "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Updated {print_name} & {print_white_name}")

    print("\n[ALL COMPLETE] All labels successfully regenerated with 1:1 actual size printing support!")

if __name__ == "__main__":
    main()
