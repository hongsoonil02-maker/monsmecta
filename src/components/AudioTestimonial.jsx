import { useRef, useState, useEffect } from 'react';
import { useTranslation } from 'react-i18next';

function formatTime(seconds) {
  if (!Number.isFinite(seconds)) return '0:00';
  const m = Math.floor(seconds / 60);
  const s = Math.floor(seconds % 60);
  return `${m}:${String(s).padStart(2, '0')}`;
}

export default function AudioTestimonial() {
  const { t } = useTranslation();
  const audioRef = useRef(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [progress, setProgress] = useState(0);
  const [currentTime, setCurrentTime] = useState(0);
  const [duration, setDuration] = useState(0);
  const [showTranscript, setShowTranscript] = useState(false);

  useEffect(() => {
    const audio = audioRef.current;
    if (!audio) return undefined;

    const onTimeUpdate = () => {
      setCurrentTime(audio.currentTime);
      if (audio.duration) setProgress(audio.currentTime / audio.duration);
    };
    const onLoadedMetadata = () => setDuration(audio.duration);
    const onPlay = () => setIsPlaying(true);
    const onPause = () => setIsPlaying(false);
    const onEnded = () => {
      setIsPlaying(false);
      setProgress(0);
      setCurrentTime(0);
    };

    audio.addEventListener('timeupdate', onTimeUpdate);
    audio.addEventListener('loadedmetadata', onLoadedMetadata);
    audio.addEventListener('play', onPlay);
    audio.addEventListener('pause', onPause);
    audio.addEventListener('ended', onEnded);
    return () => {
      audio.removeEventListener('timeupdate', onTimeUpdate);
      audio.removeEventListener('loadedmetadata', onLoadedMetadata);
      audio.removeEventListener('play', onPlay);
      audio.removeEventListener('pause', onPause);
      audio.removeEventListener('ended', onEnded);
    };
  }, []);

  const togglePlay = () => {
    const audio = audioRef.current;
    if (!audio) return;
    if (audio.paused) audio.play().catch(() => {});
    else audio.pause();
  };

  const seek = (e) => {
    const audio = audioRef.current;
    if (!audio || !audio.duration) return;
    const rect = e.currentTarget.getBoundingClientRect();
    const ratio = Math.min(Math.max((e.clientX - rect.left) / rect.width, 0), 1);
    audio.currentTime = ratio * audio.duration;
    setProgress(ratio);
  };

  return (
    <section
      id="audio-testimonial"
      aria-label={t('audioTestimonial.title', '"구토·복통·설사 환축 몬스멕타 즉시 투여 반응"')}
      className="bg-white text-slate-900 rounded-3xl p-6 sm:p-8 md:p-10 my-[28px] max-w-7xl mx-4 sm:mx-6 lg:mx-auto border border-slate-200/90 shadow-xl"
    >
      <audio ref={audioRef} src={`${import.meta.env.BASE_URL}assets/kimdongjun-call.m4a`} preload="metadata" />
      <div className="flex flex-col md:flex-row items-center justify-between gap-6">
        <div className="space-y-2 text-center md:text-left">
          <div className="flex flex-wrap items-center gap-2 justify-center md:justify-start">
            <span className="px-3 py-1 bg-amber-50 text-amber-800 text-xs font-bold rounded-full border border-amber-200">
              {t('audioTestimonial.tag', '🎙️ 현장 수의사 임상 녹음 인터뷰')}
            </span>
            <a
              href="#clinical-case-study"
              className="px-3 py-1 bg-emerald-50 hover:bg-emerald-100 text-emerald-800 text-xs font-bold rounded-full border border-emerald-200 transition-colors flex items-center gap-1"
            >
              <span>📋 55일령 발작 푸들 자필 차트·직캠 보기</span>
              <span>↑</span>
            </a>
          </div>
          <h4 className="text-xl sm:text-2xl font-black text-slate-900 break-keep">
            {t('audioTestimonial.title', '"구토·복통·설사 환축 몬스멕타 즉시 투여 반응"')}
          </h4>
          <p className="text-xs sm:text-sm text-slate-500 break-keep font-medium">
            {t('audioTestimonial.sub', '사랑동물병원 김동준 원장님 현장 반응 통화 녹음')}
          </p>
        </div>

        <div
          aria-live="polite"
          className="bg-slate-50 p-4 sm:p-5 rounded-2xl border border-slate-200 w-full md:w-84 flex flex-col items-center gap-3 shadow-inner"
        >
          <div className="flex items-center gap-3 w-full">
            <button
              onClick={togglePlay}
              aria-label={isPlaying ? 'Pause audio interview' : 'Play audio interview'}
              className="w-12 h-12 bg-emerald-600 hover:bg-emerald-700 text-white rounded-full flex items-center justify-center font-bold text-xl shadow-md transition-transform active:scale-95 shrink-0 focus:outline-none focus:ring-2 focus:ring-emerald-400"
            >
              {isPlaying ? '⏸' : '▶'}
            </button>
            <div className="flex-1 min-w-0">
              <div className="text-xs font-extrabold text-slate-900 truncate">
                {t('audioTestimonial.docName', '김동준 원장 (사랑동물병원)')}
              </div>
              <div className="text-[10px] text-slate-500 font-medium">
                {t('audioTestimonial.docSub', '몬스멕타 현장 반응 통화 녹음')}
              </div>
              <div
                role="slider"
                aria-label="Audio progress"
                aria-valuemin={0}
                aria-valuemax={100}
                aria-valuenow={Math.round(progress * 100)}
                tabIndex={0}
                onClick={seek}
                onKeyDown={(e) => {
                  if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') {
                    const audio = audioRef.current;
                    if (audio && audio.duration) {
                      const step = 5;
                      audio.currentTime += e.key === 'ArrowRight' ? step : -step;
                    }
                  }
                }}
                className="w-full bg-slate-200 h-1.5 rounded-full mt-1.5 overflow-hidden cursor-pointer"
              >
                <div className="h-full bg-emerald-500" style={{ width: `${progress * 100}%` }} />
              </div>
              <div className="flex justify-between text-[10px] text-slate-400 mt-1 font-mono font-medium">
                <span>{formatTime(currentTime)}</span>
                <span>{formatTime(duration)}</span>
              </div>
            </div>
          </div>
          <p className="text-[11px] text-slate-600 italic break-keep leading-relaxed text-center">
            {t('audioTestimonial.quote', '"단순 설사 치료를 넘어 구토·복통 환축도 잘 받아먹는 압도적 기호성과 즉각적 복통 완화로, 소화기 트러블 전체의 1차 상비·처방 보조제로 필수적입니다."')}
          </p>

          {/* 청각 장애인 및 음성 청취 불가 환경을 위한 텍스트 대본 (Transcript) 토글 */}
          <div className="w-full pt-2 border-t border-slate-200/80">
            <button
              onClick={() => setShowTranscript(!showTranscript)}
              className="text-xs font-bold text-emerald-700 hover:text-emerald-800 flex items-center justify-center gap-1.5 w-full py-1 rounded hover:bg-emerald-50 transition-colors cursor-pointer"
              aria-expanded={showTranscript}
              aria-controls="audio-transcript-content"
            >
              <span>{showTranscript ? '▲' : '▼'}</span>
              <span>{showTranscript ? t('audioTestimonial.hideTranscript', '녹취록 대본 닫기') : t('audioTestimonial.showTranscript', '📜 청각 보조 텍스트 녹취록 보기')}</span>
            </button>
            {showTranscript && (
              <div
                id="audio-transcript-content"
                className="mt-2.5 p-3 bg-white rounded-xl border border-slate-200 text-xs text-slate-700 leading-relaxed max-h-48 overflow-y-auto space-y-2 animate-in fade-in"
              >
                <div className="font-bold text-[#00513b] text-[11px] border-b border-slate-100 pb-1 flex items-center justify-between">
                  <span>[통화 녹음 전사본 - 김동준 원장]</span>
                  <span className="text-[10px] text-slate-400">2026.06.18</span>
                </div>
                <p>
                  "저희 병원에 내원한 강아지가 심한 구토와 물설사로 거의 탈진 상태였는데, 기존 지사제는 먹이기가 너무 힘들었습니다. 그런데 몬스멕타는 시럽 형태에 기호성이 워낙 뛰어나서 주사기 피딩 시 저항 없이 아주 잘 받아먹더군요."
                </p>
                <p>
                  "1차 투여 후 약 1~2시간 만에 복부 팽만과 통증 호소가 눈에 띄게 줄어들었고, 이튿날 아침 정상 고형변을 보기 시작했습니다. 수액 요법과 병용 시 위장관 점막을 보호해주는 1차 상비약으로 원내 모든 수의사에게 적극 권장할 만합니다."
                </p>
              </div>
            )}
          </div>
        </div>
      </div>
    </section>
  );
}
