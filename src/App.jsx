import React, { useState } from 'react';

const MonsmectaLandingPage = () => {
  const [quantity, setQuantity] = useState(5);
  const pricePerBottle = 7700; // 병당 가격 (부가세 포함)

  const handleOrder = (e) => {
    e.preventDefault();
    alert(`총 ${quantity}병, ${(quantity * pricePerBottle).toLocaleString()}원 선결제 모듈로 이동합니다.`);
  };

  return (
    <div className="min-h-screen bg-gray-50 font-sans text-gray-800">
      {/* Header */}
      <header className="bg-white/80 backdrop-blur-md shadow-sm sticky top-0 z-50 transition-all duration-300">
        <div className="max-w-6xl mx-auto px-4 py-4 flex justify-between items-center">
          <div className="flex items-center gap-3">
            <img src={`${import.meta.env.BASE_URL}assets/sj_logo.png`} alt="에스앤제이 동물병원 로고" className="h-11 w-auto" />
            <h1 className="text-2xl font-extrabold text-brand-green tracking-tight">
              에스앤제이 동물병원 원장 제임스홍
            </h1>
          </div>
          <nav className="hidden md:flex space-x-8 text-sm font-semibold text-gray-600">
            <a href="#about" className="hover:text-brand-green transition-colors">제품소개</a>
            <a href="#values" className="hover:text-brand-green transition-colors">3대 가치</a>
            <a href="#infographic" className="hover:text-brand-green transition-colors">학술 데이터</a>
            <a href="#order" className="hover:text-brand-green transition-colors">주문/발주</a>
          </nav>
        </div>
      </header>

      {/* Hero Section */}
      <section className="relative bg-gradient-to-br from-brand-green to-brand-dark text-white py-24 md:py-32 overflow-hidden">
        <div className="absolute inset-0 opacity-20 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-white via-transparent to-transparent"></div>
        <div className="max-w-6xl mx-auto px-4 relative z-10 grid md:grid-cols-2 gap-12 items-center">
          <div className="text-center md:text-left">
            <span className="inline-block py-1 px-4 rounded-full bg-yellow-500/20 border border-yellow-400/50 text-yellow-300 text-sm font-bold tracking-wider mb-6 backdrop-blur-md shadow-lg">
              전국 수의사 원장님 전용 대외비 문서
            </span>
            <h2 className="text-4xl md:text-5xl lg:text-6xl font-extrabold mb-6 leading-tight tracking-tight drop-shadow-lg break-keep">
              원장님께 드리는<br />
              처방 독점권 제안 및 <br className="hidden md:block" />
              <span className="text-yellow-400 inline-block">몬스멕타(MONSMECTA)</span> <span className="inline-block">출시</span>
            </h2>
            <p className="text-lg md:text-xl text-gray-200 mb-10 font-light max-w-lg mx-auto md:mx-0">
              에스앤제이 동물병원 원장 제임스홍(홍순일) 수의사가 6,000마리의 치명적인 파보 장염 환축들을 직접 보살피며 검증한 가장 확실한 선택입니다.
            </p>
            <a href="#order" className="inline-block bg-yellow-500 text-brand-dark font-black py-4 px-10 rounded-full text-lg hover:bg-yellow-400 hover:scale-105 transition-all duration-300 shadow-[0_0_20px_rgba(234,179,8,0.4)] ring-2 ring-yellow-300 ring-offset-2 ring-offset-brand-green">
              지금 독점 처방권 선점하기
            </a>
          </div>
          <div className="relative group perspective rounded-3xl overflow-hidden shadow-2xl border-4 border-white/10">
            {/* 동영상 영역 */}
            <video 
              autoPlay 
              loop 
              muted 
              playsInline 
              className="w-full h-auto object-cover transform group-hover:scale-105 transition-transform duration-700"
            >
              <source src={`${import.meta.env.BASE_URL}assets/video.mp4`} type="video/mp4" />
              브라우저가 동영상을 지원하지 않습니다.
            </video>
          </div>
        </div>
      </section>

      {/* 3대 가치 약속 Section */}
      <section id="values" className="py-24 bg-white relative">
        <div className="max-w-6xl mx-auto px-4">
          <div className="text-center mb-16">
            <h3 className="text-4xl font-extrabold text-brand-green mb-4">몬스멕타의 3대 가치 약속 및 임상적 우위</h3>
            <p className="text-gray-600 text-lg">수의사 원장님들의 진료 및 경영적 신뢰를 지켜드리는 확실한 기준이 되겠습니다.</p>
          </div>
          
          <div className="grid md:grid-cols-3 gap-8">
            <div className="bg-gray-50 p-8 rounded-2xl border border-gray-100 shadow-lg hover:shadow-xl hover:-translate-y-1 transition-all">
              <div className="w-14 h-14 bg-brand-green text-white rounded-xl flex items-center justify-center mb-6 text-2xl shadow-md">🔒</div>
              <h4 className="text-xl font-bold text-gray-900 mb-4">온라인 및 펫샵 유통 원천 배제</h4>
              <p className="text-gray-600 leading-relaxed">
                모든 온라인 쇼핑몰, 오픈마켓, 소셜커머스 및 일반 오프라인 펫샵에 절대 유통하지 않을 것임을 약속드립니다. 오직 동물병원을 통해서만 처방 권위를 유지하실 수 있습니다.
              </p>
            </div>
            
            <div className="bg-gray-50 p-8 rounded-2xl border border-gray-100 shadow-lg hover:shadow-xl hover:-translate-y-1 transition-all">
              <div className="w-14 h-14 bg-yellow-500 text-white rounded-xl flex items-center justify-center mb-6 text-2xl shadow-md">💸</div>
              <h4 className="text-xl font-bold text-gray-900 mb-4">최고 수준의 자율 가격 및 마진 구조</h4>
              <p className="text-gray-600 leading-relaxed">
                합리적 공급가를 보장하며, 실제 판매 가격은 원장님들께서 상황에 맞춰 자율 책정하여 운영하실 수 있습니다. 공급가 대비 압도적 마진율로 병원 경영의 활력이 되어드립니다.
              </p>
            </div>
            
            <div className="bg-gray-50 p-8 rounded-2xl border border-gray-100 shadow-lg hover:shadow-xl hover:-translate-y-1 transition-all">
              <div className="w-14 h-14 bg-brand-dark text-white rounded-xl flex items-center justify-center mb-6 text-2xl shadow-md">🔬</div>
              <h4 className="text-xl font-bold text-gray-900 mb-4">월등한 학술적 포뮬러</h4>
              <p className="text-gray-600 leading-relaxed">
                일반 스멕타이트 대비 초미세공정 몬모릴로나이트와 바실러스 서브틸리스 균주를 고함량 배합하여 장 점막 방어막을 빠르게 복구하고, 수액(IV) 치료와 폭발적인 시너지를 일으킵니다.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Product Info Section (Infographics) */}
      <section id="infographic" className="py-24 bg-brand-green/5 max-w-6xl mx-auto px-4 rounded-3xl my-12">
        <div className="text-center mb-16">
          <h3 className="text-4xl font-extrabold text-brand-green mb-4">학술적 우위와 임상 데이터</h3>
          <p className="text-gray-600 text-lg">몬스멕타(MONSMECTA) 프로젝트의 핵심 노하우를 바탕으로 개발된 혁신적인 처방 보조제입니다.</p>
        </div>
        
        <div className="space-y-12">
          {/* HTML Infographic */}
          <div className="bg-white rounded-3xl shadow-xl border border-gray-100 overflow-hidden relative" style={{ height: '1700px' }}>
            <iframe 
              src={`${import.meta.env.BASE_URL}assets/james_infographic.html`} 
              className="absolute top-0 left-0 w-full h-full border-0" 
              title="몬스멕타 인포그래픽" 
              scrolling="no"
            />
          </div>
          
          {/* Infographic 2 (Restored) */}
          <div className="bg-white p-4 rounded-3xl shadow-xl border border-gray-100 overflow-hidden">
            <img src={`${import.meta.env.BASE_URL}assets/infographic_2.png`} alt="몬스멕타 인포그래픽 2" className="w-full h-auto object-contain rounded-2xl" />
          </div>
        </div>
      </section>

      {/* Letter Message Section */}
      <section className="py-16 max-w-4xl mx-auto px-4 text-center">
        <blockquote className="relative p-8 bg-white rounded-3xl shadow-lg border border-gray-100">
          <span className="text-6xl text-brand-green/20 absolute top-4 left-6">"</span>
          <p className="text-xl text-gray-700 leading-relaxed italic relative z-10 font-medium">
            원장님, 몬스멕타는 단순한 일회성 정장 제품 공급을 넘어,<br/>
            일선 원장님들이 임상 진료 현장에서 당당히 처방의 가치와 독점성을 누릴 수 있도록<br/>
            든든하게 지켜드리는 영속적인 비즈니스 파트너가 될 것을 약속드립니다.
          </p>
          <footer className="font-extrabold text-brand-green mt-8 text-xl">
            수의학적 가치와 신뢰를 담아,<br/>닥터 젬스홍 배상
          </footer>
        </blockquote>
      </section>

      {/* Order & Payment Section */}
      <section id="order" className="py-24 max-w-4xl mx-auto px-4">
        <div className="bg-white rounded-3xl shadow-2xl overflow-hidden border border-gray-100">
          <div className="bg-brand-green p-8 text-center">
            <h3 className="text-3xl font-extrabold text-white">동물병원 처방 전용 간편 발주서</h3>
            <p className="text-brand-green-100 mt-2 text-gray-200">초도 처방 물량 공급 신청 및 차별화된 독점 정장 처방권을 먼저 선점해 보시기 바랍니다.</p>
          </div>
          
          <div className="p-8 md:p-12">
            <form onSubmit={handleOrder} className="space-y-8">
              <div className="grid md:grid-cols-2 gap-6">
                <div>
                  <label className="block text-sm font-bold text-gray-700 mb-2">동물병원명</label>
                  <input type="text" required className="w-full bg-gray-50 border border-gray-200 rounded-xl p-4 focus:ring-2 focus:ring-brand-green focus:border-brand-green transition-colors" placeholder="예: 에스앤제이 동물병원" />
                </div>
                <div>
                  <label className="block text-sm font-bold text-gray-700 mb-2">사업자등록번호</label>
                  <input type="text" required className="w-full bg-gray-50 border border-gray-200 rounded-xl p-4 focus:ring-2 focus:ring-brand-green focus:border-brand-green transition-colors" placeholder="- 없이 숫자만 입력" />
                </div>
              </div>
              
              <div>
                <label className="block text-sm font-bold text-gray-700 mb-2">배송지 주소</label>
                <input type="text" required className="w-full bg-gray-50 border border-gray-200 rounded-xl p-4 focus:ring-2 focus:ring-brand-green focus:border-brand-green transition-colors" placeholder="상세 주소를 입력해주세요" />
              </div>

              <div className="bg-gray-50 p-6 rounded-2xl border border-gray-200">
                <div className="flex flex-col md:flex-row items-center justify-between gap-4">
                  <div>
                    <h4 className="text-lg font-extrabold text-brand-green">몬스멕타(MONSMECTA) <span className="text-sm font-normal text-gray-500">(100ml / 병)</span></h4>
                    <p className="text-sm text-gray-600 mt-1">동물병원 공급가: <span className="font-bold">{pricePerBottle.toLocaleString()}원</span> (부가세 포함)</p>
                    <p className="text-xs text-brand-green mt-1 font-semibold">* 최소 주문 수량: 5병</p>
                  </div>
                  
                  <div className="flex items-center bg-white border border-gray-200 rounded-full p-1 shadow-sm">
                    <button type="button" onClick={() => setQuantity(Math.max(5, quantity - 1))} className="w-10 h-10 flex items-center justify-center text-gray-600 hover:text-brand-green hover:bg-brand-green/10 rounded-full transition-colors font-bold text-xl">-</button>
                    <span className="font-bold text-lg w-12 text-center text-gray-900">{quantity}</span>
                    <button type="button" onClick={() => setQuantity(quantity + 1)} className="w-10 h-10 flex items-center justify-center text-brand-green hover:bg-brand-green/10 rounded-full transition-colors font-bold text-xl">+</button>
                  </div>
                </div>
              </div>

              <div className="flex flex-col md:flex-row justify-between items-center bg-brand-green/5 p-6 rounded-2xl border border-brand-green/20">
                <span className="text-lg font-bold text-gray-700 mb-2 md:mb-0">총 결제 예정 금액</span>
                <span className="text-4xl font-extrabold text-brand-green">{(quantity * pricePerBottle).toLocaleString()}<span className="text-2xl font-bold ml-1">원</span></span>
              </div>

              <div className="bg-gray-50 p-4 rounded-xl border border-gray-200 text-center">
                <p className="text-gray-700 font-bold">무통장 입금 계좌: <span className="text-brand-green">카카오뱅크 3333-26-3248376</span> <span className="text-gray-500 text-sm">(예금주: 홍순일)</span></p>
              </div>

              <button type="submit" className="w-full bg-brand-green text-white font-extrabold py-5 rounded-2xl text-xl hover:bg-brand-dark transition-all duration-300 shadow-xl hover:shadow-2xl hover:-translate-y-1">
                안전하게 선결제 진행하기
              </button>
            </form>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-gray-400 py-12 text-center text-sm">
        <div className="max-w-6xl mx-auto px-4">
          <h2 className="text-2xl font-bold text-gray-500 mb-6">판매원: 에스앤제이 동물병원</h2>
          <div className="space-y-2 mb-8">
            <p>대표자: 홍순일 (닥터 젬스홍)</p>
            <p>주소: 경기도 용인시 처인구 포곡읍 선장1로 98-8</p>
            <p>사업자등록번호: 792-66-00615</p>
            <p>대표 연락처: 031-321-6562</p>
            <p>결제계좌: 카카오뱅크 3333-26-3248376 (예금주: 홍순일)</p>
          </div>
          <p className="text-gray-600">&copy; {new Date().getFullYear()} 에스앤제이 동물병원. All rights reserved.</p>
          <p className="text-xs text-gray-700 mt-4">※ 본 사이트는 대외비 문서로 전국 수의사 원장님들께 한정하여 발송됩니다.</p>
        </div>
      </footer>
    </div>
  );
};

export default MonsmectaLandingPage;
