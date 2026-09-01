import { useTranslation } from 'react-i18next';

const Letter = () => {
  const { t } = useTranslation();

  return (
    <section className="py-10 sm:py-14 md:py-[68px] bg-emerald-50/70 text-slate-800 relative overflow-hidden border-y border-emerald-200/70">
      <div className="absolute inset-0 opacity-20 bg-[radial-gradient(circle_at_50%_0%,rgba(16,185,129,0.15),transparent_50%)]"></div>
      <div className="max-w-4xl mx-auto px-4 sm:px-6 text-center relative z-10">
        <blockquote className="relative">
          <span className="text-8xl text-emerald-600/20 absolute -top-8 -left-6 md:-left-12 font-serif select-none">"</span>
          <p className="text-lg sm:text-xl md:text-2xl leading-relaxed md:leading-loose italic font-medium text-slate-800 drop-shadow-xs break-keep">
            {t('letter.message1')}<br className="hidden md:block" />
            {t('letter.message2')}<br className="hidden md:block" />
            {t('letter.message3')}
          </p>
          <footer className="mt-10">
            <div className="font-bold text-emerald-800 text-lg sm:text-xl tracking-wide">{t('letter.signature_title')}</div>
            <div className="font-black text-slate-950 text-2xl sm:text-3xl mt-2">{t('letter.signature_name')}</div>
          </footer>
        </blockquote>
      </div>
    </section>
  );
};

export default Letter;
