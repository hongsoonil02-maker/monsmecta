export const PRODUCTS = {
  monsmecta: {
    id: 'monsmecta',
    name_ko: '몬스멕타 (장 건강)',
    name_en: 'MONSMECTA',
    desc: '동물병원 전용 B2B 처방 솔루션 · 모든 동물을 위한 소화기 케어',
    icon: '🧪',
    color: 'emerald',
    bg: 'hover:bg-emerald-900',
    border: 'hover:border-emerald-500',
    text: 'text-emerald-400',
    shadow: 'hover:shadow-emerald-500/20',
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
    desc: '간 기능 개선 및 장 건강 보조제',
    icon: '🧪',
    color: 'amber',
    bg: 'hover:bg-amber-900',
    border: 'hover:border-amber-500',
    text: 'text-amber-400',
    shadow: 'hover:shadow-amber-500/20',
    isComingSoon: true, // As per user context, currently price is 0
    hero: {
      title: '임상 수의사의 해답, HEPAMAX',
      subtitle: '현장 진료의 까다로운 기준을 통과한 간 건강 솔루션. 에스앤제이 동물병원 홍순일 원장이 직접 검증하고 처방합니다.',
      badge: '동물병원 전용 B2B 처방 솔루션 · 간 건강 프리미엄 케어',
      badgeText: '간 건강',
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
  cancercare: {
    id: 'cancercare',
    name_ko: '몬스멕타 캔서케어',
    name_en: 'MONSMECTA CANCERCARE',
    desc: '면역 증진 및 종양 억제 보조제',
    icon: '🛡️',
    color: 'purple',
    bg: 'hover:bg-purple-900',
    border: 'hover:border-purple-500',
    text: 'text-purple-400',
    shadow: 'hover:shadow-purple-500/20',
    isComingSoon: true,
    hero: {
      title: '임상 수의사의 해답, CANCERCARE',
      subtitle: '현장 진료의 까다로운 기준을 통과한 면역 증진 및 종양 억제 보조제입니다.',
      badge: '동물병원 전용 B2B 처방 솔루션 · 종양/면역 프리미엄 케어',
      badgeText: '면역 증진',
      badgeColor: 'bg-purple-700',
      borderColor: 'border-purple-100',
      bgColor: 'bg-purple-50'
    },
    values: {
      title: '에스앤제이의 3대 가치 약속',
      formulaTitle: '독보적인 배합 비율',
      formulaDesc: '임상 현장에서 검증된 강력한 원료 배합으로 확실한 효과를 이끌어냅니다.'
    }
  },
  coldzero: {
    id: 'coldzero',
    name_ko: '몬스멕타 콜드제로',
    name_en: 'MONSMECTA COLDZERO',
    desc: '호흡기 및 감기 예방 보조제',
    icon: '❄️',
    color: 'cyan',
    bg: 'hover:bg-cyan-900',
    border: 'hover:border-cyan-500',
    text: 'text-cyan-400',
    shadow: 'hover:shadow-cyan-500/20',
    isComingSoon: true,
    hero: {
      title: '임상 수의사의 해답, COLDZERO',
      subtitle: '현장 진료의 까다로운 기준을 통과한 호흡기 및 감기 예방 보조제입니다.',
      badge: '동물병원 전용 B2B 처방 솔루션 · 호흡기 프리미엄 케어',
      badgeText: '호흡기 케어',
      badgeColor: 'bg-cyan-700',
      borderColor: 'border-cyan-100',
      bgColor: 'bg-cyan-50'
    },
    values: {
      title: '에스앤제이의 3대 가치 약속',
      formulaTitle: '독보적인 배합 비율',
      formulaDesc: '임상 현장에서 검증된 강력한 원료 배합으로 확실한 효과를 이끌어냅니다.'
    }
  },
  eczema: {
    id: 'eczema',
    name_ko: '몬스멕타 익제마',
    name_en: 'MONSMECTA ECZEMA',
    desc: '피부 및 아토피 개선 보조제',
    icon: '✨',
    color: 'pink',
    bg: 'hover:bg-pink-900',
    border: 'hover:border-pink-500',
    text: 'text-pink-400',
    shadow: 'hover:shadow-pink-500/20',
    isComingSoon: true,
    hero: {
      title: '임상 수의사의 해답, ECZEMA',
      subtitle: '현장 진료의 까다로운 기준을 통과한 피부 및 아토피 개선 보조제입니다.',
      badge: '동물병원 전용 B2B 처방 솔루션 · 피부/아토피 프리미엄 케어',
      badgeText: '피부 건강',
      badgeColor: 'bg-pink-700',
      borderColor: 'border-pink-100',
      bgColor: 'bg-pink-50'
    },
    values: {
      title: '에스앤제이의 3대 가치 약속',
      formulaTitle: '독보적인 배합 비율',
      formulaDesc: '임상 현장에서 검증된 강력한 원료 배합으로 확실한 효과를 이끌어냅니다.'
    }
  },
  heartcare: {
    id: 'heartcare',
    name_ko: '몬스멕타 하트케어',
    name_en: 'MONSMECTA HEARTCARE',
    desc: '심장 및 혈행 건강 보조제',
    icon: '❤️',
    color: 'red',
    bg: 'hover:bg-red-900',
    border: 'hover:border-red-500',
    text: 'text-red-400',
    shadow: 'hover:shadow-red-500/20',
    isComingSoon: true,
    hero: {
      title: '임상 수의사의 해답, HEARTCARE',
      subtitle: '현장 진료의 까다로운 기준을 통과한 심장 및 혈행 건강 보조제입니다.',
      badge: '동물병원 전용 B2B 처방 솔루션 · 심장/혈행 프리미엄 케어',
      badgeText: '심장 건강',
      badgeColor: 'bg-red-700',
      borderColor: 'border-red-100',
      bgColor: 'bg-red-50'
    },
    values: {
      title: '에스앤제이의 3대 가치 약속',
      formulaTitle: '독보적인 배합 비율',
      formulaDesc: '임상 현장에서 검증된 강력한 원료 배합으로 확실한 효과를 이끌어냅니다.'
    }
  },
  jointcare: {
    id: 'jointcare',
    name_ko: '몬스멕타 조인트케어',
    name_en: 'MONSMECTA JOINTCARE',
    desc: '관절 및 연골 건강 보조제',
    icon: '🦴',
    color: 'blue',
    bg: 'hover:bg-blue-900',
    border: 'hover:border-blue-500',
    text: 'text-blue-400',
    shadow: 'hover:shadow-blue-500/20',
    isComingSoon: true,
    hero: {
      title: '임상 수의사의 해답, JOINTCARE',
      subtitle: '현장 진료의 까다로운 기준을 통과한 관절 및 연골 건강 보조제입니다.',
      badge: '동물병원 전용 B2B 처방 솔루션 · 관절/연골 프리미엄 케어',
      badgeText: '관절 건강',
      badgeColor: 'bg-blue-700',
      borderColor: 'border-blue-100',
      bgColor: 'bg-blue-50'
    },
    values: {
      title: '에스앤제이의 3대 가치 약속',
      formulaTitle: '독보적인 배합 비율',
      formulaDesc: '임상 현장에서 검증된 강력한 원료 배합으로 확실한 효과를 이끌어냅니다.'
    }
  },
  powerase: {
    id: 'powerase',
    name_ko: '몬스멕타 파워라제',
    name_en: 'MONSMECTA POWERASE',
    desc: '기력 및 활력 회복 보조제',
    icon: '⚡',
    color: 'orange',
    bg: 'hover:bg-orange-900',
    border: 'hover:border-orange-500',
    text: 'text-orange-400',
    shadow: 'hover:shadow-orange-500/20',
    isComingSoon: true,
    hero: {
      title: '임상 수의사의 해답, POWERASE',
      subtitle: '현장 진료의 까다로운 기준을 통과한 기력 및 활력 회복 보조제입니다.',
      badge: '동물병원 전용 B2B 처방 솔루션 · 활력/기력 프리미엄 케어',
      badgeText: '활력 회복',
      badgeColor: 'bg-orange-700',
      borderColor: 'border-orange-100',
      bgColor: 'bg-orange-50'
    },
    values: {
      title: '에스앤제이의 3대 가치 약속',
      formulaTitle: '독보적인 배합 비율',
      formulaDesc: '임상 현장에서 검증된 강력한 원료 배합으로 확실한 효과를 이끌어냅니다.'
    }
  },
  probiotics: {
    id: 'probiotics',
    name_ko: '몬스멕타 프로바이오틱스',
    name_en: 'MONSMECTA PROBIOTICS',
    desc: '세계 3대 유산균 듀퐁 다니스코 프리미엄 보조제',
    icon: '🦠',
    color: 'green',
    bg: 'hover:bg-green-900',
    border: 'hover:border-green-500',
    text: 'text-green-400',
    shadow: 'hover:shadow-green-500/20',
    hero: {
      title: '세계적 유산균 명가의 선택, PROBIOTICS',
      subtitle: '글로벌 유산균 선도기업 듀퐁 다니스코(DuPont Danisco)의 프리미엄 균주로 완성된 장 건강 특화 보조제입니다.',
      badge: '동물병원 전용 B2B 처방 솔루션 · 듀퐁 다니스코 프리미엄 균주 적용',
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
  urinary: {
    id: 'urinary',
    name_ko: '몬스멕타 유리너리',
    name_en: 'MONSMECTA URINARY',
    desc: '비뇨기 및 신장 건강 보조제',
    icon: '💧',
    color: 'indigo',
    bg: 'hover:bg-indigo-900',
    border: 'hover:border-indigo-500',
    text: 'text-indigo-400',
    shadow: 'hover:shadow-indigo-500/20',
    isComingSoon: true,
    hero: {
      title: '임상 수의사의 해답, URINARY',
      subtitle: '몬모릴로나이트의 강력한 요독 흡착력과 세계적인 아디세오(Adisseo)의 프리미엄 비타민을 결합한 비뇨기 및 신장 건강 보조제입니다.',
      badge: '동물병원 전용 B2B 처방 솔루션 · 요독 흡착 및 비뇨기 프리미엄 케어',
      badgeText: '비뇨/신장 케어',
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
  vitaplus: {
    id: 'vitaplus',
    name_ko: '몬스멕타 비타플러스',
    name_en: 'MONSMECTA VITAPLUS',
    desc: '종합 비타민 및 미네랄 보조제',
    icon: '💊',
    color: 'yellow',
    bg: 'hover:bg-yellow-900',
    border: 'hover:border-yellow-500',
    text: 'text-yellow-400',
    shadow: 'hover:shadow-yellow-500/20',
    isComingSoon: true,
    hero: {
      title: '임상 수의사의 해답, VITAPLUS',
      subtitle: '현장 진료의 까다로운 기준을 통과한 종합 비타민 및 미네랄 보조제입니다.',
      badge: '동물병원 전용 B2B 처방 솔루션 · 비타민/미네랄 프리미엄 케어',
      badgeText: '종합 비타민',
      badgeColor: 'bg-yellow-700',
      borderColor: 'border-yellow-100',
      bgColor: 'bg-yellow-50'
    },
    values: {
      title: '에스앤제이의 3대 가치 약속',
      formulaTitle: '독보적인 배합 비율',
      formulaDesc: '임상 현장에서 검증된 강력한 원료 배합으로 확실한 효과를 이끌어냅니다.'
    }
  }
};

export const PRODUCT_IDS = Object.keys(PRODUCTS);
export const LINEUP_PRODUCTS = PRODUCT_IDS.filter(id => id !== 'monsmecta');
