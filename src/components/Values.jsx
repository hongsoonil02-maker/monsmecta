import React from 'react';
import { useTranslation } from 'react-i18next';

const Values = () => {
  const { t } = useTranslation();

  return (
    <section id="values" className="py-10 md:py-20 bg-white relative">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-8">
          <h2 className="text-3xl md:text-4xl font-extrabold text-[#00513b] break-keep">{t('values.title')}</h2>
          <div className="w-24 h-1.5 bg-yellow-400 mx-auto mt-6 rounded-full"></div>
          <p className="text-slate-500 text-lg mt-6 font-medium">{t('values.desc')}</p>
        </div>

        <div className="grid md:grid-cols-3 gap-8">
          <div className="bg-slate-50 p-10 rounded-3xl border border-slate-100 shadow-lg hover:shadow-2xl hover:-translate-y-2 transition-all duration-300 group">
            <div className="w-16 h-16 bg-[#00513b] text-white rounded-2xl flex items-center justify-center mb-6 text-3xl shadow-md group-hover:scale-110 transition-transform">🔒</div>
            <h4 className="text-xl font-bold text-slate-800 mb-4">{t('values.online')}</h4>
            <p className="text-slate-600 leading-relaxed">
              {t('values.online_desc')}
            </p>
          </div>

          <div className="bg-slate-50 p-10 rounded-3xl border border-slate-100 shadow-lg hover:shadow-2xl hover:-translate-y-2 transition-all duration-300 group">
            <div className="w-16 h-16 bg-gradient-to-br from-yellow-400 to-yellow-500 text-white rounded-2xl flex items-center justify-center mb-6 text-3xl shadow-md group-hover:scale-110 transition-transform">💸</div>
            <h4 className="text-xl font-bold text-slate-800 mb-4">{t('values.price')}</h4>
            <p className="text-slate-600 leading-relaxed">
              {t('values.price_desc')}
            </p>
          </div>

          <div className="bg-slate-50 p-10 rounded-3xl border border-slate-100 shadow-lg hover:shadow-2xl hover:-translate-y-2 transition-all duration-300 group">
            <div className="w-16 h-16 bg-slate-800 text-white rounded-2xl flex items-center justify-center mb-6 text-3xl shadow-md group-hover:scale-110 transition-transform">🔬</div>
            <h4 className="text-xl font-bold text-slate-800 mb-4">{t('values.formula')}</h4>
            <p className="text-slate-600 leading-relaxed">
              {t('values.formula_desc')}
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Values;
