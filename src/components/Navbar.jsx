import React from 'react';
import { useTranslation } from 'react-i18next';

const Navbar = ({ isMobileMenuOpen, setIsMobileMenuOpen }) => {
  const { t, i18n } = useTranslation();

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
          <a href="#values" className="text-sm font-semibold text-slate-600 hover:text-[#00513b] transition-colors">{t('nav.values')}</a>
        </div>
        <div className="flex items-center gap-2 sm:gap-4 shrink-0">
          {/* Language toggle - Dropdown */}
          <div className="flex items-center shrink-0">
            <select
              value={i18n.language || 'ko'}
              onChange={(e) => i18n.changeLanguage(e.target.value)}
              aria-label="Language Selector"
              className="bg-slate-100 border border-slate-200 text-[#00513b] text-xs font-bold rounded-full px-3 py-1.5 focus:outline-none focus:ring-2 focus:ring-[#00513b] cursor-pointer hover:bg-slate-200 transition-colors shadow-sm"
            >
              <option value="ko">🌐 KO (한국어)</option>
              <option value="en">🌐 EN (English)</option>
              <option value="ja">🌐 JA (日本語)</option>
              <option value="zh">🌐 ZH (中文)</option>
              <option value="es">🌐 ES (Español)</option>
              <option value="fr">🌐 FR (Français)</option>
              <option value="de">🌐 DE (Deutsch)</option>
              <option value="vi">🌐 VI (Tiếng Việt)</option>
              <option value="th">🌐 TH (ไทย)</option>
              <option value="ru">🌐 RU (Русский)</option>
              <option value="pt">🌐 PT (Português)</option>
              <option value="ar">🌐 AR (العربية)</option>
              <option value="id">🌐 ID (Bahasa Indonesia)</option>
              <option value="ms">🌐 MS (Bahasa Melayu)</option>
              <option value="tr">🌐 TR (Türkçe)</option>
            </select>
          </div>

          <a href="#order" className="hidden md:inline-block bg-[#00513b] text-white px-6 py-2.5 rounded-full text-sm font-bold shadow-md hover:bg-[#003d2b] hover:shadow-lg transform hover:-translate-y-0.5 transition-all duration-200">
            {t('nav.order')}
          </a>
          {/* Mobile menu button */}
          <button
            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
            className="md:hidden text-slate-600 hover:text-[#00513b] focus:outline-none"
            aria-label="Toggle mobile menu"
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
          <a href="#values" onClick={() => setIsMobileMenuOpen(false)} className="block text-base font-semibold text-slate-600 hover:text-[#00513b] transition-colors">{t('nav.values')}</a>
          <a href="#order" onClick={() => setIsMobileMenuOpen(false)} className="block w-full text-center bg-[#00513b] text-white px-6 py-3 rounded-xl text-sm font-bold shadow-md hover:bg-[#003d2b] transition-all duration-200 mt-4">
            {t('nav.order')}
          </a>
        </div>
      )}
    </nav>
  );
};

export default Navbar;
