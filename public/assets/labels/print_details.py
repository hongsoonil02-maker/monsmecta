import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\master\monsmecta_landing\public\assets\labels\all_11_products_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open(r'C:\Users\master\monsmecta_landing\public\assets\labels\details_output.txt', 'w', encoding='utf-8') as out:
    for i, p in enumerate(data):
        out.write(f"[{i+1}] {p['title']} ({p['en']})\n")
        out.write(f"  Tagline: {p['tagline']}\n")
        out.write(f"  Effects ({len(p['effects'])}): {p['effects']}\n")
        out.write(f"  Ing Title: {p['ing_title']} ({len(p['ing_items'])})\n")
        for it in p['ing_items']:
            out.write(f"    - {it['num']}. {it['main']} / {it['sub']}\n")
        out.write(f"  Reg No: {p['reg_no']}\n")
        out.write(f"  Feed Type: {p['feed_type']}\n")
        out.write(f"  Feed Qty: {p['feed_qty']}\n")
        out.write(f"  Feed Mat: {p['feed_mat']}\n")
        out.write(f"  Dose: {p['dose_t']} / {p['dose_s']}\n\n")

print("Saved to details_output.txt")
