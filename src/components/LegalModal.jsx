import { useTranslation } from 'react-i18next';
import { useModalBehavior, handleBackdropClick } from '../hooks/useModalBehavior';

const LegalModal = ({ legalType, setLegalType }) => {
  const { t } = useTranslation();
  const panelRef = useModalBehavior(!!legalType, () => setLegalType(null));

  if (!legalType) return null;

  return (
    <div
      className="fixed inset-0 z-[100] flex items-center justify-center p-4 bg-slate-900/80 backdrop-blur-sm animate-fade-in"
      role="dialog"
      aria-modal="true"
      aria-labelledby="legal-modal-title"
      onClick={(e) => handleBackdropClick(e, () => setLegalType(null))}
    >
      <div ref={panelRef} tabIndex={-1} className="bg-white rounded-3xl max-w-xl w-full p-6 md:p-8 shadow-2xl border border-slate-100 relative overflow-hidden transform transition-all animate-scale-up focus:outline-none">
        {/* Header */}
        <div className="flex flex-col sm:flex-row items-center justify-between pb-4 border-b border-slate-200 mb-6 text-center sm:text-start relative">
          <h3 id="legal-modal-title" className="text-lg sm:text-xl font-black text-[#00513b] flex items-center justify-center sm:justify-start gap-2 pr-8 sm:pr-0">
            <span className="w-2.5 h-2.5 rounded-full bg-emerald-500 shrink-0"></span>
            <span>
              {legalType === 'privacy' && t('legal.privacyTitle')}
              {legalType === 'terms' && t('legal.termsTitle')}
              {legalType === 'business' && t('legal.businessTitle')}
            </span>
          </h3>
          <button
            onClick={() => setLegalType(null)}
            className="absolute top-0 right-0 sm:relative w-8 h-8 sm:w-9 sm:h-9 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-500 hover:text-slate-800 flex items-center justify-center transition-colors font-bold text-base sm:text-lg"
            aria-label={t('common.close')}
          >
            ✕
          </button>
        </div>

        {/* Content */}
        <div className="text-slate-600 text-sm md:text-base leading-relaxed space-y-4 max-h-[60vh] overflow-y-auto pr-2 custom-scrollbar">
          <p className="whitespace-pre-line font-medium">
            {legalType === 'privacy' && t('legal.privacyBody')}
            {legalType === 'terms' && t('legal.termsBody')}
            {legalType === 'business' && t('legal.businessBody')}
          </p>
        </div>

        {/* Footer */}
        <div className="mt-8 pt-4 border-t border-slate-100 flex justify-end">
          <button
            onClick={() => setLegalType(null)}
            className="bg-[#00513b] hover:bg-[#003d2b] text-white px-6 py-2.5 rounded-full text-sm font-bold shadow-md hover:shadow-lg transition-all"
          >
            {t('sampleModal.confirmBtn', '확인')}
          </button>
        </div>
      </div>
    </div>
  );
};

export default LegalModal;
