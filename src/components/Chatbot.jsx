import { useState, useRef, useEffect } from 'react';
import { createPortal } from 'react-dom';
import { useTranslation } from 'react-i18next';

export default function Chatbot() {
  const { t, i18n } = useTranslation();
  const CHAT_TIMEOUT = 30000;
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isOpen]);

  const toggleChat = () => setIsOpen(!isOpen);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim() || isLoading) return;

    const userMessage = input.trim();
    setInput('');
    setMessages(prev => [...prev, { role: 'user', content: userMessage }]);
    setIsLoading(true);

    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), CHAT_TIMEOUT);

    try {
      // Agrokorea 공용 Cloudflare Worker 챗봇 프록시 호출
      const chatbotApiUrl = import.meta.env.VITE_CHATBOT_API_URL || 'https://vetacol.hongsoonil02.workers.dev/api/chat';
      const response = await fetch(chatbotApiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          product: 'monsmecta',
          message: userMessage,
          language: i18n.language
        }),
        signal: controller.signal
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      setMessages(prev => [...prev, { role: 'assistant', content: data.reply }]);
    } catch (error) {
      console.error('Chat error:', error);
      setMessages(prev => [...prev, { role: 'assistant', content: t('chat.error') }]);
    } finally {
      clearTimeout(timer);
      setIsLoading(false);
    }
  };

  const isRtl = i18n.language === 'ar';
  const langLabelMap = {
    ko: '한국어', en: 'English', ja: '日本語', zh: '中文', es: 'Español',
    fr: 'Français', de: 'Deutsch', th: 'ไทย', vi: 'Tiếng Việt', ru: 'Русский',
    pt: 'Português', ar: 'العربية', id: 'Bahasa Indonesia', ms: 'Bahasa Melayu', tr: 'Türkçe'
  };
  const currentLangLabel = langLabelMap[i18n.language] || i18n.language?.toUpperCase() || 'KO';

  if (typeof document === 'undefined') return null;

  return createPortal((
    <div className={`fixed bottom-[calc(5.2rem+env(safe-area-inset-bottom,0px))] z-[80] ${isRtl ? 'left-3 sm:left-6' : 'right-3 sm:right-6'}`}>
      {/* 챗봇 토글 버튼 */}
      <button
        onClick={toggleChat}
        className={`${isOpen ? 'hidden' : 'flex'} items-center justify-center w-14 h-14 sm:w-16 sm:h-16 bg-[#00513b] hover:bg-[#003d2b] active:bg-[#00281d] text-white rounded-full shadow-2xl border-2 border-emerald-400/50 hover:scale-105 active:scale-95 transition-all duration-300 focus:outline-none focus-visible:ring-4 focus-visible:ring-emerald-400/50`}
        aria-label={t('chat.openLabel', 'AI 임상 챗봇 열기')}
      >
        <svg xmlns="http://www.w3.org/2000/svg" className="h-7 w-7 sm:h-8 sm:w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
        </svg>
      </button>

      {/* 챗봇 창 */}
      <div
        dir={isRtl ? 'rtl' : 'ltr'}
        className={`${isOpen ? 'flex' : 'hidden'} absolute bottom-0 ${isRtl ? 'left-0 origin-bottom-left' : 'right-0 origin-bottom-right'} flex-col w-[350px] max-w-[calc(100vw-24px)] sm:w-[400px] sm:max-w-[400px] h-[550px] max-h-[82vh] bg-white rounded-2xl shadow-2xl border border-slate-200 overflow-hidden transition-all duration-300`}
      >
        {/* 헤더 */}
        <div className="flex items-center justify-between px-4 py-3 bg-[#00513b] text-white">
          <div className="flex items-center space-x-2 rtl:space-x-reverse">
            <div className="w-8 h-8 rounded-full bg-white flex items-center justify-center text-[#00513b] font-bold text-sm shadow-sm">
              AI
            </div>
            <div>
              <div className="flex items-center gap-1.5">
                <h3 className="font-bold text-sm">{t('chat.title', 'MONSMECTA AI')}</h3>
                <span className="text-[10px] bg-emerald-700/80 border border-emerald-400/40 text-emerald-100 px-1.5 py-0.2 rounded-full font-mono">
                  {currentLangLabel}
                </span>
              </div>
              <p className="text-[11px] text-[#a3e6cd] leading-tight mt-0.5">{t('chat.subtitle', '수의사 학술·임상 전용 어시스턴트')}</p>
            </div>
          </div>
          <button onClick={toggleChat} aria-label={t('chat.closeLabel', '챗봇 닫기')} className="text-white/80 hover:text-white p-1 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-400">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        {/* 언어 자동 안내 알림 바 */}
        <div className="bg-emerald-900/90 text-emerald-100 text-[11px] px-3 py-1.5 border-b border-emerald-800 flex items-center justify-between">
          <span className="flex items-center gap-1">
            <span aria-hidden="true">🌐</span>
            <span>{t('chat.langNotice', `질문하시면 ${currentLangLabel}로 자동 답변드립니다.`)}</span>
          </span>
        </div>

        {/* 메시지 영역 */}
        <div className="flex-1 p-4 overflow-y-auto bg-slate-50 space-y-4">
          <div className="flex justify-start">
            <div className={`max-w-[85%] rounded-2xl px-4 py-2.5 text-sm leading-relaxed bg-white text-slate-800 border border-slate-200 shadow-sm ${isRtl ? 'rounded-br-none' : 'rounded-bl-none'} whitespace-pre-wrap`}>
              {t('chat.greeting', '반갑습니다! 몬스멕타 학술·임상 AI 어시스턴트입니다. 성분, 임상 투여 프로토콜, 타 약물 병용에 대해 무엇이든 질문하세요.')}
            </div>
          </div>
          {messages.map((msg, index) => (
            <div key={index} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
              <div
                className={`max-w-[85%] rounded-2xl px-4 py-2.5 text-sm leading-relaxed ${
                  msg.role === 'user'
                    ? `bg-[#00513b] text-white ${isRtl ? 'rounded-bl-none' : 'rounded-br-none'}`
                    : `bg-white text-slate-800 border border-slate-200 shadow-sm ${isRtl ? 'rounded-br-none' : 'rounded-bl-none'} whitespace-pre-wrap`
                }`}
              >
                {msg.content}
              </div>
            </div>
          ))}
          {isLoading && (
            <div className="flex justify-start">
              <div className={`bg-white border border-slate-200 shadow-sm rounded-2xl ${isRtl ? 'rounded-br-none' : 'rounded-bl-none'} px-4 py-3 flex space-x-2 rtl:space-x-reverse items-center`}>
                <div className="w-2 h-2 bg-emerald-500 rounded-full animate-bounce"></div>
                <div className="w-2 h-2 bg-emerald-500 rounded-full animate-bounce delay-75"></div>
                <div className="w-2 h-2 bg-emerald-500 rounded-full animate-bounce delay-150"></div>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        {/* 입력 영역 */}
        <div className="bg-white border-t border-slate-200">
          {/* FAQ Quick Replies */}
          <div className="px-3 pt-2 pb-1 flex space-x-2 rtl:space-x-reverse overflow-x-auto scrollbar-hide">
            {['faq1', 'faq2', 'faq3'].map((faqKey) => (
              <button
                key={faqKey}
                onClick={() => setInput(t(`chat.${faqKey}`))}
                className="whitespace-nowrap px-3 py-1.5 bg-[#f0f9f6] hover:bg-[#e0f2ec] text-[#00513b] text-xs font-medium rounded-full transition-colors border border-[#c2e5d9]"
                disabled={isLoading}
              >
                {t(`chat.${faqKey}`)}
              </button>
            ))}
          </div>
          <form onSubmit={handleSubmit} className="px-3 pb-3 pt-1">
            <div className="flex items-center bg-slate-100 rounded-full overflow-hidden px-2 py-1 border border-slate-200 focus-within:border-emerald-500 focus-within:ring-2 focus-within:ring-emerald-500/20">
              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder={t('chat.placeholder', '궁금한 점을 입력하세요...')}
                className="flex-1 bg-transparent px-3 py-2 text-sm focus:outline-none text-slate-800"
                disabled={isLoading}
              />
              <button
                type="submit"
                disabled={!input.trim() || isLoading}
                className="w-8 h-8 flex items-center justify-center bg-[#00513b] text-white rounded-full disabled:opacity-50 hover:bg-[#003d2b] transition-colors shrink-0"
                aria-label={t('chat.send', '전송')}
              >
                <svg xmlns="http://www.w3.org/2000/svg" className={`h-4 w-4 transform ${isRtl ? '-rotate-90' : 'rotate-90'}`} viewBox="0 0 20 20" fill="currentColor">
                  <path d="M10.894 2.553a1 1 0 00-1.788 0l-7 14a1 1 0 001.169 1.409l5-1.429A1 1 0 009 15.571V11a1 1 0 112 0v4.571a1 1 0 00.725.962l5 1.428a1 1 0 001.17-1.408l-7-14z" />
                </svg>
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  ), document.body);
}
