import os
import glob
import re
import sys

scripts_dir = os.path.dirname(os.path.abspath(__file__))
if scripts_dir not in sys.path:
    sys.path.insert(0, scripts_dir)

from generate_all_30ml_labels import PRODUCTS
from generate_all_100ml_labels_110x75 import render_100ml_label_html, hex_to_rgb

labels_dir = r"c:\Users\master\monsmecta_landing\public\assets\labels"

# =========================================================================
# 1. monsmecta_*_white_label.html 생성 (110x75mm, 100ml 규격 단독 화이트 뒷면 파일)
# =========================================================================
for p in PRODUCTS:
    html_content = render_100ml_label_html(p)
    # 초기 로드 시 white 모드가 기본으로 뜨도록 변경
    white_html = html_content.replace(
        '<body class="mode-compare print-white">',
        '<body class="mode-white print-white">'
    ).replace(
        "const initialMode = urlParams.get('mode') || 'compare';",
        "const initialMode = urlParams.get('mode') || 'white';"
    )
    
    # 단독 화이트 라벨 파일명: monsmecta_{key}_white_label.html
    key = p["id"]
    if key == "monsmecta":
        white_filename = "monsmecta_original_white_label.html"
    elif key == "urinary":
        white_filename = "monsmecta_renal_white_label.html"
    else:
        white_filename = f"monsmecta_{key}_white_label.html"
        
    white_target_path = os.path.join(labels_dir, white_filename)
    with open(white_target_path, "w", encoding="utf-8") as f:
        f.write(white_html)
    print(f"Created standalone white label: {white_filename}")

print("\n[PART 1 DONE] 11 monsmecta_*_white_label.html files generated.")

# =========================================================================
# 2. *_label_print_white.html 생성 (인쇄용 라벨 11종의 화이트 뒷면 버전)
# =========================================================================
print_files = glob.glob(os.path.join(labels_dir, "*_label_print.html"))

