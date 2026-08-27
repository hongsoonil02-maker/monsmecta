import { useTranslation } from 'react-i18next';

export default function StickyBottomCTA({ onOpenModal, onOpenNoticeModal }) {
  const { t } = useTranslation();

  return (
    <nav 
      aria-label={t('stickyCta.navLabel', '하단 바로가기 메뉴')}
      className="fixed bottom-0 left-0 right-0 z-40 bg-[#003d2b]/95 backdrop-blur-md border-t border-emerald-500/30 shadow-[0_-4px_20px_rgba(0,0,0,0.3)] px-4 pt-3 pb-[calc(0.75rem+env(safe-area-inset-bottom,0px))] sm:px-6 text-white"
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
            onClick={onOpenNoticeModal}
            aria-label={t('notice.title', '원내 A4 알림판 만들기')}
            className="flex-1 md:flex-initial min-h-[44px] px-4 py-2.5 bg-blue-600 hover:bg-blue-500 text-white font-extrabold text-xs sm:text-sm rounded-xl shadow-lg transition-all flex items-center justify-center gap-1.5 focus:ring-2 focus:ring-blue-400 focus:outline-none active:scale-[0.98]"
          >
            <span>🖨️ {t('notice.stickyBtn', '알림판 만들기')}</span>
          </button>
          <button
            onClick={onOpenModal}
            aria-label={t('stickyCta.sampleBtn', '수의사 무료 샘플 신청')}
            className="flex-1 md:flex-initial min-h-[44px] px-4 py-2.5 bg-emerald-600 hover:bg-emerald-500 text-white font-extrabold text-xs sm:text-sm rounded-xl shadow-lg transition-all flex items-center justify-center gap-1.5 focus:ring-2 focus:ring-emerald-400 focus:outline-none active:scale-[0.98]"
          >
            <span>{t('stickyCta.sampleBtn', '📦 무료 샘플 신청')}</span>
          </button>
        </div>
      </div>
    </nav>
  );
}
