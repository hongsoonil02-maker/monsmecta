import React from 'react';
import { useTranslation } from 'react-i18next';

const OrderForm = ({
  isOrderComplete,
  setIsOrderComplete,
  quantity,
  setQuantity,
  hospitalName,
  setHospitalName,
  bizNumber,
  setBizNumber,
  address,
  setAddress,
  isSubmitting,
  handleCheckout
}) => {
  const { t } = useTranslation();
  const pricePerBottle = 7700;

  return (
    <section id="order" className="py-10 md:py-20 bg-slate-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="bg-white rounded-3xl shadow-2xl overflow-hidden border border-slate-200 transform transition-all duration-500 hover:shadow-[0_20px_50px_rgba(0,81,59,0.1)]">
          <div className="bg-gradient-to-r from-[#00513b] to-[#003d2b] p-8 md:p-10 text-center relative overflow-hidden">
            <div className="absolute top-0 right-0 w-32 h-32 bg-white opacity-5 rounded-full blur-2xl transform translate-x-1/2 -translate-y-1/2"></div>
            <h2 className="text-3xl font-black text-white drop-shadow-md break-keep">{t('order.title')}</h2>
            <p className="text-emerald-100/80 font-medium mt-3">{t('order.desc')}</p>
          </div>

          {isOrderComplete ? (
            <div className="p-8 md:p-12 text-center space-y-6">
              <div className="w-20 h-20 bg-emerald-100 text-[#00513b] rounded-full flex items-center justify-center mx-auto mb-6">
                <svg className="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="3" d="M5 13l4 4L19 7"></path></svg>
              </div>
              <h3 className="text-2xl font-black text-slate-800 break-keep">주문 정보가 접수되었습니다!</h3>
              <p className="text-slate-600 font-medium break-keep">아래 계좌로 입금을 완료해 주시면 배송이 시작됩니다.</p>

              <div className="bg-slate-50 border border-slate-200 rounded-2xl p-6 my-8 inline-block text-left w-full max-w-md">
                <div className="flex justify-between items-center mb-3">
                  <span className="text-sm font-bold text-slate-500">입금 은행</span>
                  <strong className="text-slate-800">카카오뱅크</strong>
                </div>
                <div className="flex justify-between items-center mb-3">
                  <span className="text-sm font-bold text-slate-500">계좌 번호</span>
                  <strong className="text-xl font-black text-[#00513b]">3333-26-3248376</strong>
                </div>
                <div className="flex justify-between items-center mb-3">
                  <span className="text-sm font-bold text-slate-500">예금주</span>
                  <strong className="text-slate-800">홍순일</strong>
                </div>
                <div className="flex justify-between items-center pt-3 border-t border-slate-200">
                  <span className="text-sm font-bold text-slate-500">입금하실 금액</span>
                  <strong className="text-2xl font-black text-rose-600">{(quantity * pricePerBottle).toLocaleString()}원</strong>
                </div>
              </div>

              <p className="text-sm text-slate-500 break-keep">입금 확인 후, 입력해주신 사업자번호로 <span className="font-bold text-slate-700">전자세금계산서가 자동 발행</span>됩니다.<br />관련 문의는 우측 하단 챗봇을 이용해 주세요.</p>
            </div>
          ) : (
            <form onSubmit={handleCheckout} className="p-6 md:p-12 space-y-6">
              <div className="space-y-6">
                <h3 className="text-xl font-black text-slate-800 border-b-2 border-emerald-100 pb-3 flex items-center gap-2">
                  <span className="bg-emerald-100 text-[#00513b] w-8 h-8 rounded-full flex items-center justify-center text-sm">1</span>
                  {t('order.hospital_info')}
                </h3>
                <div className="grid md:grid-cols-2 gap-6">
                  <div>
                    <label className="block text-sm font-bold text-slate-700 mb-2">{t('order.hospital_name')} <span className="text-red-500">*</span></label>
                    <input
                      type="text"
                      value={hospitalName}
                      onChange={(e) => setHospitalName(e.target.value)}
                      className="w-full px-5 py-4 rounded-xl border border-slate-300 focus:ring-4 focus:ring-emerald-500/20 focus:border-[#00513b] outline-none bg-slate-50 transition-all font-medium"
                      placeholder={t('order.hospital_name_placeholder')}
                      required
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-bold text-slate-700 mb-2">{t('order.biz_number')} <span className="text-red-500">*</span></label>
                    <input
                      type="text"
                      value={bizNumber}
                      onChange={(e) => setBizNumber(e.target.value)}
                      className="w-full px-5 py-4 rounded-xl border border-slate-300 focus:ring-4 focus:ring-emerald-500/20 focus:border-[#00513b] outline-none bg-slate-50 transition-all font-medium tracking-wide"
                      placeholder={t('order.biz_number_placeholder')}
                      required
                      maxLength="12"
                    />
                  </div>
                </div>
                <div>
                  <label className="block text-sm font-bold text-slate-700 mb-2">{t('order.address')} <span className="text-red-500">*</span></label>
                  <input
                    type="text"
                    value={address}
                    onChange={(e) => setAddress(e.target.value)}
                    className="w-full px-5 py-4 rounded-xl border border-slate-300 focus:ring-4 focus:ring-emerald-500/20 focus:border-[#00513b] outline-none bg-slate-50 transition-all font-medium"
                    placeholder={t('order.address_placeholder')}
                    required
                  />
                </div>
              </div>

              <div className="space-y-6">
                <h3 className="text-xl font-black text-slate-800 border-b-2 border-emerald-100 pb-3 flex items-center gap-2">
                  <span className="bg-emerald-100 text-[#00513b] w-8 h-8 rounded-full flex items-center justify-center text-sm">2</span>
                  {t('order.quantity_select')}
                </h3>
                <div className="flex flex-col md:flex-row items-center justify-between bg-slate-50 p-8 rounded-2xl border border-slate-200 hover:border-emerald-200 transition-colors shadow-inner">
                  <div className="mb-6 md:mb-0 text-center md:text-left">
                    <div className="font-black text-2xl text-slate-800 tracking-tight">{t('clinical.chart_monsmecta')} <span className="text-lg font-bold text-slate-500">{t('order.unit')}</span></div>
                    <div className="text-sm font-medium text-slate-500 mt-2">{t('order.supply_price')} <span className="font-black text-xl text-[#00513b] ml-1">{pricePerBottle.toLocaleString()}원</span> <span className="text-xs">{t('order.vat_included')}</span></div>
                    <p className="text-xs text-[#00513b] mt-1 font-semibold">{t('order.min_order')}</p>
                  </div>

                  <div className="flex items-center bg-white border-2 border-slate-200 rounded-xl overflow-hidden shadow-sm">
                    <button type="button" onClick={() => setQuantity(Math.max(5, quantity - 1))} className="w-14 h-14 flex items-center justify-center bg-slate-50 text-slate-600 hover:bg-emerald-50 hover:text-[#00513b] text-2xl font-black transition-colors">-</button>
                    <div className="w-20 h-14 flex items-center justify-center font-black text-2xl text-slate-800 border-x-2 border-slate-200">{quantity}</div>
                    <button type="button" onClick={() => setQuantity(quantity + 1)} className="w-14 h-14 flex items-center justify-center bg-slate-50 text-slate-600 hover:bg-emerald-50 hover:text-[#00513b] text-2xl font-black transition-colors">+</button>
                  </div>
                </div>
              </div>

              <div className="bg-[#003d2b] p-8 md:p-10 rounded-2xl text-white shadow-2xl relative overflow-hidden">
                <div className="absolute -right-10 -top-10 w-40 h-40 bg-yellow-400 opacity-10 rounded-full blur-3xl"></div>
                <div className="flex flex-col md:flex-row justify-between items-center mb-8 gap-4 relative z-10">
                  <span className="text-xl font-bold text-slate-300">{t('order.total_price')}</span>
                  <span className="text-5xl font-black text-yellow-400 drop-shadow-lg tracking-tight">{(quantity * pricePerBottle).toLocaleString()}<span className="text-2xl ml-2 text-yellow-500">{t('order.won')}</span></span>
                </div>
                <button type="submit" disabled={isSubmitting} className="w-full bg-gradient-to-r from-yellow-400 to-yellow-500 text-slate-900 text-2xl font-black py-5 rounded-xl hover:from-yellow-300 hover:to-yellow-400 transition duration-300 shadow-[0_0_20px_rgba(250,204,21,0.3)] transform hover:-translate-y-1 flex justify-center items-center gap-3 disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:translate-y-0">
                  <span>{isSubmitting ? '처리 중...' : t('order.btn')}</span>
                  {!isSubmitting && <svg className="w-7 h-7 animate-bounce-x" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="3" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>}
                </button>
                <p className="text-center text-slate-400 text-sm mt-6 font-medium">{t('order.bank_info')}</p>
              </div>
            </form>
          )}
        </div>
      </div>
    </section >
  );
};

export default OrderForm;
