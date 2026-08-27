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
      title: "응급 내원, 심한 발작 및 몬스멕타 긴급 투약",
      src: "assets/clinical/chart_day1_day2.jpg",
      highlights: [
        "7/28 18:50 내원 즉시 파보/코로나 5종 키트 음성(Neg, Neg) 확인",
        "7/28 18:55 [촬영] 1차 몬스멕타 1pump + 베타루킨 분말 0.5g 투약",
        "7/28 20:00 [촬영] 2차 몬스멕타 1pump 추가 투약 후 경련 진정",
        "7/29 05:50 상태 급호전으로 DHPPL 1차 종합백신 접종 가능"
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
      phase: "초진 응급 (7/28)",
      phaseKey: "phase1",
      stepNum: "STEP 1",
      badge: "🚨 전신 발작 경련",
      badgeColor: "bg-red-600 text-white",
      title: "동영상 1 : 내원 당시 전신 발작(Seizure) 증상",
      desc: "55일령 환축이 옆으로 쓰러져 입을 벌리고 몸을 심하게 뒤틀며 경련하는 초진 응급 순간. 파보·코로나 음성 확인 즉시 몬스멕타 투약 결정.",
      isCrucial: true
    },
    {
      id: "v2",
      userOrder: 2,
      file: "kimdongjun_case_02.mp4",
      thumb: "kimdongjun_thumb_2.jpg",
      duration: "24.5초",
      phase: "경과 점검 (8/4)",
      phaseKey: "phase3",
      stepNum: "STEP 3",
      badge: "🎉 복합 처방 & 완치 퇴원",
      badgeColor: "bg-purple-600 text-white",
      title: "동영상 2 : 몬스멕타+헤파맥스 복합 처방 후 최종 퇴원",
      desc: "책상 위 몬스멕타와 헤파맥스를 확인하고, 입맛을 다시며 편안하게 안정을 되찾은 환축을 안고 최종 완치 퇴원을 판정하는 순간.",
      isCrucial: true
    },
    {
      id: "v3",
      userOrder: 3,
      file: "kimdongjun_case_03.mp4",
      thumb: "kimdongjun_thumb_3.jpg",
      duration: "15.6초",
      phase: "기립 투약 (8/1)",
      phaseKey: "phase2",
      stepNum: "STEP 2",
      badge: "💡 처치대 기립 펌핑 투약",
      badgeColor: "bg-emerald-600 text-white",
      title: "동영상 3 : 처치대 위 기립 몬스멕타 원터치 펌프 투약",
      desc: "처치대 위에서 강아지가 스스로 일어서서 원장님의 몬스멕타 펌프를 적극적으로 꿀꺽꿀꺽 받아먹는 놀라운 활력 회복 순간.",
      isCrucial: false
    },
    {
      id: "v4",
      userOrder: 4,
      file: "kimdongjun_case_04.mp4",
      thumb: "kimdongjun_thumb_4.jpg",
      duration: "24.2초",
      phase: "신경계 검사 (8/2)",
      phaseKey: "phase2",
      stepNum: "STEP 2",
      badge: "✨ 보행 & 자세 반사 정상화",
      badgeColor: "bg-blue-600 text-white",
      title: "동영상 4 : 보행 및 자세 반사 완벽 정상화 검사",
      desc: "차트 8/2 [20:57 (촬영) 기립 양호, 보행 양호]. 네 발로 꼿꼿이 서고 들어올렸을 때 정상적인 사지 반사를 보이며 완벽히 회복된 순간.",
      isCrucial: true
    },
    {
      id: "v5",
      userOrder: 5,
      file: "kimdongjun_case_05.mp4",
      thumb: "kimdongjun_thumb_5.jpg",
      duration: "15.5초",
      phase: "입원 격리 (7/28)",
      phaseKey: "phase1",
      stepNum: "STEP 1",
      badge: "⚠️ 케이지 전신 무기력",
      badgeColor: "bg-amber-600 text-white",
      title: "동영상 5 : 케이지 안 전신 무기력(Depression) 상태",
      desc: "케이지 안에서 당근 인형 옆에 눈을 감고 미동도 없이 축 늘어져 있는 소화기 허탈 및 탈진 상태.",
      isCrucial: false
    },
    {
      id: "v6",
      userOrder: 6,
      file: "kimdongjun_case_06.mp4",
      thumb: "kimdongjun_thumb_6.jpg",
      duration: "27.8초",
      phase: "의식 회복 (7/30)",
      phaseKey: "phase2",
      stepNum: "STEP 2",
      badge: "🌱 또렷한 정면 응시",
      badgeColor: "bg-cyan-600 text-white",
      title: "동영상 6 : 케이지 안 고개 들고 또렷한 눈빛 회복",
      desc: "투약 2일 만에 경련이 멈추고 고개를 꼿꼿이 든 채 정면을 또렷하게 응시하는 괄목할 만한 의식 회복 순간.",
      isCrucial: false
    },
    {
      id: "v7",
      userOrder: 7,
      file: "kimdongjun_case_07.mp4",
      thumb: "kimdongjun_thumb_7.jpg",
      duration: "7.2초",
      phase: "식욕 폭발 (7/31)",
      phaseKey: "phase2",
      stepNum: "STEP 2",
      badge: "🔥 캔사료 폭풍 완식 먹방",
      badgeColor: "bg-rose-600 text-white",
      title: "동영상 7 : 식욕 전폐 환축의 캔사료 폭풍 완식",
      desc: "차트 7/31 [식욕↑, 식사량↑ 완식]. 밥그릇에 머리를 박고 싹싹 핥아먹는 기적 같은 식욕 폭발의 결정적 증거.",
      isCrucial: true
    },
    {
      id: "v8",
      userOrder: 8,
      file: "kimdongjun_case_08.mp4",
      thumb: "kimdongjun_thumb_8.jpg",
      duration: "23.2초",
      phase: "초진 투약 (7/29)",
      phaseKey: "phase1",
      stepNum: "STEP 1",
      badge: "💡 원장님 한 손 투약 시연",
      badgeColor: "bg-emerald-600 text-white",
      title: "동영상 8 : 55일령 환축에게 한 손으로 펌핑 투약 시연",
      desc: "알약을 삼킬 수 없는 초소형 환축에게 김동준 원장이 머리를 가볍게 지지하고 몬스멕타를 입안에 부드럽게 펌핑 투약하는 시연.",
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
