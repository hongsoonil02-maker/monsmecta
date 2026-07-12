import React from 'react';
import { useTranslation } from 'react-i18next';

const ClinicalEvidence = () => {
  const { t } = useTranslation();

  return (
    <section id="clinical" className="py-10 md:py-20 bg-slate-100 border-y border-slate-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-8">
          <h2 className="text-3xl md:text-4xl font-extrabold text-[#00513b] break-keep">{t('clinical.title')}</h2>
          <div className="w-24 h-1.5 bg-yellow-400 mx-auto mt-6 rounded-full"></div>
        </div>

        <div className="grid lg:grid-cols-2 gap-10">

          {/* Card 1: LIQI Technology Comparison Table */}
          <div className="bg-white p-5 md:p-10 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-shadow duration-300">
            <h3 className="text-xl md:text-2xl font-black text-slate-800 mb-3 flex items-start sm:items-center gap-3 break-keep break-words">
              <span className="w-8 h-8 rounded-full shrink-0 bg-[#00513b] text-white flex items-center justify-center text-sm shadow-md">1</span>
              <span>{t('clinical.card1_title')}</span>
            </h3>
            <p className="text-slate-600 mb-6 leading-relaxed text-sm md:text-base">
              {t('clinical.card1_desc')}
            </p>
            <div className="w-full overflow-hidden">
              <table className="w-full text-sm border-collapse table-fixed">
                <colgroup>
                  <col style={{width: '30%'}} />
                  <col style={{width: '30%'}} />
                  <col style={{width: '30%'}} />
                  <col className="hidden sm:table-column" style={{width: '10%'}} />
                </colgroup>
                <thead>
                  <tr className="bg-[#00513b] text-white">
                    <th className="px-2 py-2.5 text-left font-bold text-xs break-keep">{t('clinical.table1_col1')}</th>
                    <th className="px-2 py-2.5 text-center font-bold text-xs break-keep">{t('clinical.table1_col2')}</th>
                    <th className="px-2 py-2.5 text-center font-bold text-xs bg-[#003d2b] break-keep">{t('clinical.table1_col3')}</th>
                    <th className="px-2 py-2.5 text-center font-bold text-xs hidden sm:table-cell">{t('clinical.table1_col_diff')}</th>
                  </tr>
                </thead>
                <tbody>
                  <tr className="border-b border-slate-100 hover:bg-emerald-50/50 transition-colors">
                    <td className="px-2 py-2.5 font-bold text-slate-700 text-xs break-keep">{t('clinical.table1_row1_label')}</td>
                    <td className="px-2 py-2.5 text-center text-slate-500 text-xs break-all">{t('clinical.table1_row1_val1')}</td>
                    <td className="px-2 py-2.5 text-center font-black text-[#00513b] text-xs bg-emerald-50 break-all">{t('clinical.table1_row1_val2')}</td>
                    <td className="px-2 py-2.5 text-center text-amber-600 font-bold text-xs hidden sm:table-cell">{t('clinical.table1_row1_diff')}</td>
                  </tr>
                  <tr className="border-b border-slate-100 hover:bg-emerald-50/50 transition-colors">
                    <td className="px-2 py-2.5 font-bold text-slate-700 text-xs break-keep">{t('clinical.table1_row2_label')}</td>
                    <td className="px-2 py-2.5 text-center text-slate-500 text-xs break-all">{t('clinical.table1_row2_val1')}</td>
                    <td className="px-2 py-2.5 text-center font-black text-[#00513b] text-xs bg-emerald-50 break-all">{t('clinical.table1_row2_val2')}</td>
                    <td className="px-2 py-2.5 text-center text-amber-600 font-bold text-xs hidden sm:table-cell">{t('clinical.table1_row2_diff')}</td>
                  </tr>
                  <tr className="border-b border-slate-100 hover:bg-emerald-50/50 transition-colors">
                    <td className="px-2 py-2.5 font-bold text-slate-700 text-xs break-keep">{t('clinical.table1_row3_label')}</td>
                    <td className="px-2 py-2.5 text-center text-slate-500 text-xs break-all">{t('clinical.table1_row3_val1')}</td>
                    <td className="px-2 py-2.5 text-center font-black text-[#00513b] text-xs bg-emerald-50 break-all">{t('clinical.table1_row3_val2')}</td>
                    <td className="px-2 py-2.5 text-center text-amber-600 font-bold text-xs hidden sm:table-cell">{t('clinical.table1_row3_diff')}</td>
                  </tr>
                  <tr className="hover:bg-emerald-50/50 transition-colors">
                    <td className="px-2 py-2.5 font-bold text-slate-700 text-xs break-keep">{t('clinical.table1_row4_label')}</td>
                    <td className="px-2 py-2.5 text-center text-slate-500 text-xs break-all">{t('clinical.table1_row4_val1')}</td>
                    <td className="px-2 py-2.5 text-center font-black text-[#00513b] text-xs bg-emerald-50 break-all">{t('clinical.table1_row4_val2')}</td>
                    <td className="px-2 py-2.5 text-center text-amber-600 font-bold text-xs hidden sm:table-cell">{t('clinical.table1_row4_diff')}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          {/* Card 2: Clinical Efficacy Test Data */}
          <div className="bg-white p-5 md:p-10 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-shadow duration-300">
            <h3 className="text-xl md:text-2xl font-black text-slate-800 mb-3 flex items-start sm:items-center gap-3 break-keep break-words">
              <span className="w-8 h-8 rounded-full shrink-0 bg-[#00513b] text-white flex items-center justify-center text-sm shadow-md">2</span>
              <span>{t('clinical.card2_title')}</span>
            </h3>
            <p className="text-slate-600 mb-6 leading-relaxed text-sm md:text-base">
              {t('clinical.card2_desc')}
            </p>
            <div className="space-y-3">
              <div className="bg-slate-50 rounded-xl p-4 border border-slate-200 hover:border-emerald-300 transition-colors">
                <div className="flex items-start gap-2 mb-1">
                  <span className="font-bold text-slate-700 text-sm flex-1 min-w-0 break-keep">{t('clinical.table2_row1_label')}</span>
                  <span className="text-[#00513b] font-black text-lg shrink-0">98.5%</span>
                </div>
                <p className="text-xs text-slate-500">{t('clinical.table2_row1_cond')}</p>
                <p className="text-xs font-bold text-emerald-700 mt-1">{t('clinical.table2_row1_result')}</p>
              </div>
              <div className="bg-slate-50 rounded-xl p-4 border border-slate-200 hover:border-emerald-300 transition-colors">
                <div className="flex items-start gap-2 mb-1">
                  <span className="font-bold text-slate-700 text-sm flex-1 min-w-0 break-keep">{t('clinical.table2_row2_label')}</span>
                  <span className="text-[#00513b] font-black text-lg shrink-0">pH 4.5~5.5</span>
                </div>
                <p className="text-xs text-slate-500">{t('clinical.table2_row2_cond')}</p>
                <p className="text-xs font-bold text-emerald-700 mt-1">{t('clinical.table2_row2_result')}</p>
              </div>
              <div className="bg-slate-50 rounded-xl p-4 border border-slate-200 hover:border-emerald-300 transition-colors">
                <div className="flex items-start gap-2 mb-1">
                  <span className="font-bold text-slate-700 text-sm flex-1 min-w-0 break-keep">{t('clinical.table2_row3_label')}</span>
                  <span className="text-[#00513b] font-black text-lg shrink-0">{t('clinical.table2_row3_value')}</span>
                </div>
                <p className="text-xs text-slate-500">{t('clinical.table2_row3_cond')}</p>
                <p className="text-xs font-bold text-emerald-700 mt-1">{t('clinical.table2_row3_result')}</p>
              </div>
              <div className="bg-slate-50 rounded-xl p-4 border border-slate-200 hover:border-emerald-300 transition-colors">
                <div className="flex items-start gap-2 mb-1">
                  <span className="font-bold text-slate-700 text-sm flex-1 min-w-0 break-keep">{t('clinical.table2_row4_label')}</span>
                  <span className="text-[#00513b] font-black text-lg shrink-0">{t('clinical.table2_row4_value')}</span>
                </div>
                <p className="text-xs text-slate-500">{t('clinical.table2_row4_cond')}</p>
                <p className="text-xs font-bold text-emerald-700 mt-1">{t('clinical.table2_row4_result')}</p>
              </div>
            </div>
          </div>

          {/* Card 3: Antiviral Effects Table */}
          <div className="bg-white p-5 md:p-10 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-shadow duration-300">
            <h3 className="text-xl md:text-2xl font-black text-slate-800 mb-3 flex items-start sm:items-center gap-3 break-keep break-words">
              <span className="w-8 h-8 rounded-full shrink-0 bg-[#00513b] text-white flex items-center justify-center text-sm shadow-md">3</span>
              <span>{t('clinical.card3_title')}</span>
            </h3>
            <p className="text-slate-600 mb-6 leading-relaxed text-sm md:text-base">
              {t('clinical.card3_desc')}
            </p>
            <div className="w-full overflow-hidden">
              <table className="w-full text-sm border-collapse table-fixed">
                <colgroup>
                  <col style={{width: '32%'}} />
                  <col style={{width: '48%'}} />
                  <col style={{width: '20%'}} />
                </colgroup>
                <thead>
                  <tr className="bg-[#00513b] text-white">
                    <th className="px-2 py-2.5 text-left font-bold text-xs">바이러스 계통</th>
                    <th className="px-2 py-2.5 text-left font-bold text-xs">{t('clinical.table3_header')}</th>
                    <th className="px-2 py-2.5 text-center font-bold text-xs">효과</th>
                  </tr>
                </thead>
                <tbody>
                  <tr className="border-b border-slate-100 hover:bg-emerald-50/50 transition-colors">
                    <td className="px-2 py-2.5 text-xs text-slate-500 break-words">Arteriviruses</td>
                    <td className="px-2 py-2.5 text-xs font-medium text-slate-700 break-keep">{t('clinical.table3_row1')}</td>
                    <td className="px-2 py-2.5 text-center"><span className="inline-block bg-emerald-100 text-emerald-700 text-xs font-bold px-1.5 py-0.5 rounded-full whitespace-nowrap">{t('clinical.table3_effect')}</span></td>
                  </tr>
                  <tr className="border-b border-slate-100 hover:bg-emerald-50/50 transition-colors">
                    <td className="px-2 py-2.5 text-xs text-slate-500 break-words">Orthomyxoviridae</td>
                    <td className="px-2 py-2.5 text-xs font-medium text-slate-700 break-keep">{t('clinical.table3_row2')}</td>
                    <td className="px-2 py-2.5 text-center"><span className="inline-block bg-emerald-100 text-emerald-700 text-xs font-bold px-1.5 py-0.5 rounded-full whitespace-nowrap">{t('clinical.table3_effect')}</span></td>
                  </tr>
                  <tr className="border-b border-slate-100 hover:bg-emerald-50/50 transition-colors">
                    <td className="px-2 py-2.5 text-xs text-slate-500 break-words">Pestiviruses</td>
                    <td className="px-2 py-2.5 text-xs font-medium text-slate-700 break-keep">{t('clinical.table3_row3')}</td>
                    <td className="px-2 py-2.5 text-center"><span className="inline-block bg-emerald-100 text-emerald-700 text-xs font-bold px-1.5 py-0.5 rounded-full whitespace-nowrap">{t('clinical.table3_effect')}</span></td>
                  </tr>
                  <tr className="border-b border-slate-100 hover:bg-emerald-50/50 transition-colors">
                    <td className="px-2 py-2.5 text-xs text-slate-500 break-words">Bunyaviridae</td>
                    <td className="px-2 py-2.5 text-xs font-medium text-slate-700 break-keep">{t('clinical.table3_row4')}</td>
                    <td className="px-2 py-2.5 text-center"><span className="inline-block bg-emerald-100 text-emerald-700 text-xs font-bold px-1.5 py-0.5 rounded-full whitespace-nowrap">{t('clinical.table3_effect')}</span></td>
                  </tr>
                  <tr className="hover:bg-emerald-50/50 transition-colors">
                    <td className="px-2 py-2.5 text-xs text-slate-500 break-words">Rhabdoviridae</td>
                    <td className="px-2 py-2.5 text-xs font-medium text-slate-700 break-keep">{t('clinical.table3_row5')}</td>
                    <td className="px-2 py-2.5 text-center"><span className="inline-block bg-emerald-100 text-emerald-700 text-xs font-bold px-1.5 py-0.5 rounded-full whitespace-nowrap">{t('clinical.table3_effect')}</span></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          {/* Card 4: Expert Review Meeting Feedback */}
          <div className="bg-white p-5 md:p-10 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-shadow duration-300 flex flex-col justify-between">
            <div>
              <h3 className="text-xl md:text-2xl font-black text-slate-800 mb-3 flex items-start sm:items-center gap-3 break-keep break-words">
                <span className="w-8 h-8 rounded-full shrink-0 bg-[#00513b] text-white flex items-center justify-center text-sm shadow-md">4</span>
                <span>{t('clinical.card4_title')}</span>
              </h3>
              <p className="text-slate-600 mb-6 leading-relaxed text-sm md:text-base">
                {t('clinical.card4_desc')}
              </p>
              <div className="space-y-5">
                <div className="bg-gradient-to-r from-emerald-50 to-slate-50 p-5 rounded-xl border-l-4 border-[#00513b]">
                  <p className="text-slate-700 italic font-medium text-sm mb-2">{t('clinical.card4_quote1')}</p>
                  <p className="text-xs font-bold text-[#00513b]">— {t('clinical.card4_quote1_author')}</p>
                </div>
                <div className="bg-gradient-to-r from-amber-50 to-slate-50 p-5 rounded-xl border-l-4 border-amber-500">
                  <p className="text-slate-700 italic font-medium text-sm mb-2">{t('clinical.card4_quote4')}</p>
                  <p className="text-xs font-bold text-amber-700">— {t('clinical.card4_quote4_author')}</p>
                </div>
                <div className="bg-gradient-to-r from-emerald-50 to-slate-50 p-5 rounded-xl border-l-4 border-[#00513b]">
                  <p className="text-slate-700 italic font-medium text-sm mb-2">{t('clinical.card4_quote2')}</p>
                  <p className="text-xs font-bold text-[#00513b]">— {t('clinical.card4_quote2_author')}</p>
                </div>
                <div className="bg-gradient-to-r from-amber-50 to-slate-50 p-5 rounded-xl border-l-4 border-amber-500">
                  <p className="text-slate-700 italic font-medium text-sm mb-2">{t('clinical.card4_quote3')}</p>
                  <p className="text-xs font-bold text-amber-700">— {t('clinical.card4_quote3_author')}</p>
                </div>
              </div>
            </div>
            <div className="mt-6 bg-amber-50 border border-amber-200 rounded-xl p-4">
              <p className="text-xs font-medium text-amber-800">📌 {t('clinical.card4_note')}</p>
            </div>
          </div>

        </div>
      </div>
    </section>
  );
};

export default ClinicalEvidence;
