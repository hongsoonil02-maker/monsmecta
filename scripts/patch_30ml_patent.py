import os

with open('scripts/generate_all_30ml_labels.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('50/041,096')
if pos == -1:
    print("50/041,096 not found")
    exit(1)

start = text.rfind('reg-num-line', 0, pos) - 12
end = text.find('</div>', pos) + 6
target = text[start:end]

replacement = """<div class="reg-num-line">
                            <span class="reg-num-label">사료의 성분등록번호 :</span>
                            <span class="reg-num-val">{p["reg_no"]}</span>
                        </div>
                        <div class="tm-dual-grid" style="display:flex; justify-content:space-between; align-items:center; border-top:0.15mm dashed {p['border']}; border-bottom:0.15mm dashed {p['border']}; padding:0.15mm 0; margin:0.1mm 0; font-size:0.92mm; line-height:1.15;">
                            <span style="font-weight:800; color:{p['neon']}; white-space:nowrap;">🇰🇷 특허청 상표출원: <strong style='color:#ffffff;'>제40-2026-0140274호 (05류/31류)</strong></span>
                            <span style="font-weight:800; color:{p['neon_sub']}; white-space:nowrap;">🇺🇸 USPTO: <strong style='color:#ffffff;'>App No. 50/041,096</strong></span>
                        </div>"""

text = text.replace(target, replacement)
with open('scripts/generate_all_30ml_labels.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated generate_all_30ml_labels.py successfully")

