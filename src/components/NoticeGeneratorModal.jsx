import React, { useState, useRef, useEffect } from 'react';
import { useTranslation } from 'react-i18next';

const NoticeGeneratorModal = ({ isOpen, onClose }) => {
  const { t } = useTranslation();
  const iframeRef = useRef(null);
  
  const [hospitalName, setHospitalName] = useState('');
  const [address, setAddress] = useState('');
  const [tel, setTel] = useState('');
  const [vetTel, setVetTel] = useState('');

  // Update iframe when inputs change
  useEffect(() => {
    if (iframeRef.current && iframeRef.current.contentWindow) {
      iframeRef.current.contentWindow.postMessage({
        type: 'UPDATE_POSTER',
        name: hospitalName,
        address,
        tel,
        vetTel
      }, '*');
    }
  }, [hospitalName, address, tel, vetTel]);

  const handlePrint = () => {
    if (iframeRef.current && iframeRef.current.contentWindow) {
      iframeRef.current.contentWindow.postMessage({ type: 'PRINT_POSTER' }, '*');
    }
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-[70] flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm transition-opacity">
      <div className="bg-slate-100 rounded-3xl shadow-2xl w-full max-w-6xl max-h-[95vh] overflow-hidden flex flex-col relative animate-in fade-in zoom-in duration-300">
        
        {/* Modal Header */}
        <div className="bg-white border-b border-slate-200 p-4 md:p-6 flex justify-between items-center shrink-0">
          <h3 className="text-xl md:text-2xl font-black text-[#00513b] flex items-center gap-2">
            동물병원 알림판 커스텀 출력
          </h3>
          <button onClick={onClose} className="text-slate-400 hover:text-slate-600 bg-slate-100 hover:bg-slate-200 rounded-full p-2 transition-colors focus:outline-none">
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
              <p className="text-slate-600 mb-4">병원명, 주소, 연락처를 입력하시면 알림판 하단에 자동으로 적용됩니다.</p>
              
              <div className="space-y-4" translate="no">
                <div>
                  <label className="block text-sm font-bold text-slate-700 mb-1">동물병원명</label>
                  <input 
                    type="text" 
                    value={hospitalName}
                    onChange={(e) => setHospitalName(e.target.value)}
                    placeholder="예) 에스앤제이 동물병원" 
                    className="w-full px-4 py-3 rounded-xl border border-slate-300 focus:ring-2 focus:ring-[#10B981] focus:border-[#10B981] transition-all bg-slate-50 focus:bg-white"
                  />
                </div>
                <div>
                  <label className="block text-sm font-bold text-slate-700 mb-1">병원주소(선택)</label>
                  <input 
                    type="text" 
                    value={address}
                    onChange={(e) => setAddress(e.target.value)}
                    placeholder="예) 경기도 용인시 처인구 ..." 
                    className="w-full px-4 py-3 rounded-xl border border-slate-300 focus:ring-2 focus:ring-[#10B981] focus:border-[#10B981] transition-all bg-slate-50 focus:bg-white"
                  />
                </div>
                <div>
                  <label className="block text-sm font-bold text-slate-700 mb-1">병원전화번호(선택)</label>
                  <input 
                    type="text" 
                    value={tel}
                    onChange={(e) => setTel(e.target.value)}
                    placeholder="예) 031-321-6562" 
                    className="w-full px-4 py-3 rounded-xl border border-slate-300 focus:ring-2 focus:ring-[#10B981] focus:border-[#10B981] transition-all bg-slate-50 focus:bg-white"
                  />
                </div>
                <div>
                  <label className="block text-sm font-bold text-slate-700 mb-1">원장님전화번호(선택)</label>
                  <input 
                    type="text" 
                    value={vetTel}
                    onChange={(e) => setVetTel(e.target.value)}
                    placeholder="예) 010-1234-5678" 
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
              A4 사이즈로 인쇄하기
            </button>
            <p className="text-xs text-slate-400 text-center mt-3">
              인쇄 창이 뜨면 <strong>'머리글 및 바닥글'</strong> 옵션을 해제해주세요.
            </p>
          </div>

          {/* Right: Iframe Preview */}
          <div className="w-full lg:w-2/3 bg-gray-200/50 p-4 md:p-8 flex justify-center items-center overflow-y-auto min-h-[500px]">
            <div className="w-full h-full max-w-[794px] max-h-[1123px] aspect-[1/1.414] bg-white shadow-2xl overflow-hidden border border-slate-300 mx-auto relative">
              <iframe 
                ref={iframeRef}
                src={`${import.meta.env.BASE_URL}notice_a4_winner_poster.html`}
                className="w-full h-full border-0 absolute top-0 left-0"
                title="Notice Board Preview"
              />
            </div>
          </div>
        </div>

      </div>
    </div>
  );
};

export default NoticeGeneratorModal;
