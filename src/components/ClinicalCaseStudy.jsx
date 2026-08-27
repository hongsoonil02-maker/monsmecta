import { useState, useRef } from 'react';
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

  return (
    <section id="clinical-case-study" className="py-20 bg-gradient-to-b from-slate-900 via-slate-950 to-slate-900 text-white relative overflow-hidden border-t border-b border-emerald-500/20">
      {/* 배경 장식 글로우 */}
      <div className="absolute top-1/4 left-1/2 -translate-x-1/2 w-[800px] h-[400px] bg-emerald-500/10 blur-[140px] pointer-events-none rounded-full" />
      <div className="absolute bottom-10 right-10 w-96 h-96 bg-amber-500/10 blur-[120px] pointer-events-none rounded-full" />

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        
        {/* 헤더 섹션 */}
        <div className="text-center max-w-3xl mx-auto mb-14">
          <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-emerald-950/80 border border-emerald-400/40 text-emerald-300 text-xs sm:text-sm font-black mb-4 shadow-lg shadow-emerald-950/50">
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-ping" />
            🎙️ 몬스멕타 자문위원 리얼 임상 다큐멘터리
          </div>
          <h2 className="text-2xl sm:text-4xl lg:text-5xl font-black text-white tracking-tight leading-tight mb-4">
            55일령 발작 환축의 <span className="text-transparent bg-clip-text bg-gradient-to-r from-emerald-300 via-emerald-400 to-amber-300">7일간의 기적</span>
          </h2>
          <p className="text-sm sm:text-base text-slate-300 font-medium break-keep">
            하남 사랑동물병원 <strong className="text-emerald-400">김동준 원장님</strong>이 환축의 생사를 다투며 직접 작성한 <strong className="text-white">자필 수기 차트</strong>와 <strong className="text-white">진료실 무편집 직캠 동영상 8편</strong>의 기록입니다.
          </p>

          {/* 환축 초진 스펙 바 */}
          <div className="mt-8 grid grid-cols-2 sm:grid-cols-4 gap-3 bg-white/5 p-4 rounded-2xl border border-white/10 backdrop-blur-md text-left">
            <div className="border-r border-white/10 pr-2">
              <span className="text-[11px] font-bold text-slate-400 block">환축 정보</span>
              <span className="text-xs sm:text-sm font-bold text-white">토이푸들 ♂ (55일령)</span>
            </div>
            <div className="border-r border-white/10 pr-2">
              <span className="text-[11px] font-bold text-slate-400 block">내원시 증상</span>
              <span className="text-xs sm:text-sm font-bold text-rose-400">심한 발작·식욕전폐</span>
            </div>
            <div className="border-r border-white/10 pr-2">
              <span className="text-[11px] font-bold text-slate-400 block">5종 키트 검사</span>
              <span className="text-xs sm:text-sm font-bold text-emerald-400">파보·코로나 음성(Neg)</span>
            </div>
            <div>
              <span className="text-[11px] font-bold text-slate-400 block">최종 예후</span>
              <span className="text-xs sm:text-sm font-bold text-amber-300">7일 만에 완치 [퇴원]</span>
            </div>
          </div>
        </div>

        {/* 3단계 타임라인 스텝퍼 탭 */}
        <div className="flex flex-col sm:flex-row gap-3 max-w-4xl mx-auto mb-10">
          {CLINICAL_CASE_DATA.charts.map((chart, idx) => {
            const isActive = idx === activePhaseIndex;
            return (
              <button
                key={chart.id}
                onClick={() => handleSelectPhase(idx)}
                className={`flex-1 text-left p-4 rounded-2xl border transition-all duration-300 relative overflow-hidden ${
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
                <h4 className={`text-sm sm:text-base font-bold line-clamp-1 ${isActive ? 'text-white' : 'text-slate-300'}`}>
                  {chart.title}
                </h4>
              </button>
            );
          })}
        </div>

        {/* 메인 듀얼 스크린 (좌: 수기 차트 원본 / 우: 실제 직캠 영상) */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 mb-16 items-stretch">
          
          {/* 좌측: 수기 차트 원본 카드 (5 cols) */}
          <div className="lg:col-span-5 flex flex-col bg-slate-900/90 rounded-3xl p-5 sm:p-6 border border-white/10 shadow-2xl backdrop-blur-xl">
            <div className="flex items-center justify-between mb-4">
              <div className="flex items-center gap-2">
                <span className="w-3 h-3 rounded-full bg-amber-400" />
                <h4 className="text-base font-bold text-white">김동준 원장 자필 차트 원본</h4>
              </div>
              <button
                onClick={() => setIsChartModalOpen(true)}
                className="text-xs font-bold px-3 py-1.5 rounded-xl bg-white/10 hover:bg-emerald-600 hover:text-white transition-colors border border-white/10 text-emerald-300 flex items-center gap-1.5 shadow"
              >
                <span>🔍 원본 크게보기</span>
              </button>
            </div>

            {/* 차트 썸네일 이미지 (클릭 시 확대) */}
            <div 
              onClick={() => setIsChartModalOpen(true)}
              className="relative group rounded-2xl overflow-hidden cursor-pointer border border-white/15 bg-white/5 flex-1 min-h-[300px] flex items-center justify-center p-2 hover:border-emerald-400 transition-all shadow-inner"
            >
              <img
                src={`${import.meta.env.BASE_URL}${currentChart.src}`}
                alt={currentChart.title}
                className="w-full h-auto max-h-[360px] object-contain rounded-xl transition-transform duration-500 group-hover:scale-[1.02]"
              />
              <div className="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center backdrop-blur-xs">
                <span className="px-4 py-2 bg-emerald-600/90 text-white rounded-xl text-xs font-bold shadow-lg flex items-center gap-1.5">
                  🔍 고해상도 자필 글씨 확대보기
                </span>
              </div>
            </div>

            {/* 자필 차트 하이라이트 해설 */}
            <div className="mt-4 pt-4 border-t border-white/10 space-y-2">
              <span className="text-[11px] font-bold text-amber-300 tracking-wide uppercase block">
                📋 자필 차트 주요 기록
              </span>
              <ul className="space-y-1.5 text-xs text-slate-300">
                {currentChart.highlights.map((h, i) => (
                  <li key={i} className="flex items-start gap-2">
                    <span className="text-emerald-400 font-bold shrink-0">✔</span>
                    <span className="leading-snug">{h}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>

          {/* 우측: 실제 진료실 비디오 플레이어 (7 cols) */}
          <div className="lg:col-span-7 flex flex-col bg-slate-900/90 rounded-3xl p-5 sm:p-6 border border-white/10 shadow-2xl backdrop-blur-xl">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-4">
              <div className="flex items-center gap-2">
                <span className="w-3 h-3 rounded-full bg-emerald-400 animate-pulse" />
                <h4 className="text-base font-bold text-white">진료실 무편집 직캠 비디오</h4>
              </div>
              
              {/* 해당 페이즈에 영상이 여러 개일 때 스위치 탭 */}
              {phaseVideos.length > 1 && (
                <div className="flex items-center gap-1.5 bg-black/40 p-1 rounded-xl border border-white/10">
                  {phaseVideos.map((v) => (
                    <button
                      key={v.id}
                      onClick={() => handleSelectVideo(v)}
                      className={`text-xs px-2.5 py-1 rounded-lg font-bold transition-all ${
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

            {/* 비디오 화면 */}
            <div className="relative rounded-2xl overflow-hidden bg-black border border-white/10 flex items-center justify-center min-h-[340px] max-h-[460px]">
              <video
                ref={videoRef}
                key={selectedVideo.file}
                controls
                playsInline
                preload="metadata"
                className="w-full h-full max-h-[440px] object-contain"
              >
                <source src={`${import.meta.env.BASE_URL}assets/${selectedVideo.file}`} type="video/mp4" />
                귀하의 브라우저는 비디오 태그를 지원하지 않습니다.
              </video>
            </div>

            {/* 비디오 설명 카드 */}
            <div className="mt-4 pt-4 border-t border-white/10 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
              <div>
                <div className="flex items-center gap-2 mb-1">
                  <span className={`text-[10px] font-bold px-2 py-0.5 rounded-full ${selectedVideo.badgeColor}`}>
                    {selectedVideo.badge}
                  </span>
                  <span className="text-xs text-slate-400 font-mono">길이: {selectedVideo.duration}</span>
                </div>
                <h5 className="text-sm sm:text-base font-bold text-white">{selectedVideo.title}</h5>
                <p className="text-xs text-slate-300 mt-1 leading-relaxed">{selectedVideo.desc}</p>
              </div>

              <button
                onClick={() => openVideoModal(selectedVideo)}
                className="shrink-0 text-xs px-3.5 py-2 rounded-xl bg-emerald-600/20 hover:bg-emerald-600 border border-emerald-500/40 text-emerald-300 hover:text-white font-bold transition-all flex items-center gap-1.5 self-start sm:self-center"
              >
                <span>⛶ 큰 화면 재생</span>
              </button>
            </div>
          </div>
        </div>

        {/* 8대 직캠 숏폼 비디오 전체 갤러리 */}
        <div className="mt-12 mb-16">
          <div className="flex items-center justify-between mb-6">
            <div>
              <h3 className="text-xl sm:text-2xl font-extrabold text-white">
                📹 사랑동물병원 직캠 8대 영상 전편 아카이브
              </h3>
              <p className="text-xs sm:text-sm text-slate-400 mt-1">
                내원 당시 발작 순간부터 한 손 펌핑 투약, 폭풍 식욕 회복, 완치 퇴원까지 날것 그대로의 영상입니다.
              </p>
            </div>
          </div>

          {/* 8개 카드 그리드 */}
          <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4">
            {CLINICAL_CASE_DATA.videos.map((vid, idx) => (
              <div
                key={vid.id}
                onClick={() => openVideoModal(vid)}
                className="group relative bg-slate-900/80 rounded-2xl p-3 border border-white/10 hover:border-emerald-400/80 transition-all duration-300 cursor-pointer flex flex-col justify-between hover:shadow-xl hover:shadow-emerald-950/40"
              >
                <div>
                  <div className="relative aspect-video rounded-xl overflow-hidden bg-black mb-3 border border-white/5">
                    <img
                      src={`${import.meta.env.BASE_URL}assets/clinical_thumbs/thumb_${idx + 1}_${vid.file.slice(0, 20)}.jpg`}
                      alt={vid.title}
                      className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
                      onError={(e) => {
                        // fallback to simple placeholder if thumb fails
                        e.target.style.display = 'none';
                      }}
                    />
                    <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent flex items-end justify-between p-2">
                      <span className="text-[10px] font-bold px-1.5 py-0.5 rounded bg-black/60 text-white font-mono">
                        {vid.duration}
                      </span>
                      <div className="w-7 h-7 rounded-full bg-emerald-500 text-slate-950 flex items-center justify-center text-xs font-black shadow group-hover:scale-110 transition-transform">
                        ▶
                      </div>
                    </div>
                  </div>
                  <span className={`inline-block text-[10px] font-bold px-2 py-0.5 rounded-full mb-1.5 ${vid.badgeColor}`}>
                    {vid.phase} · {vid.badge.split(' ')[1] || '임상영상'}
                  </span>
                  <h6 className="text-xs sm:text-sm font-bold text-white group-hover:text-emerald-300 transition-colors line-clamp-2">
                    {vid.title}
                  </h6>
                </div>
                <p className="text-[11px] text-slate-400 mt-2 line-clamp-2 leading-relaxed">
                  {vid.desc}
                </p>
              </div>
            ))}
          </div>
        </div>

        {/* B2B 수의사용 3단계 응급 프로토콜 카드 */}
        <div className="bg-gradient-to-br from-emerald-950/90 via-slate-900 to-slate-950 p-6 sm:p-10 rounded-3xl border border-emerald-500/30 shadow-2xl relative overflow-hidden">
          <div className="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-6 mb-8 border-b border-white/10 pb-6">
            <div>
              <span className="px-3 py-1 bg-amber-400/20 text-amber-300 text-xs font-extrabold rounded-full border border-amber-400/30 inline-block mb-2">
                Veterinary Clinical Protocol
              </span>
              <h3 className="text-xl sm:text-2xl lg:text-3xl font-black text-white">
                {CLINICAL_CASE_DATA.protocol.title}
              </h3>
              <p className="text-xs sm:text-sm text-emerald-300/90 mt-1">
                적용 대상: {CLINICAL_CASE_DATA.protocol.target}
              </p>
            </div>

            <a
              href="#audio-testimonial"
              className="px-5 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs sm:text-sm transition-colors shrink-0 shadow-lg flex items-center gap-2 border border-emerald-400/40"
            >
              <span>🎙️ 김동준 원장 통화 육성 인터뷰 듣기</span>
              <span>↓</span>
            </a>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {CLINICAL_CASE_DATA.protocol.steps.map((s, idx) => (
              <div key={idx} className="bg-white/5 p-5 rounded-2xl border border-white/10 flex flex-col justify-between">
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
        </div>

      </div>

      {/* 수기 차트 전체화면 돋보기 라이트박스 모달 */}
      {isChartModalOpen && (
        <div 
          className="fixed inset-0 z-50 bg-black/90 backdrop-blur-md flex items-center justify-center p-4"
          onClick={() => setIsChartModalOpen(false)}
        >
          <div 
            className="relative max-w-4xl w-full max-h-[90vh] bg-slate-900 rounded-3xl p-4 sm:p-6 border border-white/20 flex flex-col shadow-2xl"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="flex items-center justify-between mb-3 border-b border-white/10 pb-3">
              <div>
                <h4 className="text-base sm:text-lg font-bold text-white">{currentChart.title}</h4>
                <p className="text-xs text-emerald-300">{currentChart.period} · 하남 사랑동물병원 김동준 원장 자필 차트</p>
              </div>
              <button
                onClick={() => setIsChartModalOpen(false)}
                className="w-9 h-9 rounded-full bg-white/10 hover:bg-white/20 text-white flex items-center justify-center font-bold text-lg"
              >
                ✕
              </button>
            </div>
            <div className="flex-1 overflow-auto flex items-center justify-center p-2 bg-slate-950/60 rounded-2xl border border-white/5">
              <img
                src={`${import.meta.env.BASE_URL}${currentChart.src}`}
                alt={currentChart.title}
                className="max-w-full max-h-[75vh] object-contain rounded-xl shadow-2xl"
              />
            </div>
          </div>
        </div>
      )}

      {/* 비디오 큰 화면 팝업 모달 */}
      {isVideoModalOpen && modalVideo && (
        <div 
          className="fixed inset-0 z-50 bg-black/95 backdrop-blur-lg flex items-center justify-center p-4"
          onClick={() => setIsVideoModalOpen(false)}
        >
          <div 
            className="relative max-w-2xl w-full bg-slate-900 rounded-3xl p-5 border border-white/20 flex flex-col shadow-2xl"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="flex items-center justify-between mb-3 border-b border-white/10 pb-3">
              <div>
                <span className={`text-[10px] font-bold px-2 py-0.5 rounded-full ${modalVideo.badgeColor} mr-2`}>
                  {modalVideo.badge}
                </span>
                <h4 className="text-base font-bold text-white inline-block">{modalVideo.title}</h4>
              </div>
              <button
                onClick={() => setIsVideoModalOpen(false)}
                className="w-9 h-9 rounded-full bg-white/10 hover:bg-white/20 text-white flex items-center justify-center font-bold text-lg"
              >
                ✕
              </button>
            </div>
            
            <div className="aspect-video bg-black rounded-2xl overflow-hidden flex items-center justify-center">
              <video
                controls
                autoPlay
                playsInline
                className="w-full h-full object-contain"
              >
                <source src={`${import.meta.env.BASE_URL}assets/${modalVideo.file}`} type="video/mp4" />
                브라우저가 비디오를 지원하지 않습니다.
              </video>
            </div>
            
            <p className="text-xs sm:text-sm text-slate-300 mt-4 leading-relaxed bg-white/5 p-3 rounded-xl border border-white/5">
              {modalVideo.desc}
            </p>
          </div>
        </div>
      )}

    </section>
  );
}
