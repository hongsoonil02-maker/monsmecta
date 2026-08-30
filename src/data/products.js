export const PRODUCTS = {
  monsmecta: {
    id: 'monsmecta',
    name_ko: '몬스멕타 (오리지널)',
    name_en: 'MONSMECTA (ORIGINAL)',
    volume: '100ml',
    desc: '동물병원 전용 B2B 처방 솔루션 · 모든 동물을 위한 소화기 케어',
    icon: '🧪',
    color: 'emerald',
    bg: 'hover:bg-emerald-900',
    border: 'hover:border-emerald-500',
    text: 'text-emerald-400',
    shadow: 'hover:shadow-emerald-500/20',
    price: 7700,
    isComingSoon: false,
    hero: {
      titleKey: 'hero.title',
      subtitleKey: 'hero.subtitle',
      badge: '동물병원 전용 B2B 처방 솔루션 · 모든 동물을 위한 소화기 케어',
      badgeText: '장 건강',
      badgeColor: 'bg-emerald-600',
      borderColor: 'border-white',
      bgColor: 'bg-white'
    },
    values: {
      title: '에스앤제이의 3대 가치 약속',
      formulaTitle: '독보적인 배합 비율',
      formulaDesc: '임상 현장에서 검증된 강력한 원료 배합으로 확실한 효과를 이끌어냅니다.'
    }
  },
  hepamax: {
    id: 'hepamax',
    name_ko: '몬스멕타 헤파맥스',
    name_en: 'MONSMECTA HEPAMAX',
    volume: '30ml',
    desc: '간 기능 개선 및 장 건강 보조제 (30ml)',
    icon: '🧪',
    color: 'amber',
    bg: 'hover:bg-amber-900',
    border: 'hover:border-amber-500',
    text: 'text-amber-400',
    shadow: 'hover:shadow-amber-500/20',
    price: 3300,
    isComingSoon: false,
    hero: {
      title: '임상 수의사의 해답, HEPAMAX',
      subtitle: '현장 진료의 까다로운 기준을 통과한 간 건강 솔루션. 에스앤제이 동물병원 홍순일 원장이 직접 검증하고 처방합니다.',
      badge: '동물병원 전용 B2B 처방 솔루션 · 간 건강 프리미엄 케어 (30ml)',
      badgeText: '간 건강 (30ml)',
      badgeColor: 'bg-amber-700',
      borderColor: 'border-amber-100',
      bgColor: 'bg-amber-50'
    },
    values: {
      title: '에스앤제이의 3대 가치 약속',
      formulaTitle: '독보적인 배합 비율',
      formulaDesc: '임상 현장에서 검증된 강력한 원료 배합으로 확실한 효과를 이끌어냅니다.'
    }
  },
  urinary: {
    id: 'urinary',
    name_ko: '몬스멕타 레날디톡스',
    name_en: 'MONSMECTA RENAL DETOX',
    volume: '30ml',
    desc: '신장 요독 흡착 및 비뇨기 디톡스 보조제 (30ml)',
    icon: '💧',
    color: 'indigo',
    bg: 'hover:bg-indigo-900',
    border: 'hover:border-indigo-500',
    text: 'text-indigo-400',
    shadow: 'hover:shadow-indigo-500/20',
    price: 7700,
    isComingSoon: false,
    hero: {
      title: '임상 수의사의 해답, RENAL DETOX',
      subtitle: '몬모릴로나이트의 강력한 요독 흡착력과 세계적인 아디세오(Adisseo)의 프리미엄 비타민을 결합한 신장 요독 디톡스 및 비뇨기 건강 보조제입니다.',
      badge: '동물병원 전용 B2B 처방 솔루션 · 신장 요독 디톡스 프리미엄 케어 (30ml)',
      badgeText: '신장/요독 디톡스 (30ml)',
      badgeColor: 'bg-indigo-700',
      borderColor: 'border-indigo-100',
      bgColor: 'bg-indigo-50'
    },
    values: {
      title: '에스앤제이의 3대 가치 약속',
      formulaTitle: '독보적인 배합 비율',
      formulaDesc: '임상 현장에서 검증된 강력한 원료 배합으로 확실한 효과를 이끌어냅니다.'
    }
  },
  cancercare: {
    id: 'cancercare',
    name_ko: '몬스멕타 캔서케어',
    name_en: 'MONSMECTA CANCERCARE',
    volume: '30ml',
    desc: '면역 증진 및 종양 억제 보조제',
    icon: '🛡️',
    color: 'purple',
    bg: 'hover:bg-purple-900',
    border: 'hover:border-purple-500',
    text: 'text-purple-400',
    shadow: 'hover:shadow-purple-500/20',
    price: null,
    isComingSoon: true,
    hero: {
      title: '임상 수의사의 해답, CANCERCARE',
      subtitle: '천연 항암 물질과 몬스멕타의 시너지로 부작용 없이 면역력을 높여주는 종양 억제 보조제입니다.',
      badge: '수석 B2B 처방 전용 / 천연 항암 보조 (출시 예정)',
      badgeText: '항암/면역',
      badgeColor: 'bg-purple-700',
      borderColor: 'border-purple-100',
      bgColor: 'bg-purple-50'
    },
    values: {
      title: '제 3의 보조 치료 옵션',
      formulaTitle: '천연 항암 복합체 배합',
      formulaDesc: '베타글루칸, 알리신, 설포라판, 커큐민 등 검증된 천연 추출물을 배합하여 면역 세포(NK세포)를 활성화하고, 표준 항암 치료의 부작용 완화 및 악액질 방지에 도움을 줍니다.'
    }
  },
  coldzero: {
    id: 'coldzero',
    name_ko: '몬스멕타 콜드제로',
    name_en: 'MONSMECTA COLDZERO',
    volume: '30ml',
    desc: '호흡기 및 감기 예방 보조제',
    icon: '❄️',
    color: 'cyan',
    bg: 'hover:bg-cyan-900',
    border: 'hover:border-cyan-500',
    text: 'text-cyan-400',
    shadow: 'hover:shadow-cyan-500/20',
    price: null,
    isComingSoon: true,
    hero: {
      title: '임상 수의사의 해답, COLDZERO',
      subtitle: '전통 쌍화 처방과 천연 호흡기 케어 성분을 몬스멕타와 결합하여 호흡기 염증 및 초기 감기를 효과적으로 예방하는 보조제입니다.',
      badge: '동물병원 전용 B2B 처방 솔루션 · 호흡기 프리미엄 케어 (출시 예정)',
      badgeText: '호흡기 케어',
      badgeColor: 'bg-cyan-700',
      borderColor: 'border-cyan-100',
      bgColor: 'bg-cyan-50'
    },
    values: {
      title: '천연 호흡기/감기 케어',
      formulaTitle: '쌍화 복합체 및 호흡기 특화 배합',
      formulaDesc: '원기 회복에 탁월한 쌍화 복합 추출물과 퀘르세틴, 맥문동, 유근피 등 천연 호흡기 항염증 성분을 배합하여 기관지 윤활 및 기침 완화에 도움을 줍니다.'
    }
  },
  skincare: {
    id: 'skincare',
    name_ko: '몬스멕타 스킨케어',
    name_en: 'MONSMECTA SKINCARE',
    volume: '30ml',
    desc: '피부 및 아토피 개선 보조제',
    icon: '✨',
    color: 'pink',
    bg: 'hover:bg-pink-900',
    border: 'hover:border-pink-500',
    text: 'text-pink-400',
    shadow: 'hover:shadow-pink-500/20',
    price: null,
    isComingSoon: true,
    hero: {
      title: '임상 수의사의 해답, SKINCARE',
      subtitle: '피부 장벽 강화 성분으로 가려움·발적·아토피를 잡아주는 피부/아토피 프리미엄 케어 보조제입니다.',
      badge: '동물병원 전용 B2B 처방 솔루션 · 피부/아토피 프리미엄 케어 (출시 예정)',
      badgeText: '피부 건강',
      badgeColor: 'bg-pink-700',
      borderColor: 'border-pink-100',
      bgColor: 'bg-pink-50'
    },
    values: {
      title: '에스앤제이의 3대 가치 약속',
      formulaTitle: '피부 장벽 특화 복합 배합',
      formulaDesc: '오메가3, 세라마이드, 비오틴, 아연 등 피부 장벽 재생과 알러지 억제에 검증된 성분을 배합하여 피부 염증 완화 및 모질 개선에 도움을 줍니다.'
    }
  },
  heartcare: {
    id: 'heartcare',
    name_ko: '몬스멕타 하트케어',
    name_en: 'MONSMECTA HEARTCARE',
    volume: '30ml',
    desc: '심장 및 혈행 건강 보조제',
    icon: '❤️',
    color: 'red',
    bg: 'hover:bg-red-900',
    border: 'hover:border-red-500',
    text: 'text-red-400',
    shadow: 'hover:shadow-red-500/20',
    price: null,
    isComingSoon: true,
    hero: {
      title: '임상 수의사의 해답, HEARTCARE',
      subtitle: '코큐텐(Q10)과 산사나무 열매 추출물, L-카르니틴, 타우린, 오메가3를 배합하여 심근 수축력 강화와 혈행 개선을 돕는 심장 및 혈행 프리미엄 케어 보조제입니다.',
      badge: '동물병원 전용 B2B 처방 솔루션 · 심장/혈행 프리미엄 케어 (출시 예정)',
      badgeText: '심장 건강',
      badgeColor: 'bg-red-700',
      borderColor: 'border-red-100',
      bgColor: 'bg-red-50'
    },
    values: {
      title: '심장/혈행 집중 케어',
      formulaTitle: '심장 특화 5중 복합 배합',
      formulaDesc: '코큐텐(Q10) 20%, 산사나무 열매 추출물·L-카르니틴 각 10%, 타우린·오메가3 각 5%의 배합비중으로 심장 근육 에너지 생성, 혈류·혈압 개선, 항염 작용을 돕습니다.'
    }
  },
  jointcare: {
    id: 'jointcare',
    name_ko: '몬스멕타 조인트케어',
    name_en: 'MONSMECTA JOINTCARE',
    volume: '30ml',
    desc: '관절 및 연골 건강 보조제',
    icon: '🦴',
    color: 'blue',
    bg: 'hover:bg-blue-900',
    border: 'hover:border-blue-500',
    text: 'text-blue-400',
    shadow: 'hover:shadow-blue-500/20',
    price: null,
    isComingSoon: true,
    hero: {
      title: '임상 수의사의 해답, JOINTCARE',
      subtitle: 'MSM과 그린립 머슬 추출물, 보스웰리아, 콘드로이친, 오메가3를 배합하여 관절 염증 완화와 연골·윤활액 건강을 돕는 관절/연골 프리미엄 케어 보조제입니다.',
      badge: '동물병원 전용 B2B 처방 솔루션 · 관절/연골 프리미엄 케어 (출시 예정)',
      badgeText: '관절 건강',
      badgeColor: 'bg-blue-700',
      borderColor: 'border-blue-100',
      bgColor: 'bg-blue-50'
    },
    values: {
      title: '에스앤제이의 3대 가치 약속',
      formulaTitle: '관절 특화 5중 복합 배합',
      formulaDesc: 'MSM 20%, 그린립 머슬 추출물·보스웰리아 각 10%, 콘드로이친·오메가3 각 5%의 배합비중으로 연골 재생, 윤활액 유지, 관절 항염을 돕습니다.'
    }
  },
  powerase: {
    id: 'powerase',
    name_ko: '몬스멕타 파워라제',
    name_en: 'MONSMECTA POWERASE',
    volume: '30ml',
    desc: '기력 및 활력 회복 보조제',
    icon: '⚡',
    color: 'orange',
    bg: 'hover:bg-orange-900',
    border: 'hover:border-orange-500',
    text: 'text-orange-400',
    shadow: 'hover:shadow-orange-500/20',
    price: null,
    isComingSoon: true,
    hero: {
      title: '임상 수의사의 해답, POWERASE',
      subtitle: '엔도 프로테아제·알파 아밀라제·라이페이스 3대 소화 효소 배합으로 소화와 영양 흡수를 돕고 기력·활력 회복을 지원하는 프리미엄 케어 보조제입니다.',
      badge: '동물병원 전용 B2B 처방 솔루션 · 활력/기력 프리미엄 케어 (출시 예정)',
      badgeText: '활력 회복',
      badgeColor: 'bg-orange-700',
      borderColor: 'border-orange-100',
      bgColor: 'bg-orange-50'
    },
    values: {
      title: '에스앤제이의 3대 가치 약속',
      formulaTitle: '3대 소화 효소 고활성 배합',
      formulaDesc: '단백질·탄수화물·지방을 분해하는 엔도 프로테아제(506,000 pu/g)·알파 아밀라제(770 u/g)·라이페이스(3,277 u/g) 고활성 효소로 소화·흡수율을 높여 수술 후 회복과 기력 증진을 돕습니다.'
    }
  },
  probiotics: {
    id: 'probiotics',
    name_ko: '몬스멕타 프로바이오틱스',
    name_en: 'MONSMECTA PROBIOTICS',
    volume: '30ml',
    desc: '세계 3대 유산균 듀퐁 다니스코 프리미엄 보조제',
    icon: '🦠',
    color: 'green',
    bg: 'hover:bg-green-900',
    border: 'hover:border-green-500',
    text: 'text-green-400',
    shadow: 'hover:shadow-green-500/20',
    price: null,
    isComingSoon: true,
    hero: {
      title: '세계적 유산균 명가의 선택, PROBIOTICS',
      subtitle: '글로벌 유산균 선도기업 듀퐁 다니스코(DuPont Danisco)의 프리미엄 균주로 완성된 장 건강 특화 보조제입니다.',
      badge: '동물병원 전용 B2B 처방 솔루션 · 듀퐁 다니스코 프리미엄 균주 적용 (출시 예정)',
      badgeText: '듀퐁 다니스코 유산균',
      badgeColor: 'bg-green-700',
      borderColor: 'border-green-100',
      bgColor: 'bg-green-50'
    },
    values: {
      title: '에스앤제이의 3대 가치 약속',
      formulaTitle: '세계 최고 수준의 검증된 균주 배합',
      formulaDesc: '우수한 생존력과 장내 정착력을 자랑하는 듀퐁 다니스코의 임상 검증 원료를 독보적인 비율로 배합했습니다.'
    }
  },
  vitaplus: {
    id: 'vitaplus',
    name_ko: '몬스멕타 비타플러스',
    name_en: 'MONSMECTA VITAPLUS',
    volume: '30ml',
    desc: '종합 비타민 및 미네랄 보조제',
    icon: '💊',
    color: 'yellow',
    bg: 'hover:bg-yellow-900',
    border: 'hover:border-yellow-500',
    text: 'text-yellow-400',
    shadow: 'hover:shadow-yellow-500/20',
    price: null,
    isComingSoon: true,
    hero: {
      title: '임상 수의사의 해답, VITAPLUS',
      subtitle: '비타민 A·C·D3·E·K3·B군 10종을 액상원료 10% 기준으로 정량 배합해 피로 회복·항산화·뼈 건강을 돕는 종합 비타민 프리미엄 케어 보조제입니다.',
      badge: '동물병원 전용 B2B 처방 솔루션 · 비타민/미네랄 프리미엄 케어 (출시 예정)',
      badgeText: '종합 비타민',
      badgeColor: 'bg-yellow-700',
      borderColor: 'border-yellow-100',
      bgColor: 'bg-yellow-50'
    },
    values: {
      title: '에스앤제이의 3대 가치 약속',
      formulaTitle: '종합 비타민 10종 고함량 배합',
      formulaDesc: '비타민 10종을 액상원료 10% 첨가 기준으로 1L 당 함량을 환산해, 피로 회복·항산화·면역·뼈 건강을 종합적으로 돕습니다.'
    }
  }
};

export const PRODUCT_IDS = Object.keys(PRODUCTS);
export const LINEUP_PRODUCTS = PRODUCT_IDS.filter(id => id !== 'monsmecta');

export const getProductDisplayName = (product, isKoreanLang) =>
  isKoreanLang ? product.name_ko : (product.name_en || product.name_ko);
