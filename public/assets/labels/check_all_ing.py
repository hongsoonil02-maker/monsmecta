import json

with open(r'C:\Users\master\monsmecta_landing\public\assets\labels\all_11_products_data.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

for p in products:
    print('===', p['title'], '===')
    for it in p['ing_items']:
        print(f"  {it['num']}: {it['main']}")

