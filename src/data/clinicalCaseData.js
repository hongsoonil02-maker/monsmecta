// 하남 사랑동물병원 김동준 원장 (몬스멕타 자문위원) 실제 임상 증례 데이터
export const CLINICAL_CASE_DATA = {
  patient: {
    species: "강아지 (토이푸들, ♂)",
    age: "55일령 (초소형 자견)",
    hospital: "하남 사랑동물병원",
    vet: "김동준 원장 (몬스멕타 자문위원)",
    admissionDate: "2026. 07. 28 (18:50 응급 내원)",
    dischargeDate: "2026. 08. 04 (완치 퇴원)",
    admissionReason: "급성 전신 발작(Seizure), 심한 우울(Depression), 식욕 전폐(Anorexia)",
    kitTest: "파보 바이러스(Parvo) Neg / 코로나 장염(Corona) Neg (5종 키트 음성)",
    diagnosis: "원인불명 급성 대사성 장독소증 및 소화기 급성 허탈 의심"
  },
  
  charts: [
    {
      id: "phase1",
      period: "Day 1 ~ Day 2 (7/28 ~ 7/29)",
      title: "수액·기타처방 0% 배제, 오직 몬스멕타 긴급 단독 투약",
      src: "assets/clinical/chart_day1_day2.jpg",
      highlights: [
        "7/28 18:50 내원 즉시 파보/코로나 5종 키트 음성(Neg, Neg) 확인",
        "★ [단독 처치] 수액 요법 및 기타 처방 일체 배제, 오직 몬스멕타 단독 급여 결정",
        "7/28 18:55 [촬영] 1차 몬스멕타 1pump 긴급 투약",
        "7/28 20:00 [촬영] 2차 몬스멕타 1pump 추가 투약 후 극심한 신경 경련 진정",
        "7/29 05:50 2일 만에 상태 급호전으로 DHPPL 1차 종합백신 접종 가능 수준 회복"
      ]
    },
    {
      id: "phase2",
      period: "Day 3 ~ Day 5 (7/30 ~ 8/2)",
      title: "식욕 폭발(식욕↑, 식사량↑), 소화기 안정 및 기립 회복",
      src: "assets/clinical/chart_day3_day5.jpg",
      highlights: [
        "7/30 19:33 [촬영] 몬스멕타 2pump 지속 투여로 장독소 배출 가속",
        "7/31 '어제 lowfat can 섞어먹여 식욕↑, 식사량↑, 변 안정'",
        "7/31 16:20 [촬영] 밥그릇에 머리를 박고 캔사료를 폭풍 완식",
        "8/2 20:57 [촬영] 네 발로 당당히 서서 전신 자세 반사 완전 회복"
      ]
    },
    {
      id: "phase3",
      period: "Day 6 ~ Day 7 (8/3 ~ 8/4)",
      title: "몬스멕타 + 헤파맥스 복합 처방 및 최종 완치 [퇴원]",
      src: "assets/clinical/chart_day6_day7.jpg",
      highlights: [
        "8/3 경미한 콧물 증상 외 소화기 완벽 정상화 (대증 처치)",
        "8/4 몬스멕타 2pump + 헤파맥스 2pump (1ml, 1ml 2회 PO) 병용",
        "간 해독 기능 보강 및 장 점막 최종 재생 확인",
        "하남 사랑동물병원 김동준 원장 자필 서명과 함께 최종 [퇴원] 완료"
      ]
    }
  ],

  videos: [
    {
      id: "v1",
      userOrder: 1,
      file: "kimdongjun_case_01.mp4",
      thumb: "kimdongjun_thumb_1.jpg",
      duration: "9.0초",
      phase: "STEP 1 (초기 처치)",
      phaseKey: "phase1",
      stepNum: "STEP 1",
      badge: "🚨 내원 당시 응급 발작",
      badgeColor: "bg-red-600 text-white",
      title: "동영상 1 : 내원 당시 급성 전신 발작(Seizure) 증상",
      desc: "55일령 환축이 옆으로 쓰러져 입을 벌리고 온몸을 뒤틀며 경련하는 초진 응급 순간. 파보·코로나 음성 확인 즉시 몬스멕타 처치 돌입.",
      isCrucial: true
    },
    {
      id: "v2",
      userOrder: 2,
      file: "kimdongjun_case_02.mp4",
      thumb: "kimdongjun_thumb_2.jpg",
      duration: "24.5초",
      phase: "STEP 1 (초기 처치)",
      phaseKey: "phase1",
      stepNum: "STEP 1",
      badge: "🩺 입원 초기 활력 점검",
      badgeColor: "bg-amber-600 text-white",
      title: "동영상 2 : 입원 초기 처치대 활력 및 반응 점검",
      desc: "처치대 위에서 환축의 전신 상태와 호흡, 동공 반사를 꼼꼼히 살피며 초기 입원 처치를 진행하는 진료실 장면.",
      isCrucial: true
    },
    {
      id: "v3",
      userOrder: 3,
      file: "kimdongjun_case_03.mp4",
      thumb: "kimdongjun_thumb_3.jpg",
      duration: "15.6초",
      phase: "STEP 1 (초기 처치)",
      phaseKey: "phase1",
      stepNum: "STEP 1",
      badge: "💡 처치대 기립 펌핑 투약",
      badgeColor: "bg-emerald-600 text-white",
      title: "동영상 3 : 처치대 위 몬스멕타 원터치 펌프 투약",
      desc: "환축이 처치대 위에서 스스로 힘을 내어 일어서서 원장님의 몬스멕타 펌프를 꿀꺽꿀꺽 받아먹는 자발 연하 확인.",
      isCrucial: false
    },
    {
      id: "v4",
      userOrder: 4,
      file: "kimdongjun_case_04.mp4",
      thumb: "kimdongjun_thumb_4.jpg",
      duration: "24.2초",
      phase: "STEP 2 (회복 경과)",
      phaseKey: "phase2",
      stepNum: "STEP 2",
      badge: "✨ 보행 & 사지 반사 검사",
      badgeColor: "bg-blue-600 text-white",
      title: "동영상 4 : 보행 및 자세 반사 정상화 정밀 점검",
      desc: "네 발로 꼿꼿이 서고 들어올렸을 때 정상적인 사지 반사를 보이며 신경계와 근력이 뚜렷하게 회복된 모습 점검.",
      isCrucial: true
    },
    {
      id: "v5",
      userOrder: 5,
      file: "kimdongjun_case_05.mp4",
      thumb: "kimdongjun_thumb_5.jpg",
      duration: "15.5초",
      phase: "STEP 2 (회복 경과)",
      phaseKey: "phase2",
      stepNum: "STEP 2",
      badge: "⚠️ 케이지 집중 안정 케어",
      badgeColor: "bg-slate-700 text-white",
      title: "동영상 5 : 케이지 안 집중 안정 및 휴식 상태",
      desc: "입원장 케이지 안에서 안정을 취하며 체력과 장 점막을 회복 중인 환축의 경과 관찰.",
      isCrucial: false
    },
    {
      id: "v6",
      userOrder: 6,
      file: "kimdongjun_case_06.mp4",
      thumb: "kimdongjun_thumb_6.jpg",
      duration: "27.8초",
      phase: "STEP 2 (회복 경과)",
      phaseKey: "phase2",
      stepNum: "STEP 2",
      badge: "🌱 고개 들고 또렷한 눈빛",
      badgeColor: "bg-cyan-600 text-white",
      title: "동영상 6 : 케이지 안 고개 들고 또렷한 눈빛 회복",
      desc: "경련이 완전히 멈추고 고개를 꼿꼿이 든 채 정면을 또렷하게 응시하는 괄목할 만한 의식 회복 순간.",
      isCrucial: false
    },
    {
      id: "v7",
      userOrder: 7,
      file: "kimdongjun_case_07.mp4",
      thumb: "kimdongjun_thumb_7.jpg",
      duration: "7.2초",
      phase: "STEP 2 (회복 경과)",
      phaseKey: "phase2",
      stepNum: "STEP 2",
      badge: "🔥 캔사료 폭풍 완식 먹방",
      badgeColor: "bg-rose-600 text-white",
      title: "동영상 7 : 식욕 전폐 환축의 캔사료 폭풍 완식",
      desc: "밥그릇에 머리를 박고 싹싹 핥아먹는 기적 같은 식욕 폭발! 장내 소화기 기능이 완벽히 정상 궤도에 올랐음을 입증.",
      isCrucial: true
    },
    {
      id: "v8",
      userOrder: 8,
      file: "kimdongjun_case_08.mp4",
      thumb: "kimdongjun_thumb_8.jpg",
      duration: "23.2초",
      phase: "STEP 3 (완치 퇴원)",
      phaseKey: "phase3",
      stepNum: "STEP 3",
      badge: "🎉 퇴원 직전 몬스멕타 최종 투여",
      badgeColor: "bg-purple-600 text-white",
      title: "동영상 8 : 퇴원 직전 몬스멕타 최종 투여 및 완치 퇴원",
      desc: "퇴원 직전 환축의 입안에 몬스멕타를 최종 투약하며, 안락사 위기에서 100% 기적처럼 살아나 완치 퇴원하는 감동의 순간!",
      isCrucial: true
    }
  ],

  protocol: {
    title: "김동준 원장의 '소아 자견 급성 독소/소화기 허탈' 3단계 임상 프로토콜",
    target: "55일령 전후 어린 자견 / 알약 복용 불가 환축 / 원인불명 급성 소화기 독소증",
    steps: [
      {
        step: "1단계 : 즉각적 장내 독소 흡착 & 장벽 보호",
        product: "몬스멕타 (MONSMECTA)",
        dosage: "1회 1~2 pump 경구 직투여 (하루 2~4회)",
        detail: "내원 즉시 파보·코로나 감별 후 1pump 직투여. 초미세 몬모릴로나이트가 장내 세균 독소(Endotoxin)를 즉각 흡착 배출하고 장점막에 보호막 형성."
      },
      {
        step: "2단계 : 장관 면역 및 전해질 밸런스 부스팅",
        product: "베타루킨 (베타글루칸 분말) 병용",
        dosage: "1회 0.5g 혼합 투여",
        detail: "장내 유익균 활성화 및 장관 면역세포 자극. 탈수와 전해질 불균형을 신속히 교정하여 투약 24시간 만에 백신 접종이 가능할 정도로 회복 유도."
      },
      {
        step: "3단계 : 간 해독 부스팅 & 재발 방지 퇴원 처방",
        product: "몬스멕타 + 몬스멕타 헤파맥스 (HEPAMAX)",
        dosage: "몬스멕타 1ml + 헤파맥스 1ml 2회 PO",
        detail: "독소로 지친 간세포를 실리마린·밀크씨슬·메치오닌 복합체(헤파맥스)로 정화하여 완치 퇴원 후 재발 없는 완벽한 소화기 정상화 달성."
      }
    ]
  }
};
