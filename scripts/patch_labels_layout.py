import re

path = r'c:\Users\master\monsmecta_landing\scripts\rebuild_all_100ml_labels_with_a4_scale.py'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Title/Hero sizes
old_hero = '''    # 몬스멕타는 '오리지널' 수식어 없이 단독 브랜드명이므로 글씨를 키워 존재감 극대화
    if p["id"] == "monsmecta":
        title_font_size = "7.6mm"
        en_title_font_size = "3.2mm"
        en_letter_spacing = "0.12em"
        hero_margin_bottom = "5.4mm"
        calib_title = "몬스멕타™"
    else:
        title_font_size = "5.8mm"
        en_title_font_size = "2.65mm"
        en_letter_spacing = "0.07em"
        hero_margin_bottom = "7.0mm"
        calib_title = f"몬스멕타™ {p['name_ko'].replace('몬스멕타 ', '')}"'''

new_hero = '''    # 몬스멕타는 '오리지널' 수식어 없이 단독 브랜드명이므로 글씨를 키워 존재감 극대화
    if p["id"] == "monsmecta":
        title_font_size = "7.2mm"
        en_title_font_size = "3.0mm"
        en_letter_spacing = "0.10em"
        hero_margin_bottom = "3.2mm"
        calib_title = "몬스멕타™"
    else:
        title_font_size = "5.6mm"
        en_title_font_size = "2.55mm"
        en_letter_spacing = "0.07em"
        hero_margin_bottom = "3.5mm"
        calib_title = f"몬스멕타™ {p['name_ko'].replace('몬스멕타 ', '')}"'''

assert old_hero in text, 'old_hero not found'
text = text.replace(old_hero, new_hero)

# 2. top accent bar & content wrap
old_wrap = '''.top-accent-bar {{
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
        }}'''

new_wrap = '''.top-accent-bar {{
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
            padding: 0.8mm 1.5mm 0.5mm 1.5mm;
            justify-content: space-between;
        }}'''

assert old_wrap in text, 'old_wrap not found'
text = text.replace(old_wrap, new_wrap)

# 3. brand-badge margin
old_badge = '''            margin-bottom: 3.2mm; /* 제품명을 아래로 1줄 내리기 위한 여백 */'''
new_badge = '''            margin-bottom: 2.0mm;'''
assert old_badge in text, 'old_badge not found'
text = text.replace(old_badge, new_badge)

# 4. core-effects-box & ingredients-table-box
old_core = '''        .core-effects-box {{
            background: rgba(0, 0, 0, 0.65);
            border: 0.25mm solid {neon};
            border-radius: 1.0mm;
            padding: 1.1mm 1.6mm 1.0mm 1.6mm;
            position: relative;
            margin-bottom: 5.0mm; /* 주요 성분 데이터 표와의 균형 잡힌 호흡 공간 */
        }}'''
new_core = '''        .core-effects-box {{
            background: rgba(0, 0, 0, 0.65);
            border: 0.25mm solid {neon};
            border-radius: 1.0mm;
            padding: 0.9mm 1.5mm 0.8mm 1.5mm;
            position: relative;
            margin-bottom: 2.5mm;
        }}'''
assert old_core in text, 'old_core not found'
text = text.replace(old_core, new_core)

old_table = '''        .ingredients-table-box {{
            background: rgba(0, 0, 0, 0.65);
            border: 0.25mm solid rgba(255, 255, 255, 0.25);
            border-radius: 1.0mm;
            padding: 1.0mm 1.5mm;
            position: relative;
            margin-bottom: 1.2mm;
            display: flex;
            flex-direction: column;
        }}'''
new_table = '''        .ingredients-table-box {{
            background: rgba(0, 0, 0, 0.65);
            border: 0.25mm solid rgba(255, 255, 255, 0.25);
            border-radius: 1.0mm;
            padding: 0.8mm 1.4mm;
            position: relative;
            margin-bottom: 0.6mm;
            display: flex;
            flex-direction: column;
        }}'''
assert old_table in text, 'old_table not found'
text = text.replace(old_table, new_table)

# 5. col-left-bottom-bar
old_left_bar = '''        .col-left-bottom-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(0, 0, 0, 0.8);
            border: 0.25mm solid {neon};
            border-radius: 0.8mm;
            padding: 0.8mm 1.5mm;
            margin-top: auto;
        }}'''
