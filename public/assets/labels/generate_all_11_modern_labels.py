# -*- coding: utf-8 -*-
"""
11종 전 라인업 모던 라벨 생성기 (v3 - 주요성분량 우측 끝 맞춤 정렬)
- 주요성분량 실제 수치(함량)를 테이블 박스 내 우측 끝 맞춤(Right-Aligned)으로 칼같이 정돈
- 성분명(좌측) + 실제 수치(우측) 1:1 대칭 정렬 구조
- 오리지널은 단독 빅 타이틀, 라인업(02~11)은 2단 입체 타이틀(브랜드+서브명칭+영문캡슐)
- 100ml / 30ml 원클릭 전환 툴바 & URL 파라미터 지원
- 제품별 고유 컬러 & 법정 고시 컨텐츠 1:1 완벽 이식
"""

import os
import json
import base64

base_dir = r"C:\Users\master\monsmecta_landing\public\assets\labels"

# 에스앤제이 로고 base64
logo_path = os.path.join(base_dir, "monsmecta_label_sj_logo.png")
with open(logo_path, "rb") as f:
    sj_logo_b64 = "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")

# 11개 제품 데이터 로드
json_path = os.path.join(base_dir, "all_11_products_data.json")
with open(json_path, "r", encoding="utf-8") as f:
    products = json.load(f)

# 제품별 정밀 색상 팔레트 정의
palette = {
    "01": {
        "deep": "#06402f", "deep_sub": "#032b1f", "bg": "#01140e",
        "primary": "#10b981", "point": "#d8f46a", "accent": "#ffd166",
        "card_bg": "#fff7e8", "ing_bg": "#eefdf5", "sub_bg": "#bff0d6",
        "legal_border": "#ffd166", "legal_head": "#06402f", "legal_head_txt": "#d8f46a",
        "tag": "DEEP EMERALD", "color_name": "에메랄드 딥그린"
    },
    "02": {
        "deep": "#3a1205", "deep_sub": "#260b03", "bg": "#170601",
        "primary": "#ea4c10", "point": "#fb923c", "accent": "#f97316",
        "card_bg": "#fff7ed", "ing_bg": "#ffedd5", "sub_bg": "#fed7aa",
        "legal_border": "#fb923c", "legal_head": "#3a1205", "legal_head_txt": "#fb923c",
        "tag": "DEEP ORANGE", "color_name": "딥 오렌지"
    },
    "03": {
        "deep": "#0b203d", "deep_sub": "#06152a", "bg": "#030a17",
        "primary": "#2563eb", "point": "#60a5fa", "accent": "#3b82f6",
        "card_bg": "#eff6ff", "ing_bg": "#dbeafe", "sub_bg": "#bfdbfe",
        "legal_border": "#60a5fa", "legal_head": "#0b203d", "legal_head_txt": "#60a5fa",
        "tag": "DEEP BLUE", "color_name": "딥 블루"
    },
    "04": {
        "deep": "#2e0a3b", "deep_sub": "#20062a", "bg": "#13031a",
        "primary": "#a855f7", "point": "#c084fc", "accent": "#e879f9",
        "card_bg": "#faf5ff", "ing_bg": "#f3e8ff", "sub_bg": "#e9d5ff",
        "legal_border": "#c084fc", "legal_head": "#2e0a3b", "legal_head_txt": "#c084fc",
        "tag": "ROYAL PURPLE", "color_name": "로열 퍼플"
    },
    "05": {
        "deep": "#042e3b", "deep_sub": "#021f29", "bg": "#011218",
        "primary": "#06b6d4", "point": "#22d3ee", "accent": "#38bdf8",
        "card_bg": "#ecfeff", "ing_bg": "#cffafe", "sub_bg": "#a5f3fc",
        "legal_border": "#22d3ee", "legal_head": "#042e3b", "legal_head_txt": "#22d3ee",
        "tag": "CYAN AQUA", "color_name": "시안 아쿠아"
    },
    "06": {
        "deep": "#3d0d26", "deep_sub": "#2a0719", "bg": "#19030e",
        "primary": "#db2777", "point": "#f472b6", "accent": "#fb7185",
        "card_bg": "#fdf2f8", "ing_bg": "#fce7f3", "sub_bg": "#fbcfe8",
        "legal_border": "#f472b6", "legal_head": "#3d0d26", "legal_head_txt": "#f472b6",
        "tag": "ROSE PINK", "color_name": "로즈 핑크"
    },
    "07": {
        "deep": "#3d090d", "deep_sub": "#290407", "bg": "#1a0204",
        "primary": "#dc2626", "point": "#f87171", "accent": "#fca5a5",
        "card_bg": "#fef2f2", "ing_bg": "#fee2e2", "sub_bg": "#fecaca",
        "legal_border": "#f87171", "legal_head": "#3d090d", "legal_head_txt": "#f87171",
        "tag": "CRIMSON RED", "color_name": "크림슨 레드"
    },
    "08": {
        "deep": "#243306", "deep_sub": "#182303", "bg": "#0e1401",
        "primary": "#65a30d", "point": "#a3e635", "accent": "#bef264",
        "card_bg": "#f7fee7", "ing_bg": "#ecfccb", "sub_bg": "#d9f99d",
        "legal_border": "#a3e635", "legal_head": "#243306", "legal_head_txt": "#a3e635",
        "tag": "OLIVE LIME", "color_name": "올리브 라임"
    },
    "09": {
        "deep": "#3d1c05", "deep_sub": "#2a1202", "bg": "#190901",
        "primary": "#ea580c", "point": "#fb923c", "accent": "#fdba74",
        "card_bg": "#fff7ed", "ing_bg": "#ffedd5", "sub_bg": "#fed7aa",
        "legal_border": "#fb923c", "legal_head": "#3d1c05", "legal_head_txt": "#fb923c",
        "tag": "VIVID ORANGE", "color_name": "비비드 오렌지"
    },
    "10": {
        "deep": "#063319", "deep_sub": "#032110", "bg": "#011309",
        "primary": "#16a34a", "point": "#4ade80", "accent": "#86efac",
        "card_bg": "#f0fdf4", "ing_bg": "#dcfce7", "sub_bg": "#bbf7d0",
        "legal_border": "#4ade80", "legal_head": "#063319", "legal_head_txt": "#4ade80",
        "tag": "VITAL GREEN", "color_name": "바이탈 그린"
    },
    "11": {
        "deep": "#382b04", "deep_sub": "#261c02", "bg": "#171001",
        "primary": "#ca8a04", "point": "#facc15", "accent": "#fde047",
        "card_bg": "#fefce8", "ing_bg": "#fef9c3", "sub_bg": "#fef08a",
        "legal_border": "#facc15", "legal_head": "#382b04", "legal_head_txt": "#facc15",
        "tag": "GOLDEN YELLOW", "color_name": "골든 옐로우"
    }
}

sub_names = {
    "01": "",
    "02": "헤파맥스",
    "03": "레날 디톡스",
    "04": "캔서케어",
    "05": "콜드제로",
    "06": "스킨케어",
    "07": "하트케어",
    "08": "조인트케어",
    "09": "파워에이스",
    "10": "프로바이오틱스",
    "11": "비타플러스"
}

def split_ingredient(main_txt, p_id):
    """성분명과 실제 수치(함량)를 분리"""
    if " - " in main_txt:
        parts = main_txt.split(" - ")
        name_part = parts[0].strip()
        val_part = " - ".join(parts[1:]).strip()
    elif " – " in main_txt:
        parts = main_txt.split(" – ")
        name_part = parts[0].strip()
        val_part = " – ".join(parts[1:]).strip()
    else:
        name_part = main_txt.strip()
        val_part = ""
    
    # 01 오리지널 특수 처리 (깔끔한 테이블 정렬)
    if p_id == "01":
        if "DNJ" in val_part:
            val_part = "특허균주 MORI (DNJ)"
        elif "몬모릴로나이트" in val_part:
            val_part = "몬모릴로나이트"
        elif "Sodium" in val_part:
            val_part = "Sodium acetate / propionate"
        
    return name_part, val_part

