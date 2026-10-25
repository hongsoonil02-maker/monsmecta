import re

def refine_label(html_file, is_renal=True):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    theme_color = '#818cf8' if is_renal else '#ffd700'
    theme_rgba = 'rgba(129, 140, 248' if is_renal else 'rgba(212, 175, 55'

    # 1. Widths & Spacing
    # content-wrap padding: 0.20mm 0.30mm 0.20mm 0.30mm (total 84.4mm usable)
    content = re.sub(
        r'/\* 콘텐츠 랩 \*/\s*\.content-wrap\s*\{[^}]+\}',
        '''/* 콘텐츠 랩 */
        .content-wrap {
            position: relative;
            z-index: 2;
            display: flex;
            height: calc(40mm - 0.35mm);
            width: 85mm;
            padding: 0.20mm 0.30mm 0.20mm 0.30mm;
            justify-content: space-between;
        }''',
        content
    )

    # col-left: 39.5mm
    content = re.sub(
        r'/\* 좌측: 전면 메인 노출부[^*]+\*/\s*\.col-left\s*\{[^}]+\}',
        '''/* 좌측: 전면 메인 노출부 (너비 39.5mm) */
        .col-left {
            width: 39.5mm;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }''',
        content
    )

    # divider-col: 1.8mm (충분히 넓고 시원한 좌우 분리 간격)
    content = re.sub(
        r'/\* 중앙 디바이더[^*]+\*/\s*\.divider-col\s*\{[^}]+\}',
        '''/* 중앙 디바이더 (너비 1.8mm: 좌우 분리 간격 확실히 확보) */
        .divider-col {
            width: 1.8mm;
            height: 100%;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
        }''',
        content
    )

    # col-right: 43.1mm (너비 여유 확보)
    content = re.sub(
        r'/\* 우측: 법정 고시사항 노출부[^*]+\*/\s*\.col-right\s*\{[^}]+\}',
        '''/* 우측: 법정 고시사항 노출부 (너비 43.1mm) */
        .col-right {
            width: 43.1mm;
            height: 100%;
            display: flex;
            flex-direction: column;
        }''',
        content
    )

    # 2. Left side: Effects Box
    content = re.sub(
        r'\.effects-card\s*\{[^}]+\}',
        f'''.effects-card {{
            background: rgba(0, 0, 0, 0.65);
            border: 0.15mm solid {theme_color};
            border-radius: 0.5mm;
            padding: 0.85mm 0.50mm 0.25mm 0.50mm;
            display: flex;
            flex-direction: column;
            gap: 0.20mm;
        }}''',
        content
    )

    content = re.sub(
        r'\.eff-item\s*\{[^}]+\}',
        f'''.eff-item {{
            font-size: 1.32mm;
            font-weight: 800;
            color: #ffffff;
            display: inline-flex;
            align-items: center;
            gap: 0.22mm;
            line-height: 1.05;
            white-space: nowrap;
        }}''',
        content
    )

    # 3. Left side: Ingredients Box
    if is_renal:
        # 6 items: generous font size
        content = re.sub(
            r'\.tech-box-ing\s*\{[^}]+\}',
            f'''.tech-box-ing {{
            background: rgba(0, 0, 0, 0.55);
            border: 0.15mm solid {theme_rgba}, 0.35);
            border-radius: 0.5mm;
            padding: 0.18mm 0.50mm;
        }}''',
            content
        )
        content = re.sub(
            r'\.ing-row\s*\{[^}]+\}',
            '''.ing-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 1.32mm;
            line-height: 1.15;
            border-bottom: 0.05mm solid rgba(255, 255, 255, 0.08);
            padding: 0.04mm 0;
        }''',
            content
        )
        content = re.sub(
            r'\.ing-val\s*\{[^}]+\}',
            '''.ing-val {
            font-weight: 900;
            color: #ffffff;
            font-family: 'Orbitron', 'Noto Sans KR', sans-serif;
            font-size: 1.30mm;
        }''',
            content
        )
    else:
        # 7 items: nicely fitted
        content = re.sub(
            r'\.tech-box-ing\s*\{[^}]+\}',
            f'''.tech-box-ing {{
            background: rgba(0, 0, 0, 0.55);
            border: 0.15mm solid {theme_rgba}, 0.35);
            border-radius: 0.5mm;
            padding: 0.12mm 0.50mm;
        }}''',
            content
        )
        content = re.sub(
            r'\.ing-row\s*\{[^}]+\}',
            '''.ing-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 1.25mm;
            line-height: 1.12;
            border-bottom: 0.05mm solid rgba(255, 255, 255, 0.08);
            padding: 0.02mm 0;
        }''',
            content
        )
        content = re.sub(
            r'\.ing-val\s*\{[^}]+\}',
            '''.ing-val {
            font-weight: 900;
            color: #ffffff;
            font-family: 'Orbitron', 'Noto Sans KR', sans-serif;
            font-size: 1.25mm;
        }''',
            content
        )

    # 4. Right side: Legal Header
    content = re.sub(
        r'\.legal-header\s*\{[^}]+\}',
        f'''.legal-header {{
            border-bottom: 0.1mm solid {theme_rgba}, 0.4);
            padding-bottom: 0.04mm;
            display: flex;
            flex-direction: column;
            gap: 0.02mm;
        }}''',
        content
    )

    content = re.sub(
        r'\.reg-num-label\s*\{[^}]+\}',
        f'''.reg-num-label {{
            font-size: 1.16mm;
            color: {theme_color};
            font-weight: 800;
            line-height: 1;
        }}''',
        content
    )

    content = re.sub(
        r'\.reg-num-val\s*\{[^}]+\}',
        '''.reg-num-val {
            font-size: 1.32mm;
            font-weight: 900;
            color: #ffffff;
            line-height: 1;
        }''',
        content
    )

    content = re.sub(
        r'\.feed-type-line\s*\{[^}]+\}',
        f'''.feed-type-line {{
            font-size: 1.02mm;
            font-weight: 700;
            color: #e2e8f0;
            line-height: 1.15;
            white-space: nowrap;
        }}''',
        content
    )

    # 5. Right side: Statutory content rows & Effects list
    content = re.sub(
        r'\.sec-content\s*\{[^}]+\}',
        '''.sec-content {
            display: flex;
            flex-direction: column;
            gap: 0.08mm;
            margin: 0.02mm 0;
            text-align: left;
        }''',
        content
    )

    content = re.sub(
        r'\.info-row\s*\{[^}]+\}',
        '''.info-row {
            display: flex;
            align-items: baseline;
            font-size: 1.15mm;
            line-height: 1.22;
            color: #f8fafc;
            text-align: left;
        }''',
        content
    )

    content = re.sub(
        r'\.sec-lbl\s*\{[^}]+\}',
        f'''.sec-lbl {{
            font-weight: 800;
            color: {theme_color};
            margin-right: 0.25mm;
            white-space: nowrap;
            flex-shrink: 0;
            text-align: left;
        }}''',
        content
    )

    content = re.sub(
        r'\.materials-val-box\s*\{[^}]+\}',
        '''.materials-val-box {
            display: flex;
            flex-direction: column;
            gap: 0.02mm;
            flex: 1;
            color: #f8fafc;
            font-weight: 600;
            line-height: 1.20;
        }''',
        content
    )

    content = re.sub(
        r'\.effects-sub-list\s*\{[^}]+\}',
        '''.effects-sub-list {
            list-style: none;
            padding-left: 0.4mm;
            display: flex;
            flex-direction: column;
            gap: 0.04mm;
            margin: 0.01mm 0;
        }''',
        content
    )

    content = re.sub(
        r'\.effects-sub-list li\s*\{[^}]+\}',
        '''.effects-sub-list li {
            font-size: 1.12mm;
            font-weight: 600;
            color: #f1f5f9;
            line-height: 1.22;
            display: flex;
            align-items: baseline;
        }''',
        content
    )

    content = re.sub(
        r'\.effects-sub-list \.roman\s*\{[^}]+\}',
        f'''.effects-sub-list .roman {{
            color: {theme_color};
            font-weight: 900;
            margin-right: 0.20mm;
            flex-shrink: 0;
        }}''',
        content
    )

    # 6. Dose Box
    content = re.sub(
        r'\.dose-box\s*\{[^}]+\}',
        f'''.dose-box {{
            background: {theme_rgba}, 0.15);
            border: 0.12mm solid {theme_color};
            border-radius: 0.35mm;
            padding: 0.12mm 0.45mm;
            display: flex;
            align-items: baseline;
            justify-content: space-between;
            line-height: 1.12;
            box-sizing: border-box;
            flex-wrap: wrap;
            gap: 0.15mm;
        }}''',
        content
    )

    content = re.sub(
        r'\.dose-title\s*\{[^}]+\}',
        f'''.dose-title {{
            font-size: 1.16mm;
            font-weight: 900;
            color: {theme_color};
            white-space: nowrap;
        }}''',
        content
    )

    content = re.sub(
        r'\.dose-desc\s*\{[^}]+\}',
        '''.dose-desc {
            font-size: 1.25mm;
            font-weight: 900;
            color: #ffffff;
            white-space: nowrap;
        }''',
        content
    )

    content = re.sub(
        r'\.dose-sub\s*\{[^}]+\}',
        '''.dose-sub {
            font-size: 1.02mm;
            color: #f1f5f9;
            font-weight: 700;
            white-space: nowrap;
        }''',
        content
    )

    # 7. Warn Box
    content = re.sub(
        r'\.warn-box\s*\{[^}]+\}',
        '''.warn-box {
            background: rgba(220, 38, 38, 0.15);
            border: 0.15mm solid rgba(239, 68, 68, 0.65);
            border-radius: 0.45mm;
            padding: 0.20mm 0.50mm 0.20mm 0.50mm;
            box-sizing: border-box;
            margin: 0.04mm 0;
        }''',
        content
    )

    content = re.sub(
        r'\.warn-title\s*\{[^}]+\}',
        '''.warn-title {
            font-size: 1.16mm;
            font-weight: 800;
            color: #f87171;
            display: flex;
            align-items: center;
            gap: 0.20mm;
            line-height: 1;
            margin-bottom: 0.08mm;
        }''',
        content
    )

    content = re.sub(
        r'\.warn-list\s*\{[^}]+\}',
        '''.warn-list {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 0.06mm;
        }''',
        content
    )

    content = re.sub(
        r'\.warn-item\s*\{[^}]+\}',
        '''.warn-item {
            font-size: 1.10mm;
            color: #f8fafc;
            line-height: 1.18;
            font-weight: 600;
            display: flex;
            align-items: baseline;
        }''',
        content
    )

    # 8. MFG & EXP Bar with Recycle: prevent awkward wrap!
    content = re.sub(
        r'\.mfg-exp-bar-with-recycle\s*\{[^}]+\}',
        '''.mfg-exp-bar-with-recycle {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 0.1mm solid rgba(255, 255, 255, 0.2);
            border-bottom: 0.1mm solid rgba(255, 255, 255, 0.2);
            padding: 0.08mm 0.20mm;
            line-height: 1;
            box-sizing: border-box;
        }''',
        content
    )

    content = re.sub(
        r'\.mfg-exp-info\s*\{[^}]+\}',
        '''.mfg-exp-info {
            display: flex;
            align-items: center;
            gap: 0.7mm;
            font-size: 0.98mm;
            font-weight: 700;
            color: #e2e8f0;
            white-space: nowrap;
        }''',
        content
    )

    content = re.sub(
        r'\.recycle-sub\s*\{[^}]+\}',
        '''.recycle-sub {
            font-size: 0.90mm;
            font-weight: 900;
            color: #ffffff;
            line-height: 1;
            letter-spacing: 0.02em;
        }''',
        content
    )

    # 9. Company Footer: clean 2-line layout
    content = re.sub(
        r'\.legal-footer\s*\{[^}]+\}',
        '''.legal-footer {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            padding-top: 0.04mm;
            gap: 0.35mm;
        }''',
        content
    )

    content = re.sub(
        r'\.company-info\s*\{[^}]+\}',
        '''.company-info {
            font-size: 0.98mm;
            color: #f1f5f9;
            line-height: 1.20;
            font-weight: 600;
            text-align: left;
        }''',
        content
    )

    content = re.sub(
        r'\.company-info \.co-title\s*\{[^}]+\}',
        f'''.company-info .co-title {{
            font-weight: 800;
            color: {theme_color};
            font-size: 1.06mm;
        }}''',
        content
    )

    # HTML fix for mfg-exp-info so each item has white-space: nowrap
    content = content.replace(
        '<div><span class="lbl">포장 단위 :</span><span class="val">30ml</span></div>',
        '<div style="white-space:nowrap;"><span class="lbl">포장 단위 :</span><span class="val">30ml</span></div>'
    ).replace(
        '<div><span class="lbl">제조일자 :</span><span class="val">2026년 9월 15일</span></div>',
        '<div style="white-space:nowrap;"><span class="lbl">제조일자 :</span><span class="val">2026.09.15</span></div>'
    ).replace(
        '<div><span class="lbl">유통기한 :</span><span class="val">제조일로부터 18 개월</span></div>',
        '<div style="white-space:nowrap;"><span class="lbl">유통기한 :</span><span class="val">제조일로부터 18개월</span></div>'
    )

    # Address fix so numbers stay with street on 2nd line nicely
    content = content.replace(
        '주소 : 경기도 용인시 포곡읍 선장1로 98-8',
        '주소 : 경기도 용인시 포곡읍 선장1로 98-8'
    ).replace(
        '주소 : 경기도 화성시 팔탄면 석포로 74번길 10-25',
        '주소 : 경기도 화성시 팔탄면 석포로 74번길 10-25'
    )

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Refined {html_file} successfully.")

if __name__ == '__main__':
    refine_label('public/assets/labels/monsmecta_renal_label.html', is_renal=True)
    refine_label('public/assets/labels/monsmecta_hepamax_label.html', is_renal=False)
