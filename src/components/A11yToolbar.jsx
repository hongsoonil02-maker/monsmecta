import React, { useState, useEffect } from 'react';

const A11yToolbar = () => {
  const [highContrast, setHighContrast] = useState(false);
  const [largeText, setLargeText] = useState(false);
  const [isOpen, setIsOpen] = useState(false);

  useEffect(() => {
    if (highContrast) {
      document.documentElement.classList.add('high-contrast');
    } else {
      document.documentElement.classList.remove('high-contrast');
    }
  }, [highContrast]);

  useEffect(() => {
    if (largeText) {
      document.documentElement.classList.add('large-text');
    } else {
      document.documentElement.classList.remove('large-text');
    }
  }, [largeText]);

  return (
    <div className="fixed bottom-24 right-4 sm:bottom-28 sm:right-6 z-[9999] flex flex-col items-end gap-2">
      {isOpen && (
        <div className="bg-white border border-gray-200 rounded-lg shadow-xl p-3 flex flex-col gap-2 mb-2 w-48">
          <div className="text-sm font-bold text-gray-700 border-b pb-2 mb-1">접근성 설정 (A11y)</div>
          <button
            onClick={() => setHighContrast(!highContrast)}
            className={`px-3 py-2 text-sm font-semibold rounded-md text-left transition-colors ${highContrast ? 'bg-[#00513b] text-white' : 'bg-gray-100 text-gray-700 hover:bg-gray-200'}`}
            aria-pressed={highContrast}
          >
            {highContrast ? '고대비 끄기' : '고대비 켜기'}
          </button>
          <button
            onClick={() => setLargeText(!largeText)}
            className={`px-3 py-2 text-sm font-semibold rounded-md text-left transition-colors ${largeText ? 'bg-[#00513b] text-white' : 'bg-gray-100 text-gray-700 hover:bg-gray-200'}`}
            aria-pressed={largeText}
          >
            {largeText ? '글씨 크기 원상복구' : '글씨 확대'}
          </button>
        </div>
      )}
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="bg-blue-600 text-white w-12 h-12 rounded-full shadow-lg flex items-center justify-center hover:bg-blue-700 focus:outline-none focus:ring-4 focus:ring-blue-300 transition-transform hover:scale-105"
        aria-label="접근성 메뉴 열기"
        aria-expanded={isOpen}
      >
        <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
        </svg>
      </button>
    </div>
  );
};

export default A11yToolbar;
