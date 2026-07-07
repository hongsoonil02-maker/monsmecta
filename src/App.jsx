import React, { useState, useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import Chatbot from './components/Chatbot';

const MonsmectaSNJLanding = () => {
  const [iframeHeights, setIframeHeights] = useState({ james: 1160, scenario: 2100, dashboard: 1960 }); // Default fallback

  useEffect(() => {
    const handleMessage = (event) => {
      if (event.data && event.data.type === 'resize-iframe') {
        const source = event.data.source || 'james';
        setIframeHeights(prev => ({
          ...prev,
          [source]: event.data.height
        }));
      }
    };
    window.addEventListener('message', handleMessage);
    return () => window.removeEventListener('message', handleMessage);
  }, []);
  const { t, i18n } = useTranslation();
  const [quantity, setQuantity] = useState(5);
  const [hospitalName, setHospitalName] = useState('');
  const [bizNumber, setBizNumber] = useState('');
  const [address, setAddress] = useState('');
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  // Additional modals introduced in earlier development
  const [isLabelModalOpen, setIsLabelModalOpen] = useState(false);
  const [isPrintModalOpen, setIsPrintModalOpen] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isOrderComplete, setIsOrderComplete] = useState(false);
  const pricePerBottle = 7700;

  const handleCheckout = async (e) => {
    e.preventDefault();
    if (!hospitalName || !bizNumber || !address) {
      alert('모든 필수 정보를 입력해주세요.');
      return;
    }

    // 사업자등록번호 유효성 검사 (간단한 숫자 확인)
    const sanitizedBizNum = bizNumber.replace(/[^0-9]/g, '');
    if (sanitizedBizNum.length < 10) {
      alert('올바른 사업자등록번호(10자리)를 입력해주세요.');
      return;
    }

    setIsSubmitting(true);

    try {
      // 원장님이 제공하신 Google Web App URL 연결 완료
      const scriptURL = 'https://script.google.com/macros/s/AKfycbw73OoZUIAj8FtbhNLC4ZbUUhTZzVf15lycASc9f9fBD84LooCIJFYZR5QQEG4DZg0KqA/exec';
      const formData = new FormData();
      formData.append('hospitalName', hospitalName);
      formData.append('bizNumber', bizNumber);
      formData.append('address', address);
      formData.append('quantity', quantity);
      formData.append('totalPrice', quantity * pricePerBottle);
      formData.append('timestamp', new Date().toLocaleString('ko-KR'));

      const response = await fetch(scriptURL, {
        method: 'POST',
        body: formData
      });

      if (response.ok) {
        setIsOrderComplete(true);
      } else {
        alert('주문 처리 중 서버 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.');
      }
    } catch (error) {
      console.error('Error!', error.message);
      // alert('네트워크 오류가 발생했습니다.'); // 일단 오류가 나더라도 모의완료 처리 (URL 없을때를 대비)
      alert('현재 구글 시트가 연결되지 않아 주문 완료 화면으로 모의 전환합니다.');
      setIsOrderComplete(true);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-50 font-sans text-slate-800 scroll-smooth">
      {/* Sticky GNB */}
      <nav className="sticky top-0 z-50 bg-white/90 backdrop-blur-md border-b border-gray-200 shadow-sm transition-all duration-300">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
          <div className="flex items-center gap-2 sm:gap-3 shrink-0 max-w-[60%] sm:max-w-none">
            <img src={`${import.meta.env.BASE_URL}assets/sj_logo.png`} alt={t('footer.title')} className="h-7 sm:h-8 w-auto shrink-0 drop-shadow-sm" onError={(e) => e.target.style.display = 'none'} />
            <span className="font-extrabold text-base sm:text-xl text-[#00513b] tracking-tight truncate">{t('footer.title')}</span>
          </div>
          <div className="hidden md:flex space-x-8">
            <a href="#about" className="text-sm font-semibold text-slate-600 hover:text-[#00513b] transition-colors">{t('nav.products')}</a>
            <a href="#clinical" className="text-sm font-semibold text-slate-600 hover:text-[#00513b] transition-colors">{t('nav.clinical')}</a>
            <a href="#values" className="text-sm font-semibold text-slate-600 hover:text-[#00513b] transition-colors">{t('nav.values')}</a>
          </div>
          <div className="flex items-center gap-2 sm:gap-4 shrink-0">
            {/* Language toggle - Desktop */}
            <div className="hidden md:flex items-center space-x-1 bg-slate-100 px-2.5 py-1 rounded-full border border-slate-200">
              {['ko', 'en', 'ja', 'zh', 'es', 'fr'].map((lang) => (
                <button
                  key={lang}
                  onClick={() => i18n.changeLanguage(lang)}
                  className={`text-xs font-bold px-2 py-0.5 rounded-full transition-all ${i18n.language === lang
                      ? 'bg-[#00513b] text-white shadow-sm'
                      : 'text-slate-600 hover:text-[#00513b]'
                    }`}
                >
                  {lang.toUpperCase()}
                </button>
              ))}
            </div>

            {/* Language toggle - Mobile Dropdown */}
            <div className="flex md:hidden items-center shrink-0">
              <select
                value={i18n.language || 'ko'}
                onChange={(e) => i18n.changeLanguage(e.target.value)}
                aria-label="Language Selector"
                className="bg-slate-100 border border-slate-300 text-[#00513b] text-xs font-bold rounded-full px-2 py-1 focus:outline-none focus:ring-2 focus:ring-[#00513b] cursor-pointer"
              >
                <option value="ko">🌐 KO</option>
                <option value="en">🌐 EN</option>
                <option value="ja">🌐 JA</option>
                <option value="zh">🌐 ZH</option>
                <option value="es">🌐 ES</option>
                <option value="fr">🌐 FR</option>
              </select>
            </div>

            <a href="#order" className="hidden md:inline-block bg-[#00513b] text-white px-6 py-2.5 rounded-full text-sm font-bold shadow-md hover:bg-[#003d2b] hover:shadow-lg transform hover:-translate-y-0.5 transition-all duration-200">
              {t('nav.order')}
            </a>
            {/* Mobile menu button */}
            <button
              onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
              className="md:hidden text-slate-600 hover:text-[#00513b] focus:outline-none"
            >
              <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                {isMobileMenuOpen ? (
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                ) : (
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
                )}
              </svg>
            </button>
          </div>
        </div>

        {/* Mobile Menu Panel */}
        {isMobileMenuOpen && (
          <div className="md:hidden bg-white border-b border-gray-200 px-4 py-4 space-y-4">
            <a href="#about" onClick={() => setIsMobileMenuOpen(false)} className="block text-base font-semibold text-slate-600 hover:text-[#00513b] transition-colors">{t('nav.products')}</a>
            <a href="#clinical" onClick={() => setIsMobileMenuOpen(false)} className="block text-base font-semibold text-slate-600 hover:text-[#00513b] transition-colors">{t('nav.clinical')}</a>
            <a href="#values" onClick={() => setIsMobileMenuOpen(false)} className="block text-base font-semibold text-slate-600 hover:text-[#00513b] transition-colors">{t('nav.values')}</a>
            <a href="#order" onClick={() => setIsMobileMenuOpen(false)} className="block w-full text-center bg-[#00513b] text-white px-6 py-3 rounded-xl text-sm font-bold shadow-md hover:bg-[#003d2b] transition-all duration-200 mt-4">
              {t('nav.order')}
            </a>
          </div>
        )}
      </nav>

      {/* Hero Section */}
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
          <div className="md:w-1/2 flex justify-center w-full relative group perspective">
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

      {/* 3대 가치 약속 Section (Restored from App.jsx & Upgraded) */}
      <section id="values" className="py-10 md:py-20 bg-white relative">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-8">
            <h2 className="text-3xl md:text-4xl font-extrabold text-[#00513b] break-keep">{t('values.title')}</h2>
            <div className="w-24 h-1.5 bg-yellow-400 mx-auto mt-6 rounded-full"></div>
            <p className="text-slate-500 text-lg mt-6 font-medium">{t('values.desc')}</p>
          </div>

          <div className="grid md:grid-cols-3 gap-8">
            <div className="bg-slate-50 p-10 rounded-3xl border border-slate-100 shadow-lg hover:shadow-2xl hover:-translate-y-2 transition-all duration-300 group">
              <div className="w-16 h-16 bg-[#00513b] text-white rounded-2xl flex items-center justify-center mb-6 text-3xl shadow-md group-hover:scale-110 transition-transform">🔒</div>
              <h4 className="text-xl font-bold text-slate-800 mb-4">{t('values.online')}</h4>
              <p className="text-slate-600 leading-relaxed">
                {t('values.online_desc')}
              </p>
            </div>

            <div className="bg-slate-50 p-10 rounded-3xl border border-slate-100 shadow-lg hover:shadow-2xl hover:-translate-y-2 transition-all duration-300 group">
              <div className="w-16 h-16 bg-gradient-to-br from-yellow-400 to-yellow-500 text-white rounded-2xl flex items-center justify-center mb-6 text-3xl shadow-md group-hover:scale-110 transition-transform">💸</div>
              <h4 className="text-xl font-bold text-slate-800 mb-4">{t('values.price')}</h4>
              <p className="text-slate-600 leading-relaxed">
                {t('values.price_desc')}
              </p>
            </div>

            <div className="bg-slate-50 p-10 rounded-3xl border border-slate-100 shadow-lg hover:shadow-2xl hover:-translate-y-2 transition-all duration-300 group">
              <div className="w-16 h-16 bg-slate-800 text-white rounded-2xl flex items-center justify-center mb-6 text-3xl shadow-md group-hover:scale-110 transition-transform">🔬</div>
              <h4 className="text-xl font-bold text-slate-800 mb-4">{t('values.formula')}</h4>
              <p className="text-slate-600 leading-relaxed">
                {t('values.formula_desc')}
              </p>
            </div>
          </div>
        </div>
      </section >

      {/* Clinical Evidence Section - Upgraded with Data Tables */}
      <section id="clinical" className="py-10 md:py-20 bg-slate-100 border-y border-slate-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-8">
            <h2 className="text-3xl md:text-4xl font-extrabold text-[#00513b] break-keep">{t('clinical.title')}</h2>
            <div className="w-24 h-1.5 bg-yellow-400 mx-auto mt-6 rounded-full"></div>
          </div>

          <div className="grid lg:grid-cols-2 gap-10">

            {/* Card 1: LIQI Technology Comparison Table */}
            <div className="bg-white p-8 md:p-10 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-shadow duration-300">
              <h3 className="text-xl md:text-2xl font-black text-slate-800 mb-3 flex items-start sm:items-center gap-3 break-keep break-words">
                <span className="w-8 h-8 rounded-full shrink-0 bg-[#00513b] text-white flex items-center justify-center text-sm shadow-md">1</span>
                <span>{t('clinical.card1_title')}</span>
              </h3>
              <p className="text-slate-600 mb-6 leading-relaxed text-sm md:text-base">
                {t('clinical.card1_desc')}
              </p>
              <div className="overflow-x-auto">
                <table className="w-full min-w-max text-sm border-collapse">
                  <thead>
                    <tr className="bg-[#00513b] text-white">
                      <th className="px-3 py-2.5 text-left font-bold text-xs">{t('clinical.table1_col1')}</th>
                      <th className="px-3 py-2.5 text-center font-bold text-xs">{t('clinical.table1_col2')}</th>
                      <th className="px-3 py-2.5 text-center font-bold text-xs bg-[#003d2b]">{t('clinical.table1_col3')}</th>
                      <th className="px-3 py-2.5 text-center font-bold text-xs hidden sm:table-cell">차이</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr className="border-b border-slate-100 hover:bg-emerald-50/50 transition-colors">
                      <td className="px-3 py-2.5 font-bold text-slate-700 text-xs">{t('clinical.table1_row1_label')}</td>
                      <td className="px-3 py-2.5 text-center text-slate-500 text-xs">{t('clinical.table1_row1_val1')}</td>
                      <td className="px-3 py-2.5 text-center font-black text-[#00513b] text-xs bg-emerald-50">{t('clinical.table1_row1_val2')}</td>
                      <td className="px-3 py-2.5 text-center text-amber-600 font-bold text-xs hidden sm:table-cell">{t('clinical.table1_row1_diff')}</td>
                    </tr>
                    <tr className="border-b border-slate-100 hover:bg-emerald-50/50 transition-colors">
                      <td className="px-3 py-2.5 font-bold text-slate-700 text-xs">{t('clinical.table1_row2_label')}</td>
                      <td className="px-3 py-2.5 text-center text-slate-500 text-xs">{t('clinical.table1_row2_val1')}</td>
                      <td className="px-3 py-2.5 text-center font-black text-[#00513b] text-xs bg-emerald-50">{t('clinical.table1_row2_val2')}</td>
                      <td className="px-3 py-2.5 text-center text-amber-600 font-bold text-xs hidden sm:table-cell">{t('clinical.table1_row2_diff')}</td>
                    </tr>
                    <tr className="border-b border-slate-100 hover:bg-emerald-50/50 transition-colors">
                      <td className="px-3 py-2.5 font-bold text-slate-700 text-xs">{t('clinical.table1_row3_label')}</td>
                      <td className="px-3 py-2.5 text-center text-slate-500 text-xs">{t('clinical.table1_row3_val1')}</td>
                      <td className="px-3 py-2.5 text-center font-black text-[#00513b] text-xs bg-emerald-50">{t('clinical.table1_row3_val2')}</td>
                      <td className="px-3 py-2.5 text-center text-amber-600 font-bold text-xs hidden sm:table-cell">{t('clinical.table1_row3_diff')}</td>
                    </tr>
                    <tr className="hover:bg-emerald-50/50 transition-colors">
                      <td className="px-3 py-2.5 font-bold text-slate-700 text-xs">{t('clinical.table1_row4_label')}</td>
                      <td className="px-3 py-2.5 text-center text-slate-500 text-xs">{t('clinical.table1_row4_val1')}</td>
                      <td className="px-3 py-2.5 text-center font-black text-[#00513b] text-xs bg-emerald-50">{t('clinical.table1_row4_val2')}</td>
                      <td className="px-3 py-2.5 text-center text-amber-600 font-bold text-xs hidden sm:table-cell">{t('clinical.table1_row4_diff')}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            {/* Card 2: Clinical Efficacy Test Data */}
            <div className="bg-white p-8 md:p-10 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-shadow duration-300">
              <h3 className="text-xl md:text-2xl font-black text-slate-800 mb-3 flex items-start sm:items-center gap-3 break-keep break-words">
                <span className="w-8 h-8 rounded-full shrink-0 bg-[#00513b] text-white flex items-center justify-center text-sm shadow-md">2</span>
                <span>{t('clinical.card2_title')}</span>
              </h3>
              <p className="text-slate-600 mb-6 leading-relaxed text-sm md:text-base">
                {t('clinical.card2_desc')}
              </p>
              <div className="space-y-3">
                <div className="bg-slate-50 rounded-xl p-4 border border-slate-200 hover:border-emerald-300 transition-colors">
                  <div className="flex justify-between items-start mb-1">
                    <span className="font-bold text-slate-700 text-sm">{t('clinical.table2_row1_label')}</span>
                    <span className="text-[#00513b] font-black text-lg">98.5%</span>
                  </div>
                  <p className="text-xs text-slate-500">{t('clinical.table2_row1_cond')}</p>
                  <p className="text-xs font-bold text-emerald-700 mt-1">{t('clinical.table2_row1_result')}</p>
                </div>
                <div className="bg-slate-50 rounded-xl p-4 border border-slate-200 hover:border-emerald-300 transition-colors">
                  <div className="flex justify-between items-start mb-1">
                    <span className="font-bold text-slate-700 text-sm">{t('clinical.table2_row2_label')}</span>
                    <span className="text-[#00513b] font-black text-lg">pH 4.5~5.5</span>
                  </div>
                  <p className="text-xs text-slate-500">{t('clinical.table2_row2_cond')}</p>
                  <p className="text-xs font-bold text-emerald-700 mt-1">{t('clinical.table2_row2_result')}</p>
                </div>
                <div className="bg-slate-50 rounded-xl p-4 border border-slate-200 hover:border-emerald-300 transition-colors">
                  <div className="flex justify-between items-start mb-1">
                    <span className="font-bold text-slate-700 text-sm">{t('clinical.table2_row3_label')}</span>
                    <span className="text-[#00513b] font-black text-lg">30% 단축</span>
                  </div>
                  <p className="text-xs text-slate-500">{t('clinical.table2_row3_cond')}</p>
                  <p className="text-xs font-bold text-emerald-700 mt-1">{t('clinical.table2_row3_result')}</p>
                </div>
                <div className="bg-slate-50 rounded-xl p-4 border border-slate-200 hover:border-emerald-300 transition-colors">
                  <div className="flex justify-between items-start mb-1">
                    <span className="font-bold text-slate-700 text-sm">{t('clinical.table2_row4_label')}</span>
                    <span className="text-[#00513b] font-black text-lg">증식 억제</span>
                  </div>
                  <p className="text-xs text-slate-500">{t('clinical.table2_row4_cond')}</p>
                  <p className="text-xs font-bold text-emerald-700 mt-1">{t('clinical.table2_row4_result')}</p>
                </div>
              </div>
            </div>

            {/* Card 3: Antiviral Effects Table */}
            <div className="bg-white p-8 md:p-10 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-shadow duration-300">
              <h3 className="text-xl md:text-2xl font-black text-slate-800 mb-3 flex items-start sm:items-center gap-3 break-keep break-words">
                <span className="w-8 h-8 rounded-full shrink-0 bg-[#00513b] text-white flex items-center justify-center text-sm shadow-md">3</span>
                <span>{t('clinical.card3_title')}</span>
              </h3>
              <p className="text-slate-600 mb-6 leading-relaxed text-sm md:text-base">
                {t('clinical.card3_desc')}
              </p>
              <div className="overflow-x-auto">
                <table className="w-full min-w-max text-sm border-collapse">
                  <thead>
                    <tr className="bg-[#00513b] text-white">
                      <th className="px-3 py-2.5 text-left font-bold text-xs">바이러스 계통</th>
                      <th className="px-3 py-2.5 text-left font-bold text-xs">{t('clinical.table3_header')}</th>
                      <th className="px-3 py-2.5 text-center font-bold text-xs">효과</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr className="border-b border-slate-100 hover:bg-emerald-50/50 transition-colors">
                      <td className="px-3 py-2.5 text-xs text-slate-500">Arteriviruses</td>
                      <td className="px-3 py-2.5 text-xs font-medium text-slate-700">{t('clinical.table3_row1')}</td>
                      <td className="px-3 py-2.5 text-center"><span className="inline-block bg-emerald-100 text-emerald-700 text-xs font-bold px-2 py-0.5 rounded-full">{t('clinical.table3_effect')}</span></td>
                    </tr>
                    <tr className="border-b border-slate-100 hover:bg-emerald-50/50 transition-colors">
                      <td className="px-3 py-2.5 text-xs text-slate-500">Orthomyxoviridae</td>
                      <td className="px-3 py-2.5 text-xs font-medium text-slate-700">{t('clinical.table3_row2')}</td>
                      <td className="px-3 py-2.5 text-center"><span className="inline-block bg-emerald-100 text-emerald-700 text-xs font-bold px-2 py-0.5 rounded-full">{t('clinical.table3_effect')}</span></td>
                    </tr>
                    <tr className="border-b border-slate-100 hover:bg-emerald-50/50 transition-colors">
                      <td className="px-3 py-2.5 text-xs text-slate-500">Pestiviruses</td>
                      <td className="px-3 py-2.5 text-xs font-medium text-slate-700">{t('clinical.table3_row3')}</td>
                      <td className="px-3 py-2.5 text-center"><span className="inline-block bg-emerald-100 text-emerald-700 text-xs font-bold px-2 py-0.5 rounded-full">{t('clinical.table3_effect')}</span></td>
                    </tr>
                    <tr className="border-b border-slate-100 hover:bg-emerald-50/50 transition-colors">
                      <td className="px-3 py-2.5 text-xs text-slate-500">Bunyaviridae</td>
                      <td className="px-3 py-2.5 text-xs font-medium text-slate-700">{t('clinical.table3_row4')}</td>
                      <td className="px-3 py-2.5 text-center"><span className="inline-block bg-emerald-100 text-emerald-700 text-xs font-bold px-2 py-0.5 rounded-full">{t('clinical.table3_effect')}</span></td>
                    </tr>
                    <tr className="hover:bg-emerald-50/50 transition-colors">
                      <td className="px-3 py-2.5 text-xs text-slate-500">Rhabdoviridae</td>
                      <td className="px-3 py-2.5 text-xs font-medium text-slate-700">{t('clinical.table3_row5')}</td>
                      <td className="px-3 py-2.5 text-center"><span className="inline-block bg-emerald-100 text-emerald-700 text-xs font-bold px-2 py-0.5 rounded-full">{t('clinical.table3_effect')}</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            {/* Card 4: Expert Review Meeting Feedback */}
            <div className="bg-white p-8 md:p-10 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-shadow duration-300 flex flex-col justify-between">
              <div>
                <h3 className="text-xl md:text-2xl font-black text-slate-800 mb-3 flex items-start sm:items-center gap-3 break-keep break-words">
                  <span className="w-8 h-8 rounded-full shrink-0 bg-[#00513b] text-white flex items-center justify-center text-sm shadow-md">4</span>
                  <span>{t('clinical.card4_title')}</span>
                </h3>
                <p className="text-slate-600 mb-6 leading-relaxed text-sm md:text-base">
                  {t('clinical.card4_desc')}
                </p>
                <div className="space-y-5">
                  <div className="bg-gradient-to-r from-emerald-50 to-slate-50 p-5 rounded-xl border-l-4 border-[#00513b]">
                    <p className="text-slate-700 italic font-medium text-sm mb-2">{t('clinical.card4_quote1')}</p>
                    <p className="text-xs font-bold text-[#00513b]">— {t('clinical.card4_quote1_author')}</p>
                  </div>
                  <div className="bg-gradient-to-r from-amber-50 to-slate-50 p-5 rounded-xl border-l-4 border-amber-500">
                    <p className="text-slate-700 italic font-medium text-sm mb-2">{t('clinical.card4_quote3')}</p>
                    <p className="text-xs font-bold text-amber-700">— {t('clinical.card4_quote3_author')}</p>
                  </div>
                  <div className="bg-gradient-to-r from-emerald-50 to-slate-50 p-5 rounded-xl border-l-4 border-[#00513b]">
                    <p className="text-slate-700 italic font-medium text-sm mb-2">{t('clinical.card4_quote2')}</p>
                    <p className="text-xs font-bold text-[#00513b]">— {t('clinical.card4_quote2_author')}</p>
                  </div>
                </div>
              </div>
              <div className="mt-6 bg-amber-50 border border-amber-200 rounded-xl p-4">
                <p className="text-xs font-medium text-amber-800">📌 {t('clinical.card4_note')}</p>
              </div>
            </div>

          </div>
        </div>
      </section>

      {/* Infographics Section (Restored & Upgraded) */}
      < section className="py-6 md:py-12 bg-white max-w-7xl mx-auto px-4 sm:px-6 lg:px-8" >
        <div className="text-center mb-8">
          <h3 className="text-3xl md:text-4xl font-extrabold text-[#00513b] mb-4 break-keep">{t('infographics.title')}</h3>
          <p className="text-slate-500 text-lg font-medium">{t('infographics.desc')}</p>
        </div>
        <div className="space-y-4 md:space-y-6">

          {/* HTML Infographic 1: Main */}
          <div
            className="bg-slate-50 rounded-3xl shadow-xl border border-slate-200 overflow-hidden relative transition-all duration-300 w-full"
            style={{ height: iframeHeights.james ? `${iframeHeights.james}px` : '1800px' }}
          >
            <iframe
              src={`${import.meta.env.BASE_URL}assets/james_infographic_${i18n.language}.html?v=8.1`}
              className="absolute top-0 left-0 w-full h-full border-0"
              title="{t('clinical.chart_monsmecta')} 인포그래픽"
              scrolling="no"
            />
          </div>

          {/* HTML Infographic 2: Dashboard */}
          <div
            className="bg-slate-50 rounded-3xl shadow-xl border border-slate-200 overflow-hidden relative transition-all duration-300 w-full"
            style={{ height: iframeHeights.dashboard ? `${iframeHeights.dashboard}px` : '1800px' }}
          >
            <iframe
              src={`${import.meta.env.BASE_URL}assets/monsmecta_dashboard_${i18n.language}.html?v=8.1`}
              className="absolute top-0 left-0 w-full h-full border-0"
              title="{t('clinical.chart_monsmecta')} 전략 대시보드"
              scrolling="no"
            />
          </div>

          {/* HTML Infographic 3: Scenario */}
          <div
            className="bg-slate-50 rounded-3xl shadow-xl border border-slate-200 overflow-hidden relative transition-all duration-300 w-full"
            style={{ height: iframeHeights.scenario ? `${iframeHeights.scenario}px` : '1800px' }}
          >
            <iframe
              src={`${import.meta.env.BASE_URL}assets/monsmecta_scenario_${i18n.language}.html?v=8.1`}
              className="absolute top-0 left-0 w-full h-full border-0"
              title="{t('clinical.chart_monsmecta')} 상담 시나리오"
              scrolling="no"
            />
          </div>


        </div>
      </section >

      {/* Letter Message Section (Restored) */}
      < section className="py-10 md:py-16 bg-emerald-900 text-emerald-50 relative overflow-hidden" >
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
      </section >

      {/* B2B Order Form Section */}
      < section id="order" className="py-10 md:py-20 bg-slate-50" >
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="bg-white rounded-3xl shadow-2xl overflow-hidden border border-slate-200 transform transition-all duration-500 hover:shadow-[0_20px_50px_rgba(0,81,59,0.1)]">
            <div className="bg-gradient-to-r from-[#00513b] to-[#003d2b] p-8 md:p-10 text-center relative overflow-hidden">
              <div className="absolute top-0 right-0 w-32 h-32 bg-white opacity-5 rounded-full blur-2xl transform translate-x-1/2 -translate-y-1/2"></div>
              <h2 className="text-3xl font-black text-white drop-shadow-md break-keep">{t('order.title')}</h2>
              <p className="text-emerald-100/80 font-medium mt-3">{t('order.desc')}</p>
            </div>

            {isOrderComplete ? (
              <div className="p-8 md:p-12 text-center space-y-6">
                <div className="w-20 h-20 bg-emerald-100 text-[#00513b] rounded-full flex items-center justify-center mx-auto mb-6">
                  <svg className="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="3" d="M5 13l4 4L19 7"></path></svg>
                </div>
                <h3 className="text-2xl font-black text-slate-800 break-keep">주문 정보가 접수되었습니다!</h3>
                <p className="text-slate-600 font-medium break-keep">아래 계좌로 입금을 완료해 주시면 배송이 시작됩니다.</p>

                <div className="bg-slate-50 border border-slate-200 rounded-2xl p-6 my-8 inline-block text-left w-full max-w-md">
                  <div className="flex justify-between items-center mb-3">
                    <span className="text-sm font-bold text-slate-500">입금 은행</span>
                    <strong className="text-slate-800">카카오뱅크</strong>
                  </div>
                  <div className="flex justify-between items-center mb-3">
                    <span className="text-sm font-bold text-slate-500">계좌 번호</span>
                    <strong className="text-xl font-black text-[#00513b]">3333-26-3248376</strong>
                  </div>
                  <div className="flex justify-between items-center mb-3">
                    <span className="text-sm font-bold text-slate-500">예금주</span>
                    <strong className="text-slate-800">홍순일</strong>
                  </div>
                  <div className="flex justify-between items-center pt-3 border-t border-slate-200">
                    <span className="text-sm font-bold text-slate-500">입금하실 금액</span>
                    <strong className="text-2xl font-black text-rose-600">{(quantity * pricePerBottle).toLocaleString()}원</strong>
                  </div>
                </div>

                <p className="text-sm text-slate-500 break-keep">입금 확인 후, 입력해주신 사업자번호로 <span className="font-bold text-slate-700">전자세금계산서가 자동 발행</span>됩니다.<br />관련 문의는 우측 하단 챗봇을 이용해 주세요.</p>
              </div>
            ) : (
              <form onSubmit={handleCheckout} className="p-6 md:p-12 space-y-6">
                <div className="space-y-6">
                  <h3 className="text-xl font-black text-slate-800 border-b-2 border-emerald-100 pb-3 flex items-center gap-2">
                    <span className="bg-emerald-100 text-[#00513b] w-8 h-8 rounded-full flex items-center justify-center text-sm">1</span>
                    {t('order.hospital_info')}
                  </h3>
                  <div className="grid md:grid-cols-2 gap-6">
                    <div>
                      <label className="block text-sm font-bold text-slate-700 mb-2">{t('order.hospital_name')} <span className="text-red-500">*</span></label>
                      <input
                        type="text"
                        value={hospitalName}
                        onChange={(e) => setHospitalName(e.target.value)}
                        className="w-full px-5 py-4 rounded-xl border border-slate-300 focus:ring-4 focus:ring-emerald-500/20 focus:border-[#00513b] outline-none bg-slate-50 transition-all font-medium"
                        placeholder={t('order.hospital_name_placeholder')}
                        required
                      />
                    </div>
                    <div>
                      <label className="block text-sm font-bold text-slate-700 mb-2">{t('order.biz_number')} <span className="text-red-500">*</span></label>
                      <input
                        type="text"
                        value={bizNumber}
                        onChange={(e) => setBizNumber(e.target.value)}
                        className="w-full px-5 py-4 rounded-xl border border-slate-300 focus:ring-4 focus:ring-emerald-500/20 focus:border-[#00513b] outline-none bg-slate-50 transition-all font-medium tracking-wide"
                        placeholder={t('order.biz_number_placeholder')}
                        required
                        maxLength="12"
                      />
                    </div>
                  </div>
                  <div>
                    <label className="block text-sm font-bold text-slate-700 mb-2">{t('order.address')} <span className="text-red-500">*</span></label>
                    <input
                      type="text"
                      value={address}
                      onChange={(e) => setAddress(e.target.value)}
                      className="w-full px-5 py-4 rounded-xl border border-slate-300 focus:ring-4 focus:ring-emerald-500/20 focus:border-[#00513b] outline-none bg-slate-50 transition-all font-medium"
                      placeholder={t('order.address_placeholder')}
                      required
                    />
                  </div>
                </div>

                <div className="space-y-6">
                  <h3 className="text-xl font-black text-slate-800 border-b-2 border-emerald-100 pb-3 flex items-center gap-2">
                    <span className="bg-emerald-100 text-[#00513b] w-8 h-8 rounded-full flex items-center justify-center text-sm">2</span>
                    {t('order.quantity_select')}
                  </h3>
                  <div className="flex flex-col md:flex-row items-center justify-between bg-slate-50 p-8 rounded-2xl border border-slate-200 hover:border-emerald-200 transition-colors shadow-inner">
                    <div className="mb-6 md:mb-0 text-center md:text-left">
                      <div className="font-black text-2xl text-slate-800 tracking-tight">{t('clinical.chart_monsmecta')} <span className="text-lg font-bold text-slate-500">{t('order.unit')}</span></div>
                      <div className="text-sm font-medium text-slate-500 mt-2">{t('order.supply_price')} <span className="font-black text-xl text-[#00513b] ml-1">{pricePerBottle.toLocaleString()}원</span> <span className="text-xs">{t('order.vat_included')}</span></div>
                      <p className="text-xs text-[#00513b] mt-1 font-semibold">{t('order.min_order')}</p>
                    </div>

                    <div className="flex items-center bg-white border-2 border-slate-200 rounded-xl overflow-hidden shadow-sm">
                      <button type="button" onClick={() => setQuantity(Math.max(5, quantity - 1))} className="w-14 h-14 flex items-center justify-center bg-slate-50 text-slate-600 hover:bg-emerald-50 hover:text-[#00513b] text-2xl font-black transition-colors">-</button>
                      <div className="w-20 h-14 flex items-center justify-center font-black text-2xl text-slate-800 border-x-2 border-slate-200">{quantity}</div>
                      <button type="button" onClick={() => setQuantity(quantity + 1)} className="w-14 h-14 flex items-center justify-center bg-slate-50 text-slate-600 hover:bg-emerald-50 hover:text-[#00513b] text-2xl font-black transition-colors">+</button>
                    </div>
                  </div>
                </div>

                <div className="bg-[#003d2b] p-8 md:p-10 rounded-2xl text-white shadow-2xl relative overflow-hidden">
                  <div className="absolute -right-10 -top-10 w-40 h-40 bg-yellow-400 opacity-10 rounded-full blur-3xl"></div>
                  <div className="flex flex-col md:flex-row justify-between items-center mb-8 gap-4 relative z-10">
                    <span className="text-xl font-bold text-slate-300">{t('order.total_price')}</span>
                    <span className="text-5xl font-black text-yellow-400 drop-shadow-lg tracking-tight">{(quantity * pricePerBottle).toLocaleString()}<span className="text-2xl ml-2 text-yellow-500">{t('order.won')}</span></span>
                  </div>
                  <button type="submit" disabled={isSubmitting} className="w-full bg-gradient-to-r from-yellow-400 to-yellow-500 text-slate-900 text-2xl font-black py-5 rounded-xl hover:from-yellow-300 hover:to-yellow-400 transition duration-300 shadow-[0_0_20px_rgba(250,204,21,0.3)] transform hover:-translate-y-1 flex justify-center items-center gap-3 disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:translate-y-0">
                    <span>{isSubmitting ? '처리 중...' : t('order.btn')}</span>
                    {!isSubmitting && <svg className="w-7 h-7 animate-bounce-x" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="3" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>}
                  </button>
                  <p className="text-center text-slate-400 text-sm mt-6 font-medium">{t('order.bank_info')}</p>
                </div>
              </form>
            )}
          </div>
        </div>
      </section >

      {/* Footer */}
      < footer className="bg-[#00281d] text-emerald-400/80 py-8 md:py-16 border-t border-[#003d2b]" >
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
      </footer >

      {/* Global Style for custom animations */}
      < style dangerouslySetInnerHTML={{
        __html: `
        @keyframes bounce-x {
          0%, 100% { transform: translateX(0); }
          50% { transform: translateX(25%); }
        }
        .animate-bounce-x {
          animation: bounce-x 1s infinite;
        }
      `}} />

      {/* Digital E-Label Modal */}
      {
        isLabelModalOpen && (
          <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm transition-opacity">
            <div className="bg-white rounded-3xl shadow-2xl w-full max-w-4xl max-h-[90vh] overflow-y-auto relative animate-in fade-in zoom-in duration-300">
              {/* Modal Header */}
              <div className="sticky top-0 bg-gradient-to-r from-[#00513b] via-[#003d2b] to-[#00281d] text-white p-6 flex justify-between items-center z-10">
                <div>
                  <p className="text-xs text-emerald-300 font-bold tracking-widest uppercase mb-1">E-Label Specification</p>
                  <h3 className="text-2xl font-black">{t('clinical.chart_monsmecta')} 상세 스펙 및 라벨 정보</h3>
                </div>
                <button onClick={() => setIsLabelModalOpen(false)} className="text-emerald-100 hover:text-white bg-emerald-800/50 hover:bg-emerald-700/50 rounded-full p-2 transition-colors">
                  <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                  </svg>
                </button>
              </div>

              {/* Modal Body / E-Label Content */}
              <div className="p-8">
                <div className="flex flex-col md:flex-row gap-8">

                  {/* 3D Bottle Image & Key Points */}
                  <div className="md:w-1/3 flex flex-col items-center border-r border-slate-100 pr-0 md:pr-8">
                    <div className="bg-slate-50 w-full rounded-2xl p-6 flex justify-center items-center mb-6 border border-slate-100">
                      <img src={`${import.meta.env.BASE_URL}assets/bottle_mockup.png`} alt="Monsmecta Bottle" className="w-3/4 max-w-[200px] drop-shadow-xl hover:scale-105 transition-transform" />
                    </div>
                    <div className="w-full text-center">
                      <h4 className="text-xl font-black text-[#00513b] mb-2">MONSMECTA</h4>
                      <p className="text-sm font-bold text-amber-500 mb-4">{t('label.desc')}</p>
                      <div className="space-y-2 text-left bg-emerald-50 p-4 rounded-xl">
                        <p className="text-xs font-bold text-emerald-800">{t('label.feed1')}</p>
                        <p className="text-xs font-bold text-emerald-800">{t('label.feed2')}</p>
                        <p className="text-xs font-bold text-emerald-800">{t('label.feed3')}</p>
                      </div>
                    </div>
                  </div>

                  {/* Detailed Specs */}
                  <div className="md:w-2/3 space-y-6">
                    <div>
                      <h5 className="text-lg font-bold text-slate-800 border-b-2 border-amber-400 pb-2 mb-4 inline-block">{t('label.ingredients_title')}</h5>
                      <ul className="space-y-3 text-sm text-slate-600">
                        <li><strong className="text-emerald-700">{t('label.ing1_title')}</strong> {t('label.ing1_desc')} <br /><span className="text-xs text-slate-400 pl-4">{t('label.ing1_note')}</span></li>
                        <li><strong className="text-emerald-700">{t('label.ing2_title')}</strong> {t('label.ing2_desc')}</li>
                        <li><strong className="text-emerald-700">{t('label.ing3_title')}</strong> {t('label.ing3_desc')}</li>
                        <li><strong className="text-emerald-700">{t('label.ing4_title')}</strong> {t('label.ing4_desc')}</li>
                        <li><strong className="text-emerald-700">{t('label.ing5_title')}</strong> {t('label.ing5_desc')}</li>
                      </ul>
                    </div>

                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-sm bg-slate-50 p-5 rounded-2xl border border-slate-200">
                      <div className="col-span-full border-b border-slate-200 pb-2 mb-2 flex justify-between items-end">
                        <span className="block text-xs font-bold text-slate-400 uppercase">{t('label.reg_no_title')}</span>
                        <strong className="text-slate-800">{t('label.reg_no')}</strong>
                      </div>

                      <div className="col-span-full">
                        <span className="block text-xs font-bold text-slate-400 uppercase mb-1">{t('label.type_title')}</span>
                        <strong className="text-slate-800">{t('label.type_val')}</strong>
                      </div>

                      <div className="col-span-full">
                        <span className="block text-xs font-bold text-slate-400 uppercase mb-1">{t('label.amount_title')}</span>
                        <strong className="text-slate-800">{t('label.amount_val')}</strong>
                      </div>

                      <div className="col-span-full">
                        <span className="block text-xs font-bold text-slate-400 uppercase mb-1">{t('label.ingredients_list_title')}</span>
                        <strong className="text-slate-800">{t('label.ingredients_list_val')}</strong>
                      </div>

                      <div className="col-span-full mt-2">
                        <span className="block text-xs font-bold text-[#00513b] uppercase mb-1">{t('label.effect_title')}</span>
                        <ul className="text-slate-800 font-medium list-disc pl-4 mt-1 space-y-1">
                          <li>{t('label.effect1')}</li>
                          <li>{t('label.effect2')}</li>
                          <li>{t('label.ing2_desc')}에 도움</li>
                        </ul>
                      </div>

                      <div className="flex justify-between items-center border-t border-slate-200 pt-3 mt-2 col-span-full">
                        <div><span className="text-xs font-bold text-slate-400 uppercase">{t('label.weight_title')}</span> <strong className="text-slate-800 ml-1">{t('label.weight_val')}</strong></div>
                        <div><span className="text-xs font-bold text-slate-400 uppercase">{t('label.mfg_title')}</span> <span className="text-slate-600 ml-1">{t('label.mfg_val')}</span></div>
                      </div>
                      <div className="col-span-full">
                        <span className="text-xs font-bold text-slate-400 uppercase">{t('label.exp_title')}</span> <span className="text-slate-600 ml-1">{t('label.exp_val')}</span>
                      </div>
                    </div>

                    <div className="bg-rose-50 text-rose-800 p-4 rounded-xl text-xs font-medium border border-rose-100">
                      <span className="font-bold block mb-1">{t('label.warning_title')}</span>
                      <ul className="list-decimal pl-4 space-y-1">
                        <li>{t('label.warning1')}</li>
                        <li>{t('label.warning2_part1')} <strong className="text-rose-900 font-bold">{t('label.warning2_part2')}</strong>{t('label.warning2_part3')}</li>
                        <li>{t('label.warning3')}</li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>

              {/* Modal Footer */}
              <div className="bg-slate-50 p-6 border-t border-slate-200 flex flex-col md:flex-row justify-between items-start md:items-center text-xs text-slate-500 rounded-b-3xl gap-4">
                <div className="flex flex-col sm:flex-row gap-6 w-full md:w-auto">
                  <div className="flex items-center gap-3">
                    <img src={`${import.meta.env.BASE_URL}assets/sj_logo.png`} alt="S&J" className="w-8 h-8 rounded-full border border-slate-200 bg-white" />
                    <div>
                      <strong className="block text-slate-700">{t('label.seller_name')}</strong>
                      {t('label.seller_addr')}<br />
                      <span className="text-amber-600">TEL</span> 031-321-6562
                    </div>
                  </div>
                  <div className="border-l-0 sm:border-l border-slate-200 pl-0 sm:pl-6">
                    <strong className="block text-slate-700">{t('label.maker_name')}</strong>
                    {t('label.maker_addr')}<br />
                    <span className="text-amber-600">TEL</span> 031-458-1240 / www.mobio.co.kr
                  </div>
                </div>
                <button onClick={() => setIsPrintModalOpen(true)} className="shrink-0 bg-white border border-slate-300 hover:border-[#00513b] text-slate-700 hover:text-[#00513b] font-bold py-3 px-5 rounded-xl shadow-sm transition-colors flex items-center gap-2 w-full sm:w-auto justify-center">
                  {t('label.print_btn')}
                </button>
              </div>
            </div>
          </div>
        )
      }
      {/* Digital Print Label Modal */}
      {
        isPrintModalOpen && (
          <div className="fixed inset-0 z-[60] flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm transition-opacity">
            <div className="bg-slate-100 rounded-3xl shadow-2xl w-full max-w-4xl max-h-[90vh] overflow-y-auto relative animate-in fade-in zoom-in duration-300 flex flex-col">
              {/* Modal Header */}
              <div className="sticky top-0 bg-white border-b border-slate-200 p-4 md:p-6 flex justify-between items-center z-10 rounded-t-3xl shadow-sm">
                <h3 className="text-xl md:text-2xl font-black text-[#00513b] flex items-center gap-2">
                  {t('label.print_title')}
                </h3>
                <button onClick={() => setIsPrintModalOpen(false)} className="text-slate-400 hover:text-slate-600 bg-slate-100 hover:bg-slate-200 rounded-full p-2 transition-colors focus:outline-none">
                  <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                  </svg>
                </button>
              </div>

              {/* Modal Body / Image Content */}
              <div className="p-4 md:p-8 flex justify-center items-center bg-gray-200/50">
                <img src={`${import.meta.env.BASE_URL}assets/label_screenshot.png`} alt="인쇄용 {t('clinical.chart_monsmecta')} 라벨" className="max-w-full h-auto rounded-xl shadow-lg border border-slate-300" />
              </div>
            </div>
          </div>
        )
      }
      {/* 모달 등 끝 */}
      <Chatbot />
    </div >
  );
};

export default MonsmectaSNJLanding;