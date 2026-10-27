import os
import json

out_dir = r"c:\Users\master\monsmecta_landing\public\assets\labels"
os.makedirs(out_dir, exist_ok=True)

with open(r"scripts/extracted_logo_b64.txt", encoding="utf-8") as f:
    LOGO_B64 = f.read().strip()

PRODUCTS = [
    {
        "id": "monsmecta",
        "file_name": "monsmecta_original_label.html",
        "name_ko": "몬스멕타",
        "name_en": "MONSMECTA",
        "sub_desc": "연변 시 장 기능 개선 및 정장 작용에 뛰어난",
        "neon": "#10b981",
        "neon_sub": "#34d399",
        "neon_pale": "#a7f3d0",
        "border": "#059669",
        "bg_gradient": "linear-gradient(135deg, #022319 0%, #01140e 50%, #030a08 100%)",
        "top_bar": "linear-gradient(90deg, #059669, #10b981, #6ee7b7, #059669)",
        "front_effects": [
            ("장 관련 질환 저항력 향상", "면역 기능 및 건강 상태 유지"),
            ("장 기능 개선 및 정장 작용", None, "(*등의 개선에 도움)")
        ],
        "ingredients_header_ref": "100ml / 30ml 공용",
        "ingredients": [
            ("Bacillus subtilis (고초균)", "항균·항바이러스 작용"),
            ("Glucose (포도당)", "장 기능 개선 및 정장 작용"),
            ("Vitamin A (비타민 A)", "상피세포의 회복"),
            ("Sodium acetate, Sodium propionate", "전해질 보충"),
            ("Montmorillonite (몬모릴로나이트)", "연변/설사 개선, 독소 제거"),
            ("기타 식물추출물 및 부형제", "적량")
        ],
        "reg_no": "제 XX9UY0145호",
        "feed_type": "보조사료/미생물제/바실러스 서브틸리스l액상l반려동물",
        "reg_ing": "바실러스 서브틸리스 1.0 x 10⁶ cfu/g 이상, 부형제( 정제수 )",
        "raw_mat_lines": [
            "바실러스 서브틸리스, 비타민A, 아세트산 나트륨,",
            "프로피온산 나트륨, 포도당, 몬모릴로나이트, 정제수"
        ],
        "target": "반려견, 반려묘",
        "statutory_effects": [
            "장 관련 질병( 파보, 로타, 코로나 등 )에 대한 저항력 향상에 도움",
            "면역 기능 및 건강 상태 유지에 도움",
            "장 기능 개선 및 정장 작용에 도움"
        ],
        "dosage_desc": "1일 1~2ml / 체중 5kg",
        "dosage_sub": "( 1 펌프 = 약 1ml ) - 증상에 따라 조절 가능"
    },
    {
        "id": "hepamax",
        "file_name": "monsmecta_hepamax_label.html",
        "name_ko": "몬스멕타 헤파맥스",
        "name_en": "MONSMECTA HEPAMAX",
        "sub_desc": "간 기능 보호 및 해독 활성화 보조제",
        "neon": "#ffd700",
        "neon_sub": "#fbbf24",
        "neon_pale": "#fef08a",
        "border": "#d97706",
        "bg_gradient": "linear-gradient(135deg, #2a1205 0%, #150802 50%, #0d0c05 100%)",
        "top_bar": "linear-gradient(90deg, #b45309, #f59e0b, #fef08a, #b45309)",
        "front_effects": [
            ("간 건강 개선", "지방간 개선"),
            ("장 건강 개선", "항병력 증진", "(*등의 개선에 도움)")
        ],
        "ingredients_header_ref": "1L 기준",
        "ingredients": [
            ("Montmorillonite (몬모릴로나이트)", "고함량"),
            ("Monsmecta Original 베이스 배합", "핵심 원료"),
            ("Taurine (타우린)", "200mg"),
            ("D-Sorbitol (D-소르비톨)", "4.5mg"),
            ("L-lysine HCl", "30mg"),
            ("L-methionine", "30mg"),
            ("Vitamin B12", "100μg")
        ],
        "reg_no": "제 XX9UY0145호",
        "feed_type": "보조사료/미생물제/바실러스 서브틸리스l액상l반려동물",
        "reg_ing": "바실러스 서브틸리스 1.0 x 10⁶ cfu/g 이상, 부형제( 정제수 )",
        "raw_mat_lines": [
            "바실러스 서브틸리스, 비타민A, 아세트산나트륨, 프로피온산나트륨,",
            "포도당, 몬모릴로나이트, 타우린, D-소르비톨, L-라이신, 메티오닌, 정제수"
        ],
        "target": "반려견, 반려묘",
        "statutory_effects": [
            "간 기능 보호 및 지방간 개선에 도움",
            "장 건강 개선 및 체내 독소 배출 보조",
            "항병력 증진 및 질병 회복 촉진에 도움"
        ],
        "dosage_desc": "1일 1~2ml / 체중 5kg",
        "dosage_sub": "( 1 펌프 = 약 1ml ) - 증상에 따라 조절 가능"
    },
    {
        "id": "urinary",
        "file_name": "monsmecta_renal_label.html",
        "name_ko": "몬스멕타 레날 디톡스",
        "name_en": "MONSMECTA RENAL DETOX",
        "sub_desc": "비뇨기 및 신장 건강 보조제",
        "neon": "#818cf8",
        "neon_sub": "#a5b4fc",
        "neon_pale": "#c7d2fe",
        "border": "#6366f1",
        "bg_gradient": "linear-gradient(135deg, #180b2d 0%, #0b071a 50%, #050d14 100%)",
        "top_bar": "linear-gradient(90deg, #6366f1, #818cf8, #a5b4fc, #6366f1)",
        "front_effects": [
            ("요소(Urea) 및 요독 배출 촉진", "인독실설페이트 흡착 제거"),
            ("신장 수치 안정화 보조", "활력 증진 및 에너지 대사", "(*등의 개선에 도움)")
        ],
        "ingredients_header_ref": "1L 기준",
        "ingredients": [
            ("Montmorillonite (몬모릴로나이트)", "고함량"),
            ("Bifidobacterium longum", "1.0 x 10¹¹ cfu"),
            ("비타민 A (Vitamin A)", "400,000 IU"),
            ("비타민 D3 (Vitamin D3)", "80,000 IU"),
            ("비타민 E (Vitamin E)", "200 IU"),
            ("기타 식물추출물 및 부형제", "적량")
        ],
        "reg_no": "제 XX9UY0145호",
        "feed_type": "보조사료/미생물제/바실러스 서브틸리스l액상l반려동물",
        "reg_ing": "바실러스 서브틸리스 1.0 x 10⁶ cfu/g 이상, 부형제( 정제수 )",
        "raw_mat_lines": [
            "바실러스 서브틸리스, 비타민A, 아세트산 나트륨,",
            "프로피온산 나트륨, 포도당, 정제수"
        ],
        "target": "반려견, 반려묘",
        "statutory_effects": [
            "장 관련 질병( 파보, 로타, 코로나 등 )에 대한 저항력 향상에 도움",
            "면역 기능 및 건강 상태 유지에 도움",
            "장 기능 개선 및 정장 작용에 도움"
        ],
        "dosage_desc": "1일 1~2ml / 체중 5kg",
        "dosage_sub": "( 1 펌프 = 약 1ml ) - 증상에 따라 조절 가능"
    },
    {
        "id": "cancercare",
        "file_name": "monsmecta_cancercare_label.html",
        "name_ko": "몬스멕타 캔서케어",
        "name_en": "MONSMECTA CANCERCARE",
        "sub_desc": "면역 증진 및 종양 억제 보조제",
        "neon": "#c084fc",
        "neon_sub": "#d8b4fe",
        "neon_pale": "#f3e8ff",
        "border": "#9333ea",
        "bg_gradient": "linear-gradient(135deg, #24082e 0%, #14041a 50%, #0a040f 100%)",
        "top_bar": "linear-gradient(90deg, #9333ea, #c084fc, #e9d5ff, #9333ea)",
        "front_effects": [
            ("강력한 면역 세포 활성화", "종양 억제 보조 기전"),
            ("항암 치료 부작용 완화", "염증 반응 감소", "(*등의 개선에 도움)")
        ],
        "ingredients_header_ref": "1L 기준",
        "ingredients": [
            ("Montmorillonite (독소 흡착)", "고함량"),
            ("Beta-glucan (베타글루칸)", "30,000mg"),
            ("Allicin (알리신)", "20,000mg"),
            ("Sulforaphane (설포라판)", "20,000mg"),
            ("Curcumin (커큐민)", "10,000mg"),
            ("Catechin (카테킨)", "10,000mg"),
            ("AFNC (천연복합추출물)", "10,000mg")
        ],
        "reg_no": "제 XX9UY0145호",
        "feed_type": "보조사료/미생물제/바실러스 서브틸리스l액상l반려동물",
        "reg_ing": "바실러스 서브틸리스 1.0 x 10⁶ cfu/g 이상, 부형제( 정제수 )",
        "raw_mat_lines": [
            "바실러스 서브틸리스, 베타글루칸, 알리신, 설포라판,",
            "커큐민, 카테킨, AFNC(천연복합추출물), 정제수"
        ],
        "target": "반려견, 반려묘",
        "statutory_effects": [
            "강력한 면역 세포 활성화 및 항병력 강화",
            "종양 억제 보조 기전 및 세포 건강 유지",
            "항암 치료 시 부작용 완화 및 염증 반응 억제에 도움"
        ],
        "dosage_desc": "1일 1~2ml / 체중 5kg",
        "dosage_sub": "( 1 펌프 = 약 1ml ) - 증상에 따라 조절 가능"
    },
    {
        "id": "coldzero",
        "file_name": "monsmecta_coldzero_label.html",
        "name_ko": "몬스멕타 콜드제로",
        "name_en": "MONSMECTA COLDZERO",
        "sub_desc": "호흡기 및 감기 예방 보조제",
        "neon": "#22d3ee",
        "neon_sub": "#67e8f9",
        "neon_pale": "#cffafe",
        "border": "#0891b2",
        "bg_gradient": "linear-gradient(135deg, #04252e 0%, #02141a 50%, #030c10 100%)",
        "top_bar": "linear-gradient(90deg, #0891b2, #22d3ee, #a5f3fc, #0891b2)",
        "front_effects": [
            ("쌍화 추출물 기력 회복", "호흡기 점막 면역 강화"),
            ("비염·마른 기침 증상 완화", "기관지 윤활·항염증", "(*등의 개선에 도움)")
        ],
        "ingredients_header_ref": "1L 기준",
        "ingredients": [
            ("Montmorillonite (독소 흡착)", "고함량"),
            ("Ssanghwa Extract (쌍화 추출물)", "100,000mg"),
            ("Quercetin (퀘르세틴)", "40,000mg"),
            ("Liriope (맥문동)", "30,000mg"),
            ("Ulmus (유근피)", "30,000mg"),
            ("기타 식물추출물 및 부형제", "적량")
        ],
        "reg_no": "제 XX9UY0145호",
        "feed_type": "보조사료/미생물제/바실러스 서브틸리스l액상l반려동물",
        "reg_ing": "바실러스 서브틸리스 1.0 x 10⁶ cfu/g 이상, 부형제( 정제수 )",
        "raw_mat_lines": [
            "바실러스 서브틸리스, 퀘르세틴, 맥문동추출물,",
            "유근피추출물, 쌍화복합추출물, 정제수"
        ],
        "target": "반려견, 반려묘",
        "statutory_effects": [
            "쌍화 복합 추출물로 기력 회복 및 초기 감기 완화",
            "호흡기 점막 면역 강화 및 기관지 윤활에 도움",
            "비염, 마른 기침 증상 완화 및 알레르기 억제에 도움"
        ],
        "dosage_desc": "1일 1~2ml / 체중 5kg",
        "dosage_sub": "( 1 펌프 = 약 1ml ) - 증상에 따라 조절 가능"
    },
    {
        "id": "skincare",
        "file_name": "monsmecta_skincare_label.html",
        "name_ko": "몬스멕타 스킨케어",
        "name_en": "MONSMECTA SKINCARE",
        "sub_desc": "피부 및 아토피 개선 보조제",
        "neon": "#f472b6",
        "neon_sub": "#f9a8d4",
        "neon_pale": "#fce7f3",
        "border": "#db2777",
        "bg_gradient": "linear-gradient(135deg, #2e081e 0%, #1a0410 50%, #11030b 100%)",
        "top_bar": "linear-gradient(90deg, #db2777, #f472b6, #fbcfe8, #db2777)",
        "front_effects": [
            ("피부 장벽 강화 및 재생", "가려움증 및 발적 완화"),
            ("아토피 등 알러지 억제", "모질 개선 및 탈모 방지", "(*등의 개선에 도움)")
        ],
        "ingredients_header_ref": "1L 기준",
        "ingredients": [
            ("Montmorillonite (알러지 독소 흡착)", "고함량"),
            ("Quercetin (퀘르세틴)", "40,000mg"),
            ("Bromelain (브로멜라인)", "30,000mg"),
            ("Omega-3 (오메가3 EPA/DHA)", "30,000mg"),
            ("Monsmecta 베이스 배합", "핵심 원료"),
            ("기타 식물추출물 및 부형제", "적량")
        ],
        "reg_no": "제 XX9UY0145호",
        "feed_type": "보조사료/미생물제/바실러스 서브틸리스l액상l반려동물",
        "reg_ing": "바실러스 서브틸리스 1.0 x 10⁶ cfu/g 이상, 부형제( 정제수 )",
        "raw_mat_lines": [
            "바실러스 서브틸리스, 몬모릴로나이트, 퀘르세틴,",
            "브로멜라인, 오메가3(EPA/DHA), 정제수"
        ],
        "target": "반려견, 반려묘",
        "statutory_effects": [
            "피부 장벽 강화 및 피부 재생 촉진에 도움",
            "가려움증, 발적 및 아토피성 알레르기 억제",
            "피모 건강 유지, 모질 개선 및 탈모 방지에 도움"
        ],
        "dosage_desc": "1일 1~2ml / 체중 5kg",
        "dosage_sub": "( 1 펌프 = 약 1ml ) - 증상에 따라 조절 가능"
    },
    {
        "id": "heartcare",
        "file_name": "monsmecta_heartcare_label.html",
        "name_ko": "몬스멕타 하트케어",
        "name_en": "MONSMECTA HEARTCARE",
        "sub_desc": "심장 및 혈행 건강 보조제",
        "neon": "#f87171",
        "neon_sub": "#fca5a5",
        "neon_pale": "#fee2e2",
        "border": "#dc2626",
        "bg_gradient": "linear-gradient(135deg, #2e080b 0%, #1a0305 50%, #100203 100%)",
        "top_bar": "linear-gradient(90deg, #dc2626, #f87171, #fecaca, #dc2626)",
        "front_effects": [
            ("심장 근육 수축력 강화", "혈전 예방 및 혈류 개선"),
            ("심부전 진행 지연 보조", "혈압 정상화 보조", "(*등의 개선에 도움)")
        ],
        "ingredients_header_ref": "1L 기준 (배합비중)",
        "ingredients": [
            ("Coenzyme Q10 (코큐텐)", "25,000mg (20%)"),
            ("Hawthorn Extract (산사나무 열매)", "25,000mg (10%)"),
            ("L-carnitine (L-카르니틴)", "25,000mg (10%)"),
            ("Taurine (타우린)", "25,000mg (5%)"),
            ("Omega-3 EPA/DHA (오메가3)", "25,000mg (5%)"),
            ("기타 식물추출물 및 부형제", "적량")
        ],
        "reg_no": "제 XX9UY0145호",
        "feed_type": "보조사료/미생물제/바실러스 서브틸리스l액상l반려동물",
        "reg_ing": "바실러스 서브틸리스 1.0 x 10⁶ cfu/g 이상, 부형제( 정제수 )",
        "raw_mat_lines": [
            "바실러스 서브틸리스, 코큐텐(Q10), 산사나무 열매 추출물,",
            "L-카르니틴, 타우린, 오메가3(EPA/DHA), 정제수"
        ],
        "target": "반려견, 반려묘",
        "statutory_effects": [
            "심장 근육 수축력 강화 및 심근 세포 에너지 생성",
            "혈전 예방, 혈류 개선 및 혈압 안정화에 도움",
            "심부전 진행 지연 보조 및 심혈관 항염 작용"
        ],
        "dosage_desc": "1일 1~2ml / 체중 5kg",
        "dosage_sub": "( 1 펌프 = 약 1ml ) - 증상에 따라 조절 가능"
    },
    {
        "id": "jointcare",
        "file_name": "monsmecta_jointcare_label.html",
        "name_ko": "몬스멕타 조인트케어",
        "name_en": "MONSMECTA JOINTCARE",
        "sub_desc": "관절 및 연골 건강 보조제",
        "neon": "#a3e635",
        "neon_sub": "#bef264",
        "neon_pale": "#ecfccb",
        "border": "#65a30d",
        "bg_gradient": "linear-gradient(135deg, #1b2605 0%, #0e1502 50%, #080d02 100%)",
        "top_bar": "linear-gradient(90deg, #65a30d, #a3e635, #d9f99d, #65a30d)",
        "front_effects": [
            ("관절 연골 영양 공급", "관절 염증 및 통증 완화"),
            ("관절 윤활액 증가 보조", "관절염 진행 지연", "(*등의 개선에 도움)")
        ],
        "ingredients_header_ref": "1L 기준 (배합비중)",
        "ingredients": [
            ("MSM (식이유황)", "25,000mg (20%)"),
            ("Green Lipped Mussel (초록입홍합)", "25,000mg (10%)"),
            ("Boswellia (보스웰리아)", "25,000mg (10%)"),
            ("Chondroitin (콘드로이친)", "25,000mg (5%)"),
            ("Omega-3 EPA/DHA (오메가3)", "25,000mg (5%)"),
            ("기타 식물추출물 및 부형제", "적량")
        ],
        "reg_no": "제 XX9UY0145호",
        "feed_type": "보조사료/미생물제/바실러스 서브틸리스l액상l반려동물",
        "reg_ing": "바실러스 서브틸리스 1.0 x 10⁶ cfu/g 이상, 부형제( 정제수 )",
        "raw_mat_lines": [
            "바실러스 서브틸리스, 식이유황(MSM), 그린립 머슬 추출물,",
            "보스웰리아, 콘드로이친, 오메가3, 정제수"
        ],
        "target": "반려견, 반려묘",
        "statutory_effects": [
            "관절 연골 재생 및 윤활액 유지 보조",
            "관절 염증 완화 및 통증 경감에 도움",
            "퇴행성 관절염 진행 지연 및 기동성 개선"
        ],
        "dosage_desc": "1일 1~2ml / 체중 5kg",
        "dosage_sub": "( 1 펌프 = 약 1ml ) - 증상에 따라 조절 가능"
    },
    {
        "id": "powerase",
        "file_name": "monsmecta_powerase_label.html",
        "name_ko": "몬스멕타 파워라제",
        "name_en": "MONSMECTA POWERASE",
        "sub_desc": "기력 및 활력 회복 보조제",
        "neon": "#fb923c",
        "neon_sub": "#fdba74",
        "neon_pale": "#ffedd5",
        "border": "#ea580c",
        "bg_gradient": "linear-gradient(135deg, #2e1604 0%, #1a0b02 50%, #100701 100%)",
        "top_bar": "linear-gradient(90deg, #ea580c, #fb923c, #fed7aa, #ea580c)",
        "front_effects": [
            ("3대 소화 효소 복합 배합", "소화 개선·영양 흡수 촉진"),
            ("수술 후 빠른 회복 촉진", "기력 증진 및 대사 활성화", "(*등의 개선에 도움)")
        ],
        "ingredients_header_ref": "고활성 복합 효소",
        "ingredients": [
            ("Endo Protease (단백질 분해)", "506,000 pu/g"),
            ("Alpha Amylase (탄수화물 분해)", "770 u/g"),
            ("Lipase (지방 분해 효소)", "3,277 u/g"),
            ("Monsmecta 베이스 배합", "핵심 원료"),
            ("기타 복합효소 및 부형제", "적량")
        ],
        "reg_no": "제 XX9UY0145호",
        "feed_type": "보조사료/미생물제/바실러스 서브틸리스l액상l반려동물",
        "reg_ing": "바실러스 서브틸리스 1.0 x 10⁶ cfu/g 이상, 부형제( 정제수 )",
        "raw_mat_lines": [
            "바실러스 서브틸리스, 엔도 프로테아제, 알파 아밀라제,",
            "라이페이스, 포도당, 정제수"
        ],
        "target": "반려견, 반려묘",
        "statutory_effects": [
            "단백질·지방·탄수화물 3대 소화 효소로 영양 흡수 촉진",
            "수술 후 빠른 회복 및 소화기 안정화 지원",
            "노령견·묘 기력 증진 및 체내 대사 활성화에 도움"
        ],
        "dosage_desc": "1일 1~2ml / 체중 5kg",
        "dosage_sub": "( 1 펌프 = 약 1ml ) - 증상에 따라 조절 가능"
    },
    {
        "id": "probiotics",
        "file_name": "monsmecta_probiotics_label.html",
        "name_ko": "몬스멕타 프로바이오틱스",
        "name_en": "MONSMECTA PROBIOTICS",
        "sub_desc": "세계 3대 유산균 듀퐁 다니스코 프리미엄 적용",
        "neon": "#4ade80",
        "neon_sub": "#86efac",
        "neon_pale": "#dcfce7",
        "border": "#16a34a",
        "bg_gradient": "linear-gradient(135deg, #062b14 0%, #03170a 50%, #020f06 100%)",
        "top_bar": "linear-gradient(90deg, #16a34a, #4ade80, #bbf7d0, #16a34a)",
        "front_effects": [
            ("듀퐁 다니스코 프리미엄 균주", "항생제 연관 설사·장염 예방"),
            ("염증성 장질환·IBS 완화", "유해균 억제·장벽 강화", "(*등의 개선에 도움)")
        ],
        "ingredients_header_ref": "1L 기준 복합 균주",
        "ingredients": [
            ("Bacillus subtilis (바실러스 균)", "1.0 x 10¹⁰ cfu"),
            ("듀퐁 다니스코 프리미엄 18종 균주", "1.0 x 10¹⁰ cfu"),
            ("└ 생물학적 보호 기술(안정성)", "핵심 기술"),
            ("└ 위산 및 담즙산 생존력 우수", "임상 검증"),
            ("└ 우수한 장내 정착 및 증식 작용", "핵심 균주"),
            ("FOS (프락토올리고당)", "프리바이오틱스"),
            ("기타 식물추출물 및 부형제", "적량")
        ],
        "reg_no": "제 XX9UY0145호",
        "feed_type": "보조사료/미생물제/바실러스 서브틸리스l액상l반려동물",
        "reg_ing": "바실러스 서브틸리스·듀퐁 다니스코 유산균 각 1.0 x 10⁷ cfu/g 이상",
        "raw_mat_lines": [
            "바실러스 서브틸리스, 듀퐁 다니스코 특화 유산균(18종),",
            "프락토올리고당, 포도당, 정제수"
        ],
        "target": "반려견, 반려묘",
        "statutory_effects": [
            "세계 3대 유산균 듀퐁 다니스코 프리미엄 균주 장내 정착",
            "항생제 연관 설사, 장염 예방 및 IBS 증상 완화",
            "유해균 억제, 유익균 증식 및 장벽 방어력 강화"
        ],
        "dosage_desc": "1일 1~2ml / 체중 5kg",
        "dosage_sub": "( 1 펌프 = 약 1ml ) - 증상에 따라 조절 가능"
    },
    {
        "id": "vitaplus",
        "file_name": "monsmecta_vitaplus_label.html",
        "name_ko": "몬스멕타 비타플러스",
        "name_en": "MONSMECTA VITAPLUS",
        "sub_desc": "종합 비타민 및 미네랄 보조제",
        "neon": "#facc15",
        "neon_sub": "#fde047",
        "neon_pale": "#fef9c3",
        "border": "#ca8a04",
        "bg_gradient": "linear-gradient(135deg, #2a2203 0%, #171301 50%, #0e0b01 100%)",
        "top_bar": "linear-gradient(90deg, #ca8a04, #facc15, #fef08a, #ca8a04)",
        "front_effects": [
            ("필수 비타민 10종 종합 공급", "피로 회복 및 항산화 작용"),
            ("뼈·치아 건강 지원", "신진대사 활성화 보조", "(*등의 개선에 도움)")
        ],
        "ingredients_header_ref": "1L 기준 (10종 비타민)",
        "ingredients": [
            ("Vitamin A (비타민 A)", "750,000 IU"),
            ("Vitamin D3 (비타민 D3)", "150,000 IU"),
            ("Vitamin E (비타민 E)", "300 mg"),
            ("L-Methionine (L-메티오닌)", "300 mg"),
            ("L-Arginine (L-아르기닌)", "80 mg"),
            ("기타 복합 비타민 및 미네랄", "적량")
        ],
        "reg_no": "제 XX9UY0145호",
        "feed_type": "보조사료/미생물제/바실러스 서브틸리스l액상l반려동물",
        "reg_ing": "바실러스 서브틸리스 1.0 x 10⁶ cfu/g 이상, 부형제( 정제수 )",
        "raw_mat_lines": [
            "바실러스 서브틸리스, 비타민A, 비타민D3, 비타민E,",
            "L-메티오닌, L-아르기닌, 복합비타민, 정제수"
        ],
        "target": "반려견, 반려묘",
        "statutory_effects": [
            "필수 비타민 10종 고함량 복합 공급으로 활력 증진",
            "피로 회복, 항산화 작용 및 면역 건강 유지",
            "뼈·치아 건강 및 체내 대사 활성화에 도움"
        ],
        "dosage_desc": "1일 1~2ml / 체중 5kg",
        "dosage_sub": "( 1 펌프 = 약 1ml ) - 증상에 따라 조절 가능"
    }
]

