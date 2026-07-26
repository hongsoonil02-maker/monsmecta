import React from 'react';
import { useTranslation } from 'react-i18next';

export default function StickyBottomCTA({ onOpenModal }) {
  const { t } = useTranslation();

  return (
    <nav 
      aria-label="Quick Action Footer Bar"
      className="fixed bottom-0 left-0 right-0 z-40 bg-slate-900/95 backdrop-blur-md border-t border-blue-500/30 shadow-[0_-4px_20px_rgba(0,0,0,0.3)] px-4 py-3 sm:px-6 text-white"
    >
      <div className="max-w-6xl mx-auto flex items-center justify-between gap-3">
        <div className="hidden md:flex items-center gap-3">
          <div className="w-10 h-10 rounded-full bg-blue-600 text-white flex items-center justify-center font-black text-lg">
            🩺
          </div>
          <div>
            <div className="font-extrabold text-white text-sm">
              {t('stickyCta.title', 'MONSMECTA 수의사 전용 처방 솔루션')}
            </div>
            <div className="text-xs text-blue-300 font-semibold">
              {t('stickyCta.sub', '고순도 나노 몬모릴로나이트 장 점막 보호제')}
            </div>
          </div>
        </div>

        <div className="flex items-center gap-2 w-full md:w-auto">
          <button
            onClick={onOpenModal}
            aria-label={t('stickyCta.sampleBtn', '수의사 무료 샘플 신청')}
            className="flex-1 md:flex-initial px-4 py-2.5 bg-blue-600 hover:bg-blue-700 text-white font-extrabold text-xs sm:text-sm rounded-xl shadow-lg transition-all flex items-center justify-center gap-1.5 focus:ring-2 focus:ring-blue-400 focus:outline-none"
          >
            <span>{t('stickyCta.sampleBtn', '📦 수의사 무료 샘플 신청')}</span>
          </button>
          
          <a
            href="tel:02-1234-5678"
            aria-label={t('stickyCta.consultBtn', '독점 공급 문의')}
            className="flex-1 md:flex-initial px-4 py-2.5 bg-slate-800 hover:bg-slate-700 text-blue-300 border border-blue-400/40 font-bold text-xs sm:text-sm rounded-xl shadow-lg transition-all flex items-center justify-center gap-1.5 focus:ring-2 focus:ring-blue-400 focus:outline-none"
          >
            <span>{t('stickyCta.consultBtn', '📞 독점 공급 문의')}</span>
          </a>
        </div>
      </div>
    </nav>
  );
}
