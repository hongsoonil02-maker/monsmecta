import React from 'react';
import { useTranslation } from 'react-i18next';

const LabelModal = ({ isLabelModalOpen, setIsLabelModalOpen, setIsPrintModalOpen }) => {
  const { t } = useTranslation();

  if (!isLabelModalOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm transition-opacity">
      <div className="bg-white rounded-3xl shadow-2xl w-full max-w-4xl max-h-[90vh] overflow-y-auto relative animate-in fade-in zoom-in duration-300">
        {/* Modal Header */}
        <div className="sticky top-0 bg-gradient-to-r from-[#00513b] via-[#003d2b] to-[#00281d] text-white p-6 flex justify-between items-center z-10">
          <div>
            <p className="text-xs text-emerald-300 font-bold tracking-widest uppercase mb-1">E-Label Specification</p>
            <h3 className="text-2xl font-black">{t('clinical.chart_monsmecta')} 상세 스펙 및 라벨 정보</h3>
          </div>
          <button onClick={() => setIsLabelModalOpen(false)} className="text-emerald-100 hover:text-white bg-emerald-800/50 hover:bg-emerald-700/50 rounded-full p-2 transition-colors">
            <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        {/* Modal Body / E-Label Content */}
        <div className="p-8">
          <div className="flex flex-col md:flex-row gap-8">

            {/* 3D Bottle Image & Key Points */}
            <div className="md:w-1/3 flex flex-col items-center border-r border-slate-100 pr-0 md:pr-8">
              <div className="bg-slate-50 w-full rounded-2xl p-6 flex justify-center items-center mb-6 border border-slate-100">
                <img src={`${import.meta.env.BASE_URL}assets/bottle_mockup.png`} alt="Monsmecta Bottle" className="w-3/4 max-w-[200px] drop-shadow-xl hover:scale-105 transition-transform" />
              </div>
              <div className="w-full text-center">
                <h4 className="text-xl font-black text-[#00513b] mb-2">MONSMECTA</h4>
                <p className="text-sm font-bold text-amber-500 mb-4">{t('label.desc')}</p>
                <div className="space-y-2 text-left bg-emerald-50 p-4 rounded-xl">
                  <p className="text-xs font-bold text-emerald-800">{t('label.feed1')}</p>
                  <p className="text-xs font-bold text-emerald-800">{t('label.feed2')}</p>
                  <p className="text-xs font-bold text-emerald-800">{t('label.feed3')}</p>
                </div>
              </div>
            </div>

            {/* Detailed Specs */}
            <div className="md:w-2/3 space-y-6">
              <div>
                <h5 className="text-lg font-bold text-slate-800 border-b-2 border-amber-400 pb-2 mb-4 inline-block">{t('label.ingredients_title')}</h5>
                <ul className="space-y-3 text-sm text-slate-600">
                  <li><strong className="text-emerald-700">{t('label.ing1_title')}</strong> {t('label.ing1_desc')} <br /><span className="text-xs text-slate-400 pl-4">{t('label.ing1_note')}</span></li>
                  <li><strong className="text-emerald-700">{t('label.ing2_title')}</strong> {t('label.ing2_desc')}</li>
                  <li><strong className="text-emerald-700">{t('label.ing3_title')}</strong> {t('label.ing3_desc')}</li>
                  <li><strong className="text-emerald-700">{t('label.ing4_title')}</strong> {t('label.ing4_desc')}</li>
                  <li><strong className="text-emerald-700">{t('label.ing5_title')}</strong> {t('label.ing5_desc')}</li>
                </ul>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-sm bg-slate-50 p-5 rounded-2xl border border-slate-200">
                <div className="col-span-full border-b border-slate-200 pb-2 mb-2 flex justify-between items-end">
                  <span className="block text-xs font-bold text-slate-400 uppercase">{t('label.reg_no_title')}</span>
                  <strong className="text-slate-800">{t('label.reg_no')}</strong>
                </div>

                <div className="col-span-full">
                  <span className="block text-xs font-bold text-slate-400 uppercase mb-1">{t('label.type_title')}</span>
                  <strong className="text-slate-800">{t('label.type_val')}</strong>
                </div>

                <div className="col-span-full">
                  <span className="block text-xs font-bold text-slate-400 uppercase mb-1">{t('label.amount_title')}</span>
                  <strong className="text-slate-800">{t('label.amount_val')}</strong>
                </div>

                <div className="col-span-full">
                  <span className="block text-xs font-bold text-slate-400 uppercase mb-1">{t('label.ingredients_list_title')}</span>
                  <strong className="text-slate-800">{t('label.ingredients_list_val')}</strong>
                </div>

                <div className="col-span-full mt-2">
                  <span className="block text-xs font-bold text-[#00513b] uppercase mb-1">{t('label.effect_title')}</span>
                  <ul className="text-slate-800 font-medium list-disc pl-4 mt-1 space-y-1">
                    <li>{t('label.effect1')}</li>
                    <li>{t('label.effect2')}</li>
                    <li>{t('label.ing2_desc')}에 도움</li>
                  </ul>
                </div>

                <div className="flex justify-between items-center border-t border-slate-200 pt-3 mt-2 col-span-full">
                  <div><span className="text-xs font-bold text-slate-400 uppercase">{t('label.weight_title')}</span> <strong className="text-slate-800 ml-1">{t('label.weight_val')}</strong></div>
                  <div><span className="text-xs font-bold text-slate-400 uppercase">{t('label.mfg_title')}</span> <span className="text-slate-600 ml-1">{t('label.mfg_val')}</span></div>
                </div>
                <div className="col-span-full">
                  <span className="text-xs font-bold text-slate-400 uppercase">{t('label.exp_title')}</span> <span className="text-slate-600 ml-1">{t('label.exp_val')}</span>
                </div>
              </div>

              <div className="bg-rose-50 text-rose-800 p-4 rounded-xl text-xs font-medium border border-rose-100">
                <span className="font-bold block mb-1">{t('label.warning_title')}</span>
                <ul className="list-decimal pl-4 space-y-1">
                  <li>{t('label.warning1')}</li>
                  <li>{t('label.warning2_part1')} <strong className="text-rose-900 font-bold">{t('label.warning2_part2')}</strong>{t('label.warning2_part3')}</li>
                  <li>{t('label.warning3')}</li>
                </ul>
              </div>
            </div>
          </div>
        </div>

        {/* Modal Footer */}
        <div className="bg-slate-50 p-6 border-t border-slate-200 flex flex-col md:flex-row justify-between items-start md:items-center text-xs text-slate-500 rounded-b-3xl gap-4">
          <div className="flex flex-col sm:flex-row gap-6 w-full md:w-auto">
            <div className="flex items-center gap-3">
              <img src={`${import.meta.env.BASE_URL}assets/sj_logo.png`} alt="S&J" className="w-8 h-8 rounded-full border border-slate-200 bg-white" />
              <div>
                <strong className="block text-slate-700">{t('label.seller_name')}</strong>
                {t('label.seller_addr')}<br />
                <span className="text-amber-600">TEL</span> 031-321-6562
              </div>
            </div>
            <div className="border-l-0 sm:border-l border-slate-200 pl-0 sm:pl-6">
              <strong className="block text-slate-700">{t('label.maker_name')}</strong>
              {t('label.maker_addr')}<br />
              <span className="text-amber-600">TEL</span> 031-458-1240 / www.mobio.co.kr
            </div>
          </div>
          <button onClick={() => setIsPrintModalOpen(true)} className="shrink-0 bg-white border border-slate-300 hover:border-[#00513b] text-slate-700 hover:text-[#00513b] font-bold py-3 px-5 rounded-xl shadow-sm transition-colors flex items-center gap-2 w-full sm:w-auto justify-center">
            {t('label.print_btn')}
          </button>
        </div>
      </div>
    </div>
  );
};

export default LabelModal;
