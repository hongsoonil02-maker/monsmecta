import { useState, useEffect, useRef } from 'react';
import { useTranslation } from 'react-i18next';

const A11yToolbar = () => {
  const { t } = useTranslation();
  const [highContrast, setHighContrast] = useState(false);
  const [largeText, setLargeText] = useState(false);
  const [isOpen, setIsOpen] = useState(false);
  const menuRef = useRef(null);
  const triggerRef = useRef(null);

  useEffect(() => {
    if (highContrast) {
      document.documentElement.classList.add('high-contrast');
    } else {
      document.documentElement.classList.remove('high-contrast');
    }
  }, [highContrast]);

  useEffect(() => {
    if (largeText) {
      document.documentElement.classList.add('large-text');
    } else {
      document.documentElement.classList.remove('large-text');
    }
  }, [largeText]);

  // ESC 키로 메뉴 닫기 접근성 지원
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'Escape' && isOpen) {
        setIsOpen(false);
        triggerRef.current?.focus();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen]);

  return (
    <aside
      aria-label={t('a11y.toolbarLabel', '웹 접근성 설정 도구')}
      className="fixed bottom-[calc(6rem+env(safe-area-inset-bottom,0px))] end-4 sm:end-6 z-[9999] flex flex-col items-end gap-2"
    >
      {isOpen && (
        <div
          ref={menuRef}
          role="dialog"
          aria-modal="false"
          aria-label={t('a11y.title', '접근성 설정 (A11y)')}
          className="bg-white dark:bg-slate-900 border border-gray-200 dark:border-slate-700 rounded-2xl shadow-2xl p-4 flex flex-col gap-2.5 mb-2 w-52 text-slate-800 dark:text-white backdrop-blur-md"
        >
          <div className="flex items-center justify-between border-b border-gray-200 dark:border-slate-800 pb-2 mb-1">
            <span className="text-xs font-bold text-gray-700 dark:text-slate-200 flex items-center gap-1.5">
              <span>♿</span> {t('a11y.title', '접근성 설정')}
            </span>
            <button
              onClick={() => setIsOpen(false)}
              className="text-gray-400 hover:text-gray-600 dark:hover:text-white text-xs font-bold p-1 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
              aria-label={t('common.close', '닫기')}
            >
              ✕
            </button>
          </div>
          
          <button
            onClick={() => setHighContrast(!highContrast)}
            className={`min-h-[44px] px-3.5 py-2.5 text-xs sm:text-sm font-bold rounded-xl text-start transition-all flex items-center justify-between ${
              highContrast
                ? 'bg-emerald-700 text-white shadow-md'
                : 'bg-gray-100 dark:bg-slate-800 text-gray-700 dark:text-slate-300 hover:bg-gray-200 dark:hover:bg-slate-700'
            } focus:outline-none focus:ring-2 focus:ring-blue-500`}
            aria-pressed={highContrast}
          >
            <span>{highContrast ? t('a11y.contrastOff', '고대비 끄기') : t('a11y.contrastOn', '고대비 켜기')}</span>
            <span className="text-xs">{highContrast ? 'ON' : 'OFF'}</span>
          </button>

          <button
            onClick={() => setLargeText(!largeText)}
            className={`min-h-[44px] px-3.5 py-2.5 text-xs sm:text-sm font-bold rounded-xl text-start transition-all flex items-center justify-between ${
              largeText
                ? 'bg-emerald-700 text-white shadow-md'
                : 'bg-gray-100 dark:bg-slate-800 text-gray-700 dark:text-slate-300 hover:bg-gray-200 dark:hover:bg-slate-700'
            } focus:outline-none focus:ring-2 focus:ring-blue-500`}
            aria-pressed={largeText}
          >
            <span>{largeText ? t('a11y.largeTextOff', '글씨 크기 복구') : t('a11y.largeTextOn', '큰 글씨 모드')}</span>
            <span className="text-xs">{largeText ? 'ON' : 'OFF'}</span>
          </button>
        </div>
      )}

      {/* 플로팅 접근성 토글 버튼 (48x48px 표준 터치 타깃 준수) */}
      <button
        ref={triggerRef}
        onClick={() => setIsOpen(!isOpen)}
        className="bg-blue-600 hover:bg-blue-700 text-white w-12 h-12 min-w-[48px] min-h-[48px] rounded-full shadow-2xl flex items-center justify-center focus:outline-none focus-visible:ring-4 focus-visible:ring-blue-300 transition-all hover:scale-105 active:scale-95"
        aria-label={t('a11y.openMenu', '웹 접근성 설정 메뉴 열기')}
        aria-expanded={isOpen}
        aria-haspopup="dialog"
      >
        <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
        </svg>
      </button>
    </aside>
  );
};

export default A11yToolbar;
