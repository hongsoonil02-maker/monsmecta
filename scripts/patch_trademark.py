import sys

def main():
    with open('scripts/generate_all_lineup_labels_with_white_back.py', 'r', encoding='utf-8') as f:
        text = f.read()

    css_old = """        .reg-num-val {{
            font-size: 1.30mm;
            font-weight: 900;
            line-height: 1;
        }}
        .feed-type-line {{"""

    css_new = """        .reg-num-val {{
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
        .feed-type-line {{"""

    if css_old not in text:
        print("ERROR: css_old not found")
        sys.exit(1)
    text = text.replace(css_old, css_new, 1)

    theme_dark_old = """        #card-dark .reg-num-val {{ color: #ffffff; }}
        #card-dark .feed-type-line {{ color: #ffffff; }}"""

    theme_dark_new = """        #card-dark .reg-num-val {{ color: #ffffff; }}
        #card-dark .tm-dual-grid {{ border-top-color: rgba(255, 255, 255, 0.25); }}
        #card-dark .tm-line .tm-lbl {{ color: {neon}; font-weight: 800; }}
        #card-dark .tm-line .tm-num {{ color: #fef08a; font-weight: 900; }}
        #card-dark .feed-type-line {{ color: #ffffff; }}"""

    if theme_dark_old not in text:
        print("ERROR: theme_dark_old not found")
        sys.exit(1)
    text = text.replace(theme_dark_old, theme_dark_new, 1)

    theme_white_old = """        #card-white .reg-num-val {{ color: #000000 !important; font-weight: 900 !important; }}
        #card-white .feed-type-line {{ color: #000000 !important; font-weight: 700 !important; }}"""

    theme_white_new = """        #card-white .reg-num-val {{ color: #000000 !important; font-weight: 900 !important; }}
        #card-white .tm-dual-grid {{ border-top-color: #94a3b8 !important; }}
        #card-white .tm-line .tm-lbl {{ color: #000000 !important; font-weight: 900 !important; }}
        #card-white .tm-line .tm-num {{ color: #000000 !important; font-weight: 900 !important; }}
        #card-white .feed-type-line {{ color: #000000 !important; font-weight: 700 !important; }}"""

    if theme_white_old not in text:
        print("ERROR: theme_white_old not found")
        sys.exit(1)
    text = text.replace(theme_white_old, theme_white_new, 1)

    header_old = """                            <div class="reg-num-line">
                                <span class="reg-num-label">사료의 성분등록번호 :</span>
                                <span class="reg-num-val">{p["reg_no"]}</span>
                            </div>
                            <div class="feed-type-line">"""

    tm_block_html = """                            <div class="reg-num-line">
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
                            <div class="feed-type-line">"""

    count = text.count(header_old)
    if count != 2:
        print(f"ERROR: Expected 2 occurrences of header_old, found {count}")
        sys.exit(1)
    text = text.replace(header_old, tm_block_html)

    with open('scripts/generate_all_lineup_labels_with_white_back.py', 'w', encoding='utf-8') as f:
        f.write(text)

    print("SUCCESS: generate_all_lineup_labels_with_white_back.py updated successfully.")

if __name__ == '__main__':
    main()

