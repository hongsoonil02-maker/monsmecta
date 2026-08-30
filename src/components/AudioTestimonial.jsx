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
      className="bg-white text-slate-900 rounded-3xl p-6 sm:p-8 md:p-10 my-12 max-w-7xl mx-4 sm:mx-6 lg:mx-auto border border-slate-200/90 shadow-xl"
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
        </div>
      </div>
    </section>
  );
}
