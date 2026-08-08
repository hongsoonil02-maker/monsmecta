import React from 'react';
import { useTranslation } from 'react-i18next';
import { LABEL_DATA } from '../data/labels';

const THEME_MAP = {
  monsmecta: {
    bg: 'bg-[#002b1f]',
    bodyBg: 'bg-[#051110]',
    text: 'text-emerald-400',
    border: 'border-[#00513b]',
    headerGradient: 'from-[#00513b] via-[#003d2b] to-[#00281d]',
    accentBg: 'bg-emerald-900/30',
    accentText: 'text-emerald-300',
    buttonBorder: 'border-emerald-500/30 hover:border-emerald-400',
    buttonText: 'text-emerald-300 hover:text-emerald-200'
  },
  hepamax: {
    bg: 'bg-[#2b1d00]',
    bodyBg: 'bg-[#110d05]',
    text: 'text-amber-400',
    border: 'border-[#513b00]',
    headerGradient: 'from-[#513b00] via-[#3d2b00] to-[#281d00]',
    accentBg: 'bg-amber-900/30',
    accentText: 'text-amber-300',
    buttonBorder: 'border-amber-500/30 hover:border-amber-400',
    buttonText: 'text-amber-300 hover:text-amber-200'
  },
  probiotics: {
    bg: 'bg-[#0a1c2b]',
    bodyBg: 'bg-[#0b1115]',
    text: 'text-sky-400',
    border: 'border-[#003b51]',
    headerGradient: 'from-[#003b51] via-[#002b3d] to-[#001d28]',
    accentBg: 'bg-sky-900/30',
    accentText: 'text-sky-300',
    buttonBorder: 'border-sky-500/30 hover:border-sky-400',
    buttonText: 'text-sky-300 hover:text-sky-200'
  },
  urinary: {
    bg: 'bg-[#2b001a]',
    bodyBg: 'bg-[#11000b]',
    text: 'text-pink-400',
    border: 'border-[#51003b]',
    headerGradient: 'from-[#51003b] via-[#3d002b] to-[#28001d]',
    accentBg: 'bg-pink-900/30',
    accentText: 'text-pink-300',
    buttonBorder: 'border-pink-500/30 hover:border-pink-400',
    buttonText: 'text-pink-300 hover:text-pink-200'
  },
  cancercare: {
    bg: 'bg-[#2b0a2b]',
    bodyBg: 'bg-[#0b050b]',
    text: 'text-purple-400',
    border: 'border-[#510051]',
    headerGradient: 'from-[#510051] via-[#3d003d] to-[#280028]',
    accentBg: 'bg-purple-900/30',
    accentText: 'text-purple-300',
    buttonBorder: 'border-purple-500/30 hover:border-purple-400',
    buttonText: 'text-purple-300 hover:text-purple-200'
  },
  coldzero: {
    bg: 'bg-[#0a2b2b]',
    bodyBg: 'bg-[#051515]',
    text: 'text-cyan-400',
    border: 'border-[#005151]',
    headerGradient: 'from-[#005151] via-[#003d3d] to-[#002828]',
    accentBg: 'bg-cyan-900/30',
    accentText: 'text-cyan-300',
    buttonBorder: 'border-cyan-500/30 hover:border-cyan-400',
    buttonText: 'text-cyan-300 hover:text-cyan-200'
  }
};

