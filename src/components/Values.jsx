import { useTranslation } from 'react-i18next';
import { PRODUCTS } from '../data/products';

const Values = ({ activeProduct }) => {
  const { t } = useTranslation();

  return (
    <section id="values" className="py-16 sm:py-24 md:py-28 bg-white relative">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-10 sm:mb-14">
          <h2 className="text-3xl sm:text-4xl md:text-5xl font-black text-[#00513b] break-keep tracking-tight">
            {activeProduct === 'monsmecta' ? t('values.title') : (PRODUCTS[activeProduct]?.values?.title || '에스앤제이의 3대 가치 약속')}
          </h2>
          <div className="w-20 sm:w-24 h-1.5 bg-yellow-400 mx-auto mt-4 sm:mt-6 rounded-full"></div>
          <p className="text-slate-500 text-sm sm:text-base md:text-lg mt-4 sm:mt-6 font-medium max-w-2xl mx-auto leading-relaxed break-keep">{t('values.desc')}</p>
        </div>

        <div className="grid md:grid-cols-3 gap-6 sm:gap-8">
          <div className="bg-slate-50 p-6 sm:p-8 md:p-10 rounded-3xl border border-slate-100 shadow-lg hover:shadow-2xl hover:-translate-y-1 transition-all duration-300 group">
            <div className="w-14 h-14 sm:w-16 sm:h-16 bg-[#00513b] text-white rounded-2xl flex items-center justify-center mb-6 text-2xl sm:text-3xl shadow-md group-hover:scale-110 transition-transform">🔒</div>
            <h4 className="text-lg sm:text-xl font-black text-slate-900 mb-3 sm:mb-4 break-keep">{t('values.online')}</h4>
            <p className="text-slate-600 text-sm sm:text-base leading-relaxed break-keep">
              {t('values.online_desc')}
            </p>
          </div>

          <div className="bg-slate-50 p-6 sm:p-8 md:p-10 rounded-3xl border border-slate-100 shadow-lg hover:shadow-2xl hover:-translate-y-1 transition-all duration-300 group">
            <div className="w-14 h-14 sm:w-16 sm:h-16 bg-gradient-to-br from-yellow-400 to-yellow-500 text-white rounded-2xl flex items-center justify-center mb-6 text-2xl sm:text-3xl shadow-md group-hover:scale-110 transition-transform">💸</div>
            <h4 className="text-lg sm:text-xl font-black text-slate-900 mb-3 sm:mb-4 break-keep">{t('values.price')}</h4>
            <p className="text-slate-600 text-sm sm:text-base leading-relaxed break-keep">
              {t('values.price_desc')}
            </p>
          </div>

          <div className="bg-slate-50 p-6 sm:p-8 md:p-10 rounded-3xl border border-slate-100 shadow-lg hover:shadow-2xl hover:-translate-y-1 transition-all duration-300 group">
            <div className="w-14 h-14 sm:w-16 sm:h-16 bg-[#00513b] text-white rounded-2xl flex items-center justify-center mb-6 text-2xl sm:text-3xl shadow-md group-hover:scale-110 transition-transform">🔬</div>
            <h4 className="text-lg sm:text-xl font-black text-slate-900 mb-3 sm:mb-4 break-keep">
              {activeProduct === 'monsmecta' ? t('values.formula') : (PRODUCTS[activeProduct]?.values?.formulaTitle || '독보적인 배합 비율')}
            </h4>
            <p className="text-slate-600 text-sm sm:text-base leading-relaxed break-keep">
              {activeProduct === 'monsmecta' ? t('values.formula_desc') : (PRODUCTS[activeProduct]?.values?.formulaDesc || '임상 현장에서 검증된 강력한 원료 배합으로 확실한 효과를 이끌어냅니다.')}
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Values;