def generate_modern_html(prod, p_id):
    c = palette[p_id]
    s_name = sub_names[p_id]
    is_original = (p_id == "01")
    
    # Title 레이아웃 생성
    if is_original:
        title_block = f"""
        <div class="ttl-wrap">
          <h1 class="title-orig">몬스멕타<sup class="tm">™</sup></h1>
          <span class="sub-orig en">MONSMECTA<sup class="tm">™</sup></span>
        </div>"""
    else:
        title_block = f"""
        <div class="ttl-wrap">
          <div class="brand-sub-main">몬스멕타<sup class="tm">™</sup></div>
          <div class="brand-sub-name">{s_name}</div>
          <span class="brand-sub-en en">{prod['en']}<sup class="tm">™</sup></span>
        </div>"""

    # 효능 목록 HTML (최대 4개)
    effects_html_100 = ""
    for eff in prod["effects"][:4]:
        effects_html_100 += f"""<div class="fx-item"><span class="chk">✓</span><span>{eff}</span></div>\n"""
        
    effects_html_30 = ""
    for eff in prod["effects"][:3]:  # 30ml는 3개 압축
        effects_html_30 += f"""<div class="fx-item"><span class="chk">✓</span><span>{eff}</span></div>\n"""

    # 성분 목록 HTML (성분명 좌측 + 실제 수치 우측 끝 맞춤)
    ing_title = prod["ing_title"]
    ing_rows_100 = ""
    ing_rows_30 = ""
    
    for it in prod["ing_items"][:5]:
        num = it["num"]
        main_txt = it["main"]
        sub_txt = it.get("sub", "")
        name_part, val_part = split_ingredient(main_txt, p_id)
        
        # 100ml 행
        if p_id == "01" and num == "5":
            sub_html_100 = """<div class="rn">(곰팡이 독소 제거, 면역 증강 및 장 환경 개선에 도움)</div>"""
        elif p_id == "01" and num == "1":
            sub_html_100 = """<div class="rn">· 특허균주 Bacillus subtilis MORI (Patent No. 201180042602.8)</div>"""
        else:
            sub_html_100 = f"""<div class="rn">{sub_txt}</div>""" if sub_txt and sub_txt != main_txt and is_original else ""
        ing_rows_100 += f"""
        <div class="row">
          <span class="no">{num}</span>
          <div class="rb">
            <div class="rm-row">
              <span class="rm-name">{name_part}</span>
              <span class="rm-val">{val_part}</span>
            </div>
            {sub_html_100}
          </div>
        </div>"""

        # 30ml 행 (우측 끝 맞춤 정렬)
        if p_id == "01" and num == "1":
            sub_html_30 = """<div class="rn">· 특허균주 Bacillus subtilis MORI (Patent No. 201180042602.8)</div>"""
        else:
            sub_html_30 = ""
        ing_rows_30 += f"""
        <div class="row">
          <span class="no">{num}</span>
          <div class="rb">
            <div class="rm-row">
              <span class="rm-name">{name_part}</span>
              <span class="rm-val">{val_part}</span>
            </div>
            {sub_html_30}
          </div>
        </div>"""

    # 주의사항
    warn_items = "".join([f"<div>{w}</div>" for w in prod["warnings"][:3]])

    # 법정 효능
    back_eff_html = ""
    romans = ["I", "II", "III", "IV"]
    for idx, beff in enumerate(prod["back_effects"][:4]):
        rom = romans[idx] if idx < len(romans) else "•"
        back_eff_html += f"""<li style="display:flex;gap:0.4mm;"><b>[{rom}]</b><span>{beff}</span></li>"""

    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{prod['title']} Label (모던 {c['tag']} · 100ml / 30ml)</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;600;700;800;900&family=Outfit:wght@600;700;800;900&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; word-break: keep-all; overflow-wrap: break-word; }}
html, body {{ font-family: 'Pretendard Variable', Pretendard, 'Noto Sans KR', -apple-system, 'Segoe UI', sans-serif; background: {c['bg']}; color: {c['deep']}; }}
.en {{ font-family: 'Outfit', 'Pretendard Variable', sans-serif; }}

