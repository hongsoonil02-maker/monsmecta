import { useTranslation, Trans } from 'react-i18next';
import { PRODUCTS, LINEUP_PRODUCTS, getProductDisplayName } from '../data/products';

const Lineup = ({ setIsLabelModalOpen, setActiveProduct }) => {
  const { t, i18n } = useTranslation();
  const isKoreanLang = (i18n.language || 'ko').toLowerCase().startsWith('ko');

  return (
    <section className="session-section bg-gradient-to-br from-[#00513b] via-[#004230] to-[#00281d] text-white py-16 md:py-24">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12 flex flex-col items-center">
          <div className="mb-4 inline-flex items-center gap-2 px-4 py-1.5 bg-yellow-400/20 border border-yellow-400/50 rounded-full text-yellow-300 text-sm font-bold shadow-[0_0_15px_rgba(250,204,21,0.2)]">
            <span className="relative flex h-2.5 w-2.5">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-yellow-400 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-2.5 w-2.5 bg-yellow-500"></span>
            </span>
            {t('lineup.badge', '9월 초 10종 라인업 공식 런칭 예정')}
          </div>
          <h2 className="text-3xl md:text-4xl font-extrabold text-white mb-4">
            <Trans
              i18nKey="lineup.title"
              defaults="몬스멕타 <count>10종</count> 라인업"
              components={{ count: <span className="text-emerald-400" /> }}
            />
          </h2>
          <p className="text-slate-400 text-sm md:text-base">
            {t('lineup.subtitle', '반려동물의 증상과 상태에 맞춘 프리미엄 맞춤형 처방 솔루션')}
          </p>
        </div>

        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4">
          {LINEUP_PRODUCTS.map((id) => {
            const product = PRODUCTS[id];
            return (
              <div key={id} className="bg-[#003627] border border-[#00513b] rounded-2xl p-5 flex flex-col hover:border-[#007555] hover:shadow-[0_0_15px_rgba(16,185,129,0.15)] transition-all group">
                <div className="text-3xl mb-4 transform group-hover:scale-110 transition-transform origin-left">{product.icon}</div>
                <div className="mb-4 flex-1">
                  <div className="flex items-center justify-between gap-1 mb-1">
                    <h3 className={`text-base font-bold ${product.text}`}>{getProductDisplayName(product, isKoreanLang)}</h3>
                    {product.volume && (
                      <span className="text-[10px] font-bold px-1.5 py-0.5 rounded bg-black/40 text-slate-300 border border-white/10 shrink-0">{product.volume}</span>
                    )}
                  </div>
                  <p className="text-[10px] text-slate-500 mb-2 font-mono uppercase tracking-wider">{product.name_en}</p>
                  <p className="text-xs text-slate-400 leading-snug break-keep">{t(`products.${product.id}.desc`, { defaultValue: product.desc })}</p>
                  
                  {/* 가격 및 출시 상태 안내 */}
                  <div className="mt-3 pt-2.5 border-t border-[#00513b]/60 flex items-center justify-between">
                    <span className="text-[11px] text-emerald-300/80 font-medium">{t('lineup.priceLabel', '공급가')}</span>
                    {product.price ? (
                      <span className="text-xs font-black text-yellow-400 font-mono">
                        {product.price.toLocaleString()}{t('order.won', '원')} <span className="text-[9px] text-slate-400 font-normal">(VAT포함)</span>
                      </span>
                    ) : (
                      <span className="text-[10px] font-bold text-amber-300/90 bg-amber-950/40 px-2 py-0.5 rounded border border-amber-800/40">
                        {t('lineup.priceTBD', '출시 예정 (가격미책정)')}
                      </span>
                    )}
                  </div>
                </div>
                <div className="space-y-2 mt-auto">
                  {product.isComingSoon ? (
                    <div className="inline-flex items-center gap-1 px-2.5 py-1 rounded-full bg-slate-900/80 text-amber-300 text-[10px] font-bold border border-amber-600/30">
                      <span className="w-1.5 h-1.5 rounded-full bg-amber-400 animate-pulse"></span>
                      {t('lineup.comingSoon', '커밍순 (출시예정)')}
                    </div>
                  ) : (
                    <div className="inline-flex items-center gap-1 px-2.5 py-1 rounded-full bg-emerald-950 text-emerald-300 text-[10px] font-bold border border-emerald-700/50">
                      <span className="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
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
                    className="w-full py-2 bg-[#004a36] hover:bg-[#005c43] text-emerald-50 text-xs font-bold rounded-lg transition-colors flex items-center justify-center gap-1 border border-[#006045]"
                  >
                    <svg className="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1" /></svg>
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
