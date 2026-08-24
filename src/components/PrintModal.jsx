import { useTranslation } from 'react-i18next';
import { useModalBehavior, handleBackdropClick } from '../hooks/useModalBehavior';

const PrintModal = ({ isPrintModalOpen, setIsPrintModalOpen, printUrl }) => {
  const { t } = useTranslation();
  const panelRef = useModalBehavior(isPrintModalOpen, () => setIsPrintModalOpen(false));

  if (!isPrintModalOpen) return null;

  return (
    <div
      className="fixed inset-0 z-[60] flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm transition-opacity"
      role="dialog"
      aria-modal="true"
      aria-labelledby="print-modal-title"
      onClick={(e) => handleBackdropClick(e, () => setIsPrintModalOpen(false))}
    >
      <div ref={panelRef} tabIndex={-1} className={`bg-slate-100 rounded-3xl shadow-2xl w-full max-w-[1250px] max-h-[90vh] overflow-y-auto relative animate-in fade-in zoom-in duration-300 flex flex-col focus:outline-none`}>
        {/* Modal Header */}
        <div className="sticky top-0 bg-white border-b border-slate-200 p-4 md:p-6 flex justify-between items-center z-10 rounded-t-3xl shadow-sm">
          <h3 id="print-modal-title" className="text-xl md:text-2xl font-black text-[#00513b] flex items-center gap-2">
            {t('label.print_title')}
          </h3>
          <button onClick={() => setIsPrintModalOpen(false)} aria-label={t('common.close')} className="text-slate-400 hover:text-slate-600 bg-slate-100 hover:bg-slate-200 rounded-full p-2 transition-colors focus:outline-none">
            <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        {/* Modal Body / Image Content */}
        <div className={`flex-1 w-full overflow-auto bg-gray-900 rounded-b-3xl min-h-[500px]`}>
          <iframe 
            src={printUrl}
            className={`min-w-[1200px] w-full h-[600px] scale-100 border-none bg-white origin-top`}
            title="Print Preview"
          />
        </div>
      </div>
    </div>
  );
};

export default PrintModal;
