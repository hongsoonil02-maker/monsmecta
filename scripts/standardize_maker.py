import glob, os

files = glob.glob('public/assets/labels/*.html')
count = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as fl:
        c = fl.read()
    new_c = c
    new_c = new_c.replace('<span class="co-name">엠오바이오</span>', '<span class="co-name">엠오 바이오</span>')
    new_c = new_c.replace('<div class="co-line-main">제조원: 엠오바이오</div>', '<div class="co-line-main">제조원 : 엠오 바이오</div>')
    new_c = new_c.replace('제조원: 엠오바이오', '제조원 : 엠오 바이오')
    new_c = new_c.replace('제조원 : 엠오바이오', '제조원 : 엠오 바이오')
    new_c = new_c.replace('제조원 : ㈜ 엠오 바이오', '제조원 : 엠오 바이오')
    new_c = new_c.replace('제조원: ㈜ 엠오바이오', '제조원 : 엠오 바이오')
    new_c = new_c.replace('제조원: ㈜ 엠오 바이오', '제조원 : 엠오 바이오')
    
    if new_c != c:
        with open(f, 'w', encoding='utf-8') as fl:
            fl.write(new_c)
        count += 1

print(f"Updated {count} label html files.")
