import { useTranslation } from 'react-i18next';
import { useModalBehavior, handleBackdropClick } from '../hooks/useModalBehavior';

const PrintModal = ({ isPrintModalOpen, setIsPrintModalOpen, printUrl }) => {
  const { t } = useTranslation();
  const panelRef = useModalBehavior(isPrintModalOpen, () => setIsPrintModalOpen(false));

  if (!isPrintModalOpen) return null;

  const handlePrint = () => {
    const iframe = document.getElementById('label-print-iframe');
    if (iframe && iframe.contentWindow) {
      try {
        iframe.contentWindow.focus();
        iframe.contentWindow.print();
        return;
      } catch {
        // fallback to opening in new window
      }
    }
    window.open(printUrl, '_blank');
  };

  return (
    <div
      className="fixed inset-0 z-[60] flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm transition-opacity"
      role="dialog"
      aria-modal="true"
      aria-labelledby="print-modal-title"
      onClick={(e) => handleBackdropClick(e, () => setIsPrintModalOpen(false))}
    >
      <div ref={panelRef} tabIndex={-1} className="bg-slate-900 border border-slate-700 rounded-3xl shadow-2xl w-full max-w-[1250px] max-h-[92vh] overflow-hidden relative animate-in fade-in zoom-in duration-300 flex flex-col focus:outline-none">
        
        {/* Modal Header */}
        <div className="bg-slate-900 border-b border-slate-800 p-4 md:px-6 md:py-4 flex flex-col sm:flex-row justify-between items-center z-10 rounded-t-3xl shadow-sm text-center sm:text-start gap-3">
          <div className="flex items-center gap-3">
            <span className="text-2xl">🖨️</span>
            <div>
              <h3 id="print-modal-title" className="text-base md:text-xl font-black text-white break-keep flex items-center gap-2">
                {t('label.print_title')}
                <span className="text-xs font-bold text-emerald-400 bg-emerald-950/80 border border-emerald-500/40 px-2 py-0.5 rounded-full">100ml 정품 규격 (110×75mm)</span>
              </h3>
              <p className="text-xs text-slate-400 font-medium">일반 A4 프린터(재단선/50mm 확인자 포함) 및 110×75mm 라벨 프린터 지원</p>
            </div>
          </div>

          <div className="flex items-center gap-2.5 w-full sm:w-auto justify-end">
            <button
              onClick={handlePrint}
              className="bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs sm:text-sm px-4 py-2.5 rounded-xl shadow-lg shadow-emerald-900/40 transition-all flex items-center gap-2 cursor-pointer active:scale-95"
            >
              <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z" />
              </svg>
              1:1 실제 크기 인쇄
            </button>

            <button
              onClick={() => window.open(printUrl, '_blank')}
              className="bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-600 font-semibold text-xs px-3 py-2.5 rounded-xl transition-all flex items-center gap-1.5 cursor-pointer"
              title="새 창에서 원본 열기"
            >
              <span>새 창</span>
              <svg className="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
              </svg>
            </button>

            <button
              onClick={() => setIsPrintModalOpen(false)}
              aria-label={t('common.close')}
              className="text-slate-400 hover:text-white bg-slate-800 hover:bg-slate-700 border border-slate-700 rounded-full p-2 transition-colors focus:outline-none cursor-pointer"
            >
              <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
        </div>

        {/* 1:1 Actual Scale Instruction Banner */}
        <div className="bg-emerald-950/40 border-b border-emerald-900/60 px-4 py-2.5 text-xs text-emerald-200 flex flex-col sm:flex-row items-center justify-between gap-1">
          <div className="flex items-center gap-2">
            <span className="font-black text-emerald-400">💡 1:1 실측 인쇄 안내:</span>
            <span>인쇄 창 설정에서 <strong>[배율: 100% (실제 크기)]</strong> 및 <strong>[여백: 없음]</strong>을 선택하시면 110mm × 75mm 실제 크기로 오차 없이 인쇄됩니다.</span>
          </div>
          <span className="text-[11px] text-emerald-400/80 bg-emerald-900/30 px-2 py-0.5 rounded border border-emerald-700/40">50mm 실측 확인 자 내장</span>
        </div>

        {/* Modal Body / Image Content */}
        <div className="flex-1 w-full overflow-auto bg-slate-950 rounded-b-3xl min-h-[550px]">
          <iframe 
            id="label-print-iframe"
            src={printUrl}
            className="w-full h-full min-h-[550px] border-none bg-slate-950"
            title="Print Preview"
          />
        </div>
      </div>
    </div>
  );
};

export default PrintModal;
