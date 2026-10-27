import glob

print_files = glob.glob('public/assets/labels/*_label_print.html')
for fpath in print_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    if '50/041,096' not in c:
        target = '<div class="text-[22px] font-bold text-white">제XX9UY0145호</div>'
        replacement = '<div class="text-[22px] font-bold text-white">제XX9UY0145호</div>\n                                    <div class="text-[14px] text-amber-300 font-bold mt-1">U.S. TM App: 50/041,096</div>'
        c = c.replace(target, replacement)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f'Updated {fpath}')
