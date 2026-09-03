import { useState } from 'react';
import { useTranslation } from 'react-i18next';

const Infographics = ({ iframeHeights }) => {
  const { t, i18n } = useTranslation();
  const [activeTab, setActiveTab] = useState('james');
  const rawLang = (i18n.language || 'ko').split('-')[0];
  const supportedLangs = ['ko', 'en', 'es', 'fr', 'ja', 'zh', 'ar', 'de', 'ru', 'vi', 'th', 'pt', 'id', 'ms', 'tr'];
  const lang = supportedLangs.includes(rawLang) ? rawLang : 'ko';

  const tabs = [
    {
      id: 'james',
      title: t('infographics.tab1', '🔬 메인 기술 인포그래픽'),
      sub: t('infographics.tab1_sub', '나노 몬모릴로나이트의 작용 기전 및 특허 공정'),
      iframeSrc: `${import.meta.env.BASE_URL}assets/james_infographic_${lang}.html?v=8.3`,
      titleAttr: t('infographics.iframe1'),
      height: iframeHeights.james ? `${iframeHeights.james}px` : '1800px'
    },
    {
      id: 'dashboard',
      title: t('infographics.tab2', '📊 비교 분석 대시보드'),
      sub: t('infographics.tab2_sub', '기존 정장지사제 대비 흡착력 및 배출 지표'),
      iframeSrc: `${import.meta.env.BASE_URL}assets/monsmecta_dashboard_${lang}.html?v=8.3`,
      titleAttr: t('infographics.iframe2'),
      height: iframeHeights.dashboard ? `${iframeHeights.dashboard}px` : '1800px'
    },
    {
      id: 'scenario',
      title: t('infographics.tab3', '🩺 원내 임상 처방 시나리오'),
      sub: t('infographics.tab3_sub', '급·만성 소화기 질환별 단계적 투약 가이드'),
      iframeSrc: `${import.meta.env.BASE_URL}assets/monsmecta_scenario_${lang}.html?v=8.3`,
      titleAttr: t('infographics.iframe3'),
      height: iframeHeights.scenario ? `${iframeHeights.scenario}px` : '1800px'
    }
  ];

  const currentTab = tabs.find(t => t.id === activeTab) || tabs[0];

  return (
    <section className="py-8 sm:py-12 md:py-[68px] bg-white max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div className="text-center mb-8 sm:mb-10">
        <h3 className="text-3xl sm:text-4xl md:text-5xl font-black text-[#00513b] mb-4 break-keep tracking-tight">{t('infographics.title')}</h3>
        <p className="text-slate-500 text-sm sm:text-base md:text-lg font-medium max-w-2xl mx-auto break-keep leading-relaxed">{t('infographics.desc')}</p>
      </div>

      {/* 탭 네비게이션 */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-2.5 sm:gap-4 mb-6">
        {tabs.map((tab) => {
          const isActive = activeTab === tab.id;
          return (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`p-3.5 sm:p-4 rounded-2xl text-left border transition-all duration-200 cursor-pointer ${
                isActive
                  ? 'bg-emerald-50/90 border-emerald-600 shadow-md ring-2 ring-emerald-500/20'
                  : 'bg-slate-50 hover:bg-slate-100 border-slate-200 text-slate-600 hover:border-slate-300'
              }`}
            >
              <div className={`font-black text-sm sm:text-base ${isActive ? 'text-[#00513b]' : 'text-slate-800'}`}>
                {tab.title}
              </div>
              <div className="text-xs text-slate-500 mt-1 leading-normal line-clamp-2">
                {tab.sub}
              </div>
            </button>
          );
        })}
      </div>

      {/* 선택된 탭의 인포그래픽 프레임 */}
      <div
        key={currentTab.id}
        className="bg-slate-50 rounded-3xl shadow-xl border border-slate-200 overflow-hidden relative transition-all duration-300 w-full animate-in fade-in duration-300"
        style={{ height: currentTab.height }}
      >
        <iframe
          src={currentTab.iframeSrc}
          className="absolute top-0 left-0 w-full h-full border-0"
          title={currentTab.titleAttr}
          scrolling="no"
          loading="lazy"
        />
      </div>
    </section>
  );
};

export default Infographics;
