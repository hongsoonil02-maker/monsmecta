import { useState, useEffect, useRef } from 'react';
import { useTranslation } from 'react-i18next';

const A11yToolbar = () => {
  const { t, i18n } = useTranslation();
  const [highContrast, setHighContrast] = useState(false);
  const [largeText, setLargeText] = useState(false);
  const [reduceMotion, setReduceMotion] = useState(false);
  const [readableFont, setReadableFont] = useState(false);
  const [isSpeaking, setIsSpeaking] = useState(false);
  const [isOpen, setIsOpen] = useState(false);
  const menuRef = useRef(null);
  const triggerRef = useRef(null);

  // 1. 고대비 모드
  useEffect(() => {
    if (highContrast) {
      document.documentElement.classList.add('high-contrast');
    } else {
      document.documentElement.classList.remove('high-contrast');
    }
  }, [highContrast]);

  // 2. 큰 글씨 모드
  useEffect(() => {
    if (largeText) {
      document.documentElement.classList.add('large-text');
    } else {
      document.documentElement.classList.remove('large-text');
    }
  }, [largeText]);

  // 3. 움직임 줄이기 (전정기관 장애 배려)
  useEffect(() => {
    if (reduceMotion) {
      document.documentElement.classList.add('reduce-motion');
    } else {
      document.documentElement.classList.remove('reduce-motion');
    }
  }, [reduceMotion]);

  // 4. 가독성 향상 모드 (자간/줄간격 확장)
  useEffect(() => {
    if (readableFont) {
      document.documentElement.classList.add('readable-font');
    } else {
      document.documentElement.classList.remove('readable-font');
    }
  }, [readableFont]);

  // 5. 본문 음성 읽어주기 (TTS)
  const handleToggleSpeech = () => {
    if (!('speechSynthesis' in window)) {
      alert(t('a11y.ttsNotSupported', '현재 브라우저에서는 음성 읽기 기능을 지원하지 않습니다.'));
      return;
    }

    if (isSpeaking) {
      window.speechSynthesis.cancel();
      setIsSpeaking(false);
      return;
    }

    window.speechSynthesis.cancel();
    const textToRead = [
      t('hero.title', '임상 수의사의 해답, MONSMECTA'),
      t('hero.subtitle', '현장 진료의 까다로운 기준을 통과한 위장관 솔루션.'),
      t('clinicalCase.title', '55일령 발작 환축의 7일간의 기적'),
      t('clinicalCase.subtitle', '하남 사랑동물병원 김동준 원장의 실제 임상 치료 일지입니다.')
    ].join('. ');

    const utterance = new SpeechSynthesisUtterance(textToRead);
    utterance.lang = i18n.language === 'en' ? 'en-US' : (i18n.language === 'ja' ? 'ja-JP' : (i18n.language === 'zh' ? 'zh-CN' : 'ko-KR'));
    utterance.rate = 0.95;
    utterance.onend = () => setIsSpeaking(false);
    utterance.onerror = () => setIsSpeaking(false);

    setIsSpeaking(true);
    window.speechSynthesis.speak(utterance);
  };

  // 컴포넌트 언마운트 시 음성 정지
  useEffect(() => {
    return () => {
      if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
      }
    };
  }, []);

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
      className="fixed bottom-[calc(5.2rem+env(safe-area-inset-bottom,0px))] start-3 sm:start-6 z-[80] flex flex-col items-start gap-2"
    >
      {isOpen && (
        <div
          ref={menuRef}
          role="dialog"
          aria-modal="false"
          aria-label={t('a11y.title', '접근성 설정 (A11y)')}
          className="bg-white dark:bg-slate-900 border border-emerald-300 dark:border-slate-700 rounded-2xl shadow-2xl p-4 flex flex-col gap-2 mb-2 w-64 text-slate-800 dark:text-white backdrop-blur-md origin-bottom-left animate-in fade-in zoom-in"
        >
          <div className="flex items-center justify-between border-b border-gray-200 dark:border-slate-800 pb-2 mb-1">
            <span className="text-xs font-black text-gray-800 dark:text-slate-100 flex items-center gap-1.5">
              <span aria-hidden="true">♿</span> {t('a11y.title', '장애인 접근 편의 도구')}
            </span>
            <button
              onClick={() => setIsOpen(false)}
              className="text-gray-400 hover:text-gray-600 dark:hover:text-white text-xs font-bold p-1 rounded focus:outline-none focus:ring-2 focus:ring-emerald-500 cursor-pointer"
              aria-label={t('common.close', '닫기')}
            >
              ✕
            </button>
          </div>
          
          {/* 고대비 모드 */}
          <button
            onClick={() => setHighContrast(!highContrast)}
            className={`min-h-[42px] px-3 py-2 text-xs font-bold rounded-xl text-start transition-all flex items-center justify-between cursor-pointer ${
              highContrast
                ? 'bg-[#00513b] text-white shadow-md ring-2 ring-lime-400'
                : 'bg-gray-100 dark:bg-slate-800 text-gray-700 dark:text-slate-300 hover:bg-gray-200 dark:hover:bg-slate-700'
            } focus:outline-none focus:ring-2 focus:ring-emerald-500`}
            aria-pressed={highContrast}
          >
            <span>{highContrast ? t('a11y.contrastOff', '고대비 끄기') : t('a11y.contrastOn', '고대비 켜기')}</span>
            <span className="text-[11px] px-1.5 py-0.5 rounded bg-black/20">{highContrast ? 'ON' : 'OFF'}</span>
          </button>

          {/* 큰 글씨 모드 */}
          <button
            onClick={() => setLargeText(!largeText)}
            className={`min-h-[42px] px-3 py-2 text-xs font-bold rounded-xl text-start transition-all flex items-center justify-between cursor-pointer ${
              largeText
                ? 'bg-[#00513b] text-white shadow-md ring-2 ring-lime-400'
                : 'bg-gray-100 dark:bg-slate-800 text-gray-700 dark:text-slate-300 hover:bg-gray-200 dark:hover:bg-slate-700'
            } focus:outline-none focus:ring-2 focus:ring-emerald-500`}
            aria-pressed={largeText}
          >
            <span>{largeText ? t('a11y.largeTextOff', '글씨 크기 복구') : t('a11y.largeTextOn', '큰 글씨 확대')}</span>
            <span className="text-[11px] px-1.5 py-0.5 rounded bg-black/20">{largeText ? 'ON' : 'OFF'}</span>
          </button>

          {/* 움직임 줄이기 */}
          <button
            onClick={() => setReduceMotion(!reduceMotion)}
            className={`min-h-[42px] px-3 py-2 text-xs font-bold rounded-xl text-start transition-all flex items-center justify-between cursor-pointer ${
              reduceMotion
                ? 'bg-[#00513b] text-white shadow-md ring-2 ring-lime-400'
                : 'bg-gray-100 dark:bg-slate-800 text-gray-700 dark:text-slate-300 hover:bg-gray-200 dark:hover:bg-slate-700'
            } focus:outline-none focus:ring-2 focus:ring-emerald-500`}
            aria-pressed={reduceMotion}
          >
            <span>{reduceMotion ? t('a11y.reduceMotionOff', '움직임 효과 켜기') : t('a11y.reduceMotionOn', '움직임 줄이기')}</span>
            <span className="text-[11px] px-1.5 py-0.5 rounded bg-black/20">{reduceMotion ? 'ON' : 'OFF'}</span>
          </button>

          {/* 가독성 향상 모드 */}
          <button
            onClick={() => setReadableFont(!readableFont)}
            className={`min-h-[42px] px-3 py-2 text-xs font-bold rounded-xl text-start transition-all flex items-center justify-between cursor-pointer ${
              readableFont
                ? 'bg-[#00513b] text-white shadow-md ring-2 ring-lime-400'
                : 'bg-gray-100 dark:bg-slate-800 text-gray-700 dark:text-slate-300 hover:bg-gray-200 dark:hover:bg-slate-700'
            } focus:outline-none focus:ring-2 focus:ring-emerald-500`}
            aria-pressed={readableFont}
          >
            <span>{readableFont ? t('a11y.readableFontOff', '기본 줄간격 복구') : t('a11y.readableFontOn', '가독성 줄간격 확대')}</span>
            <span className="text-[11px] px-1.5 py-0.5 rounded bg-black/20">{readableFont ? 'ON' : 'OFF'}</span>
          </button>

          {/* 음성 읽어주기 (TTS) */}
          <button
            onClick={handleToggleSpeech}
            className={`min-h-[42px] px-3 py-2 text-xs font-bold rounded-xl text-start transition-all flex items-center justify-between cursor-pointer ${
              isSpeaking
                ? 'bg-amber-500 text-slate-950 shadow-md ring-2 ring-amber-300 animate-pulse'
                : 'bg-gray-100 dark:bg-slate-800 text-gray-700 dark:text-slate-300 hover:bg-gray-200 dark:hover:bg-slate-700'
            } focus:outline-none focus:ring-2 focus:ring-emerald-500`}
            aria-pressed={isSpeaking}
          >
            <span className="flex items-center gap-1.5">
              <span>{isSpeaking ? '🔊' : '🔈'}</span>
              <span>{isSpeaking ? t('a11y.readAloudOff', '음성 읽기 멈춤') : t('a11y.readAloudOn', '본문 음성 읽기')}</span>
            </span>
            <span className="text-[11px] px-1.5 py-0.5 rounded bg-black/20">{isSpeaking ? '재생중' : 'OFF'}</span>
          </button>
        </div>
      )}

      {/* 플로팅 접근성 토글 버튼 (한국아그로 스타일 딥그린 원형 + 유니버설 접근성 아이콘) */}
      <button
        ref={triggerRef}
        onClick={() => setIsOpen(!isOpen)}
        className="bg-[#00513b] hover:bg-[#003d2b] active:bg-[#00281d] text-lime-300 w-14 h-14 min-w-[48px] min-h-[48px] rounded-full shadow-2xl border-2 border-lime-400/80 flex items-center justify-center focus:outline-none focus-visible:ring-4 focus-visible:ring-lime-400/50 transition-all hover:scale-110 active:scale-95 group cursor-pointer"
        aria-label={t('a11y.openMenu', '장애인 접근 편의 도구 열기')}
        aria-expanded={isOpen}
        aria-haspopup="dialog"
      >
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" className="w-7 h-7 transition-transform group-hover:scale-105" fill="none" stroke="currentColor" strokeWidth="1.8" aria-hidden="true">
          <circle cx="12" cy="12" r="10" strokeWidth="1.6" />
          <circle cx="12" cy="6.8" r="1.6" fill="currentColor" stroke="none" />
          <path strokeLinecap="round" strokeLinejoin="round" d="M6.5 10.2h11M12 9.5v4.5l-2.2 4.5M12 14l2.2 4.5" />
        </svg>
      </button>
    </aside>
  );
};

export default A11yToolbar;
