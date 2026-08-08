import os

out_dir = r"c:\Users\master\monsmecta-landing\public\assets\labels"
os.makedirs(out_dir, exist_ok=True)

products = [
    {
        "id": "monsmecta",
        "name_ko": "몬스멕타 오리지널",
        "name_en": "MONSMECTA ORIGINAL",
        "desc": "장 건강 보조 및 장내 환경 개선",
        "color1": "#00513b", "color2": "#001a13",
        "neon": "#10b981", # emerald-500
        "effects": ["장내 유해물질 흡착 배출", "설사 및 연변 개선", "장 점막 보호 및 회복", "장내 미생물 균형 유지"],
        "ingredients": [
            ("Smectite (스멕타이트)", "200g"),
            ("L-glutamine (L-글루타민)", "5,000mg"),
            ("Zinc (아연)", "500mg"),
            ("Probiotics (프로바이오틱스)", "1x10^9 CFU")
        ]
    },
    {
        "id": "hepamax",
        "name_ko": "몬스멕타 헤파맥스",
        "name_en": "MONSMECTA HEPAMAX",
        "desc": "간 기능 보호 및 해독 활성화",
        "color1": "#3A0F0F", "color2": "#0B1515", 
        "neon": "#D4AF37", # Gold
        "effects": ["간 건강 개선", "장 건강 개선", "지방간 개선", "항병력 증진", "질병 회복 촉진"],
        "ingredients": [
            ("Smectite (스멕타이트)", "200g"),
            ("L-glutamine & Zinc & Probiotics", "베이스 배합"),
            ("Taurine (타우린)", "200mg"),
            ("D-Sorbitol (D-소르비톨)", "4.5g"),
            ("L-lysine HCl", "30mg"),
            ("L-methionine", "30mg"),
            ("Vitamin B12", "100μg")
        ]
    },
    {
        "id": "cancercare",
        "name_ko": "몬스멕타 캔서케어",
        "name_en": "MONSMECTA CANCERCARE",
        "desc": "면역 증진 및 종양 억제 보조제",
        "color1": "#2B0A2B", "color2": "#0B1515",
        "neon": "#a855f7", # purple-500
        "effects": ["강력한 면역 세포 활성화", "종양 억제 보조 기전", "항암 치료 시 부작용 완화", "염증 반응 감소"],
        "ingredients": [
            ("Montmorillonite (요독 흡착 핵심성분)", "고함량"),
            ("Beta-glucan (베타글루칸)", "30,000mg"),
            ("Allicin (알리신)", "20,000mg"),
            ("Sulforaphane (설포라판)", "20,000mg"),
            ("Curcumin (커큐민)", "10,000mg"),
            ("Catechin (카테킨)", "10,000mg"),
            ("AFNC (천연복합추출물)", "10,000mg")
        ]
    },
    {
        "id": "coldzero",
        "name_ko": "몬스멕타 콜드제로",
        "name_en": "MONSMECTA COLDZERO",
        "desc": "호흡기 및 감기 예방 보조제",
        "color1": "#0A2B2B", "color2": "#0B1515",
        "neon": "#06b6d4", # cyan-500
        "effects": ["쌍화 복합 추출물로 기력 회복 및 초기 감기 완화", "호흡기 점막 면역 강화 및 기관지 윤활", "비염, 마른 기침, 호흡 곤란 증상 완화", "천연 항염증제로 호흡기 알레르기 억제"],
        "ingredients": [
            ("Montmorillonite (요독 흡착 핵심성분)", "고함량"),
            ("Ssanghwa Extract (쌍화 복합 추출물)", "100,000mg"),
            ("Quercetin (퀘르세틴)", "40,000mg"),
            ("Liriope (맥문동)", "30,000mg"),
            ("Ulmus (유근피)", "30,000mg")
        ]
    },
    {
        "id": "skincare",
        "name_ko": "몬스멕타 스킨케어",
        "name_en": "MONSMECTA SKINCARE",
        "desc": "피부 및 아토피 개선 보조제",
        "color1": "#2B0A1A", "color2": "#0B1515",
        "neon": "#ec4899", # pink-500
        "effects": ["피부 장벽 강화 및 재생", "가려움증 및 발적 완화", "아토피 등 알러지 억제", "모질 개선 및 탈모 방지"],
        "ingredients": [
            ("Omega-3 EPA/DHA", "15,000mg"),
            ("Ceramide (세라마이드)", "1,000mg"),
            ("Biotin (비오틴)", "50,000μg"),
            ("Zinc (아연)", "800mg")
        ]
    },
    {
        "id": "heartcare",
        "name_ko": "몬스멕타 하트케어",
        "name_en": "MONSMECTA HEARTCARE",
        "desc": "심장 및 혈행 건강 보조제",
        "color1": "#2B0A0E", "color2": "#0B1515",
        "neon": "#ef4444", # red-500
        "effects": ["심장 근육 수축력 강화", "혈전 예방 및 혈류 개선", "심부전 진행 지연 보조", "혈압 정상화 보조"],
        "unit_desc": "1L 기준",
        "ingredients": [
            ("Coenzyme Q10 (코큐텐)", "25,000mg (배합비중 20%)"),
            ("Hawthorn Extract (산사나무 열매 추출물)", "25,000mg (배합비중 10%)"),
            ("L-carnitine (L-카르니틴)", "25,000mg (배합비중 10%)"),
            ("Taurine (타우린)", "25,000mg (배합비중 5%)"),
            ("Omega-3 EPA/DHA (오메가3)", "25,000mg (배합비중 5%)")
        ]
    },
    {
        "id": "jointcare",
        "name_ko": "몬스멕타 조인트케어",
        "name_en": "MONSMECTA JOINTCARE",
        "desc": "관절 및 연골 건강 보조제",
        "color1": "#1A1A0A", "color2": "#0B1515",
        "neon": "#84cc16", # lime-500
        "effects": ["관절 연골 영양 공급", "관절 염증 및 통증 완화", "관절 윤활액 증가 보조", "관절염 진행 지연"],
        "unit_desc": "1L 기준",
        "ingredients": [
            ("MSM (식이유황)", "25,000mg (배합비중 20%)"),
            ("Green Lipped Mussel Extract (그린립 머슬 추출물)", "25,000mg (배합비중 10%)"),
            ("Boswellia (보스웰리아)", "25,000mg (배합비중 10%)"),
            ("Chondroitin (콘드로이친)", "25,000mg (배합비중 5%)"),
            ("Omega-3 EPA/DHA (오메가3)", "25,000mg (배합비중 5%)")
        ]
    },
    {
        "id": "powerase",
        "name_ko": "몬스멕타 파워라제",
        "name_en": "MONSMECTA POWERASE",
        "desc": "기력 및 활력 회복 보조제",
        "color1": "#2B1A0A", "color2": "#0B1515",
        "neon": "#f97316", # orange-500
        "effects": ["단백질·지방·탄수화물 3대 소화 효소 복합 배합", "소화 기능 개선 및 영양 흡수 촉진", "수술 후 빠른 회복 촉진", "노령견/묘 기력 증진 및 대사 활성화"],
        "ingredients": [
            ("Endo Protease (엔도 프로테아제)", "506,000 pu/g"),
            ("Alpha Amylase (알파 아밀라제)", "770 u/g"),
            ("Lipase (라이페이스)", "3,277 u/g")
        ]
    },
    {
        "id": "probiotics",
        "name_ko": "몬스멕타 프로바이오틱스",
        "name_en": "MONSMECTA PROBIOTICS",
        "desc": "세계 3대 유산균 듀퐁 다니스코 프리미엄 적용",
        "color1": "#0A2B11", "color2": "#0B1515",
        "neon": "#22c55e", # green-500
        "effects": ["[Premium] 듀퐁 다니스코 프리미엄 균주 적용", "항생제 연관 설사 및 장염 예방 보조", "염증성 장질환 및 IBS 증상 완화", "유해균 억제 및 장벽 방어력 강화"],
        "registered_ingredients": "바실러스 서브틸리스 1.0 x 10⁷ CFU/g 이상, 듀퐁 다니스코 특화 유산균 1.0 x 10⁷ CFU/g 이상",
        "ingredients": [
            ("Bacillus subtilis (바실러스 균)", "1.0x10^10 CFU"),
            ("세계 3대 유산균 듀퐁 다니스코 프리미엄", "1.0x10^10 CFU"),
            ("└ 생물학적 보호 기술(안정성 극대화)", "핵심 균주"),
            ("└ 위산 및 담즙산 통과 생존력 우수", "핵심 균주"),
            ("└ L. plantarum 등 18종 복합 배합", "핵심 균주"),
            ("└ 우수한 장내 정착 및 증식 작용", "핵심 균주")
        ]
    },
    {
        "id": "urinary",
        "name_ko": "몬스멕타 유리너리",
        "name_en": "MONSMECTA URINARY",
        "desc": "비뇨기 및 신장 건강 보조제",
        "color1": "#120A2B", "color2": "#0B1515",
        "neon": "#6366f1", # indigo-500
        "effects": ["요소(Urea) 및 요독 배출 촉진", "인독실설페이트 흡착 제거", "신장 수치 안정화 보조", "활력 증진 및 에너지 대사"],
        "unit_desc": "1L 기준 (괄호 안은 1ml 당 함량)",
        "ingredients": [
            ("Smectite (스멕타이트)", "200g"),
            ("L-glutamine & Zinc & Probiotics", "베이스 배합"),
            ("└ 비타민 A (Vitamin A)", "400,000 IU (400 IU)"),
            ("└ 비타민 D3 (Vitamin D3)", "80,000 IU (80 IU)"),
            ("└ 비타민 E (Vitamin E)", "200 IU (0.2 IU)"),
            ("└ 비타민 B1, B2, C", "각 100mg (0.1mg)"),
            ("└ 니코틴산아미드", "300mg (0.3mg)"),
            ("└ 판토텐산 칼슘", "100mg (0.1mg)")
        ]
    },
    {
        "id": "vitaplus",
        "name_ko": "몬스멕타 비타플러스",
        "name_en": "MONSMECTA VITAPLUS",
        "desc": "종합 비타민 및 미네랄 보조제",
        "color1": "#2B2A0A", "color2": "#0B1515",
        "neon": "#eab308", # yellow-500
        "effects": ["필수 비타민 고함량 복합 배합", "필수 아미노산 및 보조 성분 배합", "피로 회복 및 항산화 작용", "뼈·치아 건강 및 대사 활성화"],
        "ing_list_class": "space-y-1 text-[15px]",
        "raw_materials": "비타민A, 비타민C, 비타민D3, 비타민E, 비타민K3, 비타민B1, 비타민B6, 비타민B12, 니코틴아미드, 판토텐산칼슘, L-메티오닌, 염산라이신, 정제수",
        "ingredients": [
            ("Vit A (비타민A)", "750,000 IU"),
            ("Vit C (비타민C)", "299.9 mg"),
            ("Vit D3 (비타민D3·콜레칼시페롤)", "150,000 IU"),
            ("Vit E 50% (비타민E)", "300 IU"),
            ("Vit K3 (비타민K3·메나디온) 50%", "200 mg"),
            ("Vit B1 HCl (비타민B1) 99%", "203 mg"),
            ("Vit B6 (비타민B6·피리독신)", "98 mg"),
            ("Vit B12 (비타민B12·코발라민)", "1 mg"),
            ("Nicotinamide (니코틴아미드)", "500 mg"),
            ("Calcium Pantothenate (판토텐산칼슘)", "300 mg"),
            ("L-Methionine (L-메티오닌)", "300 mg"),
            ("Lysine HCl (라이신)", "500 mg")
        ]
    }
]

template = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=1250">
    <title>{name_en} High-Tech Label</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&family=Orbitron:wght@700;900&display=swap" rel="stylesheet">
    <style>
        * {{ word-break: keep-all; overflow-wrap: break-word; }}
        body {{ font-family: 'Noto Sans KR', sans-serif; }}
        .orbitron {{ font-family: 'Orbitron', sans-serif; }}
        .cyber-bg {{ background: linear-gradient(135deg, {color1} 0%, {color2} 100%); }}
        .glass-panel {{ background: rgba(0, 0, 0, 0.4); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3); border-top: 1px solid rgba(255,255,255,0.2); border-left: 1px solid rgba(255,255,255,0.2); }}
        .neon-text {{ color: {neon}; text-shadow: 0 0 5px {neon}, 0 0 10px {neon}; }}
        .neon-border {{ border-color: {neon}; box-shadow: 0 0 10px {neon} inset, 0 0 10px {neon}; }}
        @media print {{
            @page {{ size: A4 portrait; margin: 0; }}
            body {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; background: white !important; margin: 0; padding: 0; }}
            #label-container {{ width: 900px !important; zoom: 0.8; transform-origin: top center; margin: 0; border: none !important; box-shadow: none !important; }}
        }}
        
        .pet-icon-svg {{
            width: 144px; height: 144px;
            fill: {neon};
            filter: drop-shadow(0 0 8px {neon});
        }}
    </style>
