import os
import base64

# Base paths
BASE_DIR = "/home/hongsoonil02/monsmecta"
LABELS_DIR = os.path.join(BASE_DIR, "public/assets/labels")
LOGO_PATH = os.path.join(LABELS_DIR, "sj_logo_thumb.png")

# Read base64 logo
with open(LOGO_PATH, "rb") as f:
    b64_logo = base64.b64encode(f.read()).decode("utf-8")
data_uri_logo = f"data:image/png;base64,{b64_logo}"

# Products configuration
PRODUCTS = [
    {
        "key": "hepamax",
        "html_name": "monsmecta_hepamax_label.html",
        "print_name": "hepamax_label_print.html",
        "name_ko": "몬스멕타 헤파맥스",
        "name_en": "MONSMECTA HEPAMAX",
        "sub_desc": "간 기능 보호 및 해독 활성화",
        "theme": {
            "bg": "linear-gradient(135deg, #280909 0%, #100404 50%, #050d0d 100%)",
            "border": "#a3824c",
            "grid": "#D4AF37",
            "accent_bar": "linear-gradient(90deg, #b8860b, #ffd700, #b8860b)",
            "glow": "rgba(255, 215, 0, 0.8)",
            "divider": "linear-gradient(180deg, transparent, #D4AF37, transparent)",
            "screen_bg": "#0f172a",
            "screen_shadow": "rgba(212, 175, 55, 0.4)",
        },
        "effects_row1": [
            ("간 건강 개선", True),
            ("장 건강 개선", True),
            ("지방간 개선", True),
        ],
        "effects_row2": [
            ("항병력 증진", True),
            ("질병 회복 촉진", True),
        ],
        "unit_desc": "1L 기준",
        "ingredients": [
            ("Montmorillonite (몬모릴로나이트)", "고함량"),
            ("Taurine (타우린)", "2,000mg"),
            ("D-Sorbitol (D-소르비톨)", "45g"),
            ("L-lysine HCl", "300mg"),
            ("L-methionine", "300mg"),
            ("Vitamin B1", "1,000μg"),
            ("기타 식물추출물 및 부형제", "적량"),
        ],
        "reg_amount": "바실러스 서브틸리스 1.0 x 10⁷ cfu/g 이상, 부형제( 정제수 )",
        "raw_mat_l1": "바실러스 서브틸리스, 비타민A, 아세트산 나트륨,",
        "raw_mat_l2": "프로피온산 나트륨, 포도당, 정제수",
        "feed_type": "보조사료/미생물제/바실러스 서브틸리스l액상l반려동물",
        "dose_main": "1일 1~2ml / 체중 5kg",
        "dose_sub": "( 1 펌프 = 약 1ml ) - 증상에 따라 조절 가능",
    },
    {
        "key": "urinary",
        "html_name": "monsmecta_renal_label.html",
        "print_name": "urinary_label_print.html",
        "name_ko": "몬스멕타 레날 디톡스",
        "name_en": "MONSMECTA RENAL DETOX",
        "sub_desc": "비뇨기 및 신장 건강 보조제",
        "theme": {
            "bg": "linear-gradient(135deg, #180b2d 0%, #0b071a 50%, #050d14 100%)",
            "border": "#6366f1",
            "grid": "#818cf8",
            "accent_bar": "linear-gradient(90deg, #6366f1, #a855f7, #ffd700, #6366f1)",
            "glow": "rgba(129, 140, 248, 0.9)",
            "divider": "linear-gradient(180deg, transparent, #818cf8, #ffd700, transparent)",
            "screen_bg": "#09090b",
            "screen_shadow": "rgba(129, 140, 248, 0.35)",
        },
        "effects_row1": [
            ("요소(Urea) 및 요독 배출 촉진", True),
            ("인독실설페이트 흡착 제거", True),
        ],
        "effects_row2": [
            ("신장 수치 안정화 보조", True),
            ("활력 증진 및 에너지 대사", True),
        ],
        "unit_desc": "1L 기준",
        "ingredients": [
            ("Montmorillonite (몬모릴로나이트)", "고함량"),
            ("Bifidobacterium longum", "1.0 x 10<sup style=\"font-size:0.75em; vertical-align:0.38em; font-family:'Noto Sans KR', sans-serif;\">11</sup> cfu"),
            ("비타민 A (Vitamin A)", "400,000 IU"),
            ("비타민 D3 (Vitamin D3)", "80,000 IU"),
            ("비타민 E (Vitamin E)", "200 IU"),
        ],
        "reg_amount": "바실러스 서브틸리스 1.0 x 10<sup style=\"font-size:0.75em; vertical-align:0.38em; font-family:'Noto Sans KR', sans-serif;\">6</sup> cfu/g 이상, 부형제( 정제수 )",
        "raw_mat_l1": "바실러스 서브틸리스, 비타민A, 아세트산 나트륨,",
        "raw_mat_l2": "프로피온산 나트륨, 포도당, 정제수",
        "feed_type": "보조사료/미생물제/바실러스 서브틸리스l액상l반려동물",
        "dose_main": "1일 1~2ml / 체중 5kg",
        "dose_sub": "( 1 펌프 = 약 1ml ) - 증상에 따라 조절 가능",
    },
    {
        "key": "probiotics",
        "html_name": "monsmecta_probiotics_label.html",
        "print_name": "probiotics_label_print.html",
        "name_ko": "몬스멕타 프로바이오틱스",
        "name_en": "MONSMECTA PROBIOTICS",
        "sub_desc": "세계 3대 유산균 듀퐁 다니스코 프리미엄 적용",
        "theme": {
            "bg": "linear-gradient(135deg, #071a2e 0%, #030e1a 50%, #020a12 100%)",
            "border": "#0284c7",
            "grid": "#38bdf8",
            "accent_bar": "linear-gradient(90deg, #0284c7, #38bdf8, #ffd700, #0284c7)",
            "glow": "rgba(56, 189, 248, 0.9)",
            "divider": "linear-gradient(180deg, transparent, #38bdf8, #ffd700, transparent)",
            "screen_bg": "#05111c",
            "screen_shadow": "rgba(56, 189, 248, 0.35)",
        },
        "effects_row1": [
            ("항생제 연관 설사 완화", True),
            ("장염 예방 보조", True),
        ],
        "effects_row2": [
            ("유해균 억제 및 장벽 방어력 강화", True),
            ("염증성 장질환(IBD) 완화", True),
        ],
        "unit_desc": "1L 기준",
        "ingredients": [
            ("Bacillus subtilis (바실러스 균)", "1.0 x 10⁷ CFU/g 이상"),
            ("듀퐁 다니스코 특화 유산균 18종", "1.0 x 10⁷ CFU/g 이상"),
            ("Montmorillonite (몬모릴로나이트)", "고함량"),
            ("비타민 A (상피세포 회복)", "적량"),
            ("프락토올리고당 (FOS 프리바이오틱스)", "적량"),
            ("포도당 및 전해질 복합제", "적량"),
        ],
        "reg_amount": "바실러스 서브틸리스 1.0 x 10⁷ CFU/g 이상, 듀퐁 다니스코 유산균 1.0 x 10⁷ CFU/g 이상",
        "raw_mat_l1": "바실러스 서브틸리스, 비타민A, 아세트산나트륨, 프로피온산나트륨,",
        "raw_mat_l2": "포도당, 몬모릴로나이트, 듀퐁 다니스코 특화 유산균, 정제수",
        "feed_type": "보조사료/미생물제/바실러스 서브틸리스l액상l반려동물",
        "dose_main": "1일 1~2ml / 체중 5kg",
        "dose_sub": "( 1 펌프 = 약 1ml ) - 증상에 따라 조절 가능",
    },
    {
        "key": "cancercare",
        "html_name": "monsmecta_cancercare_label.html",
        "print_name": "cancercare_label_print.html",
        "name_ko": "몬스멕타 캔서케어",
        "name_en": "MONSMECTA CANCERCARE",
        "sub_desc": "면역 증진 및 종양 억제 보조제",
        "theme": {
            "bg": "linear-gradient(135deg, #220726 0%, #100312 50%, #08030d 100%)",
            "border": "#9333ea",
            "grid": "#c084fc",
            "accent_bar": "linear-gradient(90deg, #9333ea, #c084fc, #ffd700, #9333ea)",
            "glow": "rgba(192, 132, 252, 0.9)",
            "divider": "linear-gradient(180deg, transparent, #c084fc, #ffd700, transparent)",
            "screen_bg": "#120214",
            "screen_shadow": "rgba(192, 132, 252, 0.35)",
        },
        "effects_row1": [
            ("체내 면역세포(NK/T) 활성화", True),
            ("종양 세포 증식 억제 보조", True),
        ],
        "effects_row2": [
            ("항암 치료 부작용 완화", True),
            ("염증성 악액질 방지 보조", True),
        ],
        "unit_desc": "1L 기준",
        "ingredients": [
            ("Montmorillonite (몬모릴로나이트)", "고함량"),
            ("Beta-glucan (베타글루칸)", "30,000mg"),
            ("Allicin (알리신)", "20,000mg"),
            ("Sulforaphane (설포라판)", "20,000mg"),
            ("Curcumin (커큐민)", "10,000mg"),
            ("Catechin (카테킨)", "10,000mg"),
            ("AFNC (천연복합추출물)", "10,000mg"),
        ],
        "reg_amount": "바실러스 서브틸리스 1.0 x 10⁷ CFU/g 이상, 부형제( 정제수 )",
        "raw_mat_l1": "바실러스 서브틸리스, 베타글루칸, 알리신, 설포라판, 커큐민,",
        "raw_mat_l2": "카테킨, AFNC, 몬모릴로나이트, 정제수",
        "feed_type": "보조사료/미생물제/바실러스 서브틸리스l액상l반려동물",
        "dose_main": "1일 1~2ml / 체중 5kg",
        "dose_sub": "( 1 펌프 = 약 1ml ) - 항암 식단 혼합 급여 권장",
    },
    {
        "key": "coldzero",
        "html_name": "monsmecta_coldzero_label.html",
        "print_name": "coldzero_label_print.html",
        "name_ko": "몬스멕타 콜드제로",
        "name_en": "MONSMECTA COLDZERO",
        "sub_desc": "호흡기 및 감기 예방 보조제",
        "theme": {
            "bg": "linear-gradient(135deg, #051f22 0%, #021114 50%, #010a0c 100%)",
            "border": "#0d9488",
            "grid": "#2dd4bf",
            "accent_bar": "linear-gradient(90deg, #0d9488, #2dd4bf, #ffd700, #0d9488)",
            "glow": "rgba(45, 212, 191, 0.9)",
            "divider": "linear-gradient(180deg, transparent, #2dd4bf, #ffd700, transparent)",
            "screen_bg": "#021214",
            "screen_shadow": "rgba(45, 212, 191, 0.35)",
        },
        "effects_row1": [
            ("쌍화 추출물 초기 감기 완화", True),
            ("호흡기 점막 면역 강화", True),
        ],
        "effects_row2": [
            ("기관지 윤활 및 마른 기침 완화", True),
            ("알레르기·비염 증상 개선", True),
        ],
        "unit_desc": "1L 기준",
        "ingredients": [
            ("Montmorillonite (몬모릴로나이트)", "고함량"),
            ("쌍화 복합 추출물 (Ssanghwa)", "100,000mg"),
            ("Quercetin (퀘르세틴)", "40,000mg"),
            ("Liriope (맥문동 추출물)", "30,000mg"),
            ("Ulmus (유근피 추출물)", "30,000mg"),
            ("Bacillus subtilis (고초균)", "적량"),
        ],
        "reg_amount": "바실러스 서브틸리스 1.0 x 10⁷ CFU/g 이상, 부형제( 정제수 )",
        "raw_mat_l1": "바실러스 서브틸리스, 퀘르세틴, 맥문동추출물, 유근피추출물,",
        "raw_mat_l2": "쌍화복합추출물, 몬모릴로나이트, 정제수",
        "feed_type": "보조사료/미생물제/바실러스 서브틸리스l액상l반려동물",
        "dose_main": "1일 1~2ml / 체중 5kg",
        "dose_sub": "( 1 펌프 = 약 1ml ) - 호흡기 증상 시 직접 급여 권장",
    },
    {
        "key": "skincare",
        "html_name": "monsmecta_skincare_label.html",
        "print_name": "skincare_label_print.html",
        "name_ko": "몬스멕타 스킨케어",
        "name_en": "MONSMECTA SKINCARE",
        "sub_desc": "피부 장벽 강화 및 아토피 개선 보조제",
        "theme": {
            "bg": "linear-gradient(135deg, #280518 0%, #14020b 50%, #0c0107 100%)",
            "border": "#e11d48",
            "grid": "#fb7185",
            "accent_bar": "linear-gradient(90deg, #e11d48, #fb7185, #ffd700, #e11d48)",
            "glow": "rgba(251, 113, 133, 0.9)",
            "divider": "linear-gradient(180deg, transparent, #fb7185, #ffd700, transparent)",
            "screen_bg": "#15020c",
            "screen_shadow": "rgba(251, 113, 133, 0.35)",
        },
        "effects_row1": [
            ("피부 장벽 각질층 복구", True),
            ("알러지 독소 흡착 배출", True),
        ],
        "effects_row2": [
            ("가려움증 즉각 억제", True),
            ("피부 모질 개선 및 탈모 방지", True),
        ],
        "unit_desc": "1L 기준",
        "ingredients": [
            ("Montmorillonite (초미세 나노)", "고함량"),
            ("Quercetin (퀘르세틴)", "40,000mg"),
            ("Bromelain (브로멜라인)", "30,000mg"),
            ("Omega-3 EPA/DHA (오메가3)", "30,000mg"),
            ("비타민 A (피부 상피세포 회복)", "적량"),
        ],
        "reg_amount": "바실러스 서브틸리스 1.0 x 10⁷ CFU/g 이상, 부형제( 정제수 )",
        "raw_mat_l1": "바실러스 서브틸리스, 퀘르세틴, 브로멜라인, 오메가3,",
        "raw_mat_l2": "몬모릴로나이트, 비타민A, 정제수",
        "feed_type": "보조사료/미생물제/바실러스 서브틸리스l액상l반려동물",
        "dose_main": "1일 1~2ml / 체중 5kg",
        "dose_sub": "( 1 펌프 = 약 1ml ) - 사료 혼합 또는 직접 경구 급여",
    },
    {
        "key": "heartcare",
        "html_name": "monsmecta_heartcare_label.html",
        "print_name": "heartcare_label_print.html",
        "name_ko": "몬스멕타 하트케어",
        "name_en": "MONSMECTA HEARTCARE",
        "sub_desc": "심장 및 혈행 건강 보조제",
        "theme": {
            "bg": "linear-gradient(135deg, #2b0507 0%, #140204 50%, #0a0102 100%)",
            "border": "#dc2626",
            "grid": "#f87171",
            "accent_bar": "linear-gradient(90deg, #dc2626, #f87171, #ffd700, #dc2626)",
            "glow": "rgba(248, 113, 113, 0.9)",
            "divider": "linear-gradient(180deg, transparent, #f87171, #ffd700, transparent)",
            "screen_bg": "#140102",
            "screen_shadow": "rgba(248, 113, 113, 0.35)",
        },
        "effects_row1": [
            ("심장 근육 수축력 강화", True),
            ("혈전 예방 및 혈류 개선", True),
        ],
        "effects_row2": [
            ("심부전 진행 지연 보조", True),
            ("혈압 안정화 및 심근 보호", True),
        ],
        "unit_desc": "1L 기준",
        "ingredients": [
            ("Coenzyme Q10 (코큐텐)", "25,000mg"),
            ("Hawthorn Extract (산사나무 열매 추출물)", "25,000mg"),
            ("L-Carnitine (L-카르니틴)", "25,000mg"),
            ("Taurine (타우린)", "25,000mg"),
            ("Omega-3 EPA/DHA (오메가3)", "25,000mg"),
        ],
        "reg_amount": "바실러스 서브틸리스 1.0 x 10⁷ CFU/g 이상, 부형제( 정제수 )",
        "raw_mat_l1": "바실러스 서브틸리스, 코큐텐(Q10), 산사나무열매추출물, L-카르니틴,",
        "raw_mat_l2": "타우린, 오메가3, 몬모릴로나이트, 정제수",
        "feed_type": "보조사료/미생물제/바실러스 서브틸리스l액상l반려동물",
        "dose_main": "1일 1~2ml / 체중 5kg",
        "dose_sub": "( 1 펌프 = 약 1ml ) - 식후 경구 급여 권장",
    },
    {
        "key": "jointcare",
        "html_name": "monsmecta_jointcare_label.html",
        "print_name": "jointcare_label_print.html",
        "name_ko": "몬스멕타 조인트케어",
        "name_en": "MONSMECTA JOINTCARE",
        "sub_desc": "관절 및 연골 건강 보조제",
        "theme": {
            "bg": "linear-gradient(135deg, #172005 0%, #0b1002 50%, #060901 100%)",
            "border": "#65a30d",
            "grid": "#a3e635",
            "accent_bar": "linear-gradient(90deg, #65a30d, #a3e635, #ffd700, #65a30d)",
            "glow": "rgba(163, 230, 53, 0.9)",
            "divider": "linear-gradient(180deg, transparent, #a3e635, #ffd700, transparent)",
            "screen_bg": "#0a1002",
            "screen_shadow": "rgba(163, 230, 53, 0.35)",
        },
        "effects_row1": [
            ("관절 연골 영양 공급", True),
            ("관절 염증 및 통증 완화", True),
        ],
        "effects_row2": [
            ("관절 윤활액 분비 촉진", True),
            ("관절염 진행 지연 보조", True),
        ],
        "unit_desc": "1L 기준",
        "ingredients": [
            ("MSM (식이유황)", "25,000mg"),
            ("초록입홍합 추출물 (Green Mussel)", "25,000mg"),
            ("Boswellia (보스웰리아)", "25,000mg"),
            ("Chondroitin (콘드로이친)", "25,000mg"),
            ("Omega-3 EPA/DHA (오메가3)", "25,000mg"),
        ],
        "reg_amount": "바실러스 서브틸리스 1.0 x 10⁷ CFU/g 이상, 부형제( 정제수 )",
        "raw_mat_l1": "바실러스 서브틸리스, MSM, 초록입홍합추출물, 보스웰리아,",
        "raw_mat_l2": "콘드로이친, 오메가3, 몬모릴로나이트, 정제수",
        "feed_type": "보조사료/미생물제/바실러스 서브틸리스l액상l반려동물",
        "dose_main": "1일 1~2ml / 체중 5kg",
        "dose_sub": "( 1 펌프 = 약 1ml ) - 사료 혼합 급여 권장",
    },
    {
        "key": "powerase",
        "html_name": "monsmecta_powerase_label.html",
        "print_name": "powerase_label_print.html",
        "name_ko": "몬스멕타 파워라제",
        "name_en": "MONSMECTA POWERASE",
        "sub_desc": "소화 효소 및 기력·활력 회복 보조제",
        "theme": {
            "bg": "linear-gradient(135deg, #291204 0%, #150902 50%, #0a0401 100%)",
            "border": "#ea580c",
            "grid": "#fb923c",
            "accent_bar": "linear-gradient(90deg, #ea580c, #fb923c, #ffd700, #ea580c)",
            "glow": "rgba(251, 146, 60, 0.9)",
            "divider": "linear-gradient(180deg, transparent, #fb923c, #ffd700, transparent)",
            "screen_bg": "#140801",
            "screen_shadow": "rgba(251, 146, 60, 0.35)",
        },
        "effects_row1": [
            ("3대 소화 효소 복합 분해", True),
            ("영양 흡수율 극대화", True),
        ],
        "effects_row2": [
            ("수술 후 빠른 회복 촉진", True),
            ("노령견/묘 기력 증진 보조", True),
        ],
        "unit_desc": "총량 기준",
        "ingredients": [
            ("Endo Protease (엔도 프로테아제)", "506,000 pu/g"),
            ("Alpha Amylase (알파 아밀라제)", "770 u/g"),
            ("Lipase (라이페이스)", "3,277 u/g"),
            ("Montmorillonite (몬모릴로나이트)", "고함량"),
            ("Bacillus subtilis (바실러스 균)", "1.0 x 10⁷ cfu/g"),
        ],
        "reg_amount": "바실러스 서브틸리스 1.0 x 10⁷ CFU/g 이상, 부형제( 정제수 )",
        "raw_mat_l1": "바실러스 서브틸리스, 엔도 프로테아제, 알파 아밀라제, 라이페이스,",
        "raw_mat_l2": "몬모릴로나이트, 포도당, 정제수",
        "feed_type": "보조사료/미생물제/바실러스 서브틸리스l액상l반려동물",
        "dose_main": "1일 1~2ml / 체중 5kg",
        "dose_sub": "( 1 펌프 = 약 1ml ) - 식전 또는 식후 급여",
    },
    {
        "key": "vitaplus",
        "html_name": "monsmecta_vitaplus_label.html",
        "print_name": "vitaplus_label_print.html",
        "name_ko": "몬스멕타 비타플러스",
        "name_en": "MONSMECTA VITAPLUS",
        "sub_desc": "종합 비타민 및 미네랄 보조제",
        "theme": {
            "bg": "linear-gradient(135deg, #2b2404 0%, #151102 50%, #0c0a01 100%)",
            "border": "#ca8a04",
            "grid": "#facc15",
            "accent_bar": "linear-gradient(90deg, #ca8a04, #facc15, #ffd700, #ca8a04)",
            "glow": "rgba(250, 204, 21, 0.9)",
            "divider": "linear-gradient(180deg, transparent, #facc15, #ffd700, transparent)",
            "screen_bg": "#141101",
            "screen_shadow": "rgba(250, 204, 21, 0.35)",
        },
        "effects_row1": [
            ("필수 비타민 10종 종합 공급", True),
            ("피로 회복 및 항산화 작용", True),
        ],
        "effects_row2": [
            ("활력 증진 및 대사 촉진", True),
            ("뼈·치아 건강 및 면역 강화", True),
        ],
        "unit_desc": "1L 기준",
        "ingredients": [
            ("Vitamin A (비타민A)", "750,000 IU"),
            ("Vitamin D3 (비타민D3)", "150,000 IU"),
            ("Vitamin E (비타민E)", "300 mg"),
            ("L-Methionine (L-메티오닌)", "300 mg"),
            ("L-Arginine (L-아르기닌)", "80 mg"),
            ("Montmorillonite (몬모릴로나이트)", "고함량"),
        ],
        "reg_amount": "바실러스 서브틸리스 1.0 x 10⁷ CFU/g 이상, 부형제( 정제수 )",
        "raw_mat_l1": "바실러스 서브틸리스, 비타민A, 비타민D3, 비타민E, L-메티오닌,",
        "raw_mat_l2": "L-아르기닌, 몬모릴로나이트, 포도당, 정제수",
        "feed_type": "보조사료/미생물제/바실러스 서브틸리스l액상l반려동물",
        "dose_main": "1일 1~2ml / 체중 5kg",
        "dose_sub": "( 1 펌프 = 약 1ml ) - 일일 활력 보충 급여",
    },
    {
        "key": "monsmecta",
        "html_name": "monsmecta_original_30ml_label.html",
        "print_name": "monsmecta_label_print.html",
        "name_ko": "몬스멕타 오리지널",
        "name_en": "MONSMECTA ORIGINAL",
        "sub_desc": "소화기 케어 및 장 점막 보호 솔루션",
        "theme": {
            "bg": "linear-gradient(135deg, #00281b 0%, #00150e 50%, #010a07 100%)",
            "border": "#059669",
            "grid": "#34d399",
            "accent_bar": "linear-gradient(90deg, #059669, #34d399, #ffd700, #059669)",
            "glow": "rgba(52, 211, 153, 0.9)",
            "divider": "linear-gradient(180deg, transparent, #34d399, #ffd700, transparent)",
            "screen_bg": "#01120b",
            "screen_shadow": "rgba(52, 211, 153, 0.35)",
        },
        "effects_row1": [
            ("장 질병 저항력 향상", True),
            ("연변 및 급성 설사 완화", True),
        ],
        "effects_row2": [
            ("장 점막 코팅 및 독소 흡착", True),
            ("장 기능 개선 및 정장 작용", True),
        ],
        "unit_desc": "1L 기준",
        "ingredients": [
            ("Montmorillonite (초미세 나노)", "고함량"),
            ("Bacillus subtilis (특허 고초균)", "1.0 x 10⁷ cfu/g"),
            ("1-DNJ 천연 성분 (천연 항균)", "고함량"),
            ("Glucose (포도당)", "적량"),
            ("Vitamin A (상피세포 회복)", "적량"),
            ("전해질 복합제 (Sodium acetate 등)", "적량"),
        ],
        "reg_amount": "바실러스 서브틸리스 1.0 x 10⁷ cfu/g 이상, 부형제( 정제수 )",
        "raw_mat_l1": "바실러스 서브틸리스, 비타민A, 아세트산나트륨, 프로피온산나트륨,",
        "raw_mat_l2": "포도당, 몬모릴로나이트, 정제수",
        "feed_type": "보조사료/미생물제/바실러스 서브틸리스l액상l반려동물",
        "dose_main": "1일 1~2ml / 체중 5kg",
        "dose_sub": "( 1 펌프 = 약 1ml ) - 연변·설사 시 1일 2~3회 증량",
    }
]

