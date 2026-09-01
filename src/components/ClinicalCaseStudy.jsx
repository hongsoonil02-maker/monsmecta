import { useState, useRef, useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import { CLINICAL_CASE_DATA } from '../data/clinicalCaseData';

export default function ClinicalCaseStudy() {
  const { t } = useTranslation();
  const [activePhaseIndex, setActivePhaseIndex] = useState(0);
  const [selectedVideo, setSelectedVideo] = useState(CLINICAL_CASE_DATA.videos[0]);
  const [isChartModalOpen, setIsChartModalOpen] = useState(false);
  const [isVideoModalOpen, setIsVideoModalOpen] = useState(false);
  const [isDocuModalOpen, setIsDocuModalOpen] = useState(false);
  const [isTranscriptOpen, setIsTranscriptOpen] = useState(false);
  const [copySuccess, setCopySuccess] = useState(false);
  const [modalVideo, setModalVideo] = useState(null);
  const videoRef = useRef(null);

  const docuVideoUrl = `${import.meta.env.BASE_URL}assets/kimdongjun_clinical_documentary_v2.mp4?v=20260828b`;

  const handleCopyDocuLink = (e) => {
    e.stopPropagation();
    const url = 'https://monsmecta.kr/assets/kimdongjun_clinical_documentary_v2.mp4';
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(url).then(() => {
        setCopySuccess(true);
        setTimeout(() => setCopySuccess(false), 2500);
      });
    } else {
      alert('동영상 링크: ' + url);
    }
  };

  const currentChart = CLINICAL_CASE_DATA.charts[activePhaseIndex];
  const phaseVideos = CLINICAL_CASE_DATA.videos.filter(v => v.phaseKey === currentChart.id);

  const handleSelectPhase = (index) => {
    setActivePhaseIndex(index);
    const targetChart = CLINICAL_CASE_DATA.charts[index];
    const firstVid = CLINICAL_CASE_DATA.videos.find(v => v.phaseKey === targetChart.id) || CLINICAL_CASE_DATA.videos[0];
    setSelectedVideo(firstVid);
    if (videoRef.current) {
      videoRef.current.load();
      videoRef.current.play().catch(() => {});
    }
  };

  const handleSelectVideo = (video) => {
    setSelectedVideo(video);
    // 선택한 영상의 STEP으로 상단 차트/스텝 탭도 자동 동기화
    const chartIndex = CLINICAL_CASE_DATA.charts.findIndex(c => c.id === video.phaseKey);
    if (chartIndex !== -1) {
      setActivePhaseIndex(chartIndex);
    }
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
        if (isDocuModalOpen) setIsDocuModalOpen(false);
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isChartModalOpen, isVideoModalOpen, isDocuModalOpen]);

  // 모달 활성화 시 배경 스크롤 락 (모바일 터치 편의 최적화)
  useEffect(() => {
    if (isChartModalOpen || isVideoModalOpen || isDocuModalOpen) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = '';
    }
    return () => {
      document.body.style.overflow = '';
    };
  }, [isChartModalOpen, isVideoModalOpen, isDocuModalOpen]);

  return (
    <section 
      id="clinical-case-study" 
      aria-labelledby="clinical-case-heading"
      className="py-10 sm:py-14 bg-slate-50 text-slate-900 relative overflow-hidden border-y border-slate-200"
    >
      {/* 배경 은은한 앰비언트 글로우 */}
      <div className="absolute top-1/4 left-1/2 -translate-x-1/2 w-[800px] h-[400px] bg-emerald-300/20 blur-[140px] pointer-events-none rounded-full" />
      <div className="absolute bottom-10 end-10 w-96 h-96 bg-amber-200/20 blur-[120px] pointer-events-none rounded-full" />

      {/* 모바일 여유로운 컨테이너 */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        
        {/* 헤더 섹션 */}
        <header className="text-center max-w-3xl mx-auto mb-8 sm:mb-10">
          <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-emerald-100 border border-emerald-300 text-emerald-800 text-xs sm:text-sm font-black mb-4 shadow-sm">
            <span className="w-2 h-2 rounded-full bg-emerald-500 animate-ping" aria-hidden="true" />
            {t('clinicalCase.badge', '🎙️ 몬스멕타 자문위원 리얼 임상 다큐멘터리')}
          </div>
          
          <h2 id="clinical-case-heading" className="text-2xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight leading-tight mb-4 break-keep">
            {t('clinicalCase.title', '55일령 발작 환축의')}{' '}
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-emerald-600 via-teal-600 to-amber-600">
              {t('clinicalCase.titleHighlight', '7일간의 기적')}
            </span>
          </h2>
          
          <p className="text-xs sm:text-base text-slate-600 font-medium break-keep leading-relaxed max-w-2xl mx-auto">
            {t('clinicalCase.subtitle', '하남 사랑동물병원 김동준 원장님이 환축의 생사를 다투며 직접 작성한 자필 수기 차트와 진료실 무편집 직캠 동영상 8편의 기록입니다.')}
          </p>

          {/* 문화권 배려: 100% 천연 미네랄 무독성 안심 뱃지 */}
          <div className="mt-4 inline-block px-3.5 py-1.5 bg-emerald-50 border border-emerald-200 rounded-full text-[11px] text-emerald-800 font-bold shadow-xs">
            {t('clinicalCase.mineralSafe', '🌿 100% 천연 점토 광물 미네랄 제제 (무동물성 성분 · 비스테로이드 · 간/신장 부담 제로)')}
          </div>

          {/* 환축 초진 스펙 바 */}
          <div className="mt-6 grid grid-cols-2 sm:grid-cols-4 gap-2.5 sm:gap-3 bg-white p-3.5 sm:p-4 rounded-2xl border border-slate-200/90 shadow-sm text-start">
            <div className="border-e border-slate-100 pe-2">
              <span className="text-[11px] font-bold text-slate-400 block">{t('clinicalCase.patient', '환축 정보')}</span>
              <span className="text-xs sm:text-sm font-bold text-slate-900">{t('clinicalCase.patientVal', '토이푸들 ♂ (55일령)')}</span>
            </div>
            <div className="border-e border-slate-100 pe-2">
              <span className="text-[11px] font-bold text-slate-400 block">{t('clinicalCase.symptom', '내원시 증상')}</span>
              <span className="text-xs sm:text-sm font-bold text-rose-600">{t('clinicalCase.symptomVal', '심한 발작·식욕전폐')}</span>
            </div>
            <div className="border-e border-slate-100 pe-2">
              <span className="text-[11px] font-bold text-slate-400 block">{t('clinicalCase.kit', '5종 키트 검사')}</span>
              <span className="text-xs sm:text-sm font-bold text-emerald-700">{t('clinicalCase.kitVal', '파보·코로나 음성(Neg)')}</span>
            </div>
            <div>
              <span className="text-[11px] font-bold text-slate-400 block">{t('clinicalCase.prognosis', '최종 예후')}</span>
              <span className="text-xs sm:text-sm font-bold text-amber-700">{t('clinicalCase.prognosisVal', '7일 만에 완치 [퇴원]')}</span>
            </div>
          </div>
        </header>

        {/* 2분 54초 리얼 다큐멘터리 완성본 스페셜 쇼케이스 & 원클릭 공유 배너 */}
        <div className="mb-10 max-w-4xl mx-auto p-4 sm:p-6 bg-gradient-to-r from-[#006247] via-[#00513b] to-[#004432] rounded-3xl border border-emerald-500/50 shadow-xl text-start flex flex-col md:flex-row items-center justify-between gap-5 relative overflow-hidden group text-white">
          <div className="absolute top-0 right-0 w-80 h-80 bg-white/10 blur-3xl pointer-events-none" />
          
          <div className="space-y-2 z-10 flex-1">
            <div className="flex flex-wrap items-center gap-2">
              <span className="px-3 py-1 bg-amber-300 text-slate-950 text-[11px] sm:text-xs font-black rounded-full shadow-sm">
                {t('clinicalCase.docuBadge', '🎬 2분 54초 풀 다큐멘터리 완성본')}
              </span>
              <span className="text-xs text-emerald-200 font-bold">
                {t('clinicalCase.docuSpec', '1080p 세로 직캠 + AI 성우 내레이션')}
              </span>
            </div>
            <h3 className="text-base sm:text-2xl font-black text-white leading-snug break-keep">
              {t('clinicalCase.docuBannerTitle', '55일령 발작 토이푸들의 7일간의 기적 (전편 통합본)')}
            </h3>
            <p className="text-xs sm:text-sm text-emerald-100 leading-relaxed max-w-xl break-keep">
              {t('clinicalCase.docuBannerDesc', '응급 내원부터 1차 펌프 투약, 신경 반사 회복, 캔사료 폭풍 완식 먹방, 그리고 최종 완치 퇴원까지 8편의 직캠과 자필 차트를 2분 54초의 감동적인 다큐멘터리로 감상하고 동료 수의사분들께 바로 공유해 보세요.')}
            </p>
          </div>

          <div className="flex flex-col sm:flex-row md:flex-col lg:flex-row items-stretch sm:items-center gap-2.5 w-full md:w-auto shrink-0 z-10">
            <button
              onClick={() => setIsDocuModalOpen(true)}
              className="px-6 py-3.5 bg-gradient-to-r from-yellow-400 to-yellow-500 hover:from-yellow-300 hover:to-yellow-400 text-slate-950 font-black text-sm rounded-2xl shadow-lg hover:scale-105 active:scale-95 transition-all flex items-center justify-center gap-2 cursor-pointer focus:outline-none focus-visible:ring-2 focus-visible:ring-yellow-300"
              aria-label={t('clinicalCase.docuWatchBtn', '다큐 영상 전체 시청')}
            >
              <span className="text-lg" aria-hidden="true">▶</span>
              <span>{t('clinicalCase.docuWatchBtn', '다큐 영상 전체 시청')}</span>
            </button>
            <button
              onClick={handleCopyDocuLink}
              className="px-4 py-3.5 bg-white/15 hover:bg-white/25 text-white font-bold text-xs sm:text-sm rounded-2xl border border-white/30 hover:border-white/50 transition-all flex items-center justify-center gap-1.5 cursor-pointer focus:outline-none focus-visible:ring-2 focus-visible:ring-emerald-400"
              aria-label={copySuccess ? t('clinicalCase.docuCopied', '링크 복사됨!') : t('clinicalCase.docuCopyBtn', '영상 링크 복사')}
            >
              <span>{copySuccess ? t('clinicalCase.docuCopied', '✅ 링크 복사됨!') : t('clinicalCase.docuCopyBtn', '🔗 영상 링크 복사')}</span>
            </button>
          </div>
        </div>

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
                    ? 'bg-[#005a41] text-white border-[#004632] shadow-lg ring-2 ring-emerald-600/40'
                    : 'bg-slate-100/90 border-slate-300/80 hover:bg-slate-200/80 hover:border-slate-400 text-slate-800 shadow-sm'
                }`}
              >
                <div className="flex items-center justify-between mb-1">
                  <span className={`text-[11px] font-extrabold px-2 py-0.5 rounded-full ${isActive ? 'bg-amber-300 text-slate-950' : 'bg-white text-slate-700 border border-slate-200'}`}>
                    STEP 0{idx + 1}
                  </span>
                  <span className={`text-[11px] font-mono ${isActive ? 'text-emerald-200' : 'text-slate-500 font-semibold'}`}>
                    {chart.period}
                  </span>
                </div>
                <h3 className={`text-xs sm:text-base font-bold line-clamp-1 ${isActive ? 'text-white' : 'text-slate-900'}`}>
                  {chart.title}
                </h3>
              </button>
            );
          })}
        </nav>

        {/* 메인 듀얼 스크린 (좌: 수기 차트 원본 / 우: 스마트폰 세로 직캠 영상) */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 sm:gap-8 mb-16 items-stretch">
          
          {/* 좌측: 수기 차트 원본 카드 (5 cols) */}
          <article className="lg:col-span-5 flex flex-col bg-white rounded-3xl p-4 sm:p-6 border border-slate-200/90 shadow-lg text-start">
            <div className="flex items-center justify-between mb-3 sm:mb-4">
              <div className="flex items-center gap-2">
                <span className="w-3 h-3 rounded-full bg-amber-500" aria-hidden="true" />
                <h4 className="text-sm sm:text-base font-bold text-slate-900">
                  {t('clinicalCase.handwrittenTitle', '김동준 원장 자필 차트 원본')}
                </h4>
              </div>
              <button
                onClick={() => setIsChartModalOpen(true)}
                className="min-h-[40px] text-xs font-bold px-3 py-1.5 rounded-xl bg-emerald-50 hover:bg-emerald-600 hover:text-white transition-colors border border-emerald-200 text-emerald-800 flex items-center gap-1.5 shadow-xs focus:outline-none focus-visible:ring-2 focus-visible:ring-emerald-400 cursor-pointer"
                aria-label={t('clinicalCase.zoomBtn', '차트 원본 크게보기')}
              >
                <span>{t('clinicalCase.zoomBtn', '🔍 원본 크게보기')}</span>
              </button>
            </div>

            {/* 차트 썸네일 이미지 (클릭 시 확대) */}
            <figure 
              onClick={() => setIsChartModalOpen(true)}
              className="relative group rounded-2xl overflow-hidden cursor-pointer border border-slate-200 bg-slate-50 flex-1 min-h-[260px] sm:min-h-[300px] flex items-center justify-center p-2 hover:border-emerald-500 transition-all shadow-inner"
            >
              <img
                src={`${import.meta.env.BASE_URL}${currentChart.src}`}
                alt={`${currentChart.title} - 김동준 원장 자필 수기 임상 차트`}
                className="w-full h-auto max-h-[360px] object-contain rounded-xl transition-transform duration-500 group-hover:scale-[1.02]"
              />
              <figcaption className="absolute inset-0 bg-black/30 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center backdrop-blur-xs">
                <span className="px-4 py-2 bg-emerald-600 text-white rounded-xl text-xs font-bold shadow-lg flex items-center gap-1.5">
                  {t('clinicalCase.zoomHover', '🔍 고해상도 자필 글씨 확대보기')}
                </span>
              </figcaption>
            </figure>

            {/* 자필 차트 하이라이트 해설 */}
            <div className="mt-4 pt-4 border-t border-slate-100 space-y-2">
              <span className="text-[11px] font-bold text-amber-700 tracking-wide uppercase block">
                {t('clinicalCase.chartRecord', '📋 자필 차트 주요 기록')}
              </span>
              <ul className="space-y-1.5 text-xs text-slate-600 text-start">
                {currentChart.highlights.map((h, i) => (
                  <li key={i} className="flex items-start gap-2">
                    <span className="text-emerald-600 font-bold shrink-0" aria-hidden="true">✔</span>
                    <span className="leading-snug">{h}</span>
                  </li>
                ))}
              </ul>
            </div>
          </article>

          {/* 우측: 실제 진료실 비디오 플레이어 (스마트폰 세로 9:16 최적화) (7 cols) - 밝고 산뜻한 화이트 테마 */}
          <article className="lg:col-span-7 flex flex-col bg-white rounded-3xl p-4 sm:p-6 border border-slate-200/90 shadow-xl text-start">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-3 sm:mb-4">
              <div className="flex items-center gap-2">
                <span className="w-3 h-3 rounded-full bg-emerald-500 animate-pulse" aria-hidden="true" />
                <h4 className="text-sm sm:text-base font-black text-slate-900">
                  {t('clinicalCase.camTitle', '진료실 무편집 직캠 비디오')}
                </h4>
              </div>
              
              {/* 해당 페이즈에 영상이 여러 개일 때 스위치 탭 */}
              {phaseVideos.length > 1 && (
                <div className="flex items-center gap-1 bg-slate-100 p-1 rounded-xl border border-slate-200 overflow-x-auto">
                  {phaseVideos.map((v) => (
                    <button
                      key={v.id}
                      onClick={() => handleSelectVideo(v)}
                      className={`text-xs px-2.5 py-1.5 rounded-lg font-bold min-h-[36px] transition-all whitespace-nowrap focus:outline-none focus-visible:ring-2 focus-visible:ring-emerald-400 cursor-pointer ${
                        selectedVideo.id === v.id
                          ? 'bg-emerald-600 text-white shadow'
                          : 'text-slate-600 hover:text-slate-900 hover:bg-white/50'
                      }`}
                    >
                      동영상 {v.userOrder} {v.badge.slice(0, 2)}
                    </button>
                  ))}
                </div>
              )}
            </div>

            {/* 비디오 화면 - 스마트폰 세로형 9:16 핏 최적화 & 밝고 깔끔한 라이트 프레임 */}
            <div className="relative rounded-2xl overflow-hidden bg-slate-100 border border-slate-200 p-3 sm:p-5 flex items-center justify-center shadow-inner">
              <div className="w-full max-w-[260px] sm:max-w-[290px] aspect-[9/16] rounded-2xl overflow-hidden bg-black border-2 border-slate-300 shadow-2xl relative">
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
            <div className="mt-4 pt-4 border-t border-slate-100 flex flex-col sm:flex-row sm:items-center justify-between gap-3 text-start">
              <div>
                <div className="flex items-center gap-2 mb-1.5 flex-wrap">
                  <span className="text-[11px] font-extrabold px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-900 font-mono border border-emerald-200">
                    {selectedVideo.stepNum} · {selectedVideo.phase}
                  </span>
                  <span className={`text-[10px] font-bold px-2 py-0.5 rounded-full ${selectedVideo.badgeColor}`}>
                    {selectedVideo.badge}
                  </span>
                  <span className="text-xs text-slate-500 font-mono">
                    {t('clinicalCase.length', '길이')}: {selectedVideo.duration}
                  </span>
                </div>
                <h5 className="text-sm sm:text-base font-bold text-slate-900">{selectedVideo.title}</h5>
                <p className="text-xs text-slate-600 mt-1 leading-relaxed">{selectedVideo.desc}</p>
              </div>

              <button
                onClick={() => openVideoModal(selectedVideo)}
                className="shrink-0 min-h-[42px] text-xs px-3.5 py-2 rounded-xl bg-emerald-50 hover:bg-emerald-600 border border-emerald-200 text-emerald-800 hover:text-white font-bold transition-all flex items-center gap-1.5 self-start sm:self-center focus:outline-none focus-visible:ring-2 focus-visible:ring-emerald-400 active:scale-95 cursor-pointer shadow-xs"
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
              <h3 id="cam-archive-heading" className="text-lg sm:text-2xl font-black text-slate-900">
                {t('clinicalCase.archiveTitle', '📹 사랑동물병원 직캠 8대 영상 전편 아카이브')}
              </h3>
              <p className="text-xs sm:text-sm text-slate-500 mt-1">
                {t('clinicalCase.archiveSubtitle', '스마트폰 세로 직캠으로 촬영된 무편집 진료실 현장 영상입니다. (클릭 시 고화질 재생)')}
              </p>
            </div>
          </div>

          {/* 8개 세로형 숏폼 카드 그리드 (치료 일자 1일차~7일차 순서 엄격 정렬 & STEP 동기화) */}
          <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3 sm:gap-4">
            {CLINICAL_CASE_DATA.videos.map((vid) => {
              const isSelected = selectedVideo.id === vid.id;
              const isCurrentStep = currentChart.id === vid.phaseKey;
              return (
                <div
                  key={vid.id}
                  role="button"
                  tabIndex={0}
                  onKeyDown={(e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); handleSelectVideo(vid); } }}
                  onClick={() => handleSelectVideo(vid)}
                  aria-label={`${vid.stepNum} ${vid.phase} ${vid.title} 영상 선택 및 재생`}
                  className={`group relative rounded-2xl p-2.5 sm:p-3 border transition-all duration-300 cursor-pointer flex flex-col justify-between hover:shadow-xl text-start focus:outline-none focus-visible:ring-2 focus-visible:ring-emerald-400 active:scale-[0.98] ${
                    isSelected
                      ? 'bg-emerald-50/90 border-2 border-emerald-500 ring-2 ring-emerald-400/40 shadow-lg'
                      : isCurrentStep
                      ? 'bg-white border-2 border-emerald-400/80 hover:border-emerald-500 shadow-sm'
                      : 'bg-white border border-slate-200/90 hover:border-slate-300 shadow-xs hover:shadow-md'
                  }`}
                >
                  <div>
                    {/* 상단 STEP 및 치료 순서 번호 헤더 */}
                    <div className="flex items-center justify-between mb-2">
                      <span className={`text-[10px] font-extrabold px-2 py-0.5 rounded-full ${
                        isSelected || isCurrentStep ? 'bg-emerald-600 text-white' : 'bg-slate-100 text-slate-600'
                      }`}>
                        {vid.stepNum} · 동영상 {vid.userOrder}
                      </span>
                      <span className="text-[11px] font-mono text-emerald-700 font-bold">
                        {vid.badge.slice(0, 2)}
                      </span>
                    </div>

                    {/* 세로형 9:16 썸네일 */}
                    <div className="relative aspect-[9/16] rounded-xl overflow-hidden bg-black mb-2.5 border border-slate-200 shadow-xs">
                      <img
                        src={`${import.meta.env.BASE_URL}assets/clinical_thumbs/${vid.thumb}`}
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
                        <div className={`w-7 h-7 sm:w-8 sm:h-8 rounded-full flex items-center justify-center text-xs font-black shadow-lg group-hover:scale-110 transition-transform ${
                          isSelected ? 'bg-amber-400 text-slate-950 ring-2 ring-white' : 'bg-emerald-500 text-slate-950'
                        }`}>
                          {isSelected ? '■' : '▶'}
                        </div>
                      </div>
                    </div>
                    
                    <span className={`inline-block text-[10px] font-bold px-2 py-0.5 rounded-full mb-1.5 ${vid.badgeColor}`}>
                      {vid.badge}
                    </span>
                    <h4 className="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-emerald-700 transition-colors line-clamp-2">
                      {vid.title}
                    </h4>
                  </div>
                  <p className="text-[11px] text-slate-500 mt-2 line-clamp-2 leading-relaxed">
                    {vid.desc}
                  </p>
                </div>
              );
            })}
          </div>
        </section>

        {/* B2B 수의사용 3단계 응급 프로토콜 카드 (옅고 산뜻한 프리미엄 라이트 테마) */}
        <section aria-labelledby="protocol-heading" className="bg-gradient-to-br from-emerald-50/90 via-white to-teal-50/70 p-5 sm:p-10 rounded-3xl border border-emerald-200 shadow-xl relative overflow-hidden text-slate-900">
          <div className="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-4 sm:gap-6 mb-6 sm:mb-8 border-b border-slate-200 pb-6 text-start">
            <div>
              <span className="px-3 py-1 bg-amber-100 text-amber-900 text-xs font-extrabold rounded-full border border-amber-300 inline-block mb-2 shadow-2xs">
                {t('clinicalCase.protocolSub', 'Veterinary Clinical Protocol')}
              </span>
              <h3 id="protocol-heading" className="text-lg sm:text-2xl lg:text-3xl font-black text-slate-900 break-keep">
                {CLINICAL_CASE_DATA.protocol.title}
              </h3>
              <p className="text-xs sm:text-sm text-emerald-800 font-semibold mt-1">
                적용 대상: {CLINICAL_CASE_DATA.protocol.target}
              </p>
            </div>

            <a
              href="#audio-testimonial"
              className="min-h-[44px] px-4 sm:px-5 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs sm:text-sm transition-colors shrink-0 shadow-md flex items-center gap-2 border border-emerald-500 focus:outline-none focus-visible:ring-2 focus-visible:ring-emerald-400 active:scale-95"
            >
              <span>{t('clinicalCase.listenCall', '🎙️ 김동준 원장 통화 육성 인터뷰 듣기')}</span>
              <span className="rtl:rotate-180" aria-hidden="true">↓</span>
            </a>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 sm:gap-6 text-start">
            {CLINICAL_CASE_DATA.protocol.steps.map((s, idx) => (
              <div key={idx} className="bg-white p-4 sm:p-5 rounded-2xl border border-slate-200/90 shadow-sm hover:shadow-md transition-shadow flex flex-col justify-between">
                <div>
                  <div className="w-8 h-8 rounded-xl bg-emerald-100 border border-emerald-300 text-emerald-800 flex items-center justify-center font-black text-sm mb-3">
                    0{idx + 1}
                  </div>
                  <h4 className="text-sm sm:text-base font-black text-slate-900 mb-1">{s.step}</h4>
                  <div className="text-xs font-bold text-emerald-700 mb-2">{s.product} ({s.dosage})</div>
                  <p className="text-xs text-slate-600 leading-relaxed">{s.detail}</p>
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
            className="relative max-w-4xl w-full max-h-[90dvh] bg-[#002b1e] rounded-3xl p-4 sm:p-6 border border-emerald-500/40 flex flex-col shadow-2xl"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="flex items-center justify-between mb-3 border-b border-white/10 pb-3 text-start">
              <div>
                <h4 className="kr-title-2line text-sm sm:text-lg font-bold text-white" style={{WebkitLineClamp: 2}}>{currentChart.title}</h4>
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
            <div className="flex-1 overflow-auto flex items-center justify-center p-2 bg-black/40 rounded-2xl border border-white/5">
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
            className="relative max-w-sm sm:max-w-md w-full bg-[#002b1e] rounded-3xl p-4 sm:p-5 border border-emerald-500/40 flex flex-col shadow-2xl max-h-[92dvh] overflow-y-auto"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="flex items-center justify-between mb-3 border-b border-white/10 pb-3 text-start">
              <div className="pe-2 flex-1">
                <div className="kr-hanging-title">
                  <span className={`kr-icon text-[10px] font-bold px-2 py-0.5 rounded-full ${modalVideo.badgeColor}`}>
                    {modalVideo.badge}
                  </span>
                  <h4 className="kr-text text-sm sm:text-base font-bold text-white leading-snug">{modalVideo.title}</h4>
                </div>
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

      {/* 2분 54초 리얼 다큐멘터리 전편 전체화면 모달 (모바일 최적화 & 장애인 전체 자막/대본 포함) */}
      {isDocuModalOpen && (
        <div 
          role="dialog"
          aria-modal="true"
          aria-label={t('clinicalCase.docuModalTitle', '55일령 발작 환축의 7일간의 기적 다큐멘터리')}
          className="fixed inset-0 z-50 bg-black/95 backdrop-blur-md flex items-center justify-center p-2.5 sm:p-4"
          onClick={() => setIsDocuModalOpen(false)}
        >
          <div 
            className="relative max-w-sm sm:max-w-md w-[94vw] sm:w-full bg-[#002b1e] rounded-3xl p-3.5 sm:p-5 border border-emerald-500/40 flex flex-col shadow-2xl max-h-[92dvh] overflow-y-auto"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="flex items-center justify-between mb-2.5 sm:mb-3 border-b border-white/10 pb-2.5 sm:pb-3 text-start">
              <div className="pe-2 flex-1">
                <div className="kr-hanging-title">
                  <span className="kr-icon text-[10px] font-black px-2.5 py-0.5 rounded-full bg-yellow-400 text-slate-950">
                    🎬 2분 54초
                  </span>
                  <h4 className="kr-text text-xs sm:text-base font-bold text-white leading-snug">
                    {t('clinicalCase.docuModalTitle', '55일령 발작 환축의 7일간의 기적')}
                  </h4>
                </div>
              </div>
              <button
                onClick={() => setIsDocuModalOpen(false)}
                className="w-10 h-10 min-w-[40px] min-h-[40px] rounded-full bg-white/10 hover:bg-white/20 text-white flex items-center justify-center font-bold text-base shrink-0 focus:outline-none focus-visible:ring-2 focus-visible:ring-emerald-400 cursor-pointer"
                aria-label={t('common.close', '닫기')}
              >
                ✕
              </button>
            </div>
            
            {/* 스마트폰 9:16 세로 핏 비디오 컨테이너 */}
            <div className="w-full max-w-[270px] sm:max-w-[310px] max-h-[48vh] sm:max-h-[54vh] mx-auto aspect-[9/16] bg-black rounded-2xl overflow-hidden shadow-2xl border border-emerald-500/30 flex items-center justify-center relative">
              <video
                key="docu-video-v2"
                controls
                autoPlay
                playsInline
                aria-label={t('clinicalCase.docuModalTitle', '김동준 원장 55일령 발작 환축 7일간의 기적 다큐멘터리')}
                className="w-full h-full object-cover"
              >
                <source src={docuVideoUrl} type="video/mp4" />
                브라우저가 비디오를 지원하지 않습니다.
              </video>
            </div>

            {/* 장애인 접근성: 전체 대본/자막 전문 보기 아코디언 */}
            <div className="mt-3">
              <button
                type="button"
                onClick={() => setIsTranscriptOpen(!isTranscriptOpen)}
                className="w-full py-2 px-3 bg-white/5 hover:bg-white/10 text-emerald-300 text-xs font-bold rounded-xl border border-emerald-500/20 transition-all flex items-center justify-between cursor-pointer focus:outline-none focus-visible:ring-2 focus-visible:ring-emerald-400"
                aria-expanded={isTranscriptOpen}
              >
                <span className="flex items-center gap-1.5">
                  <span aria-hidden="true">📄</span>
                  <span>{t('clinicalCase.docuTranscriptBtn', '다큐멘터리 전체 자막/대본 전문 보기')}</span>
                </span>
                <span className="text-[11px] text-slate-400 font-mono">
                  {isTranscriptOpen ? t('clinicalCase.docuTranscriptHide', '▲ 닫기') : t('clinicalCase.docuTranscriptShow', '▼ 전문 펼치기')}
                </span>
              </button>

              {isTranscriptOpen && (
                <div 
                  tabIndex={0} 
                  role="region" 
                  aria-label="다큐멘터리 전체 대본 텍스트"
                  className="mt-2 p-3 bg-[#001d14] rounded-xl border border-emerald-500/20 text-[11px] sm:text-xs text-slate-300 space-y-2 max-h-40 overflow-y-auto leading-relaxed focus:outline-none focus:ring-1 focus:ring-emerald-400"
                >
                  <p className="border-b border-white/10 pb-1 text-emerald-400 font-bold">
                    [프롤로그 0:00~0:12] 하남 사랑동물병원 김동준 원장의 실제 임상 치료 일지. 생후 55일 된 환축의 7일간의 기적 같은 회복 다큐멘터리입니다.
                  </p>
                  <p className="border-b border-white/10 pb-1">
                    <strong className="text-rose-300">[STEP 1 응급 내원 0:12~0:26]</strong> 2026년 7월 28일 저녁, 어린 토이푸들이 스스로 서지 못하고 온몸을 떨며 응급 내원했습니다. 안락사까지 거론되던 위급한 순간이었습니다.
                  </p>
                  <p className="border-b border-white/10 pb-1">
                    <strong className="text-amber-300">[STEP 1 초진 진단 0:26~0:50]</strong> 파보와 코로나 키트 검사는 음성. 김동준 원장은 원인불명의 급성 장독소증으로 인한 소화기 허탈과 신경 발작으로 진단했습니다.
                  </p>
                  <p className="border-b border-white/10 pb-1">
                    <strong className="text-emerald-300">[STEP 1 긴급 투약 0:50~1:06]</strong> 내원 즉시 몬스멕타 1차 펌프를 긴급 투약했습니다. 초미세 몬모릴로나이트가 장내 독소를 즉시 흡착 배출하며 치료가 시작됩니다.
                  </p>
                  <p className="border-b border-white/10 pb-1">
                    <strong className="text-emerald-300">[자필 차트 기록 1:06~1:16]</strong> 투약 몇 시간 만에 심한 경련이 진정되었고, 다음 날 새벽에는 종합백신 접종이 가능할 정도로 활력이 급호전되었습니다.
                  </p>
                  <p className="border-b border-white/10 pb-1">
                    <strong className="text-cyan-300">[STEP 2 반사 회복 1:16~1:40]</strong> 입원 3일 차. 환축은 네 발로 꼿꼿이 일어서며, 비틀거리던 사지 반사와 보행 능력을 완전히 회복했습니다.
                  </p>
                  <p className="border-b border-white/10 pb-1">
                    <strong className="text-cyan-300">[STEP 2 의식 회복 1:40~2:08]</strong> 입원장 안에서 안정을 취하며 장 점막을 회복 중인 환축. 흐려졌던 눈빛은 생기를 되찾고 고개를 꼿꼿이 들어 정면을 응시합니다.
                  </p>
                  <p className="border-b border-white/10 pb-1">
                    <strong className="text-yellow-300">[STEP 2 식욕 폭발 2:08~2:20]</strong> 식욕을 완전히 잃었던 환축이 밥그릇에 머리를 묻고 캔사료를 폭풍 흡입합니다! 장 기능이 완벽히 정상 궤도에 올랐음을 보여줍니다.
                  </p>
                  <p className="border-b border-white/10 pb-1">
                    <strong className="text-emerald-300">[STEP 3 완치 퇴원 2:20~2:43]</strong> 입원 7일 차. 몬스멕타와 헤파맥스를 복합 처방하여 간 해독을 보강한 후, 환축은 기적처럼 건강을 회복하고 최종 완치 퇴원했습니다.
                  </p>
                  <p>
                    <strong className="text-slate-400">[에필로그 2:43~2:54]</strong> 원인불명 급성 소화기 허탈의 1차 해답. 수의사 원장님들의 임상 현장을 지키는 동물병원 전용 처방 솔루션, 몬스멕타입니다.
                  </p>
                </div>
              )}
            </div>

            {/* 원클릭 모바일 공유 & 다운로드 버튼군 */}
            <div className="mt-3 pt-2.5 border-t border-white/10 flex flex-col sm:flex-row items-stretch sm:items-center gap-2">
              <button
                onClick={handleCopyDocuLink}
                className="flex-1 py-2.5 px-3 bg-[#00513b] hover:bg-[#003d2b] text-white text-xs font-bold rounded-xl transition-colors flex items-center justify-center gap-1.5 cursor-pointer shadow-lg shadow-emerald-950/60"
              >
                <span>{copySuccess ? t('clinicalCase.docuCopied', '✅ 영상 링크 복사완료!') : t('clinicalCase.docuCopyBtnMobile', '🔗 카톡/모바일 공유 링크 복사')}</span>
              </button>
              <a
                href={docuVideoUrl}
                download="김동준원장_55일령발작환축_7일임상다큐_v2.mp4"
                className="px-4 py-2.5 bg-white/10 hover:bg-white/20 text-white text-xs font-bold rounded-xl transition-colors flex items-center justify-center gap-1 shrink-0 text-center"
              >
                <span>{t('clinicalCase.docuDownload', '📥 MP4 다운로드')}</span>
              </a>
            </div>
          </div>
        </div>
      )}

    </section>
  );
}
