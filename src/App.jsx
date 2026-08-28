import { useState, useRef, lazy, Suspense } from 'react';
import { useTranslation } from 'react-i18next';
import { PRODUCTS } from './data/products';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import Lineup from './components/Lineup';
import Values from './components/Values';
import ClinicalEvidence from './components/ClinicalEvidence';
import ClinicalCaseStudy from './components/ClinicalCaseStudy';
import Infographics from './components/Infographics';
import Letter from './components/Letter';
import AudioTestimonial from './components/AudioTestimonial';
import OrderForm from './components/OrderForm';
import Footer from './components/Footer';
import StickyBottomCTA from './components/StickyBottomCTA';
import useIframeHeight from './hooks/useIframeHeight';
import A11yToolbar from './components/A11yToolbar';

// 상호작용 이후에만 필요한 컴포넌트는 지연 로딩하여 초기 번들을 줄인다.
const Chatbot = lazy(() => import('./components/Chatbot'));
const LabelModal = lazy(() => import('./components/LabelModal'));
const PrintModal = lazy(() => import('./components/PrintModal'));
const VetSampleModal = lazy(() => import('./components/VetSampleModal'));
const LegalModal = lazy(() => import('./components/LegalModal'));
const NoticeGeneratorModal = lazy(() => import('./components/NoticeGeneratorModal'));

const ALLOWED_IFRAME_SOURCES = new Set(['james', 'dashboard', 'scenario']);

const ORDER_DONE_KEY = 'monsmecta_order_done_v1';
const ORDER_LAST_KEY = 'monsmecta_order_last_v1';
const ORDER_AUTOFILL_KEY = 'monsmecta_order_autofill_v1';
const ORDER_DONE_TTL = 30 * 24 * 60 * 60 * 1000;
const ORDER_LAST_TTL = 5 * 60 * 1000;
const ORDER_FETCH_TIMEOUT = 60000;
const ORDER_MIN_QUANTITY = 5;

const genId = () =>
  (typeof crypto !== 'undefined' && crypto.randomUUID)
    ? crypto.randomUUID()
    : 'id-' + Date.now().toString(36) + '-' + Math.random().toString(36).slice(2);

const isValidBizNumber = (num) => {
  const v = num.replace(/[^0-9]/g, '');
  if (!/^\d{10}$/.test(v)) return false;
  const weights = [1, 3, 7, 1, 3, 7, 1, 3, 5];
  let sum = 0;
  for (let i = 0; i < 9; i++) sum += Number(v[i]) * weights[i];
  sum += Math.floor((Number(v[8]) * 5) / 10);
  const check = (10 - (sum % 10)) % 10;
  return check === Number(v[9]);
};

