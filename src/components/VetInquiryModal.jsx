import React, { useState } from 'react';

const VetInquiryModal = ({ isOpen, onClose }) => {
  const [hospitalName, setHospitalName] = useState('');
  const [vetName, setVetName] = useState('');
  const [phone, setPhone] = useState('');
  const [memo, setMemo] = useState('');
  const [isSubmitted, setIsSubmitted] = useState(false);

  if (!isOpen) return null;

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!hospitalName || !phone) {
      alert('병원명과 연락처를 입력해 주세요.');
      return;
    }
    // 접수 완료 시뮬레이션
    setIsSubmitted(true);
  };

  return (
    <div className="fixed inset-0 z-[100] flex items-center justify-center bg-black/60 backdrop-blur-sm p-4 animate-in fade-in">
      <div className="bg-white rounded-2xl shadow-2xl max-w-lg w-full overflow-hidden border border-emerald-100 flex flex-col">
        {/* Header */}
        <div className="bg-gradient-to-r from-emerald-800 to-teal-900 px-6 py-5 text-white flex items-center justify-between">
          <div className="flex items-center gap-2.5">
            <span className="text-2xl">🏥</span>
            <div>
              <h3 className="font-extrabold text-lg sm:text-xl tracking-tight">동물병원 입점 및 납품 직통 상담</h3>
              <p className="text-xs text-emerald-200 mt-0.5">전국 동물병원 원장님을 위한 1:1 VIP 전담 상담 창구</p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="text-white/80 hover:text-white bg-white/10 hover:bg-white/20 p-1.5 rounded-full transition-colors cursor-pointer"
            aria-label="닫기"
          >
            <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        {/* Content */}
        <div className="p-6 overflow-y-auto max-h-[80vh] space-y-5">
          {/* VIP Notice Banner */}
          <div className="bg-amber-50 border border-amber-200/90 rounded-xl p-4 text-xs text-amber-900 leading-relaxed">
            <div className="font-extrabold flex items-center gap-1.5 text-amber-950 mb-1 text-sm">
              <span>📞</span>
              <span>동물병원 상담 및 계산서 발행 안내</span>
            </div>
            동물병원 맞춤 단가 및 계산서 관련은 에스앤제이 동물병원 원장과 직접 상의하시기 바랍니다.
          </div>

          {isSubmitted ? (
            <div className="text-center py-8 space-y-4">
              <div className="w-16 h-16 bg-emerald-100 text-emerald-700 rounded-full flex items-center justify-center mx-auto text-3xl">
                ✓
              </div>
              <h4 className="text-xl font-bold text-slate-900">상담 신청이 정상 접수되었습니다!</h4>
              <p className="text-sm text-slate-600 leading-relaxed max-w-sm mx-auto">
                남겨주신 <strong>{hospitalName}</strong> 담당자님께 대표 직통으로 신속히 연락드려 상세 공급가 및 초도 샘플 발송을 안내해 드리겠습니다.
              </p>
              <button
                onClick={() => { setIsSubmitted(false); onClose(); }}
                className="mt-4 px-6 py-2.5 bg-emerald-700 hover:bg-emerald-800 text-white rounded-xl font-bold text-sm transition-all"
              >
                확인
              </button>
            </div>
          ) : (
            <>
              {/* Direct Phone / Call Buttons */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                <a
                  href="tel:031-321-6562"
                  className="flex items-center justify-center gap-2 py-3.5 px-4 bg-emerald-700 hover:bg-emerald-800 text-white font-extrabold rounded-xl shadow-md text-sm transition-all group"
                >
                  <svg className="w-4 h-4 group-hover:scale-110 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                  </svg>
                  <span>유선 직통 전화걸기</span>
                </a>
                <div className="flex items-center justify-center gap-2 py-3.5 px-4 bg-slate-100 border border-slate-200 text-slate-800 font-bold rounded-xl text-xs">
                  <span>📞 031-321-6562</span>
                  <span className="text-[10px] text-slate-500">(에스앤제이)</span>
                </div>
              </div>

              <div className="relative flex py-2 items-center">
                <div className="flex-grow border-t border-slate-200"></div>
                <span className="flex-shrink mx-4 text-xs font-semibold text-slate-400">또는 간편 상담 요청 남기기</span>
                <div className="flex-grow border-t border-slate-200"></div>
              </div>

              {/* Inquiry Form */}
              <form onSubmit={handleSubmit} className="space-y-3">
                <div>
                  <label className="block text-xs font-bold text-slate-700 mb-1">동물병원 상호명 *</label>
                  <input
                    type="text"
                    required
                    value={hospitalName}
                    onChange={(e) => setHospitalName(e.target.value)}
                    placeholder="예) 하남사랑동물병원"
                    className="w-full px-3.5 py-2.5 bg-slate-50 border border-slate-300 rounded-xl text-sm focus:ring-2 focus:ring-emerald-600 focus:bg-white outline-none"
                  />
                </div>
                <div className="grid grid-cols-2 gap-3">
                  <div>
                    <label className="block text-xs font-bold text-slate-700 mb-1">원장님 성함</label>
                    <input
                      type="text"
                      value={vetName}
                      onChange={(e) => setVetName(e.target.value)}
                      placeholder="예) 김동준 원장"
                      className="w-full px-3.5 py-2.5 bg-slate-50 border border-slate-300 rounded-xl text-sm focus:ring-2 focus:ring-emerald-600 focus:bg-white outline-none"
                    />
                  </div>
                  <div>
                    <label className="block text-xs font-bold text-slate-700 mb-1">연락처 *</label>
                    <input
                      type="tel"
                      required
                      value={phone}
                      onChange={(e) => setPhone(e.target.value)}
                      placeholder="010-0000-0000"
                      className="w-full px-3.5 py-2.5 bg-slate-50 border border-slate-300 rounded-xl text-sm focus:ring-2 focus:ring-emerald-600 focus:bg-white outline-none"
                    />
                  </div>
                </div>
                <div>
                  <label className="block text-xs font-bold text-slate-700 mb-1">문의 사항 / 필요 라인업</label>
                  <textarea
                    rows={2}
                    value={memo}
                    onChange={(e) => setMemo(e.target.value)}
                    placeholder="초도 샘플 요청, 납품 최소 수량(MOQ), 결제 방식 등 자유롭게 기재해 주세요."
                    className="w-full px-3.5 py-2 bg-slate-50 border border-slate-300 rounded-xl text-sm focus:ring-2 focus:ring-emerald-600 focus:bg-white outline-none resize-none"
                  />
                </div>

                <button
                  type="submit"
                  className="w-full py-3 bg-gradient-to-r from-emerald-700 to-teal-800 hover:from-emerald-800 hover:to-teal-900 text-white font-extrabold rounded-xl shadow-md text-sm transition-all cursor-pointer mt-2"
                >
                  입점 상담 및 공급가 안내 요청하기 🚀
                </button>
              </form>
            </>
          )}
        </div>
      </div>
    </div>
  );
};

export default VetInquiryModal;

