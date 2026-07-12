import React from 'react';
import { useTranslation } from 'react-i18next';

const PrintModal = ({ isPrintModalOpen, setIsPrintModalOpen }) => {
  const { t } = useTranslation();

  if (!isPrintModalOpen) return null;

  return (
    <div className="fixed inset-0 z-[60] flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm transition-opacity">
      <div className="bg-slate-100 rounded-3xl shadow-2xl w-full max-w-4xl max-h-[90vh] overflow-y-auto relative animate-in fade-in zoom-in duration-300 flex flex-col">
        {/* Modal Header */}
        <div className="sticky top-0 bg-white border-b border-slate-200 p-4 md:p-6 flex justify-between items-center z-10 rounded-t-3xl shadow-sm">
          <h3 className="text-xl md:text-2xl font-black text-[#00513b] flex items-center gap-2">
            {t('label.print_title')}
          </h3>
          <button onClick={() => setIsPrintModalOpen(false)} className="text-slate-400 hover:text-slate-600 bg-slate-100 hover:bg-slate-200 rounded-full p-2 transition-colors focus:outline-none">
            <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        {/* Modal Body / Image Content */}
        <div className="p-4 md:p-8 flex justify-center items-center bg-gray-200/50">
          <img src={`${import.meta.env.BASE_URL}assets/label_screenshot.png`} alt={`인쇄용 ${t('clinical.chart_monsmecta')} 라벨`} className="max-w-full h-auto rounded-xl shadow-lg border border-slate-300" />
        </div>
      </div>
    </div>
  );
};

export default PrintModal;
