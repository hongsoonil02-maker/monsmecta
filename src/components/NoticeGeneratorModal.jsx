import { useState, useRef, useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import { useModalBehavior, handleBackdropClick } from '../hooks/useModalBehavior';

const NoticeGeneratorModal = ({ isOpen, onClose }) => {
  const { t } = useTranslation();
  const iframeRef = useRef(null);
  const panelRef = useModalBehavior(isOpen, onClose);
  
  const [hospitalName, setHospitalName] = useState('');
  const [address, setAddress] = useState('');
  const [tel, setTel] = useState('');
  const [vetTel, setVetTel] = useState('');
  const [price, setPrice] = useState('');
  const [activeTab, setActiveTab] = useState('form'); // 'form' | 'preview' for mobile

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

  // Construct URL with query parameters for new window & autoprint
  const getPosterUrl = (autoprint = false) => {
    const params = new URLSearchParams();
    if (hospitalName) params.set('name', hospitalName);
    if (address) params.set('address', address);
    if (tel) params.set('tel', tel);
    if (vetTel) params.set('vetTel', vetTel);
    if (price) params.set('price', price);
    if (autoprint) params.set('autoprint', '1');
    return `${import.meta.env.BASE_URL}notice_a4_winner_poster.html?${params.toString()}`;
  };

  const handlePrint = () => {
    const isMobileDevice = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) || window.innerWidth < 1024;
    
    if (isMobileDevice) {
      // 모바일 환경: iframe 내부 window.print() 차단 우회를 위해 최상위 새 창에서 autoprint로 직접 AirPrint/Wi-Fi 인쇄 다이얼로그 호출
      const printUrl = getPosterUrl(true);
      window.open(printUrl, '_blank');
    } else {
      // PC 환경: iframe 내부 postMessage 트리거 시도
      if (iframeRef.current && iframeRef.current.contentWindow) {
        try {
          iframeRef.current.contentWindow.postMessage({ type: 'PRINT_POSTER' }, '*');
        } catch {
          window.open(getPosterUrl(true), '_blank');
        }
      } else {
        window.open(getPosterUrl(true), '_blank');
      }
    }
  };

  const handleOpenDirect = () => {
    window.open(getPosterUrl(false), '_blank');
  };

  if (!isOpen) return null;

  return (
    <div
      className="fixed inset-0 z-[70] flex items-center justify-center p-2 sm:p-4 bg-black/80 backdrop-blur-sm transition-opacity"
      role="dialog"
      aria-modal="true"
      aria-labelledby="notice-modal-title"
      onClick={(e) => handleBackdropClick(e, onClose)}
    >
      <div ref={panelRef} tabIndex={-1} className="bg-slate-100 rounded-2xl sm:rounded-3xl shadow-2xl w-full max-w-6xl max-h-[96vh] overflow-hidden flex flex-col relative animate-in fade-in zoom-in duration-300 focus:outline-none">
        
        {/* Modal Header */}
        <div className="bg-white border-b border-slate-200 p-4 md:p-5 flex justify-between items-center shrink-0">
          <div>
            <h3 id="notice-modal-title" className="text-base sm:text-xl md:text-2xl font-black text-[#00513b] flex items-start gap-2 text-start">
              <span className="text-lg md:text-2xl shrink-0 select-none mt-0.5">🖨️</span>
              <span className="break-keep flex-1">{t('notice.title', '동물병원 알림판 커스텀 출력')}</span>
            </h3>
            <p className="text-xs text-slate-500 hidden sm:block mt-1">{t('notice.desc', '병원명, 주소, 연락처를 입력하시면 알림판 하단에 자동으로 적용됩니다.')}</p>
          </div>
          <button onClick={onClose} aria-label={t('common.close', '닫기')} className="text-slate-400 hover:text-slate-600 bg-slate-100 hover:bg-slate-200 rounded-full p-2 transition-colors focus:outline-none">
            <svg className="w-5 h-5 md:w-6 md:h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        {/* Mobile Tabs: Only on small screens */}
        <div className="lg:hidden flex border-b border-slate-200 bg-white shrink-0">
          <button
            type="button"
            onClick={() => setActiveTab('form')}
            className={`flex-1 py-3 text-sm font-bold text-center border-b-2 transition-all flex items-center justify-center gap-1.5 ${
              activeTab === 'form'
                ? 'border-[#00513b] text-[#00513b] bg-emerald-50/50'
                : 'border-transparent text-slate-500 hover:text-slate-700'
            }`}
          >
            <span>✏️</span> {t('notice.tabForm', '정보 입력')}
          </button>
          <button
            type="button"
            onClick={() => setActiveTab('preview')}
            className={`flex-1 py-3 text-sm font-bold text-center border-b-2 transition-all flex items-center justify-center gap-1.5 ${
              activeTab === 'preview'
                ? 'border-[#00513b] text-[#00513b] bg-emerald-50/50'
                : 'border-transparent text-slate-500 hover:text-slate-700'
            }`}
          >
            <span>👁️</span> {t('notice.tabPreview', '알림판 미리보기')}
          </button>
        </div>

        {/* Modal Body */}
        <div className="flex flex-col lg:flex-row flex-1 overflow-hidden">
          {/* Left: Input Form (Always on lg, conditionally on mobile) */}
          <div className={`${activeTab === 'form' ? 'flex' : 'hidden'} lg:flex flex-col w-full lg:w-1/3 bg-white p-5 md:p-6 overflow-y-auto border-r border-slate-200 shrink-0`}>
            <div className="mb-5 flex-1">
              <div className="space-y-3.5" translate="no">
                <div>
                  <label className="block text-xs font-bold text-slate-700 mb-1">{t('notice.hospitalName', '동물병원명')}</label>
                  <input 
                    type="text" 
                    value={hospitalName}
                    onChange={(e) => setHospitalName(e.target.value)}
                    placeholder={t('notice.hospitalNamePlaceholder', '예) 에스앤제이 동물병원')} 
                    className="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 focus:ring-2 focus:ring-[#10B981] focus:border-[#10B981] transition-all bg-slate-50 focus:bg-white text-sm"
                  />
                </div>
                <div>
                  <label className="block text-xs font-bold text-slate-700 mb-1">{t('notice.hospitalAddress', '병원주소(선택)')}</label>
                  <input 
                    type="text" 
                    value={address}
                    onChange={(e) => setAddress(e.target.value)}
                    placeholder={t('notice.hospitalAddressPlaceholder', '예) 경기도 용인시 처인구 포곡읍 ...')} 
                    className="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 focus:ring-2 focus:ring-[#10B981] focus:border-[#10B981] transition-all bg-slate-50 focus:bg-white text-sm"
                  />
                </div>
                <div>
                  <label className="block text-xs font-bold text-slate-700 mb-1">{t('notice.hospitalTel', '병원전화번호(선택)')}</label>
                  <input 
                    type="text" 
                    value={tel}
                    onChange={(e) => setTel(e.target.value)}
                    placeholder={t('notice.hospitalTelPlaceholder', '예) 031-321-6562')} 
                    className="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 focus:ring-2 focus:ring-[#10B981] focus:border-[#10B981] transition-all bg-slate-50 focus:bg-white text-sm"
                  />
                </div>
                <div>
                  <label className="block text-xs font-bold text-slate-700 mb-1">{t('notice.vetTel', '원장님전화번호(선택)')}</label>
                  <input 
                    type="text" 
                    value={vetTel}
                    onChange={(e) => setVetTel(e.target.value)}
                    placeholder={t('notice.vetTelPlaceholder', '예) 010-1234-5678')} 
                    className="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 focus:ring-2 focus:ring-[#10B981] focus:border-[#10B981] transition-all bg-slate-50 focus:bg-white text-sm"
                  />
                </div>
                <div>
                  <label className="block text-xs font-bold text-slate-700 mb-1">{t('notice.price', '판매가(선택)')}</label>
                  <input 
                    type="text" 
                    value={price}
                    onChange={(e) => setPrice(e.target.value)}
                    placeholder={t('notice.pricePlaceholder', '예) 18,000')} 
                    className="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 focus:ring-2 focus:ring-[#10B981] focus:border-[#10B981] transition-all bg-slate-50 focus:bg-white text-sm"
                  />
                </div>
              </div>
            </div>

            {/* Mobile quick view toggle button */}
            <button
              type="button"
              onClick={() => setActiveTab('preview')}
              className="lg:hidden w-full mb-3 py-2.5 bg-emerald-50 text-[#00513b] border border-emerald-300 rounded-xl font-bold text-xs flex items-center justify-center gap-1.5 hover:bg-emerald-100 transition-colors"
            >
              <span>👁️</span> 알림판 미리보기 확인하기
            </button>

            {/* Print Buttons */}
            <div className="space-y-2 pt-2 border-t border-slate-200">
              <button 
                onClick={handlePrint}
                className="w-full py-3.5 bg-[#00513b] hover:bg-[#003b2b] text-white rounded-xl font-bold text-base shadow-lg hover:shadow-xl transition-all transform hover:-translate-y-0.5 flex items-center justify-center gap-2"
              >
                <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z" />
                </svg>
                {t('notice.printBtn', 'A4 알림판 인쇄하기')}
              </button>

              <button
                type="button"
                onClick={handleOpenDirect}
                className="w-full py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-xl font-semibold text-xs transition-colors flex items-center justify-center gap-1.5 border border-slate-300"
              >
                <svg className="w-3.5 h-3.5 text-slate-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                </svg>
                {t('notice.openNewTab', '새 창에서 원본 보기 & Wi-Fi 출력')}
              </button>

              <p className="text-[11px] text-slate-400 text-center leading-snug">
                {t('notice.printHelp', "모바일 Wi-Fi 프린터 및 PC 인쇄를 모두 지원합니다. 인쇄 창에서 '머리글/바닥글'을 해제하시면 깔끔합니다.")}
              </p>
            </div>
          </div>

          {/* Right: Iframe Preview (Always on lg, conditionally on mobile) */}
          <div className={`${activeTab === 'preview' ? 'flex' : 'hidden'} lg:flex flex-col flex-1 bg-slate-200/80 p-3 sm:p-6 items-center justify-start overflow-y-auto relative`}>
            {/* Mobile preview action bar */}
            <div className="lg:hidden w-full max-w-[400px] flex items-center justify-between gap-2 mb-3 bg-white p-2.5 rounded-xl border border-slate-300 shadow-sm shrink-0">
              <button
                type="button"
                onClick={() => setActiveTab('form')}
                className="text-xs font-bold text-slate-600 px-3 py-1.5 rounded-lg bg-slate-100 hover:bg-slate-200 transition-colors"
              >
                ← 정보 수정
              </button>
              <button
                type="button"
                onClick={handlePrint}
                className="text-xs font-bold text-white px-4 py-1.5 rounded-lg bg-[#00513b] hover:bg-[#003b2b] shadow transition-colors flex items-center gap-1"
              >
                <span>🖨️</span> 바로 인쇄하기
              </button>
            </div>

            {/* Poster Canvas container */}
            <div className="w-full flex justify-center items-start my-auto py-2">
              <div className="origin-top transform scale-[0.38] xs:scale-[0.45] sm:scale-[0.55] md:scale-[0.65] lg:scale-[0.5] xl:scale-[0.62] 2xl:scale-[0.7] transition-transform duration-200">
                <div className="w-[794px] h-[1123px] bg-white shadow-2xl overflow-hidden border border-slate-300 relative rounded-sm">
                  <iframe 
                    ref={iframeRef}
                    src={`${import.meta.env.BASE_URL}notice_a4_winner_poster.html`}
                    className="w-[794px] h-[1123px] border-0 absolute top-0 left-0"
                    title={t('notice.previewTitle', '알림판 미리보기')}
                  />
                </div>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  );
};

export default NoticeGeneratorModal;