</head>
<body class="bg-gray-900 flex items-center justify-center min-h-screen p-4">
    <div class="scale-[0.5] origin-center">
        <div id="label-container" class="cyber-bg text-gray-100 w-[2375px] h-[1125px] shrink-0 rounded-[40px] overflow-hidden border-[8px] border-[#8B7355] relative flex flex-col">
            
            <div class="absolute inset-0 opacity-10" style="background-image: linear-gradient({neon} 1px, transparent 1px), linear-gradient(90deg, {neon} 1px, transparent 1px); background-size: 50px 50px;"></div>
            
            <div class="h-4 shrink-0 bg-[{neon}] shadow-[0_0_15px_{neon}] relative z-10"></div>
            
            <div class="px-14 py-10 relative z-10 h-full flex flex-col justify-between">
                <div class="flex flex-row gap-16 justify-between h-full">
                    
                    <div class="w-[45%] flex flex-col justify-between h-full pr-4 relative">
                        <div class="flex flex-col items-center justify-center pt-2">
                            <div class="flex items-center gap-6 mb-6">
                                <span class="text-[72px] drop-shadow-[0_0_15px_{neon}]">🐶</span>
                                <div class="inline-block bg-black/50 border border-[{neon}] rounded-full px-8 py-3">
                                    <span class="text-[20px] font-bold text-gray-300 tracking-[0.2em] uppercase"><span class="neon-text">S&J</span> ADVANCED VET FORMULA</span>
                                </div>
                                <span class="text-[72px] drop-shadow-[0_0_15px_{neon}]">🐱</span>
                            </div>
                            
                            <p class="text-[24px] font-medium text-gray-400 mb-2 tracking-wide">{desc}</p>
                            <h1 class="text-[85px] font-black text-white tracking-tight leading-none mb-3 drop-shadow-[0_0_10px_rgba(255,255,255,0.3)]">{name_ko}</h1>
                            <h2 class="text-[36px] font-bold orbitron neon-text tracking-[0.1em]">{name_en}</h2>
                        </div>

                        <div class="bg-black/40 border border-white/10 px-8 py-4 rounded-3xl relative">
                            <div class="absolute -top-4 left-6 bg-white/10 backdrop-blur-md px-4 py-1 rounded-lg border border-white/20">
                                <span class="font-bold text-white tracking-wide">핵심 효능</span>
                            </div>
                            <ul class="grid grid-cols-3 gap-y-2 gap-x-6 text-[18px] font-bold text-gray-200 tracking-tight mt-2">
                                {effects_html}
                            </ul>
                        </div>

                        <div class="bg-black/40 border border-white/10 px-8 py-5 rounded-3xl relative">
                            <div class="flex justify-between items-end mb-4 border-b border-white/20 pb-3">
                                <h3 class="text-[26px] font-bold text-white flex items-center gap-3">
                                    주요 성분 데이터
                                </h3>
                                <div class="bg-white/10 backdrop-blur-md px-3 py-1 rounded border border-white/20 text-[15px] text-[{neon}]">{unit_desc}</div>
                            </div>
                            <ul class="{ing_list_class} font-medium">
                                {ingredients_html}
                            </ul>
                        </div>
                        
                        <div class="flex justify-center pb-2">
                            <div class="border border-[{neon}]/50 rounded-full px-8 py-2 bg-black/40">
                                <span class="text-white text-[22px] font-bold">포장단위 :</span>
                                <span class="text-[{neon}] text-[24px] font-bold ml-2">{weight_str}</span>
                            </div>
                        </div>
                    </div>
                    
                    <div class="w-[4px] shrink-0 bg-gradient-to-b from-transparent via-[{neon}] to-transparent opacity-50 relative">
                        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-8 h-8 border-4 border-[{neon}] rotate-45 bg-black"></div>
                    </div>
                    
                    <div class="w-[50%] flex flex-col h-full pl-4 relative">
                        
                        <div class="glass-panel p-8 rounded-3xl h-full flex flex-col justify-between relative z-10">
                            
                            <div class="flex justify-between items-start border-b border-white/20 pb-4">
                                <div>
                                    <div class="text-[14px] text-[{neon}] mb-1 font-bold">사료 성분등록번호</div>
                                    <div class="text-[22px] font-bold text-white">제XX9UY0145호</div>
                                </div>
                                <div class="text-right">
                                    <div class="text-[16px] text-gray-400 mb-1">사료의 종류 및 명칭 / 형태 / 용도</div>
                                    <div class="text-[22px] font-bold text-white">보조사료 / 미생물제 / 바실러스 서브틸리스 / 액상 / 반려동물용</div>
                                </div>
                            </div>
                            
                            <div>
                                <div class="text-[18px] text-[{neon}] font-bold mb-2">등록성분량</div>
                                <div class="text-[18px] font-medium text-white">바실러스 서브틸리스 1.0 x 10^7 CFU/g 이상, 부형제(정제수)</div>
                            </div>
                            
                            <div>
                                <div class="text-[18px] text-[{neon}] font-bold mb-2">사용한 원료의 명칭</div>
                                <div class="text-[18px] text-gray-300 leading-relaxed font-medium">{raw_materials}</div>
                            </div>
                            
                            <div>
                                <div class="text-[18px] text-[{neon}] font-bold mb-2">대상축종</div>
                                <div class="text-[20px] font-bold text-white">반려견 · 반려묘</div>
                            </div>
                            
                            <div class="bg-[{neon}]/10 border border-[{neon}]/30 p-6 rounded-2xl">
                                <div class="text-[18px] text-[{neon}] font-bold mb-2">용법 및 용량</div>
                                <div class="text-[26px] font-bold text-white">체중 5kg 당 1일 1회 2ml 급여 <span class="text-[16px] text-gray-400 font-normal ml-2">(1 펌프/스포이드 = 약 1ml)</span></div>
                            </div>
                            
                            <div>
                                <div class="bg-black/40 border border-red-500/30 p-5 rounded-2xl mb-4">
                                    <div class="text-[18px] font-bold text-red-400 flex items-center gap-2 mb-3">
                                        <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd"></path></svg>
                                        주의사항
                                    </div>
                                    <ul class="list-disc pl-6 space-y-1.5 text-gray-300 text-[18px] font-medium leading-relaxed">
                                        <li>직사광선을 피하여 <strong class="text-white">건조하고 서늘한 곳에 보관</strong>하십시오.</li>
                                        <li>제품 특성 상 가라앉는 성분들이 있어서 <strong class="text-[{neon}] underline">흔들어서 사용</strong>하십시오.</li>
                                        <li>제품에 대하여 문의하실 경우 제조원 또는 판매원으로 연락하여 주시기 바랍니다.</li>
                                    </ul>
                                </div>
                                
                                <div class="grid grid-cols-2 gap-4 border-t border-white/20 pt-4 font-bold">
                                    <div class="flex items-center gap-4">
                                        <span class="text-[20px]">제조일자</span>
                                        <span class="text-gray-400">별도표기</span>
                                    </div>
                                    <div class="flex items-center gap-4">
                                        <span class="text-[20px]">유통기한</span>
                                        <span class="text-gray-300">제조일로부터 24개월</span>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="border-t border-[{neon}]/50 pt-4 flex items-center justify-between text-[16px] text-gray-300 w-full">
                                <div class="flex items-center gap-4">
                                    <div class="w-16 h-16 rounded-full bg-white flex items-center justify-center shrink-0 border-4 border-[{neon}] shadow-[0_0_10px_{neon}] overflow-hidden">
                                        <img src="../sj_logo.png" alt="S&J" class="w-full h-full object-contain p-1.5">
                                    </div>
                                    <div>
                                        <div class="font-bold text-white text-[19px] mb-1">판매원 : 에스앤제이 동물병원</div>
                                        <div class="text-gray-400">경기도 용인시 처인구 포곡읍 선장1로 98-8</div>
                                        <div class="mt-0.5"><span class="text-[{neon}] font-bold">TEL</span> <span class="font-bold">031-321-6562</span></div>
                                    </div>
                                </div>
                                
                                <div class="w-[1px] h-20 bg-white/20 mx-2"></div>
                                
                                <div>
                                    <div class="font-bold text-white text-[19px] mb-1">제조원 : ㈜ 엠오 바이오</div>
                                    <div class="text-gray-400">경기도 화성시 팔탄면 석포로 74번길 10-25(공장)</div>
                                    <div class="mt-0.5"><span class="text-[{neon}] font-bold">TEL</span> <span class="font-bold">031-458-1240 / www.mobio.co.kr</span></div>
                                </div>
                                
                                <div class="flex flex-col items-center justify-center shrink-0 gap-1 text-[{neon}]">
                                    <div class="logo-area flex flex-col items-center">
                                        <svg width="45" height="15" viewBox="0 0 120 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path d="M20 20 L30 10 L40 20 L30 30 Z" fill="{neon}"/>
                                            <path d="M35 20 L45 10 L55 20 L45 30 Z" fill="white" opacity="0.7"/>
                                            <text x="65" y="26" fill="white" font-family="Arial" font-weight="900" font-size="20" letter-spacing="1">S&J</text>
                                        </svg>
                                        {logo_html}
                                    </div>
                                    <div class="relative w-16 h-16 mt-2">
                                        <svg viewBox="0 0 100 100" class="w-full h-full fill-none stroke-current stroke-[6px]" stroke-linejoin="round" stroke-linecap="round">
                                            <path d="M50 15 L85 75 L15 75 Z"/>
                                            <path d="M50 15 L60 25 M85 75 L70 75 M15 75 L25 60" />
                                        </svg>
                                        <div class="absolute inset-0 flex items-center justify-center pt-3">
                                            <span class="text-[14px] font-bold tracking-tighter text-white">플라스틱</span>
                                        </div>
                                    </div>
                                    <span class="text-[14px] font-black tracking-widest text-white">OTHER</span>
                                </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
            </div>
        </div>
    </div>
