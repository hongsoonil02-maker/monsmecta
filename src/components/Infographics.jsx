import { useTranslation } from 'react-i18next';

const Infographics = ({ iframeHeights }) => {
  const { t, i18n } = useTranslation();
  const rawLang = (i18n.language || 'ko').split('-')[0];
  const supportedLangs = ['ko', 'en', 'es', 'fr', 'ja', 'zh', 'ar', 'de', 'ru', 'vi', 'th', 'pt', 'id', 'ms', 'tr'];
  const lang = supportedLangs.includes(rawLang) ? rawLang : 'ko';

  return (
    <section className="py-6 md:py-12 bg-white max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div className="text-center mb-8">
        <h3 className="text-3xl md:text-4xl font-extrabold text-[#00513b] mb-4 break-keep">{t('infographics.title')}</h3>
        <p className="text-slate-500 text-lg font-medium break-keep">{t('infographics.desc')}</p>
      </div>
      <div className="space-y-4 md:space-y-6">

        {/* HTML Infographic 1: Main */}
        <div
          className="bg-slate-50 rounded-3xl shadow-xl border border-slate-200 overflow-hidden relative transition-all duration-300 w-full"
          style={{ height: iframeHeights.james ? `${iframeHeights.james}px` : '1800px' }}
        >
          <iframe
            src={`${import.meta.env.BASE_URL}assets/james_infographic_${lang}.html?v=8.2`}
            className="absolute top-0 left-0 w-full h-full border-0"
            title={t('infographics.iframe1')}
            scrolling="no"
            loading="lazy"
          />
        </div>

        {/* HTML Infographic 2: Dashboard */}
        <div
          className="bg-slate-50 rounded-3xl shadow-xl border border-slate-200 overflow-hidden relative transition-all duration-300 w-full"
          style={{ height: iframeHeights.dashboard ? `${iframeHeights.dashboard}px` : '1800px' }}
        >
          <iframe
            src={`${import.meta.env.BASE_URL}assets/monsmecta_dashboard_${lang}.html?v=8.2`}
            className="absolute top-0 left-0 w-full h-full border-0"
            title={t('infographics.iframe2')}
            scrolling="no"
            loading="lazy"
          />
        </div>

        {/* HTML Infographic 3: Scenario */}
        <div
          className="bg-slate-50 rounded-3xl shadow-xl border border-slate-200 overflow-hidden relative transition-all duration-300 w-full"
          style={{ height: iframeHeights.scenario ? `${iframeHeights.scenario}px` : '1800px' }}
        >
          <iframe
            src={`${import.meta.env.BASE_URL}assets/monsmecta_scenario_${lang}.html?v=8.2`}
            className="absolute top-0 left-0 w-full h-full border-0"
            title={t('infographics.iframe3')}
            scrolling="no"
            loading="lazy"
          />
        </div>

      </div>
    </section>
  );
};

export default Infographics;
