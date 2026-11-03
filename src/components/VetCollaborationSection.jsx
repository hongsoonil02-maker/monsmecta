import React, { useState, useEffect } from 'react';

const VetCollaborationSection = () => {
  const [promoCode, setPromoCode] = useState('');
  const [isCodeApplied, setIsCodeApplied] = useState(false);
  const [errorMessage, setErrorMessage] = useState('');

  // URL 파라미터 (?ref=... 또는 ?code=...) 자동 감지
  useEffect(() => {
    try {
      const urlParams = new URLSearchParams(window.location.search);
      const ref = urlParams.get('ref') || urlParams.get('code');
      if (ref && (ref.toLowerCase().includes('vettalk') || ref.toLowerCase().includes('park') || ref.toLowerCase().includes('hanam'))) {
        setPromoCode(ref);
        setIsCodeApplied(true);
      }
    } catch {
      // ignore
    }
  }, []);

  const handleApplyCode = (e) => {
    e.preventDefault();
    const clean = promoCode.trim().toLowerCase();
    const validCodes = ['vettalk', '박선생', '하남사랑', '김동준', '사랑', 'hanam', 'vet', 'park'];
    
    if (validCodes.some(c => clean.includes(c)) || clean.length >= 3) {
      setIsCodeApplied(true);
      setErrorMessage('');
    } else {
      setErrorMessage('올바른 카페 제휴 프로모션 코드를 입력해 주세요. (예: vettalk, 박선생)');
    }
  };

  return (
    <section id="collaboration" className="py-14 sm:py-20 bg-gradient-to-b from-white via-emerald-50/40 to-slate-50 border-b border-slate-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Header Badge & Title */}
        <div className="text-center max-w-3xl mx-auto mb-10 sm:mb-14">
          <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-emerald-100 border border-emerald-300 text-emerald-900 text-xs sm:text-sm font-extrabold mb-4 shadow-xs">
            <span>🤝</span>
            <span>OFFICIAL VET PARTNERSHIP</span>
          </div>
          <h2 className="text-2xl sm:text-4xl md:text-5xl font-black text-slate-900 tracking-tight leading-tight">
            하남사랑동물병원 <span className="text-emerald-700">김동준 원장</span>
            <span className="block text-lg sm:text-2xl md:text-3xl font-extrabold text-teal-800 mt-2">
              (네이버 10만 카페 &lsquo;온라인동물병원&rsquo; 박선생) 공식 협업
            </span>
          </h2>
          <p className="mt-4 text-slate-600 text-sm sm:text-base md:text-lg leading-relaxed break-keep">
            임상 현장의 전문 처방 노하우와 10만 반려인의 건강 멘토(박선생)로 신뢰받는 김동준 원장과 몬스멕타가 함께합니다. 
            가격 덤핑 없이 안전한 정품 공급과 전용 사은 혜택을 약속드립니다.
          </p>
        </div>

        {/* Unified Single Profile Card (1인 단일 통합 카드 - 중복 분리 제거) */}
        <div className="bg-white rounded-3xl p-6 sm:p-10 border border-emerald-200/90 shadow-xl hover:shadow-2xl transition-all relative overflow-hidden mb-12">
          <div className="absolute top-0 right-0 w-64 h-64 bg-gradient-to-bl from-teal-500/10 via-emerald-500/5 to-transparent rounded-bl-full pointer-events-none" />

          {/* Top Profile Header */}
          <div className="flex flex-col md:flex-row md:items-center justify-between gap-6 pb-6 border-b border-slate-100">
            <div className="flex items-start sm:items-center gap-4 sm:gap-5">
              <div className="w-16 h-16 sm:w-20 sm:h-20 rounded-2xl bg-gradient-to-br from-emerald-600 to-teal-800 text-white flex items-center justify-center text-3xl sm:text-4xl shadow-md font-bold shrink-0">
                👨‍⚕️
              </div>
              <div className="space-y-1">
                <div className="flex flex-wrap items-center gap-2">
                  <span className="text-[11px] font-black text-emerald-800 bg-emerald-50 px-2.5 py-1 rounded-md border border-emerald-200">
                    🏥 임상 자문 및 처방 전문의
                  </span>
                  <span className="text-[11px] font-black text-teal-800 bg-teal-50 px-2.5 py-1 rounded-md border border-teal-200">
                    💬 네이버 10만 반려인 카페 운영자 &lsquo;박선생&rsquo;
                  </span>
                </div>
                <h3 className="text-xl sm:text-3xl font-black text-slate-900 tracking-tight">
                  김동준 대표원장 <span className="text-teal-700 font-extrabold text-base sm:text-xl">(하남사랑동물병원 · 닉네임: 박선생)</span>
                </h3>
                <p className="text-xs sm:text-sm text-slate-500 font-medium">
                  경기 하남시 소재 하남사랑동물병원 대표원장 · 소화기 내과 및 신장 질환 표적 케어 전문 임상 수의사
                </p>
              </div>
            </div>

            <div className="shrink-0 flex sm:flex-col items-center sm:items-end justify-between gap-1 text-xs">
              <span className="px-3 py-1 rounded-full bg-slate-100 text-slate-700 font-bold">📍 경기 하남시 소재 오프라인 병원</span>
              <span className="text-emerald-700 font-extrabold text-xs sm:text-sm">전문 임상 자문처</span>
            </div>
          </div>

          {/* Vet Quote */}
          <div className="my-6 sm:my-8 bg-slate-50/90 border-l-4 border-emerald-600 p-5 sm:p-6 rounded-r-2xl">
            <blockquote className="text-xs sm:text-base text-slate-700 leading-relaxed font-medium break-keep">
              “만성 묽은변과 파보·코로나 장염, 간·신장 질환 환축에서 몬스멕타는 단순 보조제를 넘어 
              <strong className="text-slate-900 font-black"> 정전기적 독소 흡착과 신속한 장 점막 코팅</strong>으로 신뢰할 수 있는 임상 결과를 보여줍니다. 
              동시에 밤마다 아이들 설사로 발을 동동 구르시는 10만 카페 가족분들을 위해, 
              불법 덤핑 대신 <strong className="text-emerald-800 font-black">수의사가 보증하는 안전한 정품 공급과 전용 무료배송·사은품 혜택</strong>을 약속드립니다.”
            </blockquote>
          </div>

          {/* 3 Key Guarantees Grid */}
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 text-xs sm:text-sm">
            <div className="bg-emerald-50/60 border border-emerald-100 rounded-2xl p-4">
              <span className="text-emerald-700 font-black block text-sm mb-1">✓ 정품 규격 처방</span>
              <p className="text-slate-600 text-xs leading-relaxed">
                임상 현장과 동일한 전 제품 100ml 정품 처방 기준 엄수
              </p>
            </div>
            <div className="bg-teal-50/60 border border-teal-100 rounded-2xl p-4">
              <span className="text-teal-700 font-black block text-sm mb-1">✓ 권장소비자가격 보호</span>
              <p className="text-slate-600 text-xs leading-relaxed">
                몬스멕타 15,000원 / 헤파맥스 17,000원 / 레날 22,000원
              </p>
            </div>
            <div className="bg-amber-50/60 border border-amber-100 rounded-2xl p-4">
              <span className="text-amber-800 font-black block text-sm mb-1">✓ 카페 회원 단독 혜택</span>
              <p className="text-slate-600 text-xs leading-relaxed">
                시크릿 코드 적용 시 무료배송 + 정품 체험 파우치 무료 증정
              </p>
            </div>
          </div>

        </div>

        {/* Secret Promotion Code Box */}
        <div className="bg-gradient-to-r from-emerald-900 via-[#004d38] to-teal-950 rounded-3xl p-6 sm:p-10 text-white shadow-2xl relative overflow-hidden">
          <div className="max-w-2xl mx-auto text-center space-y-4">
            <div className="inline-block px-3 py-1 bg-amber-400 text-slate-950 text-xs font-black rounded-full uppercase tracking-wider">
              🎁 Secret Benefit Voucher
            </div>
            <h3 className="text-2xl sm:text-3xl font-black tracking-tight">
              온라인동물병원 카페 회원(박선생 추천) 전용 시크릿 프로모션
            </h3>
            <p className="text-xs sm:text-sm text-emerald-200 leading-relaxed break-keep">
              카페 게시판 또는 박선생님 추천 글에서 확인하신 <strong>시크릿 코드</strong>를 입력하시면, 
              <strong> [전 제품 무료배송] + [몬스멕타 특별 체험용 파우치 사은품]</strong>이 주문 시 자동 증정됩니다.
            </p>

            {isCodeApplied ? (
              <div className="bg-white/10 backdrop-blur-md border-2 border-amber-300 rounded-2xl p-5 mt-6 animate-in zoom-in-95">
                <div className="flex items-center justify-center gap-2 text-amber-300 text-lg font-black mb-1">
                  <span>🎉</span>
                  <span>카페 제휴 회원 인증이 완료되었습니다!</span>
                </div>
                <p className="text-xs sm:text-sm text-slate-100 mb-4">
                  코드: <strong className="text-amber-300 uppercase underline">{promoCode || 'VETTALK'}</strong> | 혜택: <strong>전 제품 무료배송 + 정품 체험 파우치 무료 증정</strong> 적용 중
                </p>
                <a
                  href="#order"
                  className="inline-flex items-center justify-center gap-2 px-8 py-3.5 bg-amber-400 hover:bg-amber-300 text-slate-950 font-black text-sm rounded-xl shadow-lg transition-all transform hover:-translate-y-0.5"
                >
                  <span>혜택 적용하고 주문하러 가기</span>
                  <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M14 5l7 7m0 0l-7 7m7-7H3" />
                  </svg>
                </a>
              </div>
            ) : (
              <form onSubmit={handleApplyCode} className="mt-6 flex flex-col sm:flex-row items-center justify-center gap-3 max-w-md mx-auto">
                <input
                  type="text"
                  value={promoCode}
                  onChange={(e) => setPromoCode(e.target.value)}
                  placeholder="카페 전용 시크릿 코드 (예: vettalk)"
                  className="w-full sm:w-auto flex-1 px-4 py-3.5 rounded-xl bg-white/10 border border-white/30 text-white placeholder-emerald-300/70 text-sm font-bold focus:outline-none focus:ring-2 focus:ring-amber-400 focus:bg-white/20 transition-all text-center sm:text-left"
                />
                <button
                  type="submit"
                  className="w-full sm:w-auto px-6 py-3.5 bg-amber-400 hover:bg-amber-300 text-slate-950 font-black text-sm rounded-xl shadow-md transition-all shrink-0 cursor-pointer"
                >
                  코드 적용
                </button>
              </form>
            )}

            {errorMessage && (
              <p className="text-xs text-rose-300 font-bold mt-2">{errorMessage}</p>
            )}
          </div>
        </div>

      </div>
    </section>
  );
};

export default VetCollaborationSection;