</body>
</html>"""

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
        elif unit == 'mg':
            formatted_num = f"{per_ml:g}"
        else:
            formatted_num = f"{per_ml:g}"
    orig_num_str = f"{int(num):,}" if num.is_integer() else f"{num:g}"
    return f"{orig_num_str}{unit} / L <span class='text-[18px] text-[{{neon}}]/80 ml-2 font-normal'>(1ml당 {formatted_num}{unit})</span>"

for p in products:
    effects_html = "\n".join([f'<li class="flex items-start gap-2"><div class="w-2 h-2 rounded-full bg-[{{neon}}] shadow-[0_0_5px_{{neon}}] shrink-0 mt-1.5"></div> <span class="leading-tight">{e}</span></li>' for e in p['effects']])
    effects_html += "\n" + f'<li class="col-start-3 text-left text-[14px] font-medium text-[{{neon}}]/80 flex items-start mt-1 pl-4">* (등의 개선에 도움)</li>'
    
    ingredients_html = ""
    for ing, amt in p['ingredients']:
        if "CFU" in amt or amt == "적량" or "%" in amt or "핵심" in amt or "고함량" in amt or "보조제" in amt or "/" in amt:
            ingredients_html += f'''
            <li class="flex justify-between items-center border-b border-white/5 pb-1">
                <div class="text-white font-bold">{ing}</div>
                <div class="text-gray-300 orbitron tracking-wide text-right">{amt}</div>
            </li>'''
        else:
            ingredients_html += f'''
            <li class="flex justify-between items-center border-b border-white/5 pb-1">
                <div class="text-white font-bold">{ing}</div>
                <div class="text-gray-300 orbitron tracking-wide text-right">{get_1ml_amount(amt)}</div>
            </li>'''
            
    ingredients_html += f'''
    <li class="flex justify-between items-center border-b border-white/5 pb-1">
        <div class="text-gray-400 font-bold text-[16px]">기타 식물추출물 및 부형제</div>
        <div class="text-gray-500 orbitron tracking-wide">적량</div>
    </li>'''
            
    logo_html = ""
    if p['id'] == 'probiotics':
        logo_html = '<div class="mt-2 text-center text-white/90 bg-white/10 px-2 py-1 rounded"><span class="text-[9px]">Formulated with</span><br><strong class="text-[11px]">DuPont Danisco®</strong></div>'
    elif p['id'] == 'urinary':
        logo_html = '<div class="mt-2 text-center text-white/90 bg-white/10 px-2 py-1 rounded"><span class="text-[9px]">Formulated with</span><br><strong class="text-[11px]">Adisseo Vigovisol®</strong></div>'

    weight_str = "100 ml / 병" if p['id'] == "monsmecta" else "30 ml / 병"

    html = template.format(
        name_ko=p['name_ko'],
        name_en=p['name_en'],
        desc=p['desc'],
        color1=p['color1'],
        color2=p['color2'],
        neon=p['neon'],
        effects_html=effects_html.format(neon=p['neon']),
        ingredients_html=ingredients_html.format(neon=p['neon']),
        weight_str=weight_str,
        logo_html=logo_html,
        ing_list_class=p.get('ing_list_class', "space-y-2 text-[22px]"),
        raw_materials=p.get('raw_materials', "바실러스 서브틸리스, 비타민A, 아세트산나트륨, 프로피온산나트륨, 포도당, 정제수"),
        unit_desc="총량 기준" if p['id'] == 'powerase' else ("1L 기준 (액상원료 10% 첨가 함량 환산)" if p['id'] == 'vitaplus' else ("1L 기준" if p['id'] == 'probiotics' or p['id'] == 'urinary' else "1L 기준 (권장량 1ml 당 성분량)"))
    )
    
    with open(os.path.join(out_dir, f"{p['id']}_label_print.html"), "w", encoding="utf-8") as f:
        f.write(html)
        
print("Successfully generated all 11 modern hi-tech label HTMLs.")