def render_html(p):
    ing_rows_html = []
    # Dynamic styling depending on number of ingredient rows
    num_ing = len(p["ingredients"])
    row_font_size = "1.25mm" if num_ing >= 7 else "1.32mm"
    row_padding = "0.02mm 0" if num_ing >= 7 else "0.04mm 0"
    box_padding = "0.12mm 0.50mm" if num_ing >= 7 else "0.18mm 0.50mm"
    
    for k, v in p["ingredients"]:
        val_display = v
        # format superscript powers if any
        if "10^" in val_display:
            val_display = val_display.replace("10^10", "1.0 x 10<sup style=\"font-size:0.75em; vertical-align:0.38em; font-family:'Noto Sans KR', sans-serif;\">10</sup>")
            val_display = val_display.replace("10^11", "1.0 x 10<sup style=\"font-size:0.75em; vertical-align:0.38em; font-family:'Noto Sans KR', sans-serif;\">11</sup>")
            val_display = val_display.replace("10^7", "1.0 x 10<sup style=\"font-size:0.75em; vertical-align:0.38em; font-family:'Noto Sans KR', sans-serif;\">7</sup>")
            val_display = val_display.replace("10^6", "1.0 x 10<sup style=\"font-size:0.75em; vertical-align:0.38em; font-family:'Noto Sans KR', sans-serif;\">6</sup>")
        
        ing_rows_html.append(f'''                    <div class="ing-row">
                        <span class="ing-name">{k}</span>
                        <span class="ing-val">{val_display}</span>
                    </div>''')
    
    ing_rows_joined = "\n".join(ing_rows_html)
    
    # Front effects
    row1 = p["front_effects"][0]
    row2 = p["front_effects"][1]
    
    row1_html = f'''                            <span class="eff-item"><span class="eff-dot"></span>{row1[0]}</span>
                            <span class="eff-item"><span class="eff-dot"></span>{row1[1]}</span>'''
    
    note_html = f'<span class="eff-note">{row2[2]}</span>' if len(row2) > 2 and row2[2] else ""
    row2_items = []
    if row2[0]: row2_items.append(f'<span class="eff-item"><span class="eff-dot"></span>{row2[0]}</span>')
    if row2[1]: row2_items.append(f'<span class="eff-item"><span class="eff-dot"></span>{row2[1]}</span>')
    row2_joined = "\n                            ".join(row2_items)
    if note_html:
        row2_joined += f"\n                            {note_html}"
    
    # Statutory effects list
    stat_eff_html = []
    romans = ["I.", "II.", "III.", "IV."]
    for idx, eff in enumerate(p["statutory_effects"]):
        r = romans[idx] if idx < len(romans) else "•"
        stat_eff_html.append(f'                            <li><span class="roman">{r}</span>{eff}</li>')
    stat_eff_joined = "\n".join(stat_eff_html)
    
    # Raw materials lines
    raw_mat_html = f'''                                <div>{p["raw_mat_lines"][0]}</div>
                                <div>{p["raw_mat_lines"][1]}</div>'''
    
    html = f'''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>{p["name_en"]} Label (85mm x 40mm)</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@500;700;800;900&family=Orbitron:wght@700;900&display=swap" rel="stylesheet">
    
    <style>
        @page {{
            size: 85mm 40mm;
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
            margin: 0;
            padding: 0;
            font-family: 'Noto Sans KR', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }}

        .orbitron {{
            font-family: 'Orbitron', sans-serif;
        }}

        /* 화면 뷰어 모드 (여백 및 잘림 완전 방지) */
        @media screen {{
            html, body {{
                width: 100% !important;
                min-height: 100vh !important;
                background: #09090b !important;
                display: flex !important;
                flex-direction: column !important;
                align-items: center !important;
                justify-content: flex-start !important;
                padding: 70px 20px 40px 20px !important;
                overflow-x: auto !important;
            }}
            .label-sheet-container {{
                padding: 20px;
                display: flex;
                justify-content: center;
                align-items: center;
            }}
            .label-sheet {{
                box-shadow: 0 25px 60px rgba(0, 0, 0, 0.95), 0 0 35px {p["neon"]}55;
                transform: scale(2.5);
                transform-origin: top center;
                margin-bottom: 75mm;
            }}
        }}

        /* 인쇄 전용 (85mm x 40mm 1:1 출력) */
        @media print {{
            html, body {{
                width: 85mm !important;
                height: 40mm !important;
                margin: 0 !important;
                padding: 0 !important;
                background: transparent !important;
                overflow: hidden !important;
            }}
            .label-sheet {{
                border: none !important;
                width: 85mm !important;
                height: 40mm !important;
                transform: none !important;
                box-shadow: none !important;
                margin: 0 !important;
            }}
            .no-print {{
                display: none !important;
            }}
        }}

        /* 30ml 맞춤 규격 (85mm x 40mm) */
        .label-sheet {{
            width: 85mm;
            height: 40mm;
            background: {p["bg_gradient"]};
            color: #f8fafc;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            border: 0.15mm solid {p["border"]};
            flex-shrink: 0;
        }}

        .grid-overlay {{
            position: absolute;
            inset: 0;
            opacity: 0.08;
            background-image: 
                linear-gradient({p["neon"]} 1px, transparent 1px),
                linear-gradient(90deg, {p["neon"]} 1px, transparent 1px);
            background-size: 2.5mm 2.5mm;
            pointer-events: none;
            z-index: 1;
        }}

        /* 슬림 탑 엑센트 바 */
        .top-accent-bar {{
            height: 0.35mm;
            background: {p["top_bar"]};
            box-shadow: 0 0 1.2mm {p["neon"]}E6;
            z-index: 2;
            flex-shrink: 0;
        }}

        /* 콘텐츠 랩 */
        .content-wrap {{
            position: relative;
            z-index: 2;
            display: flex;
            height: calc(40mm - 0.35mm);
            width: 85mm;
            padding: 0.20mm 0.30mm 0.20mm 0.30mm;
            justify-content: space-between;
        }}

        /* 좌측: 전면 메인 노출부 (너비 39.5mm) */
        .col-left {{
            width: 39.5mm;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}

        /* 중앙 디바이더 (너비 1.8mm: 좌우 분리 간격 확실히 확보) */
        .divider-col {{
            width: 1.8mm;
            height: 100%;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .divider-line {{
            width: 0.15mm;
            height: 98%;
            background: linear-gradient(180deg, transparent, {p["neon"]}, transparent);
            opacity: 0.7;
        }}
        .divider-diamond {{
            position: absolute;
            width: 0.8mm;
            height: 0.8mm;
            background: #000;
            border: 0.15mm solid {p["neon"]};
            transform: rotate(45deg);
        }}

        /* 우측: 법정 고시사항 노출부 (너비 43.1mm) */
        .col-right {{
            width: 43.1mm;
            height: 100%;
            display: flex;
            flex-direction: column;
        }}

        /* 브랜드 배지 */
        .brand-badge {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.6mm;
            background: rgba(0, 0, 0, 0.65);
            border: 0.15mm solid {p["neon"]};
            border-radius: 999px;
            padding: 0.12mm 1.0mm;
            line-height: 1;
            box-sizing: border-box;
        }}
        .brand-badge .emoji {{
            font-size: 2.2mm;
            line-height: 1;
            display: inline-flex;
            align-items: center;
        }}
        .brand-badge .text {{
            font-size: 1.28mm;
            font-weight: 800;
            letter-spacing: 0.02em;
            color: #ffffff;
            line-height: 1;
            display: inline-flex;
            align-items: center;
        }}
        .brand-badge .accent {{
            color: {p["neon"]};
            font-weight: 900;
        }}

        /* 히어로 섹션 */
        .hero-section {{
            text-align: center;
            padding: 0;
            margin: 0;
        }}
        .sub-desc {{
            font-size: 1.45mm;
            font-weight: 700;
            color: #f1f5f9;
            line-height: 1.05;
            margin-bottom: 0.04mm;
            text-shadow: 0 0 0.6mm rgba(0,0,0,0.8);
        }}
        .main-title {{
            font-size: 3.95mm;
            font-weight: 900;
            color: #ffffff;
            line-height: 1.0;
            letter-spacing: -0.03em;
            text-shadow: 0 0 1.2mm rgba(255, 255, 255, 0.5), 0 1px 2px #000;
            margin-bottom: 0.04mm;
        }}
        .en-title {{
            font-size: 1.62mm;
            font-weight: 900;
            color: {p["neon"]};
            letter-spacing: 0.05em;
            line-height: 1;
        }}

        /* 핵심 효능 박스 */
        .effects-box-wrapper {{
            position: relative;
            padding-top: 0.95mm;
            margin: 0.06mm 0;
        }}
        .effects-badge-top {{
            position: absolute;
            top: 0;
            left: 1.2mm;
            z-index: 3;
            background: {p["neon"]};
            color: #000;
            border: 0.12mm solid #000;
            border-radius: 0.25mm;
            padding: 0.05mm 0.65mm 0.23mm 0.65mm;
            font-size: 1.15mm;
            font-weight: 900;
            line-height: 1;
            box-shadow: 0 0.2mm 0.4mm rgba(0, 0, 0, 0.9);
            display: inline-flex;
            align-items: center;
            justify-content: center;
        }}
        .effects-card {{
            background: rgba(0, 0, 0, 0.65);
            border: 0.15mm solid {p["neon"]};
            border-radius: 0.5mm;
            padding: 0.85mm 0.50mm 0.25mm 0.50mm;
            display: flex;
            flex-direction: column;
            gap: 0.20mm;
        }}
        .effects-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            line-height: 1.10;
            white-space: nowrap;
        }}
        .eff-item {{
            font-size: 1.32mm;
            font-weight: 800;
            color: #ffffff;
            display: inline-flex;
            align-items: center;
            gap: 0.22mm;
            line-height: 1.05;
            white-space: nowrap;
        }}
        .eff-dot {{
            width: 0.60mm;
            height: 0.60mm;
            border-radius: 50%;
            background: {p["neon"]};
            box-shadow: 0 0 0.3mm {p["neon"]};
            flex-shrink: 0;
        }}
        .eff-note {{
            font-size: 1.05mm;
            color: {p["neon_sub"]};
            font-weight: 700;
            line-height: 1;
            white-space: nowrap;
            opacity: 0.95;
        }}

        /* 성분 테이블 */
        .tech-box-ing {{
            background: rgba(0, 0, 0, 0.55);
            border: 0.15mm solid {p["neon"]}55;
            border-radius: 0.5mm;
            padding: {box_padding};
        }}
        .ing-header {{
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            border-bottom: 0.1mm solid {p["neon"]}66;
            padding-bottom: 0.04mm;
            margin-bottom: 0.04mm;
        }}
        .ing-header .title {{
            font-size: 1.30mm;
            font-weight: 800;
            color: #fff;
        }}
        .ing-header .ref {{
            font-size: 1.15mm;
            color: {p["neon"]};
            font-weight: 800;
        }}
        .ing-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: {row_font_size};
            line-height: 1.15;
            border-bottom: 0.05mm solid rgba(255, 255, 255, 0.08);
            padding: {row_padding};
        }}
        .ing-row:last-child {{
            border-bottom: none;
        }}
        .ing-name {{
            font-weight: 700;
            color: #f1f5f9;
        }}
        .ing-val {{
            font-weight: 900;
            color: #ffffff;
            font-family: 'Orbitron', 'Noto Sans KR', sans-serif;
            font-size: {row_font_size};
        }}

        /* 포장단위 배지 */
        .pack-tag {{
            align-self: center;
            background: rgba(0, 0, 0, 0.65);
            border: 0.18mm solid {p["neon"]};
            border-radius: 999px;
            padding: 0.14mm 1.4mm;
            font-size: 1.32mm;
            font-weight: 800;
            display: flex;
            gap: 0.5mm;
            align-items: center;
            justify-content: center;
            line-height: 1;
            box-sizing: border-box;
            color: #ffffff;
        }}
        .pack-tag .val {{
            color: {p["neon"]};
            font-weight: 900;
        }}

        /* ------------------------------------------------------------- */
        /* 우측 법정 고시 패널 */
        /* ------------------------------------------------------------- */
        .legal-panel {{
            background: rgba(0, 0, 0, 0.55);
            border: 0.15mm solid rgba(255, 255, 255, 0.22);
            border-radius: 0.5mm;
            height: 100%;
            padding: 0.15mm 0.50mm 0.12mm 0.50mm;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}

        /* 헤더: 성분등록번호 & 종류/명칭 */
        .legal-header {{
            border-bottom: 0.1mm solid {p["neon"]}66;
            padding-bottom: 0.10mm;
            display: flex;
            flex-direction: column;
            gap: 0.16mm;
        }}
        .reg-num-line {{
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            line-height: 1.15;
        }}
        .reg-num-label {{
            font-size: 1.14mm;
            color: {p["neon"]};
            font-weight: 800;
            line-height: 1;
        }}
        .reg-num-val {{
            font-size: 1.28mm;
            font-weight: 900;
            color: #ffffff;
            line-height: 1;
        }}
        .feed-type-line {{
            font-size: 0.98mm;
            font-weight: 700;
            color: #e2e8f0;
            line-height: 1.15;
            white-space: nowrap;
        }}
        .feed-type-line .lbl {{
            color: {p["neon"]};
            font-weight: 800;
        }}

        /* 1. 고시 본문 영역: 모든 소제목 좌측선 완벽 일치 */
        .sec-content {{
            display: flex;
            flex-direction: column;
            gap: 0.08mm;
            margin: 0.02mm 0;
            text-align: left;
        }}
        
        .info-row {{
            display: flex;
            align-items: baseline;
            font-size: 1.15mm;
            line-height: 1.22;
            color: #f8fafc;
            text-align: left;
        }}
        .sec-lbl {{
            font-weight: 800;
            color: {p["neon"]};
            margin-right: 0.25mm;
            white-space: nowrap;
            flex-shrink: 0;
            text-align: left;
        }}
        .sec-val {{
            color: #ffffff;
            font-weight: 700;
            flex: 1;
        }}

        /* 2. 사용한 원료의 명칭: 2줄 넉넉하게 */
        .materials-val-box {{
            display: flex;
            flex-direction: column;
            gap: 0.02mm;
            flex: 1;
            color: #f8fafc;
            font-weight: 600;
            line-height: 1.20;
        }}

        /* 효과 3가지 리스트 */
        .effects-sub-list {{
            list-style: none;
            padding-left: 0.4mm;
            display: flex;
            flex-direction: column;
            gap: 0.04mm;
            margin: 0.01mm 0;
        }}
        .effects-sub-list li {{
            font-size: 1.12mm;
            font-weight: 600;
            color: #f1f5f9;
            line-height: 1.22;
            display: flex;
            align-items: baseline;
        }}
        .effects-sub-list .roman {{
            color: {p["neon"]};
            font-weight: 900;
            margin-right: 0.20mm;
            flex-shrink: 0;
        }}

        /* 용법 및 용량 */
        .dose-box {{
            background: {p["neon"]}22;
            border: 0.12mm solid {p["neon"]};
            border-radius: 0.35mm;
            padding: 0.22mm 0.45mm;
            display: flex;
            align-items: center;
            justify-content: space-between;
            line-height: 1;
            box-sizing: border-box;
            flex-wrap: wrap;
            gap: 0.15mm;
        }}
        .dose-title {{
            font-size: 1.16mm;
            font-weight: 900;
            color: {p["neon"]};
            white-space: nowrap;
            line-height: 1;
            display: inline-flex;
            align-items: center;
        }}
        .dose-desc {{
            font-size: 1.25mm;
            font-weight: 900;
            color: #ffffff;
            white-space: nowrap;
            line-height: 1;
            display: inline-flex;
            align-items: center;
        }}
        .dose-sub {{
            font-size: 1.02mm;
            color: #f1f5f9;
            font-weight: 700;
            white-space: nowrap;
            line-height: 1;
            display: inline-flex;
            align-items: center;
        }}

        /* 4. 주의사항 박스 */
        .warn-box {{
            background: rgba(220, 38, 38, 0.15);
            border: 0.15mm solid rgba(239, 68, 68, 0.65);
            border-radius: 0.45mm;
            padding: 0.20mm 0.50mm 0.20mm 0.50mm;
            box-sizing: border-box;
            margin: 0.04mm 0;
        }}
        .warn-title {{
            font-size: 1.16mm;
            font-weight: 800;
            color: #f87171;
            display: flex;
            align-items: center;
            gap: 0.20mm;
            line-height: 1;
            margin-bottom: 0.08mm;
        }}
        .warn-list {{
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 0.06mm;
        }}
        .warn-item {{
            font-size: 1.10mm;
            color: #f8fafc;
            line-height: 1.18;
            font-weight: 600;
            display: flex;
            align-items: baseline;
        }}
        .warn-item .num {{
            color: #fca5a5;
            font-weight: 800;
            margin-right: 0.3mm;
            flex-shrink: 0;
        }}
        .warn-item .hl-shake {{
            color: {p["neon"]};
            text-decoration: underline;
            text-decoration-thickness: 0.12mm;
            text-underline-offset: 0.12mm;
            font-weight: 800;
        }}

        /* 3. 제조 및 유통기한 바 & 재활용 표식 상단 배치 */
        .mfg-exp-bar-with-recycle {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 0.1mm solid rgba(255, 255, 255, 0.2);
            border-bottom: 0.1mm solid rgba(255, 255, 255, 0.2);
            padding: 0.08mm 0.20mm;
            line-height: 1;
            box-sizing: border-box;
        }}
        .mfg-exp-info {{
            display: flex;
            align-items: center;
            gap: 0.7mm;
            font-size: 0.98mm;
            font-weight: 700;
            color: #e2e8f0;
            white-space: nowrap;
        }}
        .mfg-exp-info .lbl {{
            color: #cbd5e1;
            margin-right: 0.2mm;
        }}
        .mfg-exp-info .val {{
            color: #ffffff;
            font-weight: 800;
        }}

        /* 3. 단정하고 깔끔한 재활용 표식 */
        .recycle-badge-raised {{
            display: flex;
            align-items: center;
            gap: 0.35mm;
            padding: 0.05mm 0.3mm;
            flex-shrink: 0;
        }}
        .recycle-icon-wrap {{
            width: 2.3mm;
            height: 2.3mm;
            position: relative;
            flex-shrink: 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .recycle-icon {{
            width: 100%;
            height: 100%;
            display: block;
        }}
        .recycle-text {{
            position: absolute;
            inset: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.65mm;
            font-weight: 900;
            color: #ffffff;
            padding-top: 0.3mm;
            letter-spacing: -0.05em;
        }}
        .recycle-sub {{
            font-size: 0.90mm;
            font-weight: 900;
            color: #ffffff;
            line-height: 1;
            letter-spacing: 0.02em;
        }}

        /* 제조원 및 판매원 풋터 */
        .legal-footer {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            padding-top: 0.08mm;
            gap: 0.50mm;
        }}
        .company-block {{
            display: flex;
            align-items: flex-start;
            gap: 0.25mm;
            flex: 1;
        }}
        .company-logo-circle {{
            width: 3.2mm;
            height: 3.2mm;
            border-radius: 50%;
            background: #fff;
            border: 0.15mm solid {p["neon"]};
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            flex-shrink: 0;
            box-shadow: 0 0 0.6mm {p["neon"]}99;
            margin-top: 0.05mm;
        }}
        .company-logo-circle img {{
            width: 100%;
            height: 100%;
            object-fit: contain;
            padding: 0.06mm;
        }}
        .company-info {{
            font-size: 0.92mm;
            color: #f1f5f9;
            line-height: 1.18;
            font-weight: 600;
            text-align: left;
        }}
        .company-info .co-title {{
            font-weight: 800;
            color: {p["neon"]};
            font-size: 0.94mm;
            letter-spacing: -0.02em;
        }}
        .company-info .co-name {{
            color: #ffffff;
            font-weight: 800;
        }}
        .company-info .co-addr {{
            color: #cbd5e1;
        }}
        .company-info .tel-accent {{
            color: {p["neon"]};
            font-weight: 800;
        }}
    </style>
</head>
<body>

<div class="no-print" style="position:fixed; top:12px; left:50%; transform:translateX(-50%); z-index:99999; background:rgba(15,23,42,0.95); border:1px solid {p["neon"]}; padding:10px 24px; border-radius:12px; display:flex; align-items:center; gap:16px; box-shadow:0 10px 30px rgba(0,0,0,0.8); font-family:sans-serif;">
    <div style="color:#fff; font-size:13px; font-weight:700;">
        <span style="color:{p["neon"]};">★ {p["name_ko"]} (85mm × 40mm)</span> | 30ml 프리미엄 라벨 규격
    </div>
    <button onclick="window.print()" style="background:linear-gradient(135deg, {p["neon"]}, {p["border"]}); color:#fff; font-weight:800; font-size:13px; padding:6px 16px; border:none; border-radius:8px; cursor:pointer;">
        라벨 즉시 인쇄 (Ctrl+P)
    </button>
</div>

<div class="label-sheet-container">
    <div class="label-sheet">
        <div class="grid-overlay"></div>
        <div class="top-accent-bar"></div>

        <div class="content-wrap">
            <!-- LEFT COLUMN (전면 메인) -->
            <div class="col-left">
                <!-- Brand Badge -->
                <div class="brand-badge">
                    <span class="emoji">🐶</span>
                    <span class="text"><span class="accent">S&J</span>&nbsp;ADVANCED VET FORMULA</span>
                    <span class="emoji">🐱</span>
                </div>

                <!-- Hero Title -->
                <div class="hero-section">
                    <div class="sub-desc">{p["sub_desc"]}</div>
                    <h1 class="main-title">{p["name_ko"]}</h1>
                    <h2 class="en-title orbitron">{p["name_en"].replace("MONSMECTA", "MONSMECTA<span style=\"font-size:0.65em; vertical-align:super; color:" + p["neon_sub"] + "; margin-left:0.3mm;\">™</span>")}</h2>
                </div>

                <!-- 핵심 효능 박스 -->
                <div class="effects-box-wrapper">
                    <div class="effects-badge-top">핵심 효능</div>
                    <div class="effects-card">
                        <div class="effects-row">
{row1_html}
                        </div>
                        <div class="effects-row">
                            {row2_joined}
                        </div>
                    </div>
                </div>

                <!-- Ingredients Table (주요 성분량) -->
                <div class="tech-box-ing">
                    <div class="ing-header">
                        <span class="title">주요 성분량</span>
                        <span class="ref">{p["ingredients_header_ref"]}</span>
                    </div>
                    
{ing_rows_joined}
                </div>

                <!-- Pack size -->
                <div class="pack-tag">
                    <span>포장 단위 :</span>
                    <span class="val">30ml / 병</span>
                </div>
            </div>

            <!-- CENTER DIVIDER -->
            <div class="divider-col">
                <div class="divider-line"></div>
                <div class="divider-diamond"></div>
            </div>

            <!-- RIGHT COLUMN (오른쪽-뒷면: 법정 고시사항) -->
            <div class="col-right">
                <div class="legal-panel">
                    <!-- 헤더: 성분등록번호 & 사료의 종류와 명칭 / 형태 / 용도 -->
                    <div class="legal-header">
                        <div class="reg-num-line" style="display:flex; justify-content:space-between; align-items:center;">
                            <div>
                                <span class="reg-num-label">사료의 성분등록번호 :</span>
                                <span class="reg-num-val">{p["reg_no"]}</span>
                            </div>
                            <span style="font-size:0.95mm; color:{p["neon_sub"]}; font-weight:800; white-space:nowrap;">U.S. TM App: 50/041,096</span>
                        </div>
                        <div class="feed-type-line">
                            <span class="lbl">사료의 종류와 명칭 / 형태 / 용도 :</span> {p["feed_type"]}
                        </div>
                    </div>

                    <!-- 1 & 2. 고시 본문: 모든 소제목 좌측선 일치 + 사용한 원료 명칭 2줄 정렬 -->
                    <div class="sec-content">
                        <!-- 등록성분량 -->
                        <div class="info-row">
                            <span class="sec-lbl">등록성분량 :</span>
                            <span class="sec-val">{p["reg_ing"]}</span>
                        </div>

                        <!-- 2. 사용한 원료의 명칭 -->
                        <div class="info-row">
                            <span class="sec-lbl">사용한 원료의 명칭 :</span>
                            <div class="materials-val-box">
{raw_mat_html}
                            </div>
                        </div>

                        <!-- 대상 -->
                        <div class="info-row">
                            <span class="sec-lbl">대상 :</span>
                            <span class="sec-val">{p["target"]}</span>
                        </div>

                        <!-- 효과 -->
                        <div class="info-row">
                            <span class="sec-lbl">효과 :</span>
                        </div>
                        <ul class="effects-sub-list">
{stat_eff_joined}
                        </ul>
                    </div>

                    <!-- 용법 및 용량 -->
                    <div class="dose-box">
                        <div style="display:flex; align-items:center; gap:0.3mm;">
                            <span class="dose-title">용법 및 용량 :</span>
                            <span class="dose-desc">{p["dosage_desc"]}</span>
                        </div>
                        <span class="dose-sub">{p["dosage_sub"]}</span>
                    </div>

                    <!-- 4. 주의사항 박스 -->
                    <div class="warn-box">
                        <div class="warn-title">
                            <svg width="2.0mm" height="2.0mm" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd"></path></svg>
                            <span>주의사항 :</span>
                        </div>
                        <ul class="warn-list">
                            <li class="warn-item">
                                <span class="num">1)</span>
                                <span>직사광선을 피하여 서늘한 곳에 보관하십시오.</span>
                            </li>
                            <li class="warn-item">
                                <span class="num">2)</span>
                                <span>제품특성상 가라앉는 성분들이 있어서 <span class="hl-shake">흔들어서 사용</span>하십시오.</span>
                            </li>
                            <li class="warn-item">
                                <span class="num">3)</span>
                                <span>제품에 대하여 문의하실 경우 제조원 또는 판매원으로 연락하여 주시기 바랍니다</span>
                            </li>
                        </ul>
                    </div>

                    <!-- 3. 제조 및 유통기한 바 & 재활용 표식 -->
                    <div class="mfg-exp-bar-with-recycle">
                        <div class="mfg-exp-info">
                            <div style="white-space:nowrap;"><span class="lbl">포장 단위 :</span><span class="val">30ml</span></div>
                            <div style="white-space:nowrap;"><span class="lbl">제조일자 :</span><span class="val">2026.09.15</span></div>
                            <div style="white-space:nowrap;"><span class="lbl">유통기한 :</span><span class="val">제조일로부터 18개월</span></div>
                        </div>

                        <!-- 3. 재활용 표식 -->
                        <div class="recycle-badge-raised">
                            <div class="recycle-icon-wrap">
                                <svg class="recycle-icon" viewBox="0 0 100 100">
                                    <path d="M50 14 L88 80 L12 80 Z" fill="none" stroke="{p["neon"]}" stroke-width="7" stroke-linejoin="round"/>
                                </svg>
                                <span class="recycle-text">플라스틱</span>
                            </div>
                            <span class="recycle-sub">OTHER</span>
                        </div>
                    </div>

                    <!-- 판매원 / 제조원 풋터 -->
                    <div class="legal-footer">
                        <!-- 위탁제조판매원: 에스앤제이 동물병원 -->
                        <div class="company-block">
                            <div class="company-logo-circle">
                                <img src="{LOGO_B64}" alt="에스앤제이 동물병원">
                            </div>
                            <div class="company-info">
                                <div><span class="co-title">위탁제조판매원 :</span> <span class="co-name">에스앤제이 동물병원</span></div>
                                <div class="co-addr">주소 : 경기도 용인시 포곡읍 선장1로 98-8</div>
                                <div>전화번호 : <span class="tel-accent">031-321-6562</span></div>
                            </div>
                        </div>

                        <!-- 제조원: 엠오바이오 -->
                        <div class="company-block">
                            <div class="company-info">
                                <div><span class="co-title">제조원:</span><span class="co-name">엠오바이오</span></div>
                                <div class="co-addr">주소 : 경기도 화성시 팔탄면 석포로 74번길 10-25</div>
                                <div>전화번호 : <span class="tel-accent">031-458-1240</span></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

</body>
</html>
'''
    return html

for p in PRODUCTS:
    target_path = os.path.join(out_dir, p["file_name"])
    # If it's renal or hepamax, keep existing if requested or overwrite with exact format
    html_content = render_html(p)
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated {p['name_ko']} -> {target_path}")

print("All 11 product labels generated successfully!")
