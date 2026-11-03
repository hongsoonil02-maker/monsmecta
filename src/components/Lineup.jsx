import { useTranslation, Trans } from 'react-i18next';
import { PRODUCTS, LINEUP_PRODUCTS, getProductDisplayName } from '../data/products';

const Lineup = ({ setIsLabelModalOpen, setActiveProduct, onOpenSampleModal }) => {
  const { t, i18n } = useTranslation();
  const isKoreanLang = (i18n.language || 'ko').toLowerCase().startsWith('ko');

  return (
    <section id="lineup" className="py-10 sm:py-14 md:py-[68px] bg-slate-50 border-y border-slate-200/80">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-10 sm:mb-14 flex flex-col items-center">
          <div className="mb-4 inline-flex items-center gap-2 px-4 py-1.5 bg-amber-50 border border-amber-300/80 rounded-full text-amber-900 text-xs sm:text-sm font-bold shadow-sm">
            <span className="relative flex h-2.5 w-2.5">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-amber-400 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-2.5 w-2.5 bg-amber-500"></span>
            </span>
            {t('lineup.badge', '9월 초 10종 라인업 공식 런칭 예정')}
          </div>
          <h2 className="text-3xl sm:text-4xl md:text-5xl font-black text-slate-900 mb-4 tracking-tight">
            <Trans
              i18nKey="lineup.title"
              defaults="몬스멕타 <count>10종</count> 라인업"
              components={{ count: <span className="text-emerald-600" /> }}
            />
          </h2>
          <p className="text-slate-600 text-sm sm:text-base md:text-lg max-w-2xl mx-auto leading-relaxed break-keep">
            {t('lineup.subtitle', '반려동물의 증상과 상태에 맞춘 프리미엄 맞춤형 처방 솔루션')}
          </p>
        </div>

        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-3.5 sm:gap-5">
          {LINEUP_PRODUCTS.map((id) => {
            const product = PRODUCTS[id];
            return (
              <div key={id} className="bg-white border border-slate-200/90 rounded-2xl p-4 sm:p-5 flex flex-col hover:border-emerald-500 hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group shadow-sm">
                <div className="text-3xl sm:text-4xl mb-3 sm:mb-4 transform group-hover:scale-110 transition-transform origin-left">{product.icon}</div>
                <div className="mb-4 flex-1">
                  <div className="flex items-center justify-between gap-1 mb-1">
                    <h3 className="text-sm sm:text-base font-extrabold text-slate-900 group-hover:text-emerald-700 transition-colors">{getProductDisplayName(product, isKoreanLang)}</h3>
                    {product.volume && (
                      <span className="text-[10px] font-bold px-1.5 py-0.5 rounded bg-slate-100 text-slate-600 border border-slate-200 shrink-0">{product.volume}</span>
                    )}
                  </div>
                  <p className="text-[10px] text-slate-400 mb-2 font-mono uppercase tracking-wider">{product.name_en}</p>
                  <p className="text-xs text-slate-600 leading-relaxed break-keep">{t(`products.${product.id}.desc`, { defaultValue: product.desc })}</p>
                  
                  {/* 소비자 권장가격 표기 */}
                  <div className="mt-3 pt-2.5 border-t border-slate-100 flex items-center justify-between">
                    <span className="text-[11px] text-slate-500 font-semibold">{t('lineup.retailPriceLabel', '권장소비자가')}</span>
                    {product.retail_price ? (
                      <span className="text-sm font-black text-emerald-800 tracking-tight">
                        {product.retail_price.toLocaleString()}원
                      </span>
                    ) : (
                      <span className="inline-flex items-center gap-1 text-[11px] font-bold text-slate-500 bg-slate-100 px-2 py-0.5 rounded-md border border-slate-200 select-none">
                        <span>출시 예정</span>
                      </span>
                    )}
                  </div>
                </div>
                <div className="space-y-2 mt-auto">
                  {product.isComingSoon ? (
                    <div className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-slate-100 text-slate-600 text-[10px] font-bold border border-slate-200">
                      <span className="w-1.5 h-1.5 rounded-full bg-amber-500 animate-pulse"></span>
                      {t('lineup.comingSoon', '커밍순 (출시예정)')}
                    </div>
                  ) : (
                    <div className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-emerald-50 text-emerald-700 text-[10px] font-bold border border-emerald-200">
                      <span className="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
                      {t('lineup.available', '공식 처방 가능')}
                    </div>
                  )}
                  {product.isComingSoon ? (
                    <button
                      onClick={() => onOpenSampleModal && onOpenSampleModal()}
                      className="w-full py-2.5 bg-amber-500 hover:bg-amber-600 text-slate-900 text-xs font-bold rounded-xl transition-all shadow-sm flex items-center justify-center gap-1.5 cursor-pointer active:scale-95"
                    >
                      <svg className="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" /></svg>
                      {t('lineup.notifyBtn', '출시 알림·샘플 신청')}
                    </button>
                  ) : (
                    <button
                      onClick={() => {
                        setActiveProduct(id);
                        setIsLabelModalOpen(true);
                      }}
                      className="w-full py-2.5 bg-emerald-700 hover:bg-emerald-800 text-white text-xs font-bold rounded-xl transition-all shadow-sm flex items-center justify-center gap-1.5 cursor-pointer active:scale-95"
                    >
                      <svg className="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1" /></svg>
                      {t('lineup.elabelBtn', 'E-Label 확인')}
                    </button>
                  )}
                </div>
              </div>
            );
          })}
        </div>

        {/* B2B 병원 직통 안내 배너 */}
        <div className="mt-10 bg-emerald-900/90 text-white rounded-2xl p-4 sm:p-5 flex flex-col sm:flex-row items-center justify-between gap-3 shadow-lg border border-emerald-700/60">
          <div className="flex items-center gap-3 text-center sm:text-left">
            <span className="text-2xl sm:text-3xl">🏥</span>
            <div>
              <p className="font-extrabold text-sm sm:text-base">동물병원 원장님이신가요? (입점 및 대량 납품 1:1 직통 상담)</p>
              <p className="text-xs text-emerald-200 mt-0.5">동물병원 맞춤 단가 및 계산서 관련은 에스앤제이 동물병원 원장과 직접 상의하시기 바랍니다.</p>
            </div>
          </div>
          <button
            onClick={() => onOpenSampleModal && onOpenSampleModal()}
            className="px-5 py-2.5 bg-amber-400 hover:bg-amber-300 text-slate-950 font-black text-xs sm:text-sm rounded-xl shadow-md transition-all shrink-0 cursor-pointer"
          >
            병원 직통 상담 신청 ↗
          </button>
        </div>

      </div>
    </section>
  );
};

export default Lineup;
