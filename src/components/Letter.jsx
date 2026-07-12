import React from 'react';
import { useTranslation } from 'react-i18next';

const Letter = () => {
  const { t } = useTranslation();

  return (
    <section className="py-10 md:py-16 bg-emerald-900 text-emerald-50 relative overflow-hidden">
      <div className="absolute inset-0 opacity-10 bg-[url('https://www.transparenttextures.com/patterns/stardust.png')]"></div>
      <div className="max-w-4xl mx-auto px-4 text-center relative z-10">
        <blockquote className="relative">
          <span className="text-8xl text-emerald-400/20 absolute -top-8 -left-8 md:-left-12 font-serif">"</span>
          <p className="text-xl md:text-2xl leading-loose italic font-light drop-shadow-md">
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