const MonsmectaSNJLanding = () => {
  const iframeHeights = useIframeHeight(ALLOWED_IFRAME_SOURCES);
  const { t } = useTranslation();
  const [isSampleModalOpen, setIsSampleModalOpen] = useState(false);
  const [isNoticeModalOpen, setIsNoticeModalOpen] = useState(false);
  const [legalType, setLegalType] = useState(null);
  const [activeProduct, setActiveProduct] = useState('monsmecta');
  const [quantities, setQuantities] = useState(
    Object.keys(PRODUCTS).reduce((acc, key) => ({ ...acc, [key]: 0 }), {})
  );

  const [hospitalName, setHospitalName] = useState('');
  const [vetName, setVetName] = useState('');
  const [bizNumber, setBizNumber] = useState('');
  const [bizCategory, setBizCategory] = useState('');
  const [bizType, setBizType] = useState('');
  const [email, setEmail] = useState('');
  const [address, setAddress] = useState('');
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [isLabelModalOpen, setIsLabelModalOpen] = useState(false);
  const [isPrintModalOpen, setIsPrintModalOpen] = useState(false);
  const [printUrl, setPrintUrl] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isOrderComplete, setIsOrderComplete] = useState(() => {
    try {
      const done = JSON.parse(localStorage.getItem(ORDER_DONE_KEY));
      return !!(done && done.ts && Date.now() - done.ts < ORDER_DONE_TTL);
    } catch { /* ignore */ }
    return false;
  });
  const [orderError, setOrderError] = useState('');
  const [honeypot, setHoneypot] = useState('');
  const lastSubmitRef = useRef(0);
  const submittingRef = useRef(false);
  const orderRequestIdRef = useRef(null);

  const handleHospitalNameChange = (name) => {
    setHospitalName(name);
    if (name && name.length > 1) {
      try {
        const saved = JSON.parse(localStorage.getItem(ORDER_AUTOFILL_KEY));
        if (saved && saved.hospitalName === name) {
          if (!vetName && saved.vetName) setVetName(saved.vetName);
          if (!bizNumber && saved.bizNumber) setBizNumber(saved.bizNumber);
          if (!bizCategory && saved.bizCategory) setBizCategory(saved.bizCategory);
          if (!bizType && saved.bizType) setBizType(saved.bizType);
          if (!email && saved.email) setEmail(saved.email);
          if (!address && saved.address) setAddress(saved.address);
        }
      } catch { /* ignore */ }
    }
  };

  const handleCheckout = async (e) => {
    e.preventDefault();
    setOrderError('');
    if (submittingRef.current || isSubmitting) return;

    if (honeypot) {
      setIsOrderComplete(true);
      return;
    }

    if (Date.now() - lastSubmitRef.current < 5000) {
      return;
    }
    lastSubmitRef.current = Date.now();

    if (!hospitalName || !vetName || !bizNumber || !bizCategory || !bizType || !email || !address) {
      alert(t('order.validationRequired'));
      return;
    }

    const totalQuantity = Object.values(quantities).reduce((sum, q) => sum + q, 0);
    if (totalQuantity === 0) {
      alert(t('order.validationQuantity', '발주할 제품의 수량을 1개 이상 선택해주세요.'));
      return;
    }
    if (totalQuantity < ORDER_MIN_QUANTITY) {
      alert(t('order.validationMinQuantity', { min: ORDER_MIN_QUANTITY, defaultValue: `최소 주문 수량은 ${ORDER_MIN_QUANTITY}병입니다.` }));
      return;
    }

    if (!isValidBizNumber(bizNumber)) {
      alert(t('order.validationBizNumber'));
      return;
    }

    const normBiz = bizNumber.replace(/[^0-9]/g, '');
    let last = null;
    try {
      last = JSON.parse(localStorage.getItem(ORDER_LAST_KEY));
    } catch { /* ignore */ }
    if (last && last.biz && last.biz === normBiz && Date.now() - last.ts < ORDER_LAST_TTL) {
      alert(t('order.recentSubmit'));
      return;
    }

    submittingRef.current = true;
    setIsSubmitting(true);
    if (!orderRequestIdRef.current) orderRequestIdRef.current = genId();

    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), ORDER_FETCH_TIMEOUT);

    try {
      const scriptURL = import.meta.env.VITE_GOOGLE_APPS_SCRIPT_URL;
      if (!scriptURL) {
        throw new Error('Google Apps Script URL is not configured');
      }
      const formData = new URLSearchParams();
      formData.append('type', 'order');
      formData.append('requestId', orderRequestIdRef.current);
      formData.append('동물병원명', hospitalName);
      formData.append('원장님 성함', vetName);
      formData.append('사업자등록번호', normBiz);
      formData.append('업태', bizCategory);
      formData.append('종목', bizType);
      formData.append('이메일', email);
      formData.append('배송지 주소', address);
      let totalPrice = 0;
      Object.entries(quantities).forEach(([key, q]) => {
        if (q > 0) {
          formData.append(`${PRODUCTS[key]?.name_ko || key} 수량(병)`, q);
          totalPrice += q * (PRODUCTS[key]?.price || 0);
        }
      });
      formData.append('총 결제금액', totalPrice);
      formData.append('접수일시', new Date().toLocaleString('ko-KR'));

      const response = await fetch(scriptURL, {
        method: 'POST',
        body: formData,
        signal: controller.signal
      });

      let json = null;
      try {
        json = await response.json();
      } catch { /* ignore */ }

      if (!response.ok) {
        alert(t('order.errorServer'));
        return;
      }
      if (json && json.status === 'duplicate') {
        alert(t('order.duplicateError'));
        return;
      }
      if (json && json.status === 'error') {
        alert(t('order.errorServer'));
        return;
      }

      try {
        localStorage.setItem(ORDER_DONE_KEY, JSON.stringify({ biz: normBiz, ts: Date.now() }));
        localStorage.setItem(ORDER_LAST_KEY, JSON.stringify({ biz: normBiz, ts: Date.now() }));
        localStorage.setItem(ORDER_AUTOFILL_KEY, JSON.stringify({
          hospitalName, vetName, bizNumber, bizCategory, bizType, email, address
        }));
      } catch { /* ignore */ }
      setIsOrderComplete(true);
    } catch (error) {
      console.error('Error!', error.message);
      if (error.name === 'AbortError') {
        setOrderError(t('order.timeoutError'));
      } else {
        setOrderError(t('order.errorNetwork'));
      }
    } finally {
      clearTimeout(timer);
      submittingRef.current = false;
      setIsSubmitting(false);
    }
  };

  const handleResetOrder = () => {
    try {
      localStorage.removeItem(ORDER_DONE_KEY);
    } catch { /* ignore */ }
    setIsOrderComplete(false);
  };

  const openPrintModal = (product) => {
    setPrintUrl(`${import.meta.env.BASE_URL}assets/labels/${product}_label_print.html?v=${Date.now()}`);
    setIsPrintModalOpen(true);
  };

  return (
    <div className="min-h-screen bg-slate-50 font-sans text-slate-800 scroll-smooth overflow-x-hidden">
      <a href="#main-content" className="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 focus:z-[100] focus:bg-[#00513b] focus:text-white focus:px-4 focus:py-2 focus:rounded-md focus:shadow-lg focus:outline-none">
        {t('nav.skipToContent')}
      </a>

      <Navbar isMobileMenuOpen={isMobileMenuOpen} setIsMobileMenuOpen={setIsMobileMenuOpen} onOpenNoticeModal={() => setIsNoticeModalOpen(true)} activeProduct={activeProduct} setActiveProduct={setActiveProduct} />
      <main id="main-content">
        <Hero setIsLabelModalOpen={setIsLabelModalOpen} activeProduct={activeProduct} setActiveProduct={setActiveProduct} />
        <Lineup setIsLabelModalOpen={setIsLabelModalOpen} activeProduct={activeProduct} setActiveProduct={setActiveProduct} />
        <Values activeProduct={activeProduct} />
        <ClinicalEvidence activeProduct={activeProduct} />
        <ClinicalCaseStudy />
        <Infographics iframeHeights={iframeHeights} />
        <Letter />
        <AudioTestimonial />
        <OrderForm
          isOrderComplete={isOrderComplete}
          setIsOrderComplete={setIsOrderComplete}
          quantities={quantities}
          setQuantities={setQuantities}
          minQuantity={ORDER_MIN_QUANTITY}
          hospitalName={hospitalName}
          onHospitalNameChange={handleHospitalNameChange}
          vetName={vetName}
          setVetName={setVetName}
          bizNumber={bizNumber}
          setBizNumber={setBizNumber}
          bizCategory={bizCategory}
          setBizCategory={setBizCategory}
          bizType={bizType}
          setBizType={setBizType}
          email={email}
          setEmail={setEmail}
          address={address}
          setAddress={setAddress}
          isSubmitting={isSubmitting}
          orderError={orderError}
          honeypot={honeypot}
          setHoneypot={setHoneypot}
          onResetOrder={handleResetOrder}
          handleCheckout={handleCheckout}
        />
        <Footer setLegalType={setLegalType} />
      </main>

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

      {/* 모달은 열릴 때만 마운트하여 해당 청크를 지연 로딩한다. */}
      <Suspense fallback={null}>
        {isLabelModalOpen && (
          <LabelModal isLabelModalOpen={isLabelModalOpen} setIsLabelModalOpen={setIsLabelModalOpen} onOpenPrint={() => openPrintModal(activeProduct)} activeProduct={activeProduct} />
        )}
        {isPrintModalOpen && (
          <PrintModal isPrintModalOpen={isPrintModalOpen} setIsPrintModalOpen={setIsPrintModalOpen} printUrl={printUrl} />
        )}
        {isSampleModalOpen && (
          <VetSampleModal isOpen={isSampleModalOpen} onClose={() => setIsSampleModalOpen(false)} />
        )}
        {legalType && (
          <LegalModal legalType={legalType} setLegalType={setLegalType} />
        )}
        {isNoticeModalOpen && (
          <NoticeGeneratorModal isOpen={isNoticeModalOpen} onClose={() => setIsNoticeModalOpen(false)} />
        )}
      </Suspense>
      <StickyBottomCTA onOpenModal={() => setIsSampleModalOpen(true)} onOpenNoticeModal={() => setIsNoticeModalOpen(true)} />
      <A11yToolbar />
      <Suspense fallback={null}>
        <Chatbot />
      </Suspense>
    </div>
  );
};


export default MonsmectaSNJLanding;
