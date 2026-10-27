import re

files_en = [
    'public/assets/monsmecta_orange_label_en.html',
    'public/assets/monsmecta_teal_label_en.html',
    'public/assets/monsmecta_blue_label_en.html',
    'public/assets/monsmecta_amber_label_en.html'
]

files_ko = [
    'public/assets/monsmecta_orange_label.html',
    'public/assets/monsmecta_teal_label.html',
    'public/assets/monsmecta_blue_label.html',
    'public/assets/monsmecta_amber_label.html'
]

tm_span = '<span class="text-3xl font-extrabold text-orange-400 align-super ml-1">™</span>'

for fpath in files_en:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if tm_span not in content:
        content = re.sub(
            r'<h1 class="text-6xl font-black text-white tracking-tight leading-none mb-2 text-center">MONSMECTA</h1>',
            r'<h1 class="text-6xl font-black text-white tracking-tight leading-none mb-2 text-center">MONSMECTA' + tm_span + r'</h1>',
            content
        )
    
    if '50/041,096' not in content:
        content = content.replace(
            '&bull; Patent No. 201180042602.8</div>',
            '&bull; Patent No. 201180042602.8<br>&bull; U.S. Trademark App. No. 50/041,096</div>'
        )
        content = content.replace(
            '<span class="text-white/70 font-bold">No. XX9UY0145</span>\n                                </div>\n                            </div>',
            '<span class="text-white/70 font-bold">No. XX9UY0145</span>\n                                </div>\n                                <div class="flex justify-between items-center text-[11px] text-emerald-300 mt-1">\n                                    <span>U.S. Trademark App. No.</span>\n                                    <span class="font-mono font-bold text-orange-300">50/041,096</span>\n                                </div>\n                            </div>'
        )
        # Footer
        content = content.replace(
            '<div class="text-center bg-white/10 p-2 rounded-lg ml-auto',
            '<div class="flex flex-col items-end gap-1.5 ml-auto">\n                    <div class="text-[10px] text-emerald-200/90 bg-emerald-950/60 border border-emerald-500/40 rounded px-2.5 py-1 whitespace-nowrap">\n                        <span class="text-orange-400 font-bold">U.S. Trademark</span> App. No. <strong class="text-white font-mono">50/041,096</strong>\n                    </div>\n                    <div class="text-center bg-white/10 p-2 rounded-lg'
        )
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated {fpath}')

for fpath in files_ko:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if tm_span not in content:
        content = re.sub(
            r'<h1 class="text-6xl font-black text-white tracking-tight leading-none mb-2 text-center">몬스멕타</h1>',
            r'<h1 class="text-6xl font-black text-white tracking-tight leading-none mb-2 text-center">몬스멕타' + tm_span + r'</h1>',
            content
        )
        content = re.sub(
            r'<h2 class="text-2xl font-bold montserrat [^"]* tracking-\[0\.2em\] mb-10 text-center">MONSMECTA</h2>',
            r'<h2 class="text-2xl font-bold montserrat text-green-200/80 tracking-[0.2em] mb-10 text-center">MONSMECTA™</h2>',
            content
        )
    if '50/041,096' not in content:
        content = content.replace(
            '&bull; Patent No. 201180042602.8</div>',
            '&bull; Patent No. 201180042602.8<br>&bull; 미국 상표 출원번호: 50/041,096 (U.S. App No.)</div>'
        )
        content = content.replace(
            '<span class="text-white/70 font-bold">제XX9UY0145호</span>\n                                </div>\n                            </div>',
            '<span class="text-white/70 font-bold">제XX9UY0145호</span>\n                                </div>\n                                <div class="flex justify-between items-center text-[11px] text-green-300 mt-1">\n                                    <span>미국 상표 출원번호 (U.S. TM App)</span>\n                                    <span class="font-mono font-bold text-orange-300">50/041,096</span>\n                                </div>\n                            </div>'
        )
        content = content.replace(
            '<div class="text-center bg-white/10 p-2 rounded-lg ml-auto',
            '<div class="flex flex-col items-end gap-1.5 ml-auto">\n                    <div class="text-[10px] text-green-200/90 bg-green-950/60 border border-green-500/40 rounded px-2.5 py-1 whitespace-nowrap">\n                        <span class="text-orange-400 font-bold">미국 상표 출원:</span> App No. <strong class="text-white font-mono">50/041,096</strong>\n                    </div>\n                    <div class="text-center bg-white/10 p-2 rounded-lg'
        )
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated {fpath}')
