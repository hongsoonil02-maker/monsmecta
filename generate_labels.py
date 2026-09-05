import os
import base64
import json

# 1. Base64 encode the thumbnail logo
logo_thumb_path = 'public/assets/labels/sj_logo_thumb.png'
with open(logo_thumb_path, 'rb') as f:
    logo_base64 = base64.b64encode(f.read()).decode('utf-8')
logo_src = f"data:image/png;base64,{logo_base64}"

products = {
    'hepamax': {
        'title': 'MONSMECTA HEPAMAX Label (94mm x 45mm)',
        'name_ko': '몬스멕타 헤파맥스',
        'name_en': 'MONSMECTA HEPAMAX',
        'front_subtitle': '간 기능 보호 및 해독 활성화',
        'theme': {
            'bg': 'linear-gradient(135deg, #3A0F0F 0%, #150808 50%, #0B1515 100%)',
            'border': '#8B7355',
            'primary': '#D4AF37',
            'badge_bg': 'rgba(212, 175, 55, 0.25)',
            'dose_bg': 'rgba(212, 175, 55, 0.12)'
        },
        'effects_box_title': '핵심 효능',
        'front_effects': ['간 건강 개선', '장 건강 개선', '지방간 개선', '항병력 증진', '질병 회복 촉진'],
        'effects_note': '(등의 개선에 도움)',
        'ing_box_title': '주요 성분량',
        'ing_box_ref': '1L 기준',
        'front_ingredients': [
            {'name': 'Montmorillonite (몬모릴로나이트)', 'val': '고함량'},
            {'name': 'Taurine (타우린)', 'val': '2,000mg'},
            {'name': 'D-Sorbitol (D-소르비톨)', 'val': '45g'},
            {'name': 'L-lysine HCl', 'val': '300mg'},
            {'name': 'L-methionine', 'val': '300mg'},
            {'name': 'Vitamin B1', 'val': '1,000μg'},
            {'name': '기타 식물추출물 및 부형제', 'val': '적량'}
        ],
        'reg_no': '제 XX9UY0145호',
        'feed_type': '보조사료 / 미생물제 / 바실러스 서브틸리스 / 액상 / 반려동물용',
        'reg_amount': '바실러스 서브틸리스 1.0 x 10⁷ cfu/g 이상, 부형제(정제수)',
        'raw_materials': '바실러스 서브틸리스, 비타민A, 아세트산나트륨, 프로피온산나트륨, 포도당, 정제수',
        'target_species': '반려견 · 반려묘',
        'effect_summary': '장 질환 저항력 향상, 면역 유지, 정장 작용 등에 도움',
        'dosage_main': '1일 1~2ml / 체중 5kg',
        'dosage_sub': '(1펌프=약 1ml, 증상별 조절)',
        'mfg_date': '2026. 09. 15',
        'exp_date': '제조일로부터 18개월'
    },
    'renal': {
        'title': 'MONSMECTA RENAL DETOX Label (94mm x 45mm)',
        'name_ko': '몬스멕타 레날 디톡스',
        'name_en': 'MONSMECTA RENAL DETOX',
        'front_subtitle': '비뇨기 및 신장 건강 보조제',
        'theme': {
            'bg': 'linear-gradient(135deg, #120A2B 0%, #0A081C 50%, #08111A 100%)',
            'border': '#584288',
            'primary': '#818cf8',
            'badge_bg': 'rgba(129, 140, 248, 0.25)',
            'dose_bg': 'rgba(129, 140, 248, 0.12)'
        },
        'effects_box_title': '핵심 효능',
        'front_effects': ['요소(Urea) 및 요독 배출 촉진', '인독실설페이트 흡착 제거', '신장 수치 안정화 보조', '활력 증진 및 에너지 대사'],
        'effects_note': '(등의 개선에 도움)',
        'ing_box_title': '주요 성분량',
        'ing_box_ref': '1L 기준',
        'front_ingredients': [
            {'name': 'Montmorillonite (몬모릴로나이트)', 'val': '고함량'},
            {'name': 'Lactobacillus Longum', 'val': '1.0 x 10⁶ cfu/g'},
            {'name': '비타민 A (Vitamin A)', 'val': '400,000 IU'},
            {'name': '비타민 D3 (Vitamin D3)', 'val': '80,000 IU'},
            {'name': '비타민 E (Vitamin E)', 'val': '200 IU'},
            {'name': '기타 식물추출물 및 부형제', 'val': '적량'}
        ],
        'reg_no': '제 XX9UY0145호',
        'feed_type': '보조사료 / 미생물제 / 바실러스 서브틸리스 / 액상 / 반려동물용',
        'reg_amount': '바실러스 서브틸리스 1.0 x 10⁷ cfu/g 이상, 부형제(정제수)',
        'raw_materials': '바실러스 서브틸리스, 비타민A, 아세트산나트륨, 프로피온산나트륨, 포도당, 정제수',
        'target_species': '반려견 · 반려묘',
        'effect_summary': '장 질환 저항력 향상, 면역 유지, 정장 작용 등에 도움',
        'dosage_main': '1일 1~2ml / 체중 5kg',
        'dosage_sub': '(1펌프=약 1ml, 증상별 조절)',
        'mfg_date': '2026. 09. 15',
        'exp_date': '제조일로부터 18개월'
    },
    'original': {
        'title': 'MONSMECTA ORIGINAL Label (94mm x 45mm)',
        'name_ko': '몬스멕타 오리지널',
        'name_en': 'MONSMECTA ORIGINAL',
        'front_subtitle': '장 기능 개선 및 정장 작용에 도움되는',
        'theme': {
            'bg': 'linear-gradient(135deg, #023828 0%, #012218 50%, #03141b 100%)',
            'border': '#065f46',
            'primary': '#10b981',
            'badge_bg': 'rgba(16, 185, 129, 0.25)',
            'dose_bg': 'rgba(16, 185, 129, 0.12)'
        },
        'effects_box_title': '핵심 성분 복합 효과',
        'front_effects': ['항균·항바이러스 특허균주 작용', '상피세포 신속 회복 보조', '전해질 밸런스 균형 공급', '곰팡이 독소 제거 & 연변 개선'],
        'effects_note': '(면역증강 및 장 환경 개선에 도움)',
        'ing_box_title': '핵심 5가지 복합체',
        'ing_box_ref': 'Veterinary Formula',
        'front_ingredients': [
            {'name': '고초균 (Bacillus subtilis MORI)', 'val': '특허 제201188042602.8호'},
            {'name': '고순도 초미세 몬모릴로나이트', 'val': '연변/설사개선·독소흡착'},
            {'name': '비타민 A (Vitamin A)', 'val': '상피 세포 회복'},
            {'name': '전해질제재 (Na-Acetate/Propionate)', 'val': '전해질 균형'},
            {'name': '포도당 (Glucose) & 부형제', 'val': '정장작용·에너지공급'}
        ],
        'reg_no': '제 XX9UY0145호',
        'feed_type': '보조사료 / 미생물제 / 바실러스 서브틸리스 / 액상 / 반려동물용',
        'reg_amount': '바실러스 서브틸리스 1.0 x 10⁷ cfu/g 이상, 부형제(정제수)',
        'raw_materials': '바실러스 서브틸리스, 비타민A, 아세트산나트륨, 프로피온산나트륨, 포도당, 정제수',
        'target_species': '반려견 · 반려묘',
        'effect_summary': '장 질환 저항력 향상, 면역 유지, 정장 작용 등에 도움',
        'dosage_main': '1일 1~2ml / 체중 5kg',
        'dosage_sub': '(1펌프=약 1ml, 증상별 조절)',
        'mfg_date': '별도표기',
        'exp_date': '제조일로부터 18개월'
    }
}

