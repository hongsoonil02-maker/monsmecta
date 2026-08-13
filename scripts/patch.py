import os

# 1. Read current generate_hitech_labels.py
file_path = r"c:\Users\master\monsmecta-landing\scripts\generate_hitech_labels.py"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 2. Extract the part before `template = """...`
# We'll split by `template = """<!DOCTYPE html>`
parts = content.split('template = """<!DOCTYPE html>')
prefix = parts[0]

# 3. Create a new elegant template based on label_preview.html styling but with the updated layout
new_template = """template = \"\"\"<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=1250">
    <title>{name_en} Label Design</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&family=Montserrat:wght@700;800;900&family=Orbitron:wght@700;900&display=swap" rel="stylesheet">
    <style>
        * {{ word-break: keep-all; overflow-wrap: break-word; }}
        body {{ font-family: 'Noto Sans KR', sans-serif; }}
        .montserrat {{ font-family: 'Montserrat', sans-serif; }}
        .orbitron {{ font-family: 'Orbitron', sans-serif; }}
        .elegant-gradient {{ background: linear-gradient(135deg, {color1} 30%, {color2} 70%, #0B1515 100%); }}
        @media print {{
            @page {{ size: A4 portrait; margin: 0; }}
            body {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; background: white !important; margin: 0; padding: 0; }}
            #label-container {{ width: 900px !important; zoom: 0.8; transform-origin: top center; margin: 0; border: none !important; box-shadow: none !important; }}
        }}
    </style>
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen p-4">
    <div class="scale-[0.5] origin-center">
        <div id="label-container" class="elegant-gradient text-amber-50 w-[2375px] h-[1125px] shrink-0 rounded-[40px] shadow-2xl overflow-hidden border-[12px] border-[#3A0F0F] relative flex flex-col">
            
            <!-- Top Gold/Amber Accent -->
            <div class="h-6 shrink-0 bg-gradient-to-r from-amber-600 via-yellow-500 to-amber-600 relative z-10"></div>
            
            <div class="px-14 py-16 relative z-10 h-full flex flex-col justify-between">
                
                <!-- Background Texture -->
                <div class="absolute inset-0 opacity-5 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')]"></div>
                
                <div class="relative z-10 flex flex-row gap-16 justify-between h-full">
                    
                    <!-- Left Column (Brand & Key Selling Points) -->
                    <div class="w-[46%] flex flex-col justify-between pr-4 h-full">
                        <!-- Title Area -->
                        <div class="flex flex-col items-center justify-center mt-2">
                            <div class="flex items-center gap-4 mb-6">
                                <!-- Dog Icon -->
                                <svg class="w-10 h-10 fill-teal-400" viewBox="0 0 24 24"><path d="M19.46 8.54c-1.34-1.34-3.32-1.78-5.1-.96L12 8.65 9.64 7.58c-1.78-.82-3.76-.38-5.1.96-1.57 1.57-2.12 3.96-1.3 6 .82 2.05 3.02 3.46 5.22 3.46h6.54c2.2 0 4.4-1.41 5.22-3.46.82-2.04.27-4.43-1.3-6-1.56-1.55-2.05-3.38-2.22-5.08-.09-.85-.85-1.46-1.7-1.46h-1c-.55 0-1 .45-1 1v2.54z"/></svg>
                                
                                <div class="inline-block bg-black/30 border-2 border-teal-500/30 rounded-full px-6 py-2">
                                    <span class="text-[18px] font-bold text-teal-300 tracking-widest uppercase">S&J ADVANCED VET FORMULA</span>
                                </div>
                                
                                <!-- Cat Icon -->
                                <svg class="w-10 h-10 fill-teal-400" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6zm-5-3.5L6.5 11l1.5-1.5L9.5 11l-1.5-1.5zm7 0L14.5 11 16 9.5 17.5 11 16 12.5z"/></svg>
                            </div>
                            
                            <p class="text-[22px] font-semibold text-teal-400 mb-2 tracking-wide text-center">{desc}</p>
                            <h1 class="text-[85px] font-black text-white tracking-tight leading-none mb-3 text-center">{name_ko}</h1>
                            <h2 class="text-[32px] font-bold montserrat text-amber-200/80 tracking-[0.1em] text-center">{name_en}</h2>
                        </div>

                        <!-- Core Effects Box -->
                        <div class="bg-black/30 p-6 rounded-2xl border-2 border-teal-500/30 shadow-inner mt-8">
                            <h3 class="text-[20px] font-bold text-teal-400 mb-3 flex items-center gap-3">
                                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M11.3 1.046A1 1 0 0112 2v5h4a1 1 0 01.82 1.573l-7 10A1 1 0 018 18v-5H4a1 1 0 01-.82-1.573l7-10a1 1 0 011.12-.38z" clip-rule="evenodd"></path></svg>
                                핵심 효능
                            </h3>
                            <ul class="grid grid-cols-2 gap-y-2 gap-x-4 text-[18px] font-bold text-amber-100/90 tracking-tight">
                                {effects_html}
                            </ul>
                            <div class="mt-4 text-right text-[15px] font-medium text-amber-200/70 tracking-normal">* (등의 개선에 도움)</div>
                        </div>

                        <!-- Main Ingredients Data -->
                        <div class="bg-black/20 p-6 rounded-3xl border-2 border-teal-500/20 shadow-inner mt-6 mb-4">
                            <div class="flex justify-between items-end mb-4 border-b-2 border-teal-500/30 pb-2">
                                <h3 class="text-[24px] font-bold text-teal-400">■ 주요 성분량 (본제 1L 기준)</h3>
                            </div>
                            <ul class="space-y-3 text-[20px] font-medium">
                                {ingredients_html}
                            </ul>
                        </div>
                        
                        <!-- Package Unit at Bottom Left -->
                        <div class="flex justify-center border-t-2 border-teal-500/30 pt-4 font-bold text-[18px] mt-auto">
                            <div class="bg-black/40 px-6 py-2 rounded-full border border-teal-500/30">
                                <span class="text-teal-300 text-[20px]">포장단위 :</span> <span class="text-amber-100/90 font-bold ml-2 text-[22px]">30 ml / 병</span>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Vertical Divider (Label Fold Line) -->
                    <div class="border-l-[2px] border-dashed border-teal-500/30 shrink-0 mx-2"></div>
                    
                    <!-- Right Column (Specs & Details) -->
                    <div class="w-[50%] flex flex-col justify-between pl-4 h-full relative">
                        <div class="bg-black/20 text-amber-100/90 border-2 border-teal-500/20 rounded-3xl p-8 shadow-inner flex flex-col h-full">
                            
                            <!-- Box 1: Specs -->
                            <div class="grid grid-cols-3 gap-x-6 border-b-2 border-teal-500/30 pb-4 mb-6">
                                <div>
                                    <span class="font-bold text-teal-300 block mb-1">사료 성분등록번호</span>
                                    <span class="font-medium text-[18px]">제XX9UY0145호</span>
                                </div>
                                <div>
                                    <span class="font-bold text-teal-300 block mb-1">사료의 종류/명칭</span>
                                    <span class="font-medium text-[18px]">보조사료 / 혼합제</span>
                                </div>
                                <div>
                                    <span class="font-bold text-teal-300 block mb-1">형태 및 용도</span>
                                    <span class="font-medium text-[18px]">액상(겔) | 반려견·반려묘</span>
                                </div>
                            </div>

                            <!-- Box 2: 사용한 원료의 명칭 -->
                            <div class="mb-6">
                                <span class="font-bold text-teal-300 block mb-2 text-[18px]">사용한 원료의 명칭</span>
                                <span class="font-medium text-[18px] leading-relaxed block text-amber-100/80">바실러스 서브틸리스, 몬모릴로나이트, 천연 추출물 혼합, 프로피온산나트륨, 포도당, 정제수 등 (제품별 상세 원료는 설명서 참조)</span>
                            </div>

                            <!-- Box 3: 용법 및 용량 -->
                            <div class="bg-teal-900/40 p-5 rounded-2xl border-2 border-teal-500/30 mb-6">
                                <span class="font-black text-teal-300 block mb-1 text-[20px]">용법 및 용량</span>
                                <span class="text-teal-100 font-bold text-[22px]">체중 5kg 당 1일 1회 2ml 급여 <span class="text-[16px] font-medium text-teal-300/80 ml-2">(1 펌프/스포이드 = 약 1ml)</span></span>
                            </div>

                            <!-- Box 4: 주의사항 -->
                            <div class="bg-black/30 p-5 rounded-2xl border-2 border-teal-500/20 mb-auto">
                                <span class="font-bold text-yellow-500 block mb-2 text-[18px]">⚠️ 주의사항</span>
                                <ul class="font-medium text-[16px] space-y-1 list-disc pl-6 text-amber-100/80">
                                    <li>직사광선을 피하여 <strong class="text-white">건조하고 서늘한 곳에 보관</strong>하십시오.</li>
                                    <li>제품 특성 상 가라앉는 성분들이 있어서 <strong class="text-yellow-400 text-[14px]">흔들어서 사용</strong>하십시오.</li>
                                    <li>제품에 대하여 문의하실 경우 제조원 또는 판매원으로 연락하여 주시기 바랍니다.</li>
                                </ul>
                            </div>
                            
                            <!-- Box 5: 유통기한 등 (Bottom) -->
                            <div class="grid grid-cols-2 gap-x-4 border-t-2 border-teal-500/30 pt-4 font-bold text-[18px] mt-6">
                                <div class="text-teal-300">제조일자 <span class="text-amber-100/90 font-normal ml-2">별도표기</span></div>
                                <div class="text-teal-300">유통기한 <span class="text-amber-100/90 font-normal ml-2">제조일로부터 18개월</span></div>
                            </div>
                        </div>
                        
                        <!-- Footer Manufacturer Info at Bottom Right (Moved here) -->
                        <div class="border-t-2 border-white/20 pt-6 mt-6 flex flex-row justify-between items-center text-[18px] text-amber-100/70 shrink-0">
                            <div class="flex flex-col gap-1">
                                <div class="font-bold text-white text-[20px] mb-1">판매원 : 에스앤제이 동물병원</div>
                                <div class="text-amber-200/80">경기도 용인시 처인구 포곡읍 선장1로 98-8</div>
                                <div class="text-amber-200/80"><span class="font-bold text-teal-400">TEL</span> 031-321-6562</div>
                            </div>
                            <div class="w-[2px] h-20 bg-white/20 mx-4"></div>
                            <div class="flex flex-col gap-1">
                                <div class="font-bold text-white text-[20px] mb-1">제조원 : ㈜ 엠오 바이오</div>
                                <div class="text-amber-200/80">경기도 화성시 팔탄면 석포로 74번길 10-25 (공장)</div>
                                <div class="text-amber-200/80"><span class="font-bold text-teal-400">TEL</span> 031-458-1240 / www.mobio.co.kr</div>
                            </div>
                            <div class="text-center bg-white/10 p-3 rounded-2xl border-2 border-teal-500/30 shrink-0 ml-6">
                                <div class="w-10 h-10 border-2 border-teal-300 mx-auto rotate-45 flex items-center justify-center mb-2">
                                    <span class="text-[9px] -rotate-45 font-bold text-teal-300">플라스틱</span>
                                </div>
                                <div class="text-[12px] text-teal-300 font-bold uppercase tracking-wider">OTHER</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>\"\"\"

def get_1ml_amount(amt_str):
    amt_str = amt_str.replace(",", "").strip()
    import re
    match = re.match(r"([\d\.]+)(.*)", amt_str)
    if not match: return amt_str
    num = float(match.group(1))
    unit = match.group(2).strip()
    per_ml = num / 1000
    if per_ml.is_integer():
        formatted_num = f"{int(per_ml):,}"
    else:
        if unit == 'g':
            formatted_num = f"{int(per_ml * 1000):,}"
            unit = 'mg'
        else:
            formatted_num = f"{per_ml:g}"
    orig_num_str = f"{int(num):,}" if num.is_integer() else f"{num:g}"
    return f"{orig_num_str}{unit} / L <span class='text-[16px] text-teal-300/80 ml-2 font-normal'>(1ml당 {formatted_num}{unit})</span>"

for p in products:
    effects_html = "\\n".join([f'<li class="flex items-start gap-1"><span class="text-teal-400 leading-none">·</span> {{e}}</li>'.format(e=e) for e in p['effects']])
    
    ingredients_html = ""
    for ing, amt in p['ingredients']:
        if "CFU" in amt or amt == "적량":
            val = amt
            if "CFU" in amt:
                try:
                    num_part, pow_part = amt.split("x10^")
                    pow_num = int(pow_part.replace(" CFU", ""))
                    val = f"{amt} / L <span class='text-[16px] text-teal-300/80 ml-2 font-normal'>(1ml당 {{num_part}}x10^{{pow_num-3}} CFU)</span>".format(num_part=num_part)
                except:
                    pass
            ingredients_html += f'''
            <li class="flex justify-between items-center border-b border-white/5 pb-1">
                <div class="text-amber-100 font-bold">{{ing}}</div>
                <div class="text-amber-300 orbitron tracking-wide text-right">{{val}}</div>
            </li>'''.format(ing=ing, val=val)
        else:
            ingredients_html += f'''
            <li class="flex justify-between items-center border-b border-white/5 pb-1">
                <div class="text-amber-100 font-bold">{{ing}}</div>
                <div class="text-amber-300 orbitron tracking-wide text-right">{{val}}</div>
            </li>'''.format(ing=ing, val=get_1ml_amount(amt))
            
    ingredients_html += f'''
    <li class="flex justify-between items-center border-b border-white/5 pb-1">
        <div class="text-amber-100/60 font-bold text-[14px]">식물추출물 및 기타 부형제</div>
        <div class="text-amber-300/80 orbitron text-[14px] text-right">적량</div>
    </li>'''
            
    html = new_template.format(
        name_ko=p['name_ko'],
        name_en=p['name_en'],
        desc=p['desc'],
        color1=p['color1'],
        color2=p['color2'],
        effects_html=effects_html,
        ingredients_html=ingredients_html
    )
    
    with open(os.path.join(out_dir, f"{{p['id']}}_label_print.html"), "w", encoding="utf-8") as f:
        f.write(html)
        
print("Successfully regenerated all labels with elegant label_preview.html styling.")
"""

with open(r"c:\Users\master\monsmecta-landing\scripts\update.py", "w", encoding="utf-8") as f:
    f.write(prefix + new_template)

print("Created update.py")