new_left_bar = '''        .col-left-bottom-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(0, 0, 0, 0.8);
            border: 0.25mm solid {neon};
            border-radius: 0.8mm;
            padding: 0.6mm 1.2mm;
            margin-top: auto;
            margin-bottom: 0.3mm;
        }}'''
assert old_left_bar in text, 'old_left_bar not found'
text = text.replace(old_left_bar, new_left_bar)

# 6. legal-panel and right column styles
old_legal = '''        /* ---------------- [우측 법정 고시사항 패널 공통 타이포그래피] ---------------- */
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

        /* 하단 푸터: 사용자 요청에 따라 로고 및 글씨 크기를 50% 수준으로 축소하여 정갈하게 배치 */
        .original-footer {{
            margin-top: 0.6mm;
            border-top: 0.25mm solid #cbd5e1;
            padding-top: 0.5mm;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1.0mm;
        }}
        .footer-seller {{
            display: flex;
            align-items: center;
            gap: 0.8mm;
            flex: 1.08;
        }}
        .footer-maker {{
            flex: 1.0;
            border-left: 0.25mm solid #cbd5e1;
            padding-left: 1.0mm;
        }}
        .co-logo-circle {{
            width: 3.8mm; /* 기존 7.2mm의 약 50% 축소 */
            height: 3.8mm;
            border-radius: 50%;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            background: #ffffff;
            border: 0.20mm solid #cbd5e1;
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
            line-height: 1.2;
            min-width: 0;
        }}
        .co-line-main {{
            font-size: 1.05mm; /* 기존 1.70mm 대비 약 50% 축소 */
            font-weight: 900;
            white-space: nowrap;
            letter-spacing: -0.01em;
        }}
        .co-line-sub {{
            font-size: 0.90mm; /* 기존 1.48mm 대비 약 50% 축소 */
            font-weight: 700;
            line-height: 1.25;
            letter-spacing: -0.01em;
            word-break: keep-all;
        }}
        .co-tel-line {{
            font-size: 0.90mm; /* 기존 1.45mm 대비 약 50% 축소 */
            font-weight: 800;
            white-space: nowrap;
            letter-spacing: 0;
        }}'''

