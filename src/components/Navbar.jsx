import { useTranslation } from 'react-i18next';
import { PRODUCTS, getProductDisplayName } from '../data/products';

const LANGUAGES = [
  { code: 'ko', label: '한국어', flag: '🇰🇷' },
  { code: 'en', label: 'English', flag: '🇺🇸' },
  { code: 'ja', label: '日本語', flag: '🇯🇵' },
  { code: 'zh', label: '中文', flag: '🇨🇳' },
  { code: 'es', label: 'Español', flag: '🇪🇸' },
  { code: 'fr', label: 'Français', flag: '🇫🇷' },
  { code: 'de', label: 'Deutsch', flag: '🇩🇪' },
  { code: 'th', label: 'ไทย', flag: '🇹🇭' },
  { code: 'vi', label: 'Tiếng Việt', flag: '🇻🇳' },
  { code: 'ru', label: 'Русский', flag: '🇷🇺' },
  { code: 'pt', label: 'Português', flag: '🇵🇹' },
  { code: 'ar', label: 'العربية', flag: '🇸🇦' },
  { code: 'id', label: 'Bahasa Indonesia', flag: '🇮🇩' },
  { code: 'ms', label: 'Bahasa Melayu', flag: '🇲🇾' },
  { code: 'tr', label: 'Türkçe', flag: '🇹🇷' },
];

