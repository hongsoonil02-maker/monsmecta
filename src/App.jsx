import React, { useState, useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import Chatbot from './components/Chatbot';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import Values from './components/Values';
import ClinicalEvidence from './components/ClinicalEvidence';
import Infographics from './components/Infographics';
import Letter from './components/Letter';
import OrderForm from './components/OrderForm';
import Footer from './components/Footer';
import LabelModal from './components/LabelModal';
import PrintModal from './components/PrintModal';

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

  const { t } = useTranslation();
  const [quantity, setQuantity] = useState(5);
  const [hospitalName, setHospitalName] = useState('');
  const [bizNumber, setBizNumber] = useState('');
  const [address, setAddress] = useState('');
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
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
      const scriptURL = import.meta.env.VITE_GOOGLE_APPS_SCRIPT_URL;
      if (!scriptURL) {
        throw new Error('Google Apps Script URL is not configured');
      }
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
      alert('현재 구글 시트가 연결되지 않아 주문 완료 화면으로 모의 전환합니다.');
      setIsOrderComplete(true);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-50 font-sans text-slate-800 scroll-smooth">
      {/* Accessibility Skip Link */}
      <a href="#main-content" className="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 focus:z-[100] focus:bg-[#00513b] focus:text-white focus:px-4 focus:py-2 focus:rounded-md focus:shadow-lg focus:outline-none">
        본문 바로가기
      </a>

      <Navbar isMobileMenuOpen={isMobileMenuOpen} setIsMobileMenuOpen={setIsMobileMenuOpen} />
      <Hero setIsLabelModalOpen={setIsLabelModalOpen} />
      <Values />
      <ClinicalEvidence />
      <Infographics iframeHeights={iframeHeights} />
      <Letter />
      <OrderForm
        isOrderComplete={isOrderComplete}
        setIsOrderComplete={setIsOrderComplete}
        quantity={quantity}
        setQuantity={setQuantity}
        hospitalName={hospitalName}
        setHospitalName={setHospitalName}
        bizNumber={bizNumber}
        setBizNumber={setBizNumber}
        address={address}
        setAddress={setAddress}
        isSubmitting={isSubmitting}
        handleCheckout={handleCheckout}
      />
      <Footer />

      {/* Global Style for custom animations */}
      <style dangerouslySetInnerHTML={{
        __html: `
        @keyframes bounce-x {
          0%, 100% { transform: translateX(0); }
          50% { transform: translateX(25%); }
        }
        .animate-bounce-x {
          animation: bounce-x 1s infinite;
        }
      `}} />

      <LabelModal isLabelModalOpen={isLabelModalOpen} setIsLabelModalOpen={setIsLabelModalOpen} setIsPrintModalOpen={setIsPrintModalOpen} />
      <PrintModal isPrintModalOpen={isPrintModalOpen} setIsPrintModalOpen={setIsPrintModalOpen} />
      <Chatbot />
    </div>
  );
};

export default MonsmectaSNJLanding;
