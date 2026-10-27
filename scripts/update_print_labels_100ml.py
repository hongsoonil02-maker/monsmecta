import glob
import re
import os

print_files = glob.glob('public/assets/labels/*_label_print.html')

for fpath in print_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    # 1. 30 ml / 병 -> 100 ml / 병
    c = re.sub(r'30\s*ml\s*/\s*병', '100 ml / 병', c)
    c = re.sub(r'30ml\s*/\s*병', '100 ml / 병', c)

    # 2. 110mm x 75mm 비율 (w-[2200px] h-[1500px])
    c = c.replace('w-[2375px] h-[1125px]', 'w-[2200px] h-[1500px]')
    c = c.replace('scale-[0.5]', 'scale-[0.42]')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Updated print label {fpath} -> 100ml / 110x75mm ratio")

print("All print labels updated successfully!")
