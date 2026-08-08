import React from 'react';
import { PRODUCTS, LINEUP_PRODUCTS } from '../data/products';
import { useTranslation } from 'react-i18next';

const Lineup = ({ setIsLabelModalOpen, activeProduct, setActiveProduct }) => {
  const { t } = useTranslation();
  return (
    <section className="bg-[#002b1f] text-white py-16 md:py-24">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <h2 className="text-3xl md:text-4xl font-extrabold text-white mb-4">
            몬스멕타 <span className="text-emerald-400">10종</span> 라인업
          </h2>
          <p className="text-slate-400 text-sm md:text-base">
            반려동물의 증상과 상태에 맞춘 프리미엄 맞춤형 처방 솔루션
          </p>
        </div>

        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4">
          {LINEUP_PRODUCTS.map((id) => {
            const product = PRODUCTS[id];
            return (
              <div key={id} className="bg-[#003627] border border-[#00513b] rounded-2xl p-5 flex flex-col hover:border-[#007555] hover:shadow-[0_0_15px_rgba(16,185,129,0.15)] transition-all group">
                <div className="text-3xl mb-4 transform group-hover:scale-110 transition-transform origin-left">{product.icon}</div>
                <div className="mb-4 flex-1">
                  <h3 className={`text-base font-bold mb-1 ${product.text}`}>{product.name_ko}</h3>
                  <p className="text-[10px] text-slate-500 mb-2 font-mono uppercase tracking-wider">{product.name_en}</p>
                  <p className="text-xs text-slate-400 leading-snug break-keep">{product.desc}</p>
                </div>
                <div className="space-y-2 mt-auto">
                  {product.isComingSoon && (
                    <div className="inline-block px-2 py-1 rounded-full bg-emerald-950 text-emerald-300 text-[10px] font-bold border border-emerald-800">
                      출시 준비중
                    </div>
                  )}
                  <button 
                    onClick={() => {
                      if (!product.isComingSoon) {
                        setActiveProduct(id);
                        setIsLabelModalOpen(true);
                      } else {
                        alert('출시 준비중인 제품입니다.');
                      }
                    }}
                    className="w-full py-2 bg-[#004a36] hover:bg-[#005c43] text-emerald-50 text-xs font-bold rounded-lg transition-colors flex items-center justify-center gap-1 border border-[#006045]"
                  >
                    <svg className="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1" /></svg>
                    E-Label 확인
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
