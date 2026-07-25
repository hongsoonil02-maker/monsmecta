import React from 'react';
import { useTranslation } from 'react-i18next';

const ClinicalEvidence = () => {
  const { t } = useTranslation();

  return (
    <section id="clinical" className="py-12 md:py-24 bg-slate-100 border-y border-slate-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <h2 className="text-3xl md:text-4xl font-extrabold text-[#00513b] break-keep">{t('clinical.title')}</h2>
          <div className="w-24 h-1.5 bg-yellow-400 mx-auto mt-6 rounded-full"></div>
        </div>

        <div className="grid lg:grid-cols-2 gap-8 md:gap-10">

          {/* Card 1: LIQI Technology Comparison Table */}
          <div className="bg-white p-6 md:p-9 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-all duration-300 flex flex-col justify-between">
            <div>
              <h3 className="text-xl md:text-2xl font-black text-slate-800 mb-4 flex items-center gap-3 break-keep">
                <span className="w-9 h-9 rounded-full shrink-0 bg-[#00513b] text-white flex items-center justify-center text-sm font-bold shadow-md">1</span>
                <span>{t('clinical.card1_title')}</span>
              </h3>
              <p className="text-slate-600 mb-6 leading-relaxed text-sm md:text-base font-normal">
                {t('clinical.card1_desc')}
              </p>
              <div className="w-full overflow-hidden rounded-2xl border border-slate-200 shadow-sm mb-6">
                <table className="w-full text-sm border-collapse table-fixed">
                  <colgroup>
                    <col style={{width: '28%'}} />
                    <col style={{width: '28%'}} />
                    <col style={{width: '22%'}} />
                    <col style={{width: '22%'}} />
                  </colgroup>
                  <thead>
                    <tr className="bg-[#00513b] text-white">
                      <th className="px-2 py-3.5 text-center font-bold text-xs break-keep">{t('clinical.table1_col1')}</th>
                      <th className="px-2 py-3.5 text-center font-bold text-xs bg-[#003d2b] break-keep">{t('clinical.table1_col2')}</th>
                      <th className="px-2 py-3.5 text-center font-bold text-xs break-keep">{t('clinical.table1_col3')}</th>
                      <th className="px-2 py-3.5 text-center font-bold text-xs break-keep">{t('clinical.table1_col4')}</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr className="border-b border-slate-100 hover:bg-emerald-50/50 transition-colors">
                      <td className="px-2 py-4 text-center font-bold text-slate-700 text-xs break-keep">{t('clinical.table1_row1_label')}</td>
                      <td className="px-2 py-4 text-center font-black text-[#00513b] text-sm bg-emerald-50/80 break-all">{t('clinical.table1_row1_val1')}</td>
                      <td className="px-2 py-4 text-center text-slate-500 text-xs break-all">{t('clinical.table1_row1_val2')}</td>
                      <td className="px-2 py-4 text-center text-slate-500 text-xs break-all">{t('clinical.table1_row1_val3')}</td>
                    </tr>
                    <tr className="hover:bg-emerald-50/50 transition-colors">
                      <td className="px-2 py-4 text-center font-bold text-slate-700 text-xs break-keep">{t('clinical.table1_row2_label')}</td>
                      <td className="px-2 py-4 text-center font-black text-red-600 text-sm bg-emerald-50/80 break-all">{t('clinical.table1_row2_val1')}</td>
                      <td className="px-2 py-4 text-center text-slate-500 text-xs break-all">{t('clinical.table1_row2_val2')}</td>
                      <td className="px-2 py-4 text-center text-slate-500 text-xs break-all">{t('clinical.table1_row2_val3')}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            
            {/* 하단 균형용 핵심 요약 박스 */}
            <div className="bg-emerald-50/90 border border-emerald-200 rounded-2xl p-4 text-xs font-medium text-[#00513b] leading-relaxed shadow-sm flex flex-col gap-3">
              <div>
                <span className="font-bold text-sm block mb-1">💡 초미세공정 핵심 기술</span>
                일반 몬모릴로나이트 대비 표면적 8배 이상(≥800 m²/g), 입자도 50배 이상 초미세화(≤6.5 µm)를 통해 장내 독소 및 유해 바이러스의 물리적 흡착 배출 성능을 극대화하였습니다.
              </div>
              <div className="pt-2.5 border-t border-emerald-200/80 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                <span className="text-[11px] text-emerald-900 font-semibold">📚 Montmorillonite(몬모릴로나이트) 독소 흡착·지사 글로벌 연구 자료</span>
                <a
                  href="https://www.google.com/search?q=montmorillonite+toxin+adsorption"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center justify-center gap-1.5 shrink-0 bg-[#00513b] hover:bg-[#003d2b] text-white text-[11px] font-bold px-3 py-1.5 rounded-xl transition-all shadow-sm hover:shadow-md hover:-translate-y-0.5"
                >
                  <span>🔍 Google 학술 논문 검색</span>
                  <svg className="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" /></svg>
                </a>
              </div>
            </div>
          </div>

          {/* Card 2: Clinical Efficacy Test Data */}
          <div className="bg-white p-6 md:p-9 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-all duration-300 flex flex-col justify-between">
            <div>
              <h3 className="text-xl md:text-2xl font-black text-slate-800 mb-4 flex items-center gap-3 break-keep">
                <span className="w-9 h-9 rounded-full shrink-0 bg-[#00513b] text-white flex items-center justify-center text-sm font-bold shadow-md">2</span>
                <span>{t('clinical.card2_title')}</span>
              </h3>
              <p className="text-slate-600 mb-6 leading-relaxed text-sm md:text-base font-normal">
                {t('clinical.card2_desc')}
              </p>
              <div className="space-y-3.5">
                <div className="bg-slate-50 rounded-2xl p-4 border border-slate-200 hover:border-emerald-300 transition-colors shadow-sm">
                  <div className="flex items-center justify-between mb-1">
                    <span className="font-bold text-slate-800 text-sm break-keep">{t('clinical.table2_row1_label')}</span>
                    <span className="text-[#00513b] font-black text-lg">98.5%</span>
                  </div>
                  <p className="text-xs text-slate-500 mb-1">{t('clinical.table2_row1_cond')}</p>
                  <p className="text-xs font-bold text-emerald-700">{t('clinical.table2_row1_result')}</p>
                </div>
                <div className="bg-slate-50 rounded-2xl p-4 border border-slate-200 hover:border-emerald-300 transition-colors shadow-sm">
                  <div className="flex items-center justify-between mb-1">
                    <span className="font-bold text-slate-800 text-sm break-keep">{t('clinical.table2_row2_label')}</span>
                    <span className="text-[#00513b] font-black text-lg">pH 4.5~5.5</span>
                  </div>
                  <p className="text-xs text-slate-500 mb-1">{t('clinical.table2_row2_cond')}</p>
                  <p className="text-xs font-bold text-emerald-700">{t('clinical.table2_row2_result')}</p>
                </div>
                <div className="bg-slate-50 rounded-2xl p-4 border border-slate-200 hover:border-emerald-300 transition-colors shadow-sm">
                  <div className="flex items-center justify-between mb-1">
                    <span className="font-bold text-slate-800 text-sm break-keep">{t('clinical.table2_row3_label')}</span>
                    <span className="text-[#00513b] font-black text-base">{t('clinical.table2_row3_value')}</span>
                  </div>
                  <p className="text-xs text-slate-500 mb-1">{t('clinical.table2_row3_cond')}</p>
                  <p className="text-xs font-bold text-emerald-700">{t('clinical.table2_row3_result')}</p>
                </div>
                <div className="bg-slate-50 rounded-2xl p-4 border border-slate-200 hover:border-emerald-300 transition-colors shadow-sm">
                  <div className="flex items-center justify-between mb-1">
                    <span className="font-bold text-slate-800 text-sm break-keep">{t('clinical.table2_row4_label')}</span>
                    <span className="text-[#00513b] font-black text-base">{t('clinical.table2_row4_value')}</span>
                  </div>
                  <p className="text-xs text-slate-500 mb-1">{t('clinical.table2_row4_cond')}</p>
                  <p className="text-xs font-bold text-emerald-700">{t('clinical.table2_row4_result')}</p>
                </div>
              </div>
            </div>
          </div>

          {/* Card 3: Antiviral Effects Table */}
          <div className="bg-white p-6 md:p-9 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-all duration-300 flex flex-col justify-between">
            <div>
              <h3 className="text-xl md:text-2xl font-black text-slate-800 mb-4 flex items-center gap-3 break-keep">
                <span className="w-9 h-9 rounded-full shrink-0 bg-[#00513b] text-white flex items-center justify-center text-sm font-bold shadow-md">3</span>
                <span>{t('clinical.card3_title')}</span>
              </h3>
              <p className="text-slate-600 mb-6 leading-relaxed text-sm md:text-base font-normal">
                {t('clinical.card3_desc')}
              </p>
              <div className="w-full overflow-hidden rounded-2xl border border-slate-200 shadow-sm mb-6">
                <table className="w-full text-sm border-collapse table-fixed">
                  <colgroup>
                    <col style={{width: '32%'}} />
                    <col style={{width: '48%'}} />
                    <col style={{width: '20%'}} />
                  </colgroup>
                  <thead>
                    <tr className="bg-[#00513b] text-white">
                      <th className="px-3 py-3 text-left font-bold text-xs">바이러스 계통</th>
                      <th className="px-3 py-3 text-left font-bold text-xs">{t('clinical.table3_header')}</th>
                      <th className="px-3 py-3 text-center font-bold text-xs">효과</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr className="border-b border-slate-100 hover:bg-emerald-50/50 transition-colors">
                      <td className="px-3 py-3 text-xs text-slate-500 break-words font-medium">Arteriviruses</td>
                      <td className="px-3 py-3 text-xs font-medium text-slate-700 break-keep">{t('clinical.table3_row1')}</td>
                      <td className="px-3 py-3 text-center"><span className="inline-block bg-emerald-100 text-emerald-800 text-xs font-bold px-2 py-0.5 rounded-full whitespace-nowrap">{t('clinical.table3_effect')}</span></td>
                    </tr>
                    <tr className="border-b border-slate-100 hover:bg-emerald-50/50 transition-colors">
                      <td className="px-3 py-3 text-xs text-slate-500 break-words font-medium">Orthomyxoviridae</td>
                      <td className="px-3 py-3 text-xs font-medium text-slate-700 break-keep">{t('clinical.table3_row2')}</td>
                      <td className="px-3 py-3 text-center"><span className="inline-block bg-emerald-100 text-emerald-800 text-xs font-bold px-2 py-0.5 rounded-full whitespace-nowrap">{t('clinical.table3_effect')}</span></td>
                    </tr>
                    <tr className="border-b border-slate-100 hover:bg-emerald-50/50 transition-colors">
                      <td className="px-3 py-3 text-xs text-slate-500 break-words font-medium">Pestiviruses</td>
                      <td className="px-3 py-3 text-xs font-medium text-slate-700 break-keep">{t('clinical.table3_row3')}</td>
                      <td className="px-3 py-3 text-center"><span className="inline-block bg-emerald-100 text-emerald-800 text-xs font-bold px-2 py-0.5 rounded-full whitespace-nowrap">{t('clinical.table3_effect')}</span></td>
                    </tr>
                    <tr className="border-b border-slate-100 hover:bg-emerald-50/50 transition-colors">
                      <td className="px-3 py-3 text-xs text-slate-500 break-words font-medium">Bunyaviridae</td>
                      <td className="px-3 py-3 text-xs font-medium text-slate-700 break-keep">{t('clinical.table3_row4')}</td>
                      <td className="px-3 py-3 text-center"><span className="inline-block bg-emerald-100 text-emerald-800 text-xs font-bold px-2 py-0.5 rounded-full whitespace-nowrap">{t('clinical.table3_effect')}</span></td>
                    </tr>
                    <tr className="hover:bg-emerald-50/50 transition-colors">
                      <td className="px-3 py-3 text-xs text-slate-500 break-words font-medium">Rhabdoviridae</td>
                      <td className="px-3 py-3 text-xs font-medium text-slate-700 break-keep">{t('clinical.table3_row5')}</td>
                      <td className="px-3 py-3 text-center"><span className="inline-block bg-emerald-100 text-emerald-800 text-xs font-bold px-2 py-0.5 rounded-full whitespace-nowrap">{t('clinical.table3_effect')}</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            {/* 하단 균형용 연구 요약 박스 */}
            <div className="bg-emerald-50/90 border border-emerald-200 rounded-2xl p-4 text-xs font-medium text-[#00513b] leading-relaxed shadow-sm flex flex-col gap-3">
              <div>
                <span className="font-bold text-sm block mb-1">🔬 항바이러스 학술 검증</span>
                DNG-1000 핵심 균주(Bacillus subtilis MORI)가 생산하는 DNJ 성분이 소, 돼지, 조류 등 주요 5대 바이러스 계통의 증식을 유의미하게 억제함을 입증하였습니다.
              </div>
              <div className="pt-2.5 border-t border-emerald-200/80 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                <span className="text-[11px] text-emerald-900 font-semibold">📚 1-Deoxynojirimycin(DNJ) 학술 논문 및 글로벌 연구 자료</span>
                <a
                  href="https://www.google.com/search?q=1-deoxynojirimycin+antiviral"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center justify-center gap-1.5 shrink-0 bg-[#00513b] hover:bg-[#003d2b] text-white text-[11px] font-bold px-3 py-1.5 rounded-xl transition-all shadow-sm hover:shadow-md hover:-translate-y-0.5"
                >
                  <span>🔍 Google 학술 논문 검색</span>
                  <svg className="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" /></svg>
                </a>
              </div>
            </div>
          </div>

          {/* Card 4: Expert Review Meeting Feedback */}
          <div className="bg-white p-6 md:p-9 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-all duration-300 flex flex-col justify-between">
            <div>
              <h3 className="text-xl md:text-2xl font-black text-slate-800 mb-4 flex items-center gap-3 break-keep">
                <span className="w-9 h-9 rounded-full shrink-0 bg-[#00513b] text-white flex items-center justify-center text-sm font-bold shadow-md">4</span>
                <span>{t('clinical.card4_title')}</span>
              </h3>
              <p className="text-slate-600 mb-6 leading-relaxed text-sm md:text-base font-normal">
                {t('clinical.card4_desc')}
              </p>
              <div className="space-y-3.5">
                <div className="bg-gradient-to-r from-emerald-50/80 to-slate-50 p-4 rounded-2xl border-l-4 border-[#00513b] shadow-sm">
                  <p className="text-slate-700 italic font-medium text-xs md:text-sm leading-relaxed mb-2">{t('clinical.card4_quote1')}</p>
                  <p className="text-xs font-bold text-[#00513b]">— {t('clinical.card4_quote1_author')}</p>
                </div>
                <div className="bg-gradient-to-r from-amber-50/80 to-slate-50 p-4 rounded-2xl border-l-4 border-amber-500 shadow-sm">
                  <p className="text-slate-700 italic font-medium text-xs md:text-sm leading-relaxed mb-2">{t('clinical.card4_quote4')}</p>
                  <p className="text-xs font-bold text-amber-800">— {t('clinical.card4_quote4_author')}</p>
                </div>
                <div className="bg-gradient-to-r from-emerald-50/80 to-slate-50 p-4 rounded-2xl border-l-4 border-[#00513b] shadow-sm">
                  <p className="text-slate-700 italic font-medium text-xs md:text-sm leading-relaxed mb-2">{t('clinical.card4_quote2')}</p>
                  <p className="text-xs font-bold text-[#00513b]">— {t('clinical.card4_quote2_author')}</p>
                </div>
                <div className="bg-gradient-to-r from-amber-50/80 to-slate-50 p-4 rounded-2xl border-l-4 border-amber-500 shadow-sm">
                  <p className="text-slate-700 italic font-medium text-xs md:text-sm leading-relaxed mb-2">{t('clinical.card4_quote3')}</p>
                  <p className="text-xs font-bold text-amber-800">— {t('clinical.card4_quote3_author')}</p>
                </div>
              </div>
            </div>
            
            <div className="mt-5 bg-amber-50/90 border border-amber-200 rounded-2xl p-4 shadow-sm">
              <p className="text-xs font-medium text-amber-900 leading-relaxed">📌 {t('clinical.card4_note')}</p>
            </div>
          </div>

        </div>
      </div>
    </section>
  );
};

export default ClinicalEvidence;
