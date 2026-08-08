import React, { useState } from 'react';
import { useTranslation } from 'react-i18next';

const ClinicalEvidence = ({ activeProduct }) => {
  const { t } = useTranslation();

  return (
    <section id="clinical" className="py-12 md:py-24 bg-slate-100 border-y border-slate-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <h2 className="text-3xl md:text-4xl font-extrabold text-[#00513b] break-keep">{t('clinical.title', '학술 검증 및 임상 시험 데이터')}</h2>
          <div className="w-24 h-1.5 bg-yellow-400 mx-auto mt-6 rounded-full mb-8"></div>
        </div>

        {activeProduct === 'monsmecta' ? (
        <div className="grid lg:grid-cols-2 gap-8 md:gap-10 animate-in fade-in zoom-in-95 duration-300">

          {/* Card 1: LIQI Technology Comparison Table */}
          <div className="bg-white p-4 sm:p-6 md:p-9 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-all duration-300 flex flex-col justify-between">
            <div>
              <h3 className="text-xl md:text-2xl font-black text-slate-800 mb-4 flex items-center gap-3 break-keep">
                <span className="w-9 h-9 rounded-full shrink-0 bg-[#00513b] text-white flex items-center justify-center text-sm font-bold shadow-md">1</span>
                <span>{t('clinical.card1_title', '초미세공정 기술 차별성')}</span>
              </h3>
              <p className="text-slate-600 mb-6 leading-relaxed text-sm md:text-base font-normal">
                {t('clinical.card1_desc', '몬스멕타의 핵심 기술인 올트라파인 초미세공정이 기존 정장지사제 원료와 비교하여 압도적인 성능을 입증합니다.')}
              </p>
              <div className="w-full overflow-x-auto rounded-2xl border border-slate-200 shadow-sm mb-6">
                <table className="w-full text-sm border-collapse table-fixed">
                  <colgroup>
                    <col style={{width: '28%'}} />
                    <col style={{width: '28%'}} />
                    <col style={{width: '22%'}} />
                    <col style={{width: '22%'}} />
                  </colgroup>
                  <thead>
                    <tr className="bg-[#00513b] text-white">
                      <th className="px-2 py-3.5 text-center font-bold text-xs break-keep">{t('clinical.table1_col1', '지표')}</th>
                      <th className="px-2 py-3.5 text-center font-bold text-xs bg-[#003d2b] break-keep">{t('clinical.table1_col2', '몬스멕타 고순도 초미세 나노 몬모릴로나이트')}</th>
                      <th className="px-2 py-3.5 text-center font-bold text-xs break-keep">{t('clinical.table1_col3', '약품등급 몬모릴로나이트')}</th>
                      <th className="px-2 py-3.5 text-center font-bold text-xs break-keep">{t('clinical.table1_col4', '일반 몬모릴로나이트')}</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr className="border-b border-slate-100 hover:bg-emerald-50/50 transition-colors">
                      <td className="px-2 py-4 text-center font-bold text-slate-700 text-xs break-words sm:break-keep">{t('clinical.table1_row1_label', '표면적 m²/g')}</td>
                      <td className="px-2 py-4 text-center font-black text-[#00513b] text-sm bg-emerald-50/80 break-all">{t('clinical.table1_row1_val1', '≥800')}</td>
                      <td className="px-2 py-4 text-center text-slate-500 text-xs break-all">{t('clinical.table1_row1_val2', '71 *')}</td>
                      <td className="px-2 py-4 text-center text-slate-500 text-xs break-all">{t('clinical.table1_row1_val3', '≥100')}</td>
                    </tr>
                    <tr className="hover:bg-emerald-50/50 transition-colors">
                      <td className="px-2 py-4 text-center font-bold text-slate-700 text-xs break-words sm:break-keep">{t('clinical.table1_row2_label', '입자도 (um) D90')}</td>
                      <td className="px-2 py-4 text-center font-black text-red-600 text-sm bg-emerald-50/80 break-all">{t('clinical.table1_row2_val1', '≤6.5')}</td>
                      <td className="px-2 py-4 text-center text-slate-500 text-xs break-all">{t('clinical.table1_row2_val2', '≥200')}</td>
                      <td className="px-2 py-4 text-center text-slate-500 text-xs break-all">{t('clinical.table1_row2_val3', '≥325')}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            
            {/* 하단 균형용 핵심 요약 박스 */}
            <div className="bg-emerald-50/90 border border-emerald-200 rounded-2xl p-4 text-xs font-medium text-[#00513b] leading-relaxed shadow-sm flex flex-col gap-3">
              <div>
                <div className="flex items-start gap-1 mb-1">
                  <span className="font-bold text-sm shrink-0">💡</span>
                  <span className="font-bold text-sm break-keep">{t('clinical.techSummaryTitle', '초미세공정 핵심 기술')}</span>
                </div>
                <p className="break-keep">{t('clinical.techSummaryBody', '일반 몬모릴로나이트 대비 표면적 8배 이상(≥800 m²/g), 입자도 50배 이상 초미세화(≤6.5 µm)를 통해 장내 독소 및 유해 바이러스의 물리적 흡착 배출 성능을 극대화하였습니다.')}</p>
              </div>
              <div className="pt-2.5 border-t border-emerald-200/80 flex flex-col sm:flex-row sm:items-start justify-between gap-2">
                <div className="flex items-start gap-1">
                  <span className="text-[11px] shrink-0">📚</span>
                  <span className="text-[11px] text-emerald-900 font-semibold break-keep">{t('clinical.paperRef1', 'Smectite & Montmorillonite 독소 흡착·지사 글로벌 연구 자료')}</span>
                </div>
                <a
                  href="https://www.google.com/search?q=smectite+and+montmorillonite+adsorption"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center justify-center gap-1.5 shrink-0 bg-[#00513b] hover:bg-[#003d2b] text-white text-[11px] font-bold px-3 py-1.5 rounded-xl transition-all shadow-sm hover:shadow-md hover:-translate-y-0.5"
                >
                  <span className="shrink-0">🔍</span>
                  <span className="break-keep">{t('clinical.searchGoogle', 'Google 학술 논문 검색')}</span>
                </a>
              </div>
            </div>
          </div>

          {/* Card 2: Clinical Efficacy Test Data */}
          <div className="bg-white p-4 sm:p-6 md:p-9 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-all duration-300 flex flex-col justify-between">
            <div>
              <h3 className="text-xl md:text-2xl font-black text-slate-800 mb-4 flex items-center gap-3 break-keep">
                <span className="w-9 h-9 rounded-full shrink-0 bg-[#00513b] text-white flex items-center justify-center text-sm font-bold shadow-md">2</span>
                <span>{t('clinical.card2_title', '임상 효능 시험 데이터')}</span>
              </h3>
              <p className="text-slate-600 mb-6 leading-relaxed text-sm md:text-base font-normal">
                {t('clinical.card2_desc', '경상국립대 수의과대학 연구진의 학술적 근거를 바탕으로 한 시험 결과입니다.')}
              </p>
              <div className="space-y-3.5">
                <div className="bg-slate-50 rounded-2xl p-4 border border-slate-200 hover:border-emerald-300 transition-colors shadow-sm">
                  <div className="flex items-center justify-between mb-1">
                    <span className="font-bold text-slate-800 text-sm break-keep">{t('clinical.table2_row1_label', '곰팡이 독소 (AFB1)')}</span>
                    <span className="text-[#00513b] font-black text-lg">98.5%</span>
                  </div>
                  <p className="text-xs text-slate-500 mb-1">{t('clinical.table2_row1_cond', '100 ppm 농도 노출')}</p>
                  <p className="text-xs font-bold text-emerald-700">{t('clinical.table2_row1_result', '98.5% 흡착 제거')}</p>
                </div>
                <div className="bg-slate-50 rounded-2xl p-4 border border-slate-200 hover:border-emerald-300 transition-colors shadow-sm">
                  <div className="flex items-center justify-between mb-1">
                    <span className="font-bold text-slate-800 text-sm break-keep">{t('clinical.table2_row2_label', '위내 산도 완충')}</span>
                    <span className="text-[#00513b] font-black text-lg">pH 4.5~5.5</span>
                  </div>
                  <p className="text-xs text-slate-500 mb-1">{t('clinical.table2_row2_cond', 'pH 2.0 (위산 환경)')}</p>
                  <p className="text-xs font-bold text-emerald-700">{t('clinical.table2_row2_result', 'pH 4.5~5.5 유지')}</p>
                </div>
                <div className="bg-slate-50 rounded-2xl p-4 border border-slate-200 hover:border-emerald-300 transition-colors shadow-sm">
                  <div className="flex items-center justify-between mb-1">
                    <span className="font-bold text-slate-800 text-sm break-keep">{t('clinical.table2_row3_label', '임상 회복 속도')}</span>
                    <span className="text-[#00513b] font-black text-base">{t('clinical.table2_row3_value', '회복 단축 보조')}</span>
                  </div>
                  <p className="text-xs text-slate-500 mb-1">{t('clinical.table2_row3_cond', '파보 장염 환축 약 6,000례 임상 경험')}</p>
                  <p className="text-xs font-bold text-emerald-700">{t('clinical.table2_row3_result', '증상 회복 기간 단축에 도움')}</p>
                </div>
                <div className="bg-slate-50 rounded-2xl p-4 border border-slate-200 hover:border-emerald-300 transition-colors shadow-sm">
                  <div className="flex items-center justify-between mb-1">
                    <span className="font-bold text-slate-800 text-sm break-keep">{t('clinical.table2_row4_label', '바이러스 증식 억제')}</span>
                    <span className="text-[#00513b] font-black text-base">{t('clinical.table2_row4_value', '증식 억제')}</span>
                  </div>
                  <p className="text-xs text-slate-500 mb-1">{t('clinical.table2_row4_cond', '바실러스 서브틸리스 병용')}</p>
                  <p className="text-xs font-bold text-emerald-700">{t('clinical.table2_row4_result', '유의미한 증식 억제')}</p>
                </div>
              </div>
            </div>
          </div>

          {/* Card 3: Antiviral Effects Table */}
          <div className="bg-white p-4 sm:p-6 md:p-9 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-all duration-300 flex flex-col justify-between">
            <div>
              <h3 className="text-xl md:text-2xl font-black text-slate-800 mb-4 flex items-center gap-3 break-keep">
                <span className="w-9 h-9 rounded-full shrink-0 bg-[#00513b] text-white flex items-center justify-center text-sm font-bold shadow-md">3</span>
                <span>{t('clinical.card3_title', '항바이러스 효과 (바실러스 서브틸리스)')}</span>
              </h3>
              <p className="text-slate-600 mb-6 leading-relaxed text-sm md:text-base font-normal">
                {t('clinical.card3_desc', 'DNG-1000의 핵심 균주인 Bacillus subtilis MORI가 생산하는 DNJ 성분의 바이러스 계통별 억제 효과입니다.')}
              </p>
              <div className="w-full overflow-x-auto rounded-2xl border border-slate-200 shadow-sm mb-6">
                <table className="w-full text-sm border-collapse table-fixed">
                  <colgroup>
                    <col style={{width: '32%'}} />
                    <col style={{width: '48%'}} />
                    <col style={{width: '20%'}} />
                  </colgroup>
                  <thead>
                    <tr className="bg-[#00513b] text-white">
                      <th className="px-1 py-3 text-center font-bold text-xs">{t('clinical.table3_col1', '바이러스 계통')}</th>
                      <th className="px-1 py-3 text-center font-bold text-xs">{t('clinical.table3_header', '대상 바이러스')}</th>
                      <th className="px-1 py-3 text-center font-bold text-xs">{t('clinical.table3_col3', '효과')}</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr className="border-b border-slate-100 hover:bg-emerald-50/50 transition-colors">
                      <td className="px-1 py-3 text-xs text-slate-500 break-words font-medium">Arteriviruses</td>
                      <td className="px-1 py-3 text-xs font-medium text-slate-700 break-words sm:break-keep">{t('clinical.table3_row1', 'PRRSV (돼지생식기호흡기증후군)')}</td>
                      <td className="px-1 py-3 text-center"><span className="inline-block bg-emerald-100 text-emerald-800 text-xs font-bold px-2 py-0.5 rounded-full whitespace-nowrap">{t('clinical.table3_effect', '효과 확인')}</span></td>
                    </tr>
                    <tr className="border-b border-slate-100 hover:bg-emerald-50/50 transition-colors">
                      <td className="px-1 py-3 text-xs text-slate-500 break-words font-medium">Orthomyxoviridae</td>
                      <td className="px-1 py-3 text-xs font-medium text-slate-700 break-words sm:break-keep">{t('clinical.table3_row2', '조류독감 A (AIV)')}</td>
                      <td className="px-1 py-3 text-center"><span className="inline-block bg-emerald-100 text-emerald-800 text-xs font-bold px-2 py-0.5 rounded-full whitespace-nowrap">{t('clinical.table3_effect', '효과 확인')}</span></td>
                    </tr>
                    <tr className="border-b border-slate-100 hover:bg-emerald-50/50 transition-colors">
                      <td className="px-1 py-3 text-xs text-slate-500 break-words font-medium">Pestiviruses</td>
                      <td className="px-1 py-3 text-xs font-medium text-slate-700 break-words sm:break-keep">{t('clinical.table3_row3', '소 바이러스성 설사병 (BVDV)')}</td>
                      <td className="px-1 py-3 text-center"><span className="inline-block bg-emerald-100 text-emerald-800 text-xs font-bold px-2 py-0.5 rounded-full whitespace-nowrap">{t('clinical.table3_effect', '효과 확인')}</span></td>
                    </tr>
                    <tr className="border-b border-slate-100 hover:bg-emerald-50/50 transition-colors">
                      <td className="px-1 py-3 text-xs text-slate-500 break-words font-medium">Bunyaviridae</td>
                      <td className="px-1 py-3 text-xs font-medium text-slate-700 break-words sm:break-keep">{t('clinical.table3_row4', '아카바네, 아이노 바이러스')}</td>
                      <td className="px-1 py-3 text-center"><span className="inline-block bg-emerald-100 text-emerald-800 text-xs font-bold px-2 py-0.5 rounded-full whitespace-nowrap">{t('clinical.table3_effect', '효과 확인')}</span></td>
                    </tr>
                    <tr className="hover:bg-emerald-50/50 transition-colors">
                      <td className="px-1 py-3 text-xs text-slate-500 break-words font-medium">Rhabdoviridae</td>
                      <td className="px-1 py-3 text-xs font-medium text-slate-700 break-words sm:break-keep">{t('clinical.table3_row5', '소유행열 바이러스 (BEF)')}</td>
                      <td className="px-1 py-3 text-center"><span className="inline-block bg-emerald-100 text-emerald-800 text-xs font-bold px-2 py-0.5 rounded-full whitespace-nowrap">{t('clinical.table3_effect', '효과 확인')}</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            {/* 하단 균형용 연구 요약 박스 */}
            <div className="bg-emerald-50/90 border border-emerald-200 rounded-2xl p-4 text-xs font-medium text-[#00513b] leading-relaxed shadow-sm flex flex-col gap-3">
              <div>
                <div className="flex items-start gap-1 mb-1">
                  <span className="font-bold text-sm shrink-0">🔬</span>
                  <span className="font-bold text-sm break-keep">{t('clinical.antiviralSummaryTitle', '항바이러스 학술 검증')}</span>
                </div>
                <p className="break-keep">{t('clinical.antiviralSummaryBody', 'DNG-1000 핵심 균주(Bacillus subtilis MORI)가 생산하는 DNJ 성분이 소, 돼지, 조류 등 주요 5대 바이러스 계통의 증식을 유의미하게 억제함을 입증하였습니다.')}</p>
              </div>
              <div className="pt-2.5 border-t border-emerald-200/80 flex flex-col sm:flex-row sm:items-start justify-between gap-2">
                <div className="flex items-start gap-1">
                  <span className="text-[11px] shrink-0">📚</span>
                  <span className="text-[11px] text-emerald-900 font-semibold break-keep">{t('clinical.paperRef2', '1-Deoxynojirimycin(DNJ) 학술 논문 및 글로벌 연구 자료')}</span>
                </div>
                <a
                  href="https://www.google.com/search?q=1-deoxynojirimycin+antiviral"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center justify-center gap-1.5 shrink-0 bg-[#00513b] hover:bg-[#003d2b] text-white text-[11px] font-bold px-3 py-1.5 rounded-xl transition-all shadow-sm hover:shadow-md hover:-translate-y-0.5"
                >
                  <span className="shrink-0">🔍</span>
                  <span className="break-keep">{t('clinical.searchGoogle', 'Google 학술 논문 검색')}</span>
                </a>
              </div>
            </div>
          </div>

          {/* Card 4: Expert Review Meeting Feedback */}
          <div className="bg-white p-4 sm:p-6 md:p-9 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-all duration-300 flex flex-col justify-between">
            <div>
              <h3 className="text-xl md:text-2xl font-black text-slate-800 mb-4 flex items-center gap-3 break-keep">
                <span className="w-9 h-9 rounded-full shrink-0 bg-[#00513b] text-white flex items-center justify-center text-sm font-bold shadow-md">4</span>
                <span>{t('clinical.card4_title', '전문가 리뷰 미팅 피드백')}</span>
              </h3>
              <p className="text-slate-600 mb-6 leading-relaxed text-sm md:text-base font-normal">
                {t('clinical.card4_desc', '몬스멕타는 현재 수의학계 전문가들과의 리뷰 미팅을 통해 임상 데이터를 검증받고 있습니다.')}
              </p>
              <div className="space-y-3.5">
                <div className="bg-gradient-to-r from-emerald-50/80 to-slate-50 p-4 rounded-2xl border-l-4 border-[#00513b] shadow-sm">
                  <p className="text-slate-700 italic font-medium text-xs md:text-sm leading-relaxed mb-2">{t('clinical.card4_quote1', '"1-Deoxynojirimycin(DNJ)의 여러 바이러스 억제 효과와 차별화된 유해물질 흡착력은 확실한 차별점입니다."')}</p>
                  <p className="text-xs font-bold text-emerald-900">— {t('clinical.card4_quote1_author', '박봉균 교수 (전 농림축산검역본부장, 바이러스학 분야 권위자)')}</p>
                </div>
                <div className="bg-gradient-to-r from-amber-50/80 to-slate-50 p-4 rounded-2xl border-l-4 border-amber-500 shadow-sm">
                  <p className="text-slate-700 italic font-medium text-xs md:text-sm leading-relaxed mb-2">{t('clinical.card4_quote4', '"인체에도 좋을 거 같은데..."')}</p>
                  <p className="text-xs font-bold text-amber-800">— {t('clinical.card4_quote4_author', '윤화영 교수 (전 서울대학교 수의과대학 내과학 교수 · 전 서울대 동물병원 내과과장)')}</p>
                </div>
                <div className="bg-gradient-to-r from-emerald-50/80 to-slate-50 p-4 rounded-2xl border-l-4 border-[#00513b] shadow-sm">
                  <p className="text-slate-700 italic font-medium text-xs md:text-sm leading-relaxed mb-2">{t('clinical.card4_quote2', '"입자도, 수분 흡수율, 비표면적... 수의사가 원하는 데이터를 다 갖췄습니다."')}</p>
                  <p className="text-xs font-bold text-emerald-900">— {t('clinical.card4_quote2_author', '정성대 원장 (동진동물병원)')}</p>
                </div>
                <div className="bg-gradient-to-r from-amber-50/80 to-slate-50 p-4 rounded-2xl border-l-4 border-amber-500 shadow-sm">
                  <p className="text-slate-700 italic font-medium text-xs md:text-sm leading-relaxed mb-2">{t('clinical.card4_quote3', '"단순 설사 치료를 넘어 구토·복통 환축도 잘 받아먹는 압도적 기호성과 즉각적 복통 완화로, 소화기 트러블 전체의 1차 상비·처방 보조제로 필수적입니다."')}</p>
                  <p className="text-xs font-bold text-amber-800">— {t('clinical.card4_quote3_author', '김동준 원장 (사랑동물병원 원장)')}</p>
                </div>
              </div>
            </div>
            
            <div className="mt-5 bg-amber-50/90 border border-amber-200 rounded-2xl p-4 shadow-sm">
              <p className="text-xs font-medium text-amber-900 leading-relaxed">📌 {t('clinical.card4_note', '몬스멕타의 학술·자문단은 (전)서울대학교 수의과대학 출신 등 수의학 전문가들로 구성되어 임상 데이터와 처방 기준을 철저히 검증하고 있습니다.')}</p>
            </div>
          </div>

        </div>
        ) : activeProduct === 'hepamax' ? (
        <div className="grid lg:grid-cols-2 gap-8 md:gap-10 animate-in fade-in zoom-in-95 duration-300">
          {/* Hepamax Card 1: Key Benefits */}
          <div className="bg-white p-4 sm:p-6 md:p-9 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-all duration-300 flex flex-col justify-between">
            <div>
              <h3 className="text-xl md:text-2xl font-black text-slate-800 mb-4 flex items-center gap-3 break-keep">
                <span className="w-9 h-9 rounded-full shrink-0 bg-amber-700 text-white flex items-center justify-center text-sm font-bold shadow-md">1</span>
                <span>간 건강 핵심 효능</span>
              </h3>
              <p className="text-slate-600 mb-6 leading-relaxed text-sm md:text-base font-normal">
                헤파맥스는 반려동물의 간 건강 개선 및 항병력 증진에 특화된 프리미엄 처방 솔루션입니다.
              </p>
              <div className="space-y-3.5">
                <div className="bg-amber-50 rounded-2xl p-4 border border-amber-200 hover:border-amber-400 transition-colors shadow-sm flex items-start gap-4">
                  <div className="w-10 h-10 bg-amber-100 text-amber-700 rounded-full flex items-center justify-center text-lg shrink-0 mt-0.5">🩺</div>
                  <div>
                    <h4 className="font-bold text-slate-800">간·담도계 질환 보조 치료</h4>
                    <p className="text-xs text-slate-500 mt-1 leading-relaxed">지방간(Hepatic lipidosis), 담관간염(Cholangiohepatitis) 등 간 기능 저하 개선 및 회복을 지원합니다.</p>
                  </div>
                </div>
                <div className="bg-amber-50 rounded-2xl p-4 border border-amber-200 hover:border-amber-400 transition-colors shadow-sm flex items-start gap-4">
                  <div className="w-10 h-10 bg-amber-100 text-amber-700 rounded-full flex items-center justify-center text-lg shrink-0 mt-0.5">🛡️</div>
                  <div>
                    <h4 className="font-bold text-slate-800">해독 작용 및 세포 재생</h4>
                    <p className="text-xs text-slate-500 mt-1 leading-relaxed">약물 장기 투약 후의 간 독성을 완화하고, 손상된 간세포의 빠른 재생을 촉진합니다.</p>
                  </div>
                </div>
                <div className="bg-amber-50 rounded-2xl p-4 border border-amber-200 hover:border-amber-400 transition-colors shadow-sm flex items-start gap-4">
                  <div className="w-10 h-10 bg-amber-100 text-amber-700 rounded-full flex items-center justify-center text-lg shrink-0 mt-0.5">⚡</div>
                  <div>
                    <h4 className="font-bold text-slate-800">활력 및 식욕 증진</h4>
                    <p className="text-xs text-slate-500 mt-1 leading-relaxed">간 기능 저하로 인한 식욕 부진을 완화하고 전반적인 활력(Vitality)을 강하게 끌어올립니다.</p>
                  </div>
                </div>
                <div className="bg-amber-50 rounded-2xl p-4 border border-amber-200 hover:border-amber-400 transition-colors shadow-sm flex items-start gap-4">
                  <div className="w-10 h-10 bg-amber-100 text-amber-700 rounded-full flex items-center justify-center text-lg shrink-0 mt-0.5">💧</div>
                  <div>
                    <h4 className="font-bold text-slate-800">소화 흡수 촉진</h4>
                    <p className="text-xs text-slate-500 mt-1 leading-relaxed">담즙 분비 정상화를 유도하여 지방 소화력 및 필수 영양분 흡수율을 대폭 향상시킵니다.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Hepamax Card 2: Ingredients */}
          <div className="bg-white p-4 sm:p-6 md:p-9 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-all duration-300 flex flex-col justify-between">
            <div>
              <h3 className="text-xl md:text-2xl font-black text-slate-800 mb-4 flex items-center gap-3 break-keep">
                <span className="w-9 h-9 rounded-full shrink-0 bg-amber-700 text-white flex items-center justify-center text-sm font-bold shadow-md">2</span>
                <span>핵심 성분 및 약리기전</span>
              </h3>
              <p className="text-slate-600 mb-6 leading-relaxed text-sm md:text-base font-normal">
                헤파맥스만의 5대 핵심 성분 독자 포뮬러는 강력한 시너지 효과를 통해 최적의 결과를 이끌어냅니다.
              </p>
              
              <div className="space-y-3">
                <div className="bg-slate-50 border border-slate-200 rounded-xl p-3 flex flex-col sm:flex-row sm:items-center gap-3 hover:bg-white hover:border-amber-300 transition-colors">
                  <div className="shrink-0 flex items-center gap-2 sm:w-1/3">
                    <span className="w-2 h-2 rounded-full bg-amber-500"></span>
                    <h5 className="font-bold text-slate-800 text-sm">D-Sorbitol <span className="text-amber-700 block text-xs">(D-소르비톨) 45g</span></h5>
                  </div>
                  <p className="text-xs text-slate-600 leading-relaxed sm:w-2/3 border-l-0 sm:border-l border-slate-200 sm:pl-3">
                    담즙 분비 촉진(Choleretic)을 통해 간/담도계 울체 해소 및 체내 독성 물질 배출을 지원합니다.
                  </p>
                </div>

                <div className="bg-slate-50 border border-slate-200 rounded-xl p-3 flex flex-col sm:flex-row sm:items-center gap-3 hover:bg-white hover:border-amber-300 transition-colors">
                  <div className="shrink-0 flex items-center gap-2 sm:w-1/3">
                    <span className="w-2 h-2 rounded-full bg-amber-500"></span>
                    <h5 className="font-bold text-slate-800 text-sm">Taurine <span className="text-amber-700 block text-xs">(타우린) 2,000mg</span></h5>
                  </div>
                  <p className="text-xs text-slate-600 leading-relaxed sm:w-2/3 border-l-0 sm:border-l border-slate-200 sm:pl-3">
                    담즙산 포합(Bile acid conjugation)의 필수 요소로, 간세포막 안정화 및 강력한 항산화·세포 보호 작용을 합니다.
                  </p>
                </div>

                <div className="bg-slate-50 border border-slate-200 rounded-xl p-3 flex flex-col sm:flex-row sm:items-center gap-3 hover:bg-white hover:border-amber-300 transition-colors">
                  <div className="shrink-0 flex items-center gap-2 sm:w-1/3">
                    <span className="w-2 h-2 rounded-full bg-amber-500"></span>
                    <h5 className="font-bold text-slate-800 text-sm">L-methionine <span className="text-amber-700 block text-xs">(L-메티오닌) 300mg</span></h5>
                  </div>
                  <p className="text-xs text-slate-600 leading-relaxed sm:w-2/3 border-l-0 sm:border-l border-slate-200 sm:pl-3">
                    대표적 항지방간(Lipotropic) 물질이자, 강력한 간 해독 물질인 글루타치온(Glutathione)의 생합성 전구체입니다.
                  </p>
                </div>

                <div className="bg-slate-50 border border-slate-200 rounded-xl p-3 flex flex-col sm:flex-row sm:items-center gap-3 hover:bg-white hover:border-amber-300 transition-colors">
                  <div className="shrink-0 flex items-center gap-2 sm:w-1/3">
                    <span className="w-2 h-2 rounded-full bg-amber-500"></span>
                    <h5 className="font-bold text-slate-800 text-sm">L-lysine HCl <span className="text-amber-700 block text-xs">(L-라이신) 300mg</span></h5>
                  </div>
                  <p className="text-xs text-slate-600 leading-relaxed sm:w-2/3 border-l-0 sm:border-l border-slate-200 sm:pl-3">
                    간내 단백질 합성을 보조하고 면역 체계를 강하게 지원하는 필수 아미노산입니다.
                  </p>
                </div>

                <div className="bg-slate-50 border border-slate-200 rounded-xl p-3 flex flex-col sm:flex-row sm:items-center gap-3 hover:bg-white hover:border-amber-300 transition-colors">
                  <div className="shrink-0 flex items-center gap-2 sm:w-1/3">
                    <span className="w-2 h-2 rounded-full bg-amber-500"></span>
                    <h5 className="font-bold text-slate-800 text-sm">Vitamin B12 <span className="text-amber-700 block text-xs">(비타민 B12) 1,000μg</span></h5>
                  </div>
                  <p className="text-xs text-slate-600 leading-relaxed sm:w-2/3 border-l-0 sm:border-l border-slate-200 sm:pl-3">
                    간 손상 및 만성 소화기 질환 시 고갈되는 조효소로, 간세포 재생 및 에너지 대사를 촉진합니다.
                  </p>
                </div>
              </div>
            </div>
            
            <div className="mt-5 bg-amber-50/90 border border-amber-200 rounded-2xl p-4 text-xs font-medium text-amber-900 leading-relaxed shadow-sm">
              <p className="font-bold mb-1">📌 S&J 동물병원 자문단 코멘트:</p>
              <p>"간 수치 저하와 기력 회복에 확실한 포커스를 둔 배합입니다. 처방과 함께 병행 시 눈에 띄는 활력 개선을 확인하실 수 있습니다."</p>
            </div>
          </div>
        </div>
        ) : activeProduct === 'urinary' ? (
        <div className="grid lg:grid-cols-2 gap-8 md:gap-10 animate-in fade-in zoom-in-95 duration-300">
          {/* Urinary Card 1: Key Benefits */}
          <div className="bg-white p-4 sm:p-6 md:p-9 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-all duration-300 flex flex-col justify-between">
            <div>
              <h3 className="text-xl md:text-2xl font-black text-slate-800 mb-4 flex items-center gap-3 break-keep">
                <span className="w-9 h-9 rounded-full shrink-0 bg-indigo-700 text-white flex items-center justify-center text-sm font-bold shadow-md">1</span>
                <span>요독 흡착 및 비뇨기 핵심 효능</span>
              </h3>
              <p className="text-slate-600 mb-6 leading-relaxed text-sm md:text-base font-normal">
                유리너리는 요독증 완화와 활력 증진을 위해 설계된 비뇨기/신장 특화 처방 솔루션입니다.
              </p>
              <div className="space-y-3.5">
                <div className="bg-indigo-50 rounded-2xl p-4 border border-indigo-200 hover:border-indigo-400 transition-colors shadow-sm flex items-start gap-4">
                  <div className="w-10 h-10 bg-indigo-100 text-indigo-700 rounded-full flex items-center justify-center text-lg shrink-0 mt-0.5">🧲</div>
                  <div>
                    <h4 className="font-bold text-slate-800">강력한 요독 흡착 배출</h4>
                    <p className="text-xs text-slate-500 mt-1 leading-relaxed">몬모릴로나이트의 양이온 교환 능력으로 요소(Urea)와 인독실설페이트(Indoxyl Sulfate)를 강력하게 흡착하여 배출합니다.</p>
                  </div>
                </div>
                <div className="bg-indigo-50 rounded-2xl p-4 border border-indigo-200 hover:border-indigo-400 transition-colors shadow-sm flex items-start gap-4">
                  <div className="w-10 h-10 bg-indigo-100 text-indigo-700 rounded-full flex items-center justify-center text-lg shrink-0 mt-0.5">🩺</div>
                  <div>
                    <h4 className="font-bold text-slate-800">신장 기능 저하 보조</h4>
                    <p className="text-xs text-slate-500 mt-1 leading-relaxed">요독의 장내 배출을 통해 신장 수치를 안정화하고 만성 신부전 환축의 요독증 완화에 기여합니다.</p>
                  </div>
                </div>
                <div className="bg-indigo-50 rounded-2xl p-4 border border-indigo-200 hover:border-indigo-400 transition-colors shadow-sm flex items-start gap-4">
                  <div className="w-10 h-10 bg-indigo-100 text-indigo-700 rounded-full flex items-center justify-center text-lg shrink-0 mt-0.5">⚡</div>
                  <div>
                    <h4 className="font-bold text-slate-800">활력 증진 및 영양 공급</h4>
                    <p className="text-xs text-slate-500 mt-1 leading-relaxed">아디세오 비고비솔의 비타민 A, D3, E, B군 등이 신장 질환 시 부족해지기 쉬운 에너지를 대사하고 항산화 효과를 제공합니다.</p>
                  </div>
                </div>
                
                {/* Google Reference Button in Card 1 */}
                <div className="mt-4 p-4 bg-indigo-100/50 rounded-2xl border border-indigo-200">
                  <div className="flex flex-col sm:flex-row items-center justify-between gap-3">
                    <p className="text-xs font-bold text-indigo-900 break-keep">💡 몬모릴로나이트 요독 흡착 학술 검증 (Urea & Indoxyl Sulfate)</p>
                    <a
                      href="https://scholar.google.com/scholar?q=Montmorillonite+Urea+Indoxyl+Sulfate+adsorption"
                      target="_blank"
                      rel="noopener noreferrer"
                      className="inline-flex items-center justify-center gap-1.5 shrink-0 bg-indigo-700 hover:bg-indigo-900 text-white text-[11px] font-bold px-3 py-1.5 rounded-xl transition-all shadow-sm"
                    >
                      <span className="shrink-0">🔍</span>
                      <span className="break-keep">구글 학술 논문 검색</span>
                    </a>
                  </div>
                </div>

              </div>
            </div>
          </div>

          {/* Urinary Card 2: Ingredients */}
          <div className="bg-white p-4 sm:p-6 md:p-9 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-all duration-300 flex flex-col justify-between">
            <div>
              <h3 className="text-xl md:text-2xl font-black text-slate-800 mb-4 flex items-center gap-3 break-keep">
                <span className="w-9 h-9 rounded-full shrink-0 bg-indigo-700 text-white flex items-center justify-center text-sm font-bold shadow-md">2</span>
                <span>핵심 성분 및 약리기전</span>
              </h3>
              <p className="text-slate-600 mb-6 leading-relaxed text-sm md:text-base font-normal">
                몬모릴로나이트와 아디세오 비고비솔의 독자적인 시너지 포뮬러입니다.
              </p>
              
              <div className="space-y-3">
                <div className="bg-slate-50 border border-slate-200 rounded-xl p-3 flex flex-col sm:flex-row sm:items-center gap-3 hover:bg-white hover:border-indigo-300 transition-colors">
                  <div className="shrink-0 flex flex-col gap-1 sm:w-1/3">
                    <div className="flex items-center gap-2">
                      <span className="w-2 h-2 rounded-full bg-indigo-500"></span>
                      <h5 className="font-bold text-slate-800 text-sm">Montmorillonite</h5>
                    </div>
                    <span className="text-indigo-700 text-xs font-bold">(몬모릴로나이트 흡착제)</span>
                  </div>
                  <p className="text-xs text-slate-600 leading-relaxed sm:w-2/3 border-l-0 sm:border-l border-slate-200 sm:pl-3">
                    비표면적 800m²/g 이상의 나노 몬모릴로나이트가 장내에서 요소(Urea) 및 단백질 결합성 요독인 인독실설페이트(Indoxyl Sulfate)를 수소 결합과 정전기적 척력 변형으로 강력하게 트랩(Trap)하여 체외 배설을 돕습니다.
                  </p>
                </div>

                <div className="bg-slate-50 border border-slate-200 rounded-xl p-3 flex flex-col sm:flex-row sm:items-center gap-3 hover:bg-white hover:border-indigo-300 transition-colors">
                  <div className="shrink-0 flex flex-col gap-1 sm:w-1/3">
                    <div className="flex items-center gap-2">
                      <span className="w-2 h-2 rounded-full bg-indigo-500"></span>
                      <h5 className="font-bold text-slate-800 text-sm">Adisseo Vigovisol</h5>
                    </div>
                    <span className="text-indigo-700 text-xs font-bold">(글로벌 아디세오 프리미엄 비타민)</span>
                  </div>
                  <p className="text-xs text-slate-600 leading-relaxed sm:w-2/3 border-l-0 sm:border-l border-slate-200 sm:pl-3">
                    세계적인 사료첨가제 기업 아디세오(Adisseo)의 액상 종합 비타민으로, 활력 증진 및 에너지 대사에 필수적인 영양을 공급합니다. (Vit A 400만IU, D3 80만IU, E 2천IU, B군, C, K3 복합 배합)
                  </p>
                </div>
              </div>
            </div>
            
            <div className="mt-5 bg-indigo-50/90 border border-indigo-200 rounded-2xl p-4 text-xs font-medium text-indigo-900 leading-relaxed shadow-sm">
              <p className="font-bold mb-1">📌 S&J 동물병원 자문단 코멘트:</p>
              <p>"요독 흡착과 신장 질환 시 떨어지기 쉬운 활력을 돕는 비타민 복합체 배합으로 만성 신부전 환축의 삶의 질 향상에 탁월한 보조제가 될 것입니다."</p>
            </div>
          </div>
        </div>
        ) : activeProduct === 'probiotics' ? (
        <div className="grid lg:grid-cols-2 gap-8 md:gap-10 animate-in fade-in zoom-in-95 duration-300">
          {/* Probiotics Card 1: Key Benefits */}
          <div className="bg-white p-4 sm:p-6 md:p-9 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-all duration-300 flex flex-col justify-between">
            <div>
              <h3 className="text-xl md:text-2xl font-black text-slate-800 mb-4 flex items-center gap-3 break-keep">
                <span className="w-9 h-9 rounded-full shrink-0 bg-blue-700 text-white flex items-center justify-center text-sm font-bold shadow-md">1</span>
                <span>장 건강 핵심 효능</span>
              </h3>
              <p className="text-slate-600 mb-6 leading-relaxed text-sm md:text-base font-normal">
                프로바이오틱스는 몬스멕타 고유의 장내 유해물질 흡착 배출 능력에 세계적인 듀퐁(Danisco)사의 100억 생유산균을 더한 장 건강 특화 솔루션입니다.
              </p>
              <div className="space-y-3.5">
                <div className="bg-blue-50 rounded-2xl p-4 border border-blue-200 hover:border-blue-400 transition-colors shadow-sm flex items-start gap-4">
                  <div className="w-10 h-10 bg-blue-100 text-blue-700 rounded-full flex items-center justify-center text-lg shrink-0 mt-0.5">🛡️</div>
                  <div>
                    <h4 className="font-bold text-slate-800">장내 유해물질 흡착 배출</h4>
                    <p className="text-xs text-slate-500 mt-1 leading-relaxed">나노 몬모릴로나이트가 설사 원인균과 독소, 바이러스를 안전하게 흡착하여 배출합니다.</p>
                  </div>
                </div>
                <div className="bg-blue-50 rounded-2xl p-4 border border-blue-200 hover:border-blue-400 transition-colors shadow-sm flex items-start gap-4">
                  <div className="w-10 h-10 bg-blue-100 text-blue-700 rounded-full flex items-center justify-center text-lg shrink-0 mt-0.5">🦠</div>
                  <div>
                    <h4 className="font-bold text-slate-800">유익균 증식 및 장내 환경 정상화</h4>
                    <p className="text-xs text-slate-500 mt-1 leading-relaxed">프리미엄 100억 생유산균이 유해균 억제와 유익균 증식을 도와 붕괴된 장내 환경을 빠르게 정상화합니다.</p>
                  </div>
                </div>
                <div className="bg-blue-50 rounded-2xl p-4 border border-blue-200 hover:border-blue-400 transition-colors shadow-sm flex items-start gap-4">
                  <div className="w-10 h-10 bg-blue-100 text-blue-700 rounded-full flex items-center justify-center text-lg shrink-0 mt-0.5">✨</div>
                  <div>
                    <h4 className="font-bold text-slate-800">세계 최고 수준의 생존력</h4>
                    <p className="text-xs text-slate-500 mt-1 leading-relaxed">글로벌 듀퐁(Danisco)사의 검증된 균주 배양 기술로 위산과 담즙산에 강해 장까지 안전하게 도달합니다.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Probiotics Card 2: Ingredients */}
          <div className="bg-white p-4 sm:p-6 md:p-9 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-all duration-300 flex flex-col justify-between">
            <div>
              <h3 className="text-xl md:text-2xl font-black text-slate-800 mb-4 flex items-center gap-3 break-keep">
                <span className="w-9 h-9 rounded-full shrink-0 bg-blue-700 text-white flex items-center justify-center text-sm font-bold shadow-md">2</span>
                <span>핵심 성분 및 약리기전</span>
              </h3>
              <p className="text-slate-600 mb-6 leading-relaxed text-sm md:text-base font-normal">
                압도적인 흡착제와 글로벌 프리미엄 유산균의 이상적인 배합입니다.
              </p>
              
              <div className="space-y-3">
                <div className="bg-slate-50 border border-slate-200 rounded-xl p-3 flex flex-col sm:flex-row sm:items-center gap-3 hover:bg-white hover:border-blue-300 transition-colors">
                  <div className="shrink-0 flex items-center gap-2 sm:w-1/3">
                    <span className="w-2 h-2 rounded-full bg-blue-500"></span>
                    <h5 className="font-bold text-slate-800 text-sm">Montmorillonite <span className="text-blue-700 block text-xs">(나노 몬모릴로나이트) 90%</span></h5>
                  </div>
                  <p className="text-xs text-slate-600 leading-relaxed sm:w-2/3 border-l-0 sm:border-l border-slate-200 sm:pl-3">
                    비표면적이 극대화된 몬스멕타 고순도 원료가 장내 염증 산물과 독소를 1차적으로 깨끗하게 비워냅니다.
                  </p>
                </div>

                <div className="bg-slate-50 border border-slate-200 rounded-xl p-3 flex flex-col sm:flex-row sm:items-center gap-3 hover:bg-white hover:border-blue-300 transition-colors">
                  <div className="shrink-0 flex items-center gap-2 sm:w-1/3">
                    <span className="w-2 h-2 rounded-full bg-blue-500"></span>
                    <h5 className="font-bold text-slate-800 text-sm">Danisco Probiotics <span className="text-blue-700 block text-xs">(듀퐁 100억 생유산균) 10%</span></h5>
                  </div>
                  <p className="text-xs text-slate-600 leading-relaxed sm:w-2/3 border-l-0 sm:border-l border-slate-200 sm:pl-3">
                    세계적으로 유명한 듀퐁(Danisco)사의 검증된 프리미엄 생유산균을 적용하여, 뛰어난 장 정착력과 마이크로바이옴 복원 능력을 발휘합니다.
                  </p>
                </div>
              </div>
            </div>
            
            <div className="mt-5 bg-blue-50/90 border border-blue-200 rounded-2xl p-4 text-xs font-medium text-blue-900 leading-relaxed shadow-sm">
              <p className="font-bold mb-1">📌 S&J 동물병원 자문단 코멘트:</p>
              <p>"비워내고(몬모릴로나이트), 채워주는(듀퐁 생유산균) 가장 이상적인 장 트러블 보조제입니다. 설사 환축에게 따로 유산균을 먹일 필요가 없어 보호자 순응도가 매우 뛰어납니다."</p>
            </div>
          </div>
        </div>
        ) : activeProduct === 'heartcare' ? (
        <div className="grid lg:grid-cols-2 gap-8 md:gap-10 animate-in fade-in zoom-in-95 duration-300">
          {/* Heartcare Card 1: Key Benefits */}
          <div className="bg-white p-4 sm:p-6 md:p-9 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-all duration-300 flex flex-col justify-between">
            <div>
              <h3 className="text-xl md:text-2xl font-black text-slate-800 mb-4 flex items-center gap-3 break-keep">
                <span className="w-9 h-9 rounded-full shrink-0 bg-red-700 text-white flex items-center justify-center text-sm font-bold shadow-md">1</span>
                <span>심장 및 혈행 핵심 효능</span>
              </h3>
              <p className="text-slate-600 mb-6 leading-relaxed text-sm md:text-base font-normal">
                하트케어는 코큐텐(Q10)·산사나무 열매 추출물·L-카르니틴·타우린·오메가3를 배합한 심장/혈행 특화 처방 솔루션입니다.
              </p>
              <div className="space-y-3.5">
                <div className="bg-red-50 rounded-2xl p-4 border border-red-200 hover:border-red-400 transition-colors shadow-sm flex items-start gap-4">
                  <div className="w-10 h-10 bg-red-100 text-red-700 rounded-full flex items-center justify-center text-lg shrink-0 mt-0.5">❤️</div>
                  <div>
                    <h4 className="font-bold text-slate-800">심장 근육 수축력 강화</h4>
                    <p className="text-xs text-slate-500 mt-1 leading-relaxed">코큐텐(Q10)이 심근세포의 에너지(ATP) 생성을 촉진하여 심박출량 및 수축력을 강화합니다.</p>
                  </div>
                </div>
                <div className="bg-red-50 rounded-2xl p-4 border border-red-200 hover:border-red-400 transition-colors shadow-sm flex items-start gap-4">
                  <div className="w-10 h-10 bg-red-100 text-red-700 rounded-full flex items-center justify-center text-lg shrink-0 mt-0.5">🩸</div>
                  <div>
                    <h4 className="font-bold text-slate-800">혈전 예방 및 혈류 개선</h4>
                    <p className="text-xs text-slate-500 mt-1 leading-relaxed">오메가3가 혈중 중성지방을 낮추고 혈소판 응집을 억제하여 혈행을 원활하게 개선합니다.</p>
                  </div>
                </div>
                <div className="bg-red-50 rounded-2xl p-4 border border-red-200 hover:border-red-400 transition-colors shadow-sm flex items-start gap-4">
                  <div className="w-10 h-10 bg-red-100 text-red-700 rounded-full flex items-center justify-center text-lg shrink-0 mt-0.5">📉</div>
                  <div>
                    <h4 className="font-bold text-slate-800">혈압 정상화 보조</h4>
                    <p className="text-xs text-slate-500 mt-1 leading-relaxed">산사나무 열매 추출물이 관상동맥을 확장하여 혈압을 안정화하고 심장 부담을 덜어줍니다.</p>
                  </div>
                </div>
                <div className="bg-red-50 rounded-2xl p-4 border border-red-200 hover:border-red-400 transition-colors shadow-sm flex items-start gap-4">
                  <div className="w-10 h-10 bg-red-100 text-red-700 rounded-full flex items-center justify-center text-lg shrink-0 mt-0.5">⚡</div>
                  <div>
                    <h4 className="font-bold text-slate-800">심부전 진행 지연 보조</h4>
                    <p className="text-xs text-slate-500 mt-1 leading-relaxed">타우린의 심근 보호 작용과 L-카르니틴의 에너지 대사 지원으로 만성 심부전 환축의 삶의 질 유지를 돕습니다.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Heartcare Card 2: Ingredients */}
          <div className="bg-white p-4 sm:p-6 md:p-9 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-all duration-300 flex flex-col justify-between">
            <div>
              <h3 className="text-xl md:text-2xl font-black text-slate-800 mb-4 flex items-center gap-3 break-keep">
                <span className="w-9 h-9 rounded-full shrink-0 bg-red-700 text-white flex items-center justify-center text-sm font-bold shadow-md">2</span>
                <span>핵심 성분 및 약리기전</span>
              </h3>
              <p className="text-slate-600 mb-6 leading-relaxed text-sm md:text-base font-normal">
                5대 핵심 성분을 배합비중에 따라 정량 배합한 하트케어 독자 포뮬러입니다. (1L 기준, 각 25,000mg)
              </p>
              
              <div className="space-y-3">
                <div className="bg-slate-50 border border-slate-200 rounded-xl p-3 flex flex-col sm:flex-row sm:items-center gap-3 hover:bg-white hover:border-red-300 transition-colors">
                  <div className="shrink-0 flex items-center gap-2 sm:w-2/5">
                    <span className="w-2 h-2 rounded-full bg-red-500"></span>
                    <h5 className="font-bold text-slate-800 text-sm">Coenzyme Q10 <span className="text-red-700 block text-xs">(코큐텐) 20%</span></h5>
                  </div>
                  <p className="text-xs text-slate-600 leading-relaxed sm:w-3/5 border-l-0 sm:border-l border-slate-200 sm:pl-3">
                    심근세포 미토콘드리아의 에너지(ATP) 생성을 돕고, 노화·심부전 시 급감하는 Q10을 보충하여 심장 수축력을 강화합니다.
                  </p>
                </div>

                <div className="bg-slate-50 border border-slate-200 rounded-xl p-3 flex flex-col sm:flex-row sm:items-center gap-3 hover:bg-white hover:border-red-300 transition-colors">
                  <div className="shrink-0 flex items-center gap-2 sm:w-2/5">
                    <span className="w-2 h-2 rounded-full bg-red-500"></span>
                    <h5 className="font-bold text-slate-800 text-sm">Hawthorn Extract <span className="text-red-700 block text-xs">(산사나무 열매 추출물) 10%</span></h5>
                  </div>
                  <p className="text-xs text-slate-600 leading-relaxed sm:w-3/5 border-l-0 sm:border-l border-slate-200 sm:pl-3">
                    관상동맥을 확장하여 심장 혈류를 늘리고, 혈압을 안정화하여 심장 부담을 경감시킵니다.
                  </p>
                </div>

                <div className="bg-slate-50 border border-slate-200 rounded-xl p-3 flex flex-col sm:flex-row sm:items-center gap-3 hover:bg-white hover:border-red-300 transition-colors">
                  <div className="shrink-0 flex items-center gap-2 sm:w-2/5">
                    <span className="w-2 h-2 rounded-full bg-red-500"></span>
                    <h5 className="font-bold text-slate-800 text-sm">L-Carnitine <span className="text-red-700 block text-xs">(L-카르니틴) 10%</span></h5>
                  </div>
                  <p className="text-xs text-slate-600 leading-relaxed sm:w-3/5 border-l-0 sm:border-l border-slate-200 sm:pl-3">
                    지방산을 미토콘드리아로 운반해 심장의 핵심 에너지원을 공급하고 심근 대사를 활성화합니다.
                  </p>
                </div>

                <div className="bg-slate-50 border border-slate-200 rounded-xl p-3 flex flex-col sm:flex-row sm:items-center gap-3 hover:bg-white hover:border-red-300 transition-colors">
                  <div className="shrink-0 flex items-center gap-2 sm:w-2/5">
                    <span className="w-2 h-2 rounded-full bg-red-500"></span>
                    <h5 className="font-bold text-slate-800 text-sm">Taurine <span className="text-red-700 block text-xs">(타우린) 5%</span></h5>
                  </div>
                  <p className="text-xs text-slate-600 leading-relaxed sm:w-3/5 border-l-0 sm:border-l border-slate-200 sm:pl-3">
                    심근 세포막을 안정화하고 칼슘 항상성을 유지하여 확장성 심근병증(DCM) 진행을 지연시킵니다.
                  </p>
                </div>

                <div className="bg-slate-50 border border-slate-200 rounded-xl p-3 flex flex-col sm:flex-row sm:items-center gap-3 hover:bg-white hover:border-red-300 transition-colors">
                  <div className="shrink-0 flex items-center gap-2 sm:w-2/5">
                    <span className="w-2 h-2 rounded-full bg-red-500"></span>
                    <h5 className="font-bold text-slate-800 text-sm">Omega-3 EPA/DHA <span className="text-red-700 block text-xs">(오메가3) 5%</span></h5>
                  </div>
                  <p className="text-xs text-slate-600 leading-relaxed sm:w-3/5 border-l-0 sm:border-l border-slate-200 sm:pl-3">
                    혈중 중성지방을 낮추고 항염 작용으로 혈관 건강과 혈행 개선을 돕습니다.
                  </p>
                </div>
              </div>
            </div>
            
            <div className="mt-5 bg-red-50/90 border border-red-200 rounded-2xl p-4 text-xs font-medium text-red-900 leading-relaxed shadow-sm">
              <p className="font-bold mb-1">📌 S&J 동물병원 자문단 코멘트:</p>
              <p>"Q10·타우린·오메가3의 삼각 포뮬러로 심부전 환축의 에너지 공급과 혈행 개선을 동시에 지원합니다. 심초음파 수치 개선에 도움이 되는 배합입니다."</p>
            </div>
          </div>
        </div>
        ) : activeProduct === 'jointcare' ? (
        <div className="grid lg:grid-cols-2 gap-8 md:gap-10 animate-in fade-in zoom-in-95 duration-300">
          {/* Jointcare Card 1: Key Benefits */}
          <div className="bg-white p-4 sm:p-6 md:p-9 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-all duration-300 flex flex-col justify-between">
            <div>
              <h3 className="text-xl md:text-2xl font-black text-slate-800 mb-4 flex items-center gap-3 break-keep">
                <span className="w-9 h-9 rounded-full shrink-0 bg-blue-700 text-white flex items-center justify-center text-sm font-bold shadow-md">1</span>
                <span>관절 및 연골 핵심 효능</span>
              </h3>
              <p className="text-slate-600 mb-6 leading-relaxed text-sm md:text-base font-normal">
                조인트케어는 MSM·그린립 머슬 추출물·보스웰리아·콘드로이친·오메가3를 배합한 관절/연골 특화 처방 솔루션입니다.
              </p>
              <div className="space-y-3.5">
                <div className="bg-blue-50 rounded-2xl p-4 border border-blue-200 hover:border-blue-400 transition-colors shadow-sm flex items-start gap-4">
                  <div className="w-10 h-10 bg-blue-100 text-blue-700 rounded-full flex items-center justify-center text-lg shrink-0 mt-0.5">🦴</div>
                  <div>
                    <h4 className="font-bold text-slate-800">관절 연골 영양 공급</h4>
                    <p className="text-xs text-slate-500 mt-1 leading-relaxed">MSM(식이유황)이 연골 및 결합조직의 재생에 필요한 황을 공급하여 연골 구조를 유지합니다.</p>
                  </div>
                </div>
                <div className="bg-blue-50 rounded-2xl p-4 border border-blue-200 hover:border-blue-400 transition-colors shadow-sm flex items-start gap-4">
                  <div className="w-10 h-10 bg-blue-100 text-blue-700 rounded-full flex items-center justify-center text-lg shrink-0 mt-0.5">🌿</div>
                  <div>
                    <h4 className="font-bold text-slate-800">관절 염증 및 통증 완화</h4>
                    <p className="text-xs text-slate-500 mt-1 leading-relaxed">보스웰리아가 염증 매개 물질(5-LOX 경로)을 억제하고, 그린립 머슬의 오메가3가 관절 항염을 도와 통증을 경감시킵니다.</p>
                  </div>
                </div>
                <div className="bg-blue-50 rounded-2xl p-4 border border-blue-200 hover:border-blue-400 transition-colors shadow-sm flex items-start gap-4">
                  <div className="w-10 h-10 bg-blue-100 text-blue-700 rounded-full flex items-center justify-center text-lg shrink-0 mt-0.5">💧</div>
                  <div>
                    <h4 className="font-bold text-slate-800">관절 윤활액 증가 보조</h4>
                    <p className="text-xs text-slate-500 mt-1 leading-relaxed">콘드로이친이 활액과 연골의 수분 보유력을 높여 관절 움직임을 부드럽게 합니다.</p>
                  </div>
                </div>
                <div className="bg-blue-50 rounded-2xl p-4 border border-blue-200 hover:border-blue-400 transition-colors shadow-sm flex items-start gap-4">
                  <div className="w-10 h-10 bg-blue-100 text-blue-700 rounded-full flex items-center justify-center text-lg shrink-0 mt-0.5">⏳</div>
                  <div>
                    <h4 className="font-bold text-slate-800">관절염 진행 지연</h4>
                    <p className="text-xs text-slate-500 mt-1 leading-relaxed">연골 분해 효소(MMP) 활성을 억제하여 골관절염 환축의 관절 퇴행 속도를 늦춥니다.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Jointcare Card 2: Ingredients */}
          <div className="bg-white p-4 sm:p-6 md:p-9 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-all duration-300 flex flex-col justify-between">
            <div>
              <h3 className="text-xl md:text-2xl font-black text-slate-800 mb-4 flex items-center gap-3 break-keep">
                <span className="w-9 h-9 rounded-full shrink-0 bg-blue-700 text-white flex items-center justify-center text-sm font-bold shadow-md">2</span>
                <span>핵심 성분 및 약리기전</span>
              </h3>
              <p className="text-slate-600 mb-6 leading-relaxed text-sm md:text-base font-normal">
                5대 핵심 성분을 배합비중에 따라 정량 배합한 조인트케어 독자 포뮬러입니다. (1L 기준, 각 25,000mg)
              </p>
              
              <div className="space-y-3">
                <div className="bg-slate-50 border border-slate-200 rounded-xl p-3 flex flex-col sm:flex-row sm:items-center gap-3 hover:bg-white hover:border-blue-300 transition-colors">
                  <div className="shrink-0 flex items-center gap-2 sm:w-2/5">
                    <span className="w-2 h-2 rounded-full bg-blue-500"></span>
                    <h5 className="font-bold text-slate-800 text-sm">MSM <span className="text-blue-700 block text-xs">(식이유황) 20%</span></h5>
                  </div>
                  <p className="text-xs text-slate-600 leading-relaxed sm:w-3/5 border-l-0 sm:border-l border-slate-200 sm:pl-3">
                    관절·연골·결합조직 구성에 필수적인 유기 황을 공급하여 연골 재생을 돕고 관절 경직과 통증을 완화합니다.
                  </p>
                </div>

                <div className="bg-slate-50 border border-slate-200 rounded-xl p-3 flex flex-col sm:flex-row sm:items-center gap-3 hover:bg-white hover:border-blue-300 transition-colors">
                  <div className="shrink-0 flex items-center gap-2 sm:w-2/5">
                    <span className="w-2 h-2 rounded-full bg-blue-500"></span>
                    <h5 className="font-bold text-slate-800 text-sm">Green Lipped Mussel Extract <span className="text-blue-700 block text-xs">(그린립 머슬 추출물) 10%</span></h5>
                  </div>
                  <p className="text-xs text-slate-600 leading-relaxed sm:w-3/5 border-l-0 sm:border-l border-slate-200 sm:pl-3">
                    뉴질랜드 청색홍합의 오메가3·글루코사민·연골보호 글리코아미노글리칸이 관절 윤활 및 항염 작용을 돕습니다.
                  </p>
                </div>

                <div className="bg-slate-50 border border-slate-200 rounded-xl p-3 flex flex-col sm:flex-row sm:items-center gap-3 hover:bg-white hover:border-blue-300 transition-colors">
                  <div className="shrink-0 flex items-center gap-2 sm:w-2/5">
                    <span className="w-2 h-2 rounded-full bg-blue-500"></span>
                    <h5 className="font-bold text-slate-800 text-sm">Boswellia <span className="text-blue-700 block text-xs">(보스웰리아) 10%</span></h5>
                  </div>
                  <p className="text-xs text-slate-600 leading-relaxed sm:w-3/5 border-l-0 sm:border-l border-slate-200 sm:pl-3">
                    보스웰릭산이 류코트리엔 합성을 억제하여 관절 염증과 통증을 천연 방식으로 완화합니다.
                  </p>
                </div>

                <div className="bg-slate-50 border border-slate-200 rounded-xl p-3 flex flex-col sm:flex-row sm:items-center gap-3 hover:bg-white hover:border-blue-300 transition-colors">
                  <div className="shrink-0 flex items-center gap-2 sm:w-2/5">
                    <span className="w-2 h-2 rounded-full bg-blue-500"></span>
                    <h5 className="font-bold text-slate-800 text-sm">Chondroitin <span className="text-blue-700 block text-xs">(콘드로이친) 5%</span></h5>
                  </div>
                  <p className="text-xs text-slate-600 leading-relaxed sm:w-3/5 border-l-0 sm:border-l border-slate-200 sm:pl-3">
                    연골 기질의 핵심 구성 성분으로 윤활액 생성을 늘리고 연골 분해 효소를 억제합니다.
                  </p>
                </div>

                <div className="bg-slate-50 border border-slate-200 rounded-xl p-3 flex flex-col sm:flex-row sm:items-center gap-3 hover:bg-white hover:border-blue-300 transition-colors">
                  <div className="shrink-0 flex items-center gap-2 sm:w-2/5">
                    <span className="w-2 h-2 rounded-full bg-blue-500"></span>
                    <h5 className="font-bold text-slate-800 text-sm">Omega-3 EPA/DHA <span className="text-blue-700 block text-xs">(오메가3) 5%</span></h5>
                  </div>
                  <p className="text-xs text-slate-600 leading-relaxed sm:w-3/5 border-l-0 sm:border-l border-slate-200 sm:pl-3">
                    전신 항염 작용으로 관절의 만성 염증 상태를 완화하고 연골 보호를 돕습니다.
                  </p>
                </div>
              </div>
            </div>
            
            <div className="mt-5 bg-blue-50/90 border border-blue-200 rounded-2xl p-4 text-xs font-medium text-blue-900 leading-relaxed shadow-sm">
              <p className="font-bold mb-1">📌 S&J 동물병원 자문단 코멘트:</p>
              <p>"연골 재생(MSM·콘드로이친), 관절 항염(보스웰리아·오메가3), 윤활(그린립 머슬)을 한 병에 담은 종합 관절 솔루션입니다. 노령견 퇴행성 관절염 관리에 추천하는 배합입니다."</p>
            </div>
          </div>
        </div>
        ) : activeProduct === 'powerase' ? (
        <div className="grid lg:grid-cols-2 gap-8 md:gap-10 animate-in fade-in zoom-in-95 duration-300">
          {/* Powerase Card 1: Key Benefits */}
          <div className="bg-white p-4 sm:p-6 md:p-9 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-all duration-300 flex flex-col justify-between">
            <div>
              <h3 className="text-xl md:text-2xl font-black text-slate-800 mb-4 flex items-center gap-3 break-keep">
                <span className="w-9 h-9 rounded-full shrink-0 bg-orange-700 text-white flex items-center justify-center text-sm font-bold shadow-md">1</span>
                <span>기력·활력 핵심 효능</span>
              </h3>
              <p className="text-slate-600 mb-6 leading-relaxed text-sm md:text-base font-normal">
                파워라제는 엔도 프로테아제·알파 아밀라제·라이페이스 3대 소화 효소를 배합한 소화/활력 특화 처방 솔루션입니다.
              </p>
              <div className="space-y-3.5">
                <div className="bg-orange-50 rounded-2xl p-4 border border-orange-200 hover:border-orange-400 transition-colors shadow-sm flex items-start gap-4">
                  <div className="w-10 h-10 bg-orange-100 text-orange-700 rounded-full flex items-center justify-center text-lg shrink-0 mt-0.5">🔬</div>
                  <div>
                    <h4 className="font-bold text-slate-800">3대 소화 효소 복합 배합</h4>
                    <p className="text-xs text-slate-500 mt-1 leading-relaxed">단백질(프로테아제)·탄수화물(아밀라제)·지방(라이페이스)을 각각 분해하는 고활성 효소 3종을 복합 배합했습니다.</p>
                  </div>
                </div>
                <div className="bg-orange-50 rounded-2xl p-4 border border-orange-200 hover:border-orange-400 transition-colors shadow-sm flex items-start gap-4">
                  <div className="w-10 h-10 bg-orange-100 text-orange-700 rounded-full flex items-center justify-center text-lg shrink-0 mt-0.5">🍽️</div>
                  <div>
                    <h4 className="font-bold text-slate-800">소화 기능 개선 및 영양 흡수 촉진</h4>
                    <p className="text-xs text-slate-500 mt-1 leading-relaxed">분해된 영양소가 소장에서 흡수되어 체내 이용률을 높여 식욕 부진 환축의 영양 공급을 돕습니다.</p>
                  </div>
                </div>
                <div className="bg-orange-50 rounded-2xl p-4 border border-orange-200 hover:border-orange-400 transition-colors shadow-sm flex items-start gap-4">
                  <div className="w-10 h-10 bg-orange-100 text-orange-700 rounded-full flex items-center justify-center text-lg shrink-0 mt-0.5">🏥</div>
                  <div>
                    <h4 className="font-bold text-slate-800">수술 후 빠른 회복 촉진</h4>
                    <p className="text-xs text-slate-500 mt-1 leading-relaxed">수술·질병 후 저하된 소화력을 보완하여 영양 회복과 체력 재건을 빠르게 돕습니다.</p>
                  </div>
                </div>
                <div className="bg-orange-50 rounded-2xl p-4 border border-orange-200 hover:border-orange-400 transition-colors shadow-sm flex items-start gap-4">
                  <div className="w-10 h-10 bg-orange-100 text-orange-700 rounded-full flex items-center justify-center text-lg shrink-0 mt-0.5">⚡</div>
                  <div>
                    <h4 className="font-bold text-slate-800">노령견/묘 기력 증진 및 대사 활성화</h4>
                    <p className="text-xs text-slate-500 mt-1 leading-relaxed">활발한 대사를 유지해 노령 반려동물의 기력 저하와 무기력감 완화를 돕습니다.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Powerase Card 2: Ingredients */}
          <div className="bg-white p-4 sm:p-6 md:p-9 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-all duration-300 flex flex-col justify-between">
            <div>
              <h3 className="text-xl md:text-2xl font-black text-slate-800 mb-4 flex items-center gap-3 break-keep">
                <span className="w-9 h-9 rounded-full shrink-0 bg-orange-700 text-white flex items-center justify-center text-sm font-bold shadow-md">2</span>
                <span>핵심 성분 및 약리기전</span>
              </h3>
              <p className="text-slate-600 mb-6 leading-relaxed text-sm md:text-base font-normal">
                고활성 소화 효소 3종의 총량 기준 성분 표기를 적용한 파워라제 독자 포뮬러입니다.
              </p>
              
              <div className="space-y-3">
                <div className="bg-slate-50 border border-slate-200 rounded-xl p-3 flex flex-col sm:flex-row sm:items-center gap-3 hover:bg-white hover:border-orange-300 transition-colors">
                  <div className="shrink-0 flex items-center gap-2 sm:w-2/5">
                    <span className="w-2 h-2 rounded-full bg-orange-500"></span>
                    <h5 className="font-bold text-slate-800 text-sm">Endo Protease <span className="text-orange-700 block text-xs">(엔도 프로테아제) 506,000 pu/g</span></h5>
                  </div>
                  <p className="text-xs text-slate-600 leading-relaxed sm:w-3/5 border-l-0 sm:border-l border-slate-200 sm:pl-3">
                    단백질 내부의 펩타이드 결합을 절단하여 단백질을 아미노산·펩타이드로 분해하고 흡수율을 높입니다.
                  </p>
                </div>

                <div className="bg-slate-50 border border-slate-200 rounded-xl p-3 flex flex-col sm:flex-row sm:items-center gap-3 hover:bg-white hover:border-orange-300 transition-colors">
                  <div className="shrink-0 flex items-center gap-2 sm:w-2/5">
                    <span className="w-2 h-2 rounded-full bg-orange-500"></span>
                    <h5 className="font-bold text-slate-800 text-sm">Alpha Amylase <span className="text-orange-700 block text-xs">(알파 아밀라제) 770 u/g</span></h5>
                  </div>
                  <p className="text-xs text-slate-600 leading-relaxed sm:w-3/5 border-l-0 sm:border-l border-slate-200 sm:pl-3">
                    전분·탄수화물의 α-1,4 결합을 가수분해하여 단당류로 만들고 에너지원으로 빠르게 전환합니다.
                  </p>
                </div>

                <div className="bg-slate-50 border border-slate-200 rounded-xl p-3 flex flex-col sm:flex-row sm:items-center gap-3 hover:bg-white hover:border-orange-300 transition-colors">
                  <div className="shrink-0 flex items-center gap-2 sm:w-2/5">
                    <span className="w-2 h-2 rounded-full bg-orange-500"></span>
                    <h5 className="font-bold text-slate-800 text-sm">Lipase <span className="text-orange-700 block text-xs">(라이페이스) 3,277 u/g</span></h5>
                  </div>
                  <p className="text-xs text-slate-600 leading-relaxed sm:w-3/5 border-l-0 sm:border-l border-slate-200 sm:pl-3">
                    중성지방을 지방산·글리세롤로 분해하여 지방 소화와 필수 지방산 흡수를 돕습니다.
                  </p>
                </div>
              </div>
            </div>
            
            <div className="mt-5 bg-orange-50/90 border border-orange-200 rounded-2xl p-4 text-xs font-medium text-orange-900 leading-relaxed shadow-sm">
              <p className="font-bold mb-1">📌 S&J 동물병원 자문단 코멘트:</p>
              <p>"단백질·탄수화물·지방을 동시에 분해하는 고활성 효소 3종 구성으로, 식욕 부진·소화불량 환축과 수술 후 회복기 환축의 영양 흡수를 직접 지원합니다."</p>
            </div>
          </div>
        </div>
        ) : activeProduct === 'vitaplus' ? (
        <div className="grid lg:grid-cols-2 gap-8 md:gap-10 animate-in fade-in zoom-in-95 duration-300">
          {/* Vitaplus Card 1: Key Benefits */}
          <div className="bg-white p-4 sm:p-6 md:p-9 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-all duration-300 flex flex-col justify-between">
            <div>
              <h3 className="text-xl md:text-2xl font-black text-slate-800 mb-4 flex items-center gap-3 break-keep">
                <span className="w-9 h-9 rounded-full shrink-0 bg-yellow-700 text-white flex items-center justify-center text-sm font-bold shadow-md">1</span>
                <span>종합 비타민 핵심 효능</span>
              </h3>
              <p className="text-slate-600 mb-6 leading-relaxed text-sm md:text-base font-normal">
                비타플러스는 지용성·수용성 비타민 10종을 액상원료 10% 첨가 기준으로 배합한 종합 비타민 특화 솔루션입니다.
              </p>
              <div className="space-y-3.5">
                <div className="bg-yellow-50 rounded-2xl p-4 border border-yellow-200 hover:border-yellow-400 transition-colors shadow-sm flex items-start gap-4">
                  <div className="w-10 h-10 bg-yellow-100 text-yellow-700 rounded-full flex items-center justify-center text-lg shrink-0 mt-0.5">💊</div>
                  <div>
                    <h4 className="font-bold text-slate-800">필수 비타민 고함량 복합 배합</h4>
                    <p className="text-xs text-slate-500 mt-1 leading-relaxed">지용성 비타민(A·D3·E·K3)과 수용성 비타민(C·B1·B6·B12·니코틴아미드·판토텐산칼슘) 10종을 고함량으로 복합 배합했습니다.</p>
                  </div>
                </div>
                <div className="bg-yellow-50 rounded-2xl p-4 border border-yellow-200 hover:border-yellow-400 transition-colors shadow-sm flex items-start gap-4">
                  <div className="w-10 h-10 bg-yellow-100 text-yellow-700 rounded-full flex items-center justify-center text-lg shrink-0 mt-0.5">⚡</div>
                  <div>
                    <h4 className="font-bold text-slate-800">피로 회복 및 항산화 작용</h4>
                    <p className="text-xs text-slate-500 mt-1 leading-relaxed">비타민 C·E와 B군의 에너지 대사 지원으로 피로를 완화하고 활성산소를 제거해 세포를 보호합니다.</p>
                  </div>
                </div>
                <div className="bg-yellow-50 rounded-2xl p-4 border border-yellow-200 hover:border-yellow-400 transition-colors shadow-sm flex items-start gap-4">
                  <div className="w-10 h-10 bg-yellow-100 text-yellow-700 rounded-full flex items-center justify-center text-lg shrink-0 mt-0.5">🦴</div>
                  <div>
                    <h4 className="font-bold text-slate-800">뼈·치아 건강 및 대사 활성화</h4>
                    <p className="text-xs text-slate-500 mt-1 leading-relaxed">비타민 D3·K3가 칼슘 흡수와 골 대사를 조절해 성장기·노령 반려동물의 뼈와 치아 건강을 유지합니다.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Vitaplus Card 2: Ingredients */}
          <div className="bg-white p-4 sm:p-6 md:p-9 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-all duration-300 flex flex-col justify-between">
            <div>
              <h3 className="text-xl md:text-2xl font-black text-slate-800 mb-4 flex items-center gap-3 break-keep">
                <span className="w-9 h-9 rounded-full shrink-0 bg-yellow-700 text-white flex items-center justify-center text-sm font-bold shadow-md">2</span>
                <span>핵심 성분 및 함량 (1L 환산)</span>
              </h3>
              <p className="text-slate-600 mb-6 leading-relaxed text-sm md:text-base font-normal">
                액상원료 10% 첨가 기준으로 1L 당 함량을 환산한 비타플러스 독자 포뮬러입니다.
              </p>
              
              <div className="space-y-3">
                <div className="bg-slate-50 border border-slate-200 rounded-xl p-3">
                  <h5 className="font-bold text-slate-800 text-sm mb-2 flex items-center gap-2"><span className="w-2 h-2 rounded-full bg-yellow-500"></span>지용성 비타민</h5>
                  <p className="text-xs text-slate-600 leading-relaxed">비타민 A 750,000 IU · 비타민 D3 150,000 IU · 비타민 E 300 IU · 비타민 K3 200 mg</p>
                </div>

                <div className="bg-slate-50 border border-slate-200 rounded-xl p-3">
                  <h5 className="font-bold text-slate-800 text-sm mb-2 flex items-center gap-2"><span className="w-2 h-2 rounded-full bg-yellow-500"></span>수용성 비타민·B군</h5>
                  <p className="text-xs text-slate-600 leading-relaxed">비타민 C 299.9 mg · 비타민 B1 203 mg · 비타민 B6 98 mg · 비타민 B12 1 mg · 니코틴아미드 500 mg · 판토텐산칼슘 300 mg</p>
                </div>
              </div>
            </div>
            
            <div className="mt-5 bg-yellow-50/90 border border-yellow-200 rounded-2xl p-4 text-xs font-medium text-yellow-900 leading-relaxed shadow-sm">
              <p className="font-bold mb-1">📌 S&J 동물병원 자문단 코멘트:</p>
              <p>"비타민 10종을 한 번에 보충하는 종합 포뮬러로, 식이 부족·만성질환·회복기 환축의 필수 영양 공급에 권장합니다. 액상원료 10% 첨가 기준으로 함량을 환산해 표기했습니다."</p>
            </div>
          </div>
        </div>
        ) : (
          <div className="text-center py-20 text-slate-500 font-medium animate-in fade-in zoom-in-95 duration-300">
            해당 제품의 임상 데이터 및 학술 검증 자료는 준비 중입니다.
          </div>
        )}
      </div>
    </section>
  );
};

export default ClinicalEvidence;
