import React, { useState } from 'react';

export default function VetSampleModal({ isOpen, onClose }) {
  const [submitted, setSubmitted] = useState(false);
  const [form, setForm] = useState({
    hospitalName: '',
    vetName: '',
    phone: '',
    address: '',
    requestType: '무료 샘플 신청 (100g 2개)',
  });


  if (!isOpen) return null;

  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmitted(true);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm animate-fadeIn">
      <div className="bg-white rounded-2xl max-w-lg w-full p-6 shadow-2xl relative border border-blue-100">
        <button
          onClick={onClose}
          className="absolute top-4 right-4 text-gray-400 hover:text-gray-600 text-2xl font-bold w-8 h-8 flex items-center justify-center rounded-full hover:bg-gray-100 transition-colors"
        >
          &times;
        </button>

        <div className="flex items-center gap-3 mb-4">
          <span className="text-3xl">🩺</span>
          <div>
            <h3 className="text-xl font-extrabold text-blue-900">수의사 원장님 전용 샘플 & 처방권 문의</h3>
            <p className="text-xs text-gray-500">동물병원 독점 처방용 몬스멕타(MONSMECTA) 샘플 키트를 보내드립니다.</p>
          </div>
        </div>

        {submitted ? (
          <div className="py-8 text-center space-y-3">
            <div className="w-14 h-14 bg-emerald-100 text-emerald-600 rounded-full flex items-center justify-center mx-auto text-2xl font-bold">
              ✓
            </div>
            <h4 className="text-lg font-bold text-gray-900">신청이 완료되었습니다!</h4>
            <p className="text-xs text-gray-600 leading-relaxed max-w-xs mx-auto">
              담당 수의사 자문위원이 입력해주신 주소로 몬스멕타 샘플 및 임상 시험 리포트를 신속히 배송해 드리겠습니다.
            </p>
            <button
              onClick={() => {
                setSubmitted(false);
                onClose();
              }}
              className="mt-4 px-6 py-2 bg-blue-600 text-white font-bold text-sm rounded-xl hover:bg-blue-700 transition-colors"
            >
              확인
            </button>
          </div>
        ) : (
          <form onSubmit={handleSubmit} className="space-y-3 text-left">
            <div>
              <label className="block text-xs font-bold text-gray-700 mb-1">동물병원명 *</label>
              <input
                type="text"
                required
                placeholder="예: 에스앤제이 대동물병원"
                value={form.hospitalName}
                onChange={(e) => setForm({ ...form, hospitalName: e.target.value })}
                className="w-full px-3.5 py-2.5 border border-gray-300 rounded-xl text-sm focus:ring-2 focus:ring-blue-500 outline-none"
              />
            </div>

            <div className="grid grid-cols-2 gap-3">
              <div>
                <label className="block text-xs font-bold text-gray-700 mb-1">원장님 성함 *</label>
                <input
                  type="text"
                  required
                  placeholder="홍길동 원장"
                  value={form.vetName}
                  onChange={(e) => setForm({ ...form, vetName: e.target.value })}
                  className="w-full px-3.5 py-2.5 border border-gray-300 rounded-xl text-sm focus:ring-2 focus:ring-blue-500 outline-none"
                />
              </div>

              <div>
                <label className="block text-xs font-bold text-gray-700 mb-1">연락처 *</label>
                <input
                  type="tel"
                  required
                  placeholder="010-0000-0000"
                  value={form.phone}
                  onChange={(e) => setForm({ ...form, phone: e.target.value })}
                  className="w-full px-3.5 py-2.5 border border-gray-300 rounded-xl text-sm focus:ring-2 focus:ring-blue-500 outline-none"
                />
              </div>
            </div>

            <div>
              <label className="block text-xs font-bold text-gray-700 mb-1">샘플 배송 주소 *</label>
              <input
                type="text"
                required
                placeholder="동물병원 배송 주소 입력"
                value={form.address}
                onChange={(e) => setForm({ ...form, address: e.target.value })}
                className="w-full px-3.5 py-2.5 border border-gray-300 rounded-xl text-sm focus:ring-2 focus:ring-blue-500 outline-none"
              />
            </div>

            <div>
              <label className="block text-xs font-bold text-gray-700 mb-1">신청 구분</label>
              <select
                value={form.requestType}
                onChange={(e) => setForm({ ...form, requestType: e.target.value })}
                className="w-full px-3.5 py-2.5 border border-gray-300 rounded-xl text-sm focus:ring-2 focus:ring-blue-500 outline-none bg-white"
              >
                <option>무료 샘플 신청 (100g 2개)</option>

                <option>지역 독점 공급권 및 단가 문의</option>
                <option>임상 연구 데이터 요청</option>
              </select>
            </div>

            <button
              type="submit"
              className="w-full py-3.5 bg-blue-600 hover:bg-blue-700 text-white font-bold rounded-xl shadow-lg hover:shadow-blue-600/30 transition-all text-sm mt-2"
            >
              샘플 키트 무료 신청하기
            </button>
          </form>
        )}
      </div>
    </div>
  );
}
