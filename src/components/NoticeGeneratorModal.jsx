import { useState, useRef, useEffect } from 'react';
import { useTranslation } from 'react-i18next';

const NoticeGeneratorModal = ({ isOpen, onClose }) => {
  const { t } = useTranslation();
  const iframeRef = useRef(null);
  
  const [hospitalName, setHospitalName] = useState('');
  const [address, setAddress] = useState('');
  const [tel, setTel] = useState('');
  const [vetTel, setVetTel] = useState('');
  const [price, setPrice] = useState('');

  // Update iframe when inputs change
  useEffect(() => {
    if (iframeRef.current && iframeRef.current.contentWindow) {
      iframeRef.current.contentWindow.postMessage({
        type: 'UPDATE_POSTER',
        name: hospitalName,
        address,
        tel,
        vetTel,
        price
      }, '*');
    }
  }, [hospitalName, address, tel, vetTel, price]);

  const handlePrint = () => {
    if (iframeRef.current && iframeRef.current.contentWindow) {
      iframeRef.current.contentWindow.postMessage({ type: 'PRINT_POSTER' }, '*');
    }
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-[70] flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm transition-opacity" role="dialog" aria-modal="true" aria-labelledby="notice-modal-title">
      <div className="bg-slate-100 rounded-3xl shadow-2xl w-full max-w-6xl max-h-[95vh] overflow-hidden flex flex-col relative animate-in fade-in zoom-in duration-300">
        
        {/* Modal Header */}
        <div className="bg-white border-b border-slate-200 p-4 md:p-6 flex justify-between items-center shrink-0">
          <h3 id="notice-modal-title" className="text-xl md:text-2xl font-black text-[#00513b] flex items-center gap-2">
            {t('notice.title')}
          </h3>
          <button onClick={onClose} aria-label={t('common.close')} className="text-slate-400 hover:text-slate-600 bg-slate-100 hover:bg-slate-200 rounded-full p-2 transition-colors focus:outline-none">
            <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        {/* Modal Body */}
        <div className="flex flex-col lg:flex-row flex-1 overflow-hidden">
          {/* Left: Input Form */}
          <div className="w-full lg:w-1/3 bg-white p-6 overflow-y-auto border-r border-slate-200 shrink-0">
            <div className="mb-6">
              <p className="text-slate-600 mb-4">{t('notice.desc')}</p>
              
              <div className="space-y-4" translate="no">
                <div>
                  <label className="block text-sm font-bold text-slate-700 mb-1">{t('notice.hospitalName')}</label>
                  <input 
                    type="text" 
                    value={hospitalName}
                    onChange={(e) => setHospitalName(e.target.value)}
                    placeholder={t('notice.hospitalNamePlaceholder')} 
                    className="w-full px-4 py-3 rounded-xl border border-slate-300 focus:ring-2 focus:ring-[#10B981] focus:border-[#10B981] transition-all bg-slate-50 focus:bg-white"
                  />
                </div>
                <div>
                  <label className="block text-sm font-bold text-slate-700 mb-1">{t('notice.hospitalAddress')}</label>
                  <input 
                    type="text" 
                    value={address}
                    onChange={(e) => setAddress(e.target.value)}
                    placeholder={t('notice.hospitalAddressPlaceholder')} 
                    className="w-full px-4 py-3 rounded-xl border border-slate-300 focus:ring-2 focus:ring-[#10B981] focus:border-[#10B981] transition-all bg-slate-50 focus:bg-white"
                  />
                </div>
                <div>
                  <label className="block text-sm font-bold text-slate-700 mb-1">{t('notice.hospitalTel')}</label>
                  <input 
                    type="text" 
                    value={tel}
                    onChange={(e) => setTel(e.target.value)}
                    placeholder={t('notice.hospitalTelPlaceholder')} 
                    className="w-full px-4 py-3 rounded-xl border border-slate-300 focus:ring-2 focus:ring-[#10B981] focus:border-[#10B981] transition-all bg-slate-50 focus:bg-white"
                  />
                </div>
                <div>
                  <label className="block text-sm font-bold text-slate-700 mb-1">{t('notice.vetTel')}</label>
                  <input 
                    type="text" 
                    value={vetTel}
                    onChange={(e) => setVetTel(e.target.value)}
                    placeholder={t('notice.vetTelPlaceholder')} 
                    className="w-full px-4 py-3 rounded-xl border border-slate-300 focus:ring-2 focus:ring-[#10B981] focus:border-[#10B981] transition-all bg-slate-50 focus:bg-white"
                  />
                </div>
                <div>
                  <label className="block text-sm font-bold text-slate-700 mb-1">{t('notice.price', '판매가(선택)')}</label>
                  <input 
                    type="text" 
                    value={price}
                    onChange={(e) => setPrice(e.target.value)}
                    placeholder={t('notice.pricePlaceholder', '예) 18,000')} 
                    className="w-full px-4 py-3 rounded-xl border border-slate-300 focus:ring-2 focus:ring-[#10B981] focus:border-[#10B981] transition-all bg-slate-50 focus:bg-white"
                  />
                </div>
              </div>
            </div>

            <button 
              onClick={handlePrint}
              className="w-full py-4 bg-[#00513b] hover:bg-[#003b2b] text-white rounded-xl font-bold text-lg shadow-lg hover:shadow-xl transition-all transform hover:-translate-y-1 flex items-center justify-center gap-2"
            >
              <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z" />
              </svg>
              {t('notice.printBtn')}
            </button>
            <p className="text-xs text-slate-400 text-center mt-3">
              {t('notice.printHelp')}
            </p>
          </div>

          {/* Right: Iframe Preview */}
          <div className="w-full lg:w-2/3 bg-gray-200/50 p-4 md:p-8 flex justify-center items-center overflow-hidden min-h-[500px] relative">
            <div className="transform scale-[0.4] sm:scale-[0.5] md:scale-[0.6] lg:scale-[0.45] xl:scale-[0.6] origin-center">
              <div className="w-[794px] h-[1123px] bg-white shadow-2xl overflow-hidden border border-slate-300 relative">
                <iframe 
                  ref={iframeRef}
                  src={`${import.meta.env.BASE_URL}notice_a4_winner_poster.html`}
                  className="w-[794px] h-[1123px] border-0 absolute top-0 left-0"
                  title={t('notice.previewTitle')}
                />
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  );
};

export default NoticeGeneratorModal;