def get_html(product_key, data):
    theme = data['theme']
    
    # Left front ingredients list
    ing_rows = ""
    for item in data['front_ingredients']:
        val_sub = f"<span class='sub-val'>{item.get('sub', '')}</span>" if item.get('sub') else ""
        ing_rows += f"""
        <div class="ing-row">
            <span class="ing-name">{item['name']}</span>
            <span class="ing-val">{item['val']} {val_sub}</span>
        </div>
        """
        
    effects_items = "".join([f"<li><span class='bullet-dot'></span><span>{eff}</span></li>" for eff in data['front_effects']])
    
    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>{data['title']}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;800;900&family=Orbitron:wght@700;900&display=swap" rel="stylesheet">
    <style>
        @page {{
            size: 94mm 45mm;
            margin: 0mm;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
            word-break: keep-all;
            overflow-wrap: break-word;
        }}

        html, body {{
            width: 94mm;
            height: 45mm;
            margin: 0;
            padding: 0;
            overflow: hidden;
            background: #000;
            font-family: 'Noto Sans KR', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }}

        .orbitron {{
            font-family: 'Orbitron', sans-serif;
        }}

        /* Exact Label Physical Dimensions: 94mm x 45mm */
        .label-sheet {{
            width: 94mm;
            height: 45mm;
            background: {theme['bg']};
            color: #f1f5f9;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            border: 0.3mm solid {theme['border']};
        }}

        /* High-tech tech grid pattern */
        .grid-overlay {{
            position: absolute;
            inset: 0;
            opacity: 0.10;
            background-image: 
                linear-gradient({theme['primary']} 1px, transparent 1px),
                linear-gradient(90deg, {theme['primary']} 1px, transparent 1px);
            background-size: 3.5mm 3.5mm;
            pointer-events: none;
            z-index: 1;
        }}

        /* Accent top glow bar */
        .top-accent-bar {{
            height: 0.8mm;
            background: {theme['primary']};
            box-shadow: 0 0 1.5mm {theme['primary']};
            z-index: 2;
            flex-shrink: 0;
        }}

        /* Main Content Container (Height: 44.2mm) */
        .content-wrap {{
            position: relative;
            z-index: 2;
            display: flex;
            height: calc(45mm - 0.8mm);
            width: 94mm;
            padding: 0.8mm 1.8mm 0.8mm 1.8mm;
            justify-content: space-between;
        }}

        /* Left Side: Front View (Width: 42.5mm) */
        .col-left {{
            width: 42.5mm;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}

        /* Center Divider (Width: 1.0mm) */
        .divider-col {{
            width: 1.0mm;
            height: 100%;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .divider-line {{
            width: 0.25mm;
            height: 94%;
            background: linear-gradient(180deg, transparent, {theme['primary']}, transparent);
            opacity: 0.6;
        }}
        .divider-diamond {{
            position: absolute;
            width: 1.5mm;
            height: 1.5mm;
            background: #000;
            border: 0.25mm solid {theme['primary']};
            transform: rotate(45deg);
        }}

        /* Right Side: Back Legal Notice View (Width: 46.5mm) */
        .col-right {{
            width: 46.5mm;
            height: 100%;
            display: flex;
            flex-direction: column;
        }}

        /* Brand badge */
        .brand-badge {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 1.2mm;
            background: rgba(0, 0, 0, 0.45);
            border: 0.18mm solid {theme['primary']};
            border-radius: 999px;
            padding: 0.35mm 1.5mm;
            line-height: 1;
            box-sizing: border-box;
        }}
        .brand-badge .emoji {{
            font-size: 2.55mm;
            line-height: 1;
            display: inline-flex;
            align-items: center;
            justify-content: center;
        }}
        .brand-badge .text {{
            font-size: 1.35mm;
            font-weight: 800;
            letter-spacing: 0.04em;
            color: #e2e8f0;
            line-height: 1;
            display: inline-flex;
            align-items: center;
        }}
        .brand-badge .accent {{
            color: {theme['primary']};
        }}

        /* Hero Section */
        .hero-section {{
            text-align: center;
            padding: 0.05mm 0;
        }}
        .sub-desc {{
            font-size: 1.4mm;
            font-weight: 600;
            color: #cbd5e1;
            line-height: 1.1;
            margin-bottom: 0.1mm;
        }}
        .main-title {{
            font-size: 3.0mm;
            font-weight: 900;
            color: #ffffff;
            line-height: 1.05;
            letter-spacing: -0.02em;
            text-shadow: 0 0 1.2mm rgba(255,255,255,0.4);
            margin-bottom: 0.1mm;
        }}
        .en-title {{
            font-size: 1.6mm;
            font-weight: 800;
            color: {theme['primary']};
            letter-spacing: 0.08em;
            line-height: 1;
        }}

        /* Left side tech box */
        .tech-box {{
            background: rgba(0, 0, 0, 0.42);
            border: 0.18mm solid rgba(255, 255, 255, 0.14);
            border-radius: 0.9mm;
            padding: 0.45mm 0.9mm;
            position: relative;
        }}
        .box-badge {{
            position: absolute;
            top: -1.35mm;
            left: 1.5mm;
            background: {theme['badge_bg']};
            border: 0.15mm solid {theme['primary']};
            border-radius: 0.3mm;
            padding: 0.22mm 0.8mm;
            font-size: 1.15mm;
            font-weight: 800;
            color: {theme['primary']};
            line-height: 1;
            box-shadow: 0 0.2mm 0.5mm rgba(0, 0, 0, 0.6);
            display: inline-flex;
            align-items: center;
            justify-content: center;
            box-sizing: border-box;
        }}

        /* Core Effects list */
        .effects-list {{
            list-style: none;
            display: flex;
            flex-wrap: wrap;
            gap: 0.25mm 1.1mm;
            margin-top: 0.45mm;
            padding-top: 0.15mm;
        }}
        .effects-list li {{
            font-size: 1.3mm;
            font-weight: 700;
            color: #f1f5f9;
            display: flex;
            align-items: center;
            gap: 0.5mm;
            line-height: 1.15;
        }}
        .bullet-dot {{
            width: 0.65mm;
            height: 0.65mm;
            border-radius: 50%;
            background: {theme['primary']};
            box-shadow: 0 0 0.4mm {theme['primary']};
            flex-shrink: 0;
        }}
        .effects-note {{
            font-size: 1.05mm;
            color: {theme['primary']};
            opacity: 0.85;
            font-weight: 500;
            margin-top: 0.1mm;
            text-align: right;
        }}

        /* Ingredients Table */
        .ing-header {{
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            border-bottom: 0.12mm solid rgba(255, 255, 255, 0.2);
            padding-bottom: 0.15mm;
            margin-bottom: 0.2mm;
        }}
        .ing-header .title {{
            font-size: 1.35mm;
            font-weight: 800;
            color: #fff;
        }}
        .ing-header .ref {{
            font-size: 1.1mm;
            color: {theme['primary']};
            font-weight: 700;
        }}
        .ing-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 1.18mm;
            line-height: 1.18;
            border-bottom: 0.08mm solid rgba(255, 255, 255, 0.06);
            padding: 0.08mm 0;
        }}
        .ing-row:last-child {{
            border-bottom: none;
        }}
        .ing-name {{
            font-weight: 700;
            color: #e2e8f0;
        }}
        .ing-val {{
            font-weight: 800;
            color: #cbd5e1;
            font-family: 'Orbitron', 'Noto Sans KR', sans-serif;
            font-size: 1.12mm;
        }}
        .ing-val .sub-val {{
            font-size: 0.9mm;
            color: {theme['primary']};
            opacity: 0.9;
            margin-left: 0.4mm;
            font-family: 'Noto Sans KR', sans-serif;
        }}

        /* Pack volume tag */
        .pack-tag {{
            align-self: center;
            background: rgba(0, 0, 0, 0.5);
            border: 0.18mm solid {theme['primary']};
            border-radius: 999px;
            padding: 0.38mm 1.8mm;
            font-size: 1.3mm;
            font-weight: 800;
            display: flex;
            gap: 0.7mm;
            align-items: center;
            justify-content: center;
            line-height: 1;
            box-sizing: border-box;
        }}
        .pack-tag .val {{
            color: {theme['primary']};
            font-weight: 900;
        }}

        /* RIGHT PANEL: Statutory Notice Details */
        .legal-panel {{
            background: rgba(0, 0, 0, 0.48);
            border: 0.18mm solid rgba(255, 255, 255, 0.15);
            border-radius: 0.9mm;
            height: 100%;
            padding: 0.6mm 1.1mm 0.5mm 1.1mm;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}

        .legal-header {{
            border-bottom: 0.12mm solid rgba(255, 255, 255, 0.18);
            padding-bottom: 0.3mm;
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
        }}
        .reg-left {{
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
        }}
        .reg-num-label {{
            font-size: 0.95mm;
            color: {theme['primary']};
            font-weight: 800;
            line-height: 1;
            margin-bottom: 0.2mm;
        }}
        .reg-num-val {{
            font-size: 1.22mm;
            font-weight: 800;
            color: #fff;
            line-height: 1;
        }}
        .feed-type-val {{
            font-size: 1.05mm;
            font-weight: 700;
            color: #e2e8f0;
            line-height: 1;
            text-align: right;
            white-space: nowrap;
        }}

        /* Section rows: giving 1 extra line of comfortable breathing space */
        .sec-rows-container {{
            display: flex;
            flex-direction: column;
            gap: 0.95mm;
            margin: 0.8mm 0 1.0mm 0;
        }}
        .sec-row {{
            line-height: 1.25;
            display: flex;
            align-items: baseline;
        }}
        .sec-label {{
            font-size: 0.98mm;
            font-weight: 800;
            color: {theme['primary']};
            white-space: nowrap;
            margin-right: 0.6mm;
            flex-shrink: 0;
        }}
        .sec-val {{
            font-size: 1.02mm;
            font-weight: 600;
            color: #e2e8f0;
            line-height: 1.25;
        }}
        .sec-val-highlight {{
            color: #ffffff;
            font-weight: 700;
        }}

        /* Single-line compact Dose callout box with balanced vertical padding */
        .dose-box {{
            background: {theme['dose_bg']};
            border: 0.15mm solid {theme['primary']};
            border-radius: 0.5mm;
            padding: 0.55mm 1.0mm;
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            align-items: center;
            white-space: nowrap;
            overflow: hidden;
            line-height: 1;
            box-sizing: border-box;
        }}
        .dose-left {{
            display: inline-flex;
            align-items: center;
            gap: 0.6mm;
            line-height: 1;
        }}
        .dose-title {{
            font-size: 1.05mm;
            font-weight: 800;
            color: {theme['primary']};
            line-height: 1;
            display: inline-flex;
            align-items: center;
        }}
        .dose-desc {{
            font-size: 1.15mm;
            font-weight: 800;
            color: #ffffff;
            line-height: 1;
            display: inline-flex;
            align-items: center;
        }}
        .dose-sub {{
            font-size: 0.92mm;
            color: #cbd5e1;
            font-weight: 500;
            line-height: 1;
            display: inline-flex;
            align-items: center;
        }}

        /* Warnings box with balanced vertical padding and item margins */
        .warn-box {{
            background: rgba(220, 38, 38, 0.12);
            border: 0.12mm solid rgba(239, 68, 68, 0.4);
            border-radius: 0.5mm;
            padding: 0.55mm 0.9mm 0.55mm 0.9mm;
            box-sizing: border-box;
        }}
        .warn-title {{
            font-size: 0.98mm;
            font-weight: 800;
            color: #f87171;
            display: flex;
            align-items: center;
            gap: 0.4mm;
            line-height: 1;
            margin-bottom: 0.18mm;
        }}
        .warn-list {{
            list-style: square inside;
            font-size: 0.92mm;
            color: #e2e8f0;
            line-height: 1.25;
            font-weight: 500;
        }}
        .warn-list li {{
            margin-bottom: 0.1mm;
        }}
        .warn-list li:last-child {{
            margin-bottom: 0;
        }}
        .warn-list strong {{
            color: #fff;
            font-weight: 700;
        }}
        .warn-list .hl-shake {{
            color: {theme['primary']};
            text-decoration: underline;
            text-decoration-thickness: 0.12mm;
            text-underline-offset: 0.15mm;
            font-weight: 800;
        }}

        /* MFG & EXP Bar with balanced vertical padding */
        .mfg-exp-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.95mm;
            font-weight: 700;
            border-top: 0.12mm solid rgba(255, 255, 255, 0.15);
            border-bottom: 0.12mm solid rgba(255, 255, 255, 0.15);
            padding: 0.38mm 0.5mm;
            color: #cbd5e1;
            line-height: 1;
            box-sizing: border-box;
        }}
        .mfg-exp-bar .label {{
            color: #94a3b8;
            margin-right: 0.4mm;
            display: inline-flex;
            align-items: center;
        }}
        .mfg-exp-bar .val {{
            color: #fff;
            display: inline-flex;
            align-items: center;
        }}

        /* Manufacturer & Seller footer */
        .legal-footer {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-top: 0.18mm;
            gap: 0.5mm;
        }}
        .company-block {{
            display: flex;
            align-items: center;
            gap: 0.5mm;
        }}
        .company-logo-circle {{
            width: 3.5mm;
            height: 3.5mm;
            border-radius: 50%;
            background: #fff;
            border: 0.18mm solid {theme['primary']};
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            flex-shrink: 0;
            box-shadow: 0 0 0.8mm {theme['primary']};
        }}
        .company-logo-circle img {{
            width: 100%;
            height: 100%;
            object-fit: contain;
            padding: 0.1mm;
        }}
        .company-info {{
            font-size: 0.85mm;
            color: #cbd5e1;
            line-height: 1.15;
        }}
        .company-info .co-title {{
            font-weight: 800;
            color: #fff;
            font-size: 0.9mm;
        }}
        .company-info .tel-accent {{
            color: {theme['primary']};
            font-weight: 800;
        }}

        .recycle-block {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: {theme['primary']};
            flex-shrink: 0;
            padding-left: 0.3mm;
        }}
        .recycle-icon-wrap {{
            width: 3.2mm;
            height: 3.2mm;
            position: relative;
        }}
        .recycle-icon {{
            width: 100%;
            height: 100%;
        }}
        .recycle-text {{
            position: absolute;
            inset: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.75mm;
            font-weight: 900;
            color: #ffffff;
            padding-top: 0.45mm;
            letter-spacing: -0.05em;
        }}
        .recycle-sub {{
            font-size: 0.78mm;
            font-weight: 900;
            color: #fff;
            letter-spacing: 0.05em;
            line-height: 1;
            margin-top: 0.1mm;
        }}

        /* Print media settings */
        @media print {{
            html, body {{
                background: none !important;
                width: 94mm !important;
                height: 45mm !important;
            }}
            .label-sheet {{
                border: none !important;
                width: 94mm !important;
                height: 45mm !important;
            }}
        }}
    </style>