const LabelModal = ({ isLabelModalOpen, setIsLabelModalOpen, setIsPrintModalOpen, activeProduct }) => {
  const { t } = useTranslation();
  const labelData = LABEL_DATA[activeProduct] || LABEL_DATA['monsmecta'];
  const theme = THEME_MAP[activeProduct] || THEME_MAP['monsmecta'];

  if (!isLabelModalOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-md transition-opacity" role="dialog" aria-modal="true" aria-labelledby="label-modal-title">
      <div className={`${theme.bodyBg} border ${theme.border} rounded-3xl shadow-2xl shadow-black/50 w-full max-w-4xl max-h-[90vh] overflow-y-auto relative animate-in fade-in zoom-in duration-300`}>
        <div className={`sticky top-0 bg-gradient-to-r ${theme.headerGradient} border-b ${theme.border} text-white p-6 flex justify-between items-center z-10`}>
          <div>
            <p className={`text-xs ${theme.text} font-bold tracking-widest uppercase mb-1`}>{t('label.header_eyebrow')}</p>
            <h3 id="label-modal-title" className="text-2xl font-black text-white">{t('label.header_title')}</h3>
          </div>
          <button onClick={() => setIsLabelModalOpen(false)} aria-label={t('common.close')} className="text-white/60 hover:text-white bg-white/5 hover:bg-white/10 rounded-full p-2 transition-colors">
            <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        <div className="p-8">
          <div className="flex flex-col md:flex-row gap-8">
            <div className={`md:w-1/3 flex flex-col items-center border-r border-white/10 pr-0 md:pr-8`}>
              <div className={`${theme.accentBg} w-full rounded-2xl p-6 flex justify-center items-center mb-6 border border-white/5`}>
                <img src={`${import.meta.env.BASE_URL}assets/bottle_mockup.png`} alt={labelData.product_name} className="w-3/4 max-w-[200px] drop-shadow-[0_10px_20px_rgba(0,0,0,0.5)] hover:scale-105 transition-transform" />
              </div>
              <div className="w-full text-center">
                <h4 className={`text-xl font-black ${theme.text} mb-2`}>{labelData.product_name}</h4>
                <p className="text-sm font-bold text-gray-300 mb-4">{labelData.desc}</p>
                <div className={`space-y-2 text-left bg-white/5 border border-white/5 p-4 rounded-xl`}>
                  <p className={`text-xs font-bold ${theme.accentText} break-keep`}>{labelData.feed1}</p>
                  <p className={`text-xs font-bold ${theme.accentText} break-keep`}>{labelData.feed2}</p>
                  <p className={`text-xs font-bold ${theme.accentText} break-keep`}>{labelData.feed3}</p>
                </div>
              </div>
            </div>

            <div className="md:w-2/3 space-y-6">
              <div>
                <h5 className={`text-lg font-bold text-white border-b-2 ${theme.border} pb-2 mb-4 inline-block break-keep`}>{labelData.ingredients_title}</h5>
                <ul className="space-y-3 text-sm text-gray-300">
                  {labelData.ingredients.map((ing, i) => (
                    <li key={i} className="break-keep">
                      <strong className={theme.text}>{ing.title}</strong> <span className="text-gray-400">|</span> {ing.desc} 
                      {ing.note && <><br /><span className="text-xs text-gray-500 pl-4">{ing.note}</span></>}
                    </li>
                  ))}
                </ul>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-sm bg-white/5 p-5 rounded-2xl border border-white/10">
                <div className="col-span-full border-b border-white/10 pb-2 mb-2 flex justify-between items-end">
                  <span className="block text-xs font-bold text-gray-500 uppercase break-keep">{t('label.reg_no_title')}</span>
                  <strong className="text-white break-keep">{labelData.reg_no}</strong>
                </div>

                <div className="col-span-full">
                  <span className="block text-xs font-bold text-gray-500 uppercase mb-1 break-keep">{t('label.type_title')}</span>
                  <strong className="text-gray-200 break-keep">{labelData.type_val}</strong>
                </div>

                <div className="col-span-full">
                  <span className="block text-xs font-bold text-gray-500 uppercase mb-1 break-keep">{t('label.amount_title')}</span>
                  <strong className="text-gray-200 break-keep">{labelData.amount_val}</strong>
                </div>

                <div className="col-span-full">
                  <span className="block text-xs font-bold text-gray-500 uppercase mb-1 break-keep">{t('label.ingredients_list_title')}</span>
                  <strong className="text-gray-300 break-keep leading-relaxed">{labelData.ingredients_list_val}</strong>
                </div>

                <div className="col-span-full mt-2 bg-black/20 p-4 rounded-xl border border-white/5">
                  <span className={`block text-xs font-bold ${theme.text} uppercase mb-2 break-keep`}>{t('label.effect_title')}</span>
                  <ul className="text-gray-200 font-medium list-disc pl-4 mt-1 space-y-1.5">
                    {labelData.effects.map((eff, i) => (
                      <li key={i} className="break-keep">{eff}</li>
                    ))}
                  </ul>
                </div>

                <div className="flex justify-between items-center border-t border-white/10 pt-4 mt-2 col-span-full">
                  <div><span className="text-xs font-bold text-gray-500 uppercase break-keep">{t('label.weight_title')}</span> <strong className="text-gray-200 ml-1 break-keep">{labelData.weight_val}</strong></div>
                  <div><span className="text-xs font-bold text-gray-500 uppercase break-keep">{t('label.mfg_title')}</span> <span className="text-gray-400 ml-1 break-keep">{labelData.mfg_val}</span></div>
                </div>
                <div className="col-span-full pt-1">
                  <span className="text-xs font-bold text-gray-500 uppercase break-keep">{t('label.exp_title')}</span> <span className="text-gray-400 ml-1 break-keep">{labelData.exp_val}</span>
                </div>
              </div>

              <div className="bg-rose-950/40 text-rose-300 p-4 rounded-xl text-xs font-medium border border-rose-900/50">
                <span className="font-bold block mb-1 break-keep text-rose-400">{t('label.warning_title')}</span>
                <ul className="list-decimal pl-4 space-y-1 text-rose-300/80">
                  {labelData.warnings.map((warn, i) => (
                    <li key={i} className="break-keep">{warn}</li>
                  ))}
                </ul>
              </div>
            </div>
          </div>
        </div>

        {/* Modal Footer */}
        <div className="bg-black/40 p-6 border-t border-white/10 flex flex-col md:flex-row justify-between items-start md:items-center text-xs text-gray-400 rounded-b-3xl gap-4">
          <div className="flex flex-col sm:flex-row gap-6 w-full md:w-auto">
            <div className="flex items-center gap-3">
              <img src={`${import.meta.env.BASE_URL}assets/sj_logo.png`} alt="S&J" className="w-8 h-8 rounded-full border border-white/20 bg-black/50" />
              <div>
                <strong className="block text-gray-200">{t('label.seller_name')}</strong>
                {t('label.seller_addr')}<br />
                <span className={theme.text}>TEL</span> {t('label.seller_tel')}
              </div>
            </div>
            <div className="border-l-0 sm:border-l border-white/10 pl-0 sm:pl-6">
              <strong className="block text-gray-200">{t('label.maker_name')}</strong>
              {t('label.maker_addr')}<br />
              <span className={theme.text}>TEL</span> {t('label.maker_tel')}
            </div>
          </div>
          <button onClick={() => setIsPrintModalOpen(true)} className={`shrink-0 bg-black/40 border ${theme.buttonBorder} ${theme.buttonText} hover:bg-white/5 font-bold py-3 px-5 rounded-xl shadow-sm transition-colors flex items-center gap-2 w-full sm:w-auto justify-center`}>
            <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"></path></svg>
            {t('label.print_btn')}
          </button>
        </div>
      </div>
    </div>
  );
};

export default LabelModal;
