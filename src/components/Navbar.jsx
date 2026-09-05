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
    <nav className="sticky top-0 z-50 bg-white/95 backdrop-blur-md border-b border-gray-200 shadow-sm transition-all duration-300">
      <div className="max-w-7xl mx-auto px-3 sm:px-6 lg:px-8 h-14 sm:h-16 flex items-center justify-between gap-1 sm:gap-4">
        {/* Brand Logo & Name */}
        <a href="#" className="flex items-center gap-1.5 sm:gap-2.5 shrink-0 min-w-0 max-w-[45%] sm:max-w-none">
          <img src={`${import.meta.env.BASE_URL}assets/sj_logo.png`} alt={t('footer.title')} className="h-6 sm:h-8 w-auto shrink-0 drop-shadow-sm" onError={(e) => e.target.style.display = 'none'} />
          <span className="font-black text-xs sm:text-xl text-[#00513b] tracking-tight truncate">{t('footer.title')}</span>
        </a>

        {/* Desktop Navigation Links */}
        <div className="hidden md:flex space-x-8">
          <a href="#about" className="text-sm font-semibold text-slate-600 hover:text-[#00513b] transition-colors">{t('nav.products')}</a>
          <a href="#clinical" className="text-sm font-semibold text-slate-600 hover:text-[#00513b] transition-colors">{t('nav.clinical')}</a>
          <a href="#clinical-case-study" className="text-sm font-bold text-emerald-700 hover:text-emerald-900 transition-colors flex items-center gap-1.5">
            <span className="w-2 h-2 rounded-full bg-emerald-500 animate-ping shrink-0" />
            {t('nav.caseStudy', '임상 다큐')}
          </a>
          <a href="#values" className="text-sm font-semibold text-slate-600 hover:text-[#00513b] transition-colors">{t('nav.values')}</a>
        </div>

        {/* Right Controls */}
        <div className="flex items-center gap-1 sm:gap-3 shrink-0">
          {/* Product selector - Compact on mobile */}
          <div className="flex items-center">
            <select
              value={activeProduct}
              onChange={(e) => setActiveProduct(e.target.value)}
              aria-label="제품 선택"
              className="bg-emerald-50 border border-emerald-300/80 text-[#00513b] text-[11px] sm:text-xs font-bold rounded-full px-2 sm:px-3 py-1 sm:py-1.5 focus:outline-none focus:ring-2 focus:ring-[#00513b] cursor-pointer hover:bg-emerald-100 transition-colors shadow-sm max-w-[115px] sm:max-w-[190px] truncate"
            >
              {Object.values(PRODUCTS).map(p => (
                <option key={p.id} value={p.id}>
                  {p.icon} {getProductDisplayName(p, isKoreanLang)}
                </option>
              ))}
            </select>
          </div>

          {/* Language Selector - Desktop */}
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

          {/* Language Selector - Mobile */}
          <div className="flex md:hidden items-center shrink-0">
            <select
              value={i18n.language || 'ko'}
              onChange={(e) => i18n.changeLanguage(e.target.value)}
              aria-label={t('nav.lang')}
              className="bg-slate-100 border border-slate-300 text-[#00513b] text-xs font-bold rounded-full min-h-[36px] px-2 py-1.5 focus:outline-none focus:ring-2 focus:ring-[#00513b] cursor-pointer shadow-xs active:bg-slate-200"
            >
              {LANGUAGES.map(lang => (
                <option key={lang.code} value={lang.code}>
                  {lang.flag} {lang.code.toUpperCase()}
                </option>
              ))}
            </select>
          </div>

          {/* Desktop Action Buttons */}
          <button onClick={onOpenNoticeModal} className="hidden md:inline-block bg-teal-50 text-[#00513b] border border-[#00513b] px-4 py-2.5 rounded-full text-sm font-bold shadow-sm hover:bg-teal-100 transition-all duration-200">
            {t('nav.noticeBtn')}
          </button>
          <a href="#order" className="hidden md:inline-block bg-[#00513b] text-white px-6 py-2.5 rounded-full text-sm font-bold shadow-md hover:bg-[#003d2b] hover:shadow-lg transform hover:-translate-y-0.5 transition-all duration-200">
            {t('nav.order')}
          </a>

          {/* Mobile Hamburger Menu Button (Always visible) */}
          <button
            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
            className="md:hidden text-[#00513b] hover:bg-emerald-50 active:bg-emerald-100 focus:outline-none focus-visible:ring-2 focus-visible:ring-[#00513b] w-9 h-9 min-w-[36px] flex shrink-0 items-center justify-center rounded-lg transition-colors border border-emerald-200/80"
            aria-label={t('nav.menuToggle')}
            aria-expanded={isMobileMenuOpen}
          >
            <svg className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
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
        <div className="md:hidden bg-white border-b border-gray-200 px-4 py-4 space-y-3.5 shadow-xl animate-in fade-in">
          {/* Quick Product Switcher in Mobile Drawer */}
          <div className="pb-3 border-b border-slate-100">
            <span className="text-[11px] font-bold text-slate-400 mb-2 block">
              {t('nav.products')} 선택
            </span>
            <div className="grid grid-cols-2 gap-1.5">
              {Object.values(PRODUCTS).slice(0, 4).map(p => (
                <button
                  key={p.id}
                  onClick={() => {
                    setActiveProduct(p.id);
                    setIsMobileMenuOpen(false);
                  }}
                  className={`px-2.5 py-1.5 rounded-lg text-xs font-bold text-left flex items-center gap-1.5 transition-all ${
                    activeProduct === p.id
                      ? 'bg-[#00513b] text-white shadow-sm'
                      : 'bg-slate-50 text-slate-700 hover:bg-emerald-50'
                  }`}
                >
                  <span>{p.icon}</span>
                  <span className="truncate">{getProductDisplayName(p, isKoreanLang)}</span>
                </button>
              ))}
            </div>
          </div>

          <a href="#about" onClick={() => setIsMobileMenuOpen(false)} className="block text-base font-semibold text-slate-700 hover:text-[#00513b] py-1 transition-colors">{t('nav.products')}</a>
          <a href="#clinical" onClick={() => setIsMobileMenuOpen(false)} className="block text-base font-semibold text-slate-700 hover:text-[#00513b] py-1 transition-colors">{t('nav.clinical')}</a>
          <a href="#clinical-case-study" onClick={() => setIsMobileMenuOpen(false)} className="block text-base font-bold text-emerald-700 hover:text-emerald-900 py-1 transition-colors flex items-center gap-2">
            <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
            {t('nav.caseStudy', '임상 다큐 (55일령 발작 환축)')}
          </a>
          <a href="#values" onClick={() => setIsMobileMenuOpen(false)} className="block text-base font-semibold text-slate-700 hover:text-[#00513b] py-1 transition-colors">{t('nav.values')}</a>
          
          <div className="pt-2 space-y-2 border-t border-slate-100">
            <a href="#order" onClick={() => setIsMobileMenuOpen(false)} className="block w-full text-center bg-[#00513b] text-white px-6 py-3 rounded-xl text-sm font-bold shadow-md hover:bg-[#003d2b] transition-all">
              {t('nav.order')}
            </a>
            <button onClick={() => { setIsMobileMenuOpen(false); onOpenNoticeModal(); }} className="block w-full text-center bg-teal-50 text-[#00513b] border border-[#00513b] px-6 py-3 rounded-xl text-sm font-bold shadow-sm hover:bg-teal-100 transition-all">
              🖨️ {t('nav.noticeBtn')}
            </button>
          </div>
        </div>
      )}
    </nav>
  );
};

export default Navbar;
