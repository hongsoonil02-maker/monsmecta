import os

with open('scripts/generate_all_30ml_labels.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = "for p in PRODUCTS:\n    target_path = os.path.join(out_dir, p[\"file_name\"])"
replacement = "if __name__ == '__main__':\n    for p in PRODUCTS:\n        target_path = os.path.join(out_dir, p[\"file_name\"])\n        html_content = render_html(p)\n        with open(target_path, \"w\", encoding=\"utf-8\") as f:\n            f.write(html_content)\n        print(f\"Generated {p['name_ko']} -> {target_path}\")\n    print('All 11 product labels generated successfully!')"

if target in text:
    # replace the tail loop
    pos = text.find(target)
    text = text[:pos] + replacement
    with open('scripts/generate_all_30ml_labels.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated generate_all_30ml_labels.py successfully")
else:
    print("Target not found")