</head>
<body>

<div class="label-sheet">
    <div class="grid-overlay"></div>
    <div class="top-accent-bar"></div>

    <div class="content-wrap">
        <!-- LEFT COLUMN (Front View) -->
        <div class="col-left">
            <!-- Brand Badge -->
            <div class="brand-badge">
                <span class="emoji">🐶</span>
                <span class="text"><span class="accent">S&J</span>&nbsp;ADVANCED VET FORMULA</span>
                <span class="emoji">🐱</span>
            </div>

            <!-- Hero Title -->
            <div class="hero-section">
                <div class="sub-desc">{data['front_subtitle']}</div>
                <h1 class="main-title">{data['name_ko']}</h1>
                <h2 class="en-title orbitron">{data['name_en']}</h2>
            </div>

            <!-- Core Effects Box -->
            <div class="tech-box">
                <div class="box-badge">{data['effects_box_title']}</div>
                <ul class="effects-list">
                    {effects_items}
                </ul>
                <div class="effects-note">* {data['effects_note']}</div>
            </div>

            <!-- Ingredients Table -->
            <div class="tech-box">
                <div class="ing-header">
                    <span class="title">{data['ing_box_title']}</span>
                    <span class="ref">{data['ing_box_ref']}</span>
                </div>
                {ing_rows}
            </div>

            <!-- Pack size -->
            <div class="pack-tag">
                <span>포장단위:</span>
                <span class="val">30 ml / 병</span>
            </div>
        </div>

        <!-- CENTER DIVIDER -->
        <div class="divider-col">
            <div class="divider-line"></div>
            <div class="divider-diamond"></div>
        </div>

        <!-- RIGHT COLUMN (Statutory Notice View) -->
        <div class="col-right">
            <div class="legal-panel">
                <!-- Header (Reg No & Type in same baseline row) -->
                <div class="legal-header">
                    <div class="reg-left">
                        <div class="reg-num-label">사료 성분등록번호</div>
                        <div class="reg-num-val">{data['reg_no']}</div>
                    </div>
                    <div class="feed-type-val">{data['feed_type']}</div>
                </div>

                <!-- Registration Spec / Raw materials / Species & Effects (tight spacing) -->
                <div class="sec-rows-container">
                    <!-- Registration Spec -->
                    <div class="sec-row">
                        <span class="sec-label">등록성분량:</span>
                        <span class="sec-val sec-val-highlight">{data['reg_amount']}</span>
                    </div>

                    <!-- Raw Materials (사용한 원료의 명칭) -->
                    <div class="sec-row">
                        <span class="sec-label">사용한 원료의 명칭:</span>
                        <span class="sec-val">{data['raw_materials']}</span>
                    </div>

                    <!-- Target Species & Effect -->
                    <div class="sec-row" style="justify-content:space-between;">
                        <div style="display:flex; align-items:baseline;">
                            <span class="sec-label">대상축종:</span>
                            <span class="sec-val sec-val-highlight">{data['target_species']}</span>
                        </div>
                        <div style="display:flex; align-items:baseline;">
                            <span class="sec-label">효과:</span>
                            <span class="sec-val">{data['effect_summary']}</span>
                        </div>
                    </div>
                </div>

                <!-- Dosage & Usage Box (Single-line compact) -->
                <div class="dose-box">
                    <div class="dose-left">
                        <span class="dose-title">용법·용량:</span>
                        <span class="dose-desc">{data['dosage_main']}</span>
                    </div>
                    <span class="dose-sub">{data['dosage_sub']}</span>
                </div>

                <!-- Precautions Warning Box -->
                <div class="warn-box">
                    <div class="warn-title">
                        <svg width="2.2mm" height="2.2mm" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd"></path></svg>
                        <span>주의사항</span>
                    </div>
                    <ul class="warn-list">
                        <li>직사광선을 피하여 <strong>건조하고 서늘한 곳에 보관</strong>하십시오.</li>
                        <li>제품 특성 상 가라앉는 성분이 있어 <span class="hl-shake">흔들어서 사용</span>하십시오.</li>
                        <li>문의사항은 제조원 또는 판매원으로 연락해 주시기 바랍니다.</li>
                    </ul>
                </div>

                <!-- MFG / EXP -->
                <div class="mfg-exp-bar">
                    <div><span class="label">제조일자:</span><span class="val">{data['mfg_date']}</span></div>
                    <div><span class="label">유통기한:</span><span class="val">{data['exp_date']}</span></div>
                    <div><span class="label">포장:</span><span class="val">30ml</span></div>
                </div>

                <!-- Footer: Seller & Manufacturer & Recycle Mark -->
                <div class="legal-footer">
                    <!-- Seller -->
                    <div class="company-block">
                        <div class="company-logo-circle">
                            <img src="{logo_src}" alt="S&J">
                        </div>
                        <div class="company-info">
                            <div class="co-title">판매원: 에스앤제이 동물병원</div>
                            <div>용인시 처인구 포곡읍 선장1로 98-8</div>
                            <div><span class="tel-accent">TEL:</span> 031-321-6562</div>
                        </div>
                    </div>

                    <!-- Manufacturer -->
                    <div class="company-info" style="border-left: 0.15mm solid rgba(255,255,255,0.15); padding-left: 0.6mm;">
                        <div class="co-title">제조원: ㈜엠오바이오</div>
                        <div>화성시 팔탄면 석포로 74번길 10-25</div>
                        <div><span class="tel-accent">TEL:</span> 031-458-1240</div>
                    </div>

                    <!-- Recycling info -->
                    <div class="recycle-block">
                        <div class="recycle-icon-wrap">
                            <svg viewBox="0 0 100 100" class="recycle-icon" stroke="currentColor" stroke-width="6" fill="none" stroke-linejoin="round" stroke-linecap="round">
                                <path d="M50 12 L88 78 L12 78 Z"/>
                                <path d="M50 12 L60 22 M88 78 L73 78 M12 78 L22 63" />
                            </svg>
                            <div class="recycle-text">플라스틱</div>
                        </div>
                        <div class="recycle-sub">OTHER</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

</body>
</html>
"""
    return html

# 2. Output HTML files
output_dir = 'public/assets/labels'
html_files = {}
for key, data in products.items():
    filename = f"monsmecta_{key}_30ml_94x45.html"
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(get_html(key, data))
    html_files[key] = filepath
    print(f"Generated HTML: {filepath}")

print("HTML generation completed!")
