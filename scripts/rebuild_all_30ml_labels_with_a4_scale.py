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

def render_unified_30ml_label_html(p):
    neon = p["neon"]
    neon_sub = p.get("neon_sub", neon)
    neon_pale = p.get("neon_pale", "#ffffff")
    border = p["border"]
    bg_gradient = p["bg_gradient"]
    top_bar = p["top_bar"]

    # 상표출원 ™ 표시 처리
    tm_badge = '<span class="tm-mark">™</span>'
    name_ko_display = p["name_ko"].replace("몬스멕타", f"몬스멕타{tm_badge}")
    name_en_display = p["name_en"].replace("MONSMECTA", f"MONSMECTA{tm_badge}")

    if p["id"] == "monsmecta":
        title_font_size = "4.25mm"
        en_title_font_size = "1.78mm"
        en_letter_spacing = "0.08em"
        calib_title = "몬스멕타™"
    else:
        title_font_size = "3.65mm"
        en_title_font_size = "1.52mm"
        en_letter_spacing = "0.05em"
        calib_title = f"몬스멕타™ {p['name_ko'].replace('몬스멕타 ', '')}"

    # 1. Front effects
    row1 = p["front_effects"][0]
    row2 = p["front_effects"][1]
    
    note_html = f'<span class="eff-note">{row2[2]}</span>' if len(row2) > 2 and row2[2] else ""
    row1_html = f'''<span class="eff-item"><span class="eff-dot"></span>{row1[0]}</span>
                                <span class="eff-item" style="margin-left:auto;"><span class="eff-dot"></span>{row1[1]}</span>'''
    
    row2_items = []
    if row2[0]: row2_items.append(f'<span class="eff-item"><span class="eff-dot"></span>{row2[0]}</span>')
    if row2[1]: row2_items.append(f'<span class="eff-item" style="margin-left:1.5mm;"><span class="eff-dot"></span>{row2[1]}</span>')
    row2_joined = '\n                                '.join(row2_items)
    if note_html:
        row2_joined += f'\n                                {note_html}'

    # 2. Ingredients table
    if p.get("id") == "monsmecta":
        ing_header_title = "성분(5가지 복합체)"
        ing_header_ref = "30ml 정품 규격"
        ing_joined = '''<div class="complex-5-list">
                            <div class="c5-item">
                                <div class="c5-main">1) 항균 · 항바이러스 작용</div>
                                <div class="c5-sub">- 1-deoxynojirimycin (DNJ) 천연성분 함유</div>
                                <div class="c5-sub">· 특허균주 Bacillus subtilis MORI 균주 <span class="c5-pat">(Patent No. 201180042602.8)</span></div>
                            </div>
                            <div class="c5-item">
                                <div class="c5-main">2) 장 기능 개선 및 정장 작용 <span class="c5-inline">- 포도당</span></div>
                            </div>
                            <div class="c5-item">
                                <div class="c5-main">3) 상피세포의 회복 <span class="c5-inline">- 비타민 A</span></div>
                            </div>
                            <div class="c5-item">
                                <div class="c5-main">4) 전해질제 <span class="c5-inline">- Sodium acetate, Sodium propionate</span></div>
                            </div>
                            <div class="c5-item">
                                <div class="c5-main">5) 연변 및 설사 개선, 독소 제거 <span class="c5-inline">- 몬모릴로나이트</span></div>
                                <div class="c5-sub c5-note">(곰팡이 독소 제거, 면역 증강 및 장 환경 개선에 도움)</div>
                            </div>
                        </div>'''
    else:
        ing_header_title = "주요 성분량"
        ing_header_ref = "30ml 정품 규격"
        ing_rows = []
        for ing in p["ingredients"]:
            ing_rows.append(f'''<div class="ing-row">
                            <span class="ing-name">{ing[0]}</span>
                            <span class="ing-val">{ing[1]}</span>
                        </div>''')
        ing_joined = '\n                        '.join(ing_rows)

    # 3. Raw materials
    raw_mat_parts = []
    raw_materials = p.get("raw_mat_lines", p.get("raw_materials", []))
    for line in raw_materials:
        raw_mat_parts.append(f'<span>{line}</span>')
    raw_mat_html = '\n                                    '.join(raw_mat_parts)

    # 4. Statutory effects (Clean canonical Korean effects)
    from statutory_effects_db import STATUTORY_EFFECTS_BY_ID
    clean_effs = STATUTORY_EFFECTS_BY_ID.get(p.get("id"), [
        ("I.", "장 관련 질병에 대한 저항력 향상에 도움"),
        ("II.", "면역 기능 및 건강 상태 유지에 도움"),
        ("III.", "장 기능 개선 및 정장 작용에 도움")
    ])
    stat_eff_items = []
    for r, desc in clean_effs:
        stat_eff_items.append(f'<li><span class="roman">{r}</span><span>{desc}</span></li>')
    stat_eff_joined = '\n                                '.join(stat_eff_items)

    # 5. Dosage
    dosage_desc = p.get("dosage_desc", "1일 1~2ml / 체중 5kg")
    dosage_sub = p.get("dosage_sub", "( 1 펌프 = 약 1ml ) - 증상에 따라 조절 가능")

    html = f'''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>{p["name_en"]} Label (85mm x 40mm) - A4 실측 / 롤 라벨 1:1 출력</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;800;900&family=Orbitron:wght@700;900&display=swap" rel="stylesheet">
    
    <!-- 동적 용지 설정 스타일: A4 일반 프린터 vs 85x40mm 라벨 롤 프린터 -->
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
                background: #09090b !important;
                display: flex !important;
                flex-direction: column !important;
                align-items: center !important;
                justify-content: flex-start !important;
                padding: 75px 20px 60px 20px !important;
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
                transform: scale(2.2);
                transform-origin: top center;
                margin-bottom: 50mm;
            }}
        }}

        /* 인쇄 전용 모드: A4 실측 인쇄 vs 85x40 롤 라벨 */
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

            /* --- [A4 규격 인쇄 시: 210mm 중앙 배치 & 1:1 보정 & 재단선] --- */
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
                padding-top: 5mm !important;
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
                width: 85mm !important;
                height: 40mm !important;
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

            /* --- [롤 라벨 규격 인쇄 시: 여백 없이 85x40 꽉 차게 출력] --- */
            body.paper-roll {{
                width: 85mm !important;
                height: 40mm !important;
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
                width: 85mm !important;
                height: 40mm !important;
            }}
            body.paper-roll .crop-marks-box {{
                position: static !important;
                width: 85mm !important;
                height: 40mm !important;
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
                border: 0.18mm solid {border} !important;
                width: 85mm !important;
                height: 40mm !important;
                max-width: 85mm !important;
                max-height: 40mm !important;
                transform: none !important;
                box-shadow: none !important;
                margin: 0 auto !important;
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

        /* ---------------- 좌측 전면 메인 스타일 (100ml 전면과 동일 디자인) ---------------- */
        .tm-mark {{
            font-size: 0.52em;
            vertical-align: super;
            line-height: 1;
            font-weight: 800;
            margin-left: 0.2mm;
        }}

        .brand-badge {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.6mm;
            background: rgba(0, 0, 0, 0.72);
            border: 0.16mm solid {neon};
            border-radius: 999px;
            padding: 0.12mm 1.0mm 0.18mm 1.0mm;
            line-height: 1;
            box-sizing: border-box;
            margin-top: 0.20mm;
        }}
        .brand-badge .emoji {{
            font-size: 2.1mm;
            line-height: 1;
            display: inline-flex;
            align-items: center;
        }}
        .brand-badge .text {{
            font-size: 1.25mm;
            font-weight: 900;
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
            font-size: 1.30mm;
            font-weight: 800;
            color: {neon_pale};
            letter-spacing: -0.01em;
            line-height: 1.1;
            margin-bottom: 0.08mm;
        }}
        .main-title {{
            font-size: {title_font_size};
            font-weight: 900;
            color: #ffffff;
            line-height: 1.02;
            letter-spacing: -0.03em;
            text-shadow: 0 0 1.6mm rgba({hex_to_rgb(neon)}, 0.7);
            margin-bottom: 0.08mm;
        }}
        .en-title {{
            font-size: {en_title_font_size};
            font-weight: 900;
            color: {neon};
            letter-spacing: {en_letter_spacing};
            line-height: 1;
            text-shadow: 0 0 1.0mm {neon}AA;
        }}

        /* 핵심 효능 박스 (핵심효능 배지 및 박스 1mm 상향 이동 + 내부 텍스트 상하 정중앙 배치) */
        .core-effects-box {{
            background: rgba(0, 0, 0, 0.65);
            border: 0.18mm solid {neon};
            border-radius: 0.6mm;
            padding: 0.95mm 0.85mm 0.70mm 0.85mm;
            position: relative;
            margin-top: -0.80mm;
            margin-bottom: 0.80mm;
        }}
        .box-tag-label {{
            position: absolute;
            top: -0.90mm;
            left: 1.4mm;
            background: {neon};
            color: #000000;
            font-size: 1.05mm;
            font-weight: 900;
            padding: 0.18mm 0.75mm;
            border-radius: 0.25mm;
            line-height: 1;
            display: inline-flex;
            align-items: center;
            justify-content: center;
        }}
        .box-tag-label span {{
            position: relative;
            top: 0.04mm;
            line-height: 1;
        }}
        .effects-row {{
            display: flex;
            align-items: center;
            font-size: 1.22mm;
            font-weight: 800;
            color: #f8fafc;
            line-height: 1.18;
            white-space: nowrap;
        }}
        .effects-row:not(:last-child) {{
            margin-bottom: 0.18mm;
        }}
        .eff-item {{
            display: inline-flex;
            align-items: center;
            gap: 0.45mm;
            letter-spacing: -0.01em;
        }}
        .eff-dot {{
            width: 0.75mm;
            height: 0.75mm;
            border-radius: 50%;
            background: {neon};
            box-shadow: 0 0 0.6mm {neon};
            flex-shrink: 0;
        }}
        .eff-note {{
            font-size: 0.94mm;
            color: {neon_sub};
            font-weight: 700;
            margin-left: auto;
        }}

        /* 2. 성분 박스 상하 확장 및 내용 상·하단 여백 동일 균일화 */
        .tech-box-ing {{
            background: rgba(0, 0, 0, 0.58);
            border: 0.15mm solid rgba({hex_to_rgb(neon)}, 0.48);
            border-radius: 0.5mm;
            padding: 0.35mm 0.50mm 0.35mm 0.50mm; /* 상단 및 하단 여백 완전 동일하게 맞춤 */
            display: flex;
            flex-direction: column;
            gap: 0.06mm;
        }}
        .ing-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 0.12mm solid {neon}55;
            padding-top: 0.08mm;
            padding-bottom: 0.18mm;
            margin-bottom: 0.22mm;
        }}
        .ing-header .title {{
            font-size: 1.12mm;
            font-weight: 800;
            color: {neon};
            line-height: 1;
            position: relative;
            top: -0.04mm;
        }}
        .ing-header .ref {{
            font-size: 0.92mm;
            color: {neon_pale};
            font-weight: 700;
            line-height: 1;
            position: relative;
            top: -0.04mm;
        }}
        .ing-row {{
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            font-size: 1.03mm;
            line-height: 1.25;
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
        .complex-5-list {{
            display: flex;
            flex-direction: column;
            gap: 0.12mm;
            padding: 0.08mm 0;
        }}
        .c5-item {{
            display: flex;
            flex-direction: column;
            line-height: 1.15;
        }}
        .c5-main {{
            font-size: 0.94mm;
            font-weight: 800;
            color: #ffffff;
        }}
        .c5-inline {{
            font-size: 0.94mm;
            font-weight: 700;
            color: {neon_pale};
            margin-left: 0.3mm;
        }}
        .c5-sub {{
            font-size: 0.82mm;
            font-weight: 600;
            color: #e2e8f0;
            padding-left: 1.3mm;
            white-space: nowrap;
        }}
        .c5-pat {{
            color: #fde047;
            font-weight: 700;
            font-size: 0.82mm;
        }}
        .c5-note {{
            color: #94a3b8;
            font-size: 0.80mm;
        }}

        /* 좌측 하단 푸터 바 (100ml와 동일 디자인 - 상하 정중앙 대칭 정렬) */
        .col-left-bottom-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(0, 0, 0, 0.80);
            border: 0.18mm solid {neon};
            border-radius: 0.5mm;
            padding: 0.22mm 0.80mm;
            margin-bottom: 0.20mm;
        }}
        .left-btm-brand {{
            font-size: 1.02mm;
            font-weight: 800;
            color: #e2e8f0;
            display: inline-flex;
            align-items: center;
            gap: 0.5mm;
            white-space: nowrap;
            line-height: 1;
        }}
        .left-btm-brand strong {{
            color: {neon};
            font-weight: 900;
            line-height: 1;
        }}
        .left-btm-target {{
            font-size: 0.98mm;
            font-weight: 900;
            color: #000000;
            background: {neon};
            padding: 0.18mm 0.75mm;
            border-radius: 0.28mm;
            white-space: nowrap;
            line-height: 1;
            display: inline-flex;
            align-items: center;
            justify-content: center;
        }}
        .left-btm-target span {{
            position: relative;
            top: 0.04mm;
            line-height: 1;
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
            gap: 0.10mm;
            padding-bottom: 0.06mm;
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
        .tm-dual-grid {{
            display: flex;
            flex-direction: column;
            gap: 0.08mm;
            border-top: 0.15mm dashed #cbd5e1;
            padding-top: 0.10mm;
            margin-top: 0.04mm;
            margin-bottom: 0.04mm;
        }}
        .tm-line {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.96mm;
            line-height: 1.12;
        }}
        .tm-lbl {{
            font-weight: 800;
        }}
        .tm-num {{
            font-weight: 800;
            letter-spacing: 0.01em;
        }}
        .feed-type-line {{
            font-size: 1.08mm;
            font-weight: 700;
            line-height: 1.15;
            letter-spacing: -0.03em;
            white-space: nowrap;
        }}
        .feed-type-line .lbl {{
            font-weight: 800;
        }}

        /* 본문 내용 */
        .sec-content {{
            display: flex;
            flex-direction: column;
            gap: 0.05mm;
            margin: 0.01mm 0;
            text-align: left;
        }}
        .info-row {{
            display: flex;
            align-items: baseline;
            font-size: 1.08mm;
            line-height: 1.18;
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
            line-height: 1.16;
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
            font-size: 1.08mm;
            font-weight: 600;
            line-height: 1.18;
            display: flex;
            align-items: baseline;
            gap: 0.3mm;
        }}
        .effects-sub-list .roman {{
            font-weight: 800;
            font-size: 1.02mm;
            flex-shrink: 0;
        }}

        /* 용법용량 1줄 콤팩트 - 상하 여백 100% 동일하게 정중앙 배치 */
        .dose-box-single {{
            border-radius: 0.3mm;
            padding: 0.24mm 0.45mm;
            display: flex;
            align-items: center;
            gap: 0.32mm;
            font-size: 1.03mm;
            line-height: 1;
            white-space: nowrap;
        }}
        .dose-box-single .title,
        .dose-box-single .desc,
        .dose-box-single .sub {{
            font-size: 1.03mm;
            line-height: 1;
            display: inline-block;
        }}
        .dose-box-single .title {{
            font-weight: 900;
            flex-shrink: 0;
        }}
        .dose-box-single .desc {{
            font-weight: 800;
        }}
        .dose-box-single .sub {{
            font-weight: 700;
            letter-spacing: -0.02em;
        }}

        /* 주의사항 원본 3줄 일치 박스 - 줄간격 및 상하 여백 100% 동일하게 균일화 */
        .warn-box-orig {{
            border: 0.18mm solid;
            border-radius: 0.3mm;
            padding: 0.26mm 0.45mm;
            display: flex;
            flex-direction: column;
            gap: 0.22mm;
        }}
        .warn-title-orig {{
            font-size: 0.98mm;
            font-weight: 900;
            height: 1.12mm;
            line-height: 1;
            display: flex;
            align-items: center;
            transform: translateY(-0.04mm);
        }}
        .warn-list-orig {{
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 0.22mm;
            transform: translateY(-0.04mm);
        }}
        .warn-item-orig {{
            font-size: 0.98mm;
            height: 1.12mm;
            line-height: 1;
            display: flex;
            align-items: center;
            gap: 0.2mm;
        }}
        .warn-item-orig .hl-shake {{
            font-weight: 900;
            line-height: 1;
        }}

        /* 포장단위 / 제조일자 / 유통기한 / 재활용 한 줄 */
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
        #card-dark .tm-dual-grid {{ border-top-color: rgba(255, 255, 255, 0.25); }}
        #card-dark .tm-line .tm-lbl {{ color: {neon}; font-weight: 800; }}
        #card-dark .tm-line .tm-num {{ color: #fef08a; font-weight: 900; }}
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
        #card-white .tm-dual-grid {{ border-top-color: #94a3b8 !important; }}
        #card-white .tm-line .tm-lbl {{ color: #000000 !important; font-weight: 900 !important; }}
        #card-white .tm-line .tm-num {{ color: #000000 !important; font-weight: 900 !important; }}
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
<body class="mode-white paper-a4">

<!-- 상단 실시간 비교/인쇄 툴바 -->
<div class="no-print" style="position:fixed; top:10px; left:50%; transform:translateX(-50%); z-index:99999; background:rgba(15,23,42,0.96); border:1px solid {neon}; padding:10px 20px; border-radius:14px; display:flex; align-items:center; gap:12px; box-shadow:0 12px 35px rgba(0,0,0,0.85); backdrop-filter:blur(10px); font-family:sans-serif; max-width:98vw; overflow-x:auto;">
    <div style="color:#ffffff; font-size:13px; font-weight:700; display:flex; align-items:center; gap:8px; white-space:nowrap;">
        <span style="color:{neon}; font-size:16px;">★</span>
        <span style="color:{neon}; font-weight:900;">{p["name_ko"]} 30ml</span>
        <span style="color:#38bdf8; font-size:11px; background:rgba(56,189,248,0.12); padding:3px 8px; border-radius:6px; border:1px solid rgba(56,189,248,0.3); font-weight:800;">85mm × 40mm (1:1 실측)</span>
        <span style="color:#fde047; font-size:11px; background:rgba(253,224,71,0.15); padding:3px 8px; border-radius:6px; border:1px solid rgba(253,224,71,0.35); font-weight:800;">특허청 상표출원 완료</span>
    </div>

    <div style="height:20px; width:1px; background:rgba(255,255,255,0.2);"></div>

    <!-- 인쇄 용지 규격 선택 (A4 실측 vs 롤 라벨) -->
    <div style="display:flex; align-items:center; gap:6px; background:rgba(0,0,0,0.5); padding:3px 6px; border-radius:8px; border:1px solid rgba(255,255,255,0.15);">
        <span style="color:#94a3b8; font-size:11px; font-weight:700; margin-right:4px;">인쇄 규격:</span>
        <button id="btn-paper-a4" onclick="setPaperMode('a4')" style="background:#0284c7; color:#ffffff; border:1px solid #38bdf8; padding:5px 12px; border-radius:6px; font-size:12px; font-weight:800; cursor:pointer; transition:all 0.2s; white-space:nowrap;">
            📄 A4 실측 (자르기 가이드)
        </button>
        <button id="btn-paper-roll" onclick="setPaperMode('roll')" style="background:rgba(30,41,59,0.8); color:#94a3b8; border:1px solid #475569; padding:5px 12px; border-radius:6px; font-size:12px; font-weight:800; cursor:pointer; transition:all 0.2s; white-space:nowrap;">
            🏷️ 롤 라벨지 (85x40mm)
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

<!-- 라벨 스테이지 (A4 모드 시 A4 폭에 85x40mm 정중앙 배치) -->
<div class="labels-stage">

    <!-- [A4 인쇄 전용 헤더: 50mm 실측 캘리브레이션 자] -->
    <div class="a4-calibration-header">
        <div style="font-size:11pt; font-weight:900; color:#0f172a; margin-bottom:2mm;">
            [30ml 정품 규격] {calib_title} 용기 라벨 (85mm × 40mm)
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
                <span style="position:absolute; bottom:0.5mm; right:1mm; font-size:6.5pt;">50mm</span>
            </div>
            <span>(자로 쟀을 때 정확히 5cm)</span>
        </div>
    </div>

    <!-- [CARD 1] 원본 올 다크 라벨 -->
    <div class="label-card-wrapper" id="card-dark">
        <div class="label-type-tag tag-dark no-print">
            <span>🌙 원본 라벨 (올 다크 테마)</span>
            <span style="font-weight:400; opacity:0.85;">| 고유 아이덴티티 네온 다크 (85mm × 40mm)</span>
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
                    <!-- LEFT COLUMN (전면 메인) -->
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
                            <div class="box-tag-label"><span>핵심 효능</span></div>
                            <div class="effects-row">
                                {row1_html}
                            </div>
                            <div class="effects-row">
                                {row2_joined}
                            </div>
                        </div>

                        <div class="tech-box-ing">
                            <div class="ing-header">
                                <span class="title">{ing_header_title}</span>
                                <span class="ref">{ing_header_ref}</span>
                            </div>
                            {ing_joined}
                        </div>

                        <div class="col-left-bottom-bar">
                            <div class="left-btm-brand">
                                <strong>S&J VET FORMULA</strong>&nbsp;· 동물병원 처방
                            </div>
                            <div class="left-btm-target">반려견·반려묘 (30ml)</div>
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
                                <span><span class="lbl">제조일자 :</span> <span class="val">2026. 10. 20.</span></span>
                                <span><span class="lbl">유통기한 :</span> <span class="val">제조일로부터 18개월</span></span>
                                <div class="recycle-wrap">
                                    <svg width="2.9mm" height="2.6mm" viewBox="0 0 110 100" style="flex-shrink:0; margin:-0.4mm 0;">
                                        <path d="M55 6 L104 88 L6 88 Z" fill="none" stroke="currentColor" stroke-width="6.5" stroke-linejoin="round"/>
                                        <text x="55" y="74" font-size="18.5" font-weight="900" text-anchor="middle" fill="currentColor" letter-spacing="-1">플라스틱</text>
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
    </div>

    <!-- [CARD 2] 화이트 뒷면 라벨 (원본 내용 100% 보존, 배경만 화이트 + 글씨만 블랙) -->
    <div class="label-card-wrapper" id="card-white">
        <div class="label-type-tag tag-white no-print">
            <span>☀️ 화이트 뒷면 라벨 (우측 화이트 배경 + 블랙 텍스트)</span>
            <span style="font-weight:600; color:#475569;">| 원본 표기사항 100% 동일, 우측 배경만 화이트 및 텍스트 블랙 적용 (85mm × 40mm)</span>
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
                    <!-- LEFT COLUMN (전면 메인 - 동일한 고유 컬러 다크 테마) -->
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
                            <div class="box-tag-label"><span>핵심 효능</span></div>
                            <div class="effects-row">
                                {row1_html}
                            </div>
                            <div class="effects-row">
                                {row2_joined}
                            </div>
                        </div>

                        <div class="tech-box-ing">
                            <div class="ing-header">
                                <span class="title">{ing_header_title}</span>
                                <span class="ref">{ing_header_ref}</span>
                            </div>
                            {ing_joined}
                        </div>

                        <div class="col-left-bottom-bar">
                            <div class="left-btm-brand">
                                <strong>S&J VET FORMULA</strong>&nbsp;· 동물병원 처방
                            </div>
                            <div class="left-btm-target">반려견·반려묘 (30ml)</div>
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
                                <span><span class="lbl">제조일자 :</span> <span class="val">2026. 10. 20.</span></span>
                                <span><span class="lbl">유통기한 :</span> <span class="val">제조일로부터 18개월</span></span>
                                <div class="recycle-wrap">
                                    <svg width="2.9mm" height="2.6mm" viewBox="0 0 110 100" style="flex-shrink:0; margin:-0.4mm 0;">
                                        <path d="M55 6 L104 88 L6 88 Z" fill="none" stroke="currentColor" stroke-width="6.5" stroke-linejoin="round"/>
                                        <text x="55" y="74" font-size="18.5" font-weight="900" text-anchor="middle" fill="currentColor" letter-spacing="-1">플라스틱</text>
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

    <!-- [A4 인쇄 안내 문구] -->
    <div class="a4-cut-instructions">
        ✂️ 검정색 테두리 코너 재단선(Crop Marks)을 따라 칼이나 가위로 자르면 정확히 <strong>85mm × 40mm 정품 라벨</strong>이 완성됩니다.
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
            pageStyle.innerHTML = '@page {{ size: 85mm 40mm; margin: 0; }}';
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
    print("[1/2] Generating unified 85x40mm labels with A4 scale + crop marks + Roll mode...")
    for p in PRODUCTS:
        html_content = render_unified_30ml_label_html(p)
        target_path = os.path.join(out_dir, p["file_name"])
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Generated {p['name_ko']} (85x40mm A4-ready) -> {target_path}")

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
                f.write(render_unified_30ml_label_html(prod))
            print(f"Synced legacy file {filename} -> {legacy_path}")

    print("ALL 11 PRODUCTS GENERATED WITH PERFECT 100ML ARCHITECTURE ADAPTED FOR 85x40mm!")

if __name__ == "__main__":
    main()
