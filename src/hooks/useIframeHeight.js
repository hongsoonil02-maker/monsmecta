import { useEffect, useState } from 'react';

const useIframeHeight = (allowedSources) => {
  const [iframeHeights, setIframeHeights] = useState({});

  useEffect(() => {
    const handleMessage = (event) => {
      if (allowedSources.has(event.data.source) && event.data.type === 'resize-iframe') {
        setIframeHeights(prev => ({
          ...prev,
          [event.data.source]: event.data.height,
        }));
      }
    };

    window.addEventListener('message', handleMessage);
    return () => {
      window.removeEventListener('message', handleMessage);
    };
  }, [allowedSources]);

  return iframeHeights;
};

export default useIframeHeight;