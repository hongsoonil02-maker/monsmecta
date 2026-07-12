import React from 'react';
import { useTranslation } from 'react-i18next';

const Footer = () => {
  const { t } = useTranslation();

  return (
    <footer className="bg-[#00281d] text-emerald-400/80 py-8 md:py-16 border-t border-[#003d2b]">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h4 className="text-white font-black text-xl mb-6 tracking-wide">{t('footer.title')}</h4>
        <div className="space-y-3 mb-8 font-medium">
          <p>{t('footer.info1')}</p>
          <p>{t('footer.info2')}</p>
          <p>{t('footer.info3')}</p>
          <p className="text-emerald-500 mt-4">{t('footer.bank')}</p>
        </div>
        <div className="pt-8 border-t border-[#003d2b]/50 text-sm font-semibold tracking-wider text-emerald-600/80">
          © {new Date().getFullYear()} S&J Animal Hospital. All rights reserved.
          <br />
          <span className="text-xs font-normal mt-2 inline-block">{t('footer.notice')}</span>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
