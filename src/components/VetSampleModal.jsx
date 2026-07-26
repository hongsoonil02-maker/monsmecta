import React, { useState, useEffect } from 'react';
import { useTranslation } from 'react-i18next';

export default function VetSampleModal({ isOpen, onClose }) {
  const { t } = useTranslation();
  const [submitted, setSubmitted] = useState(false);
  const [form, setForm] = useState({
    hospitalName: '',
    vetName: '',
    phone: '',
    address: '',
    requestType: t('sampleModal.type1', '무료 샘플 신청 (100g 2개)'),
  });

  // ESC 키 닫기 이벤트 지원 (Accessibility)
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'Escape' && isOpen) {
        onClose();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmitted(true);
  };

  return (
    <div 
      className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm animate-fadeIn"
      role="dialog"
      aria-modal="true"
      aria-labelledby="modal-title"
    >
      <div className="bg-white rounded-2xl max-w-lg w-full p-6 shadow-2xl relative border border-blue-100">
        <button
          onClick={onClose}
          aria-label="Close modal"
          className="absolute top-4 right-4 text-gray-400 hover:text-gray-600 text-2xl font-bold w-8 h-8 flex items-center justify-center rounded-full hover:bg-gray-100 transition-colors focus:ring-2 focus:ring-blue-500 focus:outline-none"
        >
          &times;
        </button>

        <div className="flex items-center gap-3 mb-4">
          <span className="text-3xl">🩺</span>
          <div>
            <h3 id="modal-title" className="text-xl font-extrabold text-blue-900">
              {t('sampleModal.title', '수의사 원장님 전용 샘플 & 처방권 문의')}
            </h3>
            <p className="text-xs text-gray-500">
              {t('sampleModal.sub', '동물병원 독점 처방용 몬스멕타(MONSMECTA) 샘플 키트를 보내드립니다.')}
            </p>
          </div>
        </div>

        {submitted ? (
          <div className="py-8 text-center space-y-3" aria-live="polite">
            <div className="w-14 h-14 bg-emerald-100 text-emerald-600 rounded-full flex items-center justify-center mx-auto text-2xl font-bold">
              ✓
            </div>
            <h4 className="text-lg font-bold text-gray-900">
              {t('sampleModal.successTitle', '신청이 완료되었습니다!')}
            </h4>
            <p className="text-xs text-gray-600 leading-relaxed max-w-xs mx-auto">
              {t('sampleModal.successDesc', '담당 수의사 자문위원이 입력해주신 주소로 몬스멕타 샘플 및 임상 시험 리포트를 신속히 배송해 드리겠습니다.')}
            </p>
            <button
              onClick={() => {
                setSubmitted(false);
                onClose();
              }}
              className="mt-4 px-6 py-2 bg-blue-600 text-white font-bold text-sm rounded-xl hover:bg-blue-700 transition-colors focus:ring-2 focus:ring-blue-500"
            >
              {t('sampleModal.confirmBtn', '확인')}
            </button>
          </div>
        ) : (
          <form onSubmit={handleSubmit} className="space-y-3 text-left">
            <div>
              <label className="block text-xs font-bold text-gray-700 mb-1">
                {t('sampleModal.hospitalName', '동물병원명 *')}
              </label>
              <input
                type="text"
                required
                value={form.hospitalName}
                onChange={(e) => setForm({ ...form, hospitalName: e.target.value })}
                className="w-full px-3.5 py-2.5 border border-gray-300 rounded-xl text-sm focus:ring-2 focus:ring-blue-500 outline-none"
              />
            </div>

            <div className="grid grid-cols-2 gap-3">
              <div>
                <label className="block text-xs font-bold text-gray-700 mb-1">
                  {t('sampleModal.vetName', '원장님 성함 *')}
                </label>
                <input
                  type="text"
                  required
                  value={form.vetName}
                  onChange={(e) => setForm({ ...form, vetName: e.target.value })}
                  className="w-full px-3.5 py-2.5 border border-gray-300 rounded-xl text-sm focus:ring-2 focus:ring-blue-500 outline-none"
                />
              </div>

              <div>
                <label className="block text-xs font-bold text-gray-700 mb-1">
                  {t('sampleModal.phone', '연락처 *')}
                </label>
                <input
                  type="tel"
                  required
                  value={form.phone}
                  onChange={(e) => setForm({ ...form, phone: e.target.value })}
                  className="w-full px-3.5 py-2.5 border border-gray-300 rounded-xl text-sm focus:ring-2 focus:ring-blue-500 outline-none"
                />
              </div>
            </div>

            <div>
              <label className="block text-xs font-bold text-gray-700 mb-1">
                {t('sampleModal.address', '샘플 배송 주소 *')}
              </label>
              <input
                type="text"
                required
                value={form.address}
                onChange={(e) => setForm({ ...form, address: e.target.value })}
                className="w-full px-3.5 py-2.5 border border-gray-300 rounded-xl text-sm focus:ring-2 focus:ring-blue-500 outline-none"
              />
            </div>

            <div>
              <label className="block text-xs font-bold text-gray-700 mb-1">
                {t('sampleModal.category', '신청 구분')}
              </label>
              <select
                value={form.requestType}
                onChange={(e) => setForm({ ...form, requestType: e.target.value })}
                className="w-full px-3.5 py-2.5 border border-gray-300 rounded-xl text-sm focus:ring-2 focus:ring-blue-500 outline-none bg-white"
              >
                <option>{t('sampleModal.type1', '무료 샘플 신청 (100g 2개)')}</option>
                <option>{t('sampleModal.type2', '지역 독점 공급권 및 단가 문의')}</option>
                <option>{t('sampleModal.type3', '임상 연구 데이터 요청')}</option>
              </select>
            </div>

            <button
              type="submit"
              className="w-full py-3.5 bg-blue-600 hover:bg-blue-700 text-white font-bold rounded-xl shadow-lg hover:shadow-blue-600/30 transition-all text-sm mt-2 focus:ring-2 focus:ring-blue-500"
            >
              {t('sampleModal.submitBtn', '샘플 키트 무료 신청하기')}
            </button>
          </form>
        )}
      </div>
    </div>
  );
}
