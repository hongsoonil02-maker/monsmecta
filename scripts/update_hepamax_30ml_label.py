import os
import re

file_94x45 = "public/assets/labels/monsmecta_hepamax_30ml_94x45.html"

with open("scripts/extracted_logo_b64.txt", "r", encoding="utf-8") as f:
    logo_b64 = f.read().strip()

html_content = f'''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>MONSMECTA HEPAMAX Label (94mm x 45mm) - Dark / White Comparison</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;800;900&family=Orbitron:wght@700;900&display=swap" rel="stylesheet">
    <style>
        @page {{
            size: 94mm 45mm;
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

        /* 화면 뷰어 모드 (여백 및 확대 비교 환경) */
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
                padding: 20px 0;
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
                letter-spacing: -0.01em;
            }}

            .tag-dark {{
                background: rgba(30, 41, 59, 0.9);
                border: 1px solid rgba(212, 175, 55, 0.5);
                color: #ffd700;
                box-shadow: 0 4px 15px rgba(0,0,0,0.6);
            }}

            .tag-white {{
                background: #ffffff;
                border: 1px solid #cbd5e1;
                color: #0f172a;
                box-shadow: 0 4px 15px rgba(0,0,0,0.4);
            }}

            .label-sheet {{
                box-shadow: 0 25px 60px rgba(0, 0, 0, 0.95), 0 0 35px rgba(212, 175, 55, 0.25);
                transform: scale(2.2);
                transform-origin: top center;
                margin-bottom: 58mm; /* scale(2.2) 하단 여백 보정 */
            }}
        }}

        /* 인쇄 전용 설정 (94mm x 45mm 1:1 출력) */
        @media print {{
            html, body {{
                background: none !important;
                width: 94mm !important;
                height: 45mm !important;
                margin: 0 !important;
                padding: 0 !important;
                overflow: hidden !important;
            }}
            .no-print {{
                display: none !important;
            }}
            .label-type-tag {{
                display: none !important;
            }}
            .labels-stage {{
                display: block !important;
                gap: 0 !important;
                padding: 0 !important;
            }}
            .label-card-wrapper {{
                display: block !important;
                page-break-after: always;
            }}
            .label-card-wrapper.print-hide {{
                display: none !important;
            }}
            .label-sheet {{
                border: none !important;
                width: 94mm !important;
                height: 45mm !important;
                transform: none !important;
                box-shadow: none !important;
                margin: 0 !important;
                page-break-inside: avoid;
            }}
        }}

        /* Exact Label Physical Dimensions: 94mm x 45mm */
        .label-sheet {{
            width: 94mm;
            height: 45mm;
            background: linear-gradient(135deg, #3A0F0F 0%, #150808 50%, #0B1515 100%);
            color: #f1f5f9;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            border: 0.3mm solid #8B7355;
            flex-shrink: 0;
        }}

        /* White Back Label Sheet Variation (우측 배경 완전 화이트 일체화) */
        .label-sheet.has-white-back {{
            background: linear-gradient(to right, #3A0F0F 0mm, #150808 44.5mm, #000000 45.2mm, #f1f5f9 45.6mm, #ffffff 47mm, #ffffff 94mm);
            border: 0.3mm solid #b45309;
        }}

        /* High-tech tech grid pattern */
        .grid-overlay {{
            position: absolute;
            inset: 0;
            opacity: 0.10;
            background-image: 
                linear-gradient(#D4AF37 1px, transparent 1px),
                linear-gradient(90deg, #D4AF37 1px, transparent 1px);
            background-size: 3.5mm 3.5mm;
            pointer-events: none;
            z-index: 1;
        }}

        .label-sheet.has-white-back .grid-overlay {{
            /* 그리드를 전면(좌측)에만 은은하게 유지 */
            clip-path: polygon(0 0, 46.5mm 0, 46.5mm 100%, 0 100%);
        }}

        /* Accent top glow bar */
        .top-accent-bar {{
            height: 0.8mm;
            background: #D4AF37;
            box-shadow: 0 0 1.5mm #D4AF37;
            z-index: 2;
            flex-shrink: 0;
        }}

        /* Main Content Container (Height: 44.2mm) */
        .content-wrap {{
            position: relative;
            z-index: 2;
            display: flex;
            height: calc(45mm - 0.8mm);
            width: 94mm;
            padding: 0.8mm 1.8mm 0.8mm 1.8mm;
            justify-content: space-between;
        }}

        /* Left Side: Front View (Width: 42.5mm) */
        .col-left {{
            width: 42.5mm;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}

        /* Center Divider (Width: 1.0mm) */
        .divider-col {{
            width: 1.0mm;
            height: 100%;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .divider-line {{
            width: 0.25mm;
            height: 94%;
            background: linear-gradient(180deg, transparent, #D4AF37, transparent);
            opacity: 0.8;
        }}
        .divider-diamond {{
            position: absolute;
            width: 1.5mm;
            height: 1.5mm;
            background: #000;
            border: 0.25mm solid #D4AF37;
            transform: rotate(45deg);
        }}

        /* Right Side: Back Legal Notice View (Width: 46.5mm) */
        .col-right {{
            width: 46.5mm;
            height: 100%;
            display: flex;
            flex-direction: column;
        }}

        /* Brand badge */
        .brand-badge {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 1.2mm;
            background: rgba(0, 0, 0, 0.45);
            border: 0.18mm solid #D4AF37;
            border-radius: 999px;
            padding: 0.35mm 1.5mm;
            line-height: 1;
            box-sizing: border-box;
        }}
        .brand-badge .emoji {{
            font-size: 2.55mm;
            line-height: 1;
            display: inline-flex;
            align-items: center;
            justify-content: center;
        }}
        .brand-badge .text {{
            font-size: 1.35mm;
            font-weight: 800;
            letter-spacing: 0.04em;
            color: #e2e8f0;
            line-height: 1;
            display: inline-flex;
            align-items: center;
        }}
        .brand-badge .accent {{
            color: #D4AF37;
        }}

        /* Hero Section */
        .hero-section {{
            text-align: center;
            padding: 0.05mm 0;
        }}
        .sub-desc {{
            font-size: 1.4mm;
            font-weight: 600;
            color: #cbd5e1;
            line-height: 1.1;
            margin-bottom: 0.1mm;
        }}
        .main-title {{
            font-size: 3.0mm;
            font-weight: 900;
            color: #ffffff;
            line-height: 1.05;
            letter-spacing: -0.02em;
            text-shadow: 0 0 1.2mm rgba(255,255,255,0.4);
            margin-bottom: 0.1mm;
        }}
        .en-title {{
            font-size: 1.6mm;
            font-weight: 800;
            color: #D4AF37;
            letter-spacing: 0.08em;
            line-height: 1;
        }}

        /* Left side tech box */
        .tech-box {{
            background: rgba(0, 0, 0, 0.42);
            border: 0.18mm solid rgba(255, 255, 255, 0.14);
            border-radius: 0.9mm;
            padding: 0.45mm 0.9mm;
            position: relative;
        }}
        .box-badge {{
            position: absolute;
            top: -1.35mm;
            left: 1.5mm;
            background: rgba(212, 175, 55, 0.25);
            border: 0.15mm solid #D4AF37;
            border-radius: 0.3mm;
            padding: 0.08mm 0.8mm 0.25mm 0.8mm;
            font-size: 1.15mm;
            font-weight: 800;
            color: #D4AF37;
            line-height: 1;
            box-shadow: 0 0.2mm 0.5mm rgba(0, 0, 0, 0.6);
            display: inline-flex;
            align-items: center;
            justify-content: center;
            box-sizing: border-box;
        }}

        /* Core Effects list */
        .effects-list {{
            list-style: none;
            display: flex;
            flex-wrap: wrap;
            gap: 0.25mm 1.1mm;
            margin-top: 0.45mm;
            padding-top: 0.15mm;
        }}
        .effects-list li {{
            font-size: 1.3mm;
            font-weight: 700;
            color: #f1f5f9;
            display: flex;
            align-items: center;
            gap: 0.5mm;
            line-height: 1.15;
        }}
        .bullet-dot {{
            width: 0.65mm;
            height: 0.65mm;
            border-radius: 50%;
            background: #D4AF37;
            box-shadow: 0 0 0.4mm #D4AF37;
            flex-shrink: 0;
        }}
        .effects-note {{
            font-size: 1.05mm;
            color: #D4AF37;
            opacity: 0.85;
            font-weight: 500;
            margin-top: 0.1mm;
            text-align: right;
        }}

        /* Ingredients Table */
        .ing-header {{
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            border-bottom: 0.12mm solid rgba(255, 255, 255, 0.2);
            padding-bottom: 0.15mm;
            margin-bottom: 0.2mm;
        }}
        .ing-header .title {{
            font-size: 1.35mm;
            font-weight: 800;
            color: #fff;
        }}
        .ing-header .ref {{
            font-size: 1.1mm;
            color: #D4AF37;
            font-weight: 700;
        }}
        .ing-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 1.18mm;
            line-height: 1.18;
            border-bottom: 0.08mm solid rgba(255, 255, 255, 0.06);
            padding: 0.08mm 0;
        }}
        .ing-row:last-child {{
            border-bottom: none;
        }}
        .ing-name {{
            font-weight: 700;
            color: #e2e8f0;
        }}
        .ing-val {{
            font-weight: 800;
            color: #cbd5e1;
            font-family: 'Orbitron', 'Noto Sans KR', sans-serif;
            font-size: 1.12mm;
        }}

        /* Pack volume tag */
        .pack-tag {{
            align-self: center;
            background: rgba(0, 0, 0, 0.5);
            border: 0.18mm solid #D4AF37;
            border-radius: 999px;
            padding: 0.38mm 1.8mm;
            font-size: 1.3mm;
            font-weight: 800;
            display: flex;
            gap: 0.7mm;
            align-items: center;
            justify-content: center;
            line-height: 1;
            box-sizing: border-box;
        }}
        .pack-tag .val {{
            color: #D4AF37;
            font-weight: 900;
        }}

        /* ========================================================
           RIGHT PANEL: Statutory Notice Details (다크 모드 기본)
           ======================================================== */
        .legal-panel {{
            background: rgba(0, 0, 0, 0.48);
            border: 0.18mm solid rgba(255, 255, 255, 0.15);
            border-radius: 0.9mm;
            height: 100%;
            padding: 0.6mm 1.1mm 0.5mm 1.1mm;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}

        .legal-header {{
            border-bottom: 0.12mm solid rgba(255, 255, 255, 0.18);
            padding-bottom: 0.3mm;
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
        }}
        .reg-left {{
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
        }}
        .reg-num-label {{
            font-size: 0.95mm;
            color: #D4AF37;
            font-weight: 800;
            line-height: 1;
            margin-bottom: 0.2mm;
        }}
        .reg-num-val {{
            font-size: 1.22mm;
            font-weight: 800;
            color: #fff;
            line-height: 1;
        }}
        .feed-type-val {{
            font-size: 1.05mm;
            font-weight: 700;
            color: #e2e8f0;
            line-height: 1;
            text-align: right;
            white-space: nowrap;
        }}

        /* Section rows */
        .sec-rows-container {{
            display: flex;
            flex-direction: column;
            gap: 0.95mm;
            margin: 0.8mm 0 1.0mm 0;
        }}
        .sec-row {{
            line-height: 1.25;
            display: flex;
            align-items: baseline;
        }}
        .sec-label {{
            font-size: 0.98mm;
            font-weight: 800;
            color: #D4AF37;
            white-space: nowrap;
            margin-right: 0.6mm;
            flex-shrink: 0;
        }}
        .sec-val {{
            font-size: 1.02mm;
            font-weight: 600;
            color: #e2e8f0;
            line-height: 1.25;
        }}
        .sec-val-highlight {{
            color: #ffffff;
            font-weight: 700;
        }}

        /* Dose callout box */
        .dose-box {{
            background: rgba(212, 175, 55, 0.12);
            border: 0.15mm solid #D4AF37;
            border-radius: 0.5mm;
            padding: 0.55mm 1.0mm;
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            align-items: center;
            white-space: nowrap;
            overflow: hidden;
            line-height: 1;
            box-sizing: border-box;
        }}
        .dose-left {{
            display: inline-flex;
            align-items: center;
            gap: 0.6mm;
            line-height: 1;
        }}
        .dose-title {{
            font-size: 1.05mm;
            font-weight: 800;
            color: #D4AF37;
            line-height: 1;
            display: inline-flex;
            align-items: center;
        }}
        .dose-desc {{
            font-size: 1.15mm;
            font-weight: 800;
            color: #ffffff;
            line-height: 1;
            display: inline-flex;
            align-items: center;
        }}
        .dose-sub {{
            font-size: 0.92mm;
            color: #cbd5e1;
            font-weight: 500;
            line-height: 1;
            display: inline-flex;
            align-items: center;
        }}

        /* Warnings box */
        .warn-box {{
            background: rgba(220, 38, 38, 0.12);
            border: 0.12mm solid rgba(239, 68, 68, 0.4);
            border-radius: 0.5mm;
            padding: 0.55mm 0.9mm 0.55mm 0.9mm;
            box-sizing: border-box;
        }}
        .warn-title {{
            font-size: 0.98mm;
            font-weight: 800;
            color: #f87171;
            display: flex;
            align-items: center;
            gap: 0.4mm;
            line-height: 1;
            margin-bottom: 0.18mm;
        }}
        .warn-list {{
            list-style: square inside;
            font-size: 0.92mm;
            color: #e2e8f0;
            line-height: 1.25;
            font-weight: 500;
        }}
        .warn-list li {{
            margin-bottom: 0.1mm;
        }}
        .warn-list li:last-child {{
            margin-bottom: 0;
        }}
        .warn-list strong {{
            color: #fff;
            font-weight: 700;
        }}
        .warn-list .hl-shake {{
            color: #D4AF37;
            text-decoration: underline;
            text-decoration-thickness: 0.12mm;
            text-underline-offset: 0.15mm;
            font-weight: 800;
        }}

        /* MFG & EXP Bar */
        .mfg-exp-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.95mm;
            font-weight: 700;
            border-top: 0.12mm solid rgba(255, 255, 255, 0.15);
            border-bottom: 0.12mm solid rgba(255, 255, 255, 0.15);
            padding: 0.38mm 0.5mm;
            color: #cbd5e1;
            line-height: 1;
            box-sizing: border-box;
        }}
        .mfg-exp-bar .label {{
            color: #94a3b8;
            margin-right: 0.4mm;
            display: inline-flex;
            align-items: center;
        }}
        .mfg-exp-bar .val {{
            color: #fff;
            display: inline-flex;
            align-items: center;
        }}

        /* Manufacturer & Seller footer */
        .legal-footer {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-top: 0.18mm;
            gap: 0.5mm;
        }}
        .company-block {{
            display: flex;
            align-items: center;
            gap: 0.5mm;
        }}
        .company-logo-circle {{
            width: 3.5mm;
            height: 3.5mm;
            border-radius: 50%;
            background: #fff;
            border: 0.18mm solid #D4AF37;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            flex-shrink: 0;
            box-shadow: 0 0 0.8mm #D4AF37;
        }}
        .company-logo-circle img {{
            width: 100%;
            height: 100%;
            object-fit: contain;
            padding: 0.1mm;
        }}
        .company-info {{
            font-size: 0.85mm;
            color: #cbd5e1;
            line-height: 1.15;
        }}
        .company-info .co-title {{
            font-weight: 800;
            color: #fff;
            font-size: 0.9mm;
        }}
        .company-info .tel-accent {{
            color: #D4AF37;
            font-weight: 800;
        }}

        .recycle-block {{
            display: flex;
            align-items: center;
            justify-content: center;
            margin-top: -0.6mm;
            padding-left: 0.5mm;
            flex-shrink: 0;
        }}
        .recycle-svg {{
            width: 4.5mm;
            height: 5.17mm;
        }}

        /* ========================================================
           WHITE BACK PANEL STYLING (우측 뒷면: 배경 흰색 / 글씨 검은색)
           ======================================================== */
        .white-back .legal-panel {{
            background: #ffffff !important;
            border: 0.22mm solid #cbd5e1 !important;
            box-shadow: 0 0 1.5mm rgba(0, 0, 0, 0.18) !important;
            color: #0f172a !important;
        }}

        .white-back .legal-header {{
            border-bottom: 0.16mm solid #e2e8f0 !important;
        }}
        .white-back .reg-num-label {{
            color: #92400e !important; /* 고품격 딥 앰버/골드 */
            font-weight: 900 !important;
        }}
        .white-back .reg-num-val {{
            color: #000000 !important; /* 선명한 블랙 */
            font-weight: 900 !important;
        }}
        .white-back .feed-type-val {{
            color: #334155 !important;
            font-weight: 700 !important;
        }}

        .white-back .sec-label {{
            color: #92400e !important;
            font-weight: 900 !important;
        }}
        .white-back .sec-val {{
            color: #0f172a !important; /* 딥 블랙 차콜 */
            font-weight: 600 !important;
        }}
        .white-back .sec-val-highlight {{
            color: #000000 !important;
            font-weight: 900 !important;
        }}

        .white-back .dose-box {{
            background: #fefce8 !important; /* 소프트 웜 골드 틴트 */
            border: 0.20mm solid #eab308 !important;
        }}
        .white-back .dose-title {{
            color: #854d0e !important;
            font-weight: 900 !important;
        }}
        .white-back .dose-desc {{
            color: #000000 !important;
            font-weight: 900 !important;
        }}
        .white-back .dose-sub {{
            color: #475569 !important;
            font-weight: 600 !important;
        }}

        .white-back .warn-box {{
            background: #fef2f2 !important; /* 소프트 핑크/레드 틴트 */
            border: 0.20mm solid #fca5a5 !important;
        }}
        .white-back .warn-title {{
            color: #b91c1c !important;
            font-weight: 900 !important;
        }}
        .white-back .warn-list {{
            color: #0f172a !important;
            font-weight: 600 !important;
        }}
        .white-back .warn-list strong {{
            color: #000000 !important;
            font-weight: 900 !important;
        }}
        .white-back .warn-list .hl-shake {{
            color: #b45309 !important;
            font-weight: 900 !important;
        }}

        .white-back .mfg-exp-bar {{
            border-top: 0.16mm solid #cbd5e1 !important;
            border-bottom: 0.16mm solid #cbd5e1 !important;
            color: #334155 !important;
        }}
        .white-back .mfg-exp-bar .label {{
            color: #64748b !important;
            font-weight: 700 !important;
        }}
        .white-back .mfg-exp-bar .val {{
            color: #000000 !important;
            font-weight: 800 !important;
        }}

        .white-back .company-info {{
            color: #334155 !important;
            font-weight: 600 !important;
        }}
        .white-back .company-info .co-title {{
            color: #000000 !important;
            font-weight: 900 !important;
        }}
        .white-back .company-info .tel-accent {{
            color: #92400e !important;
            font-weight: 900 !important;
        }}
        .white-back .company-info[style*="border-left"] {{
            border-left: 0.18mm solid #cbd5e1 !important;
        }}

        .white-back .company-logo-circle {{
            background: #ffffff !important;
            border: 0.20mm solid #92400e !important;
            box-shadow: none !important;
        }}

        .white-back .recycle-svg g {{
            stroke: #0f172a !important;
        }}
        .white-back .recycle-svg text {{
            fill: #000000 !important;
            font-weight: 900 !important;
        }}
    </style>
</head>
<body>

<!-- 상단 실시간 비교 & 인쇄 컨트롤 바 (인쇄 시 자동 숨김) -->
<div class="no-print" style="position:fixed; top:12px; left:50%; transform:translateX(-50%); z-index:99999; background:rgba(15,23,42,0.95); backdrop-filter:blur(10px); border:1px solid #D4AF37; padding:8px 22px; border-radius:12px; display:flex; align-items:center; gap:16px; box-shadow:0 12px 35px rgba(0,0,0,0.85); font-family:'Noto Sans KR', sans-serif;">
    <div style="display:flex; flex-direction:column; gap:2px;">
        <div style="color:#D4AF37; font-size:13px; font-weight:800; display:flex; align-items:center; gap:6px;">
            <span>★ 몬스멕타 헤파맥스 30ml (94×45mm)</span>
            <span style="background:rgba(212,175,55,0.2); color:#fef08a; font-size:10px; padding:1px 6px; border-radius:4px; border:0.5px solid #D4AF37;">라벨 디자인 비교</span>
        </div>
        <div style="color:#94a3b8; font-size:11px; font-weight:500;">
            우측(뒷면) 배경색(흰색) & 글씨색(검은색) 비교 뷰어
        </div>
    </div>

    <!-- 비교 뷰 전환 버튼 그룹 -->
    <div style="display:flex; background:rgba(0,0,0,0.5); padding:3px; border-radius:8px; border:1px solid rgba(255,255,255,0.1); gap:4px;">
        <button id="btn-dark" onclick="switchView('dark')" style="padding:6px 12px; border:none; border-radius:6px; font-size:12px; font-weight:800; cursor:pointer; background:transparent; color:#cbd5e1; transition:all 0.2s;">
            🌙 올 다크 뒷면 (Type A)
        </button>
        <button id="btn-white" onclick="switchView('white')" style="padding:6px 12px; border:none; border-radius:6px; font-size:12px; font-weight:800; cursor:pointer; background:transparent; color:#cbd5e1; transition:all 0.2s;">
            ☀️ 화이트 뒷면 (Type B)
        </button>
        <button id="btn-compare" onclick="switchView('compare')" style="padding:6px 12px; border:none; border-radius:6px; font-size:12px; font-weight:800; cursor:pointer; background:#D4AF37; color:#000; transition:all 0.2s;">
            ⚖️ 상하 동시 비교
        </button>
    </div>

    <!-- 인쇄 버튼 -->
    <button onclick="window.print()" style="background:linear-gradient(135deg, #D4AF37, #b45309); color:#fff; font-weight:800; font-size:12px; padding:7px 14px; border:none; border-radius:8px; cursor:pointer; display:flex; align-items:center; gap:5px; box-shadow:0 2px 8px rgba(212,175,55,0.4);">
        🖨️ 인쇄 (Ctrl+P)
    </button>
</div>

<!-- 라벨 메인 스테이지 -->
<div class="labels-stage">

    <!-- TYPE A: 기존 올 다크 테마 라벨 -->
    <div id="card-dark" class="label-card-wrapper">
        <div class="label-type-tag tag-dark">
            <span>🌙 [TYPE A] 올 다크 일체형 테마 (뒷면: 다크 / 글씨: 골드·화이트)</span>
        </div>
        <div class="label-sheet">
            <div class="grid-overlay"></div>
            <div class="top-accent-bar"></div>

            <div class="content-wrap">
                <!-- LEFT COLUMN (Front View) -->
                <div class="col-left">
                    <!-- Brand Badge -->
                    <div class="brand-badge">
                        <span class="emoji">🐶</span>
                        <span class="text"><span class="accent">S&J</span>&nbsp;ADVANCED VET FORMULA</span>
                        <span class="emoji">🐱</span>
                    </div>

                    <!-- Hero Title -->
                    <div class="hero-section">
                        <div class="sub-desc">간 기능 보호 및 해독 활성화 보조제</div>
                        <h1 class="main-title">몬스멕타 헤파맥스</h1>
                        <h2 class="en-title orbitron">MONSMECTA HEPAMAX</h2>
                    </div>

                    <!-- Core Effects Box -->
                    <div class="tech-box">
                        <div class="box-badge">핵심 효능</div>
                        <ul class="effects-list">
                            <li><span class='bullet-dot'></span><span>간 건강 개선</span></li>
                            <li><span class='bullet-dot'></span><span>장 건강 개선</span></li>
                            <li><span class='bullet-dot'></span><span>지방간 개선</span></li>
                            <li><span class='bullet-dot'></span><span>항병력 증진</span></li>
                            <li><span class='bullet-dot'></span><span>질병 회복 촉진</span></li>
                        </ul>
                        <div class="effects-note">* (등의 개선에 도움)</div>
                    </div>

                    <!-- Ingredients Table -->
                    <div class="tech-box">
                        <div class="ing-header">
                            <span class="title">주요 성분량</span>
                            <span class="ref">1L 기준</span>
                        </div>
                        <div class="ing-row">
                            <span class="ing-name">Montmorillonite (몬모릴로나이트)</span>
                            <span class="ing-val">고함량</span>
                        </div>
                        <div class="ing-row">
                            <span class="ing-name">Monsmecta Original 베이스 배합</span>
                            <span class="ing-val">핵심 원료</span>
                        </div>
                        <div class="ing-row">
                            <span class="ing-name">Taurine (타우린)</span>
                            <span class="ing-val">200mg</span>
                        </div>
                        <div class="ing-row">
                            <span class="ing-name">D-Sorbitol (D-소르비톨)</span>
                            <span class="ing-val">4.5g</span>
                        </div>
                        <div class="ing-row">
                            <span class="ing-name">L-lysine HCl</span>
                            <span class="ing-val">30mg</span>
                        </div>
                        <div class="ing-row">
                            <span class="ing-name">L-methionine</span>
                            <span class="ing-val">30mg</span>
                        </div>
                        <div class="ing-row">
                            <span class="ing-name">Vitamin B12</span>
                            <span class="ing-val">100μg</span>
                        </div>
                    </div>

                    <!-- Pack size -->
                    <div class="pack-tag">
                        <span>포장단위:</span>
                        <span class="val">30 ml / 병</span>
                    </div>
                </div>

                <!-- CENTER DIVIDER -->
                <div class="divider-col">
                    <div class="divider-line"></div>
                    <div class="divider-diamond"></div>
                </div>

                <!-- RIGHT COLUMN (Statutory Notice View - Dark) -->
                <div class="col-right">
                    <div class="legal-panel">
                        <!-- Header -->
                        <div class="legal-header">
                            <div class="reg-left">
                                <div class="reg-num-label">사료 성분등록번호</div>
                                <div class="reg-num-val">제 XX9UY0145호</div>
                            </div>
                            <div class="feed-type-val">보조사료 / 미생물제 / 바실러스 서브틸리스 / 액상 / 반려동물용</div>
                        </div>

                        <!-- Registration Spec / Raw materials / Species & Effects -->
                        <div class="sec-rows-container">
                            <div class="sec-row">
                                <span class="sec-label">등록성분량:</span>
                                <span class="sec-val sec-val-highlight">바실러스 서브틸리스 1.0 x 10⁷ cfu/g 이상, 부형제(정제수)</span>
                            </div>

                            <div class="sec-row">
                                <span class="sec-label">사용한 원료의 명칭:</span>
                                <span class="sec-val">바실러스 서브틸리스, 비타민A, 아세트산나트륨, 프로피온산나트륨, 포도당, 몬모릴로나이트, 타우린, D-소르비톨, L-라이신, L-메티오닌, 비타민B12, 정제수</span>
                            </div>

                            <div class="sec-row" style="justify-content:space-between;">
                                <div style="display:flex; align-items:baseline;">
                                    <span class="sec-label">대상축종:</span>
                                    <span class="sec-val sec-val-highlight">반려견 · 반려묘</span>
                                </div>
                                <div style="display:flex; align-items:baseline;">
                                    <span class="sec-label">효과:</span>
                                    <span class="sec-val">간 기능 보호, 지방간 개선, 장 질환 저항력 향상에 도움</span>
                                </div>
                            </div>
                        </div>

                        <!-- Dosage Box -->
                        <div class="dose-box">
                            <div class="dose-left">
                                <span class="dose-title">용법·용량:</span>
                                <span class="dose-desc">1일 1~2ml / 체중 5kg</span>
                            </div>
                            <span class="dose-sub">(1펌프=약 1ml, 증상별 조절)</span>
                        </div>

                        <!-- Precautions Warning Box -->
                        <div class="warn-box">
                            <div class="warn-title">
                                <svg width="2.2mm" height="2.2mm" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd"></path></svg>
                                <span>주의사항</span>
                            </div>
                            <ul class="warn-list">
                                <li>직사광선을 피하여 <strong>건조하고 서늘한 곳에 보관</strong>하십시오.</li>
                                <li>제품 특성 상 가라앉는 성분이 있어 <span class="hl-shake">흔들어서 사용</span>하십시오.</li>
                                <li>문의사항은 제조원 또는 판매원으로 연락해 주시기 바랍니다.</li>
                            </ul>
                        </div>

                        <!-- MFG / EXP -->
                        <div class="mfg-exp-bar">
                            <div><span class="label">제조일자:</span><span class="val">2026. 09. 15</span></div>
                            <div><span class="label">유통기한:</span><span class="val">제조일로부터 18개월</span></div>
                            <div><span class="label">포장:</span><span class="val">30ml</span></div>
                        </div>

                        <!-- Footer -->
                        <div class="legal-footer">
                            <div class="company-block">
                                <div class="company-logo-circle">
                                    <img src="{logo_b64}">
                                </div>
                                <div class="company-info">
                                    <div class="co-title">판매원:에스앤제이동물병원</div>
                                    <div>용인시 처인구 포곡읍 선장1로 98-8</div>
                                    <div><span class="tel-accent">TEL:</span> 031-321-6562</div>
                                </div>
                            </div>

                            <div class="company-info" style="border-left: 0.15mm solid rgba(255,255,255,0.15); padding-left: 0.6mm;">
                                <div class="co-title">제조원:엠오바이오</div>
                                <div>화성시 팔탄면 석포로 74번길 10-25</div>
                                <div><span class="tel-accent">TEL:</span> 031-458-1240</div>
                            </div>

                            <div class="recycle-block">
                                <svg viewBox="0 0 100 115" class="recycle-svg">
                                    <g stroke="#D4AF37" stroke-width="7" fill="none" stroke-linejoin="round" stroke-linecap="round">
                                        <path d="M50 8 L90 74 L10 74 Z"/>
                                        <path d="M50 8 L61 19 M90 74 L75 74 M10 74 L21 59"/>
                                    </g>
                                    <text x="50" y="52" text-anchor="middle" dominant-baseline="central" fill="#ffffff" font-size="20" font-weight="900" font-family="'Noto Sans KR', sans-serif" letter-spacing="-0.5px">플라스틱</text>
                                    <text x="50" y="100" text-anchor="middle" dominant-baseline="central" fill="#ffffff" font-size="19" font-weight="900" font-family="'Orbitron', 'Noto Sans KR', sans-serif" letter-spacing="1px">OTHER</text>
                                </svg>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>


    <!-- TYPE B: 가독성 강화 화이트 뒷면 라벨 (배경: 흰색 / 글씨: 검은색) -->
    <div id="card-white" class="label-card-wrapper">
        <div class="label-type-tag tag-white">
            <span>☀️ [TYPE B] 가독성 강화 화이트 뒷면 (우측 배경: 흰색 / 글씨: 검은색 & 딥 골드)</span>
        </div>
        <div class="label-sheet has-white-back">
            <div class="grid-overlay"></div>
            <div class="top-accent-bar"></div>

            <div class="content-wrap">
                <!-- LEFT COLUMN (Front View - 동일 규격 유지) -->
                <div class="col-left">
                    <!-- Brand Badge -->
                    <div class="brand-badge">
                        <span class="emoji">🐶</span>
                        <span class="text"><span class="accent">S&J</span>&nbsp;ADVANCED VET FORMULA</span>
                        <span class="emoji">🐱</span>
                    </div>

                    <!-- Hero Title -->
                    <div class="hero-section">
                        <div class="sub-desc">간 기능 보호 및 해독 활성화 보조제</div>
                        <h1 class="main-title">몬스멕타 헤파맥스</h1>
                        <h2 class="en-title orbitron">MONSMECTA HEPAMAX</h2>
                    </div>

                    <!-- Core Effects Box -->
                    <div class="tech-box">
                        <div class="box-badge">핵심 효능</div>
                        <ul class="effects-list">
                            <li><span class='bullet-dot'></span><span>간 건강 개선</span></li>
                            <li><span class='bullet-dot'></span><span>장 건강 개선</span></li>
                            <li><span class='bullet-dot'></span><span>지방간 개선</span></li>
                            <li><span class='bullet-dot'></span><span>항병력 증진</span></li>
                            <li><span class='bullet-dot'></span><span>질병 회복 촉진</span></li>
                        </ul>
                        <div class="effects-note">* (등의 개선에 도움)</div>
                    </div>

                    <!-- Ingredients Table -->
                    <div class="tech-box">
                        <div class="ing-header">
                            <span class="title">주요 성분량</span>
                            <span class="ref">1L 기준</span>
                        </div>
                        <div class="ing-row">
                            <span class="ing-name">Montmorillonite (몬모릴로나이트)</span>
                            <span class="ing-val">고함량</span>
                        </div>
                        <div class="ing-row">
                            <span class="ing-name">Monsmecta Original 베이스 배합</span>
                            <span class="ing-val">핵심 원료</span>
                        </div>
                        <div class="ing-row">
                            <span class="ing-name">Taurine (타우린)</span>
                            <span class="ing-val">200mg</span>
                        </div>
                        <div class="ing-row">
                            <span class="ing-name">D-Sorbitol (D-소르비톨)</span>
                            <span class="ing-val">4.5g</span>
                        </div>
                        <div class="ing-row">
                            <span class="ing-name">L-lysine HCl</span>
                            <span class="ing-val">30mg</span>
                        </div>
                        <div class="ing-row">
                            <span class="ing-name">L-methionine</span>
                            <span class="ing-val">30mg</span>
                        </div>
                        <div class="ing-row">
                            <span class="ing-name">Vitamin B12</span>
                            <span class="ing-val">100μg</span>
                        </div>
                    </div>

                    <!-- Pack size -->
                    <div class="pack-tag">
                        <span>포장단위:</span>
                        <span class="val">30 ml / 병</span>
                    </div>
                </div>

                <!-- CENTER DIVIDER -->
                <div class="divider-col">
                    <div class="divider-line"></div>
                    <div class="divider-diamond"></div>
                </div>

                <!-- RIGHT COLUMN (Statutory Notice View - White Background & Black Text) -->
                <div class="col-right white-back">
                    <div class="legal-panel">
                        <!-- Header -->
                        <div class="legal-header">
                            <div class="reg-left">
                                <div class="reg-num-label">사료 성분등록번호</div>
                                <div class="reg-num-val">제 XX9UY0145호</div>
                            </div>
                            <div class="feed-type-val">보조사료 / 미생물제 / 바실러스 서브틸리스 / 액상 / 반려동물용</div>
                        </div>

                        <!-- Registration Spec / Raw materials / Species & Effects -->
                        <div class="sec-rows-container">
                            <div class="sec-row">
                                <span class="sec-label">등록성분량:</span>
                                <span class="sec-val sec-val-highlight">바실러스 서브틸리스 1.0 x 10⁷ cfu/g 이상, 부형제(정제수)</span>
                            </div>

                            <div class="sec-row">
                                <span class="sec-label">사용한 원료의 명칭:</span>
                                <span class="sec-val">바실러스 서브틸리스, 비타민A, 아세트산나트륨, 프로피온산나트륨, 포도당, 몬모릴로나이트, 타우린, D-소르비톨, L-라이신, L-메티오닌, 비타민B12, 정제수</span>
                            </div>

                            <div class="sec-row" style="justify-content:space-between;">
                                <div style="display:flex; align-items:baseline;">
                                    <span class="sec-label">대상축종:</span>
                                    <span class="sec-val sec-val-highlight">반려견 · 반려묘</span>
                                </div>
                                <div style="display:flex; align-items:baseline;">
                                    <span class="sec-label">효과:</span>
                                    <span class="sec-val">간 기능 보호, 지방간 개선, 장 질환 저항력 향상에 도움</span>
                                </div>
                            </div>
                        </div>

                        <!-- Dosage Box (Yellow-Gold Callout) -->
                        <div class="dose-box">
                            <div class="dose-left">
                                <span class="dose-title">용법·용량:</span>
                                <span class="dose-desc">1일 1~2ml / 체중 5kg</span>
                            </div>
                            <span class="dose-sub">(1펌프=약 1ml, 증상별 조절)</span>
                        </div>

                        <!-- Precautions Warning Box (Soft Red Callout) -->
                        <div class="warn-box">
                            <div class="warn-title">
                                <svg width="2.2mm" height="2.2mm" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd"></path></svg>
                                <span>주의사항</span>
                            </div>
                            <ul class="warn-list">
                                <li>직사광선을 피하여 <strong>건조하고 서늘한 곳에 보관</strong>하십시오.</li>
                                <li>제품 특성 상 가라앉는 성분이 있어 <span class="hl-shake">흔들어서 사용</span>하십시오.</li>
                                <li>문의사항은 제조원 또는 판매원으로 연락해 주시기 바랍니다.</li>
                            </ul>
                        </div>

                        <!-- MFG / EXP -->
                        <div class="mfg-exp-bar">
                            <div><span class="label">제조일자:</span><span class="val">2026. 09. 15</span></div>
                            <div><span class="label">유통기한:</span><span class="val">제조일로부터 18개월</span></div>
                            <div><span class="label">포장:</span><span class="val">30ml</span></div>
                        </div>

                        <!-- Footer -->
                        <div class="legal-footer">
                            <div class="company-block">
                                <div class="company-logo-circle">
                                    <img src="{logo_b64}">
                                </div>
                                <div class="company-info">
                                    <div class="co-title">판매원:에스앤제이동물병원</div>
                                    <div>용인시 처인구 포곡읍 선장1로 98-8</div>
                                    <div><span class="tel-accent">TEL:</span> 031-321-6562</div>
                                </div>
                            </div>

                            <div class="company-info" style="border-left: 0.18mm solid #cbd5e1; padding-left: 0.6mm;">
                                <div class="co-title">제조원:엠오바이오</div>
                                <div>화성시 팔탄면 석포로 74번길 10-25</div>
                                <div><span class="tel-accent">TEL:</span> 031-458-1240</div>
                            </div>

                            <div class="recycle-block">
                                <svg viewBox="0 0 100 115" class="recycle-svg">
                                    <g stroke="#0f172a" stroke-width="7" fill="none" stroke-linejoin="round" stroke-linecap="round">
                                        <path d="M50 8 L90 74 L10 74 Z"/>
                                        <path d="M50 8 L61 19 M90 74 L75 74 M10 74 L21 59"/>
                                    </g>
                                    <text x="50" y="52" text-anchor="middle" dominant-baseline="central" fill="#000000" font-size="20" font-weight="900" font-family="'Noto Sans KR', sans-serif" letter-spacing="-0.5px">플라스틱</text>
                                    <text x="50" y="100" text-anchor="middle" dominant-baseline="central" fill="#000000" font-size="19" font-weight="900" font-family="'Orbitron', 'Noto Sans KR', sans-serif" letter-spacing="1px">OTHER</text>
                                </svg>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</div>

<!-- 뷰어 모드 전환 스크립트 -->
<script>
    function switchView(mode) {{
        const cardDark = document.getElementById('card-dark');
        const cardWhite = document.getElementById('card-white');
        const btnDark = document.getElementById('btn-dark');
        const btnWhite = document.getElementById('btn-white');
        const btnCompare = document.getElementById('btn-compare');

        // Reset button states
        [btnDark, btnWhite, btnCompare].forEach(btn => {{
            btn.style.background = 'transparent';
            btn.style.color = '#cbd5e1';
        }});

        if (mode === 'dark') {{
            cardDark.style.display = 'flex';
            cardWhite.style.display = 'none';
            cardDark.classList.remove('print-hide');
            cardWhite.classList.add('print-hide');
            btnDark.style.background = '#D4AF37';
            btnDark.style.color = '#000';
        }} else if (mode === 'white') {{
            cardDark.style.display = 'none';
            cardWhite.style.display = 'flex';
            cardDark.classList.add('print-hide');
            cardWhite.classList.remove('print-hide');
            btnWhite.style.background = '#D4AF37';
            btnWhite.style.color = '#000';
        }} else {{
            // compare mode
            cardDark.style.display = 'flex';
            cardWhite.style.display = 'flex';
            cardDark.classList.remove('print-hide');
            cardWhite.classList.remove('print-hide');
            btnCompare.style.background = '#D4AF37';
            btnCompare.style.color = '#000';
        }}
    }}

    // Check query param (e.g. ?mode=white or ?mode=dark)
    const urlParams = new URLSearchParams(window.location.search);
    const initialMode = urlParams.get('mode') || 'compare';
    switchView(initialMode);
</script>

</body>
</html>
'''

with open(file_94x45, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully updated {file_94x45}")