def generate_label_html(prod):
    t = prod["theme"]
    
    # Generate effects HTML
    effects_r1_html = "".join([f'<span class="eff-item"><span class="eff-dot"></span>{item[0]}</span>' for item in prod["effects_row1"]])
    effects_r2_html = "".join([f'<span class="eff-item"><span class="eff-dot"></span>{item[0]}</span>' for item in prod["effects_row2"]])
    
    # Generate ingredients rows
    ing_rows_html = ""
    for name, val in prod["ingredients"]:
        ing_rows_html += f"""
                    <div class="ing-row">
                        <span class="ing-name">{name}</span>
                        <span class="ing-val">{val}</span>
                    </div>"""
    
    # Main title font size adjustment if needed
    title_len = len(prod["name_ko"])
    title_size = "3.85mm" if title_len > 10 else "4.05mm"
    en_title_size = "1.52mm" if len(prod["name_en"]) > 20 else "1.65mm"
    
    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>{prod['name_en']} Label (85mm x 40mm)</title>
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
                background: {t['screen_bg']} !important;
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
                box-shadow: 0 25px 60px rgba(0, 0, 0, 0.95), 0 0 35px {t['screen_shadow']};
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
            background: {t['bg']};
            color: #f8fafc;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            border: 0.15mm solid {t['border']};
            flex-shrink: 0;
        }}

        .grid-overlay {{
            position: absolute;
            inset: 0;
            opacity: 0.08;
            background-image: 
                linear-gradient({t['grid']} 1px, transparent 1px),
                linear-gradient(90deg, {t['grid']} 1px, transparent 1px);
            background-size: 2.5mm 2.5mm;
            pointer-events: none;
            z-index: 1;
        }}

        /* 슬림 탑 엑센트 바 */
        .top-accent-bar {{
            height: 0.35mm;
            background: {t['accent_bar']};
            box-shadow: 0 0 1.2mm {t['glow']};
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
            padding: 0.25mm 0.55mm 0.25mm 0.55mm;
            justify-content: space-between;
        }}

        /* 좌측: 전면 메인 노출부 (너비 39.0mm) */
        .col-left {{
            width: 39.0mm;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}

        /* 중앙 디바이더 */
        .divider-col {{
            width: 0.4mm;
            height: 100%;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .divider-line {{
            width: 0.15mm;
            height: 98%;
            background: {t['divider']};
            opacity: 0.7;
        }}
        .divider-diamond {{
            position: absolute;
            width: 0.8mm;
            height: 0.8mm;
            background: #000;
            border: 0.15mm solid #ffd700;
            transform: rotate(45deg);
        }}

        /* 우측: 법정 고시사항 노출부 (너비 44.5mm) */
        .col-right {{
            width: 44.5mm;
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
            border: 0.15mm solid #ffd700;
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
            color: #ffd700;
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
            font-size: {title_size};
            font-weight: 900;
            color: #ffffff;
            line-height: 1.0;
            letter-spacing: -0.03em;
            text-shadow: 0 0 1.2mm rgba(255, 255, 255, 0.5), 0 1px 2px #000;
            margin-bottom: 0.04mm;
        }}
        .en-title {{
            font-size: {en_title_size};
            font-weight: 900;
            color: #ffd700;
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
            background: #ffd700;
            color: #000;
            border: 0.12mm solid #000;
            border-radius: 0.25mm;
            padding: 0.12mm 0.65mm;
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
            border: 0.15mm solid #ffd700;
            border-radius: 0.5mm;
            padding: 1.10mm 0.55mm 0.35mm 0.55mm;
            display: flex;
            flex-direction: column;
            gap: 0.26mm;
        }}
        .effects-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            line-height: 1.15;
            white-space: nowrap;
        }}
        .eff-item {{
            font-size: 1.26mm;
            font-weight: 800;
            color: #ffffff;
            display: inline-flex;
            align-items: center;
            gap: 0.25mm;
            line-height: 1;
            white-space: nowrap;
        }}
        .eff-dot {{
            width: 0.55mm;
            height: 0.55mm;
            border-radius: 50%;
            background: #ffd700;
            box-shadow: 0 0 0.3mm #ffd700;
            flex-shrink: 0;
        }}
        .eff-note {{
            font-size: 0.96mm;
            color: #fcd34d;
            font-weight: 700;
            line-height: 1;
            white-space: nowrap;
            opacity: 0.95;
        }}

        /* 성분 테이블 */
        .tech-box-ing {{
            background: rgba(0, 0, 0, 0.55);
            border: 0.15mm solid rgba(255, 215, 0, 0.35);
            border-radius: 0.5mm;
            padding: 0.25mm 0.55mm;
        }}
        .ing-header {{
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            border-bottom: 0.1mm solid rgba(255, 215, 0, 0.4);
            padding-bottom: 0.06mm;
            margin-bottom: 0.06mm;
        }}
        .ing-header .title {{
            font-size: 1.28mm;
            font-weight: 800;
            color: #fff;
        }}
        .ing-header .ref {{
            font-size: 1.08mm;
            color: #ffd700;
            font-weight: 800;
        }}
        .ing-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 1.14mm;
            line-height: 1.18;
            border-bottom: 0.05mm solid rgba(255, 255, 255, 0.08);
            padding: 0.04mm 0;
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
            font-size: 1.14mm;
        }}

        /* 포장단위 배지 */
        .pack-tag {{
            align-self: center;
            background: rgba(0, 0, 0, 0.65);
            border: 0.18mm solid #ffd700;
            border-radius: 999px;
            padding: 0.14mm 1.4mm;
            font-size: 1.28mm;
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
            color: #ffd700;
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
            padding: 0.20mm 0.55mm 0.15mm 0.55mm;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}

        /* 헤더: 성분등록번호 & 종류/명칭 */
        .legal-header {{
            border-bottom: 0.1mm solid rgba(255, 215, 0, 0.4);
            padding-bottom: 0.05mm;
            display: flex;
            flex-direction: column;
            gap: 0.04mm;
        }}
        .reg-num-line {{
            display: flex;
            justify-content: space-between;
            align-items: baseline;
        }}
        .reg-num-label {{
            font-size: 1.05mm;
            color: #ffd700;
            font-weight: 800;
            line-height: 1;
        }}
        .reg-num-val {{
            font-size: 1.25mm;
            font-weight: 900;
            color: #ffffff;
            line-height: 1;
        }}
        .feed-type-line {{
            font-size: 0.92mm;
            font-weight: 700;
            color: #e2e8f0;
            line-height: 1.15;
            white-space: nowrap;
        }}
        .feed-type-line .lbl {{
            color: #ffd700;
            font-weight: 800;
        }}

        /* 1. 고시 본문 영역: 모든 노란색 소제목 좌측선(left: 0) 완벽 일치 */
        .sec-content {{
            display: flex;
            flex-direction: column;
            gap: 0.14mm;
            margin: 0.04mm 0;
            text-align: left;
        }}
        
        .info-row {{
            display: flex;
            align-items: baseline;
            font-size: 1.00mm;
            line-height: 1.18;
            color: #f8fafc;
            text-align: left;
        }}
        .sec-lbl {{
            font-weight: 800;
            color: #ffd700;
            margin-right: 0.3mm;
            white-space: nowrap;
            flex-shrink: 0;
            text-align: left;
        }}
        .sec-val {{
            color: #ffffff;
            font-weight: 700;
            flex: 1;
        }}

        /* 2. 사용한 원료의 명칭: 2줄 넉넉하게 + 둘째줄 '바'자 밑 좌측 줄맞춤 */
        .materials-val-box {{
            display: flex;
            flex-direction: column;
            gap: 0.04mm;
            flex: 1;
            color: #f8fafc;
            font-weight: 600;
            line-height: 1.16;
        }}

        /* 효과 3가지 리스트 */
        .effects-sub-list {{
            list-style: none;
            padding-left: 0.6mm;
            display: flex;
            flex-direction: column;
            gap: 0.03mm;
            margin: 0.02mm 0;
        }}
        .effects-sub-list li {{
            font-size: 0.98mm;
            font-weight: 600;
            color: #f1f5f9;
            line-height: 1.15;
            display: flex;
            align-items: baseline;
        }}
        .effects-sub-list .roman {{
            color: #ffd700;
            font-weight: 800;
            margin-right: 0.25mm;
            flex-shrink: 0;
        }}

        /* 용법 및 용량 */
        .dose-box {{
            background: rgba(212, 175, 55, 0.18);
            border: 0.12mm solid #ffd700;
            border-radius: 0.35mm;
            padding: 0.16mm 0.45mm;
            display: flex;
            align-items: baseline;
            justify-content: space-between;
            line-height: 1.15;
            box-sizing: border-box;
            flex-wrap: wrap;
            gap: 0.2mm;
        }}
        .dose-title {{
            font-size: 1.08mm;
            font-weight: 900;
            color: #ffd700;
            white-space: nowrap;
        }}
        .dose-desc {{
            font-size: 1.16mm;
            font-weight: 900;
            color: #ffffff;
            white-space: nowrap;
        }}
        .dose-sub {{
            font-size: 0.94mm;
            color: #f1f5f9;
            font-weight: 700;
            white-space: nowrap;
        }}

        /* 4. 주의사항 박스: 상하폭 넓힘 + 1), 2), 3) 간격 균일화 + 테두리 여백 확보 */
        .warn-box {{
            background: rgba(220, 38, 38, 0.15);
            border: 0.15mm solid rgba(239, 68, 68, 0.65);
            border-radius: 0.45mm;
            padding: 0.35mm 0.6mm 0.35mm 0.6mm;
            box-sizing: border-box;
            margin: 0.1mm 0;
        }}
        .warn-title {{
            font-size: 1.06mm;
            font-weight: 800;
            color: #f87171;
            display: flex;
            align-items: center;
            gap: 0.25mm;
            line-height: 1;
            margin-bottom: 0.15mm;
        }}
        .warn-list {{
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 0.12mm;
        }}
        .warn-item {{
            font-size: 0.96mm;
            color: #f8fafc;
            line-height: 1.20;
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
            color: #ffd700;
            text-decoration: underline;
            text-decoration-thickness: 0.12mm;
            text-underline-offset: 0.12mm;
            font-weight: 800;
        }}

        /* 3. 제조 및 유통기한 바 & 재활용 표식 상단 배치 (위로 2줄 이상 올림) */
        .mfg-exp-bar-with-recycle {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 0.1mm solid rgba(255, 255, 255, 0.2);
            border-bottom: 0.1mm solid rgba(255, 255, 255, 0.2);
            padding: 0.12mm 0.25mm;
            line-height: 1;
            box-sizing: border-box;
        }}
        .mfg-exp-info {{
            display: flex;
            align-items: center;
            gap: 1.2mm;
            font-size: 1.00mm;
            font-weight: 700;
            color: #e2e8f0;
        }}
        .mfg-exp-info .lbl {{
            color: #cbd5e1;
            margin-right: 0.2mm;
        }}
        .mfg-exp-info .val {{
            color: #ffffff;
            font-weight: 800;
        }}

        /* 3. 단정하고 깔끔한 재활용 표식 (선 삐져나옴 0% 완벽 차단) */
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
            font-size: 0.82mm;
            font-weight: 900;
            color: #ffffff;
            line-height: 1;
            letter-spacing: 0.02em;
        }}

        /* 제조원 및 판매원 풋터 (노란 소제목 좌측 정렬) */
        .legal-footer {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            padding-top: 0.08mm;
            gap: 0.4mm;
        }}
        .company-block {{
            display: flex;
            align-items: flex-start;
            gap: 0.3mm;
        }}
        .company-logo-circle {{
            width: 3.2mm;
            height: 3.2mm;
            border-radius: 50%;
            background: #fff;
            border: 0.15mm solid #ffd700;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            flex-shrink: 0;
            box-shadow: 0 0 0.6mm rgba(255, 215, 0, 0.6);
            margin-top: 0.05mm;
        }}
        .company-logo-circle img {{
            width: 100%;
            height: 100%;
            object-fit: contain;
            padding: 0.06mm;
        }}
        .company-info {{
            font-size: 0.86mm;
            color: #f1f5f9;
            line-height: 1.16;
            font-weight: 600;
            text-align: left;
        }}
        .company-info .co-title {{
            font-weight: 800;
            color: #ffd700;
            font-size: 0.94mm;
        }}
        .company-info .co-title .co-name {{
            color: #ffffff;
            font-weight: 800;
        }}
        .company-info .co-addr {{
            color: #cbd5e1;
        }}
        .company-info .tel-accent {{
            color: #ffd700;
            font-weight: 800;
        }}
    </style>
