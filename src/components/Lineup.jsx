import { useTranslation, Trans } from 'react-i18next';
import { PRODUCTS, LINEUP_PRODUCTS, getProductDisplayName } from '../data/products';

const Lineup = ({ setIsLabelModalOpen, setActiveProduct }) => {
  const { t, i18n } = useTranslation();
  const isKoreanLang = (i18n.language || 'ko').toLowerCase().startsWith('ko');

  return (
    <section id="lineup" className="py-16 sm:py-24 md:py-28 bg-slate-50 border-y border-slate-200/80">
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
                  
                  {/* 가격 및 출시 상태 안내 */}
                  <div className="mt-3 pt-2.5 border-t border-slate-100 flex items-center justify-between">
                    <span className="text-[11px] text-slate-500 font-medium">{t('lineup.priceLabel', '공급가')}</span>
                    {product.price ? (
                      <span className="text-xs sm:text-sm font-black text-emerald-700 font-mono">
                        {product.price.toLocaleString()}{t('order.won', '원')} <span className="text-[9px] text-slate-400 font-normal">(VAT포함)</span>
                      </span>
                    ) : (
                      <span className="text-[10px] font-bold text-amber-700 bg-amber-50 px-2 py-0.5 rounded border border-amber-200">
                        {t('lineup.priceTBD', '출시 예정 (가격미책정)')}
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
                  <button
                    onClick={() => {
                      if (!product.isComingSoon) {
                        setActiveProduct(id);
                        setIsLabelModalOpen(true);
                      } else {
                        alert(t('lineup.comingSoonAlert', '출시 준비중인 제품입니다. (가격 미책정)'));
                      }
                    }}
                    className="w-full py-2.5 bg-emerald-700 hover:bg-emerald-800 text-white text-xs font-bold rounded-xl transition-all shadow-sm flex items-center justify-center gap-1.5 cursor-pointer active:scale-95"
                  >
                    <svg className="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1" /></svg>
                    {t('lineup.elabelBtn', 'E-Label 확인')}
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
};

export default Lineup;
