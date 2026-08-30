import { useTranslation } from 'react-i18next';

const Footer = ({ setLegalType }) => {
  const { t } = useTranslation();

  return (
    <footer className="bg-slate-950 text-slate-400 pt-10 pb-28 md:pt-16 md:pb-32 border-t border-slate-800">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h4 className="text-white font-black text-xl mb-6 tracking-wide">{t('footer.title')}</h4>
        <div className="space-y-2.5 mb-6 font-medium text-xs sm:text-sm md:text-base text-slate-300">
          <p>{t('footer.info1')}</p>
          <p>{t('footer.info2')}</p>
          <p>{t('footer.info3')}</p>
          <p className="text-emerald-400 font-bold mt-4">{t('footer.bank')}</p>
        </div>

        {/* Legal Policy Links */}
        <div className="flex flex-wrap justify-center items-center gap-4 md:gap-6 my-6 text-xs md:text-sm font-semibold text-slate-400">
          <button
            onClick={() => setLegalType && setLegalType('privacy')}
            className="hover:text-yellow-400 transition-colors underline underline-offset-4 decoration-slate-600 hover:decoration-yellow-400 cursor-pointer"
          >
            {t('legal.privacyTitle')}
          </button>
          <span className="text-slate-700">|</span>
          <button
            onClick={() => setLegalType && setLegalType('terms')}
            className="hover:text-yellow-400 transition-colors underline underline-offset-4 decoration-slate-600 hover:decoration-yellow-400 cursor-pointer"
          >
            {t('legal.termsTitle')}
          </button>
          <span className="text-slate-700">|</span>
          <button
            onClick={() => setLegalType && setLegalType('business')}
            className="hover:text-yellow-400 transition-colors underline underline-offset-4 decoration-slate-600 hover:decoration-yellow-400 cursor-pointer"
          >
            {t('legal.businessTitle')}
          </button>
        </div>

        <div className="pt-6 border-t border-slate-800 text-xs sm:text-sm font-medium tracking-wider text-slate-500">
          {t('footer.copyright', `© ${new Date().getFullYear()} S&J Animal Hospital. All rights reserved.`)}
          <br />
          <span className="text-xs font-normal mt-2 inline-block text-slate-500">{t('footer.notice')}</span>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