const Navbar = ({ isMobileMenuOpen, setIsMobileMenuOpen, onOpenNoticeModal, activeProduct, setActiveProduct }) => {
  const { t, i18n } = useTranslation();
  const isKoreanLang = (i18n.language || 'ko').toLowerCase().startsWith('ko');

  return (
    <nav className="sticky top-0 z-50 bg-white/90 backdrop-blur-md border-b border-gray-200 shadow-sm transition-all duration-300">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        <div className="flex items-center gap-2 sm:gap-3 shrink-0 max-w-[60%] sm:max-w-none">
          <img src={`${import.meta.env.BASE_URL}assets/sj_logo.png`} alt={t('footer.title')} className="h-7 sm:h-8 w-auto shrink-0 drop-shadow-sm" onError={(e) => e.target.style.display = 'none'} />
          <span className="font-extrabold text-base sm:text-xl text-[#00513b] tracking-tight truncate">{t('footer.title')}</span>
        </div>
        <div className="hidden md:flex space-x-8">
          <a href="#about" className="text-sm font-semibold text-slate-600 hover:text-[#00513b] transition-colors">{t('nav.products')}</a>
          <a href="#clinical" className="text-sm font-semibold text-slate-600 hover:text-[#00513b] transition-colors">{t('nav.clinical')}</a>
          <a href="#clinical-case-study" className="text-sm font-bold text-emerald-700 hover:text-emerald-900 transition-colors flex items-center gap-1.5">
            <span className="w-2 h-2 rounded-full bg-emerald-500 animate-ping shrink-0" />
            {t('nav.caseStudy', '임상 다큐')}
          </a>
          <a href="#values" className="text-sm font-semibold text-slate-600 hover:text-[#00513b] transition-colors">{t('nav.values')}</a>
        </div>
        <div className="flex items-center gap-2 sm:gap-4 shrink-0">
          {/* Product selector - Dropdown */}
          <div className="flex items-center shrink-0">
            <select
              value={activeProduct}
              onChange={(e) => setActiveProduct(e.target.value)}
              aria-label="제품 선택"
              className="bg-emerald-50 border border-emerald-200 text-[#00513b] text-xs font-bold rounded-full px-3 py-1.5 focus:outline-none focus:ring-2 focus:ring-[#00513b] cursor-pointer hover:bg-emerald-100 transition-colors shadow-sm max-w-[200px]"
            >
              {Object.values(PRODUCTS).map(p => (
                <option key={p.id} value={p.id}>
                  {p.icon} {getProductDisplayName(p, isKoreanLang)}
                </option>
              ))}
            </select>
          </div>

          {/* Language Selector - Desktop: Dropdown */}
          <div className="hidden md:flex items-center shrink-0">
            <select
              value={i18n.language || 'ko'}
              onChange={(e) => i18n.changeLanguage(e.target.value)}
              aria-label={t('nav.lang')}
              className="bg-slate-100 border border-slate-300 text-[#00513b] text-xs font-bold rounded-full px-3 py-1.5 focus:outline-none focus:ring-2 focus:ring-[#00513b] cursor-pointer hover:bg-slate-200 transition-colors"
            >
              {LANGUAGES.map(lang => (
                <option key={lang.code} value={lang.code}>
                  {lang.flag} {lang.label}
                </option>
              ))}
            </select>
          </div>

          {/* Language Selector - Mobile: Dropdown */}
          <div className="flex md:hidden items-center shrink-0">
            <select
              value={i18n.language || 'ko'}
              onChange={(e) => i18n.changeLanguage(e.target.value)}
              aria-label={t('nav.lang')}
              className="bg-slate-100 border border-slate-300 text-[#00513b] text-xs font-bold rounded-full px-2 py-1 focus:outline-none focus:ring-2 focus:ring-[#00513b] cursor-pointer"
            >
              {LANGUAGES.map(lang => (
                <option key={lang.code} value={lang.code}>
                  {lang.flag} {lang.code.toUpperCase()}
                </option>
              ))}
            </select>
          </div>

          <button onClick={onOpenNoticeModal} className="hidden md:inline-block bg-teal-50 text-[#00513b] border border-[#00513b] px-4 py-2.5 rounded-full text-sm font-bold shadow-sm hover:bg-teal-100 transition-all duration-200">
            {t('nav.noticeBtn')}
          </button>
          <a href="#order" className="hidden md:inline-block bg-[#00513b] text-white px-6 py-2.5 rounded-full text-sm font-bold shadow-md hover:bg-[#003d2b] hover:shadow-lg transform hover:-translate-y-0.5 transition-all duration-200">
            {t('nav.order')}
          </a>
          {/* Mobile menu button */}
          <button
            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
            className="md:hidden text-slate-600 hover:text-[#00513b] focus:outline-none focus-visible:ring-2 focus-visible:ring-[#00513b] min-w-[44px] min-h-[44px] flex items-center justify-center rounded-xl transition-colors"
            aria-label={t('nav.menuToggle')}
            aria-expanded={isMobileMenuOpen}
          >
            <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              {isMobileMenuOpen ? (
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              ) : (
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
              )}
            </svg>
          </button>
        </div>
      </div>

      {/* Mobile Menu Panel */}
      {isMobileMenuOpen && (
        <div className="md:hidden bg-white border-b border-gray-200 px-4 py-4 space-y-4">
          <a href="#about" onClick={() => setIsMobileMenuOpen(false)} className="block text-base font-semibold text-slate-600 hover:text-[#00513b] transition-colors">{t('nav.products')}</a>
          <a href="#clinical" onClick={() => setIsMobileMenuOpen(false)} className="block text-base font-semibold text-slate-600 hover:text-[#00513b] transition-colors">{t('nav.clinical')}</a>
          <a href="#clinical-case-study" onClick={() => setIsMobileMenuOpen(false)} className="block text-base font-bold text-emerald-700 hover:text-emerald-900 transition-colors flex items-center gap-2">
            <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
            {t('nav.caseStudy', '임상 다큐 (55일령 발작 환축)')}
          </a>
          <a href="#values" onClick={() => setIsMobileMenuOpen(false)} className="block text-base font-semibold text-slate-600 hover:text-[#00513b] transition-colors">{t('nav.values')}</a>
          <a href="#order" onClick={() => setIsMobileMenuOpen(false)} className="block w-full text-center bg-[#00513b] text-white px-6 py-3 rounded-xl text-sm font-bold shadow-md hover:bg-[#003d2b] transition-all duration-200 mt-4">
            {t('nav.order')}
          </a>
          <button onClick={() => { setIsMobileMenuOpen(false); onOpenNoticeModal(); }} className="block w-full text-center bg-teal-50 text-[#00513b] border border-[#00513b] px-6 py-3 rounded-xl text-sm font-bold shadow-sm hover:bg-teal-100 transition-all duration-200 mt-2">
            {t('nav.noticeBtn')}
          </button>
        </div>
      )}
    </nav>
  );
};

export default Navbar;
