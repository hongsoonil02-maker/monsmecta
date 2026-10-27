import os
import sys
from playwright.sync_api import sync_playwright

scripts_dir = os.path.dirname(os.path.abspath(__file__))
workspace_dir = os.path.abspath(os.path.join(scripts_dir, ".."))
labels_dir = os.path.join(workspace_dir, "public", "assets", "labels")
os.makedirs(labels_dir, exist_ok=True)

with open(os.path.join(scripts_dir, "extracted_logo_b64.txt"), "r", encoding="utf-8") as f:
    logo_b64 = f.read().strip()

def generate_hepamax_25ml_html():
    neon = "#ffd700"
    neon_sub = "#fbbf24"
    neon_pale = "#fef08a"
    border = "#d97706"
    bg_gradient = "linear-gradient(135deg, #2a1205 0%, #150802 50%, #0d0c05 100%)"
    top_bar = "linear-gradient(90deg, #b45309, #f59e0b, #fef08a, #b45309)"

    html = f'''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>MONSMECTA HEPAMAX 25ml Label (85mm x 32mm) - White Back & Responsive</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;600;700;800;900&family=Orbitron:wght@700;900&display=swap" rel="stylesheet">
    <style id="dynamic-print-style">
        @page {{
            size: 85mm 32mm;
            margin: 0mm;
        }}
    </style>
    <style>
        :root {{
            --label-width: 85mm;
            --label-height: 32mm;
            --col-left-w: 39.5mm;
            --col-right-w: 43.1mm;
            --col-divider-w: 1.6mm;
            --primary-neon: {neon};
            --primary-border: {border};
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
            -webkit-font-smoothing: antialiased;
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
                padding: 110px 20px 80px 20px !important;
                overflow-x: auto !important;
            }}

            .labels-stage {{
                display: flex;
                flex-direction: column;
                align-items: center;
                gap: 55px;
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
                padding: 7px 22px;
                border-radius: 999px;
                display: inline-flex;
                align-items: center;
                gap: 10px;
                letter-spacing: -0.01em;
            }}

            .tag-white {{
                background: #ffffff;
                border: 1px solid #cbd5e1;
                color: #0f172a;
                box-shadow: 0 4px 18px rgba(0,0,0,0.45);
            }}

            .tag-dark {{
                background: rgba(30, 41, 59, 0.95);
                border: 1px solid rgba(255, 215, 0, 0.5);
                color: #ffd700;
                box-shadow: 0 4px 18px rgba(0,0,0,0.6);
            }}

            .label-sheet {{
                box-shadow: 0 25px 60px rgba(0, 0, 0, 0.95), 0 0 30px rgba(255, 215, 0, 0.25);
                transform: scale(2.6);
                transform-origin: top center;
                margin-bottom: 55mm;
            }}
        }}

        /* 인쇄 전용 (85mm x 32mm 1:1 정밀 출력) */
        @media print {{
            html, body {{
                width: var(--label-width) !important;
                height: var(--label-height) !important;
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

            /* 기본 인쇄: 활성화 모드 카드만 출력 */
            body.print-white #card-white,
            body.print-dark #card-dark {{
                display: block !important;
            }}

            body:not(.print-dark):not(.print-white) #card-white {{
                display: block !important;
            }}

            .label-type-tag {{
                display: none !important;
            }}

            .label-sheet {{
                border: none !important;
                width: var(--label-width) !important;
                height: var(--label-height) !important;
                transform: none !important;
                box-shadow: none !important;
                margin: 0 !important;
                page-break-after: avoid !important;
                page-break-inside: avoid !important;
            }}
        }}

        /* 라벨 메인 컨테이너 (85mm x 32mm 기본 규격) */
        .label-sheet {{
            width: var(--label-width);
            height: var(--label-height);
            background: {bg_gradient};
            color: #f8fafc;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            border: 0.15mm solid {border};
            flex-shrink: 0;
            transition: width 0.2s ease, height 0.2s ease;
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

        /* 상단 액센트 골드 바 */
        .top-accent-bar {{
            height: 0.30mm;
            background: {top_bar};
            box-shadow: 0 0 1.2mm {neon}E6;
            z-index: 2;
            flex-shrink: 0;
        }}

        /* 콘텐츠 랩 (32mm 높이 최적 맞춤) */
        .content-wrap {{
            position: relative;
            z-index: 2;
            display: flex;
            height: calc(var(--label-height) - 0.30mm);
            width: var(--label-width);
            padding: 0.20mm 0.30mm 0.20mm 0.30mm;
            justify-content: space-between;
        }}

        /* 좌측: 전면 메인 노출부 (39.5mm) */
        .col-left {{
            width: var(--col-left-w);
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}

        /* 중앙 구분선 디바이더 (1.6mm) */
        .divider-col {{
            width: var(--col-divider-w);
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
            width: 0.75mm;
            height: 0.75mm;
            background: #000;
            border: 0.15mm solid {neon};
            transform: rotate(45deg);
        }}

        /* 우측: 법정 고시사항 패널 (43.1mm) */
        .col-right {{
            width: var(--col-right-w);
            height: 100%;
            display: flex;
            flex-direction: column;
        }}

        /* ---------------- 좌측 전면 메인 스타일 (헤파맥스 골드 네온) ---------------- */
        .brand-badge {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5mm;
            background: rgba(0, 0, 0, 0.65);
            border: 0.15mm solid {neon};
            border-radius: 999px;
            padding: 0.10mm 0.8mm;
            line-height: 1;
            box-sizing: border-box;
        }}
        .brand-badge .emoji {{
            font-size: 1.8mm;
            line-height: 1;
            display: inline-flex;
            align-items: center;
        }}
        .brand-badge .text {{
            font-size: 1.15mm;
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
            margin: 0.02mm 0;
        }}
        .sub-desc {{
            font-size: 1.25mm;
            font-weight: 700;
            color: #fef08a;
            line-height: 1.05;
            margin-bottom: 0.02mm;
            text-shadow: 0 0 0.5mm rgba(0,0,0,0.8);
        }}
        .main-title {{
            font-size: 3.35mm;
            font-weight: 900;
            color: #ffffff;
            line-height: 1.0;
            letter-spacing: -0.02em;
            text-shadow: 0 0 1.0mm rgba(255, 215, 0, 0.4), 0 1px 2px #000;
            margin-bottom: 0.02mm;
        }}
        .en-title {{
            font-size: 1.35mm;
            font-weight: 900;
            color: {neon};
            letter-spacing: 0.04em;
            line-height: 1;
        }}

        .effects-box-wrapper {{
            position: relative;
            padding-top: 0.80mm;
            margin: 0.04mm 0;
        }}
        .effects-badge-top {{
            position: absolute;
            top: 0;
            left: 1.0mm;
            z-index: 3;
            background: {neon};
            color: #000;
            border: 0.12mm solid #000;
            border-radius: 0.25mm;
            padding: 0.04mm 0.55mm 0.18mm 0.55mm;
            font-size: 1.00mm;
            font-weight: 900;
            line-height: 1;
            box-shadow: 0 0.2mm 0.4mm rgba(0, 0, 0, 0.9);
            display: inline-flex;
            align-items: center;
            justify-content: center;
        }}
        .effects-card {{
            background: rgba(0, 0, 0, 0.60);
            border: 0.15mm solid {neon};
            border-radius: 0.35mm;
            padding: 0.65mm 0.50mm 0.22mm 0.50mm;
            display: flex;
            flex-direction: column;
            gap: 0.20mm;
        }}
        .effects-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            line-height: 1.05;
            white-space: nowrap;
        }}
        .eff-item {{
            font-size: 1.08mm;
            font-weight: 800;
            color: #ffffff;
            display: inline-flex;
            align-items: center;
            gap: 0.25mm;
            letter-spacing: -0.01em;
        }}
        .eff-dot {{
            width: 0.38mm;
            height: 0.38mm;
            background: {neon};
            border-radius: 50%;
            display: inline-block;
            flex-shrink: 0;
        }}
        .eff-note {{
            font-size: 0.80mm;
            color: #cbd5e1;
            font-weight: 500;
            white-space: nowrap;
        }}

        .tech-box-ing {{
            background: rgba(0, 0, 0, 0.55);
            border: 0.15mm solid rgba(255, 215, 0, 0.45);
            border-radius: 0.35mm;
            padding: 0.18mm 0.35mm;
            display: flex;
            flex-direction: column;
            gap: 0.03mm;
        }}
        .ing-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 0.1mm solid {neon}55;
            padding-bottom: 0.04mm;
            margin-bottom: 0.03mm;
        }}
        .ing-header .title {{
            font-size: 1.02mm;
            font-weight: 800;
            color: {neon};
            line-height: 1;
        }}
        .ing-header .ref {{
            font-size: 0.85mm;
            color: {neon_pale};
            font-weight: 600;
            line-height: 1;
        }}
        .ing-row {{
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            font-size: 0.94mm;
            line-height: 1.15;
        }}
        .ing-name {{
            color: #e2e8f0;
            font-weight: 600;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            max-width: 27mm;
        }}
        .ing-val {{
            color: #ffffff;
            font-weight: 800;
            white-space: nowrap;
            flex-shrink: 0;
            margin-left: 0.3mm;
        }}

        /* 25ml 포장단위 태그 */
        .pack-tag {{
            align-self: center;
            background: rgba(0, 0, 0, 0.65);
            border: 0.15mm solid {neon};
            border-radius: 999px;
            padding: 0.12mm 1.2mm;
            font-size: 1.15mm;
            font-weight: 800;
            display: flex;
            gap: 0.4mm;
            align-items: center;
            justify-content: center;
            line-height: 1;
        }}
        .pack-tag .val {{
            color: {neon};
            font-weight: 900;
        }}

        /* ---------------- 우측 법정 패널 기본 구조 (32mm 세로 정렬) ---------------- */
        .legal-panel {{
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 0.20mm 0.35mm 0.20mm 0.40mm;
            box-sizing: border-box;
            border-radius: 0.35mm;
        }}

        /* 헤더: 등록번호 & 사료명칭 */
        .legal-header {{
            border-bottom: 0.10mm solid rgba(255, 255, 255, 0.15);
            display: flex;
            flex-direction: column;
            gap: 0.08mm;
            padding-bottom: 0.06mm;
        }}
        .reg-num-line {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            line-height: 1.05;
        }}
        .reg-num-label {{
            font-size: 1.02mm;
            font-weight: 800;
            line-height: 1;
        }}
        .reg-num-val {{
            font-size: 1.14mm;
            font-weight: 900;
            line-height: 1;
        }}
        .us-tm-badge {{
            display: inline-flex;
            align-items: center;
            gap: 0.25mm;
            border-radius: 0.25mm;
            padding: 0.05mm 0.50mm;
            line-height: 1;
            white-space: nowrap;
        }}
        .us-tm-badge .tm-lbl {{
            font-size: 0.88mm;
            font-weight: 800;
        }}
        .us-tm-badge .tm-num {{
            font-size: 0.94mm;
            font-weight: 900;
            letter-spacing: 0.02em;
        }}

        .us-tm-front {{
            font-size: 0.88mm;
            font-weight: 800;
            letter-spacing: 0.03em;
            color: #fbbf24;
            line-height: 1;
            margin-top: 0.04mm;
            opacity: 0.95;
            text-shadow: 0 0 0.4mm rgba(0,0,0,0.8);
        }}
        .feed-type-line {{
            font-size: 0.88mm;
            font-weight: 700;
            line-height: 1.12;
            white-space: nowrap;
        }}
        .feed-type-line .lbl {{
            font-weight: 800;
        }}

        /* 법정 본문 내용 */
        .sec-content {{
            display: flex;
            flex-direction: column;
            gap: 0.04mm;
            margin: 0.01mm 0;
            text-align: left;
        }}
        .info-row {{
            display: flex;
            align-items: baseline;
            font-size: 1.00mm;
            line-height: 1.16;
            text-align: left;
        }}
        .sec-lbl {{
            font-weight: 800;
            margin-right: 0.20mm;
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
            gap: 0.01mm;
            flex: 1;
            font-weight: 600;
            line-height: 1.14;
            font-size: 0.88mm;
        }}

        .effects-sub-list {{
            list-style: none;
            padding-left: 0.25mm;
            display: flex;
            flex-direction: column;
            gap: 0.02mm;
            margin: 0.01mm 0;
        }}
        .effects-sub-list li {{
            font-size: 0.96mm;
            font-weight: 600;
            line-height: 1.15;
            display: flex;
            align-items: baseline;
            gap: 0.25mm;
        }}
        .effects-sub-list .roman {{
            font-weight: 800;
            font-size: 0.90mm;
            flex-shrink: 0;
        }}

        /* 용법 및 용량 (1줄 수평 골드 프레임) */
        .dose-box-single {{
            border-radius: 0.30mm;
            padding: 0.10mm 0.45mm;
            display: flex;
            align-items: center;
            justify-content: flex-start;
            gap: 0.35mm;
            line-height: 1.05;
            white-space: nowrap;
        }}
        .dose-box-single .title {{
            font-size: 0.98mm;
            font-weight: 900;
        }}
        .dose-box-single .desc {{
            font-size: 0.98mm;
            font-weight: 800;
        }}
        .dose-box-single .sub {{
            font-size: 0.84mm;
            font-weight: 600;
            margin-left: 0.15mm;
        }}

        /* 주의사항 (컴팩트 3줄) */
        .warn-box-orig {{
            border: 0.15mm solid #ef4444;
            border-radius: 0.30mm;
            padding: 0.06mm 0.35mm;
            display: flex;
            flex-direction: column;
            gap: 0.02mm;
        }}
        .warn-title-orig {{
            font-size: 0.92mm;
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
            gap: 0.01mm;
        }}
        .warn-item-orig {{
            font-size: 0.82mm;
            line-height: 1.12;
            display: flex;
            align-items: baseline;
            gap: 0.15mm;
        }}
        .hl-shake {{
            font-weight: 800;
        }}

        /* 제조일자/유통기한/재활용 + 포장단위 25ml */
        .mfg-date-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0.03mm 0.15mm;
            font-size: 0.90mm;
            line-height: 1;
            white-space: nowrap;
        }}
        .mfg-date-row .lbl {{
            font-weight: 800;
            margin-right: 0.12mm;
        }}
        .mfg-date-row .val {{
            font-weight: 800;
        }}
        .recycle-wrap {{
            display: flex;
            align-items: center;
            gap: 0.20mm;
            flex-shrink: 0;
        }}
        .recycle-other {{
            font-size: 0.82mm;
            font-weight: 900;
            letter-spacing: -0.01em;
        }}

        /* 제조원 / 위탁제조판매원 (에스앤제이 동물병원 / 엠오바이오) */
        .original-footer {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-top: 0.10mm solid rgba(255, 255, 255, 0.15);
            padding-top: 0.08mm;
            gap: 0.5mm;
        }}
        .footer-seller {{
            display: flex;
            align-items: center;
            gap: 0.35mm;
        }}
        .co-logo-circle {{
            width: 2.9mm;
            height: 2.9mm;
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
        .footer-maker {{
            display: flex;
            align-items: center;
        }}
        .co-text-col {{
            display: flex;
            flex-direction: column;
            gap: 0.01mm;
            line-height: 1.08;
        }}
        .co-line-main {{
            font-size: 0.88mm;
            font-weight: 800;
        }}
        .co-line-sub {{
            font-size: 0.74mm;
            font-weight: 600;
        }}

        /* ========================================================================= */
        /* [CARD-WHITE: 사용자 핵심 요청 "뒷면은 화이트" 전용 고대비 스타일] */
        /* ========================================================================= */
        #card-white .legal-panel {{
            background: #ffffff !important;
            border: 0.18mm solid #cbd5e1 !important;
            box-shadow: 0 0 1.2mm rgba(0,0,0,0.12);
        }}
        #card-white .legal-header {{
            border-bottom: 0.10mm solid #e2e8f0 !important;
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
            background: #fffbeb !important;
            border: 0.18mm solid #f59e0b !important;
        }}
        #card-white .dose-box-single .title {{ color: #b45309 !important; font-weight: 900 !important; }}
        #card-white .dose-box-single .desc {{ color: #000000 !important; font-weight: 800 !important; }}
        #card-white .dose-box-single .sub {{ color: #475569 !important; font-weight: 700 !important; }}

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
            padding: 0 0.20mm !important;
            border-radius: 0.2mm !important;
            text-decoration: none !important;
        }}

        #card-white .mfg-date-row .lbl {{ color: #000000 !important; font-weight: 900 !important; }}
        #card-white .mfg-date-row .val {{ color: #000000 !important; font-weight: 800 !important; }}
        #card-white .recycle-wrap {{ color: #000000 !important; }}
        #card-white .recycle-other {{ color: #000000 !important; }}

        #card-white .original-footer {{
            border-top: 0.10mm solid #e2e8f0 !important;
        }}
        #card-white .co-logo-circle {{
            border: 0.15mm solid #cbd5e1 !important;
            box-shadow: 0 0 0.3mm rgba(0,0,0,0.12);
        }}
        #card-white .co-line-main {{ color: #000000 !important; font-weight: 900 !important; }}
        #card-white .co-line-sub {{ color: #1e293b !important; font-weight: 700 !important; }}

        #card-white .us-tm-badge {{
            background: #fffbeb !important;
            border: 0.15mm solid #d97706 !important;
            box-shadow: 0 0.1mm 0.3mm rgba(217, 119, 6, 0.15) !important;
        }}
        #card-white .us-tm-badge .tm-lbl {{
            color: #92400e !important;
            font-weight: 800 !important;
        }}
        #card-white .us-tm-badge .tm-num {{
            color: #b45309 !important;
            font-weight: 900 !important;
        }}

        #card-white .divider-line {{
            background: linear-gradient(180deg, transparent, {border}, transparent) !important;
        }}
        #card-white .divider-diamond {{
            background: #fff !important;
            border-color: {border} !important;
        }}

        /* ========================================================================= */
        /* [CARD-DARK: 원본 올 다크 골드 네온 스타일] */
        /* ========================================================================= */
        #card-dark .legal-panel {{
            background: rgba(0, 0, 0, 0.45);
            border: 0.15mm solid rgba(255, 215, 0, 0.45);
        }}
        #card-dark .reg-num-label {{ color: {neon}; }}
        #card-dark .reg-num-val {{ color: #ffffff; }}
        #card-dark .feed-type-line {{ color: #e2e8f0; }}
        #card-dark .feed-type-line .lbl {{ color: {neon}; }}

        #card-dark .us-tm-badge {{
            background: rgba(245, 158, 11, 0.18) !important;
            border: 0.15mm solid #ffd700 !important;
            box-shadow: 0 0 0.4mm rgba(255, 215, 0, 0.4) !important;
        }}
        #card-dark .us-tm-badge .tm-lbl {{
            color: #fbbf24 !important;
            font-weight: 800 !important;
        }}
        #card-dark .us-tm-badge .tm-num {{
            color: #ffffff !important;
            font-weight: 900 !important;
        }}

        #card-dark .sec-lbl {{ color: {neon}; }}
        #card-dark .sec-val {{ color: #ffffff; }}
        #card-dark .materials-val-box {{ color: #e2e8f0; }}
        #card-dark .effects-sub-list li {{ color: #ffffff; }}
        #card-dark .effects-sub-list .roman {{ color: {neon}; }}

        #card-dark .dose-box-single {{
            background: rgba(0, 0, 0, 0.55);
            border: 0.15mm solid rgba(255, 215, 0, 0.5);
        }}
        #card-dark .dose-box-single .title {{ color: {neon}; }}
        #card-dark .dose-box-single .desc {{ color: #ffffff; }}
        #card-dark .dose-box-single .sub {{ color: #cbd5e1; }}

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
            border: 0.15mm solid {neon};
            box-shadow: 0 0 0.4mm rgba(255, 215, 0, 0.6);
        }}
        #card-dark .co-line-main {{ color: {neon}; }}
        #card-dark .co-line-sub {{ color: {neon}; }}
    </style>
</head>
<body class="mode-white print-white">

<!-- 상단 실시간 동적 컨트롤 바 (용기 사이즈 변경 대응 + 화이트 뒷면 인쇄) -->
<div class="no-print" style="position:fixed; top:10px; left:50%; transform:translateX(-50%); z-index:99999; background:rgba(15,23,42,0.97); border:1px solid {neon}; padding:10px 20px; border-radius:14px; display:flex; flex-direction:column; gap:8px; box-shadow:0 12px 40px rgba(0,0,0,0.85); backdrop-filter:blur(12px); font-family:sans-serif; max-width:98vw;">
    
    <!-- 첫 번째 줄: 상품 안내 & 뷰어 모드 & 인쇄 -->
    <div style="display:flex; align-items:center; justify-content:space-between; gap:16px;">
        <div style="color:#ffffff; font-size:13px; font-weight:700; display:flex; align-items:center; gap:8px;">
            <span style="color:{neon}; font-size:16px;">★</span>
            <span style="color:{neon}; font-weight:900;">몬스멕타 헤파맥스 25ml</span>
            <span id="dimension-badge" style="color:#fef08a; font-size:12px; background:rgba(245,158,11,0.2); padding:3px 9px; border-radius:6px; border:1px solid rgba(245,158,11,0.4); font-weight:800;">
                정밀 규격: 85mm × 32mm
            </span>
        </div>

        <!-- 뷰어 모드 전환 버튼 -->
        <div style="display:flex; gap:6px;">
            <button id="btn-white" onclick="setViewMode('white')" style="background:linear-gradient(135deg, {neon}, {neon_sub}); color:#000; border:1px solid {neon}; font-weight:900; font-size:12px; padding:6px 14px; border-radius:8px; cursor:pointer; box-shadow:0 0 10px rgba(255,215,0,0.3); transition:all 0.15s ease;">
                ☀️ 뒷면 화이트 (User Request)
            </button>
            <button id="btn-dark" onclick="setViewMode('dark')" style="background:rgba(30,41,59,0.8); color:{neon}; border:1px solid rgba(255,215,0,0.4); font-weight:700; font-size:12px; padding:6px 14px; border-radius:8px; cursor:pointer; transition:all 0.15s ease;">
                🌙 원본 올 다크
            </button>
            <button id="btn-compare" onclick="setViewMode('compare')" style="background:#2563eb; color:#fff; border:1px solid #60a5fa; font-weight:800; font-size:12px; padding:6px 14px; border-radius:8px; cursor:pointer; transition:all 0.15s ease;">
                ⚖️ 상하 동시 비교
            </button>
        </div>

        <!-- 1:1 즉시 인쇄 버튼 -->
        <div style="display:flex; align-items:center; gap:8px;">
            <select id="print-target" onchange="updatePrintTarget(this.value)" style="background:#1e293b; color:#e2e8f0; border:1px solid #475569; font-size:12px; font-weight:700; padding:6px 9px; border-radius:6px; cursor:pointer; outline:none;">
                <option value="white" selected>인쇄: 화이트 뒷면 (권장)</option>
                <option value="dark">인쇄: 원본 올 다크</option>
            </select>
            <button onclick="window.print()" style="background:linear-gradient(135deg, #10b981, #059669); color:#fff; font-weight:900; font-size:12px; padding:7px 18px; border:none; border-radius:8px; cursor:pointer; box-shadow:0 3px 12px rgba(16,185,129,0.4); display:flex; align-items:center; gap:6px;">
                <span>🖨️ 1:1 즉시 인쇄 (Ctrl+P)</span>
            </button>
        </div>
    </div>

    <!-- 두 번째 줄: 용기 사이즈 동적 변경 프리셋 & 커스텀 mm 입력 (용기 사이즈 변경 대비) -->
    <div style="display:flex; align-items:center; gap:12px; background:rgba(0,0,0,0.45); padding:6px 12px; border-radius:8px; border:1px solid rgba(255,255,255,0.1); font-size:12px;">
        <span style="color:#94a3b8; font-weight:700;">📐 용기 사이즈 변경 대비 프리셋:</span>
        <button onclick="setLabelDimensions(85, 32)" class="size-preset-btn active-preset" id="preset-85x32" style="background:#d97706; color:#ffffff; border:1px solid #f59e0b; padding:4px 10px; border-radius:6px; font-weight:800; font-size:11px; cursor:pointer;">
            85 × 32mm (25ml 기준 신규)
        </button>
        <button onclick="setLabelDimensions(85, 30)" class="size-preset-btn" id="preset-85x30" style="background:#1e293b; color:#cbd5e1; border:1px solid #475569; padding:4px 10px; border-radius:6px; font-weight:700; font-size:11px; cursor:pointer;">
            85 × 30mm (초소형 용기)
        </button>
        <button onclick="setLabelDimensions(85, 35)" class="size-preset-btn" id="preset-85x35" style="background:#1e293b; color:#cbd5e1; border:1px solid #475569; padding:4px 10px; border-radius:6px; font-weight:700; font-size:11px; cursor:pointer;">
            85 × 35mm (중간 용기)
        </button>
        <button onclick="setLabelDimensions(85, 40)" class="size-preset-btn" id="preset-85x40" style="background:#1e293b; color:#cbd5e1; border:1px solid #475569; padding:4px 10px; border-radius:6px; font-weight:700; font-size:11px; cursor:pointer;">
            85 × 40mm (구 30ml 규격)
        </button>

        <div style="height:14px; width:1px; background:rgba(255,255,255,0.2); margin:0 4px;"></div>

        <!-- 커스텀 mm 직접 조절 -->
        <span style="color:#94a3b8; font-weight:600;">직접 입력:</span>
        <label style="color:#cbd5e1; display:flex; align-items:center; gap:4px;">
            가로 <input id="custom-w" type="number" value="85" min="50" max="150" style="width:48px; background:#0f172a; color:#fff; border:1px solid #475569; border-radius:4px; padding:2px 5px; font-size:11px; text-align:center;"> mm
        </label>
        <label style="color:#cbd5e1; display:flex; align-items:center; gap:4px;">
            세로 <input id="custom-h" type="number" value="32" min="20" max="60" style="width:48px; background:#0f172a; color:#fff; border:1px solid #475569; border-radius:4px; padding:2px 5px; font-size:11px; text-align:center;"> mm
        </label>
        <button onclick="applyCustomDimensions()" style="background:#475569; color:#fff; border:none; padding:3px 10px; border-radius:5px; font-size:11px; font-weight:700; cursor:pointer;">적용</button>

        <!-- 확대 배율 조절 -->
        <div style="margin-left:auto; display:flex; align-items:center; gap:6px;">
            <span style="color:#94a3b8; font-size:11px;">화면확대:</span>
            <button onclick="setScale(1.5)" style="background:#1e293b; color:#cbd5e1; border:1px solid #475569; padding:2px 6px; border-radius:4px; font-size:10px; cursor:pointer;">1.5x</button>
            <button onclick="setScale(2.0)" style="background:#1e293b; color:#cbd5e1; border:1px solid #475569; padding:2px 6px; border-radius:4px; font-size:10px; cursor:pointer;">2.0x</button>
            <button onclick="setScale(2.6)" style="background:#2563eb; color:#fff; border:1px solid #3b82f6; padding:2px 6px; border-radius:4px; font-size:10px; cursor:pointer; font-weight:800;">2.6x</button>
        </div>
    </div>
</div>

<div class="labels-stage">

    <!-- [CARD 1] ☀️ 화이트 뒷면 라벨 (사용자 핵심 요청: 85mm x 32mm, 25ml, 뒷면 화이트) -->
    <div class="label-card-wrapper" id="card-white">
        <div class="label-type-tag tag-white no-print">
            <span>☀️ 화이트 뒷면 라벨 (우측 법정표시사항 화이트 + 블랙 텍스트)</span>
            <span style="font-weight:600; color:#475569;">| 25ml 전용 신규 규격 (85mm × 32mm)</span>
        </div>
        <div class="label-sheet">
            <div class="grid-overlay"></div>
            <div class="top-accent-bar"></div>

            <div class="content-wrap">
                <!-- LEFT COLUMN (전면 메인 39.5mm - 헤파맥스 시그니처 골드 네온 다크) -->
                <div class="col-left">
                    <div class="brand-badge">
                        <span class="emoji">🐶</span>
                        <span class="text"><span class="accent">S&J</span>&nbsp;ADVANCED VET FORMULA</span>
                        <span class="emoji">🐱</span>
                    </div>

                    <div class="hero-section">
                        <div class="sub-desc">간 기능 보호 및 해독 활성화 보조제</div>
                        <h1 class="main-title">몬스멕타 헤파맥스</h1>
                        <h2 class="en-title orbitron">MONSMECTA HEPAMAX</h2>
                    </div>

                    <div class="effects-box-wrapper">
                        <div class="effects-badge-top">핵심 효능</div>
                        <div class="effects-card">
                            <div class="effects-row">
                                <span class="eff-item"><span class="eff-dot"></span>간 건강 개선</span>
                                <span class="eff-item"><span class="eff-dot"></span>지방간 개선</span>
                            </div>
                            <div class="effects-row">
                                <span class="eff-item"><span class="eff-dot"></span>장 건강 개선</span>
                                <span class="eff-item"><span class="eff-dot"></span>항병력 증진</span>
                                <span class="eff-note">(*등의 개선에 도움)</span>
                            </div>
                        </div>
                    </div>

                    <div class="tech-box-ing">
                        <div class="ing-header">
                            <span class="title">주요 성분량</span>
                            <span class="ref">1L 기준</span>
                        </div>
                        <div class="ing-row"><span class="ing-name">Montmorillonite (몬모릴로나이트)</span><span class="ing-val">고함량</span></div>
                        <div class="ing-row"><span class="ing-name">Monsmecta Original 베이스 배합</span><span class="ing-val">핵심 원료</span></div>
                        <div class="ing-row"><span class="ing-name">Taurine (타우린)</span><span class="ing-val">2,000mg</span></div>
                        <div class="ing-row"><span class="ing-name">D-Sorbitol (D-소르비톨)</span><span class="ing-val">45g</span></div>
                        <div class="ing-row"><span class="ing-name">L-lysine HCl</span><span class="ing-val">300mg</span></div>
                        <div class="ing-row"><span class="ing-name">L-methionine</span><span class="ing-val">300mg</span></div>
                        <div class="ing-row"><span class="ing-name">Vitamin B12</span><span class="ing-val">100μg</span></div>
                    </div>

                    <div class="pack-tag">
                        <span>포장 단위 :</span>
                        <span class="val">25ml / 병</span>
                    </div>
                </div>

                <!-- CENTER DIVIDER (1.6mm) -->
                <div class="divider-col">
                    <div class="divider-line"></div>
                    <div class="divider-diamond"></div>
                </div>

                <!-- RIGHT COLUMN (우측 후면: 화이트 배경 + 고선명 블랙 텍스트 패널) -->
                <div class="col-right">
                    <div class="legal-panel">
                        <div class="legal-header">
                            <div class="reg-num-line">
                                <div style="display:inline-flex; align-items:baseline; gap:0.2mm;">
                                    <span class="reg-num-label">사료의 성분등록번호 :</span>
                                    <span class="reg-num-val">제 XX9UY0145호</span>
                                </div>
                                <div class="us-tm-badge">
                                    <span class="tm-lbl">U.S. TM App:</span>
                                    <span class="tm-num orbitron">50/041,096</span>
                                </div>
                            </div>
                            <div class="feed-type-line">
                                <span class="lbl">사료의 종류와 명칭 / 형태 / 용도 :</span> 보조사료/미생물제/바실러스 서브틸리스l액상l반려동물
                            </div>
                        </div>

                        <div class="sec-content">
                            <div class="info-row">
                                <span class="sec-lbl">등록성분량 :</span>
                                <span class="sec-val">바실러스 서브틸리스 1.0 x 10⁷ cfu/g 이상, 부형제( 정제수 )</span>
                            </div>
                            <div class="info-row" style="align-items:flex-start;">
                                <span class="sec-lbl">사용한 원료의 명칭 :</span>
                                <div class="materials-val-box">
                                    <div>바실러스 서브틸리스, 비타민A, 아세트산나트륨, 프로피온산나트륨,</div>
                                    <div>포도당, 몬모릴로나이트, 타우린, D-소르비톨, L-라이신, 메티오닌, 정제수</div>
                                </div>
                            </div>
                            <div class="info-row">
                                <span class="sec-lbl">대상 :</span>
                                <span class="sec-val">반려견, 반려묘</span>
                            </div>
                            <div class="info-row">
                                <span class="sec-lbl">효과 :</span>
                            </div>
                            <ul class="effects-sub-list">
                                <li><span class="roman">I.</span>간 기능 보호 및 지방간 개선에 도움</li>
                                <li><span class="roman">II.</span>장 건강 개선 및 체내 독소 배출 보조</li>
                                <li><span class="roman">III.</span>항병력 증진 및 질병 회복 촉진에 도움</li>
                            </ul>
                        </div>

                        <!-- 1줄 수평 용법 및 용량 (골드 테마 프레임) -->
                        <div class="dose-box-single">
                            <span class="title">용법 및 용량 :</span>
                            <span class="desc">1일 1~2ml / 체중 5kg</span>
                            <span class="sub">( 1 펌프 = 약 1ml ) - 증상에 따라 조절 가능</span>
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

                        <!-- 포장 단위 25ml + 제조일자/유통기한 + 재활용 -->
                        <div class="mfg-date-row">
                            <span><span class="lbl">포장 단위 :</span> <span class="val">25ml</span></span>
                            <span><span class="lbl">제조일자 :</span> <span class="val">2026.09.15</span></span>
                            <span><span class="lbl">유통기한 :</span> <span class="val">제조일로부터 18개월</span></span>
                            <div class="recycle-wrap">
                                <svg width="2.2mm" height="2.2mm" viewBox="0 0 100 100">
                                    <path d="M50 12 L90 82 L10 82 Z" fill="none" stroke="currentColor" stroke-width="7" stroke-linejoin="round"/>
                                    <text x="50" y="65" font-size="28" font-weight="900" text-anchor="middle" fill="currentColor">플라스틱</text>
                                </svg>
                                <span class="recycle-other">OTHER</span>
                            </div>
                        </div>

                        <!-- 위탁제조판매원 / 제조원 -->
                        <div class="original-footer">
                            <div class="footer-seller">
                                <div class="co-logo-circle">
                                    <img src="{logo_b64}" class="co-logo-img">
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

    <!-- [CARD 2] 🌙 원본 올 다크 라벨 (골드 네온 다크 테마) -->
    <div class="label-card-wrapper" id="card-dark">
        <div class="label-type-tag tag-dark no-print">
            <span>🌙 원본 올 다크 라벨 (골드 네온 테마)</span>
            <span style="font-weight:400; opacity:0.85;">| 고유 아이덴티티 네온 다크 (85mm × 32mm)</span>
        </div>
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
                        <div class="sub-desc">간 기능 보호 및 해독 활성화 보조제</div>
                        <h1 class="main-title">몬스멕타 헤파맥스</h1>
                        <h2 class="en-title orbitron">MONSMECTA HEPAMAX</h2>
                    </div>

                    <div class="effects-box-wrapper">
                        <div class="effects-badge-top">핵심 효능</div>
                        <div class="effects-card">
                            <div class="effects-row">
                                <span class="eff-item"><span class="eff-dot"></span>간 건강 개선</span>
                                <span class="eff-item"><span class="eff-dot"></span>지방간 개선</span>
                            </div>
                            <div class="effects-row">
                                <span class="eff-item"><span class="eff-dot"></span>장 건강 개선</span>
                                <span class="eff-item"><span class="eff-dot"></span>항병력 증진</span>
                                <span class="eff-note">(*등의 개선에 도움)</span>
                            </div>
                        </div>
                    </div>

                    <div class="tech-box-ing">
                        <div class="ing-header">
                            <span class="title">주요 성분량</span>
                            <span class="ref">1L 기준</span>
                        </div>
                        <div class="ing-row"><span class="ing-name">Montmorillonite (몬모릴로나이트)</span><span class="ing-val">고함량</span></div>
                        <div class="ing-row"><span class="ing-name">Monsmecta Original 베이스 배합</span><span class="ing-val">핵심 원료</span></div>
                        <div class="ing-row"><span class="ing-name">Taurine (타우린)</span><span class="ing-val">2,000mg</span></div>
                        <div class="ing-row"><span class="ing-name">D-Sorbitol (D-소르비톨)</span><span class="ing-val">45g</span></div>
                        <div class="ing-row"><span class="ing-name">L-lysine HCl</span><span class="ing-val">300mg</span></div>
                        <div class="ing-row"><span class="ing-name">L-methionine</span><span class="ing-val">300mg</span></div>
                        <div class="ing-row"><span class="ing-name">Vitamin B12</span><span class="ing-val">100μg</span></div>
                    </div>

                    <div class="pack-tag">
                        <span>포장 단위 :</span>
                        <span class="val">25ml / 병</span>
                    </div>
                </div>

                <!-- CENTER DIVIDER -->
                <div class="divider-col">
                    <div class="divider-line"></div>
                    <div class="divider-diamond"></div>
                </div>

                <!-- RIGHT COLUMN (올 다크 법정 패널) -->
                <div class="col-right">
                    <div class="legal-panel">
                        <div class="legal-header">
                            <div class="reg-num-line">
                                <div style="display:inline-flex; align-items:baseline; gap:0.2mm;">
                                    <span class="reg-num-label">사료의 성분등록번호 :</span>
                                    <span class="reg-num-val">제 XX9UY0145호</span>
                                </div>
                                <div class="us-tm-badge">
                                    <span class="tm-lbl">U.S. TM App:</span>
                                    <span class="tm-num orbitron">50/041,096</span>
                                </div>
                            </div>
                            <div class="feed-type-line">
                                <span class="lbl">사료의 종류와 명칭 / 형태 / 용도 :</span> 보조사료/미생물제/바실러스 서브틸리스l액상l반려동물
                            </div>
                        </div>

                        <div class="sec-content">
                            <div class="info-row">
                                <span class="sec-lbl">등록성분량 :</span>
                                <span class="sec-val">바실러스 서브틸리스 1.0 x 10⁷ cfu/g 이상, 부형제( 정제수 )</span>
                            </div>
                            <div class="info-row" style="align-items:flex-start;">
                                <span class="sec-lbl">사용한 원료의 명칭 :</span>
                                <div class="materials-val-box">
                                    <div>바실러스 서브틸리스, 비타민A, 아세트산나트륨, 프로피온산나트륨,</div>
                                    <div>포도당, 몬모릴로나이트, 타우린, D-소르비톨, L-라이신, 메티오닌, 정제수</div>
                                </div>
                            </div>
                            <div class="info-row">
                                <span class="sec-lbl">대상 :</span>
                                <span class="sec-val">반려견, 반려묘</span>
                            </div>
                            <div class="info-row">
                                <span class="sec-lbl">효과 :</span>
                            </div>
                            <ul class="effects-sub-list">
                                <li><span class="roman">I.</span>간 기능 보호 및 지방간 개선에 도움</li>
                                <li><span class="roman">II.</span>장 건강 개선 및 체내 독소 배출 보조</li>
                                <li><span class="roman">III.</span>항병력 증진 및 질병 회복 촉진에 도움</li>
                            </ul>
                        </div>

                        <!-- 1줄 수평 용법 및 용량 -->
                        <div class="dose-box-single">
                            <span class="title">용법 및 용량 :</span>
                            <span class="desc">1일 1~2ml / 체중 5kg</span>
                            <span class="sub">( 1 펌프 = 약 1ml ) - 증상에 따라 조절 가능</span>
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

                        <!-- 포장 단위 25ml + 제조일자/유통기한 + 재활용 -->
                        <div class="mfg-date-row">
                            <span><span class="lbl">포장 단위 :</span> <span class="val">25ml</span></span>
                            <span><span class="lbl">제조일자 :</span> <span class="val">2026.09.15</span></span>
                            <span><span class="lbl">유통기한 :</span> <span class="val">제조일로부터 18개월</span></span>
                            <div class="recycle-wrap">
                                <svg width="2.2mm" height="2.2mm" viewBox="0 0 100 100">
                                    <path d="M50 12 L90 82 L10 82 Z" fill="none" stroke="currentColor" stroke-width="7" stroke-linejoin="round"/>
                                    <text x="50" y="65" font-size="28" font-weight="900" text-anchor="middle" fill="currentColor">플라스틱</text>
                                </svg>
                                <span class="recycle-other">OTHER</span>
                            </div>
                        </div>

                        <!-- 위탁제조판매원 / 제조원 -->
                        <div class="original-footer">
                            <div class="footer-seller">
                                <div class="co-logo-circle">
                                    <img src="{logo_b64}" class="co-logo-img">
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
    let currentMode = 'white';
    let currentWidth = 85;
    let currentHeight = 32;

    function setViewMode(mode) {{
        currentMode = mode;
        const body = document.body;
        const btnWhite = document.getElementById('btn-white');
        const btnDark = document.getElementById('btn-dark');
        const btnCompare = document.getElementById('btn-compare');
        const cardWhite = document.getElementById('card-white');
        const cardDark = document.getElementById('card-dark');
        const printTarget = document.getElementById('print-target');

        body.classList.remove('mode-white', 'mode-dark', 'mode-compare');
        body.classList.add('mode-' + mode);

        btnWhite.style.background = 'rgba(30,41,59,0.8)';
        btnWhite.style.color = '#ffd700';
        btnWhite.style.boxShadow = 'none';

        btnDark.style.background = 'rgba(30,41,59,0.8)';
        btnDark.style.color = '#ffd700';
        btnDark.style.boxShadow = 'none';

        btnCompare.style.background = 'rgba(30,41,59,0.8)';
        btnCompare.style.color = '#93c5fd';
        btnCompare.style.boxShadow = 'none';

        if (mode === 'white') {{
            cardWhite.style.display = 'flex';
            cardDark.style.display = 'none';
            btnWhite.style.background = 'linear-gradient(135deg, #ffd700, #fbbf24)';
            btnWhite.style.color = '#000';
            btnWhite.style.boxShadow = '0 0 12px rgba(255,215,0,0.4)';
            printTarget.value = 'white';
            updatePrintTarget('white');
        }} else if (mode === 'dark') {{
            cardWhite.style.display = 'none';
            cardDark.style.display = 'flex';
            btnDark.style.background = 'linear-gradient(135deg, #ffd700, #fbbf24)';
            btnDark.style.color = '#000';
            btnDark.style.boxShadow = '0 0 12px rgba(255,215,0,0.4)';
            printTarget.value = 'dark';
            updatePrintTarget('dark');
        }} else if (mode === 'compare') {{
            cardWhite.style.display = 'flex';
            cardDark.style.display = 'flex';
            btnCompare.style.background = '#2563eb';
            btnCompare.style.color = '#fff';
            btnCompare.style.boxShadow = '0 0 12px rgba(37,99,235,0.4)';
        }}
    }}

    function updatePrintTarget(target) {{
        document.body.classList.remove('print-white', 'print-dark');
        document.body.classList.add('print-' + target);
    }}

    function setLabelDimensions(w, h) {{
        currentWidth = w;
        currentHeight = h;
        document.getElementById('custom-w').value = w;
        document.getElementById('custom-h').value = h;

        document.documentElement.style.setProperty('--label-width', w + 'mm');
        document.documentElement.style.setProperty('--label-height', h + 'mm');

        // 프린트 @page 규격도 동적 갱신
        const printStyle = document.getElementById('dynamic-print-style');
        if (printStyle) {{
            printStyle.innerHTML = `@page {{ size: ${{w}}mm ${{h}}mm; margin: 0mm; }}`;
        }}

        // 인디케이터 배지 업데이트
        document.getElementById('dimension-badge').innerText = `정밀 규격: ${{w}}mm × ${{h}}mm`;

        // 프리셋 버튼 활성화 스타일
        document.querySelectorAll('.size-preset-btn').forEach(btn => {{
            btn.style.background = '#1e293b';
            btn.style.color = '#cbd5e1';
            btn.style.borderColor = '#475569';
        }});
        const activeBtn = document.getElementById(`preset-${{w}}x${{h}}`);
        if (activeBtn) {{
            activeBtn.style.background = '#d97706';
            activeBtn.style.color = '#ffffff';
            activeBtn.style.borderColor = '#f59e0b';
        }}
    }}

    function applyCustomDimensions() {{
        const w = parseFloat(document.getElementById('custom-w').value);
        const h = parseFloat(document.getElementById('custom-h').value);
        if (w > 0 && h > 0) {{
            setLabelDimensions(w, h);
        }}
    }}

    function setScale(scaleVal) {{
        const sheets = document.querySelectorAll('.label-sheet');
        sheets.forEach(s => {{
            s.style.transform = `scale(${{scaleVal}})`;
        }});
    }}

    // 초기 실행
    window.addEventListener('DOMContentLoaded', () => {{
        const urlParams = new URLSearchParams(window.location.search);
        const mode = urlParams.get('mode') || 'white';
        const w = parseFloat(urlParams.get('w')) || 85;
        const h = parseFloat(urlParams.get('h')) || 32;

        setLabelDimensions(w, h);
        setViewMode(mode);
    }});
</script>
</body>
</html>
'''
    return html

