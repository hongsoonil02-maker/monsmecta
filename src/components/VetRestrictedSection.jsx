import React from 'react';

const VetRestrictedSection = ({ onOpenSampleModal }) => {
  return (
    <section id="restricted-vet" className="py-10 bg-slate-900 text-slate-100 border-y border-slate-800">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6">
        {/* 헤더 & 정책 알림 */}
        <div className="bg-slate-950/90 border-2 border-dashed border-slate-700/90 rounded-3xl p-6 sm:p-9 space-y-6 relative overflow-hidden shadow-2xl">
          <div className="absolute top-0 right-0 transform translate-x-4 -translate-y-4 opacity-5 text-9xl pointer-events-none select-none">
            🔒
          </div>

          <div className="space-y-3 border-b border-slate-800 pb-5">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-red-500/10 text-red-300 text-xs font-bold border border-red-500/30">
              <span>🔒 RESTRICTED AREA</span>
              <span>·</span>
              <span>동물병원 수의사 전용 비공개 영역</span>
            </div>
            <h3 className="text-2xl sm:text-3xl font-black text-white flex items-center gap-2.5">
              <span>비공개 영역 (수의사 전용)</span>
            </h3>
            <p className="text-xs sm:text-sm text-slate-300 leading-relaxed font-medium bg-slate-900/90 p-4 rounded-2xl border border-slate-800 break-keep">
              <strong className="text-amber-300 font-bold">공급 단가, 병원 발주 시스템, 수의사 전용 임상 프로토콜 다운로드는 사업자 등록증 인증 회원에게만 노출됩니다.</strong><br />
              일반 반려인 및 비인증 사용자에게는 어떠한 경우에도 도매 가격 및 발주 기능이 공개되지 않으며, 전국 동물병원 원장님들의 처방 진료 체계를 철저히 보호합니다.
            </p>
          </div>

          {/* 3대 잠금 카드 (블러 & 보안 처리 UI) */}
          <div className="grid md:grid-cols-3 gap-4">
            {/* 잠금 1: 공급 단가 */}
            <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 relative overflow-hidden flex flex-col justify-between group hover:border-slate-700 transition">
              <div className="space-y-2.5">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-bold text-slate-400">RESTRICTED #01</span>
                  <span className="px-2 py-0.5 rounded bg-red-500/20 text-red-300 text-[10px] font-bold border border-red-500/30">
                    🔒 비공개 락
                  </span>
                </div>
                <h4 className="text-base font-bold text-white">병원 도매 공급 단가표</h4>
                <div className="filter blur-[3px] select-none text-slate-500 text-xs space-y-1 py-1">
                  <p>• 몬스멕타 100ml / 500ml 병원 공급 기준가</p>
                  <p>• 10병 / 30병 / 50병 이상 대량 구매 할인율</p>
                  <p>• 전자세금계산서 발행 및 도매 유통 특전</p>
                </div>
                <p className="text-[11px] text-amber-200/80 leading-normal">
                  * 사업자등록증 및 수의사 면허 확인 후 즉시 공개
                </p>
              </div>

              <div className="pt-4">
                <a
                  href="#order-section"
                  className="w-full py-2.5 px-3 bg-slate-800 hover:bg-slate-700 text-slate-200 hover:text-white text-xs font-semibold rounded-xl border border-slate-700 transition flex items-center justify-center gap-1.5"
                >
                  <span>🔒 사업자 인증 후 발주하기</span>
                </a>
              </div>
            </div>

            {/* 잠금 2: 병원 발주 시스템 */}
            <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 relative overflow-hidden flex flex-col justify-between group hover:border-slate-700 transition">
              <div className="space-y-2.5">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-bold text-slate-400">RESTRICTED #02</span>
                  <span className="px-2 py-0.5 rounded bg-red-500/20 text-red-300 text-[10px] font-bold border border-red-500/30">
                    🔒 비공개 락
                  </span>
                </div>
                <h4 className="text-base font-bold text-white">동물병원 전용 발주 시스템</h4>
                <div className="filter blur-[3px] select-none text-slate-500 text-xs space-y-1 py-1">
                  <p>• 동물병원 정회원 전용 실시간 직발주 창구</p>
                  <p>• 당일 본사 특급 출고 및 배송 현황 추적</p>
                  <p>• 병원별 맞춤형 월간 후불 정산 관리</p>
                </div>
                <p className="text-[11px] text-amber-200/80 leading-normal">
                  * 승인된 동물병원 회원 전용 직거래 시스템
                </p>
              </div>

              <div className="pt-4">
                <button
                  type="button"
                  onClick={onOpenSampleModal}
                  className="w-full py-2.5 px-3 bg-blue-600 hover:bg-blue-500 text-white text-xs font-semibold rounded-xl transition flex items-center justify-center gap-1.5 shadow-md shadow-blue-600/30"
                >
                  <span>🎁 원장님 본품 무료샘플 신청</span>
                </button>
              </div>
            </div>

            {/* 잠금 3: 임상 프로토콜 */}
            <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 relative overflow-hidden flex flex-col justify-between group hover:border-slate-700 transition">
              <div className="space-y-2.5">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-bold text-slate-400">RESTRICTED #03</span>
                  <span className="px-2 py-0.5 rounded bg-red-500/20 text-red-300 text-[10px] font-bold border border-red-500/30">
                    🔒 비공개 락
                  </span>
                </div>
                <h4 className="text-base font-bold text-white">수의사용 임상 프로토콜 (PDF)</h4>
                <div className="filter blur-[3px] select-none text-slate-500 text-xs space-y-1 py-1">
                  <p>• 정성대 원장 임상 증례집 및 처방 가이드</p>
                  <p>• 박봉균 교수 바이러스 흡착 기전 학술 백서</p>
                  <p>• 원내 비치용 환자 상담 리플렛 원본</p>
                </div>
                <p className="text-[11px] text-amber-200/80 leading-normal">
                  * 원내 진료 및 학술 참고용 전문 리포트
                </p>
              </div>

              <div className="pt-4">
                <a
                  href="tel:010-5407-5708"
                  className="w-full py-2.5 px-3 bg-slate-800 hover:bg-slate-700 text-slate-200 hover:text-white text-xs font-semibold rounded-xl border border-slate-700 transition flex items-center justify-center gap-1.5"
                >
                  <span>📞 학술자료 유선 요청</span>
                </a>
              </div>
            </div>
          </div>

          {/* 일반 반려인을 위한 파보겔 즉시 구매 대안 박스 */}
          <div className="bg-gradient-to-r from-emerald-950/60 via-slate-900 to-slate-900 border border-emerald-500/40 rounded-2xl p-5 sm:p-6 flex flex-col md:flex-row items-center justify-between gap-4">
            <div className="space-y-1 text-center md:text-start">
              <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 text-[11px] font-bold">
                <span>🐶</span>
                <span>일반 반려인 / 보호자 안내</span>
              </div>
              <h4 className="text-base sm:text-lg font-bold text-white">
                소중한 아이를 위한 가정 상비용 보조제가 필요하신가요?
              </h4>
              <p className="text-xs text-slate-300 leading-relaxed">
                몬스멕타와 동일한 핵심 포뮬러(초미세 나노 몬모릴로나이트 800m²/g & 특허 유산균 배양물) 기반의 가정 상비용 보조사료 <strong>[파보겔(Parvogel)]</strong>을 공식 온라인몰에서 즉시 주문하실 수 있습니다.
              </p>
            </div>

            <div className="flex items-center gap-2 shrink-0 w-full md:w-auto justify-center">
              <a
                href="https://www.coupang.com/vp/products/9690739565?itemId=28983118193&vendorItemId=95912261090"
                target="_blank"
                rel="noopener noreferrer"
                className="px-4 py-2.5 bg-[#e31837] hover:bg-[#c9122e] text-white text-xs font-bold rounded-xl shadow-md transition"
              >
                🚀 쿠팡 로켓배송
              </a>
              <a
                href="https://smartstore.naver.com/petschury/products/13718496355"
                target="_blank"
                rel="noopener noreferrer"
                className="px-4 py-2.5 bg-[#03c75a] hover:bg-[#02b350] text-white text-xs font-bold rounded-xl shadow-md transition"
              >
                🟢 네이버 스마트스토어
              </a>
              <a
                href="https://parvogel.kr/"
                target="_blank"
                rel="noopener noreferrer"
                className="px-3.5 py-2.5 bg-slate-800 hover:bg-slate-700 text-emerald-400 text-xs font-bold rounded-xl border border-slate-700 transition"
              >
                파보겔몰 →
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default VetRestrictedSection;