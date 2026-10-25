import re

file_path = 'public/assets/labels/monsmecta_renal_label.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Top accent bar
    ('background: linear-gradient(90deg, #6366f1, #a855f7, #ffd700, #6366f1);', 
     'background: linear-gradient(90deg, #6366f1, #818cf8, #a5b4fc, #6366f1);'),
    
    # Divider line & diamond
    ('background: linear-gradient(180deg, transparent, #818cf8, #ffd700, transparent);', 
     'background: linear-gradient(180deg, transparent, #818cf8, transparent);'),
    ('border: 0.15mm solid #ffd700;\n            transform: rotate(45deg);',
     'border: 0.15mm solid #818cf8;\n            transform: rotate(45deg);'),
     
    # Brand badge
    ('.brand-badge {\n            display: flex;\n            align-items: center;\n            justify-content: center;\n            gap: 0.6mm;\n            background: rgba(0, 0, 0, 0.65);\n            border: 0.15mm solid #ffd700;',
     '.brand-badge {\n            display: flex;\n            align-items: center;\n            justify-content: center;\n            gap: 0.6mm;\n            background: rgba(0, 0, 0, 0.65);\n            border: 0.15mm solid #818cf8;'),
    ('.brand-badge .accent {\n            color: #ffd700;',
     '.brand-badge .accent {\n            color: #818cf8;'),
     
    # En title
    ('.en-title {\n            font-size: 1.62mm;\n            font-weight: 900;\n            color: #ffd700;',
     '.en-title {\n            font-size: 1.62mm;\n            font-weight: 900;\n            color: #818cf8;'),
     
    # Effects top badge & card
    ('.effects-badge-top {\n            position: absolute;\n            top: 0;\n            left: 1.2mm;\n            z-index: 3;\n            background: #ffd700;',
     '.effects-badge-top {\n            position: absolute;\n            top: 0;\n            left: 1.2mm;\n            z-index: 3;\n            background: #818cf8;'),
    ('.effects-card {\n            background: rgba(0, 0, 0, 0.65);\n            border: 0.15mm solid #ffd700;',
     '.effects-card {\n            background: rgba(0, 0, 0, 0.65);\n            border: 0.15mm solid #818cf8;'),
    ('.eff-dot {\n            width: 0.55mm;\n            height: 0.55mm;\n            border-radius: 50%;\n            background: #ffd700;\n            box-shadow: 0 0 0.3mm #ffd700;',
     '.eff-dot {\n            width: 0.55mm;\n            height: 0.55mm;\n            border-radius: 50%;\n            background: #818cf8;\n            box-shadow: 0 0 0.3mm #818cf8;'),
    ('.eff-note {\n            font-size: 0.95mm;\n            color: #fcd34d;',
     '.eff-note {\n            font-size: 0.95mm;\n            color: #a5b4fc;'),
     
    # Ingredients box
    ('border: 0.15mm solid rgba(255, 215, 0, 0.35);',
     'border: 0.15mm solid rgba(129, 140, 248, 0.35);'),
    ('border-bottom: 0.1mm solid rgba(255, 215, 0, 0.4);',
     'border-bottom: 0.1mm solid rgba(129, 140, 248, 0.4);'),
    ('.ing-header .ref {\n            font-size: 1.10mm;\n            color: #ffd700;',
     '.ing-header .ref {\n            font-size: 1.10mm;\n            color: #818cf8;'),
     
    # Pack tag
    ('.pack-tag {\n            align-self: center;\n            background: rgba(0, 0, 0, 0.65);\n            border: 0.18mm solid #ffd700;',
     '.pack-tag {\n            align-self: center;\n            background: rgba(0, 0, 0, 0.65);\n            border: 0.18mm solid #818cf8;'),
    ('.pack-tag .val {\n            color: #ffd700;',
     '.pack-tag .val {\n            color: #818cf8;'),
     
    # Right panel legal
    ('.reg-num-label {\n            font-size: 1.05mm;\n            color: #ffd700;',
     '.reg-num-label {\n            font-size: 1.05mm;\n            color: #818cf8;'),
    ('.feed-type-line .lbl {\n            color: #ffd700;',
     '.feed-type-line .lbl {\n            color: #818cf8;'),
    ('.sec-lbl {\n            font-weight: 800;\n            color: #ffd700;',
     '.sec-lbl {\n            font-weight: 800;\n            color: #818cf8;'),
    ('.effects-sub-list .roman {\n            color: #ffd700;',
     '.effects-sub-list .roman {\n            color: #818cf8;'),
     
    # Dose box
    ('.dose-box {\n            background: rgba(212, 175, 55, 0.18);\n            border: 0.12mm solid #ffd700;',
     '.dose-box {\n            background: rgba(129, 140, 248, 0.15);\n            border: 0.12mm solid #818cf8;'),
    ('.dose-title {\n            font-size: 1.08mm;\n            font-weight: 900;\n            color: #ffd700;',
     '.dose-title {\n            font-size: 1.08mm;\n            font-weight: 900;\n            color: #818cf8;'),
     
    # Warning shake highlight
    ('.warn-item .hl-shake {\n            color: #ffd700;',
     '.warn-item .hl-shake {\n            color: #818cf8;'),
     
    # Footer company logo circle
    ('.company-logo-circle {\n            width: 3.2mm;\n            height: 3.2mm;\n            border-radius: 50%;\n            background: #fff;\n            border: 0.15mm solid #ffd700;',
     '.company-logo-circle {\n            width: 3.2mm;\n            height: 3.2mm;\n            border-radius: 50%;\n            background: #fff;\n            border: 0.15mm solid #818cf8;'),
    ('box-shadow: 0 0 0.6mm rgba(255, 215, 0, 0.6);',
     'box-shadow: 0 0 0.6mm rgba(129, 140, 248, 0.6);'),
     
    # Company info
    ('.company-info .co-title {\n            font-weight: 800;\n            color: #ffd700;',
     '.company-info .co-title {\n            font-weight: 800;\n            color: #818cf8;'),
    ('.company-info .tel-accent {\n            color: #ffd700;',
     '.company-info .tel-accent {\n            color: #818cf8;'),
     
    # Recycle SVG
    ('<path d="M50 14 L88 80 L12 80 Z" fill="none" stroke="#ffd700" stroke-width="7" stroke-linejoin="round"/>',
     '<path d="M50 14 L88 80 L12 80 Z" fill="none" stroke="#818cf8" stroke-width="7" stroke-linejoin="round"/>'),
     
    # Top banner in no-print
    ('border:1px solid #ffd700;', 'border:1px solid #818cf8;'),
    ('<span style="color:#ffd700;">★ 몬스멕타 레날 디톡스', '<span style="color:#818cf8;">★ 몬스멕타 레날 디톡스'),
    ('background:linear-gradient(135deg, #ffd700, #b8860b); color:#000;',
     'background:linear-gradient(135deg, #818cf8, #6366f1); color:#fff;')
]

success_count = 0
for idx, (old, new) in enumerate(replacements):
    if old in content:
        content = content.replace(old, new)
        success_count += 1
        print(f"[{idx+1}/{len(replacements)}] Success")
    else:
        print(f"[{idx+1}/{len(replacements)}] FAILED to find target string:\n{repr(old[:50])}")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nAll replacements processed: {success_count}/{len(replacements)} successful.")
