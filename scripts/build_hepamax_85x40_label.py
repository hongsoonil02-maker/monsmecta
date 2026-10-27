import os

with open("scripts/extracted_logo_b64.txt", "r", encoding="utf-8") as f:
    logo_b64 = f.read().strip()

def generate_label_html(page_title="MONSMECTA HEPAMAX Label (85mm x 40mm) - Dark / White Comparison"):
    return f'''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>{page_title}</title>
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
                letter-spacing: -0.01em;
            }}

            .tag-dark {{
                background: rgba(30, 41, 59, 0.95);
                border: 1px solid rgba(255, 215, 0, 0.5);
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
                box-shadow: 0 25px 60px rgba(0, 0, 0, 0.95), 0 0 35px rgba(255, 215, 0, 0.25);
                transform: scale(2.4);
                transform-origin: top center;
                margin-bottom: 60mm;
            }}
        }}

        /* 인쇄 전용 (85mm x 40mm 1:1 출력) */
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

            /* 기본 인쇄: 활성화된 카드만 정확히 1장 1:1 출력 */
            body.print-white #card-white,
            body.print-dark #card-dark {{
                display: block !important;
            }}

            /* 둘 다 아닐 때 기본적으로 화이트(Type B) 인쇄 */
            body:not(.print-dark):not(.print-white) #card-white {{
                display: block !important;
            }}

            .label-type-tag {{
                display: none !important;
            }}

            .label-sheet {{
                border: none !important;
                width: 85mm !important;
                height: 40mm !important;
                transform: none !important;
                box-shadow: none !important;
                margin: 0 !important;
                page-break-after: avoid !important;
                page-break-inside: avoid !important;
            }}
        }}

        /* 30ml 맞춤 규격 (85mm x 40mm) */
        .label-sheet {{
            width: 85mm;
            height: 40mm;
            background: linear-gradient(135deg, #2a1205 0%, #150802 50%, #0d0c05 100%);
            color: #f8fafc;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            border: 0.15mm solid #d97706;
            flex-shrink: 0;
        }}

        .grid-overlay {{
            position: absolute;
            inset: 0;
            opacity: 0.08;
            background-image: 
                linear-gradient(#ffd700 1px, transparent 1px),
                linear-gradient(90deg, #ffd700 1px, transparent 1px);
            background-size: 2.5mm 2.5mm;
            pointer-events: none;
            z-index: 1;
        }}

        /* 슬림 탑 엑센트 바 */
        .top-accent-bar {{
            height: 0.35mm;
            background: linear-gradient(90deg, #b45309, #f59e0b, #fef08a, #b45309);
            box-shadow: 0 0 1.2mm #ffd700E6;
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

        /* 좌측: 전면 메인 노출부 (너비 39.5mm) */
        .col-left {{
            width: 39.5mm;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}

        /* 중앙 디바이더 (너비 1.8mm) */
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
            background: linear-gradient(180deg, transparent, #ffd700, transparent);
            opacity: 0.7;
        }}
        .divider-diamond {{
            position: absolute;
            width: 0.8mm;
            height: 0.8mm;
            background: #000;
            border: 0.15mm solid #ffd700;
            transform: rotate(45deg);
        }}

        /* 우측: 법정 고시사항 노출부 (너비 43.1mm) */
        .col-right {{
            width: 43.1mm;
            height: 100%;
            display: flex;
            flex-direction: column;
        }}

        /* 브랜드 배지 */
        .brand-badge {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.6mm;
            background: rgba(0, 0, 0, 0.65);
            border: 0.15mm solid #ffd700;
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
            color: #ffd700;
            font-weight: 900;
        }}

        /* 히어로 섹션 */
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
            color: #ffd700;
            letter-spacing: 0.05em;
            line-height: 1;
        }}

        /* 핵심 효능 박스 */
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
            background: #ffd700;
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
            border: 0.18mm solid #ffd700;
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
            background: #ffd700;
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

        /* 주요 성분량 테이블 */
        .tech-box-ing {{
            background: rgba(0, 0, 0, 0.55);
            border: 0.15mm solid rgba(255, 215, 0, 0.45);
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
            border-bottom: 0.1mm solid #ffd70055;
            padding-bottom: 0.06mm;
            margin-bottom: 0.04mm;
        }}
        .ing-header .title {{
            font-size: 1.15mm;
            font-weight: 800;
            color: #ffd700;
            line-height: 1;
        }}
        .ing-header .ref {{
            font-size: 0.95mm;
            color: #fef08a;
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

        /* 포장단위 배지 */
        .pack-tag {{
            align-self: center;
            background: rgba(0, 0, 0, 0.65);
            border: 0.18mm solid #ffd700;
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
            color: #ffd700;
            font-weight: 900;
        }}

        /* ------------------------------------------------------------- */
        /* 우측 법정 고시 패널 (기본: 다크 테마) */
        /* ------------------------------------------------------------- */
        .legal-panel {{
            background: rgba(0, 0, 0, 0.55);
            border: 0.15mm solid rgba(255, 255, 255, 0.22);
            border-radius: 0.5mm;
            height: 100%;
            padding: 0.15mm 0.50mm 0.12mm 0.50mm;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: all 0.2s ease;
        }}

        /* 헤더: 성분등록번호 & 종류/명칭 */
        .legal-header {{
            border-bottom: 0.1mm solid #ffd70066;
            padding-bottom: 0.10mm;
            display: flex;
            flex-direction: column;
            gap: 0.16mm;
        }}
        .reg-num-line {{
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            line-height: 1.15;
        }}
        .reg-num-label {{
            font-size: 1.14mm;
            color: #ffd700;
            font-weight: 800;
            line-height: 1;
        }}
        .reg-num-val {{
            font-size: 1.28mm;
            font-weight: 900;
            color: #ffffff;
            line-height: 1;
        }}
        .feed-type-line {{
            font-size: 0.98mm;
            font-weight: 700;
            color: #e2e8f0;
            line-height: 1.15;
            white-space: nowrap;
        }}
        .feed-type-line .lbl {{
            color: #ffd700;
            font-weight: 800;
        }}

        /* 고시 본문 영역 */
        .sec-content {{
            display: flex;
            flex-direction: column;
            gap: 0.08mm;
            margin: 0.02mm 0;
            text-align: left;
        }}
        
        .info-row {{
            display: flex;
            align-items: baseline;
            font-size: 1.15mm;
            line-height: 1.22;
            color: #f8fafc;
            text-align: left;
        }}
        .sec-lbl {{
            font-weight: 800;
            color: #ffd700;
            margin-right: 0.25mm;
            white-space: nowrap;
            flex-shrink: 0;
            text-align: left;
        }}
        .sec-val {{
            color: #ffffff;
            font-weight: 700;
            flex: 1;
        }}

        .materials-val-box {{
            display: flex;
            flex-direction: column;
            gap: 0.02mm;
            flex: 1;
            color: #f8fafc;
            font-weight: 600;
            line-height: 1.20;
        }}

        .effects-sub-list {{
            list-style: none;
            padding-left: 0.4mm;
            display: flex;
            flex-direction: column;
            gap: 0.04mm;
            margin: 0.01mm 0;
        }}
        .effects-sub-list li {{
            font-size: 1.12mm;
            font-weight: 600;
            color: #f1f5f9;
            line-height: 1.22;
            display: flex;
            align-items: baseline;
            gap: 0.3mm;
        }}
        .effects-sub-list .roman {{
            font-weight: 800;
            color: #ffd700;
            font-size: 1.05mm;
            flex-shrink: 0;
        }}

        /* 용법 및 용량 */
        .dose-box {{
            background: rgba(255, 215, 0, 0.12);
            border: 0.15mm solid #ffd70088;
            border-radius: 0.35mm;
            padding: 0.10mm 0.45mm 0.12mm 0.45mm;
            display: flex;
            flex-direction: column;
            gap: 0.02mm;
            line-height: 1.15;
        }}
        .dose-title {{
            font-size: 1.15mm;
            font-weight: 900;
            color: #ffd700;
            white-space: nowrap;
        }}
        .dose-desc {{
            font-size: 1.15mm;
            font-weight: 800;
            color: #ffffff;
            white-space: nowrap;
        }}
        .dose-sub {{
            font-size: 0.98mm;
            color: #cbd5e1;
            font-weight: 600;
            line-height: 1.05;
        }}

        /* 주의사항 */
        .warn-box {{
            background: rgba(239, 68, 68, 0.12);
            border: 0.15mm solid rgba(239, 68, 68, 0.45);
            border-radius: 0.35mm;
            padding: 0.08mm 0.40mm;
            display: flex;
            flex-direction: column;
            gap: 0.02mm;
        }}
        .warn-title {{
            font-size: 1.06mm;
            font-weight: 800;
            color: #fca5a5;
            display: flex;
            align-items: center;
            gap: 0.25mm;
            line-height: 1;
        }}
        .warn-list {{
            list-style: none;
            padding: 0;
            margin: 0;
            display: flex;
            flex-direction: column;
            gap: 0.02mm;
        }}
        .warn-item {{
            font-size: 0.98mm;
            color: #f1f5f9;
            line-height: 1.16;
            display: flex;
            align-items: baseline;
            gap: 0.2mm;
        }}
        .warn-item .num {{
            font-weight: 700;
            color: #fca5a5;
            flex-shrink: 0;
        }}
        .hl-shake {{
            color: #fde047;
            font-weight: 800;
            text-decoration: underline;
        }}

        /* 제조/유통기한 & 재활용 */
        .mfg-exp-bar-with-recycle {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: rgba(0, 0, 0, 0.50);
            border: 0.12mm solid rgba(255, 255, 255, 0.18);
            border-radius: 0.35mm;
            padding: 0.08mm 0.45mm;
            gap: 0.3mm;
        }}
        .mfg-exp-info {{
            display: flex;
            align-items: baseline;
            gap: 0.6mm;
            font-size: 1.04mm;
            line-height: 1;
        }}
        .mfg-exp-info .lbl {{
            color: #ffd700;
            font-weight: 800;
            margin-right: 0.15mm;
        }}
        .mfg-exp-info .val {{
            color: #ffffff;
            font-weight: 800;
        }}

        .recycle-badge-raised {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            border: 0.12mm solid rgba(255, 215, 0, 0.6);
            border-radius: 0.25mm;
            padding: 0.02mm 0.35mm;
            background: rgba(0,0,0,0.4);
            flex-shrink: 0;
        }}
        .recycle-icon-wrap {{
            display: flex;
            align-items: center;
            gap: 0.2mm;
            line-height: 1;
        }}
        .recycle-icon {{
            width: 1.6mm;
            height: 1.6mm;
        }}
        .recycle-text {{
            font-size: 0.85mm;
            font-weight: 800;
            color: #ffffff;
            letter-spacing: -0.02em;
        }}
        .recycle-sub {{
            font-size: 0.70mm;
            color: #cbd5e1;
            font-weight: 700;
            line-height: 0.9;
        }}

        /* 법정 풋터 */
        .legal-footer {{
            border-top: 0.1mm solid #ffd70055;
            padding-top: 0.08mm;
            display: flex;
            flex-direction: column;
            gap: 0.08mm;
        }}
        .company-block {{
            display: flex;
            align-items: center;
            gap: 0.4mm;
            line-height: 1.1;
        }}
        .company-logo-circle {{
            width: 3.4mm;
            height: 3.4mm;
            border-radius: 50%;
            background: #ffffff;
            border: 0.15mm solid #ffd700;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            flex-shrink: 0;
            box-shadow: 0 0 0.4mm rgba(255, 215, 0, 0.5);
        }}
        .company-logo-img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}
        .company-info {{
            display: flex;
            flex-direction: column;
            gap: 0.02mm;
            flex: 1;
        }}
        .co-role-name {{
            display: flex;
            align-items: baseline;
            gap: 0.35mm;
        }}
        .role-badge {{
            font-size: 0.90mm;
            font-weight: 800;
            color: #fde047;
            background: rgba(0,0,0,0.5);
            border: 0.1mm solid #ffd70066;
            border-radius: 0.2mm;
            padding: 0.02mm 0.25mm;
            line-height: 1;
            white-space: nowrap;
        }}
        .co-name {{
            font-size: 1.12mm;
            font-weight: 900;
            color: #ffffff;
            white-space: nowrap;
        }}
        .co-addr {{
            font-size: 0.90mm;
            color: #cbd5e1;
            white-space: nowrap;
            line-height: 1.1;
        }}
        .tel-accent {{
            color: #ffd700;
            font-weight: 800;
        }}

        /* ============================================================= */
        /* ★ TYPE B: 우측(뒷면) 화이트 배경 + 선명한 블랙 텍스트 전용 스타일 ★ */
        /* ============================================================= */
        .white-back .legal-panel {{
            background: #ffffff !important;
            border: 0.18mm solid #cbd5e1 !important;
            box-shadow: 0 0 1.2mm rgba(0, 0, 0, 0.12) !important;
        }}

        .white-back .legal-header {{
            border-bottom: 0.12mm solid #e2e8f0 !important;
        }}
        .white-back .reg-num-label {{
            color: #92400e !important; /* 딥 앰버/골드 헤더 */
            font-weight: 900 !important;
        }}
        .white-back .reg-num-val {{
            color: #000000 !important;
            font-weight: 900 !important;
        }}
        .white-back .feed-type-line {{
            color: #1e293b !important;
            font-weight: 700 !important;
        }}
        .white-back .feed-type-line .lbl {{
            color: #92400e !important;
            font-weight: 800 !important;
        }}

        .white-back .info-row {{
            color: #0f172a !important;
        }}
        .white-back .sec-lbl {{
            color: #92400e !important;
            font-weight: 900 !important;
        }}
        .white-back .sec-val {{
            color: #0f172a !important;
            font-weight: 700 !important;
        }}
        .white-back .materials-val-box {{
            color: #1e293b !important;
            font-weight: 600 !important;
        }}
        .white-back .materials-val-box div {{
            color: #1e293b !important;
        }}
        .white-back .effects-sub-list li {{
            color: #1e293b !important;
            font-weight: 600 !important;
        }}
        .white-back .effects-sub-list .roman {{
            color: #b45309 !important;
            font-weight: 900 !important;
        }}

        /* 용법용량: 부드러운 웜 옐로우 틴트 */
        .white-back .dose-box {{
            background: #fefce8 !important;
            border: 0.18mm solid #fde047 !important;
        }}
        .white-back .dose-title {{
            color: #854d0e !important;
            font-weight: 900 !important;
        }}
        .white-back .dose-desc {{
            color: #000000 !important;
            font-weight: 800 !important;
        }}
        .white-back .dose-sub {{
            color: #475569 !important;
            font-weight: 700 !important;
        }}

        /* 주의사항: 부드러운 안전 레드 틴트 */
        .white-back .warn-box {{
            background: #fef2f2 !important;
            border: 0.18mm solid #fecaca !important;
        }}
        .white-back .warn-title {{
            color: #b91c1c !important;
            font-weight: 900 !important;
        }}
        .white-back .warn-item {{
            color: #1e293b !important;
            font-weight: 600 !important;
        }}
        .white-back .warn-item .num {{
            color: #b91c1c !important;
            font-weight: 800 !important;
        }}
        .white-back .hl-shake {{
            color: #c2410c !important;
            font-weight: 900 !important;
            background: rgba(254, 215, 170, 0.45) !important;
            padding: 0.05mm 0.25mm !important;
            border-radius: 0.2mm !important;
            text-decoration: none !important;
        }}

        /* 제조일자/유통기한/재활용 */
        .white-back .mfg-exp-bar-with-recycle {{
            background: #f8fafc !important;
            border: 0.15mm solid #e2e8f0 !important;
        }}
        .white-back .mfg-exp-info .lbl {{
            color: #92400e !important;
            font-weight: 800 !important;
        }}
        .white-back .mfg-exp-info .val {{
            color: #0f172a !important;
            font-weight: 900 !important;
        }}
        .white-back .recycle-badge-raised {{
            background: #ffffff !important;
            border: 0.15mm solid #cbd5e1 !important;
        }}
        .white-back .recycle-badge-raised .recycle-icon path {{
            stroke: #0f172a !important;
            stroke-width: 8 !important;
        }}
        .white-back .recycle-text {{
            color: #0f172a !important;
            font-weight: 900 !important;
        }}
        .white-back .recycle-sub {{
            color: #475569 !important;
            font-weight: 700 !important;
        }}

        /* 풋터 */
        .white-back .legal-footer {{
            border-top: 0.12mm solid #e2e8f0 !important;
        }}
        .white-back .role-badge {{
            color: #475569 !important;
            background: #f1f5f9 !important;
            border: 0.12mm solid #cbd5e1 !important;
            font-weight: 800 !important;
        }}
        .white-back .co-name {{
            color: #000000 !important;
            font-weight: 900 !important;
        }}
        .white-back .co-addr {{
            color: #475569 !important;
            font-weight: 600 !important;
        }}
        .white-back .tel-accent {{
            color: #92400e !important;
            font-weight: 800 !important;
        }}
        .white-back .company-logo-circle {{
            background: #ffffff !important;
            border: 0.15mm solid #cbd5e1 !important;
            box-shadow: 0 0 0.3mm rgba(0,0,0,0.15) !important;
        }}

        /* 중앙 디바이더 (화이트 모드일 때 우측 화이트와 자연스러운 조화) */
        .white-back .divider-line {{
            background: linear-gradient(180deg, transparent, #d97706, transparent) !important;
        }}
        .white-back .divider-diamond {{
            background: #fff !important;
            border-color: #d97706 !important;
        }}
    </style>
</head>
<body class="mode-compare print-white">

<!-- 상단 플로팅 실시간 비교 및 인쇄 제어 툴바 -->
<div class="no-print" style="position:fixed; top:12px; left:50%; transform:translateX(-50%); z-index:99999; background:rgba(15,23,42,0.96); border:1px solid #ffd700; padding:10px 22px; border-radius:14px; display:flex; align-items:center; gap:14px; box-shadow:0 12px 35px rgba(0,0,0,0.85); backdrop-filter:blur(10px); font-family:sans-serif;">
    <div style="color:#ffffff; font-size:13px; font-weight:700; display:flex; align-items:center; gap:8px;">
        <span style="color:#ffd700; font-size:15px;">★</span>
        <span style="color:#ffd700; font-weight:800;">몬스멕타 헤파맥스 30ml</span>
        <span style="color:#94a3b8; font-size:12px; background:rgba(255,255,255,0.08); padding:3px 8px; border-radius:6px; border:1px solid rgba(255,255,255,0.15);">정밀 규격 85mm × 40mm</span>
    </div>

    <div style="height:18px; width:1px; background:rgba(255,255,255,0.2);"></div>

    <!-- 비교 모드 선택 버튼군 -->
    <div style="display:flex; gap:6px;">
        <button id="btn-dark" onclick="setViewMode('dark')" style="background:rgba(30,41,59,0.8); color:#ffd700; border:1px solid rgba(255,215,0,0.4); font-weight:700; font-size:12px; padding:6px 13px; border-radius:8px; cursor:pointer; transition:all 0.15s ease;">
            🌙 Type A (올 다크)
        </button>
        <button id="btn-white" onclick="setViewMode('white')" style="background:linear-gradient(135deg, #ffd700, #f59e0b); color:#000; border:1px solid #ffd700; font-weight:900; font-size:12px; padding:6px 13px; border-radius:8px; cursor:pointer; box-shadow:0 0 10px rgba(255,215,0,0.3); transition:all 0.15s ease;">
            ☀️ Type B (화이트 뒷면 · 추천)
        </button>
        <button id="btn-compare" onclick="setViewMode('compare')" style="background:#2563eb; color:#fff; border:1px solid #60a5fa; font-weight:800; font-size:12px; padding:6px 13px; border-radius:8px; cursor:pointer; transition:all 0.15s ease;">
            ⚖️ 상하 동시 비교
        </button>
    </div>

    <div style="height:18px; width:1px; background:rgba(255,255,255,0.2);"></div>

    <!-- 인쇄 타겟 선택 및 인쇄 실행 -->
    <div style="display:flex; align-items:center; gap:6px;">
        <select id="print-target" onchange="updatePrintTarget(this.value)" style="background:#1e293b; color:#e2e8f0; border:1px solid #475569; font-size:12px; font-weight:700; padding:5px 8px; border-radius:6px; cursor:pointer; outline:none;">
            <option value="white" selected>인쇄 대상: Type B (화이트 뒷면)</option>
            <option value="dark">인쇄 대상: Type A (올 다크)</option>
        </select>
        <button onclick="window.print()" style="background:linear-gradient(135deg, #10b981, #059669); color:#fff; font-weight:800; font-size:12px; padding:6px 15px; border:none; border-radius:8px; cursor:pointer; box-shadow:0 3px 10px rgba(16,185,129,0.4); display:flex; align-items:center; gap:5px;">
            <span>🖨️ 인쇄 (Ctrl+P)</span>
        </button>
    </div>
</div>

<!-- 라벨 비교 및 출력 스테이지 -->
<div class="labels-stage">

    <!-- [CARD 1] TYPE A : 오리지널 올 다크 라벨 (85mm x 40mm) -->
    <div class="label-card-wrapper" id="card-dark">
        <div class="label-type-tag tag-dark no-print">
            <span>🌙 Type A : 오리지널 올 다크 테마 (기존)</span>
            <span style="font-weight:400; opacity:0.85;">| 뒷면 다크 투명 패널 + 골드 텍스트 (85mm × 40mm)</span>
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
                        <div class="ing-row"><span class="ing-name">Taurine (타우린)</span><span class="ing-val">200mg</span></div>
                        <div class="ing-row"><span class="ing-name">D-Sorbitol (D-소르비톨)</span><span class="ing-val">4.5mg</span></div>
                        <div class="ing-row"><span class="ing-name">L-lysine HCl</span><span class="ing-val">30mg</span></div>
                        <div class="ing-row"><span class="ing-name">L-methionine</span><span class="ing-val">30mg</span></div>
                        <div class="ing-row"><span class="ing-name">Vitamin B12</span><span class="ing-val">100μg</span></div>
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

                <!-- RIGHT COLUMN (우측 뒷면: 올 다크 법정 패널) -->
                <div class="col-right">
                    <div class="legal-panel">
                        <div class="legal-header">
                            <div class="reg-num-line">
                                <span class="reg-num-label">사료의 성분등록번호 :</span>
                                <span class="reg-num-val">제 XX9UY0145호</span>
                            </div>
                            <div class="feed-type-line">
                                <span class="lbl">사료의 종류와 명칭 / 형태 / 용도 :</span> 보조사료/미생물제/바실러스 서브틸리스l액상l반려동물
                            </div>
                        </div>

                        <div class="sec-content">
                            <div class="info-row">
                                <span class="sec-lbl">등록성분량 :</span>
                                <span class="sec-val">바실러스 서브틸리스 1.0 x 10⁶ cfu/g 이상, 부형제( 정제수 )</span>
                            </div>
                            <div class="info-row">
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

                        <div class="dose-box">
                            <div style="display:flex; align-items:center; gap:0.3mm;">
                                <span class="dose-title">용법 및 용량 :</span>
                                <span class="dose-desc">1일 1~2ml / 체중 5kg</span>
                            </div>
                            <span class="dose-sub">( 1 펌프 = 약 1ml ) - 증상에 따라 조절 가능</span>
                        </div>

                        <div class="warn-box">
                            <div class="warn-title">
                                <svg width="2.0mm" height="2.0mm" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd"></path></svg>
                                <span>주의사항 :</span>
                            </div>
                            <ul class="warn-list">
                                <li class="warn-item"><span class="num">1)</span><span>직사광선을 피하여 서늘한 곳에 보관하십시오.</span></li>
                                <li class="warn-item"><span class="num">2)</span><span>제품특성상 가라앉는 성분들이 있어서 <span class="hl-shake">흔들어서 사용</span>하십시오.</span></li>
                                <li class="warn-item"><span class="num">3)</span><span>제품에 대하여 문의하실 경우 제조원 또는 판매원으로 연락하여 주시기 바랍니다</span></li>
                            </ul>
                        </div>

                        <div class="mfg-exp-bar-with-recycle">
                            <div class="mfg-exp-info">
                                <div style="white-space:nowrap;"><span class="lbl">포장 단위 :</span><span class="val">30ml</span></div>
                                <div style="white-space:nowrap;"><span class="lbl">제조일자 :</span><span class="val">2026.09.15</span></div>
                                <div style="white-space:nowrap;"><span class="lbl">유통기한 :</span><span class="val">제조일로부터 18개월</span></div>
                            </div>
                            <div class="recycle-badge-raised">
                                <div class="recycle-icon-wrap">
                                    <svg class="recycle-icon" viewBox="0 0 100 100">
                                        <path d="M50 14 L88 80 L12 80 Z" fill="none" stroke="#ffd700" stroke-width="7" stroke-linejoin="round"/>
                                    </svg>
                                    <span class="recycle-text">플라스틱</span>
                                </div>
                                <span class="recycle-sub">OTHER</span>
                            </div>
                        </div>

                        <div class="legal-footer">
                            <div class="company-block">
                                <div class="company-logo-circle">
                                    <img src="{logo_b64}" class="company-logo-img">
                                </div>
                                <div class="company-info">
                                    <div class="co-role-name">
                                        <span class="role-badge">위탁제조판매원</span>
                                        <span class="co-name">에스앤제이 동물병원</span>
                                    </div>
                                    <div class="co-addr">대전광역시 유성구 송강동 203-12 | TEL : <span class="tel-accent">042-935-8275</span></div>
                                </div>
                            </div>
                            <div class="company-block">
                                <div class="company-info">
                                    <div class="co-role-name">
                                        <span class="role-badge">제조원</span>
                                        <span class="co-name">오비티(주)</span>
                                    </div>
                                    <div class="co-addr">대전 대덕구 대화로 106번길 66, 3동 307호</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- [CARD 2] TYPE B : 우측 화이트 배경 + 선명한 블랙 텍스트 라벨 (85mm x 40mm) -->
    <div class="label-card-wrapper" id="card-white">
        <div class="label-type-tag tag-white no-print">
            <span>☀️ Type B : 우측(뒷면) 화이트 배경 + 블랙 텍스트 (신규 추천안)</span>
            <span style="font-weight:600; color:#475569;">| 법정고시 가독성 극대화 & 인쇄 선명도 최적화 (85mm × 40mm)</span>
        </div>
        <div class="label-sheet white-back">
            <div class="grid-overlay"></div>
            <div class="top-accent-bar"></div>

            <div class="content-wrap">
                <!-- LEFT COLUMN (전면 메인 - 동일한 프리미엄 딥 앰버/골드 다크 아이덴티티) -->
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
                        <div class="ing-row"><span class="ing-name">Taurine (타우린)</span><span class="ing-val">200mg</span></div>
                        <div class="ing-row"><span class="ing-name">D-Sorbitol (D-소르비톨)</span><span class="ing-val">4.5mg</span></div>
                        <div class="ing-row"><span class="ing-name">L-lysine HCl</span><span class="ing-val">30mg</span></div>
                        <div class="ing-row"><span class="ing-name">L-methionine</span><span class="ing-val">30mg</span></div>
                        <div class="ing-row"><span class="ing-name">Vitamin B12</span><span class="ing-val">100μg</span></div>
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

                <!-- RIGHT COLUMN (우측 뒷면: 화이트 배경 + 선명한 블랙 고대비 패널) -->
                <div class="col-right">
                    <div class="legal-panel">
                        <div class="legal-header">
                            <div class="reg-num-line">
                                <span class="reg-num-label">사료의 성분등록번호 :</span>
                                <span class="reg-num-val">제 XX9UY0145호</span>
                            </div>
                            <div class="feed-type-line">
                                <span class="lbl">사료의 종류와 명칭 / 형태 / 용도 :</span> 보조사료/미생물제/바실러스 서브틸리스l액상l반려동물
                            </div>
                        </div>

                        <div class="sec-content">
                            <div class="info-row">
                                <span class="sec-lbl">등록성분량 :</span>
                                <span class="sec-val">바실러스 서브틸리스 1.0 x 10⁶ cfu/g 이상, 부형제( 정제수 )</span>
                            </div>
                            <div class="info-row">
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

                        <div class="dose-box">
                            <div style="display:flex; align-items:center; gap:0.3mm;">
                                <span class="dose-title">용법 및 용량 :</span>
                                <span class="dose-desc">1일 1~2ml / 체중 5kg</span>
                            </div>
                            <span class="dose-sub">( 1 펌프 = 약 1ml ) - 증상에 따라 조절 가능</span>
                        </div>

                        <div class="warn-box">
                            <div class="warn-title">
                                <svg width="2.0mm" height="2.0mm" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd"></path></svg>
                                <span>주의사항 :</span>
                            </div>
                            <ul class="warn-list">
                                <li class="warn-item"><span class="num">1)</span><span>직사광선을 피하여 서늘한 곳에 보관하십시오.</span></li>
                                <li class="warn-item"><span class="num">2)</span><span>제품특성상 가라앉는 성분들이 있어서 <span class="hl-shake">흔들어서 사용</span>하십시오.</span></li>
                                <li class="warn-item"><span class="num">3)</span><span>제품에 대하여 문의하실 경우 제조원 또는 판매원으로 연락하여 주시기 바랍니다</span></li>
                            </ul>
                        </div>

                        <div class="mfg-exp-bar-with-recycle">
                            <div class="mfg-exp-info">
                                <div style="white-space:nowrap;"><span class="lbl">포장 단위 :</span><span class="val">30ml</span></div>
                                <div style="white-space:nowrap;"><span class="lbl">제조일자 :</span><span class="val">2026.09.15</span></div>
                                <div style="white-space:nowrap;"><span class="lbl">유통기한 :</span><span class="val">제조일로부터 18개월</span></div>
                            </div>
                            <div class="recycle-badge-raised">
                                <div class="recycle-icon-wrap">
                                    <svg class="recycle-icon" viewBox="0 0 100 100">
                                        <path d="M50 14 L88 80 L12 80 Z" fill="none" stroke="#0f172a" stroke-width="7" stroke-linejoin="round"/>
                                    </svg>
                                    <span class="recycle-text">플라스틱</span>
                                </div>
                                <span class="recycle-sub">OTHER</span>
                            </div>
                        </div>

                        <div class="legal-footer">
                            <div class="company-block">
                                <div class="company-logo-circle">
                                    <img src="{logo_b64}" class="company-logo-img">
                                </div>
                                <div class="company-info">
                                    <div class="co-role-name">
                                        <span class="role-badge">위탁제조판매원</span>
                                        <span class="co-name">에스앤제이 동물병원</span>
                                    </div>
                                    <div class="co-addr">대전광역시 유성구 송강동 203-12 | TEL : <span class="tel-accent">042-935-8275</span></div>
                                </div>
                            </div>
                            <div class="company-block">
                                <div class="company-info">
                                    <div class="co-role-name">
                                        <span class="role-badge">제조원</span>
                                        <span class="co-name">오비티(주)</span>
                                    </div>
                                    <div class="co-addr">대전 대덕구 대화로 106번길 66, 3동 307호</div>
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

        // 버튼 스타일 리셋
        btnDark.style.background = 'rgba(30,41,59,0.8)';
        btnDark.style.color = '#ffd700';
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
            btnDark.style.color = '#ffd700';
            btnDark.style.boxShadow = '0 0 10px rgba(255,215,0,0.3)';
            printSelect.value = 'dark';
            document.body.className = 'mode-dark print-dark';
        }} else if (mode === 'white') {{
            cardDark.style.display = 'none';
            cardWhite.style.display = 'flex';
            btnWhite.style.background = 'linear-gradient(135deg, #ffd700, #f59e0b)';
            btnWhite.style.color = '#000000';
            btnWhite.style.boxShadow = '0 0 10px rgba(255,215,0,0.4)';
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

    // URL 파라미터 지원
    const urlParams = new URLSearchParams(window.location.search);
    const initialMode = urlParams.get('mode') || 'compare';
    setViewMode(initialMode);
</script>

</body>
</html>
'''

# Update primary label file
file_primary = "public/assets/labels/monsmecta_hepamax_label.html"
with open(file_primary, "w", encoding="utf-8") as f:
    f.write(generate_label_html("MONSMECTA HEPAMAX Label (85mm x 40mm) - Dark / White Comparison"))
print(f"Updated {file_primary} successfully (85mm x 40mm)!")

# Update secondary file (monsmecta_hepamax_30ml_94x45.html) to also be 85x40mm with same comparison power
file_secondary = "public/assets/labels/monsmecta_hepamax_30ml_94x45.html"
with open(file_secondary, "w", encoding="utf-8") as f:
    f.write(generate_label_html("MONSMECTA HEPAMAX 30ml Label (85mm x 40mm) - Dark / White Comparison"))
print(f"Updated {file_secondary} successfully (85mm x 40mm)!")
