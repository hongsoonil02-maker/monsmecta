# -*- coding: utf-8 -*-
import base64
import os

# 1. 에스앤제이 로고 base64 가져오기
logo_path = r"C:\Users\master\monsmecta_landing\public\assets\labels\monsmecta_label_sj_logo.png"
with open(logo_path, "rb") as f:
    sj_logo_b64 = "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")

# ==============================================================================
# 2. 100ml 정품 규격 HTML 생성 (118mm × 76mm)
# ==============================================================================
html_100ml = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>몬스멕타 Label (100ml · 모던 딥그린 · 118x76mm)</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;600;700;800;900&family=Outfit:wght@600;700;800;900&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; word-break: keep-all; overflow-wrap: break-word; }}
html, body {{ font-family: 'Pretendard Variable', Pretendard, 'Noto Sans KR', -apple-system, 'Segoe UI', sans-serif; background: #01140e; color: #06402f; }}
.en {{ font-family: 'Outfit', 'Pretendard Variable', sans-serif; }}

/* ---------- 화면 뷰어 / A4 가이드 ---------- */
@media screen {{
  html, body {{ width: 100%; min-height: 100vh; background: #021a13; }}
  body {{ padding: 70px 20px 40px; display: flex; flex-direction: column; align-items: center; }}
  .a4-guide-wrapper {{ background: #fff; padding: 10mm 15mm 15mm; border-radius: 4px; box-shadow: 0 15px 40px rgba(0,0,0,.7); display: flex; flex-direction: column; align-items: center; }}
  body.paper-roll .a4-guide-wrapper {{ background: transparent; padding: 0; box-shadow: none; }}
  body.paper-roll .a4-header-guide, body.paper-roll .a4-cut-instructions, body.paper-roll .crop-line {{ display: none !important; }}
}}
.toolbar {{ position: fixed; top: 12px; left: 50%; transform: translateX(-50%); z-index: 99999; background: rgba(6,32,24,.95); border: 1px solid #10b981; padding: 8px 20px; border-radius: 14px; display: flex; align-items: center; gap: 14px; box-shadow: 0 10px 30px rgba(0,0,0,.85); color: #fff; font-size: 12.5px; font-weight: 700; }}
.toolbar button {{ font-weight: 700; font-size: 11.5px; padding: 5px 12px; border: none; border-radius: 6px; cursor: pointer; color: #fff; }}
.a4-header-guide {{ text-align: center; margin-bottom: 6mm; width: 100%; }}
.a4-header-guide h2 {{ font-size: 13.5pt; font-weight: 900; color: #06402f; margin-bottom: 2mm; }}
.a4-header-guide p {{ font-size: 8.5pt; font-weight: 700; color: #334155; margin-bottom: 3mm; }}
.ruler-50mm {{ display: flex; align-items: center; justify-content: center; gap: 3mm; font-size: 8.5pt; color: #1e293b; font-weight: 700; }}
.ruler-bar {{ width: 50mm; height: 5.5mm; border: .35mm solid #06402f; border-top: none; position: relative; }}
.ruler-tick {{ position: absolute; bottom: 0; width: .3mm; background: #06402f; }}
.tick-0 {{ left: 0; height: 5.5mm; }} .tick-1 {{ left: 10mm; height: 3mm; }} .tick-2 {{ left: 20mm; height: 3mm; }}
.tick-3 {{ left: 30mm; height: 3mm; }} .tick-4 {{ left: 40mm; height: 3mm; }} .tick-50 {{ right: 0; height: 5.5mm; }}
.ruler-note {{ font-size: 8pt; color: #64748b; }}
.a4-cut-instructions {{ margin-top: 6mm; font-size: 8.5pt; color: #475569; font-weight: 700; text-align: center; }}

.crop-marks-box {{ position: relative; width: 118mm; height: 76mm; margin: 0 auto; flex-shrink: 0; }}
.crop-line {{ position: absolute; background: #06402f; z-index: 100; pointer-events: none; }}
.crop-tl-h {{ top: 0; left: -6mm; width: 4.5mm; height: .3mm; }} .crop-tl-v {{ top: -6mm; left: 0; width: .3mm; height: 4.5mm; }}
.crop-tr-h {{ top: 0; right: -6mm; width: 4.5mm; height: .3mm; }} .crop-tr-v {{ top: -6mm; right: 0; width: .3mm; height: 4.5mm; }}
.crop-bl-h {{ bottom: 0; left: -6mm; width: 4.5mm; height: .3mm; }} .crop-bl-v {{ bottom: -6mm; left: 0; width: .3mm; height: 4.5mm; }}
.crop-br-h {{ bottom: 0; right: -6mm; width: 4.5mm; height: .3mm; }} .crop-br-v {{ bottom: -6mm; right: 0; width: .3mm; height: 4.5mm; }}

/* ---------- 스티커 본체 (118mm × 76mm) ---------- */
.sticker {{ display: flex; width: 118mm; height: 76mm; background: #fff; box-shadow: 0 0 0 .2mm #cbd5e1; position: relative; overflow: hidden; }}
.wing {{ background: #fff; flex-shrink: 0; height: 100%; display: flex; align-items: center; justify-content: center; position: relative; z-index: 20; }}
.wing-l {{ width: 7mm; border-right: .2mm dashed #94a3b8; }}
.wing-r {{ width: 3mm; }}
.wing-txt {{ writing-mode: vertical-rl; font-size: 2.200mm; color: #94a3b8; font-weight: 800; letter-spacing: 1mm; opacity: .8; white-space: nowrap; user-select: none; }}

.sheet {{ position: relative; width: 108mm; height: 76mm; flex-shrink: 0; overflow: hidden; color: #fff;
  background:
    radial-gradient(circle at 92% 4%, rgba(16,185,129,.35) 0, transparent 34%),
    radial-gradient(circle at 4% 98%, rgba(216,244,106,.20) 0, transparent 38%),
    linear-gradient(165deg, #06402f 0%, #032b1f 52%, #01140e 100%); }}
.blob {{ position: absolute; border-radius: 50%; z-index: 1; pointer-events: none; }}
.blob.b1 {{ width: 14mm; height: 14mm; right: -4mm; top: 9mm; background: rgba(255,209,102,.16); }}
.blob.b2 {{ width: 9mm; height: 9mm; left: -3mm; top: 33mm; background: rgba(216,244,106,.15); }}
.blob.b3 {{ width: 11mm; height: 11mm; left: 36mm; bottom: 6mm; background: rgba(16,185,129,.16); }}
.paw {{ position: absolute; inset: 0; background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='60' height='60' viewBox='0 0 60 60'><g fill='white' fill-opacity='0.045'><ellipse cx='30' cy='38' rx='9' ry='7'/><ellipse cx='17' cy='27' rx='4' ry='5.5'/><ellipse cx='25' cy='20' rx='4' ry='5.5'/><ellipse cx='35' cy='20' rx='4' ry='5.5'/><ellipse cx='43' cy='27' rx='4' ry='5.5'/></g></svg>"); background-size: 10.000mm 10.000mm; z-index: 1; pointer-events: none; }}
.bar-top, .bar-bot {{ position: absolute; left: 0; right: 0; height: 0.80mm; background: linear-gradient(90deg, #10b981, #d8f46a, #ffd166); z-index: 2; }}
.bar-top {{ top: 0; }} .bar-bot {{ bottom: 0; }}

/* 중앙 7mm 접착여백 */
.gap {{ position: absolute; top: 0; bottom: 0; left: 50.500mm; width: 7mm; background: #fff; z-index: 20;
  border-left: .2mm dashed #94a3b8; border-right: .2mm dashed #94a3b8; display: flex; align-items: center; justify-content: center; }}

.col-left, .col-right {{ position: absolute; top: 2.200mm; bottom: 2.200mm; width: 49.500mm; z-index: 5; }}
.col-left {{ left: 1.000mm; padding: 0 0.500mm; display: flex; flex-direction: column; justify-content: space-between; }}
.col-right {{ right: 1.000mm; }}

/* 1) 브랜드 배지 */
.badge {{ align-self: center; display: flex; align-items: center; justify-content: center; gap: 1.000mm;
  background: #fff; color: #06402f; box-shadow: 0 0.350mm 0 rgba(1,20,14,.35); border-radius: 999px; padding: 0.700mm 2.400mm; line-height: 1; }}
.badge .t {{ font-size: 1.650mm; font-weight: 800; letter-spacing: .05em; white-space: nowrap; }}
.badge .t b {{ color: #0e9f6e; font-weight: 900; }}
.badge svg {{ width: 2.000mm; height: 2.000mm; flex: 0 0 2.000mm; }}

/* 2) 히어로 */
.hero {{ text-align: center; margin-top: 0.200mm; }}
.tag {{ display: inline-block; font-size: 1.750mm; font-weight: 800; color: #06402f; background: #ffd166; border-radius: 999px; padding: 0.600mm 2.200mm; letter-spacing: -.01em; line-height: 1.15; margin-bottom: 1.000mm; box-shadow: 0 0.300mm 0 rgba(1,20,14,.3); }}
.hero-row {{ display: flex; align-items: center; justify-content: center; gap: 1.000mm; }}
.pet {{ flex: 0 0 8.400mm; width: 8.400mm; height: 8.400mm; filter: drop-shadow(0 0.350mm 0 rgba(1,20,14,.3)); }}
.pet-dog {{ transform: rotate(-8deg); }}
.pet-cat {{ transform: rotate(8deg); }}
.ttl-wrap {{ display: flex; flex-direction: column; align-items: center; }}
.title {{ font-size: 8.800mm; font-weight: 900; line-height: 1; letter-spacing: -.04em; color: #fff; text-shadow: 0.420mm 0.420mm 0 #0e9f6e, 0.700mm 0.700mm 0 rgba(1,20,14,.40); margin-bottom: 0.400mm; white-space: nowrap; }}
.title sup.tm {{ font-size: 3.800mm; font-weight: 800; vertical-align: top; margin-left: 0.500mm; text-shadow: 0.300mm 0.300mm 0 #0e9f6e; }}
.sub {{ display: inline-block; font-size: 2.200mm; font-weight: 800; letter-spacing: .18em; color: #06402f; background: #bff0d6; border-radius: 999px; padding: 0.450mm 1.800mm 0.450mm calc(1.800mm + .18em); line-height: 1.1; }}
.sub sup.tm {{ font-size: 1.400mm; font-weight: 900; vertical-align: top; margin-left: 0.300mm; }}

/* 3) 핵심 효능 */
.fx {{ position: relative; margin-top: 1.200mm; }}
.fx-tab {{ position: absolute; top: -1.700mm; left: 2.000mm; background: #d8f46a; color: #06402f; font-size: 1.650mm; font-weight: 900; padding: 0.500mm 1.800mm; border-radius: 999px; line-height: 1.1; z-index: 3; box-shadow: 0 0.250mm 0 rgba(1,20,14,.3); }}
.fx-card {{ background: #fff7e8; color: #06402f; border-radius: 2.400mm; padding: 2.000mm 1.800mm 1.400mm; display: flex; flex-direction: column; gap: 0.900mm; box-shadow: 0 0.400mm 0 rgba(1,20,14,.3); }}
.fx-item {{ display: flex; align-items: center; gap: 1.100mm; font-size: 1.900mm; font-weight: 800; line-height: 1.2; white-space: nowrap; }}
.chk {{ flex: 0 0 2.200mm; width: 2.200mm; height: 2.200mm; border-radius: 50%; background: #10b981; color: #fff; font-size: 1.350mm; font-weight: 900; display: flex; align-items: center; justify-content: center; line-height: 1; }}

/* 4) 성분 (5가지 복합체) */
.ing {{ background: #eefdf5; color: #06402f; border-radius: 2.400mm; padding: 1.100mm 1.400mm; box-shadow: 0 0.400mm 0 rgba(1,20,14,.3); }}
.ing-h {{ display: flex; align-items: center; justify-content: space-between; padding-bottom: 0.500mm; margin-bottom: 0.600mm; border-bottom: 0.180mm dashed #a7f3d0; }}
.ing-h .ti {{ font-size: 1.700mm; font-weight: 900; }}
.ing-h .ref {{ font-size: 1.350mm; font-weight: 800; color: #fff; background: #10b981; border-radius: 999px; padding: 0.300mm 1.200mm; line-height: 1.1; }}
.row {{ display: flex; align-items: flex-start; gap: 1.000mm; margin-bottom: 0.380mm; }}
.row:last-child {{ margin-bottom: 0; }}
.no {{ flex: 0 0 1.850mm; width: 1.850mm; height: 1.850mm; margin-top: 0.020mm; border-radius: 50%; background: #06402f; color: #fff; font-size: 1.250mm; font-weight: 900; display: flex; align-items: center; justify-content: center; line-height: 1; }}
.row:nth-child(2) .no {{ background: #10b981; }}
.row:nth-child(3) .no {{ background: #0d9488; }}
.row:nth-child(4) .no {{ background: #7c3aed; }}
.row:nth-child(5) .no {{ background: #ea580c; }}
.row:nth-child(6) .no {{ background: #db2777; }}
.rb {{ flex: 1; min-width: 0; }}
.rm {{ font-size: 1.550mm; font-weight: 800; line-height: 1.22; white-space: nowrap; }}
.rm i {{ font-style: normal; color: #0e9f6e; font-weight: 800; margin-left: 0.500mm; }}
.rs {{ font-size: 1.300mm; font-weight: 600; color: #1e3a2f; line-height: 1.20; white-space: nowrap; padding-left: 0.800mm; }}
.rs em {{ font-style: normal; color: #c2410c; font-weight: 800; font-size: 1.220mm; }}
.rn {{ font-size: 1.220mm; font-weight: 600; color: #2d5a47; line-height: 1.20; padding-left: 0.200mm; }}

/* 5) 포장 용량 알약 */
.pack {{ align-self: center; background: #ffd166; color: #06402f; border-radius: 999px; padding: 0.750mm 2.800mm; font-size: 1.950mm; font-weight: 900; line-height: 1; display: flex; gap: 0.800mm; align-items: center; box-shadow: 0 0.350mm 0 rgba(1,20,14,.35); margin-bottom: 0.400mm; }}
.pack b {{ color: #06402f; font-weight: 900; }}
.pack::before {{ content: ""; width: 2.200mm; height: 2.200mm; background: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 60 60'><g fill='%2306402f'><ellipse cx='30' cy='38' rx='11' ry='9'/><ellipse cx='13' cy='26' rx='5' ry='7'/><ellipse cx='24' cy='16' rx='5' ry='7'/><ellipse cx='36' cy='16' rx='5' ry='7'/><ellipse cx='47' cy='26' rx='5' ry='7'/></g></svg>") center / contain no-repeat; }}

/* ---------- 우측: 법정 고시 카드 ---------- */
.legal {{ height: 100%; background: #fff; color: #1e293b; border: 0.500mm solid #ffd166; border-radius: 2.400mm; padding: 0.800mm 1.000mm; display: flex; flex-direction: column; justify-content: space-between; }}
.lg-head {{ background: #06402f; color: #fff; border-radius: 1.200mm; padding: 0.650mm 1.100mm; display: flex; flex-direction: column; gap: 0.300mm; }}
.lg-reg {{ display: flex; justify-content: space-between; align-items: baseline; line-height: 1.15; }}
.lg-reg .l {{ font-size: 1.450mm; font-weight: 800; color: #d8f46a; }}
.lg-reg .v {{ font-size: 1.750mm; font-weight: 900; letter-spacing: .02em; color: #fff; }}
.lg-tm {{ display: flex; justify-content: space-between; font-size: 1.220mm; font-weight: 600; color: #bff0d6; border-top: 0.15mm solid rgba(255,255,255,.15); padding-top: 0.25mm; margin-top: 0.2mm; line-height: 1.15; }}
.lg-tm b {{ color: #ffd166; font-weight: 800; }}
.lg-type {{ font-size: 1.300mm; font-weight: 600; line-height: 1.20; color: #e2e8f0; }}
.lg-type b {{ color: #ffd166; font-weight: 800; }}
.lg-body {{ display: flex; flex-direction: column; gap: 0.450mm; }}
.ir {{ display: flex; align-items: baseline; font-size: 1.450mm; line-height: 1.20; padding-bottom: 0.350mm; border-bottom: 0.150mm dotted #cbd5e1; }}
.ir:last-child {{ border-bottom: none; padding-bottom: 0; }}
.ir .l {{ font-weight: 800; color: #06402f; margin-right: 0.800mm; white-space: nowrap; flex-shrink: 0; }}
.ir .v {{ flex: 1; font-weight: 600; color: #1e293b; }}
.ir .v strong {{ font-weight: 900; color: #0f172a; }}
.ef {{ list-style: none; display: flex; flex-direction: column; gap: 0.250mm; margin-top: 0.250mm; }}
.ef li {{ display: flex; align-items: baseline; gap: 0.800mm; font-size: 1.450mm; font-weight: 600; line-height: 1.20; }}
.ef .n {{ flex: 0 0 1.650mm; width: 1.650mm; height: 1.650mm; border-radius: 50%; background: #06402f; color: #fff; font-size: 1.120mm; font-weight: 900; display: flex; align-items: center; justify-content: center; line-height: 1; transform: translateY(0.150mm); }}
.dose {{ background: #eefdf5; border-left: 0.800mm solid #10b981; border-radius: 0.800mm; padding: 0.650mm 1.200mm; }}
.dose .r {{ display: flex; align-items: baseline; flex-wrap: wrap; gap: 0.800mm; font-size: 1.450mm; line-height: 1.2; }}
.dose .tt {{ font-weight: 900; color: #06402f; }}
.dose .d {{ font-weight: 800; color: #0f172a; }}
.dose .s {{ font-size: 1.250mm; color: #475569; font-weight: 600; margin-top: 0.200mm; }}
.warn {{ background: #fff1f2; border: 0.200mm solid #fecdd3; border-radius: 1.200mm; padding: 0.750mm 1.200mm; }}
.warn .tt {{ display: flex; align-items: center; gap: 0.600mm; color: #be123c; font-size: 1.500mm; font-weight: 900; margin-bottom: 0.350mm; }}
.warn ul {{ list-style: none; display: flex; flex-direction: column; gap: 0.250mm; }}
.warn li {{ display: flex; gap: 0.600mm; font-size: 1.380mm; font-weight: 600; line-height: 1.20; color: #1e293b; }}
.warn li .n {{ color: #be123c; font-weight: 900; flex-shrink: 0; }}
.warn .hl {{ color: #be123c; font-weight: 900; text-decoration: underline; text-underline-offset: 0.300mm; }}
.mfg {{ background: #f1f5f9; border-radius: 999px; padding: 0.650mm 1.400mm; display: flex; justify-content: space-between; align-items: center; font-size: 1.360mm; line-height: 1.1; }}
.mfg .l {{ color: #64748b; font-weight: 700; margin-right: 0.300mm; }}
.mfg .v {{ color: #06402f; font-weight: 900; }}
.lg-foot {{ display: grid; grid-template-columns: 48% 52%; column-gap: 1.000mm; align-items: start; }}
.co-t {{ height: 3.000mm; display: flex; align-items: center; justify-content: space-between; font-size: 1.400mm; font-weight: 900; color: #06402f; line-height: 1; white-space: nowrap; }}
.co-b {{ height: 2.250mm; margin: 0.150mm 0 0.250mm; display: flex; align-items: center; }}
.co-b img {{ height: 100%; width: auto; max-width: 100%; object-fit: contain; display: block; }}
.co-n {{ font-size: 1.480mm; font-weight: 900; color: #0f172a; line-height: 1; white-space: nowrap; }}
.co-a, .co-tel {{ font-size: 1.280mm; color: #475569; line-height: 1.2; font-weight: 600; white-space: nowrap; }}
.co-tel b {{ color: #0e9f6e; font-weight: 800; }}
.rc {{ display: flex; align-items: center; gap: 0.500mm; margin-right: 0.600mm; }}
.rc .w {{ position: relative; width: 3.000mm; height: 3.000mm; display: flex; align-items: center; justify-content: center; }}
.rc svg {{ width: 100%; height: 100%; }}
.rc .x {{ position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; font-size: 0.800mm; font-weight: 900; color: #06402f; padding-top: 0.350mm; letter-spacing: -.05em; }}
.rc .o {{ font-size: 1.100mm; font-weight: 900; color: #06402f; line-height: 1; }}

@media print {{
  body.paper-a4, html.paper-a4 {{ width: 210mm !important; min-height: 297mm !important; height: 297mm !important; margin: 0 auto !important; padding: 0 !important; background: #fff !important; }}
  body.paper-a4 .a4-guide-wrapper {{ padding: 14mm 0 0 !important; box-shadow: none !important; margin: 0 auto !important; width: 210mm !important; background: #fff !important; display: flex !important; flex-direction: column !important; align-items: center !important; }}
  .no-print {{ display: none !important; }}
  body.paper-roll, html.paper-roll {{ width: 118mm !important; height: 76mm !important; margin: 0 !important; padding: 0 !important; background: transparent !important; overflow: hidden !important; }}
  body.paper-roll .a4-header-guide, body.paper-roll .a4-cut-instructions, body.paper-roll .crop-line {{ display: none !important; }}
  body.paper-roll .a4-guide-wrapper, body.paper-roll .crop-marks-box {{ padding: 0 !important; margin: 0 !important; width: 118mm !important; height: 76mm !important; }}
  .sticker {{ box-shadow: none !important; }}
}}
</style>
<style id="page-style">@page {{ size: A4 portrait; margin: 0; }}</style>
</head>
<body class="paper-a4">

<div class="no-print toolbar">
  <div><span style="color:#10b981;">★ 몬스멕타 (100ml 실측: 118mm × 76mm)</span> | [모던 · 딥그린] (좌7mm + 중7mm + 우3mm)</div>
  <div style="display:flex;gap:6px;">
    <button onclick="setPaperMode('a4')" style="background:#059669;">📄 A4 실측 (자르기 가이드)</button>
    <button onclick="setPaperMode('roll')" style="background:#1e3a2f;color:#cbd5e1;">🏷️ 롤 라벨 (118×76mm)</button>
  </div>
  <button onclick="window.print()" style="background:linear-gradient(135deg,#10b981,#047857);font-weight:800;font-size:12px;padding:6px 16px;border-radius:8px;">라벨 인쇄 (Ctrl+P)</button>
</div>

<div class="a4-guide-wrapper">
  <div class="a4-header-guide">
    <h2>[몬스멕타 100ml 정품 규격] 용기 라벨 · 모던 딥그린 (좌측 7mm + 중간 7mm + 우측 3mm 접착 = 총 118×76mm)</h2>
    <p>※ 인쇄 설정 시 반드시 <strong>[배율: 맞춤(100%)]</strong> 또는 <strong>[실제 크기(Actual Size)]</strong>로 지정하십시오.</p>
    <div class="ruler-50mm"><span>실측 확인용 눈금자:</span>
      <div class="ruler-bar"><div class="ruler-tick tick-0"></div><div class="ruler-tick tick-1"></div><div class="ruler-tick tick-2"></div><div class="ruler-tick tick-3"></div><div class="ruler-tick tick-4"></div><div class="ruler-tick tick-50"></div></div>
      <span class="ruler-note">(자로 쟀을 때 정확히 5cm)</span></div>
  </div>

  <div class="crop-marks-box">
    <div class="crop-line crop-tl-h"></div><div class="crop-line crop-tl-v"></div><div class="crop-line crop-tr-h"></div><div class="crop-line crop-tr-v"></div>
    <div class="crop-line crop-bl-h"></div><div class="crop-line crop-bl-v"></div><div class="crop-line crop-br-h"></div><div class="crop-line crop-br-v"></div>

    <div class="sticker">
      <div class="wing wing-l"><div class="wing-txt">접착 7mm</div></div>

      <div class="sheet">
        <div class="paw"></div>
        <div class="blob b1"></div><div class="blob b2"></div><div class="blob b3"></div>
        <div class="bar-top"></div><div class="bar-bot"></div>

        <!-- 좌측: 전면 (49.5mm) -->
        <div class="col-left">
          <div class="badge">
            <svg viewBox="0 0 60 60"><g fill="#0e9f6e"><ellipse cx="30" cy="38" rx="11" ry="9"/><ellipse cx="13" cy="26" rx="5" ry="7"/><ellipse cx="24" cy="16" rx="5" ry="7"/><ellipse cx="36" cy="16" rx="5" ry="7"/><ellipse cx="47" cy="26" rx="5" ry="7"/></g></svg>
            <span class="t"><b>S&amp;J</b>&nbsp;ADVANCED VET FORMULA</span>
            <svg viewBox="0 0 60 60"><g fill="#0e9f6e"><ellipse cx="30" cy="38" rx="11" ry="9"/><ellipse cx="13" cy="26" rx="5" ry="7"/><ellipse cx="24" cy="16" rx="5" ry="7"/><ellipse cx="36" cy="16" rx="5" ry="7"/><ellipse cx="47" cy="26" rx="5" ry="7"/></g></svg>
          </div>

          <div class="hero">
            <div class="tag">연변 시 장 기능 개선 및 정장 작용에 뛰어난</div>
            <div class="hero-row">
              <svg class="pet pet-dog" viewBox="0 0 40 40"><circle cx="20" cy="20" r="19" fill="#a7f3d0"/><ellipse cx="8" cy="18" rx="4.8" ry="9" fill="#b9763f" transform="rotate(14 8 18)"/><ellipse cx="32" cy="18" rx="4.8" ry="9" fill="#b9763f" transform="rotate(-14 32 18)"/><ellipse cx="20" cy="22" rx="11.5" ry="11" fill="#fff3dc"/><circle cx="14.800" cy="20" r="1.700" fill="#06402f"/><circle cx="25.200" cy="20" r="1.700" fill="#06402f"/><circle cx="15.400" cy="19.300" r=".6" fill="#fff"/><circle cx="25.800" cy="19.300" r=".6" fill="#fff"/><circle cx="11.500" cy="25" r="2" fill="#fda4af" opacity=".7"/><circle cx="28.500" cy="25" r="2" fill="#fda4af" opacity=".7"/><ellipse cx="20" cy="26" rx="5" ry="3.800" fill="#fff"/><ellipse cx="20" cy="24.200" rx="2.300" ry="1.600" fill="#06402f"/><path d="M20 25.800v1.400M20 27.200q-2 1.800-3.800 0M20 27.200q2 1.800 3.800 0" stroke="#06402f" stroke-width=".9" fill="none" stroke-linecap="round"/><path d="M18.600 28.400q1.400 3.600 2.800 0z" fill="#fb7185"/></svg>
              <div class="ttl-wrap">
                <div class="title">몬스멕타<sup class="tm">™</sup></div>
                <div class="sub en">MONSMECTA<sup class="tm">™</sup></div>
              </div>
              <svg class="pet pet-cat" viewBox="0 0 40 40"><circle cx="20" cy="20" r="19" fill="#fde68a"/><path d="M8.500 18 9.500 4.500 21 11.500z" fill="#cbd5e1"/><path d="M31.500 18 30.500 4.500 19 11.500z" fill="#cbd5e1"/><path d="M11 14 11.500 8.500 16 11.500z" fill="#fda4af"/><path d="M29 14 28.500 8.500 24 11.500z" fill="#fda4af"/><ellipse cx="20" cy="23" rx="12.500" ry="10.500" fill="#e2e8f0"/><ellipse cx="14.500" cy="21" rx="1.800" ry="2.100" fill="#06402f"/><ellipse cx="25.500" cy="21" rx="1.800" ry="2.100" fill="#06402f"/><circle cx="15.200" cy="20.200" r=".65" fill="#fff"/><circle cx="26.200" cy="20.200" r=".65" fill="#fff"/><circle cx="10.800" cy="26" r="2" fill="#fda4af" opacity=".7"/><circle cx="29.200" cy="26" r="2" fill="#fda4af" opacity=".7"/><path d="M18.500 24.600h3L20 26.200z" fill="#f472b6"/><path d="M20 26.200q-1.600 2-3.400.6M20 26.200q1.600 2 3.400.6" stroke="#06402f" stroke-width=".8" fill="none" stroke-linecap="round"/><path d="M5 23l5 1M5 27l5-1M35 23l-5 1M35 27l-5-1" stroke="#64748b" stroke-width=".6" stroke-linecap="round"/></svg>
            </div>
          </div>

          <div class="fx">
            <div class="fx-tab">핵심 효능</div>
            <div class="fx-card">
              <div class="fx-item"><span class="chk">✓</span><span>장 관련 질환(파보, 로타, 코로나 등) 저항력 향상</span></div>
              <div class="fx-item"><span class="chk">✓</span><span>면역 기능 및 전신 건강 상태 유지에 도움</span></div>
              <div class="fx-item"><span class="chk">✓</span><span>장 점막 보호 및 설사·연변 정장 작용에 도움</span></div>
            </div>
          </div>

          <div class="ing">
            <div class="ing-h"><span class="ti">성분(5가지 복합체)</span><span class="ref">100ml 정품 규격</span></div>
            <div class="row"><span class="no">1</span><div class="rb">
              <div class="rm">항균 · 항바이러스 작용</div>
              <div class="rs">- 1-deoxynojirimycin (DNJ) 천연성분 함유</div>
              <div class="rs">· 특허균주 Bacillus subtilis MORI 균주 <em>(Patent No. 201180042602.8)</em></div></div></div>
            <div class="row"><span class="no">2</span><div class="rb"><div class="rm">장 기능 개선 및 정장 작용 <i>- 포도당</i></div></div></div>
            <div class="row"><span class="no">3</span><div class="rb"><div class="rm">상피세포의 회복 <i>- 비타민 A</i></div></div></div>
            <div class="row"><span class="no">4</span><div class="rb"><div class="rm">전해질제 <i>- Sodium acetate, Sodium propionate</i></div></div></div>
            <div class="row"><span class="no">5</span><div class="rb">
              <div class="rm">연변 및 설사 개선, 독소 제거 <i>- 몬모릴로나이트</i></div>
              <div class="rn">(곰팡이 독소 제거, 면역 증강 및 장 환경 개선에 도움)</div></div></div>
          </div>

          <div class="pack"><span>실제 중량 :</span><b>100ml</b></div>
        </div>

        <!-- 중앙 접착여백 (7mm) -->
        <div class="gap"><div class="wing-txt">접착여백 7mm</div></div>

        <!-- 우측: 법정 고시 (49.5mm) -->
        <div class="col-right"><div class="legal">
          <div class="lg-head">
            <div class="lg-reg"><span class="l">사료의 성분등록번호 :</span><span class="v">제XX9UY0145호</span></div>
            <div class="lg-tm"><span><b>KR 특허청 상표출원</b> 제40-2026-0140274호</span><span><b>US 미국 USPTO</b> App No. 50/041,096</span></div>
            <div class="lg-type"><b>종류 및 명칭 :</b> 보조사료 / 미생물제 / 바실러스 서브틸리스(액상)<br><b>형태 및 용도 :</b> 액상 / 반려동물용 (반려견, 반려묘)</div>
          </div>

          <div class="lg-body">
            <div class="ir"><span class="l">등록성분량 :</span><span class="v">바실러스 서브틸리스 1.0 x 10⁷ cfu/g 이상, 부형제(정제수)</span></div>
            <div class="ir"><span class="l">사용한 원료의 명칭 :</span><span class="v">바실러스 서브틸리스, 비타민A, 아세트산나트륨,<br>프로피온산나트륨, 포도당, <strong>몬모릴로나이트</strong>, 정제수</span></div>
            <div class="ir"><span class="l">대상 :</span><span class="v">반려견, 반려묘 (모든 반려동물 및 가축)</span></div>
            <div><div class="ir" style="border:none;padding-bottom:0;"><span class="l">효과 :</span></div>
              <ul class="ef">
                <li><span class="n">1</span><span>장 관련 질병(파보, 로타, 코로나 등)에 대한 저항력 향상에 도움</span></li>
                <li><span class="n">2</span><span>면역 기능 및 전신 건강 상태 유지에 도움</span></li>
                <li><span class="n">3</span><span>장 기능 개선 및 정장 작용에 도움</span></li>
              </ul></div>
          </div>

          <div class="dose">
            <div class="r"><span class="tt">용법 및 용량 :</span><span class="d">1일 1~2ml / 체중 5kg</span><span class="d">( 1 펌프 = 약 1ml )</span></div>
            <div class="s">- 증상에 따라 조절 가능</div>
          </div>

          <div class="warn">
            <div class="tt"><svg width="2.00mm" height="2.00mm" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd"/></svg><span>주의사항 :</span></div>
            <ul>
              <li><span class="n">1)</span><span>직사광선을 피하여 서늘한 곳에 보관하십시오.</span></li>
              <li><span class="n">2)</span><span>제품 특성상 가라앉는 성분들이 있어서 <span class="hl">반드시 흔들어서 사용</span>하십시오.</span></li>
              <li><span class="n">3)</span><span>제품에 대하여 문의하실 경우 제조원 또는 <strong>위탁제조판매원</strong>으로 연락하여 주시기 바랍니다.</span></li>
            </ul>
          </div>

          <div class="mfg"><div><span class="l">중량 :</span><span class="v">100ml</span></div><div><span class="l">제조일자 :</span><span class="v">별도표기</span></div><div><span class="l">유통기한 :</span><span class="v">제조일로부터 18개월</span></div></div>

          <div class="lg-foot">
            <div>
              <div class="co-t"><span>위탁제조판매원 :</span></div>
              <div class="co-b"><img src="{sj_logo_b64}" alt="S&amp;J 동물병원"></div>
              <div class="co-n">에스앤제이 동물병원</div>
              <div class="co-a">경기도 용인시 처인구 모현읍 백옥대로 238-8</div>
              <div class="co-tel">TEL : <b>031-321-6562</b></div>
            </div>
            <div>
              <div class="co-t"><span>제조원 :</span>
                <div class="rc"><div class="w"><svg viewBox="0 0 110 100"><path d="M55 6L104 88H6z" fill="none" stroke="#06402f" stroke-width="7" stroke-linejoin="round"/></svg><div class="x">OTHER</div></div><div class="o">플라스틱</div></div>
              </div>
              <div class="co-b" style="height:2.250mm;"></div>
              <div class="co-n">엠오바이오</div>
              <div class="co-a">경기 화성시 팔탄면 석포로74번길 10-25</div>
              <div class="co-tel">TEL : <b>031-458-1240</b></div>
            </div>
          </div>
        </div></div>
      </div>

      <div class="wing wing-r"><div class="wing-txt" style="writing-mode:vertical-rl;font-size:2.0mm;color:#94a3b8;font-weight:800;letter-spacing:1mm;">접착 3mm</div></div>
    </div>
  </div>

  <div class="a4-cut-instructions">
    ✂ 검정색 테두리 코너 재단선(Crop Marks)을 따라 칼이나 가위로 자르면 좌측 7mm, 중간 7mm, 우측 3mm 접착 여백이 포함된 총 118mm × 76mm 실측 스티커가 완성됩니다.
  </div>
</div>

<script>
function setPaperMode(mode) {{
  document.body.classList.remove('paper-a4', 'paper-roll');
  document.body.classList.add('paper-' + mode);
  document.getElementById('page-style').textContent = mode === 'roll'
    ? '@page {{ size: 118mm 76mm; margin: 0; }}'
    : '@page {{ size: A4 portrait; margin: 0; }}';
}}
</script>
</body>
</html>
"""

# ==============================================================================
# 3. 30ml 정품 규격 HTML 생성 (101mm × 42mm)
# ==============================================================================
html_30ml = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>몬스멕타 Label (30ml · 모던 딥그린 · 101x42mm)</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;600;700;800;900&family=Outfit:wght@600;700;800;900&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; word-break: keep-all; overflow-wrap: break-word; }}
html, body {{ font-family: 'Pretendard Variable', Pretendard, 'Noto Sans KR', -apple-system, 'Segoe UI', sans-serif; background: #01140e; color: #06402f; }}
.en {{ font-family: 'Outfit', 'Pretendard Variable', sans-serif; }}

/* ---------- 화면 뷰어 / A4 가이드 ---------- */
@media screen {{
  html, body {{ width: 100%; min-height: 100vh; background: #021a13; }}
  body {{ padding: 70px 20px 40px; display: flex; flex-direction: column; align-items: center; }}
  .a4-guide-wrapper {{ background: #fff; padding: 8mm 12mm 12mm; border-radius: 4px; box-shadow: 0 15px 40px rgba(0,0,0,.7); display: flex; flex-direction: column; align-items: center; }}
  body.paper-roll .a4-guide-wrapper {{ background: transparent; padding: 0; box-shadow: none; }}
  body.paper-roll .a4-header-guide, body.paper-roll .a4-cut-instructions, body.paper-roll .crop-line {{ display: none !important; }}
}}
.toolbar {{ position: fixed; top: 12px; left: 50%; transform: translateX(-50%); z-index: 99999; background: rgba(6,32,24,.95); border: 1px solid #10b981; padding: 8px 20px; border-radius: 14px; display: flex; align-items: center; gap: 14px; box-shadow: 0 10px 30px rgba(0,0,0,.85); color: #fff; font-size: 12.5px; font-weight: 700; }}
.toolbar button {{ font-weight: 700; font-size: 11.5px; padding: 5px 12px; border: none; border-radius: 6px; cursor: pointer; color: #fff; }}
.a4-header-guide {{ text-align: center; margin-bottom: 4mm; width: 100%; }}
.a4-header-guide h2 {{ font-size: 12.0pt; font-weight: 900; color: #06402f; margin-bottom: 1.5mm; }}
.a4-header-guide p {{ font-size: 8.0pt; font-weight: 700; color: #334155; margin-bottom: 2.5mm; }}
.ruler-50mm {{ display: flex; align-items: center; justify-content: center; gap: 3mm; font-size: 8.0pt; color: #1e293b; font-weight: 700; }}
.ruler-bar {{ width: 50mm; height: 4.5mm; border: .35mm solid #06402f; border-top: none; position: relative; }}
.ruler-tick {{ position: absolute; bottom: 0; width: .3mm; background: #06402f; }}
.tick-0 {{ left: 0; height: 4.5mm; }} .tick-1 {{ left: 10mm; height: 2.5mm; }} .tick-2 {{ left: 20mm; height: 2.5mm; }}
.tick-3 {{ left: 30mm; height: 2.5mm; }} .tick-4 {{ left: 40mm; height: 2.5mm; }} .tick-50 {{ right: 0; height: 4.5mm; }}
.ruler-note {{ font-size: 7.5pt; color: #64748b; }}
.a4-cut-instructions {{ margin-top: 5mm; font-size: 8.0pt; color: #475569; font-weight: 700; text-align: center; }}

.crop-marks-box {{ position: relative; width: 101mm; height: 42mm; margin: 0 auto; flex-shrink: 0; }}
.crop-line {{ position: absolute; background: #06402f; z-index: 100; pointer-events: none; }}
.crop-tl-h {{ top: 0; left: -5mm; width: 4mm; height: .3mm; }} .crop-tl-v {{ top: -5mm; left: 0; width: .3mm; height: 4mm; }}
.crop-tr-h {{ top: 0; right: -5mm; width: 4mm; height: .3mm; }} .crop-tr-v {{ top: -5mm; right: 0; width: .3mm; height: 4mm; }}
.crop-bl-h {{ bottom: 0; left: -5mm; width: 4mm; height: .3mm; }} .crop-bl-v {{ bottom: -5mm; left: 0; width: .3mm; height: 4mm; }}
.crop-br-h {{ bottom: 0; right: -5mm; width: 4mm; height: .3mm; }} .crop-br-v {{ bottom: -5mm; right: 0; width: .3mm; height: 4mm; }}

/* ---------- 스티커 본체 (101mm × 42mm) ---------- */
.sticker {{ display: flex; width: 101mm; height: 42mm; background: #fff; box-shadow: 0 0 0 .2mm #cbd5e1; position: relative; overflow: hidden; }}
.wing {{ background: #fff; flex-shrink: 0; height: 100%; display: flex; align-items: center; justify-content: center; position: relative; z-index: 20; }}
.wing-l {{ width: 7mm; border-right: .2mm dashed #94a3b8; }}
.wing-r {{ width: 3mm; }}
.wing-txt {{ writing-mode: vertical-rl; font-size: 1.600mm; color: #94a3b8; font-weight: 800; letter-spacing: 0.8mm; opacity: .8; white-space: nowrap; user-select: none; }}

.sheet {{ position: relative; width: 91mm; height: 42mm; flex-shrink: 0; overflow: hidden; color: #fff;
  background:
    radial-gradient(circle at 92% 4%, rgba(16,185,129,.35) 0, transparent 34%),
    radial-gradient(circle at 4% 98%, rgba(216,244,106,.20) 0, transparent 38%),
    linear-gradient(165deg, #06402f 0%, #032b1f 52%, #01140e 100%); }}
.blob {{ position: absolute; border-radius: 50%; z-index: 1; pointer-events: none; }}
.blob.b1 {{ width: 8mm; height: 8mm; right: -2mm; top: 4mm; background: rgba(255,209,102,.16); }}
.blob.b2 {{ width: 6mm; height: 6mm; left: -2mm; top: 16mm; background: rgba(216,244,106,.15); }}
.blob.b3 {{ width: 7mm; height: 7mm; left: 20mm; bottom: 3mm; background: rgba(16,185,129,.16); }}
.paw {{ position: absolute; inset: 0; background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='60' height='60' viewBox='0 0 60 60'><g fill='white' fill-opacity='0.045'><ellipse cx='30' cy='38' rx='9' ry='7'/><ellipse cx='17' cy='27' rx='4' ry='5.5'/><ellipse cx='25' cy='20' rx='4' ry='5.5'/><ellipse cx='35' cy='20' rx='4' ry='5.5'/><ellipse cx='43' cy='27' rx='4' ry='5.5'/></g></svg>"); background-size: 7.000mm 7.000mm; z-index: 1; pointer-events: none; }}
.bar-top, .bar-bot {{ position: absolute; left: 0; right: 0; height: 0.55mm; background: linear-gradient(90deg, #10b981, #d8f46a, #ffd166); z-index: 2; }}
.bar-top {{ top: 0; }} .bar-bot {{ bottom: 0; }}

/* 중앙 7mm 접착여백 */
.gap {{ position: absolute; top: 0; bottom: 0; left: 39.500mm; width: 7.000mm; background: #fff; z-index: 20;
  border-left: .2mm dashed #94a3b8; border-right: .2mm dashed #94a3b8; display: flex; align-items: center; justify-content: center; }}

/* 좌측 전면 (38.3mm) & 우측 후면 (43.0mm) */
.col-left {{ position: absolute; top: 1.200mm; bottom: 1.200mm; left: 0.600mm; width: 38.300mm; z-index: 5; padding: 0 0.300mm; display: flex; flex-direction: column; justify-content: space-between; }}
.col-right {{ position: absolute; top: 1.200mm; bottom: 1.200mm; left: 47.200mm; width: 43.000mm; z-index: 5; }}

/* 1) 브랜드 배지 (30ml) */
.badge {{ align-self: center; display: flex; align-items: center; justify-content: center; gap: 0.600mm;
  background: #fff; color: #06402f; box-shadow: 0 0.200mm 0 rgba(1,20,14,.35); border-radius: 999px; padding: 0.300mm 1.600mm; line-height: 1; }}
.badge .t {{ font-size: 1.150mm; font-weight: 800; letter-spacing: .04em; white-space: nowrap; }}
.badge .t b {{ color: #0e9f6e; font-weight: 900; }}
.badge svg {{ width: 1.400mm; height: 1.400mm; flex: 0 0 1.400mm; }}

/* 2) 히어로 (30ml) */
.hero {{ text-align: center; }}
.tag {{ display: inline-block; font-size: 1.200mm; font-weight: 800; color: #06402f; background: #ffd166; border-radius: 999px; padding: 0.350mm 1.500mm; letter-spacing: -.01em; line-height: 1.1; margin-bottom: 0.400mm; box-shadow: 0 0.200mm 0 rgba(1,20,14,.3); }}
.hero-row {{ display: flex; align-items: center; justify-content: center; gap: 0.800mm; }}
.pet {{ flex: 0 0 5.200mm; width: 5.200mm; height: 5.200mm; filter: drop-shadow(0 0.200mm 0 rgba(1,20,14,.3)); }}
.pet-dog {{ transform: rotate(-8deg); }}
.pet-cat {{ transform: rotate(8deg); }}
.ttl-wrap {{ display: flex; flex-direction: column; align-items: center; }}
.title {{ font-size: 5.000mm; font-weight: 900; line-height: 1; letter-spacing: -.03em; color: #fff; text-shadow: 0.250mm 0.250mm 0 #0e9f6e, 0.450mm 0.450mm 0 rgba(1,20,14,.40); margin-bottom: 0.200mm; white-space: nowrap; }}
.title sup.tm {{ font-size: 2.200mm; font-weight: 800; vertical-align: top; margin-left: 0.300mm; text-shadow: 0.200mm 0.200mm 0 #0e9f6e; }}
.sub {{ display: inline-block; font-size: 1.450mm; font-weight: 800; letter-spacing: .15em; color: #06402f; background: #bff0d6; border-radius: 999px; padding: 0.250mm 1.200mm 0.250mm calc(1.200mm + .15em); line-height: 1.1; }}
.sub sup.tm {{ font-size: 1.000mm; font-weight: 900; vertical-align: top; margin-left: 0.200mm; }}

/* 3) 핵심 효능 (30ml) */
.fx {{ position: relative; margin-top: 0.600mm; }}
.fx-tab {{ position: absolute; top: -1.100mm; left: 1.200mm; background: #d8f46a; color: #06402f; font-size: 1.150mm; font-weight: 900; padding: 0.250mm 1.100mm; border-radius: 999px; line-height: 1.1; z-index: 3; box-shadow: 0 0.150mm 0 rgba(1,20,14,.3); }}
.fx-card {{ background: #fff7e8; color: #06402f; border-radius: 1.500mm; padding: 1.100mm 1.100mm 0.800mm; display: flex; flex-direction: column; gap: 0.450mm; box-shadow: 0 0.200mm 0 rgba(1,20,14,.3); }}
.fx-item {{ display: flex; align-items: center; gap: 0.700mm; font-size: 1.280mm; font-weight: 800; line-height: 1.12; white-space: nowrap; }}
.chk {{ flex: 0 0 1.500mm; width: 1.500mm; height: 1.500mm; border-radius: 50%; background: #10b981; color: #fff; font-size: 0.950mm; font-weight: 900; display: flex; align-items: center; justify-content: center; line-height: 1; }}

/* 4) 성분 (5가지 복합체) (30ml) - 일정한 행 리듬 */
.ing {{ background: #eefdf5; color: #06402f; border-radius: 1.500mm; padding: 0.650mm 1.000mm; box-shadow: 0 0.200mm 0 rgba(1,20,14,.3); }}
.ing-h {{ display: flex; align-items: center; justify-content: space-between; padding-bottom: 0.250mm; margin-bottom: 0.350mm; border-bottom: 0.120mm dashed #a7f3d0; }}
.ing-h .ti {{ font-size: 1.180mm; font-weight: 900; }}
.ing-h .ref {{ font-size: 0.950mm; font-weight: 800; color: #fff; background: #10b981; border-radius: 999px; padding: 0.150mm 0.800mm; line-height: 1.1; }}
.row {{ display: flex; align-items: center; gap: 0.600mm; margin-bottom: 0.200mm; }}
.row:last-child {{ margin-bottom: 0; }}
.no {{ flex: 0 0 1.250mm; width: 1.250mm; height: 1.250mm; border-radius: 50%; background: #06402f; color: #fff; font-size: 0.820mm; font-weight: 900; display: flex; align-items: center; justify-content: center; line-height: 1; }}
.row:nth-child(2) .no {{ background: #10b981; }}
.row:nth-child(3) .no {{ background: #0d9488; }}
.row:nth-child(4) .no {{ background: #7c3aed; }}
.row:nth-child(5) .no {{ background: #ea580c; }}
.row:nth-child(6) .no {{ background: #db2777; }}
.rb {{ flex: 1; min-width: 0; display: flex; align-items: center; }}
.rm {{ font-size: 1.080mm; font-weight: 800; line-height: 1.15; white-space: nowrap; }}
.rm i {{ font-style: normal; color: #0e9f6e; font-weight: 800; margin-left: 0.300mm; }}

/* 5) 포장 용량 알약 (30ml) */
.pack {{ align-self: center; background: #ffd166; color: #06402f; border-radius: 999px; padding: 0.350mm 1.800mm; font-size: 1.400mm; font-weight: 900; line-height: 1; display: flex; gap: 0.500mm; align-items: center; box-shadow: 0 0.200mm 0 rgba(1,20,14,.35); }}
.pack b {{ color: #06402f; font-weight: 900; }}
.pack::before {{ content: ""; width: 1.500mm; height: 1.500mm; background: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 60 60'><g fill='%2306402f'><ellipse cx='30' cy='38' rx='11' ry='9'/><ellipse cx='13' cy='26' rx='5' ry='7'/><ellipse cx='24' cy='16' rx='5' ry='7'/><ellipse cx='36' cy='16' rx='5' ry='7'/><ellipse cx='47' cy='26' rx='5' ry='7'/></g></svg>") center / contain no-repeat; }}

/* ---------- 우측: 법정 고시 카드 (43.0mm × 39.6mm) ---------- */
.legal {{ height: 100%; background: #fff; color: #1e293b; border: 0.400mm solid #ffd166; border-radius: 1.800mm; padding: 0.500mm 0.700mm; display: flex; flex-direction: column; justify-content: space-between; }}
.lg-head {{ background: #06402f; color: #fff; border-radius: 0.900mm; padding: 0.400mm 0.700mm; display: flex; flex-direction: column; gap: 0.150mm; }}
.lg-reg {{ display: flex; justify-content: space-between; align-items: baseline; line-height: 1.1; }}
.lg-reg .l {{ font-size: 1.100mm; font-weight: 800; color: #d8f46a; }}
.lg-reg .v {{ font-size: 1.300mm; font-weight: 900; letter-spacing: .02em; color: #fff; }}
.lg-tm {{ display: flex; justify-content: space-between; font-size: 0.920mm; font-weight: 600; color: #bff0d6; border-top: 0.12mm solid rgba(255,255,255,.15); padding-top: 0.15mm; margin-top: 0.1mm; line-height: 1.1; }}
.lg-tm b {{ color: #ffd166; font-weight: 800; }}
.lg-type {{ font-size: 0.980mm; font-weight: 600; line-height: 1.12; color: #e2e8f0; }}
.lg-type b {{ color: #ffd166; font-weight: 800; }}
.lg-body {{ display: flex; flex-direction: column; gap: 0.250mm; }}
.ir {{ display: flex; align-items: baseline; font-size: 1.080mm; line-height: 1.15; padding-bottom: 0.180mm; border-bottom: 0.100mm dotted #cbd5e1; }}
.ir:last-child {{ border-bottom: none; padding-bottom: 0; }}
.ir .l {{ font-weight: 800; color: #06402f; margin-right: 0.400mm; white-space: nowrap; flex-shrink: 0; }}
.ir .v {{ flex: 1; font-weight: 600; color: #1e293b; }}
.ir .v strong {{ font-weight: 900; color: #0f172a; }}
.ef {{ list-style: none; display: flex; flex-direction: column; gap: 0.150mm; margin-top: 0.150mm; }}
.ef li {{ display: flex; align-items: baseline; gap: 0.400mm; font-size: 1.040mm; font-weight: 600; line-height: 1.12; }}
.ef .n {{ flex: 0 0 1.200mm; width: 1.200mm; height: 1.200mm; border-radius: 50%; background: #06402f; color: #fff; font-size: 0.850mm; font-weight: 900; display: flex; align-items: center; justify-content: center; line-height: 1; }}
.dose {{ background: #eefdf5; border-left: 0.600mm solid #10b981; border-radius: 0.500mm; padding: 0.350mm 0.700mm; }}
.dose .r {{ display: flex; align-items: baseline; flex-wrap: wrap; gap: 0.400mm; font-size: 1.080mm; line-height: 1.12; }}
.dose .tt {{ font-weight: 900; color: #06402f; }}
.dose .d {{ font-weight: 800; color: #0f172a; }}
.dose .s {{ font-size: 0.950mm; color: #475569; font-weight: 600; }}
.warn {{ background: #fff1f2; border: 0.150mm solid #fecdd3; border-radius: 0.700mm; padding: 0.400mm 0.700mm; }}
.warn .tt {{ display: flex; align-items: center; gap: 0.350mm; color: #be123c; font-size: 1.100mm; font-weight: 900; margin-bottom: 0.150mm; }}
.warn ul {{ list-style: none; display: flex; flex-direction: column; gap: 0.150mm; }}
.warn li {{ display: flex; gap: 0.350mm; font-size: 1.020mm; font-weight: 600; line-height: 1.12; color: #1e293b; }}
.warn li .n {{ color: #be123c; font-weight: 900; flex-shrink: 0; }}
.warn .hl {{ color: #be123c; font-weight: 900; text-decoration: underline; text-underline-offset: 0.200mm; }}
.mfg {{ background: #f1f5f9; border-radius: 999px; padding: 0.350mm 0.800mm; display: flex; justify-content: space-between; align-items: center; font-size: 1.000mm; line-height: 1.1; }}
.mfg .l {{ color: #64748b; font-weight: 700; margin-right: 0.200mm; }}
.mfg .v {{ color: #06402f; font-weight: 900; }}
.lg-foot {{ display: grid; grid-template-columns: 47% 53%; column-gap: 0.600mm; align-items: start; }}
.co-t {{ height: 2.200mm; display: flex; align-items: center; justify-content: space-between; font-size: 1.050mm; font-weight: 900; color: #06402f; line-height: 1; white-space: nowrap; }}
.co-b {{ height: 1.600mm; margin: 0.100mm 0 0.150mm; display: flex; align-items: center; }}
.co-b img {{ height: 100%; width: auto; max-width: 100%; object-fit: contain; display: block; }}
.co-n {{ font-size: 1.100mm; font-weight: 900; color: #0f172a; line-height: 1; white-space: nowrap; }}
.co-a, .co-tel {{ font-size: 0.950mm; color: #475569; line-height: 1.12; font-weight: 600; white-space: nowrap; }}
.co-tel b {{ color: #0e9f6e; font-weight: 800; }}
.rc {{ display: flex; align-items: center; gap: 0.350mm; }}
.rc .w {{ position: relative; width: 2.200mm; height: 2.200mm; display: flex; align-items: center; justify-content: center; }}
.rc svg {{ width: 100%; height: 100%; }}
.rc .x {{ position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; font-size: 0.600mm; font-weight: 900; color: #06402f; padding-top: 0.180mm; letter-spacing: -.05em; }}
.rc .o {{ font-size: 0.800mm; font-weight: 900; color: #06402f; line-height: 1; }}

@media print {{
  body.paper-a4, html.paper-a4 {{ width: 210mm !important; min-height: 297mm !important; height: 297mm !important; margin: 0 auto !important; padding: 0 !important; background: #fff !important; }}
  body.paper-a4 .a4-guide-wrapper {{ padding: 14mm 0 0 !important; box-shadow: none !important; margin: 0 auto !important; width: 210mm !important; background: #fff !important; display: flex !important; flex-direction: column !important; align-items: center !important; }}
  .no-print {{ display: none !important; }}
  body.paper-roll, html.paper-roll {{ width: 101mm !important; height: 42mm !important; margin: 0 !important; padding: 0 !important; background: transparent !important; overflow: hidden !important; }}
  body.paper-roll .a4-header-guide, body.paper-roll .a4-cut-instructions, body.paper-roll .crop-line {{ display: none !important; }}
  body.paper-roll .a4-guide-wrapper, body.paper-roll .crop-marks-box {{ padding: 0 !important; margin: 0 !important; width: 101mm !important; height: 42mm !important; }}
  .sticker {{ box-shadow: none !important; }}
}}
</style>
<style id="page-style">@page {{ size: A4 portrait; margin: 0; }}</style>
</head>
<body class="paper-a4">

<div class="no-print toolbar">
  <div><span style="color:#10b981;">★ 몬스멕타 (30ml 실측: 101mm × 42mm)</span> | [모던 · 딥그린] (좌7mm + 중7mm + 우3mm)</div>
  <div style="display:flex;gap:6px;">
    <button onclick="setPaperMode('a4')" style="background:#059669;">📄 A4 실측 (자르기 가이드)</button>
    <button onclick="setPaperMode('roll')" style="background:#1e3a2f;color:#cbd5e1;">🏷️ 롤 라벨 (101×42mm)</button>
  </div>
  <button onclick="window.print()" style="background:linear-gradient(135deg,#10b981,#047857);font-weight:800;font-size:12px;padding:6px 16px;border-radius:8px;">라벨 인쇄 (Ctrl+P)</button>
</div>

<div class="a4-guide-wrapper">
  <div class="a4-header-guide">
    <h2>[몬스멕타 30ml 정품 규격] 용기 라벨 · 모던 딥그린 (좌측 7mm + 중간 7mm + 우측 3mm 접착 = 총 101×42mm)</h2>
    <p>※ 인쇄 설정 시 반드시 <strong>[배율: 맞춤(100%)]</strong> 또는 <strong>[실제 크기(Actual Size)]</strong>로 지정하십시오.</p>
    <div class="ruler-50mm"><span>실측 확인용 눈금자:</span>
      <div class="ruler-bar"><div class="ruler-tick tick-0"></div><div class="ruler-tick tick-1"></div><div class="ruler-tick tick-2"></div><div class="ruler-tick tick-3"></div><div class="ruler-tick tick-4"></div><div class="ruler-tick tick-50"></div></div>
      <span class="ruler-note">(자로 쟀을 때 정확히 5cm)</span></div>
  </div>

  <div class="crop-marks-box">
    <div class="crop-line crop-tl-h"></div><div class="crop-line crop-tl-v"></div><div class="crop-line crop-tr-h"></div><div class="crop-line crop-tr-v"></div>
    <div class="crop-line crop-bl-h"></div><div class="crop-line crop-bl-v"></div><div class="crop-line crop-br-h"></div><div class="crop-line crop-br-v"></div>

    <div class="sticker">
      <div class="wing wing-l"><div class="wing-txt">접착 7mm</div></div>

      <div class="sheet">
        <div class="paw"></div>
        <div class="blob b1"></div><div class="blob b2"></div><div class="blob b3"></div>
        <div class="bar-top"></div><div class="bar-bot"></div>

        <!-- 좌측: 전면 (38.3mm) -->
        <div class="col-left">
          <div class="badge">
            <svg viewBox="0 0 60 60"><g fill="#0e9f6e"><ellipse cx="30" cy="38" rx="11" ry="9"/><ellipse cx="13" cy="26" rx="5" ry="7"/><ellipse cx="24" cy="16" rx="5" ry="7"/><ellipse cx="36" cy="16" rx="5" ry="7"/><ellipse cx="47" cy="26" rx="5" ry="7"/></g></svg>
            <span class="t"><b>S&amp;J</b>&nbsp;ADVANCED VET FORMULA</span>
            <svg viewBox="0 0 60 60"><g fill="#0e9f6e"><ellipse cx="30" cy="38" rx="11" ry="9"/><ellipse cx="13" cy="26" rx="5" ry="7"/><ellipse cx="24" cy="16" rx="5" ry="7"/><ellipse cx="36" cy="16" rx="5" ry="7"/><ellipse cx="47" cy="26" rx="5" ry="7"/></g></svg>
          </div>

          <div class="hero">
            <div class="tag">연변 시 장 기능 개선 및 정장 작용에 뛰어난</div>
            <div class="hero-row">
              <svg class="pet pet-dog" viewBox="0 0 40 40"><circle cx="20" cy="20" r="19" fill="#a7f3d0"/><ellipse cx="8" cy="18" rx="4.8" ry="9" fill="#b9763f" transform="rotate(14 8 18)"/><ellipse cx="32" cy="18" rx="4.8" ry="9" fill="#b9763f" transform="rotate(-14 32 18)"/><ellipse cx="20" cy="22" rx="11.5" ry="11" fill="#fff3dc"/><circle cx="14.800" cy="20" r="1.700" fill="#06402f"/><circle cx="25.200" cy="20" r="1.700" fill="#06402f"/><circle cx="15.400" cy="19.300" r=".6" fill="#fff"/><circle cx="25.800" cy="19.300" r=".6" fill="#fff"/><circle cx="11.500" cy="25" r="2" fill="#fda4af" opacity=".7"/><circle cx="28.500" cy="25" r="2" fill="#fda4af" opacity=".7"/><ellipse cx="20" cy="26" rx="5" ry="3.800" fill="#fff"/><ellipse cx="20" cy="24.200" rx="2.300" ry="1.600" fill="#06402f"/><path d="M20 25.800v1.400M20 27.200q-2 1.800-3.800 0M20 27.200q2 1.800 3.800 0" stroke="#06402f" stroke-width=".9" fill="none" stroke-linecap="round"/><path d="M18.600 28.400q1.400 3.600 2.800 0z" fill="#fb7185"/></svg>
              <div class="ttl-wrap">
                <div class="title">몬스멕타<sup class="tm">™</sup></div>
                <div class="sub en">MONSMECTA<sup class="tm">™</sup></div>
              </div>
              <svg class="pet pet-cat" viewBox="0 0 40 40"><circle cx="20" cy="20" r="19" fill="#fde68a"/><path d="M8.500 18 9.500 4.500 21 11.500z" fill="#cbd5e1"/><path d="M31.500 18 30.500 4.500 19 11.500z" fill="#cbd5e1"/><path d="M11 14 11.500 8.500 16 11.500z" fill="#fda4af"/><path d="M29 14 28.500 8.500 24 11.500z" fill="#fda4af"/><ellipse cx="20" cy="23" rx="12.500" ry="10.500" fill="#e2e8f0"/><ellipse cx="14.500" cy="21" rx="1.800" ry="2.100" fill="#06402f"/><ellipse cx="25.500" cy="21" rx="1.800" ry="2.100" fill="#06402f"/><circle cx="15.200" cy="20.200" r=".65" fill="#fff"/><circle cx="26.200" cy="20.200" r=".65" fill="#fff"/><circle cx="10.800" cy="26" r="2" fill="#fda4af" opacity=".7"/><circle cx="29.200" cy="26" r="2" fill="#fda4af" opacity=".7"/><path d="M18.500 24.600h3L20 26.200z" fill="#f472b6"/><path d="M20 26.200q-1.600 2-3.400.6M20 26.200q1.600 2 3.400.6" stroke="#06402f" stroke-width=".8" fill="none" stroke-linecap="round"/><path d="M5 23l5 1M5 27l5-1M35 23l-5 1M35 27l-5-1" stroke="#64748b" stroke-width=".6" stroke-linecap="round"/></svg>
            </div>
          </div>

          <div class="fx">
            <div class="fx-tab">핵심 효능</div>
            <div class="fx-card">
              <div class="fx-item"><span class="chk">✓</span><span>장 질환(파보·로타·코로나 등) 저항력 향상</span></div>
              <div class="fx-item"><span class="chk">✓</span><span>면역 기능 및 전신 건강 상태 유지에 도움</span></div>
              <div class="fx-item"><span class="chk">✓</span><span>장 점막 보호 및 설사·연변 정장 작용</span></div>
            </div>
          </div>

          <div class="ing">
            <div class="ing-h"><span class="ti">성분(5가지 복합체)</span><span class="ref">30ml 정품 규격</span></div>
            <div class="row"><span class="no">1</span><div class="rb">
              <div class="rm">항균 · 항바이러스 작용 <span style="font-size:0.90mm;font-weight:600;color:#2d5a47;">(DNJ/MORI 특허균주)</span></div></div></div>
            <div class="row"><span class="no">2</span><div class="rb"><div class="rm">장 기능 개선 및 정장 작용 <i>- 포도당</i></div></div></div>
            <div class="row"><span class="no">3</span><div class="rb"><div class="rm">상피세포의 회복 <i>- 비타민 A</i></div></div></div>
            <div class="row"><span class="no">4</span><div class="rb"><div class="rm">전해질제 <i>- Sodium acetate, propionate</i></div></div></div>
            <div class="row"><span class="no">5</span><div class="rb">
              <div class="rm">연변 및 설사 개선, 독소 제거 <i>- 몬모릴로나이트</i></div></div></div>
          </div>

          <div class="pack"><span>실제 중량 :</span><b>30ml</b></div>
        </div>

        <!-- 중앙 접착여백 (7mm) -->
        <div class="gap"><div class="wing-txt">접착여백 7mm</div></div>

        <!-- 우측: 법정 고시 (43.0mm) -->
        <div class="col-right"><div class="legal">
          <div class="lg-head">
            <div class="lg-reg"><span class="l">사료 성분등록번호 :</span><span class="v">제XX9UY0145호</span></div>
            <div class="lg-tm"><span><b>KR 특허상표</b> 제40-2026-0140274호</span><span><b>US USPTO</b> 50/041,096</span></div>
            <div class="lg-type"><b>명칭/용도 :</b> 보조사료/미생물제/바실러스 서브틸리스(액상)/반려동물용</div>
          </div>

          <div class="lg-body">
            <div class="ir"><span class="l">등록성분량 :</span><span class="v">바실러스 서브틸리스 1.0 x 10⁷ cfu/g 이상, 부형제</span></div>
            <div class="ir"><span class="l">원료 명칭 :</span><span class="v">바실러스 서브틸리스, 비타민A, 아세트산/프로피온산Na, 포도당, <strong>몬모릴로나이트</strong></span></div>
            <div class="ir"><span class="l">대상 :</span><span class="v">반려견, 반려묘 (모든 반려동물 및 가축)</span></div>
            <div><div class="ir" style="border:none;padding-bottom:0;"><span class="l">효과 :</span></div>
              <ul class="ef">
                <li><span class="n">1</span><span>장 질환(파보·로타·코로나 등) 저항력 향상</span></li>
                <li><span class="n">2</span><span>면역 기능 및 전신 건강 상태 유지</span></li>
                <li><span class="n">3</span><span>장 기능 개선 및 정장 작용에 도움</span></li>
              </ul></div>
          </div>

          <div class="dose">
            <div class="r"><span class="tt">용법용량 :</span><span class="d">1일 1~2ml/체중 5kg</span><span class="d">(1펌프=약 1ml)</span></div>
          </div>

          <div class="warn">
            <div class="tt"><svg width="1.60mm" height="1.60mm" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd"/></svg><span>주의사항 :</span></div>
            <ul>
              <li><span class="n">1)</span><span>직사광선 피하고 서늘한 곳 보관 / <span class="hl">반드시 흔들어서 사용</span>하십시오.</span></li>
              <li><span class="n">2)</span><span>문의 시 제조원 또는 위탁제조판매원으로 연락 바랍니다.</span></li>
            </ul>
          </div>

          <div class="mfg"><div><span class="l">중량:</span><span class="v">30ml</span></div><div><span class="l">제조:</span><span class="v">별도표기</span></div><div><span class="l">유통:</span><span class="v">18개월</span></div></div>

          <div class="lg-foot">
            <div>
              <div class="co-t"><span>위탁제조판매원 :</span></div>
              <div class="co-b"><img src="{sj_logo_b64}" alt="S&amp;J 동물병원"></div>
              <div class="co-n">에스앤제이 동물병원</div>
              <div class="co-tel">TEL : <b>031-321-6562</b></div>
            </div>
            <div>
              <div class="co-t"><span>제조원 :</span>
                <div class="rc"><div class="w"><svg viewBox="0 0 110 100"><path d="M55 6L104 88H6z" fill="none" stroke="#06402f" stroke-width="7" stroke-linejoin="round"/></svg><div class="x">OTHER</div></div><div class="o">플라스틱</div></div>
              </div>
              <div class="co-b" style="height:1.600mm;"></div>
              <div class="co-n">엠오바이오</div>
              <div class="co-tel">TEL : <b>031-458-1240</b></div>
            </div>
          </div>
        </div></div>
      </div>

      <div class="wing wing-r"><div class="wing-txt" style="writing-mode:vertical-rl;font-size:1.5mm;color:#94a3b8;font-weight:800;letter-spacing:0.8mm;">접착 3mm</div></div>
    </div>
  </div>

  <div class="a4-cut-instructions">
    ✂ 검정색 테두리 코너 재단선(Crop Marks)을 따라 칼이나 가위로 자르면 좌측 7mm, 중간 7mm, 우측 3mm 접착 여백이 포함된 총 101mm × 42mm 실측 스티커가 완성됩니다.
  </div>
</div>

<script>
function setPaperMode(mode) {{
  document.body.classList.remove('paper-a4', 'paper-roll');
  document.body.classList.add('paper-' + mode);
  document.getElementById('page-style').textContent = mode === 'roll'
    ? '@page {{ size: 101mm 42mm; margin: 0; }}'
    : '@page {{ size: A4 portrait; margin: 0; }}';
}}
</script>
</body>
</html>
"""

# 파일 저장
path_100ml = r"C:\Users\master\monsmecta_landing\public\assets\labels\monsmecta_100ml_modern.html"
path_30ml = r"C:\Users\master\monsmecta_landing\public\assets\labels\monsmecta_30ml_modern.html"

with open(path_100ml, "w", encoding="utf-8") as f:
    f.write(html_100ml)
print(f"Updated 100ml: {path_100ml}")

with open(path_30ml, "w", encoding="utf-8") as f:
    f.write(html_30ml)
print(f"Updated 30ml: {path_30ml}")
