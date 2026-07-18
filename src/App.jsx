import React, { useState } from 'react';
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
import useIframeHeight from './hooks/useIframeHeight';

const ALLOWED_IFRAME_SOURCES = new Set(['james', 'dashboard', 'scenario']);

const MonsmectaSNJLanding = () => {
  const iframeHeights = useIframeHeight(ALLOWED_IFRAME_SOURCES);
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
  const [orderError, setOrderError] = useState('');
  const pricePerBottle = 7700;

  const handleCheckout = async (e) => {
    e.preventDefault();
    setOrderError('');

    if (!hospitalName || !bizNumber || !address) {
      alert('모든 필수 정보를 입력해주세요.');
      return;
    }

    const sanitizedBizNum = bizNumber.replace(/[^0-9]/g, '');
    if (sanitizedBizNum.length < 10) {
      alert('올바른 사업자등록번호(10자리)를 입력해주세요.');
      return;
    }

    setIsSubmitting(true);

    try {
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
      setOrderError('주문이 정상 접수되지 않았습니다. 네트워크 상태를 확인한 뒤 다시 시도해 주세요.');
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-50 font-sans text-slate-800 scroll-smooth">
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
        orderError={orderError}
        handleCheckout={handleCheckout}
      />
      <Footer />

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
