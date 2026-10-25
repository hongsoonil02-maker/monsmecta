import re

with open('public/assets/labels/monsmecta_renal_label.html', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'src="(data:image/png;base64,[^"]+)"', c)
if m:
    with open('scripts/extracted_logo_b64.txt', 'w', encoding='utf-8') as out:
        out.write(m.group(1))
    print('Logo extracted, len:', len(m.group(1)))
else:
    print('Logo not found')
