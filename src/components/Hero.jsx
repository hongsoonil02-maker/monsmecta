import React from 'react';
import { useTranslation } from 'react-i18next';

const Hero = ({ setIsLabelModalOpen }) => {
  const { t } = useTranslation();

  return (
    <section id="about" className="relative bg-gradient-to-br from-[#00513b] via-[#004230] to-[#00281d] text-white overflow-hidden py-24 md:py-32">
      <div className="absolute inset-0 opacity-10 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')]"></div>
      <div className="absolute inset-0 opacity-20 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-emerald-400 via-transparent to-transparent mix-blend-overlay"></div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 flex flex-col md:flex-row items-center gap-12">
        <div className="md:w-1/2 space-y-8 text-center md:text-left">
          <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/10 text-sm font-medium border border-white/20 backdrop-blur-sm shadow-xl">
            <span className="w-2.5 h-2.5 rounded-full bg-green-400 animate-pulse shadow-[0_0_8px_rgba(74,222,128,0.8)]"></span>
            {t('heroBadge')}
          </div>
          <h1 className="text-5xl md:text-7xl font-black leading-tight tracking-tight drop-shadow-xl break-keep">
            {t('hero.title').split(',')[0]}<br />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-yellow-300 to-yellow-500 drop-shadow-sm">{t('hero.title').split(',').length > 1 ? t('hero.title').split(',')[1].trim() : ''}</span>
          </h1>
          <p className="text-lg md:text-xl text-emerald-50/90 leading-relaxed max-w-xl mx-auto md:mx-0 font-light">
            {t('hero.subtitle')}
          </p>
          <div className="pt-6 flex flex-col sm:flex-row gap-4 justify-center md:justify-start">
            <a href="#order" className="inline-block text-center bg-gradient-to-r from-yellow-400 to-yellow-500 text-[#00513b] text-lg font-black px-8 py-4 rounded-full shadow-[0_10px_30px_rgba(250,204,21,0.3)] hover:shadow-[0_15px_40px_rgba(250,204,21,0.5)] transform hover:-translate-y-1 hover:scale-105 transition-all duration-300">
              {t('hero.orderBtn')}
            </a>
            <button onClick={() => setIsLabelModalOpen(true)} className="inline-block text-center bg-white/10 backdrop-blur-md border border-white/30 text-white text-lg font-bold px-8 py-4 rounded-full hover:bg-white/20 transform hover:-translate-y-1 transition-all duration-300">
              {t('hero.specBtn')}
            </button>
          </div>
        </div>
        <div className="md:w-1/2 flex justify-center w-full relative group perspective overflow-hidden">
          {/* 3D Mockup & Video Container */}
          <div className="relative w-full max-w-md transform transition-all duration-700 hover:scale-105 z-20">
            <div className="absolute -inset-1 bg-gradient-to-r from-yellow-400 to-emerald-500 rounded-3xl blur opacity-30 group-hover:opacity-50 transition duration-500"></div>
            <div className="relative bg-white rounded-3xl shadow-2xl overflow-hidden border border-white/40">
              <video
                autoPlay
                loop
                muted
                playsInline
                className="w-full h-auto object-cover"
              >
                <source src={`${import.meta.env.BASE_URL}assets/video.mp4`} type="video/mp4" />
              </video>
            </div>

            {/* Real Bottle Photo Overlaid on corner */}
            <div className="absolute -bottom-6 -right-2 w-28 sm:-bottom-10 sm:-right-6 sm:w-40 h-auto drop-shadow-2xl hover:scale-110 transition-transform duration-500 z-30">
              <img src={`${import.meta.env.BASE_URL}assets/bottle_mockup.png`} alt="MONSMECTA Real Bottle" className="w-full h-auto object-contain rounded-2xl border-4 border-white shadow-xl bg-white" />
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;
