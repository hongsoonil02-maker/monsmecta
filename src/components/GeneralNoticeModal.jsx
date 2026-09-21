import React, { useState, useEffect } from 'react';

const GeneralNoticeModal = () => {
  const [isOpen, setIsOpen] = useState(false);

  useEffect(() => {
    try {
      const today = new Date().toISOString().slice(0, 10);
      const saved = localStorage.getItem('hide_monsmecta_general_notice');
      if (saved !== today) {
        setIsOpen(true);
      }
    } catch {
      setIsOpen(true);
    }
  }, []);

  const handleClose = () => {
    setIsOpen(false);
  };

  const handleHideToday = () => {
    try {
      const today = new Date().toISOString().slice(0, 10);
      localStorage.setItem('hide_monsmecta_general_notice', today);
    } catch { /* ignore */ }
    setIsOpen(false);
  };

  if (!isOpen) return null;

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md animate-fade-in"
      role="dialog"
      aria-modal="true"
      onClick={handleClose}
    >
      <div
        className="w-full max-w-xl max-h-[92vh] overflow-y-auto bg-slate-900 border border-slate-700/80 rounded-3xl shadow-2xl text-start text-white relative"
        onClick={(e) => e.stopPropagation()}
      >
        <button
          onClick={handleClose}
          className="absolute top-4 right-4 text-slate-400 hover:text-white text-lg p-2 rounded-full hover:bg-slate-800 transition z-10"
          aria-label="닫기"
        >
          ✕
        </button>

        {/* 상단 헤더 */}
        <div className="bg-gradient-to-r from-emerald-800 via-teal-800 to-slate-900 p-6 sm:p-7 rounded-t-3xl border-b border-slate-700 relative overflow-hidden">
          <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/10 backdrop-blur-md text-[11px] font-bold text-emerald-200 border border-white/20 mb-2.5">
            <span>🛡️</span>
            <span>(주)한국아그로 공식 알림</span>
          </div>
          <h3 className="text-xl sm:text-2xl font-black text-white leading-snug break-keep">
            몬스멕타(Monsmecta)는<br />
            동물병원 수의사 전용 처방 제품입니다
          </h3>
          <p className="text-xs sm:text-sm text-emerald-100/90 mt-2 font-medium leading-relaxed break-keep">
            본 사이트는 동물병원 수의사 선생님들의 권익과 진료 체계를 보호하기 위해 폐쇄형 B2B 인증제로 운영됩니다.
          </p>
        </div>

        {/* 본문 콘텐츠 */}
        <div className="p-6 sm:p-7 space-y-4 text-xs sm:text-sm">
          <div className="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 space-y-1.5">
            <div className="flex items-center gap-2 text-amber-300 font-bold text-xs">
              <span>🔒</span>
              <span>비공개 영역 (수의사 전용) 안내</span>
            </div>
            <p className="text-slate-300 text-xs leading-relaxed break-keep">
              <strong>공급 단가, 병원 발주 시스템, 수의사 전용 임상 프로토콜 다운로드는 사업자 등록증 인증 회원에게만 노출</strong>됩니다. 일반인에게는 도매 가격 및 발주 기능이 공개되지 않습니다.
            </p>
          </div>

          <div className="space-y-3 pt-1">
            {/* 동물병원 내원 안내 */}
            <div className="bg-slate-800/80 border border-slate-700 rounded-2xl p-4 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
              <div className="space-y-1">
                <span className="text-[11px] font-bold text-blue-400">🏥 전문 진료가 필요한 경우</span>
                <p className="text-xs font-semibold text-white">가까운 취급 동물병원 내원 및 상담</p>
                <p className="text-[11px] text-slate-400">혈변, 탈수, 발열 등 응급 증상 시 동물병원 방문 권장</p>
              </div>
              <a
                href="tel:010-5407-5708"
                className="shrink-0 px-3.5 py-2 bg-blue-600 hover:bg-blue-500 text-white font-bold rounded-xl text-xs transition"
              >
                취급 병원 문의 📞
              </a>
            </div>

            {/* 일반 상비용 파보겔 안내 */}
            <div className="bg-emerald-950/40 border border-emerald-500/40 rounded-2xl p-4 space-y-2.5">
              <div className="space-y-1">
                <div className="flex items-center justify-between">
                  <span className="text-[11px] font-bold text-emerald-400">🚀 긴급 가정 상비용</span>
                  <span className="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 text-[10px] font-bold">익일 로켓배송</span>
                </div>
                <p className="text-xs font-bold text-white">
                  동일 나노 복합 포뮬러 가정 상비용 <span className="text-emerald-300">[파보겔]</span> 바로 구매
                </p>
                <p className="text-[11px] text-slate-300 leading-relaxed">
                  몬스멕타와 동일한 초미세 나노 몬모릴로나이트(800m²/g) & 특허 유산균 배양물이 함유된 1초 원터치 펌프형 가정용 보조사료입니다.
                </p>
              </div>

              <div className="grid grid-cols-2 gap-2 pt-1">
                <a
                  href="https://www.coupang.com/vp/products/9690739565?itemId=28983118193&vendorItemId=95912261090"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center justify-center gap-1 py-2.5 px-2 bg-[#e31837] hover:bg-[#c9122e] text-white font-bold rounded-xl text-xs transition"
                >
                  쿠팡 로켓배송
                </a>
                <a
                  href="https://smartstore.naver.com/petschury/products/13718496355"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center justify-center gap-1 py-2.5 px-2 bg-[#03c75a] hover:bg-[#02b350] text-white font-bold rounded-xl text-xs transition"
                >
                  스마트스토어
                </a>
              </div>
            </div>
          </div>

          <div className="pt-2 flex items-center justify-between text-xs border-t border-slate-800">
            <button
              onClick={handleHideToday}
              className="text-slate-400 hover:text-slate-200 transition"
            >
              오늘 하루 보지 않기
            </button>
            <button
              onClick={handleClose}
              className="text-white px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 transition"
            >
              닫기
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default GeneralNoticeModal;