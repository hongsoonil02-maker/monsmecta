import re

def update_renal_label():
    path = 'public/assets/labels/monsmecta_renal_label.html'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Layout & Divider spacing
    content = re.sub(
        r'/\* 콘텐츠 랩 \*/\s*\.content-wrap\s*\{[^}]+\}',
        '''/* 콘텐츠 랩 */
        .content-wrap {
            position: relative;
            z-index: 2;
            display: flex;
            height: calc(40mm - 0.35mm);
            width: 85mm;
            padding: 0.20mm 0.35mm 0.20mm 0.35mm;
            justify-content: space-between;
        }''',
        content
    )

    content = re.sub(
        r'/\* 좌측: 전면 메인 노출부[^*]+\*/\s*\.col-left\s*\{[^}]+\}',
        '''/* 좌측: 전면 메인 노출부 (너비 39.8mm) */
        .col-left {
            width: 39.8mm;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }''',
        content
    )

    content = re.sub(
        r'/\* 중앙 디바이더 \*/\s*\.divider-col\s*\{[^}]+\}',
        '''/* 중앙 디바이더 (너비 2.0mm로 간격 시원하게 확장) */
        .divider-col {
            width: 2.0mm;
            height: 100%;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
        }''',
        content
    )

    content = re.sub(
        r'/\* 우측: 법정 고시사항 노출부[^*]+\*/\s*\.col-right\s*\{[^}]+\}',
        '''/* 우측: 법정 고시사항 노출부 (너비 42.5mm) */
        .col-right {
            width: 42.5mm;
            height: 100%;
            display: flex;
            flex-direction: column;
        }''',
        content
    )

    # 2. Effects card & items in col-left
    content = re.sub(
        r'\.effects-card\s*\{[^}]+\}',
        '''.effects-card {
            background: rgba(0, 0, 0, 0.65);
            border: 0.15mm solid #818cf8;
            border-radius: 0.5mm;
            padding: 0.85mm 0.50mm 0.25mm 0.50mm;
            display: flex;
            flex-direction: column;
            gap: 0.18mm;
        }''',
        content
    )

    content = re.sub(
        r'\.effects-row\s*\{[^}]+\}',
        '''.effects-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            line-height: 1.10;
            white-space: nowrap;
        }''',
        content
    )

    content = re.sub(
        r'\.eff-item\s*\{[^}]+\}',
        '''.eff-item {
            font-size: 1.34mm;
            font-weight: 800;
            color: #ffffff;
            display: inline-flex;
            align-items: center;
            gap: 0.22mm;
            line-height: 1.05;
            white-space: nowrap;
        }''',
        content
    )

    content = re.sub(
        r'\.eff-dot\s*\{[^}]+\}',
        '''.eff-dot {
            width: 0.60mm;
            height: 0.60mm;
            border-radius: 50%;
            background: #818cf8;
            box-shadow: 0 0 0.3mm #818cf8;
            flex-shrink: 0;
        }''',
        content
    )

    content = re.sub(
        r'\.eff-note\s*\{[^}]+\}',
        '''.eff-note {
            font-size: 1.05mm;
            color: #a5b4fc;
            font-weight: 700;
            line-height: 1;
            white-space: nowrap;
            opacity: 0.95;
        }''',
        content
    )

    # 3. Ingredients table in col-left
    content = re.sub(
        r'\.tech-box-ing\s*\{[^}]+\}',
        '''.tech-box-ing {
            background: rgba(0, 0, 0, 0.55);
            border: 0.15mm solid rgba(129, 140, 248, 0.35);
            border-radius: 0.5mm;
            padding: 0.18mm 0.50mm;
        }''',
        content
    )

    content = re.sub(
        r'\.ing-header\s*\{[^}]+\}',
        '''.ing-header {
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            border-bottom: 0.1mm solid rgba(129, 140, 248, 0.4);
            padding-bottom: 0.04mm;
            margin-bottom: 0.04mm;
        }''',
        content
    )

    content = re.sub(
        r'\.ing-header \.title\s*\{[^}]+\}',
        '''.ing-header .title {
            font-size: 1.30mm;
            font-weight: 800;
            color: #fff;
        }''',
        content
    )

    content = re.sub(
        r'\.ing-header \.ref\s*\{[^}]+\}',
        '''.ing-header .ref {
            font-size: 1.15mm;
            color: #818cf8;
            font-weight: 800;
        }''',
        content
    )

    content = re.sub(
        r'\.ing-row\s*\{[^}]+\}',
        '''.ing-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 1.34mm;
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
            font-size: 1.32mm;
        }''',
        content
    )

    content = re.sub(
        r'\.pack-tag\s*\{[^}]+\}',
        '''.pack-tag {
            align-self: center;
            background: rgba(0, 0, 0, 0.65);
            border: 0.18mm solid #818cf8;
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
        }''',
        content
    )

    # 4. Right panel (col-right legal)
    content = re.sub(
        r'\.legal-panel\s*\{[^}]+\}',
        '''.legal-panel {
            background: rgba(0, 0, 0, 0.55);
            border: 0.15mm solid rgba(255, 255, 255, 0.22);
            border-radius: 0.5mm;
            height: 100%;
            padding: 0.15mm 0.50mm 0.12mm 0.50mm;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }''',
        content
    )

    content = re.sub(
        r'\.legal-header\s*\{[^}]+\}',
        '''.legal-header {
            border-bottom: 0.1mm solid rgba(129, 140, 248, 0.4);
            padding-bottom: 0.04mm;
            display: flex;
            flex-direction: column;
            gap: 0.02mm;
        }''',
        content
    )

    content = re.sub(
        r'\.reg-num-label\s*\{[^}]+\}',
        '''.reg-num-label {
            font-size: 1.18mm;
            color: #818cf8;
            font-weight: 800;
            line-height: 1;
        }''',
        content
    )

    content = re.sub(
        r'\.reg-num-val\s*\{[^}]+\}',
        '''.reg-num-val {
            font-size: 1.35mm;
            font-weight: 900;
            color: #ffffff;
            line-height: 1;
        }''',
        content
    )

    content = re.sub(
        r'\.feed-type-line\s*\{[^}]+\}',
        '''.feed-type-line {
            font-size: 1.05mm;
            font-weight: 700;
            color: #e2e8f0;
            line-height: 1.12;
            white-space: nowrap;
        }''',
        content
    )

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
            font-size: 1.16mm;
            line-height: 1.14;
            color: #f8fafc;
            text-align: left;
        }''',
        content
    )

    content = re.sub(
        r'\.sec-lbl\s*\{[^}]+\}',
        '''.sec-lbl {
            font-weight: 800;
            color: #818cf8;
            margin-right: 0.25mm;
            white-space: nowrap;
            flex-shrink: 0;
            text-align: left;
        }''',
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
            line-height: 1.14;
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
            gap: 0.02mm;
            margin: 0.01mm 0;
        }''',
        content
    )

    content = re.sub(
        r'\.effects-sub-list li\s*\{[^}]+\}',
        '''.effects-sub-list li {
            font-size: 1.14mm;
            font-weight: 600;
            color: #f1f5f9;
            line-height: 1.12;
            display: flex;
            align-items: baseline;
        }''',
        content
    )

    content = re.sub(
        r'\.effects-sub-list \.roman\s*\{[^}]+\}',
        '''.effects-sub-list .roman {
            color: #818cf8;
            font-weight: 900;
            margin-right: 0.20mm;
            flex-shrink: 0;
        }''',
        content
    )

    content = re.sub(
        r'\.dose-box\s*\{[^}]+\}',
        '''.dose-box {
            background: rgba(129, 140, 248, 0.15);
            border: 0.12mm solid #818cf8;
            border-radius: 0.35mm;
            padding: 0.10mm 0.40mm;
            display: flex;
            align-items: baseline;
            justify-content: space-between;
            line-height: 1.10;
            box-sizing: border-box;
            flex-wrap: wrap;
            gap: 0.15mm;
        }''',
        content
    )

    content = re.sub(
        r'\.dose-title\s*\{[^}]+\}',
        '''.dose-title {
            font-size: 1.18mm;
            font-weight: 900;
            color: #818cf8;
            white-space: nowrap;
        }''',
        content
    )

    content = re.sub(
        r'\.dose-desc\s*\{[^}]+\}',
        '''.dose-desc {
            font-size: 1.28mm;
            font-weight: 900;
            color: #ffffff;
            white-space: nowrap;
        }''',
        content
    )

    content = re.sub(
        r'\.dose-sub\s*\{[^}]+\}',
        '''.dose-sub {
            font-size: 1.05mm;
            color: #f1f5f9;
            font-weight: 700;
            white-space: nowrap;
        }''',
        content
    )

    content = re.sub(
        r'\.warn-box\s*\{[^}]+\}',
        '''.warn-box {
            background: rgba(220, 38, 38, 0.15);
            border: 0.15mm solid rgba(239, 68, 68, 0.65);
            border-radius: 0.45mm;
            padding: 0.18mm 0.50mm 0.18mm 0.50mm;
            box-sizing: border-box;
            margin: 0.04mm 0;
        }''',
        content
    )

    content = re.sub(
        r'\.warn-title\s*\{[^}]+\}',
        '''.warn-title {
            font-size: 1.18mm;
            font-weight: 800;
            color: #f87171;
            display: flex;
            align-items: center;
            gap: 0.20mm;
            line-height: 1;
            margin-bottom: 0.06mm;
        }''',
        content
    )

    content = re.sub(
        r'\.warn-list\s*\{[^}]+\}',
        '''.warn-list {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 0.05mm;
        }''',
        content
    )

    content = re.sub(
        r'\.warn-item\s*\{[^}]+\}',
        '''.warn-item {
            font-size: 1.12mm;
            color: #f8fafc;
            line-height: 1.14;
            font-weight: 600;
            display: flex;
            align-items: baseline;
        }''',
        content
    )

    content = re.sub(
        r'\.mfg-exp-bar-with-recycle\s*\{[^}]+\}',
        '''.mfg-exp-bar-with-recycle {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 0.1mm solid rgba(255, 255, 255, 0.2);
            border-bottom: 0.1mm solid rgba(255, 255, 255, 0.2);
            padding: 0.06mm 0.20mm;
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
            gap: 0.8mm;
            font-size: 1.12mm;
            font-weight: 700;
            color: #e2e8f0;
        }''',
        content
    )

    content = re.sub(
        r'\.recycle-sub\s*\{[^}]+\}',
        '''.recycle-sub {
            font-size: 0.95mm;
            font-weight: 900;
            color: #ffffff;
            line-height: 1;
            letter-spacing: 0.02em;
        }''',
        content
    )

    content = re.sub(
        r'\.legal-footer\s*\{[^}]+\}',
        '''.legal-footer {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            padding-top: 0.04mm;
            gap: 0.3mm;
        }''',
        content
    )

    content = re.sub(
        r'\.company-info\s*\{[^}]+\}',
        '''.company-info {
            font-size: 1.02mm;
            color: #f1f5f9;
            line-height: 1.12;
            font-weight: 600;
            text-align: left;
        }''',
        content
    )

    content = re.sub(
        r'\.company-info \.co-title\s*\{[^}]+\}',
        '''.company-info .co-title {
            font-weight: 800;
            color: #818cf8;
            font-size: 1.10mm;
        }''',
        content
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Renal label updated successfully.")

def update_hepamax_label():
    path = 'public/assets/labels/monsmecta_hepamax_label.html'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Layout & Divider spacing
    content = re.sub(
        r'/\* 콘텐츠 랩 \*/\s*\.content-wrap\s*\{[^}]+\}',
        '''/* 콘텐츠 랩 */
        .content-wrap {
            position: relative;
            z-index: 2;
            display: flex;
            height: calc(40mm - 0.35mm);
            width: 85mm;
            padding: 0.20mm 0.35mm 0.20mm 0.35mm;
            justify-content: space-between;
        }''',
        content
    )

    content = re.sub(
        r'/\* 좌측: 전면 메인 노출부[^*]+\*/\s*\.col-left\s*\{[^}]+\}',
        '''/* 좌측: 전면 메인 노출부 (너비 39.8mm) */
        .col-left {
            width: 39.8mm;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }''',
        content
    )

    content = re.sub(
        r'/\* 중앙 디바이더 \*/\s*\.divider-col\s*\{[^}]+\}',
        '''/* 중앙 디바이더 (너비 2.0mm로 간격 시원하게 확장) */
        .divider-col {
            width: 2.0mm;
            height: 100%;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
        }''',
        content
    )

    content = re.sub(
        r'/\* 우측: 법정 고시사항 노출부[^*]+\*/\s*\.col-right\s*\{[^}]+\}',
        '''/* 우측: 법정 고시사항 노출부 (너비 42.5mm) */
        .col-right {
            width: 42.5mm;
            height: 100%;
            display: flex;
            flex-direction: column;
        }''',
        content
    )

    # 2. Effects card & items in col-left
    content = re.sub(
        r'\.effects-card\s*\{[^}]+\}',
        '''.effects-card {
            background: rgba(0, 0, 0, 0.65);
            border: 0.15mm solid #ffd700;
            border-radius: 0.5mm;
            padding: 0.85mm 0.50mm 0.25mm 0.50mm;
            display: flex;
            flex-direction: column;
            gap: 0.18mm;
        }''',
        content
    )

    content = re.sub(
        r'\.effects-row\s*\{[^}]+\}',
        '''.effects-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            line-height: 1.10;
            white-space: nowrap;
        }''',
        content
    )

    content = re.sub(
        r'\.eff-item\s*\{[^}]+\}',
        '''.eff-item {
            font-size: 1.34mm;
            font-weight: 800;
            color: #ffffff;
            display: inline-flex;
            align-items: center;
            gap: 0.22mm;
            line-height: 1.05;
            white-space: nowrap;
        }''',
        content
    )

    content = re.sub(
        r'\.eff-dot\s*\{[^}]+\}',
        '''.eff-dot {
            width: 0.60mm;
            height: 0.60mm;
            border-radius: 50%;
            background: #ffd700;
            box-shadow: 0 0 0.3mm #ffd700;
            flex-shrink: 0;
        }''',
        content
    )

    content = re.sub(
        r'\.eff-note\s*\{[^}]+\}',
        '''.eff-note {
            font-size: 1.05mm;
            color: #fcd34d;
            font-weight: 700;
            line-height: 1;
            white-space: nowrap;
            opacity: 0.95;
        }''',
        content
    )

    # 3. Ingredients table in col-left (Hepamax has 7 items, compact padding, large fonts)
    content = re.sub(
        r'\.tech-box-ing\s*\{[^}]+\}',
        '''.tech-box-ing {
            background: rgba(0, 0, 0, 0.55);
            border: 0.15mm solid rgba(255, 215, 0, 0.35);
            border-radius: 0.5mm;
            padding: 0.12mm 0.50mm;
        }''',
        content
    )

    content = re.sub(
        r'\.ing-header\s*\{[^}]+\}',
        '''.ing-header {
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            border-bottom: 0.1mm solid rgba(255, 215, 0, 0.4);
            padding-bottom: 0.04mm;
            margin-bottom: 0.04mm;
        }''',
        content
    )

    content = re.sub(
        r'\.ing-header \.title\s*\{[^}]+\}',
        '''.ing-header .title {
            font-size: 1.28mm;
            font-weight: 800;
            color: #fff;
        }''',
        content
    )

    content = re.sub(
        r'\.ing-header \.ref\s*\{[^}]+\}',
        '''.ing-header .ref {
            font-size: 1.15mm;
            color: #ffd700;
            font-weight: 800;
        }''',
        content
    )

    content = re.sub(
        r'\.ing-row\s*\{[^}]+\}',
        '''.ing-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 1.28mm;
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
            font-size: 1.28mm;
        }''',
        content
    )

    content = re.sub(
        r'\.pack-tag\s*\{[^}]+\}',
        '''.pack-tag {
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
        }''',
        content
    )

    # 4. Right panel (col-right legal)
    content = re.sub(
        r'\.legal-panel\s*\{[^}]+\}',
        '''.legal-panel {
            background: rgba(0, 0, 0, 0.55);
            border: 0.15mm solid rgba(255, 255, 255, 0.22);
            border-radius: 0.5mm;
            height: 100%;
            padding: 0.15mm 0.50mm 0.12mm 0.50mm;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }''',
        content
    )

    content = re.sub(
        r'\.legal-header\s*\{[^}]+\}',
        '''.legal-header {
            border-bottom: 0.1mm solid rgba(255, 215, 0, 0.4);
            padding-bottom: 0.04mm;
            display: flex;
            flex-direction: column;
            gap: 0.02mm;
        }''',
        content
    )

    content = re.sub(
        r'\.reg-num-label\s*\{[^}]+\}',
        '''.reg-num-label {
            font-size: 1.18mm;
            color: #ffd700;
            font-weight: 800;
            line-height: 1;
        }''',
        content
    )

    content = re.sub(
        r'\.reg-num-val\s*\{[^}]+\}',
        '''.reg-num-val {
            font-size: 1.35mm;
            font-weight: 900;
            color: #ffffff;
            line-height: 1;
        }''',
        content
    )

    content = re.sub(
        r'\.feed-type-line\s*\{[^}]+\}',
        '''.feed-type-line {
            font-size: 1.05mm;
            font-weight: 700;
            color: #e2e8f0;
            line-height: 1.12;
            white-space: nowrap;
        }''',
        content
    )

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
            font-size: 1.16mm;
            line-height: 1.14;
            color: #f8fafc;
            text-align: left;
        }''',
        content
    )

    content = re.sub(
        r'\.sec-lbl\s*\{[^}]+\}',
        '''.sec-lbl {
            font-weight: 800;
            color: #ffd700;
            margin-right: 0.25mm;
            white-space: nowrap;
            flex-shrink: 0;
            text-align: left;
        }''',
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
            line-height: 1.14;
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
            gap: 0.02mm;
            margin: 0.01mm 0;
        }''',
        content
    )

    content = re.sub(
        r'\.effects-sub-list li\s*\{[^}]+\}',
        '''.effects-sub-list li {
            font-size: 1.14mm;
            font-weight: 600;
            color: #f1f5f9;
            line-height: 1.12;
            display: flex;
            align-items: baseline;
        }''',
        content
    )

    content = re.sub(
        r'\.effects-sub-list \.roman\s*\{[^}]+\}',
        '''.effects-sub-list .roman {
            color: #ffd700;
            font-weight: 900;
            margin-right: 0.20mm;
            flex-shrink: 0;
        }''',
        content
    )

    content = re.sub(
        r'\.dose-box\s*\{[^}]+\}',
        '''.dose-box {
            background: rgba(212, 175, 55, 0.18);
            border: 0.12mm solid #ffd700;
            border-radius: 0.35mm;
            padding: 0.10mm 0.40mm;
            display: flex;
            align-items: baseline;
            justify-content: space-between;
            line-height: 1.10;
            box-sizing: border-box;
            flex-wrap: wrap;
            gap: 0.15mm;
        }''',
        content
    )

    content = re.sub(
        r'\.dose-title\s*\{[^}]+\}',
        '''.dose-title {
            font-size: 1.18mm;
            font-weight: 900;
            color: #ffd700;
            white-space: nowrap;
        }''',
        content
    )

    content = re.sub(
        r'\.dose-desc\s*\{[^}]+\}',
        '''.dose-desc {
            font-size: 1.28mm;
            font-weight: 900;
            color: #ffffff;
            white-space: nowrap;
        }''',
        content
    )

    content = re.sub(
        r'\.dose-sub\s*\{[^}]+\}',
        '''.dose-sub {
            font-size: 1.05mm;
            color: #f1f5f9;
            font-weight: 700;
            white-space: nowrap;
        }''',
        content
    )

    content = re.sub(
        r'\.warn-box\s*\{[^}]+\}',
        '''.warn-box {
            background: rgba(220, 38, 38, 0.15);
            border: 0.15mm solid rgba(239, 68, 68, 0.65);
            border-radius: 0.45mm;
            padding: 0.18mm 0.50mm 0.18mm 0.50mm;
            box-sizing: border-box;
            margin: 0.04mm 0;
        }''',
        content
    )

    content = re.sub(
        r'\.warn-title\s*\{[^}]+\}',
        '''.warn-title {
            font-size: 1.18mm;
            font-weight: 800;
            color: #f87171;
            display: flex;
            align-items: center;
            gap: 0.20mm;
            line-height: 1;
            margin-bottom: 0.06mm;
        }''',
        content
    )

    content = re.sub(
        r'\.warn-list\s*\{[^}]+\}',
        '''.warn-list {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 0.05mm;
        }''',
        content
    )

    content = re.sub(
        r'\.warn-item\s*\{[^}]+\}',
        '''.warn-item {
            font-size: 1.12mm;
            color: #f8fafc;
            line-height: 1.14;
            font-weight: 600;
            display: flex;
            align-items: baseline;
        }''',
        content
    )

    content = re.sub(
        r'\.mfg-exp-bar-with-recycle\s*\{[^}]+\}',
        '''.mfg-exp-bar-with-recycle {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 0.1mm solid rgba(255, 255, 255, 0.2);
            border-bottom: 0.1mm solid rgba(255, 255, 255, 0.2);
            padding: 0.06mm 0.20mm;
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
            gap: 0.8mm;
            font-size: 1.12mm;
            font-weight: 700;
            color: #e2e8f0;
        }''',
        content
    )

    content = re.sub(
        r'\.recycle-sub\s*\{[^}]+\}',
        '''.recycle-sub {
            font-size: 0.95mm;
            font-weight: 900;
            color: #ffffff;
            line-height: 1;
            letter-spacing: 0.02em;
        }''',
        content
    )

    content = re.sub(
        r'\.legal-footer\s*\{[^}]+\}',
        '''.legal-footer {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            padding-top: 0.04mm;
            gap: 0.3mm;
        }''',
        content
    )

    content = re.sub(
        r'\.company-info\s*\{[^}]+\}',
        '''.company-info {
            font-size: 1.02mm;
            color: #f1f5f9;
            line-height: 1.12;
            font-weight: 600;
            text-align: left;
        }''',
        content
    )

    content = re.sub(
        r'\.company-info \.co-title\s*\{[^}]+\}',
        '''.company-info .co-title {
            font-weight: 800;
            color: #ffd700;
            font-size: 1.10mm;
        }''',
        content
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Hepamax label updated successfully.")

if __name__ == '__main__':
    update_renal_label()
    update_hepamax_label()
