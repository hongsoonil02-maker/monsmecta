import os

app_path = "src/App.jsx"
chatbot_path = "src/components/Chatbot.jsx"

with open(app_path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = {
    # Clinical
    "수의사가 수의사에게 제안하는 근거": "{t('clinical.title')}",
    "신속한 장 점막 회복 임상": "{t('clinical.card1_title')}",
    "에스앤제이 동물병원의 실제 처방 케이스를 통해 입증된 유해 물질 차단력과 점막 보호막 형성 속도를 확인하세요.": "{t('clinical.card1_desc')}",
    "회복 속도 비교 (일)": "{t('clinical.chart_speed')}",
    "대조군": "{t('clinical.chart_control')}",
    "몬스멕타": "{t('clinical.chart_monsmecta')}",
    "완벽한 기호성과 투약 편의성": "{t('clinical.card2_title')}",
    "바쁜 진료 환경과 예민한 환축을 고려하여, 스트레스 없이 자발적인 섭취를 유도하도록 설계되었습니다.": "{t('clinical.card2_desc')}",
    "자발적 섭취율": "{t('clinical.intake_rate')}",
    "원내 처방 만족도": "{t('clinical.satisfaction')}",

    # Infographics
    "상세 학술 데이터 및 상담 시나리오": "{t('infographics.title')}",
    "원장님의 정확한 처방과 보호자 상담을 돕는 심층 자료입니다.": "{t('infographics.desc')}",

    # Letter
    "원장님, 몬스멕타는 단순한 일회성 정장 제품 공급을 넘어,<br className=\"hidden md:block\" />": "{t('letter.message1')}<br className=\"hidden md:block\" />",
    "일선 원장님들이 임상 진료 현장에서 당당히 처방의 가치와 독점성을 누릴 수 있도록<br className=\"hidden md:block\" />": "{t('letter.message2')}<br className=\"hidden md:block\" />",
    "든든하게 지켜드리는 영속적인 비즈니스 파트너가 될 것을 약속드립니다.": "{t('letter.message3')}",
    "수의학적 가치와 신뢰를 담아,": "{t('letter.signature_title')}",
    "닥터 젬스홍 배상": "{t('letter.signature_name')}",

    # Order form
    "동물병원 원장님 전용 퀵 발주서": "{t('order.title')}",
    "입력하신 정보는 병원 인증 및 세금계산서 발행에 엄격하게 사용됩니다.": "{t('order.desc')}",
    "동물병원 정보": "{t('order.hospital_info')}",
    "동물병원명 <span": "{t('order.hospital_name')} <span",
    "예: 에스앤제이 동물병원": "예: 에스앤제이 동물병원", # Wait, inside placeholder we use t() without {}
    "placeholder=\"예: 에스앤제이 동물병원\"": "placeholder={t('order.hospital_name_placeholder')}",
    "사업자등록번호 <span": "{t('order.biz_number')} <span",
    "placeholder=\"숫자만 10자리 입력\"": "placeholder={t('order.biz_number_placeholder')}",
    "제품 수령지 주소 <span": "{t('order.address')} <span",
    "placeholder=\"상세 주소를 정확히 입력해주세요\"": "placeholder={t('order.address_placeholder')}",
    "수량 선택 (병)": "{t('order.quantity_select')}",
    "몬스멕타 <span": "{t('order.product_name')} <span",
    "(100ml / 병)": "{t('order.unit')}",
    "병원 공급가:": "{t('order.supply_price')}",
    "(VAT 포함)": "{t('order.vat_included')}",
    "* 최소 주문 수량: 5병": "{t('order.min_order')}",
    "총 결제 예정 금액": "{t('order.total_price')}",
    "원</span></span>": "{t('order.won')}</span></span>",
    "선결제 진행하기": "{t('order.btn')}",
    "무통장 입금: 카카오뱅크 3333-26-3248376 (예금주: 홍순일)": "{t('order.bank_info')}",

    # Footer
    "에스앤제이 동물병원</h4>": "{t('footer.title')}</h4>",
    "대표자: 홍순일 (닥터 젬스홍) | 사업자등록번호: 792-66-00615": "{t('footer.info1')}",
    "주소: 경기도 용인시 처인구 포곡읍 선장1로 98-8": "{t('footer.info2')}",
    "대표 연락처: 031-321-6562 | 이메일: soonilhong@naver.com": "{t('footer.info3')}",
    "결제계좌: 카카오뱅크 3333-26-3248376 (예금주: 홍순일)": "{t('footer.bank')}",
    "※ 본 사이트는 대외비 문서로 전국 수의사 원장님들께 한정하여 발송됩니다.": "{t('footer.notice')}",

    # Modal E-Label
    "E-Label Specification</p>": "E-Label Specification</p>", # English
    "몬스멕타 상세 스펙 및 라벨 정보": "{t('label.title')}",
    "연변 시 장 기능 개선 및 정장 작용": "{t('label.desc')}",
    "✅ 1일 두당 2~4ml 급여": "{t('label.feed1')}",
    "✅ 5~7일간 경구 급여": "{t('label.feed2')}",
    "✅ 개, 고양이 전축종 적용": "{t('label.feed3')}",
    "핵심 5가지 복합체 성분": "{t('label.ingredients_title')}",
    "1) 고초균 (Bacillus subtilis):": "{t('label.ing1_title')}",
    "항균·항바이러스 작용": "{t('label.ing1_desc')}",
    "*경상대 수의대 항바이러스 효과 확인": "{t('label.ing1_note')}",
    "2) 포도당:": "{t('label.ing2_title')}",
    "장 기능 개선 및 정장 작용": "{t('label.ing2_desc')}",
    "3) 비타민 A:": "{t('label.ing3_title')}",
    "상피세포의 회복": "{t('label.ing3_desc')}",
    "4) 전해질제:": "{t('label.ing4_title')}",
    "Sodium acetate, Sodium propionate": "{t('label.ing4_desc')}",
    "5) 몬모릴로나이트:": "{t('label.ing5_title')}",
    "연변 및 설사 개선, 독소 제거, 장 환경 개선": "{t('label.ing5_desc')}",
    "사료 성분등록번호": "{t('label.reg_no_title')}",
    "제XX9UY0145호": "{t('label.reg_no')}",
    "사료의 종류 및 명칭 / 형태 / 용도": "{t('label.type_title')}",
    "보조사료 / 미생물제 / 바실러스 서브틸리스 | 액상 | 반려동물용": "{t('label.type_val')}",
    "등록성분량": "{t('label.amount_title')}",
    "바실러스 서브틸리스 1.0 x 10^7 cfu/g 이상, 부형제(정제수)": "{t('label.amount_val')}",
    "사용한 원료의 명칭": "{t('label.ingredients_list_title')}",
    "바실러스 서브틸리스, 비타민A, 아세트산나트륨, 프로피온산나트륨, 포도당, 정제수": "{t('label.ingredients_list_val')}",
    "▶ 효과": "{t('label.effect_title')}",
    "장 관련 질병(파보, 로타, 코로나 등)에 대한 저항력 향상에 도움": "{t('label.effect1')}",
    "면역 기능 및 건강 상태 유지에 도움": "{t('label.effect2')}",
    "장 기능 개선 및 정장 작용에 도움": "{t('label.effect3')}",
    "실제중량</span>": "{t('label.weight_title')}</span>",
    "100ml</strong>": "{t('label.weight_val')}</strong>",
    "제조일자</span>": "{t('label.mfg_title')}</span>",
    "별도표기</span>": "{t('label.mfg_val')}</span>",
    "유통기한</span>": "{t('label.exp_title')}</span>",
    "제조일로부터 18개월</span>": "{t('label.exp_val')}</span>",
    "⚠️ 주의사항": "{t('label.warning_title')}",
    "직사광선을 피하여 건조하고 서늘한 곳에 보관하십시오.": "{t('label.warning1')}",
    "제품 특성 상 가라앉는 성분들이 있어서": "{t('label.warning2_part1')}",
    "흔들어서 사용</strong>하십시오.": "{t('label.warning2_part2')}</strong>{t('label.warning2_part3')}",
    "제품에 대하여 문의하실 경우 제조원 또는 판매원으로 연락하여 주시기 바랍니다.": "{t('label.warning3')}",
    "판매원 : 에스앤제이 동물병원": "{t('label.seller_name')}",
    "경기도 용인시 처인구 포곡읍 선장1로 98-8<br />": "{t('label.seller_addr')}<br />",
    "제조원 : ㈜ 엠오 바이오": "{t('label.maker_name')}",
    "경기도 화성시 팔탄면 석포로 74번길 10-25(공장)<br />": "{t('label.maker_addr')}<br />",
    "🖨️ 인쇄용 원본 라벨 보기": "{t('label.print_btn')}",
    "🖨️ 인쇄용 라벨 (고해상도)": "{t('label.print_title')}"
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open(app_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated App.jsx successfully.")

# Also update Chatbot.jsx
with open(chatbot_path, "r", encoding="utf-8") as f:
    chat_content = f.read()

chat_replacements = {
    "'안녕하세요! 에스앤제이 동물병원 원장님들을 위한 몬스멕타 전용 AI 상담원입니다. 무엇을 도와드릴까요?'": "t('chat.greeting')",
    "'죄송합니다. 통신 중 오류가 발생했습니다. 잠시 후 다시 시도해주세요.'": "t('chat.error')",
    "몬스멕타 AI 전문의": "{t('chat.title')}",
    "빠르고 정확한 상담": "{t('chat.subtitle')}",
    "placeholder=\"무엇이든 물어보세요...\"": "placeholder={t('chat.placeholder')}",
    "전송": "{t('chat.send')}"
}

for k, v in chat_replacements.items():
    chat_content = chat_content.replace(k, v)

with open(chatbot_path, "w", encoding="utf-8") as f:
    f.write(chat_content)

print("Updated Chatbot.jsx successfully.")
