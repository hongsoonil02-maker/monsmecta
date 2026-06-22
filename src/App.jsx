import React, { useState, useEffect } from 'react';

const MonsmectaSNJLanding = () => {
  const [iframeHeight, setIframeHeight] = useState(1800); // Default fallback

  useEffect(() => {
    const handleMessage = (event) => {
      if (event.data && event.data.type === 'resize-iframe') {
        setIframeHeight(event.data.height);
      }
    };
    window.addEventListener('message', handleMessage);
    return () => window.removeEventListener('message', handleMessage);
  }, []);
  const [quantity, setQuantity] = useState(5);
  const [hospitalName, setHospitalName] = useState('');
  const [bizNumber, setBizNumber] = useState('');
  const [address, setAddress] = useState('');
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const pricePerBottle = 7700;

  const handleCheckout = (e) => {
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

    alert(`[${hospitalName}] 원장님, 몬스멕타 ${quantity}병 선결제 시스템으로 이동합니다.`);
  };

  return (
    <div className="min-h-screen bg-slate-50 font-sans text-slate-800 scroll-smooth">
      {/* Sticky GNB */}
      <nav className="sticky top-0 z-50 bg-white/90 backdrop-blur-md border-b border-gray-200 shadow-sm transition-all duration-300">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <img src={`${import.meta.env.BASE_URL}assets/sj_logo.png`} alt="에스앤제이 동물병원 로고" className="h-8 w-auto drop-shadow-sm" onError={(e) => e.target.style.display='none'} />
            <span className="font-extrabold text-xl text-[#00513b] tracking-tight">에스앤제이 동물병원</span>
          </div>
          <div className="hidden md:flex space-x-8">
            <a href="#about" className="text-sm font-semibold text-slate-600 hover:text-[#00513b] transition-colors">제품소개</a>
            <a href="#clinical" className="text-sm font-semibold text-slate-600 hover:text-[#00513b] transition-colors">임상데이터</a>
            <a href="#values" className="text-sm font-semibold text-slate-600 hover:text-[#00513b] transition-colors">3대 가치</a>
          </div>
          <div className="flex items-center gap-4">
            <a href="#order" className="hidden md:inline-block bg-[#00513b] text-white px-6 py-2.5 rounded-full text-sm font-bold shadow-md hover:bg-[#003d2b] hover:shadow-lg transform hover:-translate-y-0.5 transition-all duration-200">
              빠른 발주하기
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
            <a href="#about" onClick={() => setIsMobileMenuOpen(false)} className="block text-base font-semibold text-slate-600 hover:text-[#00513b] transition-colors">제품소개</a>
            <a href="#clinical" onClick={() => setIsMobileMenuOpen(false)} className="block text-base font-semibold text-slate-600 hover:text-[#00513b] transition-colors">임상데이터</a>
            <a href="#values" onClick={() => setIsMobileMenuOpen(false)} className="block text-base font-semibold text-slate-600 hover:text-[#00513b] transition-colors">3대 가치</a>
            <a href="#order" onClick={() => setIsMobileMenuOpen(false)} className="block w-full text-center bg-[#00513b] text-white px-6 py-3 rounded-xl text-sm font-bold shadow-md hover:bg-[#003d2b] transition-all duration-200 mt-4">
              빠른 발주하기
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
              전국 동물병원 전용 B2B 공급망
            </div>
            <h1 className="text-5xl md:text-7xl font-black leading-tight tracking-tight drop-shadow-xl break-keep">
              임상 수의사의 해답,<br />
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-yellow-300 to-yellow-500 drop-shadow-sm">MONSMECTA</span>
            </h1>
            <p className="text-lg md:text-xl text-emerald-50/90 leading-relaxed max-w-xl mx-auto md:mx-0 font-light">
              현장 진료의 까다로운 기준을 통과한 위장관 솔루션. 에스앤제이 동물병원 홍순일 원장이 직접 검증하고 처방합니다.
            </p>
            <div className="pt-6">
              <a href="#order" className="inline-block bg-gradient-to-r from-yellow-400 to-yellow-500 text-[#00513b] text-lg font-black px-10 py-5 rounded-full shadow-[0_10px_30px_rgba(250,204,21,0.3)] hover:shadow-[0_15px_40px_rgba(250,204,21,0.5)] transform hover:-translate-y-1 hover:scale-105 transition-all duration-300">
                원장님 전용 발주서 작성하기
              </a>
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
                  <div className="w-full h-80 bg-slate-100 flex items-center justify-center p-8">
                    <div className="text-center">
                      <div className="text-[#00513b] font-black text-3xl mb-2">MONSMECTA</div>
                      <div className="w-16 h-1 bg-yellow-400 mx-auto mb-4"></div>
                      <p className="text-slate-500 font-medium">Video Placeholder</p>
                    </div>
                  </div>
                </video>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* 3대 가치 약속 Section (Restored from App.jsx & Upgraded) */}
      <section id="values" className="py-24 bg-white relative">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-extrabold text-[#00513b] break-keep">몬스멕타의 3대 가치 약속</h2>
            <div className="w-24 h-1.5 bg-yellow-400 mx-auto mt-6 rounded-full"></div>
            <p className="text-slate-500 text-lg mt-6 font-medium">수의사 원장님들의 진료 및 경영적 신뢰를 지켜드리는 확실한 기준이 되겠습니다.</p>
          </div>
          
          <div className="grid md:grid-cols-3 gap-8">
            <div className="bg-slate-50 p-10 rounded-3xl border border-slate-100 shadow-lg hover:shadow-2xl hover:-translate-y-2 transition-all duration-300 group">
              <div className="w-16 h-16 bg-[#00513b] text-white rounded-2xl flex items-center justify-center mb-6 text-3xl shadow-md group-hover:scale-110 transition-transform">🔒</div>
              <h4 className="text-xl font-bold text-slate-800 mb-4">온라인 및 펫샵 유통 원천 배제</h4>
              <p className="text-slate-600 leading-relaxed">
                모든 온라인 쇼핑몰, 오픈마켓, 소셜커머스 및 일반 오프라인 펫샵에 절대 유통하지 않을 것임을 약속드립니다. 오직 동물병원을 통해서만 처방 권위를 유지하실 수 있습니다.
              </p>
            </div>
            
            <div className="bg-slate-50 p-10 rounded-3xl border border-slate-100 shadow-lg hover:shadow-2xl hover:-translate-y-2 transition-all duration-300 group">
              <div className="w-16 h-16 bg-gradient-to-br from-yellow-400 to-yellow-500 text-white rounded-2xl flex items-center justify-center mb-6 text-3xl shadow-md group-hover:scale-110 transition-transform">💸</div>
              <h4 className="text-xl font-bold text-slate-800 mb-4">자율 가격 및 마진 구조 보장</h4>
              <p className="text-slate-600 leading-relaxed">
                합리적 공급가를 보장하며, 실제 판매 가격은 원장님들께서 상황에 맞춰 자율 책정하여 운영하실 수 있습니다. 공급가 대비 압도적 마진율로 병원 경영의 활력이 되어드립니다.
              </p>
            </div>
            
            <div className="bg-slate-50 p-10 rounded-3xl border border-slate-100 shadow-lg hover:shadow-2xl hover:-translate-y-2 transition-all duration-300 group">
              <div className="w-16 h-16 bg-slate-800 text-white rounded-2xl flex items-center justify-center mb-6 text-3xl shadow-md group-hover:scale-110 transition-transform">🔬</div>
              <h4 className="text-xl font-bold text-slate-800 mb-4">월등한 학술적 포뮬러</h4>
              <p className="text-slate-600 leading-relaxed">
                초미세공정 몬모릴로나이트와 바실러스 서브틸리스 균주를 고함량 배합하여 장 점막 방어막을 빠르게 복구하고, 수액(IV) 치료와 폭발적인 시너지를 일으킵니다.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Clinical Evidence Section */}
      <section id="clinical" className="py-24 bg-slate-100 border-y border-slate-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-extrabold text-[#00513b] break-keep">수의사가 수의사에게 제안하는 근거</h2>
            <div className="w-24 h-1.5 bg-yellow-400 mx-auto mt-6 rounded-full"></div>
          </div>
          
          <div className="grid lg:grid-cols-2 gap-10">
            <div className="bg-white p-10 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-shadow duration-300">
              <h3 className="text-2xl font-black text-slate-800 mb-4 flex items-start sm:items-center gap-3 break-keep">
                <span className="w-8 h-8 rounded-full shrink-0 bg-[#00513b] text-white flex items-center justify-center text-sm shadow-md">1</span>
                <span>신속한 장 점막 회복 임상</span>
              </h3>
              <p className="text-slate-600 mb-8 leading-relaxed text-lg">
                에스앤제이 동물병원의 실제 처방 케이스를 통해 입증된 유해 물질 차단력과 점막 보호막 형성 속도를 확인하세요.
              </p>
              <div className="h-48 bg-slate-50 border border-slate-200 rounded-2xl flex items-end p-6 gap-6 overflow-hidden relative">
                <div className="absolute top-4 left-6 text-xs font-bold text-slate-400">회복 속도 비교 (일)</div>
                <div className="w-1/2 bg-slate-300 h-[40%] rounded-t-lg relative group transition-all duration-500 hover:bg-slate-400">
                  <span className="absolute -top-8 w-full text-center text-sm font-semibold text-slate-500">대조군</span>
                </div>
                <div className="w-1/2 bg-gradient-to-t from-[#003d2b] to-[#006e50] h-[90%] rounded-t-lg relative group transition-all duration-500 hover:brightness-110 shadow-[0_-5px_15px_rgba(0,81,59,0.3)]">
                  <span className="absolute -top-8 w-full text-center text-sm font-black text-[#00513b]">몬스멕타</span>
                </div>
              </div>
            </div>

            <div className="bg-white p-10 rounded-3xl border border-slate-200 shadow-xl hover:shadow-2xl transition-shadow duration-300 flex flex-col justify-between">
              <div>
                <h3 className="text-2xl font-black text-slate-800 mb-4 flex items-start sm:items-center gap-3 break-keep">
                  <span className="w-8 h-8 rounded-full shrink-0 bg-[#00513b] text-white flex items-center justify-center text-sm shadow-md">2</span>
                  <span>완벽한 기호성과 투약 편의성</span>
                </h3>
                <p className="text-slate-600 mb-8 leading-relaxed text-lg">
                  바쁜 진료 환경과 예민한 환축을 고려하여, 스트레스 없이 자발적인 섭취를 유도하도록 설계되었습니다.
                </p>
              </div>
              <ul className="space-y-4">
                <li className="flex justify-between items-center bg-slate-50 p-5 rounded-xl border border-slate-200 hover:border-emerald-300 transition-colors">
                  <span className="font-bold text-slate-700 text-lg">자발적 섭취율</span>
                  <div className="flex items-center gap-3">
                    <div className="w-32 h-2 bg-slate-200 rounded-full overflow-hidden hidden sm:block"><div className="h-full bg-emerald-500 w-[94%]"></div></div>
                    <span className="text-[#00513b] font-black text-2xl">94%</span>
                  </div>
                </li>
                <li className="flex justify-between items-center bg-slate-50 p-5 rounded-xl border border-slate-200 hover:border-emerald-300 transition-colors">
                  <span className="font-bold text-slate-700 text-lg">원내 처방 만족도</span>
                  <div className="flex items-center gap-3">
                    <div className="flex gap-1 text-yellow-400 text-lg">★★★★★</div>
                    <span className="text-[#00513b] font-black text-2xl">4.8</span>
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* Infographics Section (Restored) */}
      <section className="py-24 bg-white max-w-6xl mx-auto px-4">
        <div className="text-center mb-16">
          <h3 className="text-3xl md:text-4xl font-extrabold text-[#00513b] mb-4 break-keep">상세 학술 데이터</h3>
          <p className="text-slate-500 text-lg font-medium">원장님의 정확한 처방을 돕는 심층 자료입니다.</p>
        </div>
        <div className="space-y-12">
          {/* HTML Infographic */}
          <div 
            className="bg-slate-50 rounded-3xl shadow-xl border border-slate-200 overflow-hidden relative transition-all duration-300 w-full"
            style={{ height: iframeHeight ? `${iframeHeight}px` : '1800px' }}
          >
            <iframe 
              src={`${import.meta.env.BASE_URL}assets/james_infographic.html?v=2.0`} 
              className="absolute top-0 left-0 w-full h-full border-0" 
              title="몬스멕타 인포그래픽" 
              scrolling="no"
            />
          </div>
          {/* Image Infographic */}
          <div className="bg-slate-50 p-4 rounded-3xl shadow-xl border border-slate-200 overflow-hidden hover:shadow-2xl transition-shadow duration-500">
            <img src={`${import.meta.env.BASE_URL}assets/infographic_2.png`} alt="몬스멕타 임상 증례" className="w-full h-auto object-contain rounded-2xl mix-blend-multiply" />
          </div>
        </div>
      </section>

      {/* Letter Message Section (Restored) */}
      <section className="py-20 bg-emerald-900 text-emerald-50 relative overflow-hidden">
        <div className="absolute inset-0 opacity-10 bg-[url('https://www.transparenttextures.com/patterns/stardust.png')]"></div>
        <div className="max-w-4xl mx-auto px-4 text-center relative z-10">
          <blockquote className="relative">
            <span className="text-8xl text-emerald-400/20 absolute -top-8 -left-8 md:-left-12 font-serif">"</span>
            <p className="text-xl md:text-2xl leading-loose italic font-light drop-shadow-md">
              원장님, 몬스멕타는 단순한 일회성 정장 제품 공급을 넘어,<br className="hidden md:block"/>
              일선 원장님들이 임상 진료 현장에서 당당히 처방의 가치와 독점성을 누릴 수 있도록<br className="hidden md:block"/>
              든든하게 지켜드리는 영속적인 비즈니스 파트너가 될 것을 약속드립니다.
            </p>
            <footer className="mt-10">
              <div className="font-bold text-yellow-400 text-xl tracking-wide">수의학적 가치와 신뢰를 담아,</div>
              <div className="font-black text-white text-2xl mt-2">닥터 젬스홍 배상</div>
            </footer>
          </blockquote>
        </div>
      </section>

      {/* B2B Order Form Section */}
      <section id="order" className="py-24 bg-slate-50">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="bg-white rounded-3xl shadow-2xl overflow-hidden border border-slate-200 transform transition-all duration-500 hover:shadow-[0_20px_50px_rgba(0,81,59,0.1)]">
            <div className="bg-gradient-to-r from-[#00513b] to-[#003d2b] p-8 md:p-10 text-center relative overflow-hidden">
              <div className="absolute top-0 right-0 w-32 h-32 bg-white opacity-5 rounded-full blur-2xl transform translate-x-1/2 -translate-y-1/2"></div>
              <h2 className="text-3xl font-black text-white drop-shadow-md break-keep">동물병원 원장님 전용 퀵 발주서</h2>
              <p className="text-emerald-100/80 font-medium mt-3">입력하신 정보는 병원 인증 및 세금계산서 발행에 엄격하게 사용됩니다.</p>
            </div>
            
            <form onSubmit={handleCheckout} className="p-8 md:p-12 space-y-10">
              <div className="space-y-6">
                <h3 className="text-xl font-black text-slate-800 border-b-2 border-emerald-100 pb-3 flex items-center gap-2">
                  <span className="bg-emerald-100 text-[#00513b] w-8 h-8 rounded-full flex items-center justify-center text-sm">1</span> 
                  동물병원 정보
                </h3>
                <div className="grid md:grid-cols-2 gap-6">
                  <div>
                    <label className="block text-sm font-bold text-slate-700 mb-2">동물병원명 <span className="text-red-500">*</span></label>
                    <input 
                      type="text" 
                      value={hospitalName}
                      onChange={(e) => setHospitalName(e.target.value)}
                      className="w-full px-5 py-4 rounded-xl border border-slate-300 focus:ring-4 focus:ring-emerald-500/20 focus:border-[#00513b] outline-none bg-slate-50 transition-all font-medium" 
                      placeholder="예: 에스앤제이 동물병원" 
                      required 
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-bold text-slate-700 mb-2">사업자등록번호 <span className="text-red-500">*</span></label>
                    <input 
                      type="text" 
                      value={bizNumber}
                      onChange={(e) => setBizNumber(e.target.value)}
                      className="w-full px-5 py-4 rounded-xl border border-slate-300 focus:ring-4 focus:ring-emerald-500/20 focus:border-[#00513b] outline-none bg-slate-50 transition-all font-medium tracking-wide" 
                      placeholder="숫자만 10자리 입력" 
                      required 
                      maxLength="12"
                    />
                  </div>
                </div>
                <div>
                  <label className="block text-sm font-bold text-slate-700 mb-2">제품 수령지 주소 <span className="text-red-500">*</span></label>
                  <input 
                    type="text" 
                    value={address}
                    onChange={(e) => setAddress(e.target.value)}
                    className="w-full px-5 py-4 rounded-xl border border-slate-300 focus:ring-4 focus:ring-emerald-500/20 focus:border-[#00513b] outline-none bg-slate-50 transition-all font-medium" 
                    placeholder="상세 주소를 정확히 입력해주세요" 
                    required 
                  />
                </div>
              </div>

              <div className="space-y-6">
                <h3 className="text-xl font-black text-slate-800 border-b-2 border-emerald-100 pb-3 flex items-center gap-2">
                  <span className="bg-emerald-100 text-[#00513b] w-8 h-8 rounded-full flex items-center justify-center text-sm">2</span> 
                  수량 선택 (병)
                </h3>
                <div className="flex flex-col md:flex-row items-center justify-between bg-slate-50 p-8 rounded-2xl border border-slate-200 hover:border-emerald-200 transition-colors shadow-inner">
                  <div className="mb-6 md:mb-0 text-center md:text-left">
                    <div className="font-black text-2xl text-slate-800 tracking-tight">몬스멕타 <span className="text-lg font-bold text-slate-500">(100ml / 병)</span></div>
                    <div className="text-sm font-medium text-slate-500 mt-2">병원 공급가: <span className="font-black text-xl text-[#00513b] ml-1">{pricePerBottle.toLocaleString()}원</span> <span className="text-xs">(VAT 포함)</span></div>
                    <p className="text-xs text-[#00513b] mt-1 font-semibold">* 최소 주문 수량: 5병</p>
                  </div>
                  
                  <div className="flex items-center bg-white border-2 border-slate-200 rounded-xl overflow-hidden shadow-sm">
                    <button type="button" onClick={() => setQuantity(Math.max(5, quantity - 1))} className="w-14 h-14 flex items-center justify-center bg-slate-50 text-slate-600 hover:bg-emerald-50 hover:text-[#00513b] text-2xl font-black transition-colors">-</button>
                    <div className="w-20 h-14 flex items-center justify-center font-black text-2xl text-slate-800 border-x-2 border-slate-200">{quantity}</div>
                    <button type="button" onClick={() => setQuantity(quantity + 1)} className="w-14 h-14 flex items-center justify-center bg-slate-50 text-slate-600 hover:bg-emerald-50 hover:text-[#00513b] text-2xl font-black transition-colors">+</button>
                  </div>
                </div>
              </div>

              <div className="bg-slate-900 p-8 md:p-10 rounded-2xl text-white shadow-2xl relative overflow-hidden">
                <div className="absolute -right-10 -top-10 w-40 h-40 bg-yellow-400 opacity-10 rounded-full blur-3xl"></div>
                <div className="flex flex-col md:flex-row justify-between items-center mb-8 gap-4 relative z-10">
                  <span className="text-xl font-bold text-slate-300">총 결제 예정 금액</span>
                  <span className="text-5xl font-black text-yellow-400 drop-shadow-lg tracking-tight">{(quantity * pricePerBottle).toLocaleString()}<span className="text-2xl ml-2 text-yellow-500">원</span></span>
                </div>
                <button type="submit" className="w-full bg-gradient-to-r from-yellow-400 to-yellow-500 text-slate-900 text-2xl font-black py-5 rounded-xl hover:from-yellow-300 hover:to-yellow-400 transition duration-300 shadow-[0_0_20px_rgba(250,204,21,0.3)] transform hover:-translate-y-1 flex justify-center items-center gap-3">
                  <span>선결제 진행하기</span>
                  <svg className="w-7 h-7 animate-bounce-x" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="3" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                </button>
                <p className="text-center text-slate-400 text-sm mt-6 font-medium">무통장 입금: 카카오뱅크 3333-26-3248376 (예금주: 홍순일)</p>
              </div>
            </form>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-slate-950 text-slate-400 py-16 border-t border-slate-900">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h4 className="text-white font-black text-xl mb-6 tracking-wide">에스앤제이 동물병원</h4>
          <div className="space-y-3 mb-8 font-medium">
            <p>대표자: 홍순일 (닥터 젬스홍) | 사업자등록번호: 792-66-00615</p>
            <p>주소: 경기도 용인시 처인구 포곡읍 선장1로 98-8</p>
            <p>대표 연락처: 031-321-6562 | 이메일: contact@snjvet.com</p>
            <p className="text-slate-500 mt-4">결제계좌: 카카오뱅크 3333-26-3248376 (예금주: 홍순일)</p>
          </div>
          <div className="pt-8 border-t border-slate-800/50 text-sm font-semibold tracking-wider text-slate-600">
            © {new Date().getFullYear()} S&J Animal Hospital. All rights reserved.
            <br />
            <span className="text-xs font-normal mt-2 inline-block">※ 본 사이트는 대외비 문서로 전국 수의사 원장님들께 한정하여 발송됩니다.</span>
          </div>
        </div>
      </footer>

      {/* Global Style for custom animations */}
      <style dangerouslySetInnerHTML={{__html: `
        @keyframes bounce-x {
          0%, 100% { transform: translateX(0); }
          50% { transform: translateX(25%); }
        }
        .animate-bounce-x {
          animation: bounce-x 1s infinite;
        }
      `}} />
    </div>
  );
};

export default MonsmectaSNJLanding;
