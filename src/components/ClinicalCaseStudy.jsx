import { useState, useRef, useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import { CLINICAL_CASE_DATA } from '../data/clinicalCaseData';

export default function ClinicalCaseStudy() {
  const { t } = useTranslation();
  const [activePhaseIndex, setActivePhaseIndex] = useState(0);
  const [selectedVideo, setSelectedVideo] = useState(CLINICAL_CASE_DATA.videos[0]);
  const [isChartModalOpen, setIsChartModalOpen] = useState(false);
  const [isVideoModalOpen, setIsVideoModalOpen] = useState(false);
  const [modalVideo, setModalVideo] = useState(null);
  const videoRef = useRef(null);

  const currentChart = CLINICAL_CASE_DATA.charts[activePhaseIndex];
  const phaseVideos = CLINICAL_CASE_DATA.videos.filter(v => v.phaseKey === currentChart.id);

  const handleSelectPhase = (index) => {
    setActivePhaseIndex(index);
    const targetChart = CLINICAL_CASE_DATA.charts[index];
    const firstVid = CLINICAL_CASE_DATA.videos.find(v => v.phaseKey === targetChart.id) || CLINICAL_CASE_DATA.videos[0];
    setSelectedVideo(firstVid);
    if (videoRef.current) {
      videoRef.current.load();
    }
  };

  const handleSelectVideo = (video) => {
    setSelectedVideo(video);
    if (videoRef.current) {
      videoRef.current.load();
      videoRef.current.play().catch(() => {});
    }
  };

  const openVideoModal = (video) => {
    setModalVideo(video);
    setIsVideoModalOpen(true);
  };

  // 모달 키보드 ESC 닫기 접근성 지원
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'Escape') {
        if (isChartModalOpen) setIsChartModalOpen(false);
        if (isVideoModalOpen) setIsVideoModalOpen(false);
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isChartModalOpen, isVideoModalOpen]);

  return (
    <section 
      id="clinical-case-study" 
      aria-labelledby="clinical-case-heading"
      className="py-16 sm:py-20 bg-gradient-to-b from-slate-900 via-slate-950 to-slate-900 text-white relative overflow-hidden border-t border-b border-emerald-500/20"
    >
      {/* 배경 장식 글로우 */}
      <div className="absolute top-1/4 left-1/2 -translate-x-1/2 w-[800px] h-[400px] bg-emerald-500/10 blur-[140px] pointer-events-none rounded-full" />
      <div className="absolute bottom-10 end-10 w-96 h-96 bg-amber-500/10 blur-[120px] pointer-events-none rounded-full" />

      {/* 삼성 갤럭시 S20 Ultra (412px) 및 모바일 반응형 컨테이너 */}
      <div className="max-w-7xl mx-auto px-3.5 sm:px-6 lg:px-8 relative z-10">
        
        {/* 헤더 섹션 */}
        <header className="text-center max-w-3xl mx-auto mb-10 sm:mb-14">
          <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-emerald-950/90 border border-emerald-400/40 text-emerald-300 text-xs sm:text-sm font-black mb-4 shadow-lg shadow-emerald-950/50">
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-ping" aria-hidden="true" />
            {t('clinicalCase.badge', '🎙️ 몬스멕타 자문위원 리얼 임상 다큐멘터리')}
          </div>
          
          <h2 id="clinical-case-heading" className="text-2xl sm:text-4xl lg:text-5xl font-black text-white tracking-tight leading-tight mb-4 break-keep">
            {t('clinicalCase.title', '55일령 발작 환축의')}{' '}
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-emerald-300 via-emerald-400 to-amber-300">
              {t('clinicalCase.titleHighlight', '7일간의 기적')}
            </span>
          </h2>
          
          <p className="text-xs sm:text-base text-slate-300 font-medium break-keep leading-relaxed max-w-2xl mx-auto">
            {t('clinicalCase.subtitle', '하남 사랑동물병원 김동준 원장님이 환축의 생사를 다투며 직접 작성한 자필 수기 차트와 진료실 무편집 직캠 동영상 8편의 기록입니다.')}
          </p>

          {/* 문화권 배려: 100% 천연 미네랄 무독성 안심 뱃지 */}
          <div className="mt-4 inline-block px-3 py-1 bg-emerald-900/40 border border-emerald-500/30 rounded-full text-[11px] text-emerald-200 font-semibold">
            {t('clinicalCase.mineralSafe', '🌿 100% 천연 점토 광물 미네랄 제제 (무동물성 성분 · 비스테로이드 · 간/신장 부담 제로)')}
          </div>

          {/* 환축 초진 스펙 바 (삼성 S20 Ultra 412px 최적화 2x2 그리드) */}
          <div className="mt-6 grid grid-cols-2 sm:grid-cols-4 gap-2.5 sm:gap-3 bg-white/5 p-3.5 sm:p-4 rounded-2xl border border-white/10 backdrop-blur-md text-start">
            <div className="border-e border-white/10 pe-2">
              <span className="text-[11px] font-bold text-slate-400 block">{t('clinicalCase.patient', '환축 정보')}</span>
              <span className="text-xs sm:text-sm font-bold text-white">{t('clinicalCase.patientVal', '토이푸들 ♂ (55일령)')}</span>
            </div>
            <div className="border-e border-white/10 pe-2">
              <span className="text-[11px] font-bold text-slate-400 block">{t('clinicalCase.symptom', '내원시 증상')}</span>
              <span className="text-xs sm:text-sm font-bold text-rose-400">{t('clinicalCase.symptomVal', '심한 발작·식욕전폐')}</span>
            </div>
            <div className="border-e border-white/10 pe-2">
              <span className="text-[11px] font-bold text-slate-400 block">{t('clinicalCase.kit', '5종 키트 검사')}</span>
              <span className="text-xs sm:text-sm font-bold text-emerald-400">{t('clinicalCase.kitVal', '파보·코로나 음성(Neg)')}</span>
            </div>
            <div>
              <span className="text-[11px] font-bold text-slate-400 block">{t('clinicalCase.prognosis', '최종 예후')}</span>
              <span className="text-xs sm:text-sm font-bold text-amber-300">{t('clinicalCase.prognosisVal', '7일 만에 완치 [퇴원]')}</span>
            </div>
          </div>
        </header>

        {/* 3단계 타임라인 스텝퍼 탭 */}
        <nav aria-label="임상 경과 타임라인" className="flex flex-col sm:flex-row gap-2.5 sm:gap-3 max-w-4xl mx-auto mb-10">
          {CLINICAL_CASE_DATA.charts.map((chart, idx) => {
            const isActive = idx === activePhaseIndex;
            return (
              <button
                key={chart.id}
                onClick={() => handleSelectPhase(idx)}
                aria-current={isActive ? 'step' : undefined}
                className={`flex-1 text-start p-3.5 sm:p-4 rounded-2xl border min-h-[48px] transition-all duration-300 relative overflow-hidden focus:outline-none focus-visible:ring-2 focus-visible:ring-emerald-400 ${
                  isActive
                    ? 'bg-gradient-to-r from-emerald-900/90 to-emerald-950 border-emerald-400 shadow-lg shadow-emerald-950/60 ring-2 ring-emerald-400/20'
                    : 'bg-white/5 border-white/10 hover:bg-white/10 text-slate-400'
                }`}
              >
                <div className="flex items-center justify-between mb-1">
                  <span className={`text-[11px] font-extrabold px-2 py-0.5 rounded-full ${isActive ? 'bg-emerald-400 text-slate-950' : 'bg-slate-800 text-slate-400'}`}>
                    STEP 0{idx + 1}
                  </span>
                  <span className={`text-[11px] font-mono ${isActive ? 'text-emerald-300' : 'text-slate-500'}`}>
                    {chart.period}
                  </span>
                </div>
                <h3 className={`text-xs sm:text-base font-bold line-clamp-1 ${isActive ? 'text-white' : 'text-slate-300'}`}>
                  {chart.title}
                </h3>
              </button>
            );
          })}
        </nav>

        {/* 메인 듀얼 스크린 (좌: 수기 차트 원본 / 우: 스마트폰 세로 직캠 영상) */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 sm:gap-8 mb-16 items-stretch">
          
          {/* 좌측: 수기 차트 원본 카드 (5 cols) */}
          <article className="lg:col-span-5 flex flex-col bg-slate-900/90 rounded-3xl p-4 sm:p-6 border border-white/10 shadow-2xl backdrop-blur-xl">
            <div className="flex items-center justify-between mb-3 sm:mb-4">
              <div className="flex items-center gap-2">
                <span className="w-3 h-3 rounded-full bg-amber-400" aria-hidden="true" />
                <h4 className="text-sm sm:text-base font-bold text-white">
                  {t('clinicalCase.handwrittenTitle', '김동준 원장 자필 차트 원본')}
                </h4>
              </div>
              <button
                onClick={() => setIsChartModalOpen(true)}
                className="min-h-[40px] text-xs font-bold px-3 py-1.5 rounded-xl bg-white/10 hover:bg-emerald-600 hover:text-white transition-colors border border-white/10 text-emerald-300 flex items-center gap-1.5 shadow focus:outline-none focus-visible:ring-2 focus-visible:ring-emerald-400"
                aria-label={t('clinicalCase.zoomBtn', '차트 원본 크게보기')}
              >
                <span>{t('clinicalCase.zoomBtn', '🔍 원본 크게보기')}</span>
              </button>
            </div>

            {/* 차트 썸네일 이미지 (클릭 시 확대) */}
            <figure 
              onClick={() => setIsChartModalOpen(true)}
              className="relative group rounded-2xl overflow-hidden cursor-pointer border border-white/15 bg-white/5 flex-1 min-h-[260px] sm:min-h-[300px] flex items-center justify-center p-2 hover:border-emerald-400 transition-all shadow-inner"
            >
              <img
                src={`${import.meta.env.BASE_URL}${currentChart.src}`}
                alt={`${currentChart.title} - 김동준 원장 자필 수기 임상 차트`}
                className="w-full h-auto max-h-[360px] object-contain rounded-xl transition-transform duration-500 group-hover:scale-[1.02]"
              />
              <figcaption className="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center backdrop-blur-xs">
                <span className="px-4 py-2 bg-emerald-600/90 text-white rounded-xl text-xs font-bold shadow-lg flex items-center gap-1.5">
                  {t('clinicalCase.zoomHover', '🔍 고해상도 자필 글씨 확대보기')}
                </span>
              </figcaption>
            </figure>

            {/* 자필 차트 하이라이트 해설 */}
            <div className="mt-4 pt-4 border-t border-white/10 space-y-2">
              <span className="text-[11px] font-bold text-amber-300 tracking-wide uppercase block">
                {t('clinicalCase.chartRecord', '📋 자필 차트 주요 기록')}
              </span>
              <ul className="space-y-1.5 text-xs text-slate-300 text-start">
                {currentChart.highlights.map((h, i) => (
                  <li key={i} className="flex items-start gap-2">
                    <span className="text-emerald-400 font-bold shrink-0" aria-hidden="true">✔</span>
                    <span className="leading-snug">{h}</span>
                  </li>
                ))}
              </ul>
            </div>
          </article>

          {/* 우측: 실제 진료실 비디오 플레이어 (스마트폰 세로 9:16 최적화) (7 cols) */}
          <article className="lg:col-span-7 flex flex-col bg-slate-900/90 rounded-3xl p-4 sm:p-6 border border-white/10 shadow-2xl backdrop-blur-xl">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-3 sm:mb-4">
              <div className="flex items-center gap-2">
                <span className="w-3 h-3 rounded-full bg-emerald-400 animate-pulse" aria-hidden="true" />
                <h4 className="text-sm sm:text-base font-bold text-white">
                  {t('clinicalCase.camTitle', '진료실 무편집 직캠 비디오')}
                </h4>
              </div>
              
              {/* 해당 페이즈에 영상이 여러 개일 때 스위치 탭 */}
              {phaseVideos.length > 1 && (
                <div className="flex items-center gap-1 bg-black/40 p-1 rounded-xl border border-white/10 overflow-x-auto">
                  {phaseVideos.map((v) => (
                    <button
                      key={v.id}
                      onClick={() => handleSelectVideo(v)}
                      className={`text-xs px-2.5 py-1.5 rounded-lg font-bold min-h-[36px] transition-all whitespace-nowrap focus:outline-none focus-visible:ring-2 focus-visible:ring-emerald-400 ${
                        selectedVideo.id === v.id
                          ? 'bg-emerald-500 text-slate-950 shadow'
                          : 'text-slate-400 hover:text-white'
                      }`}
                    >
                      {v.badge.split(' ')[1] || v.phase}
                    </button>
                  ))}
                </div>
              )}
            </div>

            {/* 비디오 화면 - 스마트폰 세로형 9:16 핏 최적화 */}
            <div className="relative rounded-2xl overflow-hidden bg-slate-950/80 border border-white/10 p-3 sm:p-5 flex items-center justify-center">
              <div className="w-full max-w-[260px] sm:max-w-[290px] aspect-[9/16] rounded-2xl overflow-hidden bg-black border-2 border-white/20 shadow-2xl relative">
                <video
                  ref={videoRef}
                  key={selectedVideo.file}
                  controls
                  playsInline
                  preload="metadata"
                  aria-label={`${selectedVideo.title} - ${selectedVideo.desc}`}
                  className="w-full h-full object-cover"
                >
                  <source src={`${import.meta.env.BASE_URL}assets/${selectedVideo.file}`} type="video/mp4" />
                  귀하의 브라우저는 비디오 태그를 지원하지 않습니다.
                </video>
              </div>
            </div>

            {/* 비디오 설명 카드 */}
            <div className="mt-4 pt-4 border-t border-white/10 flex flex-col sm:flex-row sm:items-center justify-between gap-3 text-start">
              <div>
                <div className="flex items-center gap-2 mb-1">
                  <span className={`text-[10px] font-bold px-2 py-0.5 rounded-full ${selectedVideo.badgeColor}`}>
                    {selectedVideo.badge}
                  </span>
                  <span className="text-xs text-slate-400 font-mono">
                    {t('clinicalCase.length', '길이')}: {selectedVideo.duration}
                  </span>
                </div>
                <h5 className="text-sm sm:text-base font-bold text-white">{selectedVideo.title}</h5>
                <p className="text-xs text-slate-300 mt-1 leading-relaxed">{selectedVideo.desc}</p>
              </div>

              <button
                onClick={() => openVideoModal(selectedVideo)}
                className="shrink-0 min-h-[42px] text-xs px-3.5 py-2 rounded-xl bg-emerald-600/20 hover:bg-emerald-600 border border-emerald-500/40 text-emerald-300 hover:text-white font-bold transition-all flex items-center gap-1.5 self-start sm:self-center focus:outline-none focus-visible:ring-2 focus-visible:ring-emerald-400 active:scale-95"
              >
                <span>{t('clinicalCase.fullscreenBtn', '⛶ 큰 화면 재생')}</span>
              </button>
            </div>
          </article>
        </div>

        {/* 8대 직캠 숏폼 비디오 전체 갤러리 */}
        <section aria-labelledby="cam-archive-heading" className="mt-10 sm:mt-12 mb-16">
          <div className="flex items-center justify-between mb-6 text-start">
            <div>
              <h3 id="cam-archive-heading" className="text-lg sm:text-2xl font-extrabold text-white">
                {t('clinicalCase.archiveTitle', '📹 사랑동물병원 직캠 8대 영상 전편 아카이브')}
              </h3>
              <p className="text-xs sm:text-sm text-slate-400 mt-1">
                {t('clinicalCase.archiveSubtitle', '스마트폰 세로 직캠으로 촬영된 무편집 진료실 현장 영상입니다. (클릭 시 고화질 재생)')}
              </p>
            </div>
          </div>

          {/* 8개 세로형 숏폼 카드 그리드 (삼성 S20 Ultra 412px 기준 2열, 테블릿 3열, 데스크톱 4열) */}
          <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3 sm:gap-4">
            {CLINICAL_CASE_DATA.videos.map((vid, idx) => (
              <div
                key={vid.id}
                role="button"
                tabIndex={0}
                onKeyDown={(e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openVideoModal(vid); } }}
                onClick={() => openVideoModal(vid)}
                aria-label={`${vid.title} 영상 열기`}
                className="group relative bg-slate-900/80 rounded-2xl p-2.5 sm:p-3 border border-white/10 hover:border-emerald-400/80 transition-all duration-300 cursor-pointer flex flex-col justify-between hover:shadow-xl hover:shadow-emerald-950/40 text-start focus:outline-none focus-visible:ring-2 focus-visible:ring-emerald-400 active:scale-[0.98]"
              >
                <div>
                  {/* 세로형 9:16 썸네일 */}
                  <div className="relative aspect-[9/16] rounded-xl overflow-hidden bg-black mb-2.5 border border-white/10 shadow">
                    <img
                      src={`${import.meta.env.BASE_URL}assets/clinical_thumbs/thumb_${idx + 1}_${vid.file.slice(0, 20)}.jpg`}
                      alt={vid.title}
                      className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
                      onError={(e) => {
                        e.target.style.display = 'none';
                      }}
                    />
                    <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent flex items-end justify-between p-2">
                      <span className="text-[10px] font-bold px-1.5 py-0.5 rounded bg-black/70 text-white font-mono">
                        {vid.duration}
                      </span>
                      <div className="w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-emerald-500 text-slate-950 flex items-center justify-center text-xs font-black shadow-lg group-hover:scale-110 transition-transform">
                        ▶
                      </div>
                    </div>
                  </div>
                  <span className={`inline-block text-[10px] font-bold px-2 py-0.5 rounded-full mb-1.5 ${vid.badgeColor}`}>
                    {vid.phase}
                  </span>
                  <h4 className="text-xs sm:text-sm font-bold text-white group-hover:text-emerald-300 transition-colors line-clamp-2">
                    {vid.title}
                  </h4>
                </div>
                <p className="text-[11px] text-slate-400 mt-2 line-clamp-2 leading-relaxed">
                  {vid.desc}
                </p>
              </div>
            ))}
          </div>
        </section>

        {/* B2B 수의사용 3단계 응급 프로토콜 카드 */}
        <section aria-labelledby="protocol-heading" className="bg-gradient-to-br from-emerald-950/90 via-slate-900 to-slate-950 p-5 sm:p-10 rounded-3xl border border-emerald-500/30 shadow-2xl relative overflow-hidden">
          <div className="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-4 sm:gap-6 mb-6 sm:mb-8 border-b border-white/10 pb-6 text-start">
            <div>
              <span className="px-3 py-1 bg-amber-400/20 text-amber-300 text-xs font-extrabold rounded-full border border-amber-400/30 inline-block mb-2">
                {t('clinicalCase.protocolSub', 'Veterinary Clinical Protocol')}
              </span>
              <h3 id="protocol-heading" className="text-lg sm:text-2xl lg:text-3xl font-black text-white break-keep">
                {CLINICAL_CASE_DATA.protocol.title}
              </h3>
              <p className="text-xs sm:text-sm text-emerald-300/90 mt-1">
                적용 대상: {CLINICAL_CASE_DATA.protocol.target}
              </p>
            </div>

            <a
              href="#audio-testimonial"
              className="min-h-[44px] px-4 sm:px-5 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs sm:text-sm transition-colors shrink-0 shadow-lg flex items-center gap-2 border border-emerald-400/40 focus:outline-none focus-visible:ring-2 focus-visible:ring-emerald-400 active:scale-95"
            >
              <span>{t('clinicalCase.listenCall', '🎙️ 김동준 원장 통화 육성 인터뷰 듣기')}</span>
              <span className="rtl:rotate-180" aria-hidden="true">↓</span>
            </a>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 sm:gap-6 text-start">
            {CLINICAL_CASE_DATA.protocol.steps.map((s, idx) => (
              <div key={idx} className="bg-white/5 p-4 sm:p-5 rounded-2xl border border-white/10 flex flex-col justify-between">
                <div>
                  <div className="w-8 h-8 rounded-xl bg-emerald-500/20 border border-emerald-400/40 text-emerald-300 flex items-center justify-center font-black text-sm mb-3">
                    0{idx + 1}
                  </div>
                  <h4 className="text-sm sm:text-base font-bold text-white mb-1">{s.step}</h4>
                  <div className="text-xs font-bold text-emerald-400 mb-2">{s.product} ({s.dosage})</div>
                  <p className="text-xs text-slate-300 leading-relaxed">{s.detail}</p>
                </div>
              </div>
            ))}
          </div>
        </section>

      </div>

      {/* 수기 차트 전체화면 돋보기 라이트박스 모달 */}
      {isChartModalOpen && (
        <div 
          role="dialog"
          aria-modal="true"
          aria-label={t('clinicalCase.handwrittenTitle', '김동준 원장 자필 차트 원본')}
          className="fixed inset-0 z-50 bg-black/90 backdrop-blur-md flex items-center justify-center p-3 sm:p-4"
          onClick={() => setIsChartModalOpen(false)}
        >
          <div 
            className="relative max-w-4xl w-full max-h-[90dvh] bg-slate-900 rounded-3xl p-4 sm:p-6 border border-white/20 flex flex-col shadow-2xl"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="flex items-center justify-between mb-3 border-b border-white/10 pb-3 text-start">
              <div>
                <h4 className="text-sm sm:text-lg font-bold text-white">{currentChart.title}</h4>
                <p className="text-xs text-emerald-300">{currentChart.period} · 하남 사랑동물병원 김동준 원장 자필 차트</p>
              </div>
              <button
                onClick={() => setIsChartModalOpen(false)}
                className="w-10 h-10 min-w-[40px] min-h-[40px] rounded-full bg-white/10 hover:bg-white/20 text-white flex items-center justify-center font-bold text-lg focus:outline-none focus-visible:ring-2 focus-visible:ring-emerald-400"
                aria-label={t('clinicalCase.chartClose', '차트 닫기')}
              >
                ✕
              </button>
            </div>
            <div className="flex-1 overflow-auto flex items-center justify-center p-2 bg-slate-950/60 rounded-2xl border border-white/5">
              <img
                src={`${import.meta.env.BASE_URL}${currentChart.src}`}
                alt={currentChart.title}
                className="max-w-full max-h-[75dvh] object-contain rounded-xl shadow-2xl"
              />
            </div>
          </div>
        </div>
      )}

      {/* 비디오 큰 화면 팝업 모달 - 스마트폰 세로 9:16 핏 최적화 */}
      {isVideoModalOpen && modalVideo && (
        <div 
          role="dialog"
          aria-modal="true"
          aria-label={modalVideo.title}
          className="fixed inset-0 z-50 bg-black/95 backdrop-blur-md flex items-center justify-center p-3 sm:p-4"
          onClick={() => setIsVideoModalOpen(false)}
        >
          <div 
            className="relative max-w-sm sm:max-w-md w-full bg-slate-900/95 rounded-3xl p-4 sm:p-5 border border-white/20 flex flex-col shadow-2xl max-h-[92dvh] overflow-y-auto"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="flex items-center justify-between mb-3 border-b border-white/10 pb-3 text-start">
              <div className="pe-2">
                <span className={`text-[10px] font-bold px-2 py-0.5 rounded-full ${modalVideo.badgeColor} me-2`}>
                  {modalVideo.badge}
                </span>
                <h4 className="text-sm sm:text-base font-bold text-white inline-block">{modalVideo.title}</h4>
              </div>
              <button
                onClick={() => setIsVideoModalOpen(false)}
                className="w-9 h-9 min-w-[36px] min-h-[36px] rounded-full bg-white/10 hover:bg-white/20 text-white flex items-center justify-center font-bold text-base shrink-0 focus:outline-none focus-visible:ring-2 focus-visible:ring-emerald-400"
                aria-label={t('clinicalCase.videoClose', '비디오 닫기')}
              >
                ✕
              </button>
            </div>
            
            {/* 스마트폰 9:16 세로 핏 비디오 컨테이너 (검은 여백 제로) */}
            <div className="w-full max-w-[300px] sm:max-w-[320px] mx-auto aspect-[9/16] bg-black rounded-2xl overflow-hidden shadow-2xl border border-white/15 flex items-center justify-center relative">
              <video
                controls
                autoPlay
                playsInline
                aria-label={modalVideo.title}
                className="w-full h-full object-cover"
              >
                <source src={`${import.meta.env.BASE_URL}assets/${modalVideo.file}`} type="video/mp4" />
                브라우저가 비디오를 지원하지 않습니다.
              </video>
            </div>
            
            <p className="text-xs text-slate-300 mt-3 leading-relaxed bg-white/5 p-3 rounded-xl border border-white/5 text-start">
              {modalVideo.desc}
            </p>
          </div>
        </div>
      )}

    </section>
  );
}