for fpath in print_files:
    # 25ml 레거시는 건너뜀
    if "25ml" in fpath:
        continue

    fname = os.path.basename(fpath)
    white_fname = fname.replace("_label_print.html", "_label_print_white.html")
    white_fpath = os.path.join(labels_dir, white_fname)

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # 타이틀 변경
    content = content.replace("High-Tech Label", "High-Tech Label (White Back Edition)")

    # 우측 뒷면 패널을 화이트 배경 + 블랙 텍스트로 변환
    # 1) glass-panel 교체
    content = content.replace(
        'class="glass-panel p-8 rounded-3xl h-full flex flex-col justify-between relative z-10"',
        'class="bg-white text-slate-900 border border-slate-300 p-8 rounded-3xl h-full flex flex-col justify-between relative z-10 shadow-2xl"'
    )

    # 2) 우측 컬럼 내부의 텍스트 색상 및 보더 변환
    # 성분등록번호 & 상표출원
    content = content.replace(
        '<div class="text-[22px] font-bold text-white">제XX9UY0145호</div>',
        '<div class="text-[22px] font-extrabold text-slate-900">제XX9UY0145호</div>'
    )
    content = content.replace(
        '<div class="text-[14px] text-amber-300 font-bold mt-1">U.S. TM App: 50/041,096</div>',
        '<div class="text-[14px] text-amber-600 font-bold mt-1">U.S. TM App: 50/041,096</div>'
    )
    content = content.replace(
        '<div class="text-[16px] text-gray-400 mb-1">사료의 종류 및 명칭 / 형태 / 용도</div>',
        '<div class="text-[16px] text-slate-500 mb-1 font-semibold">사료의 종류 및 명칭 / 형태 / 용도</div>'
    )
    content = content.replace(
        '<div class="text-[22px] font-bold text-white">보조사료 / 미생물제 / 바실러스 서브틸리스 / 액상 / 반려동물용</div>',
        '<div class="text-[22px] font-bold text-slate-900">보조사료 / 미생물제 / 바실러스 서브틸리스 / 액상 / 반려동물용</div>'
    )
    content = content.replace('border-b border-white/20 pb-4', 'border-b border-slate-200 pb-4')

    # 등록성분량
    content = content.replace(
        '<div class="text-[18px] font-medium text-white">바실러스 서브틸리스',
        '<div class="text-[18px] font-semibold text-slate-800">바실러스 서브틸리스'
    )

    # 사용한 원료의 명칭
    content = content.replace('text-[18px] text-gray-300 leading-relaxed font-medium', 'text-[18px] text-slate-700 leading-relaxed font-medium')

    # 대상축종
    content = content.replace('<div class="text-[20px] font-bold text-white">반려견 · 반려묘</div>', '<div class="text-[20px] font-bold text-slate-900">반려견 · 반려묘</div>')

    # 용법 및 용량
    content = re.sub(
        r'<div class="bg-\[[^\]]+\]/10 border border-\[[^\]]+\]/30 p-6 rounded-2xl">',
        '<div class="bg-slate-100 border border-slate-300 p-6 rounded-2xl">',
        content
    )
    content = re.sub(
        r'<div class="text-\[26px\] font-bold text-white">(.*?)<span class="text-\[16px\] text-gray-400 font-normal ml-2">(.*?)</span></div>',
        r'<div class="text-[26px] font-bold text-slate-900">\1<span class="text-[16px] text-slate-500 font-medium ml-2">\2</span></div>',
        content
    )

    # 주의사항 박스
    content = content.replace('bg-black/40 border border-red-500/30 p-5 rounded-2xl mb-4', 'bg-rose-50 border border-red-300 p-5 rounded-2xl mb-4')
    content = content.replace('text-gray-300 text-[18px] font-medium leading-relaxed', 'text-slate-700 text-[18px] font-medium leading-relaxed')
    content = content.replace('<strong class="text-white">건조하고 서늘한 곳에 보관</strong>', '<strong class="text-slate-900">건조하고 서늘한 곳에 보관</strong>')

    # 제조일자 / 유통기한
    content = content.replace('border-t border-white/20 pt-4 font-bold', 'border-t border-slate-200 pt-4 font-bold text-slate-900')
    content = content.replace('text-gray-400">별도표기', 'text-slate-600">별도표기')
    content = content.replace('text-gray-300">제조일로부터 18개월', 'text-slate-600">제조일로부터 18개월')

    # 풋터
    content = re.sub(
        r'border-t border-\[[^\]]+\]/50 pt-4 flex items-center justify-between text-\[16px\] text-gray-300 w-full',
        'border-t border-slate-300 pt-4 flex items-center justify-between text-[16px] text-slate-600 w-full',
        content
    )
    content = content.replace('w-[1px] h-20 bg-white/20 mx-2', 'w-[1px] h-20 bg-slate-300 mx-2')
    content = content.replace('font-bold text-white text-[19px] mb-1', 'font-bold text-slate-900 text-[19px] mb-1')
    content = content.replace('class="text-gray-400"', 'class="text-slate-500"')
    content = content.replace('class="font-bold"', 'class="font-bold text-slate-900"')

    # 재활용 마크
    content = content.replace('<span class="text-[14px] font-bold tracking-tighter text-white">플라스틱</span>', '<span class="text-[14px] font-bold tracking-tighter text-slate-900">플라스틱</span>')
    content = content.replace('<span class="text-[14px] font-black tracking-widest text-white">OTHER</span>', '<span class="text-[14px] font-black tracking-widest text-slate-900">OTHER</span>')

    # 파일 쓰기
    with open(white_fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created print white label: {white_fname}")

print("\n[PART 2 DONE] 11 *_label_print_white.html files generated.")

# =========================================================================
# 3. 기존 *_label_print.html 파일에 상단 "다크 / 화이트 토글 바" 추가
# =========================================================================
toggle_toolbar_html = """
    <!-- 상단 다크 / 화이트 뷰 모드 토글 바 -->
    <div class="fixed top-3 left-1/2 -translate-x-1/2 z-50 flex items-center gap-2 bg-slate-900/90 border border-white/20 px-4 py-2 rounded-full shadow-2xl backdrop-blur-md">
        <a href="{self_dark}" class="px-3 py-1 rounded-full text-xs font-bold transition-all {active_dark_class}">
            🌙 올 다크 인쇄
        </a>
        <a href="{self_white}" class="px-3 py-1 rounded-full text-xs font-bold transition-all {active_white_class}">
            ☀️ 화이트 뒷면 인쇄 (권장)
        </a>
    </div>
"""

for fpath in print_files:
    if "25ml" in fpath or "_white.html" in fpath:
        continue
    fname = os.path.basename(fpath)
    white_fname = fname.replace("_label_print.html", "_label_print_white.html")

    # Dark 파일 툴바 추가
    with open(fpath, "r", encoding="utf-8") as f:
        c = f.read()

    tb_dark = toggle_toolbar_html.format(
        self_dark=fname,
        self_white=white_fname,
        active_dark_class="bg-white text-slate-900 shadow",
        active_white_class="text-slate-300 hover:text-white"
    )
    if 'id="google_translate_element"' in c and '<!-- 상단 다크 / 화이트 뷰 모드 토글 바 -->' not in c:
        c = c.replace(
            '<div id="google_translate_element"',
            tb_dark + '\n    <div id="google_translate_element"'
        )
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(c)

    # White 파일 툴바 추가
    white_fpath = os.path.join(labels_dir, white_fname)
    if os.path.exists(white_fpath):
        with open(white_fpath, "r", encoding="utf-8") as f:
            wc = f.read()
        tb_white = toggle_toolbar_html.format(
            self_dark=fname,
            self_white=white_fname,
            active_dark_class="text-slate-300 hover:text-white",
            active_white_class="bg-emerald-500 text-white shadow font-extrabold"
        )
        if 'id="google_translate_element"' in wc and '<!-- 상단 다크 / 화이트 뷰 모드 토글 바 -->' not in wc:
            wc = wc.replace(
                '<div id="google_translate_element"',
                tb_white + '\n    <div id="google_translate_element"'
            )
            with open(white_fpath, "w", encoding="utf-8") as f:
                f.write(wc)

print("\n[PART 3 DONE] Interactive toggle toolbars linked to all print labels.")
print("\n[ALL COMPLETE] ALL WHITE-BACK LABEL ARTIFACTS CREATED!")
