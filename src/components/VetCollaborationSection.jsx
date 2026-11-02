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
        <div className="text-center max-w-3xl mx-auto mb-12 sm:mb-16">
          <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-emerald-100 border border-emerald-300 text-emerald-900 text-xs sm:text-sm font-extrabold mb-4 shadow-xs">
            <span>🤝</span>
            <span>OFFICIAL VET PARTNERSHIP</span>
          </div>
          <h2 className="text-2xl sm:text-4xl md:text-5xl font-black text-slate-900 tracking-tight leading-tight">
            하남사랑동물병원 <span className="text-emerald-700">김동준 원장</span> &amp;<br className="hidden sm:inline" />
            온라인동물병원 카페 <span className="text-teal-700">박선생</span> 공식 협업
          </h2>
          <p className="mt-4 text-slate-600 text-sm sm:text-base md:text-lg leading-relaxed break-keep">
            임상 현장에서 검증된 전문 수의사의 처방 노하우와 10만 반려동물 보호자의 건강 멘토가 함께합니다. 
            가격 덤핑 없이 안전한 정품 공급과 전용 사은 혜택을 약속드립니다.
          </p>
        </div>

        {/* 2 Partners Bento Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 sm:gap-8 mb-12">
          
          {/* Partner 1: 하남사랑동물병원 김동준 원장 */}
          <div className="bg-white rounded-3xl p-6 sm:p-8 border border-emerald-200/80 shadow-md hover:shadow-xl transition-all relative overflow-hidden flex flex-col justify-between">
            <div className="absolute top-0 right-0 w-32 h-32 bg-emerald-500/10 rounded-bl-full pointer-events-none"></div>
            <div>
              <div className="flex items-center gap-4 mb-5">
                <div className="w-14 h-14 sm:w-16 sm:h-16 rounded-2xl bg-gradient-to-br from-emerald-600 to-teal-800 text-white flex items-center justify-center text-3xl shadow-md font-bold">
                  👨‍⚕️
                </div>
                <div>
                  <span className="text-[11px] font-extrabold text-emerald-800 uppercase tracking-wider bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">
                    임상 자문 및 공식 처방 병원
                  </span>
                  <h3 className="text-xl sm:text-2xl font-black text-slate-900 mt-0.5">
                    하남사랑동물병원 <span className="text-emerald-700">김동준 원장</span>
                  </h3>
                  <p className="text-xs text-slate-500">소화기 내과 · 신장 요독 케어 전문 임상 수의사</p>
                </div>
              </div>

              <blockquote className="text-xs sm:text-sm text-slate-700 leading-relaxed bg-slate-50 border-l-4 border-emerald-600 p-4 rounded-r-xl mb-5 break-keep">
                “만성 묽은변과 파보·코로나 장염, 간·신장 질환 환축에서 몬스멕타는 단순 영양제가 아닌 
                <strong> 정전기적 독소 흡착과 신속한 장 점막 코팅</strong>으로 실질적인 임상 결과를 보여줍니다. 
                병원 처방 기준의 정품 라인업을 안심하고 급여하셔도 좋습니다.”
              </blockquote>

              <div className="space-y-1.5 text-xs text-slate-600">
                <div className="flex items-center gap-2 font-semibold">
                  <span className="text-emerald-600">✓</span>
                  <span>임상 처방 공식 규격: 전 제품 100ml 정품 처방</span>
                </div>
                <div className="flex items-center gap-2 font-semibold">
                  <span className="text-emerald-600">✓</span>
                  <span>권장소비자가: 몬스멕타 15,000원 / 헤파맥스 17,000원 / 레날 22,000원</span>
                </div>
              </div>
            </div>

            <div className="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
              <span className="font-bold text-slate-700">📍 경기 하남시 소재 오프라인 진료 병원</span>
              <span className="text-emerald-700 font-extrabold">전문 임상 자문처</span>
            </div>
          </div>

          {/* Partner 2: 온라인동물병원 카페 (운영자: 박선생) */}
          <div className="bg-white rounded-3xl p-6 sm:p-8 border border-teal-200/80 shadow-md hover:shadow-xl transition-all relative overflow-hidden flex flex-col justify-between">
            <div className="absolute top-0 right-0 w-32 h-32 bg-teal-500/10 rounded-bl-full pointer-events-none"></div>
            <div>
              <div className="flex items-center gap-4 mb-5">
                <div className="w-14 h-14 sm:w-16 sm:h-16 rounded-2xl bg-gradient-to-br from-teal-600 to-cyan-800 text-white flex items-center justify-center text-3xl shadow-md font-bold">
                  💬
                </div>
                <div>
                  <span className="text-[11px] font-extrabold text-teal-800 uppercase tracking-wider bg-teal-50 px-2 py-0.5 rounded border border-teal-200">
                    반려동물 건강 커뮤니티 파트너십
                  </span>
                  <h3 className="text-xl sm:text-2xl font-black text-slate-900 mt-0.5">
                    온라인동물병원 카페 <span className="text-teal-700">(운영자: 박선생)</span>
                  </h3>
                  <p className="text-xs text-slate-500">반려인 10만 회원 소통 커뮤니티 · 분변 케어 멘토링</p>
                </div>
              </div>

              <blockquote className="text-xs sm:text-sm text-slate-700 leading-relaxed bg-slate-50 border-l-4 border-teal-600 p-4 rounded-r-xl mb-5 break-keep">
                “아이들이 갑자기 무른변이나 설사를 볼 때 밤마다 발을 동동 구르시는 카페 가족분들을 위해, 
                수의사 선생님들이 실제 처방하는 몬스멕타와 손을 잡았습니다. 
                <strong> 시장 질서를 해치는 불법 덤핑 대신, 카페 회원만을 위한 정품 무료배송과 전용 사은품 혜택</strong>을 준비했습니다.”
              </blockquote>

              <div className="space-y-1.5 text-xs text-slate-600">
                <div className="flex items-center gap-2 font-semibold">
                  <span className="text-teal-600">✓</span>
                  <span>카페 회원 전용 시크릿 프로모션 코드 상시 운영</span>
                </div>
                <div className="flex items-center gap-2 font-semibold">
                  <span className="text-teal-600">✓</span>
                  <span>Fecal Score(변 상태 1~7단계) 맞춤 상담 피드백 연계</span>
                </div>
              </div>
            </div>

            <div className="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
              <span className="font-bold text-slate-700">네이버 대표 반려동물 건강 카페</span>
              <span className="text-teal-700 font-extrabold">공식 제휴 채널</span>
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
              온라인동물병원 카페 회원 전용 시크릿 프로모션
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

