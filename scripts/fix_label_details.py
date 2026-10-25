import re

def fix_label(html_file, is_renal=True):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    theme_color = '#818cf8' if is_renal else '#ffd700'
    theme_rgba = 'rgba(129, 140, 248' if is_renal else 'rgba(212, 175, 55'

    # Fix legal header spacing so reg-num and feed-type never overlap
    content = re.sub(
        r'\.legal-header\s*\{[^}]+\}',
        f'''.legal-header {{
            border-bottom: 0.1mm solid {theme_rgba}, 0.4);
            padding-bottom: 0.10mm;
            display: flex;
            flex-direction: column;
            gap: 0.16mm;
        }}''',
        content
    )

    content = re.sub(
        r'\.reg-num-line\s*\{[^}]+\}',
        '''.reg-num-line {
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            line-height: 1.15;
        }''',
        content
    )

    content = re.sub(
        r'\.reg-num-label\s*\{[^}]+\}',
        f'''.reg-num-label {{
            font-size: 1.14mm;
            color: {theme_color};
            font-weight: 800;
            line-height: 1;
        }}''',
        content
    )

    content = re.sub(
        r'\.reg-num-val\s*\{[^}]+\}',
        '''.reg-num-val {
            font-size: 1.28mm;
            font-weight: 900;
            color: #ffffff;
            line-height: 1;
        }''',
        content
    )

    content = re.sub(
        r'\.feed-type-line\s*\{[^}]+\}',
        f'''.feed-type-line {{
            font-size: 0.98mm;
            font-weight: 700;
            color: #e2e8f0;
            line-height: 1.15;
            white-space: nowrap;
        }}''',
        content
    )

    # Fix footer spacing so both companies have comfortable breathing room
    content = re.sub(
        r'\.legal-footer\s*\{[^}]+\}',
        '''.legal-footer {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            padding-top: 0.08mm;
            gap: 0.50mm;
        }''',
        content
    )

    content = re.sub(
        r'\.company-block\s*\{[^}]+\}',
        '''.company-block {
            display: flex;
            align-items: flex-start;
            gap: 0.25mm;
            flex: 1;
        }''',
        content
    )

    content = re.sub(
        r'\.company-info\s*\{[^}]+\}',
        '''.company-info {
            font-size: 0.92mm;
            color: #f1f5f9;
            line-height: 1.18;
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
            font-size: 1.00mm;
        }}''',
        content
    )

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed {html_file}")

if __name__ == '__main__':
    fix_label('public/assets/labels/monsmecta_renal_label.html', is_renal=True)
    fix_label('public/assets/labels/monsmecta_hepamax_label.html', is_renal=False)