new_legal = '''        /* ---------------- [우측 법정 고시사항 패널 공통 타이포그래피] ---------------- */
        .legal-panel {{
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 100%;
            padding: 0.3mm 0.8mm 0.2mm 0.8mm;
            border-radius: 1.0mm;
            font-size: 1.48mm;
            line-height: 1.25;
        }}

        .top-reg-grid {{
            display: flex;
            flex-direction: column;
            gap: 0.22mm;
            border-bottom: 0.25mm solid #cbd5e1;
            padding-bottom: 0.30mm;
        }}
        .reg-num-line {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-weight: 900;
            font-size: 1.65mm;
        }}
        .tm-dual-grid {{
            display: flex;
            flex-direction: column;
            gap: 0.18mm;
            border-top: 0.20mm dashed #cbd5e1;
            padding-top: 0.22mm;
            margin-top: 0.10mm;
        }}
        .tm-line {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 1.25mm;
            line-height: 1.18;
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
            font-size: 0.95mm;
            font-weight: 900;
            padding: 0.1mm 0.6mm;
            border-radius: 0.3mm;
            background: #0f172a;
            color: #ffffff;
            margin-right: 0.5mm;
            vertical-align: middle;
            line-height: 1.1;
        }}
        #card-dark .tm-flag {{
            background: {neon};
            color: #000000;
        }}
        .feed-type-line {{
            font-size: 1.32mm;
            line-height: 1.22;
            word-break: break-all;
        }}

        .sec-block {{
            margin-top: 0.25mm;
        }}
        .sec-line {{
            display: flex;
            align-items: baseline;
            gap: 0.6mm;
            line-height: 1.22;
        }}
        .sec-lbl {{
            font-size: 1.50mm;
            font-weight: 900;
            flex-shrink: 0;
        }}
        .sec-val {{
            font-size: 1.42mm;
            line-height: 1.22;
        }}

        .materials-val-box {{
            font-size: 1.32mm;
            line-height: 1.20;
            margin-top: 0.12mm;
            padding-left: 0.3mm;
        }}

        .effects-sub-list {{
            list-style: none;
            padding-left: 0.3mm;
            margin-top: 0.12mm;
            display: flex;
            flex-direction: column;
            gap: 0.20mm;
        }}
        .effects-sub-list li {{
            font-size: 1.32mm;
            line-height: 1.20;
            display: flex;
            align-items: baseline;
            gap: 0.6mm;
        }}
        .effects-sub-list .roman {{
            font-weight: 900;
            font-size: 1.25mm;
            flex-shrink: 0;
        }}

        .dose-box-single {{
            margin-top: 0.25mm;
            border-radius: 0.8mm;
            padding: 0.30mm 0.9mm;
            display: flex;
            flex-direction: column;
            gap: 0.18mm;
            line-height: 1.20;
        }}
        .dose-title-line {{
            display: flex;
            align-items: baseline;
            gap: 1.0mm;
        }}
        .dose-box-single .title {{
            font-weight: 900;
            font-size: 1.50mm;
            white-space: nowrap;
        }}
        .dose-box-single .desc {{
            font-weight: 800;
            font-size: 1.48mm;
            white-space: nowrap;
        }}
        .dose-box-single .sub {{
            font-size: 1.20mm;
            font-weight: 700;
            line-height: 1.18;
            padding-left: 0.3mm;
        }}

        .warn-grid {{
            margin-top: 0.25mm;
            display: flex;
            flex-direction: column;
            gap: 0.16mm;
            font-size: 1.26mm;
            line-height: 1.18;
        }}
        .warn-header {{
            font-weight: 900;
            font-size: 1.40mm;
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
            margin-top: 0.25mm;
            border-top: 0.25mm solid #cbd5e1;
            padding-top: 0.25mm;
            font-size: 1.32mm;
            font-weight: 800;
        }}
        .mfg-date-row {{
            display: flex;
            align-items: center;
            gap: 0.6mm;
        }}
        .mfg-date-row .lbl {{
            font-weight: 900;
        }}
        .recycle-wrap {{
            display: flex;
            align-items: center;
            gap: 0.5mm;
            font-size: 1.15mm;
            font-weight: 900;
        }}
        .recycle-triangle {{
            width: 2.8mm;
            height: 2.8mm;
            border: 0.25mm solid currentColor;
            transform: rotate(45deg);
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 0.3mm;
        }}
        .recycle-triangle span {{
            transform: rotate(-45deg);
            font-size: 0.80mm;
            font-weight: 900;
            line-height: 1;
        }}

        /* 하단 푸터: 사용자 요청에 따라 최적화 및 바닥 잘림 완벽 방지 */
        .original-footer {{
            margin-top: 0.25mm;
            border-top: 0.25mm solid #cbd5e1;
            padding-top: 0.25mm;
            margin-bottom: 0.3mm;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 0.8mm;
        }}
        .footer-seller {{
            display: flex;
            align-items: center;
            gap: 0.6mm;
            flex: 1.12;
        }}
        .footer-maker {{
            flex: 1.0;
            border-left: 0.25mm solid #cbd5e1;
            padding-left: 0.7mm;
        }}
        .co-logo-circle {{
            width: 3.0mm;
            height: 3.0mm;
            border-radius: 50%;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            background: #ffffff;
            border: 0.20mm solid #cbd5e1;
        }}
        .co-logo-img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}
        .co-text-col {{
            display: flex;
            flex-direction: column;
            gap: 0.08mm;
            line-height: 1.12;
            min-width: 0;
        }}
        .co-line-main {{
            font-size: 0.98mm;
            font-weight: 900;
            white-space: nowrap;
            letter-spacing: -0.01em;
        }}
        .co-line-sub {{
            font-size: 0.82mm;
            font-weight: 700;
            line-height: 1.12;
            letter-spacing: -0.01em;
            word-break: keep-all;
        }}
        .co-tel-line {{
            font-size: 0.82mm;
            font-weight: 800;
            white-space: nowrap;
            letter-spacing: 0;
            line-height: 1.12;
        }}'''

assert old_legal in text, 'old_legal not found'
text = text.replace(old_legal, new_legal)

# 7. Update text inside original-footer: 에스앤제이 동물병원 -> S&J 동물병원
text = text.replace('위탁제조판매원 : 에스앤제이 동물병원', '위탁제조판매원 : S&J 동물병원')
text = text.replace('제조원 또는 판매원으로 연락하여 주시기 바랍니다.', '제조원 또는 위탁제조판매원으로 연락하여 주시기 바랍니다.')

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Successfully updated rebuild_all_100ml_labels_with_a4_scale.py')