/* ---------- 화면 뷰어 / A4 가이드 ---------- */
@media screen {{
  html, body {{ width: 100%; min-height: 100vh; background: {c['bg']}; }}
  body {{ padding: 75px 20px 40px; display: flex; flex-direction: column; align-items: center; }}
  .a4-guide-wrapper {{ background: #fff; padding: 10mm 15mm 15mm; border-radius: 4px; box-shadow: 0 15px 40px rgba(0,0,0,.7); display: flex; flex-direction: column; align-items: center; }}
  body.paper-roll .a4-guide-wrapper {{ background: transparent; padding: 0; box-shadow: none; }}
  body.paper-roll .a4-header-guide, body.paper-roll .a4-cut-instructions, body.paper-roll .crop-line {{ display: none !important; }}
}}
.toolbar {{ position: fixed; top: 12px; left: 50%; transform: translateX(-50%); z-index: 99999; background: rgba(10,18,15,.96); border: 1.5px solid {c['primary']}; padding: 8px 18px; border-radius: 14px; display: flex; align-items: center; gap: 12px; box-shadow: 0 10px 30px rgba(0,0,0,.85); color: #fff; font-size: 12px; font-weight: 700; }}
.toolbar button {{ font-weight: 800; font-size: 11.5px; padding: 5px 12px; border: none; border-radius: 6px; cursor: pointer; color: #fff; transition: all .15s ease; }}
.btn-size {{ background: #1f2937; }}
.btn-size.active {{ background: {c['point']}; color: {c['deep']}; }}
.btn-paper {{ background: #374151; }}
.btn-paper.active {{ background: {c['primary']}; color: #fff; }}
.btn-print {{ background: #ef4444; color: #fff; font-weight: 900; }}

.a4-header-guide {{ text-align: center; margin-bottom: 5mm; width: 100%; }}
.a4-header-guide h2 {{ font-size: 13pt; font-weight: 900; color: {c['deep']}; margin-bottom: 1.5mm; }}
.a4-header-guide p {{ font-size: 8pt; font-weight: 700; color: #475569; margin-bottom: 2.5mm; }}
.ruler-50mm {{ display: flex; align-items: center; justify-content: center; gap: 3mm; font-size: 8pt; color: #1e293b; font-weight: 700; }}
.ruler-bar {{ width: 50mm; height: 5.5mm; border: .35mm solid {c['deep']}; border-top: none; position: relative; }}
.ruler-tick {{ position: absolute; bottom: 0; width: .3mm; background: {c['deep']}; }}
.tick-0 {{ left: 0; height: 5.5mm; }} .tick-1 {{ left: 10mm; height: 3mm; }} .tick-2 {{ left: 20mm; height: 3mm; }}
.tick-3 {{ left: 30mm; height: 3mm; }} .tick-4 {{ left: 40mm; height: 3mm; }} .tick-50 {{ right: 0; height: 5.5mm; }}
.ruler-note {{ font-size: 7.5pt; color: #64748b; }}
.a4-cut-instructions {{ margin-top: 5mm; font-size: 8pt; color: #475569; font-weight: 700; text-align: center; }}

/* 코너 재단선 박스 */
.crop-marks-box {{ position: relative; margin: 0 auto; flex-shrink: 0; }}
.crop-line {{ position: absolute; background: {c['deep']}; z-index: 100; pointer-events: none; }}
.crop-tl-h {{ top: 0; left: -6mm; width: 4.5mm; height: .3mm; }} .crop-tl-v {{ top: -6mm; left: 0; width: .3mm; height: 4.5mm; }}
.crop-tr-h {{ top: 0; right: -6mm; width: 4.5mm; height: .3mm; }} .crop-tr-v {{ top: -6mm; right: 0; width: .3mm; height: 4.5mm; }}
.crop-bl-h {{ bottom: 0; left: -6mm; width: 4.5mm; height: .3mm; }} .crop-bl-v {{ bottom: -6mm; left: 0; width: .3mm; height: 4.5mm; }}
.crop-br-h {{ bottom: 0; right: -6mm; width: 4.5mm; height: .3mm; }} .crop-br-v {{ bottom: -6mm; right: 0; width: .3mm; height: 4.5mm; }}

/* 스티커 공통 */
.sticker {{ display: flex; background: #fff; box-shadow: 0 0 0 .2mm #cbd5e1; position: relative; overflow: hidden; }}
.wing {{ background: #fff; flex-shrink: 0; height: 100%; display: flex; align-items: center; justify-content: center; position: relative; z-index: 20; }}
.wing-l {{ width: 7mm; border-right: .2mm dashed #94a3b8; }}
.wing-r {{ width: 3mm; }}
.wing-txt {{ writing-mode: vertical-rl; color: #94a3b8; font-weight: 800; opacity: .8; white-space: nowrap; user-select: none; }}

.sheet {{ position: relative; flex-shrink: 0; overflow: hidden; color: #fff;
  background:
    radial-gradient(circle at 92% 4%, rgba(255,255,255,.18) 0, transparent 34%),
    radial-gradient(circle at 4% 98%, {c['point']}33 0, transparent 38%),
    linear-gradient(165deg, {c['deep']} 0%, {c['deep_sub']} 52%, {c['bg']} 100%); }}
.blob {{ position: absolute; border-radius: 50%; z-index: 1; pointer-events: none; }}
.blob.b1 {{ width: 14mm; height: 14mm; right: -4mm; top: 9mm; background: rgba(255,255,255,.12); }}
.blob.b2 {{ width: 9mm; height: 9mm; left: -3mm; top: 33mm; background: {c['point']}22; }}
.blob.b3 {{ width: 11mm; height: 11mm; left: 36mm; bottom: 6mm; background: {c['primary']}22; }}
.paw {{ position: absolute; inset: 0; background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='60' height='60' viewBox='0 0 60 60'><g fill='white' fill-opacity='0.045'><ellipse cx='30' cy='38' rx='9' ry='7'/><ellipse cx='17' cy='27' rx='4' ry='5.5'/><ellipse cx='25' cy='20' rx='4' ry='5.5'/><ellipse cx='35' cy='20' rx='4' ry='5.5'/><ellipse cx='43' cy='27' rx='4' ry='5.5'/></g></svg>"); background-size: 10.000mm 10.000mm; z-index: 1; pointer-events: none; }}
.bar-top, .bar-bot {{ position: absolute; left: 0; right: 0; height: 0.80mm; background: linear-gradient(90deg, {c['primary']}, {c['point']}, {c['accent']}); z-index: 2; }}
.bar-top {{ top: 0; }} .bar-bot {{ bottom: 0; }}

/* 중앙 접착여백 */
.gap {{ position: absolute; top: 0; bottom: 0; width: 7mm; background: #fff; z-index: 20;
  border-left: .2mm dashed #94a3b8; border-right: .2mm dashed #94a3b8; display: flex; align-items: center; justify-content: center; }}

/* 공통 요소 */
.badge {{ align-self: center; display: flex; align-items: center; justify-content: center;
  background: #fff; color: {c['deep']}; box-shadow: 0 0.350mm 0 rgba(0,0,0,.35); border-radius: 999px; line-height: 1; font-weight: 900; }}
.badge .t {{ font-weight: 900; }}
.badge .t b {{ color: {c['primary']}; font-weight: 900; }}
.hero {{ display: flex; flex-direction: column; align-items: center; text-align: center; }}
.tag {{ display: inline-block; font-weight: 800; color: {c['deep']}; background: {c['accent']}; border-radius: 999px; letter-spacing: -.01em; box-shadow: 0 0.300mm 0 rgba(0,0,0,.3); }}
.hero-row {{ display: flex; align-items: center; justify-content: center; }}
.pet {{ filter: drop-shadow(0 0.350mm 0 rgba(0,0,0,.3)); }}
.pet-dog {{ transform: rotate(-8deg); }}
.pet-cat {{ transform: rotate(8deg); }}
.ttl-wrap {{ display: flex; flex-direction: column; align-items: center; justify-content: center; flex: 1; min-width: 0; text-align: center; width: 100%; }}

/* 메인 타이틀 */
.title-orig {{ font-weight: 900; line-height: 1; letter-spacing: -.04em; color: #fff; text-shadow: 0.420mm 0.420mm 0 {c['primary']}, 0.700mm 0.700mm 0 rgba(0,0,0,.40); white-space: nowrap; text-align: center; width: 100%; }}
.title-orig sup.tm {{ font-weight: 800; vertical-align: top; margin-left: 0.500mm; text-shadow: 0.300mm 0.300mm 0 {c['primary']}; }}
.sub-orig {{ display: inline-block; font-weight: 800; letter-spacing: .15em; color: {c['deep']}; background: {c['sub_bg']}; border-radius: 999px; line-height: 1.1; text-align: center; }}
.sub-orig sup.tm {{ font-size: 1.200mm; font-weight: 900; vertical-align: top; margin-left: 0.300mm; }}

/* 라인업(02~11) 2단 타이틀 */
.brand-sub-main {{ font-weight: 900; color: #fff; line-height: 1; text-shadow: 0.350mm 0.350mm 0 {c['primary']}, 0.600mm 0.600mm 0 rgba(0,0,0,.40); white-space: nowrap; text-align: center; width: 100%; }}
.brand-sub-main sup.tm {{ font-size: 0.5em; vertical-align: top; margin-left: 0.3mm; text-shadow: 0.25mm 0.25mm 0 {c['primary']}; }}
.brand-sub-name {{ font-weight: 900; color: {c['point']}; line-height: 1.1; text-shadow: 0.300mm 0.300mm 0 rgba(0,0,0,.60); white-space: nowrap; letter-spacing: -0.02em; text-align: center; width: 100%; }}
.brand-sub-en {{ display: inline-block; font-weight: 800; color: {c['deep']}; background: {c['sub_bg']}; border-radius: 999px; line-height: 1.1; white-space: nowrap; letter-spacing: 0.04em; text-align: center; }}
.brand-sub-en sup.tm {{ font-size: 0.6em; vertical-align: top; margin-left: 0.2mm; }}

.fx {{ position: relative; }}
.fx-tab {{ position: absolute; background: {c['point']}; color: {c['deep']}; font-weight: 900; border-radius: 999px; z-index: 3; box-shadow: 0 0.250mm 0 rgba(0,0,0,.3); }}
.fx-card {{ background: {c['card_bg']}; color: {c['deep']}; border-radius: 2.400mm; display: flex; flex-direction: column; box-shadow: 0 0.400mm 0 rgba(0,0,0,.3); }}
.fx-item {{ display: flex; align-items: center; font-weight: 800; line-height: 1.2; white-space: nowrap; }}
.chk {{ border-radius: 50%; background: {c['primary']}; color: #fff; font-weight: 900; display: flex; align-items: center; justify-content: center; line-height: 1; }}

/* 성분 테이블 (우측 끝 맞춤 Flex 시스템) */
.ing {{ background: {c['ing_bg']}; color: {c['deep']}; border-radius: 2.400mm; box-shadow: 0 0.400mm 0 rgba(0,0,0,.3); }}
.ing-h {{ display: flex; align-items: center; justify-content: space-between; border-bottom: 0.180mm dashed {c['point']}88; }}
.ing-h .ti {{ font-weight: 900; }}
.ing-h .ref {{ font-weight: 800; color: #fff; background: {c['primary']}; border-radius: 999px; line-height: 1.1; }}
.row {{ display: flex; align-items: flex-start; }}
.no {{ border-radius: 50%; background: {c['deep']}; color: #fff; font-family: 'Outfit', sans-serif; font-weight: 900; display: flex; align-items: center; justify-content: center; text-align: center; line-height: 1; flex-shrink: 0; }}
.row:nth-child(2) .no {{ background: {c['primary']}; }}
.row:nth-child(3) .no {{ background: #0d9488; }}
.row:nth-child(4) .no {{ background: #7c3aed; }}
.row:nth-child(5) .no {{ background: #ea580c; }}
.row:nth-child(6) .no {{ background: #db2777; }}
.rb {{ flex: 1; min-width: 0; }}
.rm-row {{ display: flex; justify-content: space-between; align-items: baseline; width: 100%; }}
.rm-name {{ font-weight: 800; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; padding-right: 0.600mm; color: {c['deep']}; }}
.rm-val {{ font-weight: 900; text-align: right; white-space: nowrap; flex-shrink: 0; margin-left: auto; color: {c['deep']}; }}
.rn {{ font-weight: 700; color: #2d5a47; }}

.pack {{ align-self: center; background: {c['accent']}; color: {c['deep']}; border-radius: 999px; font-weight: 900; line-height: 1; display: flex; align-items: center; box-shadow: 0 0.350mm 0 rgba(0,0,0,.35); }}
.pack b {{ color: {c['deep']}; font-weight: 900; }}
.pack::before {{ content: ""; width: 2.200mm; height: 2.200mm; background: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 60 60'><g fill='{c['deep'].replace('#', '%23')}'><ellipse cx='30' cy='38' rx='11' ry='9'/><ellipse cx='13' cy='26' rx='5' ry='7'/><ellipse cx='24' cy='16' rx='5' ry='7'/><ellipse cx='36' cy='16' rx='5' ry='7'/><ellipse cx='47' cy='26' rx='5' ry='7'/></g></svg>") center / contain no-repeat; }}

/* 법정 고시란 */
.legal {{ height: 100%; background: #fff; color: #1e293b; border: 0.500mm solid {c['legal_border']}; border-radius: 2.400mm; display: flex; flex-direction: column; justify-content: space-between; }}
.lg-head {{ background: {c['legal_head']}; color: #fff; border-radius: 1.200mm; display: flex; flex-direction: column; }}
.lg-reg {{ display: flex; justify-content: space-between; align-items: baseline; line-height: 1.15; }}
.lg-reg .l {{ font-weight: 800; color: {c['legal_head_txt']}; }}
.lg-reg .v {{ font-weight: 900; letter-spacing: .02em; color: #fff; }}
.lg-tm {{ display: flex; justify-content: space-between; font-weight: 600; color: {c['sub_bg']}; border-top: 0.15mm solid rgba(255,255,255,.15); }}
.lg-tm b {{ color: {c['accent']}; font-weight: 800; }}
.lg-type {{ font-weight: 600; color: #e2e8f0; }}
.lg-type b {{ color: {c['accent']}; font-weight: 800; }}
.lg-body {{ display: flex; flex-direction: column; }}
.ir {{ display: flex; align-items: baseline; border-bottom: 0.150mm dotted #cbd5e1; }}
.ir:last-child {{ border-bottom: none; padding-bottom: 0; }}
.ir .l {{ font-weight: 800; color: {c['deep']}; margin-right: 0.800mm; white-space: nowrap; flex-shrink: 0; }}
.ir .v {{ flex: 1; font-weight: 600; color: #1e293b; }}
.ef {{ list-style: none; display: flex; flex-direction: column; }}
.dose {{ background: #eff6ff; border-radius: 1.200mm; border-left: 0.800mm solid #3b82f6; display: flex; align-items: flex-start; text-align: left; }}
.dose-lbl {{ font-weight: 900; color: #1d4ed8; white-space: nowrap; flex-shrink: 0; }}
.dose-body {{ display: flex; flex-direction: column; text-align: left; }}
.dose-t {{ font-weight: 900; color: #1d4ed8; }}
.dose-t span {{ font-weight: 900; color: #111827; }}
.dose-sub {{ font-weight: 700; color: #4b5563; text-align: left; white-space: nowrap; }}
.warn {{ background: #fff1f2; border-radius: 1.200mm; border: 0.300mm solid #fecdd3; }}
.warn-t {{ font-weight: 900; color: #e11d48; display: flex; align-items: center; gap: 0.600mm; }}
.warn-b {{ font-weight: 600; color: #475569; }}
.meta {{ display: flex; justify-content: space-between; border-top: 0.180mm solid #e2e8f0; font-weight: 700; color: #64748b; }}
.meta b {{ color: #1e293b; font-weight: 800; }}

/* 2열 푸터 레이아웃 */
.lg-foot {{ display: grid; grid-template-columns: 46% 54%; column-gap: 1.0mm; align-items: start; border-top: 0.200mm solid #e2e8f0; }}
.co-t {{ display: flex; align-items: center; justify-content: space-between; font-weight: 900; color: {c['deep']}; line-height: 1; white-space: nowrap; }}
.co-b {{ display: flex; align-items: center; gap: 0.600mm; }}
.sj-foot-logo {{ object-fit: contain; flex-shrink: 0; }}
.co-n {{ font-weight: 900; color: #0f172a; line-height: 1; white-space: nowrap; }}
.co-a, .co-tel {{ color: #475569; font-weight: 600; white-space: nowrap; }}
.co-tel b {{ color: {c['primary']}; font-weight: 800; }}
.rc {{ display: flex; align-items: center; gap: 0.400mm; }}
.rc .w {{ position: relative; display: flex; align-items: center; justify-content: center; }}
.rc svg {{ width: 100%; height: 100%; }}
.rc .x {{ position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; font-weight: 900; color: {c['primary']}; letter-spacing: -.05em; }}
.rc .o {{ font-weight: 900; color: {c['primary']}; line-height: 1; }}

/* ==========================================================================
   SIZE 100ML (118mm × 76mm)
   ========================================================================== */
body.size-100 .crop-marks-box {{ width: 118mm; height: 76mm; }}
body.size-100 .sticker {{ width: 118mm; height: 76mm; }}
body.size-100 .wing-txt {{ font-size: 2.200mm; letter-spacing: 1mm; }}
body.size-100 .sheet {{ width: 108mm; height: 76mm; }}
body.size-100 .gap {{ left: 50.500mm; }}
body.size-100 .col-left, body.size-100 .col-right {{ position: absolute; top: 2.200mm; bottom: 2.200mm; width: 49.500mm; z-index: 5; }}
body.size-100 .col-left {{ left: 1.000mm; padding: 0 0.500mm; display: flex; flex-direction: column; justify-content: space-between; }}
body.size-100 .col-right {{ right: 1.000mm; }}

body.size-100 .fx-card-100 {{ display: flex !important; }}
body.size-100 .fx-card-30 {{ display: none !important; }}
body.size-100 .ing-body-100 {{ display: block !important; }}
body.size-100 .ing-body-30 {{ display: none !important; }}

body.size-100 .badge {{ gap: 1.100mm; padding: 0.850mm 2.800mm; }}
body.size-100 .badge .t {{ font-size: 1.850mm; font-weight: 900; letter-spacing: .04em; }}
body.size-100 .badge svg {{ width: 2.200mm; height: 2.200mm; }}
body.size-100 .tag {{ font-size: 1.900mm; font-weight: 900; padding: 0.700mm 2.500mm; line-height: 1.15; margin-bottom: 0.900mm; }}
body.size-100 .hero-row {{ gap: 1.100mm; }}
body.size-100 .pet {{ width: 8.200mm; height: 8.200mm; flex: 0 0 8.200mm; }}

/* 100ml 오리지널 타이틀 */
body.size-100 .title-orig {{ font-size: 8.600mm; margin-bottom: 0.450mm; font-weight: 900; }}
body.size-100 .title-orig sup.tm {{ font-size: 3.800mm; }}
body.size-100 .sub-orig {{ font-size: 2.200mm; font-weight: 900; padding: 0.500mm 2.000mm 0.500mm calc(2.000mm + .15em); }}

/* 100ml 라인업(02~11) 2단 타이틀 */
body.size-100 .brand-sub-main {{ font-size: 5.800mm; margin-bottom: 0.250mm; font-weight: 900; }}
body.size-100 .brand-sub-name {{ font-size: 4.600mm; margin-bottom: 0.350mm; font-weight: 900; }}
body.size-100 .brand-sub-en {{ font-size: 1.650mm; font-weight: 900; padding: 0.350mm 1.800mm; }}

body.size-100 .fx {{ margin-top: 1.200mm; }}
body.size-100 .fx-tab {{ top: -1.800mm; left: 2.200mm; font-size: 1.780mm; font-weight: 900; padding: 0.500mm 2.000mm; line-height: 1.1; }}
body.size-100 .fx-card {{ padding: 2.300mm 1.800mm 1.600mm; gap: 1.000mm; border-radius: 2.600mm; }}
body.size-100 .fx-item {{ gap: 1.150mm; font-size: 1.900mm; font-weight: 900; line-height: 1.22; }}
body.size-100 .chk {{ width: 2.350mm; height: 2.350mm; font-size: 1.450mm; flex: 0 0 2.350mm; }}

body.size-100 .ing {{ padding: 1.250mm 1.600mm 1.150mm; border-radius: 2.600mm; }}
body.size-100 .ing-h {{ padding-bottom: 0.550mm; margin-bottom: 0.650mm; }}
body.size-100 .ing-h .ti {{ font-size: 1.850mm; font-weight: 900; }}
body.size-100 .ing-h .ref {{ font-size: 1.450mm; font-weight: 900; padding: 0.350mm 1.500mm; }}
body.size-100 .row {{ gap: 0.950mm; margin-bottom: 0.500mm; }}
body.size-100 .no {{ font-family: 'Outfit', sans-serif !important; width: 2.050mm !important; height: 2.050mm !important; min-width: 2.050mm !important; min-height: 2.050mm !important; flex: 0 0 2.050mm !important; border-radius: 50% !important; font-size: 1.350mm !important; font-weight: 900 !important; display: flex !important; align-items: center !important; justify-content: center !important; text-align: center !important; line-height: 1 !important; margin-top: 0.150mm !important; }}
body.size-100 .rm-name {{ font-size: 1.680mm; font-weight: 900; }}
body.size-100 .rm-val {{ font-size: 1.720mm; font-weight: 900; }}
body.size-100 .rn {{ font-size: 1.280mm; font-weight: 700; line-height: 1.20; padding-left: 0.200mm; }}

body.size-100 .pack {{ padding: 0.950mm 3.400mm; font-size: 2.250mm; font-weight: 900; gap: 1.000mm; margin-bottom: 0.400mm; }}
body.size-100 .pack::before {{ width: 2.600mm; height: 2.600mm; }}

body.size-100 .legal {{ padding: 1.000mm 1.200mm; }}
body.size-100 .lg-head {{ padding: 0.800mm 1.200mm; gap: 0.350mm; }}
body.size-100 .lg-reg .l {{ font-size: 1.650mm; }}
body.size-100 .lg-reg .v {{ font-size: 1.950mm; }}
body.size-100 .lg-tm {{ font-size: 1.350mm; padding-top: 0.25mm; margin-top: 0.2mm; line-height: 1.15; }}
body.size-100 .lg-type {{ font-size: 1.400mm; line-height: 1.25; }}
body.size-100 .lg-body {{ gap: 0.250mm; }}
body.size-100 .ir {{ font-size: 1.850mm; line-height: 1.22; padding-bottom: 0.200mm; border-bottom: 0.150mm dotted #cbd5e1; }}
body.size-100 .ir .l {{ font-size: 1.850mm; font-weight: 900; margin-right: 0.600mm; }}
body.size-100 .ir .v {{ font-size: 1.780mm; font-weight: 800; color: #0f172a; }}
body.size-100 .ef {{ gap: 0.180mm; margin-top: 0.180mm; }}
body.size-100 .ef li {{ font-size: 1.750mm; line-height: 1.20; font-weight: 800; color: #1e293b; }}
body.size-100 .dose {{ padding: 0.350mm 0.800mm; gap: 0.350mm; }}
body.size-100 .dose-lbl {{ font-size: 1.850mm; font-weight: 900; color: #1d4ed8; white-space: nowrap; flex-shrink: 0; line-height: 1.22; }}
body.size-100 .dose-body {{ display: flex; flex-direction: column; text-align: left; gap: 0.150mm; }}
body.size-100 .dose-t {{ font-size: 1.750mm; font-weight: 800; display: flex; align-items: baseline; gap: 0.300mm; white-space: nowrap; line-height: 1.20; }}
body.size-100 .dose-t span:first-child {{ font-size: 1.750mm; font-weight: 800; }}
body.size-100 .dose-sub {{ font-size: 1.450mm; font-weight: 700; color: #4b5563; text-align: left; line-height: 1.15; }}
body.size-100 .warn {{ padding: 0.550mm 0.900mm 0.650mm; border-radius: 1.200mm; border: 0.300mm solid #fecdd3; }}
body.size-100 .warn-t {{ font-size: 1.800mm; font-weight: 900; margin-bottom: 0.400mm; }}
body.size-100 .warn-b {{ display: flex; flex-direction: column; gap: 0.350mm; font-size: 1.550mm; line-height: 1.20; font-weight: 700; color: #334155; }}
body.size-100 .warn-b > div {{ margin: 0; padding: 0; padding-left: 1.880mm; text-indent: -1.880mm; }}
body.size-100 .meta {{ padding-top: 0.250mm; font-size: 1.550mm; font-weight: 800; }}

body.size-100 .lg-foot {{ padding-top: 0.800mm; }}
body.size-100 .co-t {{ font-size: 1.500mm; height: 3.200mm; }}
body.size-100 .co-b {{ height: 2.800mm; margin: 0.300mm 0 0.300mm; }}
body.size-100 .sj-foot-logo {{ height: 2.800mm; width: 2.800mm; }}
body.size-100 .co-n {{ font-size: 1.550mm; }}
body.size-100 .co-a, body.size-100 .co-tel {{ font-size: 1.300mm; line-height: 1.25; }}
body.size-100 .rc {{ margin-right: 3.000mm; }}
body.size-100 .rc .w {{ width: 3.200mm; height: 3.200mm; }}
body.size-100 .rc .x {{ font-size: 0.850mm; padding-top: 0.400mm; }}
body.size-100 .rc .o {{ font-size: 1.150mm; }}

/* ==========================================================================
   SIZE 30ML (101mm × 42mm)
   ========================================================================== */
body.size-30 .crop-marks-box {{ width: 101mm; height: 42mm; }}
body.size-30 .sticker {{ width: 101mm; height: 42mm; }}
body.size-30 .wing-txt {{ font-size: 1.800mm; letter-spacing: 0.6mm; }}
body.size-30 .sheet {{ width: 91mm; height: 42mm; }}
body.size-30 .gap {{ left: 39.500mm; }}
body.size-30 .col-left {{ position: absolute; top: 0.900mm; bottom: 0.900mm; left: 0.600mm; width: 38.300mm; z-index: 5; padding: 0 0.200mm; display: flex; flex-direction: column; justify-content: space-between; }}
body.size-30 .col-right {{ position: absolute; top: 1.200mm; bottom: 1.200mm; left: 47.200mm; width: 43.000mm; right: auto; z-index: 5; }}

body.size-30 .fx-card-100 {{ display: none !important; }}
body.size-30 .fx-card-30 {{ display: flex !important; }}
body.size-30 .ing-body-100 {{ display: none !important; }}
body.size-30 .ing-body-30 {{ display: block !important; }}

body.size-30 .badge {{ gap: 0.600mm; padding: 0.420mm 1.800mm; box-shadow: 0 0.250mm 0 rgba(0,0,0,.35); }}
body.size-30 .badge .t {{ font-size: 1.350mm; font-weight: 900 !important; letter-spacing: .02em; -webkit-text-stroke: 0.035mm currentColor; }}
body.size-30 .badge svg {{ width: 1.600mm; height: 1.600mm; }}

body.size-30 .tag {{ font-size: 1.380mm; font-weight: 900 !important; padding: 0.320mm 1.500mm; line-height: 1.1; margin-bottom: 0.200mm; -webkit-text-stroke: 0.03mm currentColor; }}
body.size-30 .hero-row {{ gap: 0.700mm; }}
body.size-30 .pet {{ width: 5.200mm; height: 5.200mm; flex: 0 0 5.200mm; }}

/* 30ml 오리지널 타이틀 */
body.size-30 .title-orig {{ font-size: 6.100mm; margin-bottom: 0.180mm; font-weight: 900 !important; }}
body.size-30 .title-orig sup.tm {{ font-size: 2.400mm; font-weight: 900 !important; }}
body.size-30 .sub-orig {{ font-size: 1.550mm; font-weight: 900 !important; padding: 0.250mm 1.100mm 0.250mm calc(1.100mm + .12em); -webkit-text-stroke: 0.03mm currentColor; }}

/* 30ml 라인업(02~11) 2단 타이틀 */
body.size-30 .brand-sub-main {{ font-size: 4.150mm; font-weight: 900 !important; }}
body.size-30 .brand-sub-name {{ font-size: 3.200mm; margin-top: 0.100mm; font-weight: 900 !important; }}
body.size-30 .brand-sub-en {{ font-size: 1.200mm; font-weight: 900 !important; padding: 0.200mm 1.000mm; margin-top: 0.120mm; -webkit-text-stroke: 0.03mm currentColor; }}

body.size-30 .fx {{ margin-top: 0.400mm; }}
body.size-30 .fx-tab {{ top: -1.250mm; left: 1.500mm; font-size: 1.220mm; font-weight: 900 !important; padding: 0.250mm 1.200mm; -webkit-text-stroke: 0.03mm currentColor; }}
body.size-30 .fx-card {{ padding: 1.200mm 1.050mm 0.750mm; gap: 0.350mm; border-radius: 1.600mm; }}
body.size-30 .fx-item {{ gap: 0.700mm; font-size: 1.380mm; font-weight: 900 !important; line-height: 1.15; -webkit-text-stroke: 0.035mm currentColor; }}
body.size-30 .chk {{ width: 1.600mm; height: 1.600mm; font-size: 1.000mm; font-weight: 900 !important; flex: 0 0 1.600mm; }}

/* 30ml 성분 박스 (우측 끝 맞춤) */
body.size-30 .ing {{ padding: 0.550mm 0.850mm 0.450mm; border-radius: 1.600mm; }}
body.size-30 .ing-h {{ padding-bottom: 0.200mm; margin-bottom: 0.220mm; }}
body.size-30 .ing-h .ti {{ font-size: 1.280mm; font-weight: 900 !important; -webkit-text-stroke: 0.03mm currentColor; }}
body.size-30 .ing-h .ref {{ font-size: 1.000mm; font-weight: 900 !important; padding: 0.180mm 0.850mm; -webkit-text-stroke: 0.025mm currentColor; }}
body.size-30 .row {{ gap: 0.550mm; margin-bottom: 0.120mm; line-height: 1.12; }}
body.size-30 .no {{ font-family: 'Outfit', sans-serif !important; width: 1.550mm !important; height: 1.550mm !important; min-width: 1.550mm !important; min-height: 1.550mm !important; flex: 0 0 1.550mm !important; border-radius: 50% !important; font-size: 0.950mm !important; font-weight: 900 !important; display: flex !important; align-items: center !important; justify-content: center !important; text-align: center !important; line-height: 1 !important; margin-top: 0.080mm !important; }}
body.size-30 .rm-name {{ font-size: 1.150mm; font-weight: 900 !important; letter-spacing: -0.035em; -webkit-text-stroke: 0.035mm currentColor; }}
body.size-30 .rm-val {{ font-size: 1.180mm; font-weight: 900 !important; letter-spacing: -0.02em; -webkit-text-stroke: 0.035mm currentColor; }}
body.size-30 .rn {{
  display: block;
  font-size: 0.880mm;
  font-weight: 900 !important;
  color: {c['deep']};
  line-height: 1.15;
  letter-spacing: -0.04em;
  white-space: nowrap;
  margin-top: 0.080mm;
  -webkit-text-stroke: 0.025mm currentColor;
}}

body.size-30 .pack {{ padding: 0.500mm 2.200mm; font-size: 1.550mm; font-weight: 900 !important; gap: 0.650mm; margin-bottom: 0.100mm; -webkit-text-stroke: 0.035mm currentColor; }}
body.size-30 .pack::before {{ width: 1.800mm; height: 1.800mm; }}

body.size-30 .legal {{ padding: 0.500mm 0.700mm; border-radius: 1.800mm; }}
body.size-30 .lg-head {{ padding: 0.450mm 0.700mm; gap: 0.150mm; border-radius: 1.000mm; }}
body.size-30 .lg-reg .l {{ font-size: 1.080mm; }}
body.size-30 .lg-reg .v {{ font-size: 1.250mm; }}
body.size-30 .lg-tm {{ font-size: 0.920mm; padding-top: 0.10mm; margin-top: 0.08mm; }}
body.size-30 .lg-type {{ font-size: 0.950mm; display: none; }}
body.size-30 .lg-body {{ gap: 0.100mm; }}
body.size-30 .ir {{ font-size: 1.280mm; line-height: 1.12; padding-bottom: 0.060mm; border-bottom: 0.100mm dotted #cbd5e1; }}
body.size-30 .ir .l {{ font-size: 1.280mm; font-weight: 900; margin-right: 0.350mm; }}
body.size-30 .ir .v {{ font-size: 1.250mm; font-weight: 800; color: #0f172a; }}
body.size-30 .ef {{ gap: 0.020mm; }}
body.size-30 .ef li {{ font-size: 1.240mm; line-height: 1.10; font-weight: 800; color: #1e293b; }}
body.size-30 .dose {{ padding: 0.250mm 0.500mm; gap: 0.350mm; overflow: hidden; }}
body.size-30 .dose-lbl {{ font-size: 1.280mm; font-weight: 900; color: #1d4ed8; white-space: nowrap; flex-shrink: 0; line-height: 1.22; margin-right: 0.150mm; }}
body.size-30 .dose-body {{ display: flex; flex-direction: column; text-align: left; min-width: 0; gap: 0.350mm; }}
body.size-30 .dose-t {{ font-size: 1.240mm; font-weight: 800; display: flex; align-items: baseline; gap: 0.150mm; white-space: nowrap; line-height: 1.20; }}
body.size-30 .dose-t span:first-child {{ font-size: 1.240mm; font-weight: 800; }}
body.size-30 .dose-sub {{ font-size: 1.050mm; font-weight: 700; color: #4b5563; text-align: left; line-height: 1.20; }}
body.size-30 .warn {{ padding: 0.250mm 0.500mm 0.300mm; border-radius: 0.800mm; border: 0.200mm solid #fecdd3; }}
body.size-30 .warn-t {{ font-size: 1.160mm; font-weight: 900; margin-bottom: 0.250mm; }}
body.size-30 .warn-b {{ display: flex; flex-direction: column; gap: 0.220mm; font-size: 1.050mm; line-height: 1.12; font-weight: 700; color: #334155; }}
body.size-30 .warn-b > div {{ margin: 0; padding: 0; }}
body.size-30 .meta {{ padding-top: 0.120mm; font-size: 1.050mm; font-weight: 800; }}

body.size-30 .lg-foot {{ grid-template-columns: 46% 54%; column-gap: 0.800mm; border-top: 0.150mm solid #e2e8f0; padding-top: 0.300mm; }}
body.size-30 .co-t {{ font-size: 0.850mm; height: 1.700mm; }}
body.size-30 .co-b {{ height: 1.500mm; margin: 0.080mm 0; gap: 0.400mm; }}
body.size-30 .sj-foot-logo {{ height: 1.500mm; width: 1.500mm; display: block !important; }}
body.size-30 .co-n {{ font-size: 0.880mm; }}
body.size-30 .co-a {{ font-size: 0.700mm; line-height: 1.10; color: #64748b; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; display: block !important; }}
body.size-30 .co-tel {{ font-size: 0.740mm; line-height: 1.12; color: #475569; font-weight: 600; white-space: nowrap; display: block !important; }}
body.size-30 .rc {{ gap: 0.300mm; margin-right: 1.800mm; }}
body.size-30 .rc .w {{ width: 1.700mm; height: 1.700mm; }}
body.size-30 .rc .x {{ font-size: 0.500mm; padding-top: 0.200mm; }}
body.size-30 .rc .o {{ font-size: 0.700mm; }}

/* 인쇄 스타일 */
@media print {{
  html, body {{ background: #fff !important; padding: 0 !important; margin: 0 !important; }}
  .toolbar {{ display: none !important; }}
  body.paper-roll .a4-guide-wrapper {{ padding: 0 !important; }}
  body.paper-roll .a4-header-guide, body.paper-roll .a4-cut-instructions, body.paper-roll .crop-line {{ display: none !important; }}
  body.paper-roll .crop-marks-box {{ margin: 0 !important; }}
  body.paper-roll .sticker {{ box-shadow: none !important; }}
  body.paper-a4 .a4-guide-wrapper {{ box-shadow: none !important; padding: 10mm 0 !important; }}
}}
</style>
</head>
<body class="size-100 paper-a4">

<!-- 상단 툴바 -->
<div class="toolbar no-print">
  <span style="color:{c['point']};">🐾 {prod['title']} 모던 라벨</span>
  <div style="display:flex;align-items:center;background:#111827;padding:4px 12px;border-radius:8px;font-size:11px;font-weight:900;color:{c['point']};">
    📦 100ml 표준 정품 규격 (118×76mm)
  </div>
  <div style="display:flex;gap:4px;background:#111827;padding:3px;border-radius:8px;">
    <button id="btn-a4" class="btn-paper active" onclick="setPaper('a4')">A4 실측</button>
    <button id="btn-roll" class="btn-paper" onclick="setPaper('roll')">롤 라벨</button>
  </div>
  <button class="btn-print" onclick="window.print()">🖨️ 인쇄하기</button>
</div>

<!-- A4 가이드 래퍼 -->
<div class="a4-guide-wrapper">
  
  <div class="a4-header-guide">
    <h2>[{prod['title']} 정품 규격] 용기 라벨 [실물 테스트형] <span id="guide-dims">(좌 7 + 중 7 + 우 3 = 총 118×76mm)</span></h2>
    <p>※ 인쇄 설정 시 반드시 [배율: 맞춤(100%)] 또는 [실제 크기(Actual Size)]로 지정하십시오.</p>
    <div class="ruler-50mm">
      <span>실측 확인용 눈금자:</span>
      <div class="ruler-bar">
        <div class="ruler-tick tick-0"></div><div class="ruler-tick tick-1"></div>
        <div class="ruler-tick tick-2"></div><div class="ruler-tick tick-3"></div>
        <div class="ruler-tick tick-4"></div><div class="ruler-tick tick-50"></div>
        <span style="position:absolute;bottom:0.5mm;left:1mm;font-size:6.5pt;">0</span>
        <span style="position:absolute;bottom:0.5mm;right:1mm;font-size:6.5pt;">50mm</span>
      </div>
      <span class="ruler-note">(자로 쟀을 때 정확히 5cm)</span>
    </div>
  </div>

  <!-- 코너 재단선 박스 -->
  <div class="crop-marks-box">
    <div class="crop-line crop-tl-h"></div><div class="crop-line crop-tl-v"></div>
    <div class="crop-line crop-tr-h"></div><div class="crop-line crop-tr-v"></div>
    <div class="crop-line crop-bl-h"></div><div class="crop-line crop-bl-v"></div>
    <div class="crop-line crop-br-h"></div><div class="crop-line crop-br-v"></div>

    <!-- 스티커 본체 -->
    <div class="sticker">
      <!-- 좌측 7mm 접착 여백 -->
      <div class="wing wing-l"><span class="wing-txt">접착 7mm</span></div>

      <!-- 시트 본체 -->
      <div class="sheet">
        <div class="paw"></div>
        <div class="blob b1"></div><div class="blob b2"></div><div class="blob b3"></div>
        <div class="bar-top"></div><div class="bar-bot"></div>

        <!-- 전면 영역 -->
        <div class="col-left">
          <!-- 1) 브랜드 배지 -->
          <div class="badge">
            <svg viewBox="0 0 24 24" fill="{c['deep']}"><ellipse cx="12" cy="16.2" rx="5.2" ry="4.4"/><ellipse cx="4.8" cy="10.6" rx="2.2" ry="2.9"/><ellipse cx="9.2" cy="5.6" rx="2.2" ry="3"/><ellipse cx="14.8" cy="5.6" rx="2.2" ry="3"/><ellipse cx="19.2" cy="10.6" rx="2.2" ry="2.9"/></svg>
            <span class="t">🐾 <b>S&amp;J</b> ADVANCED VET FORMULA 🐾</span>
          </div>

          <!-- 2) 히어로 -->
          <div class="hero">
            <span class="tag">{prod['tagline']}</span>
            <div class="hero-row">
              <svg class="pet pet-dog" viewBox="0 0 44 44">
                <circle cx="22" cy="22" r="20" fill="#fff" stroke="{c['deep']}" stroke-width="2"/>
                <circle cx="22" cy="24" r="14.5" fill="#ffe0b8"/>
                <circle cx="16.5" cy="22" r="1.9" fill="{c['deep']}"/>
                <circle cx="27.5" cy="22" r="1.9" fill="{c['deep']}"/>
                <ellipse cx="22" cy="27" rx="2.3" ry="1.6" fill="{c['deep']}"/>
                <path d="M9 11C2 11 0 26 6 32c3.5.5 5.5-6 5-13.5z" fill="#e9a869"/>
                <path d="M35 11c7 0 9 15 3 21-3.5.5-5.5-6-5-13.5z" fill="#e9a869"/>
                <circle cx="14" cy="27" r="2" fill="#ffb4a2"/>
                <circle cx="30" cy="27" r="2" fill="#ffb4a2"/>
              </svg>
              {title_block}
              <svg class="pet pet-cat" viewBox="0 0 44 44">
                <circle cx="22" cy="22" r="20" fill="#fff" stroke="{c['deep']}" stroke-width="2"/>
                <ellipse cx="22" cy="25" rx="14.5" ry="12.5" fill="#fff"/>
                <path d="M10 20L11 5 21 13z" fill="#fff" stroke="{c['deep']}" stroke-width="1.2"/>
                <path d="M34 20L33 5 23 13z" fill="#fff" stroke="{c['deep']}" stroke-width="1.2"/>
                <circle cx="16" cy="23" r="1.8" fill="{c['deep']}"/>
                <circle cx="28" cy="23" r="1.8" fill="{c['deep']}"/>
                <polygon points="22,26 20,28 24,28" fill="#ff8fa3"/>
                <circle cx="13" cy="26" r="2" fill="#ffb4a2"/>
                <circle cx="31" cy="26" r="2" fill="#ffb4a2"/>
              </svg>
            </div>
          </div>

          <!-- 3) 핵심 효능 카드 -->
          <div class="fx">
            <span class="fx-tab">핵심 효능</span>
            <div class="fx-card fx-card-100">{effects_html_100}</div>
            <div class="fx-card fx-card-30" style="display:none;">{effects_html_30}</div>
          </div>

          <!-- 4) 성분 복합체 카드 (우측 끝 맞춤 테이블) -->
          <div class="ing">
            <div class="ing-h">
              <span class="ti">{ing_title}</span>
              <span class="ref" id="ing-vol-tag">본제 1L 기준</span>
            </div>
            <div class="ing-body-100">{ing_rows_100}</div>
            <div class="ing-body-30" style="display:none;">{ing_rows_30}</div>
          </div>

          <!-- 5) 실제 중량 알약 캡슐 -->
          <div class="pack">실제 중량 : <b id="pack-vol">100ml</b></div>
        </div>

        <!-- 중간 7mm 접착 여백 -->
        <div class="gap"><span class="wing-txt">접착여백 7mm</span></div>

        <!-- 후면 법정 고시란 -->
        <div class="col-right">
          <div class="legal">
            <div class="lg-head">
              <div class="lg-reg">
                <span class="l">사료의 성분등록번호 :</span>
                <span class="v">{prod['reg_no']}</span>
              </div>
              <div class="lg-tm">
                <span><b>KR</b> {prod['kr_tm']}</span>
                <span><b>US</b> {prod['us_tm']}</span>
              </div>
              <div class="lg-type">
                <span><b>종류/형태:</b> {prod['feed_type']}</span>
              </div>
            </div>

            <div class="lg-body">
              <div class="ir"><span class="l">등록성분량:</span><span class="v">{prod['feed_qty']}</span></div>
              <div class="ir"><span class="l">원료명칭:</span><span class="v">{prod['feed_mat']}</span></div>
              <div class="ir"><span class="l">대상:</span><span class="v">{prod['feed_target']}</span></div>
              <div class="ir" style="flex-direction:column;align-items:flex-start;">
                <span class="l" style="margin-bottom:0.2mm;">효과:</span>
                <ul class="ef" style="width:100%;">{back_eff_html}</ul>
              </div>
            </div>

            <div class="dose">
              <span class="dose-lbl">용법 및 용량:</span>
              <div class="dose-body">
                <div class="dose-t"><span>{prod['dose_t']}</span></div>
                <div class="dose-sub">- 증상에 따라 조절 가능</div>
              </div>
            </div>

            <div class="warn">
              <div class="warn-t">▲ 주의사항:</div>
              <div class="warn-b">{warn_items}</div>
            </div>

            <div class="meta">
              <span>용량: <b id="meta-vol">100ml</b></span>
              <span>제조일자: 2026.11.13</span>
              <span>유통기한: 제조일로부터 18개월</span>
            </div>

            <div class="lg-foot">
              <div class="co-dist">
                <div class="co-t"><span>위탁제조판매원 :</span></div>
                <div class="co-b">
                  <img src="{sj_logo_b64}" class="sj-foot-logo" alt="S&J 로고">
                  <span class="co-n">에스앤제이 동물병원</span>
                </div>
                <div class="co-a">경기도 용인시 처인구 백옥대로 238-8</div>
                <div class="co-tel">TEL : <b>031-321-6562</b></div>
              </div>
              <div class="co-mfg">
                <div class="co-t">
                  <span>제조원 :</span>
                  <div class="rc">
                    <div class="w">
                      <svg viewBox="0 0 100 100"><path d="M50 14 L88 80 L12 80 Z" fill="none" stroke="{c['primary']}" stroke-width="7" stroke-linejoin="round"/></svg>
                      <span class="x">플라스틱</span>
                    </div>
                    <span class="o">OTHER</span>
                  </div>
                </div>
                <div class="co-b"><span class="co-n">엠오바이오</span></div>
                <div class="co-a">경기 화성시 팔탄면 석포로74번길 10-25</div>
                <div class="co-tel">TEL : <b>031-458-1240</b></div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 우측 3mm 접착 여백 -->
      <div class="wing wing-r"><span class="wing-txt">접착 3mm</span></div>
    </div>
  </div>

  <div class="a4-cut-instructions">
    ✂ 검정색 테두리 코너 재단선(Crop Marks)을 따라 칼이나 가위로 자르면 좌측 7mm, 중간 7mm, 우측 3mm 접착 여백이 포함된 <span id="cut-dims">총 118mm × 76mm 실측 스티커</span>가 완성됩니다.
  </div>
</div>

<script>
let currentSize = '100';

function setSize(size) {{
  currentSize = size;
  document.body.classList.remove('size-100', 'size-30');
  document.body.classList.add('size-' + size);

  const b100 = document.getElementById('btn-100');
  if (b100) b100.className = size === '100' ? 'btn-size active' : 'btn-size';
  const b30 = document.getElementById('btn-30');
  if (b30) b30.className = size === '30' ? 'btn-size active' : 'btn-size';

  const is100 = size === '100';
  const gDims = document.getElementById('guide-dims');
  if (gDims) gDims.textContent = is100 ? '(좌 7 + 중 7 + 우 3 = 총 118×76mm)' : '(좌 7 + 중 7 + 우 3 = 총 101×42mm)';
  const cDims = document.getElementById('cut-dims');
  if (cDims) cDims.textContent = is100 ? '총 118mm × 76mm 실측 스티커' : '총 101mm × 42mm 실측 스티커';
  const ivTag = document.getElementById('ing-vol-tag');
  if (ivTag) ivTag.textContent = '본제 1L 기준';
  const pVol = document.getElementById('pack-vol');
  if (pVol) pVol.textContent = is100 ? '100ml' : '30ml';
  const mVol = document.getElementById('meta-vol');
  if (mVol) mVol.textContent = is100 ? '100ml' : '30ml';

  document.querySelectorAll('.fx-card-100').forEach(e => e.style.display = is100 ? 'flex' : 'none');
  document.querySelectorAll('.fx-card-30').forEach(e => e.style.display = is100 ? 'none' : 'flex');
  document.querySelectorAll('.ing-body-100').forEach(e => e.style.display = is100 ? 'block' : 'none');
  document.querySelectorAll('.ing-body-30').forEach(e => e.style.display = is100 ? 'none' : 'block');
}}

function setPaper(paper) {{
  document.body.classList.remove('paper-a4', 'paper-roll');
  document.body.classList.add('paper-' + paper);
  document.getElementById('btn-a4').className = paper === 'a4' ? 'btn-paper active' : 'btn-paper';
  document.getElementById('btn-roll').className = paper === 'roll' ? 'btn-paper active' : 'btn-paper';
}}

// URL 파라미터 체크
const params = new URLSearchParams(window.location.search);
if (params.get('size')) {{
  setSize(params.get('size'));
}} else {{
  setSize(currentSize);
}}
if (params.get('paper') === 'roll') {{
  setPaper('roll');
}}
</script>
</body>
</html>
"""
    return html

# 11개 제품 파일 생성
std_names = {
    "01": "01_monsmecta_original_modern.html",
    "02": "02_monsmecta_hepamax_modern.html",
    "03": "03_monsmecta_renal_modern.html",
    "04": "04_monsmecta_cancercare_modern.html",
    "05": "05_monsmecta_coldzero_modern.html",
    "06": "06_monsmecta_skincare_modern.html",
    "07": "07_monsmecta_heartcare_modern.html",
    "08": "08_monsmecta_jointcare_modern.html",
    "09": "09_monsmecta_powerase_modern.html",
    "10": "10_monsmecta_probiotics_modern.html",
    "11": "11_monsmecta_vitaplus_modern.html"
}

for prod in products:
    fname = prod["file"]
    p_id = fname[:2]
    target_name = std_names[p_id]
    target_path = os.path.join(base_dir, target_name)
    
    html_content = generate_modern_html(prod, p_id)
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated v3: {target_name} ({palette[p_id]['tag']})")
    
    # 01 오리지널은 monsmecta_100ml_modern.html 과 monsmecta_30ml_modern.html 로도 복사 동기화
    if p_id == "01":
        with open(os.path.join(base_dir, "monsmecta_100ml_modern.html"), "w", encoding="utf-8") as f:
            f.write(html_content)
        content_30 = (html_content
                      .replace('class="size-100 paper-a4"', 'class="size-30 paper-a4"')
                      .replace('id="btn-100" class="btn-size active"', 'id="btn-100" class="btn-size"')
                      .replace('id="btn-30" class="btn-size"', 'id="btn-30" class="btn-size active"')
                      .replace('100ml 정품 규격', '본제 1L 기준')
                      .replace('>100ml<', '>30ml<')
                      .replace("let currentSize = '100';", "let currentSize = '30';"))
        with open(os.path.join(base_dir, "monsmecta_30ml_modern.html"), "w", encoding="utf-8") as f:
            f.write(content_30)
        print("Synchronized monsmecta_100ml_modern.html and monsmecta_30ml_modern.html")

print("\nAll 11 modern labels regenerated with right-aligned values in ingredients table!")
