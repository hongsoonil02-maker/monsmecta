import json

with open(r'C:\Users\master\monsmecta_landing\public\assets\labels\all_11_products_data.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

for p in products:
    print(f"=== {p['title']} ===")
    for it in p['ing_items'][:5]:
        main_txt = it['main']
        if ' - ' in main_txt:
            name_part, val_part = main_txt.rsplit(' - ', 1)
        elif '-' in main_txt:
            name_part, val_part = main_txt.rsplit('-', 1)
        else:
            name_part = main_txt
            val_part = ""
        print(f"  [{it['num']}] NAME: {name_part.strip()} | VAL: {val_part.strip()}")

