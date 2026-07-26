import React from 'react';
import { useTranslation } from 'react-i18next';

const Footer = ({ setLegalType }) => {
  const { t } = useTranslation();

  return (
    <footer className="bg-[#00281d] text-emerald-400/80 py-8 md:py-16 border-t border-[#003d2b]">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h4 className="text-white font-black text-xl mb-6 tracking-wide">{t('footer.title')}</h4>
        <div className="space-y-3 mb-6 font-medium text-sm md:text-base">
          <p>{t('footer.info1')}</p>
          <p>{t('footer.info2')}</p>
          <p>{t('footer.info3')}</p>
          <p className="text-emerald-500 mt-4">{t('footer.bank')}</p>
        </div>

        {/* Legal Policy Links */}
        <div className="flex flex-wrap justify-center items-center gap-4 md:gap-6 my-6 text-xs md:text-sm font-semibold text-emerald-300">
          <button
            onClick={() => setLegalType && setLegalType('privacy')}
            className="hover:text-yellow-400 transition-colors underline underline-offset-4 decoration-emerald-500/50 hover:decoration-yellow-400"
          >
            {t('legal.privacyTitle')}
          </button>
          <span className="text-emerald-700">|</span>
          <button
            onClick={() => setLegalType && setLegalType('terms')}
            className="hover:text-yellow-400 transition-colors underline underline-offset-4 decoration-emerald-500/50 hover:decoration-yellow-400"
          >
            {t('legal.termsTitle')}
          </button>
          <span className="text-emerald-700">|</span>
          <button
            onClick={() => setLegalType && setLegalType('business')}
            className="hover:text-yellow-400 transition-colors underline underline-offset-4 decoration-emerald-500/50 hover:decoration-yellow-400"
          >
            {t('legal.businessTitle')}
          </button>
        </div>

        <div className="pt-6 border-t border-[#003d2b]/50 text-sm font-semibold tracking-wider text-emerald-600/80">
          {t('footer.copyright', `© ${new Date().getFullYear()} S&J Animal Hospital. All rights reserved.`)}
          <br />
          <span className="text-xs font-normal mt-2 inline-block">{t('footer.notice')}</span>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
