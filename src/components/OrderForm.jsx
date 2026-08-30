import { useState } from 'react';
import { useTranslation } from 'react-i18next';
import { PRODUCTS, getProductDisplayName } from '../data/products';

const OrderForm = ({
  isOrderComplete,
  quantities,
  setQuantities,
  minQuantity = 1,
  hospitalName,
  onHospitalNameChange,
  vetName,
  setVetName,
  bizNumber,
  setBizNumber,
  bizCategory,
  setBizCategory,
  bizType,
  setBizType,
  email,
  setEmail,
  address,
  setAddress,
  isSubmitting,
  orderError,
  honeypot,
  setHoneypot,
  onResetOrder,
  handleCheckout
}) => {
  const { t, i18n } = useTranslation();
  const isKoreanLang = (i18n.language || 'ko').toLowerCase().startsWith('ko');
  const [selectedProduct, setSelectedProduct] = useState(Object.keys(PRODUCTS)[0]);

  const handleAddProduct = () => {
    const p = PRODUCTS[selectedProduct];
    if (!p || p.isComingSoon || !p.price) {
      alert(t('order.comingSoonCannotOrder', '해당 제품은 현재 출시 준비중(가격미책정)으로, 공식 출시 후 발주하실 수 있습니다.'));
      return;
    }
    if ((quantities[selectedProduct] || 0) === 0) {
      setQuantities(prev => ({ ...prev, [selectedProduct]: 1 }));
    }
  };

  const totalPrice = Object.entries(quantities).reduce((sum, [key, q]) => sum + (q * (PRODUCTS[key]?.price || 0)), 0);
  const totalQuantity = Object.values(quantities).reduce((sum, q) => sum + q, 0);

  return (
    <section id="order" className="py-16 sm:py-24 md:py-28 bg-slate-50 border-t border-slate-200/80">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="bg-white rounded-3xl shadow-xl overflow-hidden border border-slate-200/90 transform transition-all duration-500 hover:shadow-2xl">
          <div className="bg-gradient-to-r from-[#006247] via-[#00513b] to-[#004432] p-6 sm:p-8 md:p-10 text-center relative overflow-hidden border-b border-emerald-600/40">
            <div className="absolute top-0 right-0 w-40 h-40 bg-white/10 rounded-full blur-2xl transform translate-x-1/2 -translate-y-1/2 pointer-events-none"></div>
            <h2 className="text-2xl sm:text-3xl md:text-4xl font-black text-white drop-shadow-md break-keep">{t('order.title')}</h2>
            <p className="text-emerald-100 text-xs sm:text-sm md:text-base font-medium mt-3">{t('order.desc')}</p>
          </div>

          {isOrderComplete ? (
            <div className="p-8 md:p-12 text-center space-y-6">
              <div className="w-20 h-20 bg-emerald-100 text-[#00513b] rounded-full flex items-center justify-center mx-auto mb-6">
                <svg className="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="3" d="M5 13l4 4L19 7"></path></svg>
              </div>
              <h3 className="text-2xl font-black text-slate-800 break-keep">{t('order.success_title')}</h3>
              <p className="text-slate-600 font-medium break-keep">{t('order.success_desc')}</p>

              <div className="bg-slate-50 border border-slate-200 rounded-2xl p-6 my-8 inline-block text-left w-full max-w-md">
                <div className="flex justify-between items-center mb-3">
                  <span className="text-sm font-bold text-slate-500">{t('order.deposit_bank_label')}</span>
                  <strong className="text-slate-800">{t('order.deposit_bank_value')}</strong>
                </div>
                <div className="flex justify-between items-center mb-3">
                  <span className="text-sm font-bold text-slate-500">{t('order.deposit_account_label')}</span>
                  <strong className="text-xl font-black text-[#00513b]">{t('order.deposit_account_value')}</strong>
                </div>
                <div className="flex justify-between items-center mb-3">
                  <span className="text-sm font-bold text-slate-500">{t('order.deposit_holder_label')}</span>
                  <strong className="text-slate-800">{t('order.deposit_holder_value')}</strong>
                </div>
                <div className="flex justify-between items-center pt-3 border-t border-slate-200">
                  <span className="text-sm font-bold text-slate-500">{t('order.deposit_amount_label')}</span>
                  <strong className="text-2xl font-black text-rose-600">{totalPrice.toLocaleString()}{t('order.won')}</strong>
                </div>
              </div>

              <p className="text-sm text-slate-500 break-keep">{t('order.success_notice_prefix')}<span className="font-bold text-slate-700">{t('order.success_notice_highlight')}</span>{t('order.success_notice_suffix')}<br />{t('order.success_notice_help')}</p>
              <button
                type="button"
                onClick={onResetOrder}
                className="text-xs text-[#00513b] underline hover:text-[#003d2b]"
              >
                {t('order.resubmit')}
              </button>
            </div>
          ) : (
            <form onSubmit={handleCheckout} className="p-6 md:p-12 space-y-6">
              <div className="hidden" aria-hidden="true">
                <label>Website
                  <input type="text" name="website" value={honeypot} onChange={(e) => setHoneypot(e.target.value)} tabIndex={-1} autoComplete="off" />
                </label>
              </div>
              {orderError && (
                <div className="rounded-2xl border border-rose-200 bg-rose-50 px-5 py-4 text-sm font-medium text-rose-700">
                  {orderError}
                </div>
              )}

              <div className="space-y-6">
                <h3 className="text-xl font-black text-slate-800 border-b-2 border-emerald-100 pb-3 flex items-center gap-2">
                  <span className="bg-emerald-100 text-[#00513b] w-8 h-8 rounded-full flex items-center justify-center text-sm">1</span>
                  {t('order.hospital_info')}
                </h3>
                <div className="bg-emerald-50 text-[#00513b] px-4 py-3 rounded-xl text-sm font-medium flex items-start gap-2 border border-emerald-100">
                  <svg className="w-5 h-5 flex-shrink-0 mt-0.5 opacity-80" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                  <span className="leading-snug break-keep">
                    <strong>재발주</strong> 시에는 <strong>동물병원명과 주문수량만 입력</strong>하시면 됩니다.<br/>
                    <span className="opacity-80 text-xs">(동물병원명을 입력하시면 기존 정보가 자동으로 채워집니다.)</span>
                  </span>
                </div>
                <div className="grid md:grid-cols-2 gap-6 mb-6">
                  <div>
                    <label className="block text-sm font-bold text-slate-700 mb-2">{t('order.hospital_name')} <span className="text-red-500">*</span></label>
                    <input
                      type="text"
                      value={hospitalName}
                      onChange={(e) => onHospitalNameChange(e.target.value)}
                      className="w-full px-5 py-4 rounded-xl border border-slate-300 focus:ring-4 focus:ring-emerald-500/20 focus:border-[#00513b] outline-none bg-slate-50 transition-all font-medium"
                      placeholder={t('order.hospital_name_placeholder')}
                      required
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-bold text-slate-700 mb-2">{t('order.vet_name')} <span className="text-red-500">*</span></label>
                    <input
                      type="text"
                      value={vetName}
                      onChange={(e) => setVetName(e.target.value)}
                      className="w-full px-5 py-4 rounded-xl border border-slate-300 focus:ring-4 focus:ring-emerald-500/20 focus:border-[#00513b] outline-none bg-slate-50 transition-all font-medium"
                      placeholder={t('order.vet_name_placeholder')}
                      required
                    />
                  </div>
                </div>
                <div className="grid md:grid-cols-2 gap-6 mb-6">
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
                  <div>
                    <label className="block text-sm font-bold text-slate-700 mb-2">{t('order.email')} <span className="text-red-500">*</span></label>
                    <input
                      type="email"
                      value={email}
                      onChange={(e) => setEmail(e.target.value)}
                      className="w-full px-5 py-4 rounded-xl border border-slate-300 focus:ring-4 focus:ring-emerald-500/20 focus:border-[#00513b] outline-none bg-slate-50 transition-all font-medium"
                      placeholder={t('order.email_placeholder')}
                      required
                    />
                  </div>
                </div>
                <div className="grid md:grid-cols-2 gap-6 mb-6">
                  <div>
                    <label className="block text-sm font-bold text-slate-700 mb-2">{t('order.biz_category')} <span className="text-red-500">*</span></label>
                    <input
                      type="text"
                      value={bizCategory}
                      onChange={(e) => setBizCategory(e.target.value)}
                      className="w-full px-5 py-4 rounded-xl border border-slate-300 focus:ring-4 focus:ring-emerald-500/20 focus:border-[#00513b] outline-none bg-slate-50 transition-all font-medium"
                      placeholder={t('order.biz_category_placeholder')}
                      required
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-bold text-slate-700 mb-2">{t('order.biz_type')} <span className="text-red-500">*</span></label>
                    <input
                      type="text"
                      value={bizType}
                      onChange={(e) => setBizType(e.target.value)}
                      className="w-full px-5 py-4 rounded-xl border border-slate-300 focus:ring-4 focus:ring-emerald-500/20 focus:border-[#00513b] outline-none bg-slate-50 transition-all font-medium"
                      placeholder={t('order.biz_type_placeholder')}
                      required
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
                  {t('order.quantity_select', '발주 품목 및 수량 선택')}
                </h3>
                
                <div className="flex flex-col sm:flex-row gap-3 mb-6 bg-slate-100 p-4 rounded-xl border border-slate-200">
                  <select 
                    value={selectedProduct} 
                    onChange={(e) => setSelectedProduct(e.target.value)}
                    className="flex-1 px-4 py-3 rounded-xl border border-slate-300 focus:ring-4 focus:ring-emerald-500/20 focus:border-[#00513b] outline-none font-medium bg-white"
                  >
                    <optgroup label="✅ 즉시 발주 가능 품목">
                      {Object.values(PRODUCTS).filter(p => !p.isComingSoon && p.price).map(p => (
                        <option key={p.id} value={p.id}>
                          {getProductDisplayName(p, isKoreanLang)} ({p.volume}) - {p.price.toLocaleString()}원
                        </option>
                      ))}
                    </optgroup>
                    <optgroup label="⏳ 출시 예정 품목 (커밍순 / 가격미책정)">
                      {Object.values(PRODUCTS).filter(p => p.isComingSoon || !p.price).map(p => (
                        <option key={p.id} value={p.id} disabled>
                          {getProductDisplayName(p, isKoreanLang)} ({p.volume}) [출시 예정 / 가격미책정]
                        </option>
                      ))}
                    </optgroup>
                  </select>
                  <button
                    type="button"
                    onClick={handleAddProduct}
                    className="bg-slate-800 text-white px-6 py-3 rounded-xl font-bold hover:bg-slate-700 transition-colors shrink-0"
                  >
                    {t('order.addProduct', '추가하기')}
                  </button>
                </div>
                <p className="text-xs text-slate-500 font-medium -mt-2">
                  {t('order.minOrderNotice', { min: minQuantity, defaultValue: `* 최소 주문 수량: ${minQuantity}병` })}
                </p>

                <div className="space-y-4">
                  {totalQuantity === 0 && (
                    <div className="text-center py-8 bg-slate-50 rounded-2xl border border-dashed border-slate-300">
                      <p className="text-slate-500 font-medium">{t('order.emptyProducts', "위에서 발주할 품목을 선택 후 '추가하기'를 눌러주세요.")}</p>
                    </div>
                  )}

                  {Object.entries(quantities).map(([key, q]) => {
                    if (q === 0) return null;
                    const p = PRODUCTS[key];
                    if (!p) return null;
                    
                    return (
                      <div key={key} className={`flex flex-col md:flex-row items-center justify-between ${key === 'monsmecta' ? 'bg-slate-50 border-slate-200' : 'bg-emerald-50/30 border-emerald-200'} p-6 rounded-2xl border shadow-sm relative`}>
                        <button type="button" onClick={() => setQuantities(prev => ({ ...prev, [key]: 0 }))} className="absolute top-4 right-4 text-slate-400 hover:text-red-500 transition-colors">
                          <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" /></svg>
                        </button>
                        <div className="mb-4 md:mb-0 text-center md:text-left pr-8">
                          <div className="font-black text-xl text-slate-800 tracking-tight">
                            {getProductDisplayName(p, isKoreanLang)} 
                            <span className="text-sm font-bold text-slate-500 ml-1.5">{p.volume ? `(${p.volume} / 병)` : t('order.unit', '(병)')}</span>
                          </div>
                          <div className="text-sm font-medium text-slate-500 mt-1">
                            {t('order.supply_price')}{' '}
                            <span className={`font-bold ${key === 'monsmecta' ? 'text-[#00513b]' : 'text-emerald-700'} ml-1 font-mono text-base`}>
                              {p.price ? p.price.toLocaleString() : '0'}{t('order.won')}
                            </span>{' '}
                            <span className="text-[10px] text-slate-500">{t('order.vat_included')}</span>
                          </div>
                        </div>
                        <div className={`flex items-center bg-white border ${key === 'monsmecta' ? 'border-slate-200' : 'border-emerald-200'} rounded-xl overflow-hidden shadow-sm shrink-0`}>
                          <button type="button" onClick={() => setQuantities(prev => ({ ...prev, [key]: Math.max(1, prev[key] - 1) }))} className={`w-12 h-12 flex items-center justify-center ${key === 'monsmecta' ? 'bg-slate-50 text-slate-600 hover:bg-emerald-50 hover:text-[#00513b]' : 'bg-emerald-50 text-slate-600 hover:bg-emerald-100 hover:text-emerald-800'} text-xl font-black transition-colors`}>-</button>
                          <div className={`w-16 h-12 flex items-center justify-center font-black text-xl text-slate-800 border-x ${key === 'monsmecta' ? 'border-slate-200' : 'border-emerald-200'}`}>{q}</div>
                          <button type="button" onClick={() => setQuantities(prev => ({ ...prev, [key]: prev[key] + 1 }))} className={`w-12 h-12 flex items-center justify-center ${key === 'monsmecta' ? 'bg-slate-50 text-slate-600 hover:bg-emerald-50 hover:text-[#00513b]' : 'bg-emerald-50 text-slate-600 hover:bg-emerald-100 hover:text-emerald-800'} text-xl font-black transition-colors`}>+</button>
                        </div>
                      </div>
                    );
                  })}
                </div>
              </div>

              <div className="bg-gradient-to-br from-emerald-50/80 via-white to-emerald-50/60 p-6 sm:p-8 md:p-10 rounded-3xl text-slate-900 shadow-xl relative overflow-hidden border border-emerald-300/80">
                <div className="absolute -right-10 -top-10 w-40 h-40 bg-emerald-300 opacity-20 rounded-full blur-3xl"></div>
                <div className="flex flex-col md:flex-row justify-between items-center mb-6 sm:mb-8 gap-4 relative z-10">
                  <span className="text-lg sm:text-xl font-bold text-slate-700">{t('order.total_price')}</span>
                  <span className="text-4xl sm:text-5xl font-black text-emerald-900 drop-shadow-sm tracking-tight font-mono">{totalPrice.toLocaleString()}<span className="text-xl sm:text-2xl ml-2 text-emerald-700 font-bold">{t('order.won')}</span></span>
                </div>
                <button type="submit" disabled={isSubmitting} className="w-full bg-gradient-to-r from-amber-400 to-yellow-500 hover:from-amber-300 hover:to-yellow-400 text-slate-950 text-xl sm:text-2xl font-black py-4 sm:py-5 rounded-2xl transition duration-300 shadow-lg shadow-amber-500/20 transform hover:-translate-y-1 flex justify-center items-center gap-3 disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:translate-y-0 cursor-pointer">
                  <span>{isSubmitting ? t('order.submitting') : t('order.btn')}</span>
                  {!isSubmitting && <svg className="w-6 h-6 sm:w-7 sm:h-7 animate-bounce-x text-slate-950" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="3" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>}
                </button>
                <p className="text-center text-slate-600 text-xs sm:text-sm mt-5 sm:mt-6 font-medium">{t('order.bank_info')}</p>
              </div>
            </form>
          )}
        </div>
      </div>
    </section>
  );
};

export default OrderForm;
