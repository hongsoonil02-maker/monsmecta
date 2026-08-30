import { useTranslation } from 'react-i18next';

const Letter = () => {
  const { t } = useTranslation();

  return (
    <section className="py-14 sm:py-20 md:py-24 bg-slate-900 text-slate-100 relative overflow-hidden border-y border-slate-800">
      <div className="absolute inset-0 opacity-10 bg-[radial-gradient(circle_at_50%_0%,rgba(255,255,255,0.2),transparent_50%)]"></div>
      <div className="max-w-4xl mx-auto px-4 sm:px-6 text-center relative z-10">
        <blockquote className="relative">
          <span className="text-8xl text-emerald-500/20 absolute -top-8 -left-6 md:-left-12 font-serif select-none">"</span>
          <p className="text-lg sm:text-xl md:text-2xl leading-relaxed md:leading-loose italic font-light drop-shadow-md break-keep">
            {t('letter.message1')}<br className="hidden md:block" />
            {t('letter.message2')}<br className="hidden md:block" />
            {t('letter.message3')}
          </p>
          <footer className="mt-10">
            <div className="font-bold text-yellow-400 text-xl tracking-wide">{t('letter.signature_title')}</div>
            <div className="font-black text-white text-2xl mt-2">{t('letter.signature_name')}</div>
          </footer>
        </blockquote>
      </div>
    </section>
  );
};

export default Letter;
