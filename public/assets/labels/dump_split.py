import json

with open(r'C:\Users\master\monsmecta_landing\public\assets\labels\all_11_products_data.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

with open(r'C:\Users\master\monsmecta_landing\public\assets\labels\dump_split_utf8.txt', 'w', encoding='utf-8') as out:
    for p in products:
        out.write(f"=== {p['file'][:2]} {p['title']} ===\n")
        for it in p['ing_items'][:5]:
            main_txt = it['main']
            if ' - ' in main_txt:
                parts = main_txt.split(' - ')
                name_part = parts[0].strip()
                val_part = " - ".join(parts[1:]).strip()
            else:
                name_part = main_txt.strip()
                val_part = ""
            out.write(f"  {it['num']}. [{name_part}] ---> [{val_part}]\n")
        out.write("\n")

print("Done")
