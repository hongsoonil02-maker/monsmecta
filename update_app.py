import os

app_jsx_path = r"c:\Users\sooni\monsmecta-landing\src\App.jsx"

with open(app_jsx_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace state
content = content.replace(
    "const [iframeHeight, setIframeHeight] = useState(1800);",
    "const [iframeHeights, setIframeHeights] = useState({ james: 1800, scenario: 1800, dashboard: 1800 });"
)

# Replace message listener
old_listener = """  useEffect(() => {
    const handleMessage = (event) => {
      if (event.data && event.data.type === 'resize-iframe') {
        setIframeHeight(event.data.height);
      }
    };
    window.addEventListener('message', handleMessage);
    return () => window.removeEventListener('message', handleMessage);
  }, []);"""

new_listener = """  useEffect(() => {
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
  }, []);"""

content = content.replace(old_listener, new_listener)

# Replace iframe section
old_iframe_section = """        {/* 인포그래픽 섹션 */}
        <div id="infographic" className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-extrabold text-slate-900 sm:text-4xl">상세 학술 데이터 및 처방 가이드</h2>
            <p className="mt-4 text-lg text-slate-500">닥터 제임스홍의 실제 임상 경험이 반영된 오리지널 데이터를 확인하세요.</p>
          </div>
          
          <div 
            className="bg-slate-50 rounded-3xl shadow-xl border border-slate-200 overflow-hidden relative"
            style={{ height: iframeHeight ? `${iframeHeight}px` : '1800px' }}
          >
            <iframe 
              src={`${import.meta.env.BASE_URL}assets/james_infographic.html?v=2.0`} 
              className="absolute top-0 left-0 w-full h-full border-0" 
              title="몬스멕타 인포그래픽" 
              scrolling="no"
            />
          </div>
        </div>"""

new_iframe_section = """        {/* 인포그래픽 섹션 */}
        <div id="infographic" className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16 space-y-16">
          
          <div>
            <div className="text-center mb-12">
              <h2 className="text-3xl font-extrabold text-slate-900 sm:text-4xl">상세 학술 데이터 및 처방 가이드</h2>
              <p className="mt-4 text-lg text-slate-500">닥터 제임스홍의 실제 임상 경험이 반영된 오리지널 데이터를 확인하세요.</p>
            </div>
            
            <div 
              className="bg-slate-50 rounded-3xl shadow-xl border border-slate-200 overflow-hidden relative"
              style={{ height: iframeHeights.james ? `${iframeHeights.james}px` : '1800px' }}
            >
              <iframe 
                src={`${import.meta.env.BASE_URL}assets/james_infographic.html?v=2.1`} 
                className="absolute top-0 left-0 w-full h-full border-0" 
                title="몬스멕타 인포그래픽" 
                scrolling="no"
              />
            </div>
          </div>

          <div>
            <div 
              className="bg-slate-50 rounded-3xl shadow-xl border border-slate-200 overflow-hidden relative"
              style={{ height: iframeHeights.dashboard ? `${iframeHeights.dashboard}px` : '1800px' }}
            >
              <iframe 
                src={`${import.meta.env.BASE_URL}assets/monsmecta_dashboard.html?v=1.0`} 
                className="absolute top-0 left-0 w-full h-full border-0" 
                title="몬스멕타 전략 대시보드" 
                scrolling="no"
              />
            </div>
          </div>

          <div>
            <div 
              className="bg-slate-50 rounded-3xl shadow-xl border border-slate-200 overflow-hidden relative"
              style={{ height: iframeHeights.scenario ? `${iframeHeights.scenario}px` : '1800px' }}
            >
              <iframe 
                src={`${import.meta.env.BASE_URL}assets/monsmecta_scenario.html?v=1.0`} 
                className="absolute top-0 left-0 w-full h-full border-0" 
                title="몬스멕타 상담 시나리오" 
                scrolling="no"
              />
            </div>
          </div>

        </div>"""

content = content.replace(old_iframe_section, new_iframe_section)

with open(app_jsx_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("App.jsx updated successfully.")