</head>
<body>

<div class="no-print" style="position:fixed; top:12px; left:50%; transform:translateX(-50%); z-index:99999; background:rgba(15,23,42,0.95); border:1px solid #ffd700; padding:10px 24px; border-radius:12px; display:flex; align-items:center; gap:16px; box-shadow:0 10px 30px rgba(0,0,0,0.8); font-family:sans-serif;">
    <div style="color:#fff; font-size:13px; font-weight:700;">
        <span style="color:#ffd700;">★ {prod['name_ko']} (85mm × 40mm)</span> | 소제목 좌측 정렬 · 원료명칭 2줄 줄맞춤 · 주의사항 박스 확장 · 재활용 상단 이동
    </div>
    <button onclick="window.print()" style="background:linear-gradient(135deg, #ffd700, #b8860b); color:#000; font-weight:800; font-size:13px; padding:6px 16px; border:none; border-radius:8px; cursor:pointer;">
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
                    <div class="sub-desc">{prod['sub_desc']}</div>
                    <h1 class="main-title">{prod['name_ko']}</h1>
                    <h2 class="en-title orbitron">{prod['name_en']}</h2>
                </div>

                <!-- 핵심 효능 박스 -->
                <div class="effects-box-wrapper">
                    <div class="effects-badge-top">핵심 효능</div>
                    <div class="effects-card">
                        <div class="effects-row">
                            {effects_r1_html}
                        </div>
                        <div class="effects-row">
                            {effects_r2_html}
                            <span class="eff-note">(*등의 개선에 도움)</span>
                        </div>
                    </div>
                </div>

                <!-- Ingredients Table (주요 성분량) -->
                <div class="tech-box-ing">
                    <div class="ing-header">
                        <span class="title">주요 성분량</span>
                        <span class="ref">{prod['unit_desc']}</span>
                    </div>
                    {ing_rows_html}
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
                        <div class="reg-num-line">
                            <span class="reg-num-label">사료의 성분등록번호 :</span>
                            <span class="reg-num-val">제 XX9UY0145호</span>
                        </div>
                        <div class="feed-type-line">
                            <span class="lbl">사료의 종류와 명칭 / 형태 / 용도 :</span> {prod['feed_type']}
                        </div>
                    </div>

                    <!-- 1 & 2. 고시 본문: 모든 노란 소제목 좌측선 일치 + 사용한 원료 명칭 2줄 '바'자 밑 정렬 -->
                    <div class="sec-content">
                        <!-- 등록성분량 -->
                        <div class="info-row">
                            <span class="sec-lbl">등록성분량 :</span>
                            <span class="sec-val">{prod['reg_amount']}</span>
                        </div>

                        <!-- 2. 사용한 원료의 명칭 (2줄 넉넉하게 + 둘째줄 '바'자 밑 정렬) -->
                        <div class="info-row">
                            <span class="sec-lbl">사용한 원료의 명칭 :</span>
                            <div class="materials-val-box">
                                <div>{prod['raw_mat_l1']}</div>
                                <div>{prod['raw_mat_l2']}</div>
                            </div>
                        </div>

                        <!-- 1. 대상 (좌측선 칼맞춤) -->
                        <div class="info-row">
                            <span class="sec-lbl">대상 :</span>
                            <span class="sec-val">반려견, 반려묘</span>
                        </div>

                        <!-- 1. 효과 (좌측선 칼맞춤) -->
                        <div class="info-row">
                            <span class="sec-lbl">효과 :</span>
                        </div>
                        <ul class="effects-sub-list">
                            <li><span class="roman">I.</span>장 관련 질병( 파보, 로타, 코로나 등 )에 대한 저항력 향상에 도움</li>
                            <li><span class="roman">II.</span>면역 기능 및 건강 상태 유지에 도움</li>
                            <li><span class="roman">III.</span>장 기능 개선 및 정장 작용에 도움</li>
                        </ul>
                    </div>

                    <!-- 용법 및 용량 -->
                    <div class="dose-box">
                        <div style="display:flex; align-items:baseline; gap:0.3mm;">
                            <span class="dose-title">용법 및 용량 :</span>
                            <span class="dose-desc">{prod['dose_main']}</span>
                        </div>
                        <span class="dose-sub">{prod['dose_sub']}</span>
                    </div>

                    <!-- 4. 주의사항 박스: 상하폭 넓힘 + 1), 2), 3) 간격 균등화 + 테두리 여백 확보 -->
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

                    <!-- 3. 제조 및 유통기한 바 & 재활용 표식 (위로 2줄 이상 올림!) -->
                    <div class="mfg-exp-bar-with-recycle">
                        <div class="mfg-exp-info">
                            <div><span class="lbl">포장 단위 :</span><span class="val">30ml</span></div>
                            <div><span class="lbl">제조일자 :</span><span class="val">2026년 9월 15일</span></div>
                            <div><span class="lbl">유통기한 :</span><span class="val">제조일로부터 18 개월</span></div>
                        </div>

                        <!-- 3. 재활용 표식: 위로 2줄 이상 올림 -->
                        <div class="recycle-badge-raised">
                            <div class="recycle-icon-wrap">
                                <svg class="recycle-icon" viewBox="0 0 100 100">
                                    <path d="M50 14 L88 80 L12 80 Z" fill="none" stroke="#ffd700" stroke-width="7" stroke-linejoin="round"/>
                                </svg>
                                <span class="recycle-text">플라스틱</span>
                            </div>
                            <span class="recycle-sub">OTHER</span>
                        </div>
                    </div>

                    <!-- 판매원 / 제조원 풋터 (노란색 소제목 좌측선 맞춤 정렬) -->
                    <div class="legal-footer">
                        <!-- 판매원: 에스앤제이 동물병원 -->
                        <div class="company-block">
                            <div class="company-logo-circle">
                                <img src="{data_uri_logo}" alt="에스앤제이 동물병원">
                            </div>
                            <div class="company-info">
                                <div><span class="co-title">판매원 :</span> <span class="co-name">에스앤제이 동물병원</span></div>
                                <div class="co-addr">주소 : 경기도 용인시 포곡읍 선장1로 98-8</div>
                                <div>전화번호 : <span class="tel-accent">031-321-6562</span></div>
                            </div>
                        </div>

                        <!-- 제조원: ㈜엠오바이오 -->
                        <div class="company-block">
                            <div class="company-info">
                                <div><span class="co-title">제조원 :</span> <span class="co-name">㈜엠오바이오</span></div>
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
"""
    return html

def main():
    print(f"Generating 30ml 85x40mm labels for all products...")
    
    # Target directories
    targets = [
        LABELS_DIR,
        "/home/hongsoonil02/agrolib/monsmecta_labels_v2_modern_20260809_185950_CENTERED/labels"
    ]
    
    for prod in PRODUCTS:
        html_content = generate_label_html(prod)
        
        # 1. Write to monsmecta/public/assets/labels
        # Main label file (e.g. monsmecta_cancercare_label.html)
        file1 = os.path.join(LABELS_DIR, prod["html_name"])
        with open(file1, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Generated: {file1}")
        
        # Print modal file (e.g. cancercare_label_print.html)
        file2 = os.path.join(LABELS_DIR, prod["print_name"])
        with open(file2, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Updated Print File: {file2}")
        
        # 2. Sync to agrolib
        agrolib_dir = targets[1]
        if os.path.exists(agrolib_dir):
            file_agro = os.path.join(agrolib_dir, prod["print_name"].replace(".html", "_v2_modern.html"))
            with open(file_agro, "w", encoding="utf-8") as f:
                f.write(html_content)
            print(f"Synced to agrolib: {file_agro}")
            
    print("\nAll label HTML files successfully generated and synchronized!")

if __name__ == "__main__":
    main()