def render_and_export():
    out_html_path = os.path.join(labels_dir, "monsmecta_hepamax_25ml_label.html")
    html_content = generate_hepamax_25ml_html()
    with open(out_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated HTML: {out_html_path}")

    # Also generate standalone direct print file
    direct_print_path = os.path.join(labels_dir, "hepamax_25ml_label_print.html")
    with open(direct_print_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated Direct Print HTML: {direct_print_path}")

    # Playwright Rendering
    file_url = "file:///" + os.path.abspath(out_html_path).replace("\\", "/")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(viewport={"width": 1600, "height": 1800}, device_scale_factor=2)
        page = context.new_page()

        # 1. White Back Single Label Screenshot (User Request primary focus)
        page.goto(file_url + "?mode=white&w=85&h=32")
        page.wait_for_timeout(1000)
        white_sheet = page.locator("#card-white .label-sheet")
        white_png_path = os.path.join(labels_dir, "hepamax_25ml_85x32_white_back_preview.png")
        white_sheet.screenshot(path=white_png_path)
        print(f"Rendered White Back PNG: {white_png_path}")

        # Also save high-res named version
        hd_png_path = os.path.join(labels_dir, "몬스멕타_헤파맥스_25ml_라벨_고해상도(85x32mm).png")
        white_sheet.screenshot(path=hd_png_path)
        print(f"Rendered HD Korean PNG: {hd_png_path}")

        # 2. Dark Back Single Label Screenshot
        page.goto(file_url + "?mode=dark&w=85&h=32")
        page.wait_for_timeout(500)
        dark_sheet = page.locator("#card-dark .label-sheet")
        dark_png_path = os.path.join(labels_dir, "hepamax_25ml_85x32_dark_back_preview.png")
        dark_sheet.screenshot(path=dark_png_path)
        print(f"Rendered Dark Back PNG: {dark_png_path}")

        # 3. Comparison Screenshot
        page.goto(file_url + "?mode=compare&w=85&h=32")
        page.wait_for_timeout(800)
        comp_png_path = os.path.join(labels_dir, "hepamax_25ml_85x32_comparison_preview.png")
        page.screenshot(path=comp_png_path, full_page=True)
        print(f"Rendered Comparison PNG: {comp_png_path}")

        # 4. White Mode Vector PDF Export (85mm x 32mm exact 1:1)
        page.goto(file_url + "?mode=white&w=85&h=32")
        page.wait_for_timeout(500)
        white_pdf_path = os.path.join(labels_dir, "몬스멕타_헤파맥스_25ml_라벨_화이트뒷면(85x32mm).pdf")
        page.pdf(
            path=white_pdf_path,
            width="85mm",
            height="32mm",
            margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"},
            print_background=True
        )
        print(f"Exported White Back PDF: {white_pdf_path}")

        # Also save ASCII named version for safe server handling
        white_pdf_en = os.path.join(labels_dir, "monsmecta_hepamax_25ml_85x32_white_back.pdf")
        page.pdf(
            path=white_pdf_en,
            width="85mm",
            height="32mm",
            margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"},
            print_background=True
        )
        print(f"Exported White Back PDF (EN): {white_pdf_en}")

        # 5. Dark Mode Vector PDF Export (85mm x 32mm exact 1:1)
        page.goto(file_url + "?mode=dark&w=85&h=32")
        page.wait_for_timeout(500)
        dark_pdf_path = os.path.join(labels_dir, "몬스멕타_헤파맥스_25ml_라벨_올다크(85x32mm).pdf")
        page.pdf(
            path=dark_pdf_path,
            width="85mm",
            height="32mm",
            margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"},
            print_background=True
        )
        print(f"Exported Dark Back PDF: {dark_pdf_path}")

        browser.close()

    print("ALL 85x32mm HEPAMAX 25ml RENDERS & EXPORTS COMPLETED SUCCESSFULLY!")

if __name__ == "__main__":
    render_and_export()
