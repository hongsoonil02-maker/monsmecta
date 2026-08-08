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
            ("Taurine (타우린)", "2,000mg"),
            ("D-Sorbitol (D-소르비톨)", "45g"),
            ("L-lysine HCl", "300mg"),
            ("L-methionine", "300mg"),
            ("Vitamin B12", "1,000μg")
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
            ("Beta-glucan (베타글루칸)", "10,000mg"),
            ("Fucoidan (후코이단)", "5,000mg"),
            ("Vitamin C", "15,000mg"),
            ("Curcumin (커큐민)", "2,000mg")
        ]
    },
    {
        "id": "coldzero",
        "name_ko": "몬스멕타 콜드제로",
        "name_en": "MONSMECTA COLDZERO",
        "desc": "호흡기 및 감기 예방 보조제",
        "color1": "#0A2B2B", "color2": "#0B1515",
        "neon": "#06b6d4", # cyan-500
        "effects": ["호흡기 점막 면역 강화", "기침 및 호흡 곤란 완화", "바이러스성 질환 예방 보조", "기관지 염증 완화"],
        "ingredients": [
            ("Propolis (프로폴리스)", "5,000mg"),
            ("Bromelain (브로멜라인)", "2,000mg"),
            ("Vitamin D3", "500,000 IU"),
            ("N-Acetyl Cysteine", "3,000mg")
        ]
    },
    {
        "id": "eczema",
        "name_ko": "몬스멕타 익제마",
        "name_en": "MONSMECTA ECZEMA",
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
        "ingredients": [
            ("Coenzyme Q10 (코큐텐)", "3,000mg"),
            ("L-carnitine", "10,000mg"),
            ("Taurine (타우린)", "25,000mg"),
            ("Omega-3 EPA/DHA", "10,000mg")
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
        "ingredients": [
            ("Glucosamine (글루코사민)", "20,000mg"),
            ("Chondroitin (콘드로이친)", "10,000mg"),
            ("MSM (식이유황)", "15,000mg"),
            ("Green Lipped Mussel", "15,000mg")
        ]
    },
    {
        "id": "powerase",
        "name_ko": "몬스멕타 파워라제",
        "name_en": "MONSMECTA POWERASE",
        "desc": "기력 및 활력 회복 보조제",
        "color1": "#2B1A0A", "color2": "#0B1515",
        "neon": "#f97316", # orange-500
        "effects": ["수술 후 빠른 회복 촉진", "노령견/묘 기력 증진", "식욕 촉진 및 영양 공급", "대사 활성화 보조"],
        "ingredients": [
            ("L-arginine (L-아르기닌)", "10,000mg"),
            ("Vitamin B Complex", "5,000mg"),
            ("Maca Extract (마카)", "3,000mg"),
            ("Octacosanol (옥타코사놀)", "1,000mg")
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
            ("Montmorillonite (요독 흡착 핵심성분)", "80~90% (고함량)"),
            ("Adisseo Vigovisol (프리미엄 비타민 복합체)", "10~20% (보조)"),
            ("└ 비타민 A (Vitamin A)", "4,000,000 IU (4,000 IU)"),
            ("└ 비타민 D3 (Vitamin D3)", "800,000 IU (800 IU)"),
            ("└ 비타민 E (Vitamin E)", "2,000 IU (2 IU)"),
            ("└ 비타민 B1, B2, C", "각 1,000mg (1mg)"),
            ("└ 니코틴산아미드", "3,000mg (3mg)"),
            ("└ 판토텐산 칼슘", "1,000mg (1mg)")
        ]
    },
    {
        "id": "vitaplus",
        "name_ko": "몬스멕타 비타플러스",
        "name_en": "MONSMECTA VITAPLUS",
        "desc": "종합 비타민 및 미네랄 보조제",
        "color1": "#2B2A0A", "color2": "#0B1515",
        "neon": "#eab308", # yellow-500
        "effects": ["필수 비타민 12종 공급", "미량 미네랄 균형 유지", "피로 회복 및 항산화", "뼈 및 치아 건강 유지"],
        "ingredients": [
            ("Vitamin A", "1,000,000 IU"),
            ("Vitamin D3", "100,000 IU"),
            ("Vitamin E", "5,000 IU"),
            ("Calcium (칼슘)", "15,000mg"),
            ("Phosphorus (인)", "10,000mg")
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
        <!-- Outer border changed back to Gold/Brown (#8B7355) per earlier request -->
        <div id="label-container" class="cyber-bg text-gray-100 w-[2375px] h-[1125px] shrink-0 rounded-[40px] overflow-hidden border-[8px] border-[#8B7355] relative flex flex-col">
            
            <!-- Tech Grid Overlay -->
            <div class="absolute inset-0 opacity-10" style="background-image: linear-gradient({neon} 1px, transparent 1px), linear-gradient(90deg, {neon} 1px, transparent 1px); background-size: 50px 50px;"></div>
            
            <!-- Top Cyber Accent -->
            <div class="h-4 shrink-0 bg-[{neon}] shadow-[0_0_15px_{neon}] relative z-10"></div>
            
            <div class="px-14 py-10 relative z-10 h-full flex flex-col justify-between">
                <div class="flex flex-row gap-16 justify-between h-full">
                    
                    <!-- Left Column -->
                    <div class="w-[45%] flex flex-col justify-between h-full pr-4 relative">
                        <!-- Holographic Branding -->
                        <div class="flex flex-col items-center justify-center pt-2">
                            <div class="flex items-center gap-6 mb-6">
                                <!-- Dog Emoji -->
                                <span class="text-[72px] drop-shadow-[0_0_15px_{neon}]">🐶</span>
                                <div class="inline-block bg-black/50 border border-[{neon}] rounded-full px-8 py-3">
                                    <span class="text-[20px] font-bold text-gray-300 tracking-[0.2em] uppercase"><span class="neon-text">S&J</span> ADVANCED VET FORMULA</span>
                                </div>
                                <!-- Cat Emoji -->
                                <span class="text-[72px] drop-shadow-[0_0_15px_{neon}]">🐱</span>
                            </div>
                            
                            <p class="text-[24px] font-medium text-gray-400 mb-2 tracking-wide">{desc}</p>
                            <h1 class="text-[85px] font-black text-white tracking-tight leading-none mb-3 drop-shadow-[0_0_10px_rgba(255,255,255,0.3)]">{name_ko}</h1>
                            <h2 class="text-[36px] font-bold orbitron neon-text tracking-[0.1em]">{name_en}</h2>
                        </div>

                        <!-- Core Effects UI Panel (bg matched to ingredients box) -->
                        <div class="bg-black/40 border border-white/10 px-8 py-4 rounded-3xl relative">
                            <div class="absolute -top-4 left-6 bg-white/10 backdrop-blur-md px-4 py-1 rounded-lg border border-white/20">
                                <span class="font-bold text-white tracking-wide">핵심 효능</span>
                            </div>
                            <!-- Changed to 3 columns grid-cols-3 as requested -->
                            <ul class="grid grid-cols-3 gap-y-2 gap-x-6 text-[18px] font-bold text-gray-200 tracking-tight mt-2">
                                {effects_html}
                            </ul>
                        </div>

                        <!-- Data Table UI -->
                        <div class="bg-black/40 border border-white/10 px-8 py-5 rounded-3xl relative">
                            <div class="flex justify-between items-end mb-4 border-b border-white/20 pb-3">
                                <h3 class="text-[26px] font-bold text-white flex items-center gap-3">
                                    주요 성분 데이터
                                </h3>
                                <div class="bg-white/10 backdrop-blur-md px-3 py-1 rounded border border-white/20 text-[15px] text-[{neon}]">{unit_desc}</div>
                            </div>
                            <ul class="space-y-2 text-[22px] font-medium">
                                {ingredients_html}
                            </ul>
                        </div>
                        
                        <!-- Package Unit at Bottom Left (Centered) -->
                        <div class="flex justify-center pb-2">
                            <div class="border border-[{neon}]/50 rounded-full px-8 py-2 bg-black/40">
                                <span class="text-white text-[22px] font-bold">포장단위 :</span>
                                <span class="text-[{neon}] text-[24px] font-bold ml-2">30 ml / 병</span>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Vertical Cyber Divider -->
                    <div class="w-[4px] shrink-0 bg-gradient-to-b from-transparent via-[{neon}] to-transparent opacity-50 relative">
                        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-8 h-8 border-4 border-[{neon}] rotate-45 bg-black"></div>
                    </div>
                    
                    <!-- Right Column -->
                    <div class="w-[50%] flex flex-col h-full pl-4 relative">
                        
                        <!-- Specs Box -->
                        <div class="glass-panel p-8 rounded-3xl h-full flex flex-col justify-between relative z-10">
                            
                            <div class="flex justify-between items-start border-b border-white/20 pb-4">
                                <div>
                                    <div class="text-[14px] text-[{neon}] mb-1 font-bold">사료 성분등록번호</div>
                                    <div class="text-[22px] font-bold text-white">제XX9UY0145호</div>
                                </div>
                                <div class="text-right">
                                    <div class="text-[16px] text-gray-400 mb-1">사료의 종류 및 명칭 / 형태 / 용도</div>
                                    <div class="text-[22px] font-bold text-white">보조사료/혼합제 | 액상(겔) | 반려견·반려묘</div>
                                </div>
                            </div>
                            
                            <div>
                                <div class="text-[18px] text-[{neon}] font-bold mb-2">등록성분량</div>
                                <div class="text-[18px] font-medium text-white">{registered_ingredients}</div>
                            </div>
                            
                            <div>
                                <div class="text-[18px] text-[{neon}] font-bold mb-2">사용한 원료의 명칭</div>
                                <div class="text-[18px] text-gray-300 leading-relaxed font-medium">바실러스 서브틸리스, 몬모릴로나이트, 천연 추출물 혼합, 프로피온산나트륨, 포도당, 정제수 등 (제품별 상세 원료는 설명서 참조)</div>
                            </div>
                            
                            <div>
                                <div class="text-[18px] text-[{neon}] font-bold mb-2">대상축종</div>
                                <div class="text-[20px] font-bold text-white">반려견 · 반려묘</div>
                            </div>
                            
                            <!-- Dosage Panel -->
                            <div class="bg-[{neon}]/10 border border-[{neon}]/30 p-6 rounded-2xl">
                                <div class="text-[18px] text-[{neon}] font-bold mb-2">용법 및 용량</div>
                                <div class="text-[26px] font-bold text-white">체중 5kg 당 1일 1회 2ml 급여 <span class="text-[16px] text-gray-400 font-normal ml-2">(1 펌프/스포이드 = 약 1ml)</span></div>
                            </div>
                            
                            <!-- Warnings -->
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
                                
                                <!-- 물류 정보 (Without 포장단위) -->
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
                            
                            <!-- Manufacturer Info -->
                            <div class="border-t border-[{neon}]/50 pt-4 flex items-center justify-between text-[16px] text-gray-300 w-full">
                                <div class="flex items-center gap-4">
                                    <!-- S&J Logo -->
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
    """ Converts amount per 1L to amount per 1ml based on unit """
    amt_str = amt_str.replace(",", "").strip()
    import re
    # Extract number and unit
    match = re.match(r"([\d\.]+)(.*)", amt_str)
    if not match: return amt_str
    num = float(match.group(1))
    unit = match.group(2).strip()
    
    # 1L = 1000ml, so 1ml is 1/1000th
    per_ml = num / 1000
    
    # Format per_ml nicely
    if per_ml.is_integer():
        formatted_num = f"{int(per_ml):,}"
    else:
        # e.g., 45g -> 0.045g -> 45mg
        if unit == 'g':
            formatted_num = f"{int(per_ml * 1000):,}"
            unit = 'mg'
        elif unit == 'mg':
            formatted_num = f"{per_ml:g}"
        else:
            formatted_num = f"{per_ml:g}"
            
    # Re-add commas for original string
    orig_num_str = f"{int(num):,}" if num.is_integer() else f"{num:g}"
    
    return f"{orig_num_str}{unit} / L <span class='text-[18px] text-[{{neon}}]/80 ml-2 font-normal'>(1ml당 {formatted_num}{unit})</span>"

for p in products:
    effects_html = "\n".join([f'<li class="flex items-start gap-2"><div class="w-2 h-2 rounded-full bg-[{{neon}}] shadow-[0_0_5px_{{neon}}] shrink-0 mt-1.5"></div> <span class="leading-tight">{e}</span></li>' for e in p['effects']])
    effects_html += "\n" + f'<li class="col-start-3 text-left text-[14px] font-medium text-[{{neon}}]/80 flex items-start mt-1 pl-4">* (등의 개선에 도움)</li>'
    
    ingredients_html = ""
    for ing, amt in p['ingredients']:
        if "CFU" in amt or amt == "적량" or "%" in amt or "핵심" in amt:
            # For probiotics or untrackable
            val = amt
            if "CFU" in amt:
                val = f"{amt} / L"
            ingredients_html += f'''
            <li class="flex justify-between items-center border-b border-white/5 pb-1">
                <div class="text-white font-bold">{ing}</div>
                <div class="text-gray-300 orbitron tracking-wide text-right">{val}</div>
            </li>'''
        else:
            ingredients_html += f'''
            <li class="flex justify-between items-center border-b border-white/5 pb-1">
                <div class="text-white font-bold">{ing}</div>
                <div class="text-gray-300 orbitron tracking-wide text-right">{get_1ml_amount(amt)}</div>
            </li>'''
            
    # Add filler
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

    html = template.format(
        name_ko=p['name_ko'],
        name_en=p['name_en'],
        desc=p['desc'],
        color1=p['color1'],
        color2=p['color2'],
        neon=p['neon'],
        effects_html=effects_html.format(neon=p['neon']),
        ingredients_html=ingredients_html.format(neon=p['neon']),
        registered_ingredients=p.get('registered_ingredients', '별도 고시 (제품 설명서 참조)'),
        logo_html=logo_html,
        unit_desc="1L 기준" if p['id'] == 'probiotics' or p['id'] == 'urinary' else "1L 기준 (괄호 안은 1ml 당 함량)"
    )
    
    with open(os.path.join(out_dir, f"{p['id']}_label_print.html"), "w", encoding="utf-8") as f:
        f.write(html)
        
print("Successfully generated all 11 modern hi-tech label HTMLs.")
