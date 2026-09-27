import React from 'react';

const VetRestrictedSection = ({ onOpenSampleModal }) => {
  return (
    <section aria-labelledby="restricted-heading" className="my-12">
      <div className="max-w-6xl mx-auto px-4 sm:px-6">
        <div className="bg-[#00281d] border-2 border-dashed border-emerald-700/80 rounded-3xl p-6 sm:p-9 space-y-6 relative overflow-hidden shadow-2xl text-slate-100">
          <div className="absolute top-0 right-0 transform translate-x-4 -translate-y-4 opacity-5 text-9xl pointer-events-none select-none">
            🔒
          </div>

          <div className="space-y-2 border-b border-emerald-900/80 pb-5 text-start">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/10 text-amber-300 text-xs font-bold border border-amber-500/30">
              <span>🔒 RESTRICTED AREA</span>
              <span>·</span>
              <span>동물병원 수의사 전용 비공개 영역</span>
            </div>
            <h3 id="restricted-heading" className="text-xl sm:text-2xl font-black text-white flex items-center gap-2.5">
              <span>비공개 영역 (수의사 전용)</span>
            </h3>
            <p className="text-xs sm:text-sm text-emerald-100/80 leading-relaxed font-medium bg-[#001f16] p-4 rounded-2xl border border-emerald-900/80 break-keep">
              <strong className="text-amber-300 font-bold">공급 단가, 병원 발주 시스템, 수의사 전용 임상 프로토콜 다운로드는 사업자 등록증 인증 회원에게만 노출됩니다.</strong><br />
              일반 반려인 및 비인증 사용자에게는 어떠한 경우에도 도매 가격 및 발주 기능이 공개되지 않으며, 전국 동물병원 원장님들의 처방 진료 체계를 철저히 보호합니다.
            </p>
          </div>

          {/* 3대 잠금 카드 (블러 & 보안 처리 UI) */}
          <div className="grid md:grid-cols-3 gap-4 text-start">
            {/* 잠금 1: 공급 단가 */}
            <div className="bg-[#002016]/90 border border-emerald-900/80 rounded-2xl p-5 relative overflow-hidden flex flex-col justify-between group hover:border-emerald-600 transition">
              <div className="space-y-2.5">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-bold text-emerald-400">RESTRICTED #01</span>
                  <span className="px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 text-[10px] font-bold border border-amber-500/30">
                    🔒 비공개 락
                  </span>
                </div>
                <h4 className="text-base font-bold text-white">병원 도매 공급 단가표</h4>
                <div className="filter blur-[3px] select-none text-emerald-200/50 text-xs space-y-1 py-1">
                  <p>• 몬스멕타 100ml / 500ml 병원 공급 기준가</p>
                  <p>• 10병 / 30병 / 50병 이상 대량 구매 할인율</p>
                  <p>• 전자세금계산서 발행 및 도매 유통 안전</p>
                </div>
                <p className="text-[11px] text-amber-200/90 leading-normal">
                  * 사업자등록증 및 수의사 면허 확인 후 즉시 공개
                </p>
              </div>

              <div className="pt-4">
                <a
                  href="#order-section"
                  className="w-full py-2.5 px-3 bg-[#003828] hover:bg-emerald-800 text-emerald-100 hover:text-white text-xs font-semibold rounded-xl border border-emerald-700/60 transition flex items-center justify-center gap-1.5"
                >
                  <span>🔒 사업자 인증 후 발주하기</span>
                </a>
              </div>
            </div>

            {/* 잠금 2: 병원 발주 시스템 */}
            <div className="bg-[#002016]/90 border border-emerald-900/80 rounded-2xl p-5 relative overflow-hidden flex flex-col justify-between group hover:border-emerald-600 transition">
              <div className="space-y-2.5">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-bold text-emerald-400">RESTRICTED #02</span>
                  <span className="px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 text-[10px] font-bold border border-amber-500/30">
                    🔒 비공개 락
                  </span>
                </div>
                <h4 className="text-base font-bold text-white">동물병원 전용 발주 시스템</h4>
                <div className="filter blur-[3px] select-none text-emerald-200/50 text-xs space-y-1 py-1">
                  <p>• 동물병원 정회원 전용 실시간 직발주 창구</p>
                  <p>• 당일 본사 특급 출고 및 배송 상황 추적</p>
                  <p>• 병원별 맞춤형 월간 후불 정산 관리</p>
                </div>
                <p className="text-[11px] text-amber-200/90 leading-normal">
                  * 승인된 동물병원 정회원 전용 직거래 시스템
                </p>
              </div>

              <div className="pt-4">
                <button
                  type="button"
                  onClick={onOpenSampleModal}
                  className="w-full py-2.5 px-3 bg-gradient-to-r from-[#00513b] to-emerald-600 hover:from-emerald-700 hover:to-emerald-500 text-white text-xs font-bold rounded-xl transition flex items-center justify-center gap-1.5 shadow-md border border-emerald-500/40"
                >
                  <span>📝 원장님 전용 무료샘플 신청</span>
                </button>
              </div>
            </div>

            {/* 잠금 3: 임상 프로토콜 */}
            <div className="bg-[#002016]/90 border border-emerald-900/80 rounded-2xl p-5 relative overflow-hidden flex flex-col justify-between group hover:border-emerald-600 transition">
              <div className="space-y-2.5">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-bold text-emerald-400">RESTRICTED #03</span>
                  <span className="px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 text-[10px] font-bold border border-amber-500/30">
                    🔒 비공개 락
                  </span>
                </div>
                <h4 className="text-base font-bold text-white">수의사용 임상 프로토콜 (PDF)</h4>
                <div className="filter blur-[3px] select-none text-emerald-200/50 text-xs space-y-1 py-1">
                  <p>• 정성대 원장 임상 증례집 및 처방 가이드</p>
                  <p>• 박봉균 교수 바이러스 흡착 기전 학술 백서</p>
                  <p>• 원내 비치용 환자 상담 리플렛 원본</p>
                </div>
                <p className="text-[11px] text-amber-200/90 leading-normal">
                  * 원내 진료 및 학술 참고용 전문 리포트
                </p>
              </div>

              <div className="pt-4">
                <a
                  href="tel:010-5407-5708"
                  className="w-full py-2.5 px-3 bg-[#003828] hover:bg-emerald-800 text-emerald-100 hover:text-white text-xs font-semibold rounded-xl border border-emerald-700/60 transition flex items-center justify-center gap-1.5"
                >
                  <span>📞 학술자료 유선 요청</span>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default VetRestrictedSection;
