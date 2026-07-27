import React from 'react';
import { useTranslation } from 'react-i18next';

export default function StickyBottomCTA({ onOpenModal }) {
  const { t } = useTranslation();

  return (
    <nav 
      aria-label="Quick Action Footer Bar"
      className="fixed bottom-0 left-0 right-0 z-40 bg-[#003d2b]/95 backdrop-blur-md border-t border-emerald-500/30 shadow-[0_-4px_20px_rgba(0,0,0,0.3)] px-4 py-3 sm:px-6 text-white"
    >
      <div className="max-w-6xl mx-auto flex items-center justify-between gap-3">
        <div className="hidden md:flex items-center gap-3">
          <div className="w-10 h-10 rounded-full bg-white flex items-center justify-center text-xl shadow-md border border-slate-200">
            🩺
          </div>
          <div>
            <div className="font-extrabold text-white text-sm tracking-wide">
              {t('stickyCta.title', 'MONSMECTA 수의사 전용 처방 솔루션')}
            </div>
            <div className="text-xs text-emerald-300/90 font-semibold mt-0.5">
              {t('stickyCta.sub', '고순도 나노 몬모릴로나이트 장 점막 보호제')}
            </div>
          </div>
        </div>

        <div className="flex items-center gap-2 w-full md:w-auto">
          <button
            onClick={onOpenModal}
            aria-label={t('stickyCta.sampleBtn', '수의사 무료 샘플 신청')}
            className="flex-1 md:flex-initial px-4 py-2.5 bg-emerald-600 hover:bg-emerald-500 text-white font-extrabold text-xs sm:text-sm rounded-xl shadow-lg transition-all flex items-center justify-center gap-1.5 focus:ring-2 focus:ring-emerald-400 focus:outline-none"
          >
            <span>{t('stickyCta.sampleBtn', '📦 수의사 무료 샘플 신청')}</span>
          </button>
          
          <a
            href="tel:02-1234-5678"
            aria-label={t('stickyCta.consultBtn', '독점 공급 문의')}
            className="flex-1 md:flex-initial px-4 py-2.5 bg-yellow-400 hover:bg-yellow-300 text-slate-900 border border-yellow-500/40 font-black text-xs sm:text-sm rounded-xl shadow-lg transition-all flex items-center justify-center gap-1.5 focus:ring-2 focus:ring-yellow-400 focus:outline-none"
          >
            <span>{t('stickyCta.consultBtn', '📞 독점 공급 문의')}</span>
          </a>
        </div>
      </div>
    </nav>
  );
}
