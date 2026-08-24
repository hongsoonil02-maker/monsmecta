import { useEffect, useRef } from 'react';

/**
 * 공통 모달 동작: ESC 닫기, 배경 스크롤 잠금, 포커스 진입/복원.
 * 반환한 ref는 모달 패널 최상위 div에 연결한다 (tabIndex={-1} 권장).
 */
const useModalBehavior = (isOpen, onClose) => {
  const panelRef = useRef(null);
  const onCloseRef = useRef(onClose);

  useEffect(() => {
    onCloseRef.current = onClose;
  });

  useEffect(() => {
    if (!isOpen) return undefined;

    const previouslyFocused = document.activeElement;

    const handleKeyDown = (e) => {
      if (e.key === 'Escape') onCloseRef.current?.();
    };
    document.addEventListener('keydown', handleKeyDown);

    const { overflow } = document.body.style;
    document.body.style.overflow = 'hidden';

    const raf = requestAnimationFrame(() => {
      const panel = panelRef.current;
      if (!panel) return;
      const target =
        panel.querySelector('[data-autofocus]') ||
        panel.querySelector('input, select, textarea, button');
      if (target && typeof target.focus === 'function') {
        target.focus({ preventScroll: true });
      } else if (typeof panel.focus === 'function') {
        panel.focus({ preventScroll: true });
      }
    });

    return () => {
      document.removeEventListener('keydown', handleKeyDown);
      document.body.style.overflow = overflow;
      cancelAnimationFrame(raf);
      if (previouslyFocused && typeof previouslyFocused.focus === 'function') {
        previouslyFocused.focus({ preventScroll: true });
      }
    };
  }, [isOpen]);

  return panelRef;
};

/**
 * 배경(오버레이) 클릭 시 닫기: 오버레이 자체가 클릭된 경우에만 닫는다.
 */
const handleBackdropClick = (e, onClose) => {
  if (e.target === e.currentTarget) onClose?.();
};

export { useModalBehavior, handleBackdropClick };
export default useModalBehavior;
