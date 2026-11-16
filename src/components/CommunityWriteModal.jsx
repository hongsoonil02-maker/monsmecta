import { useState } from 'react';

const FECAL_SCORES = [
  { score: 1, label: '1단계: 완전한 물설사 (수양성)' },
  { score: 2, label: '2단계: 형태 없는 진흙/점액변' },
  { score: 3, label: '3단계: 무르고 집기 어려운 변' },
  { score: 4, label: '4단계: 형태는 있으나 약간 무른 변' },
  { score: 5, label: '5단계: 촉촉하고 이상적인 바나나변 (정상)' },
  { score: 6, label: '6단계: 다소 건조하고 단단한 변' },
  { score: 7, label: '7단계: 매우 마르고 딱딱한 변' },
];

const CommunityWriteModal = ({ isOpen, onClose, onAddPost, initialType = 'review' }) => {
  const [postType, setPostType] = useState(initialType); // 'review' | 'qna'
  const [author, setAuthor] = useState('');
  const [petType, setPetType] = useState('강아지');
  const [petInfo, setPetInfo] = useState('');
  const [productType, setProductType] = useState('몬스멕타 (오리지널)');
  const [feedDays, setFeedDays] = useState('3일차');
  const [beforeScore, setBeforeScore] = useState(2);
  const [afterScore, setAfterScore] = useState(5);
  const rating = 5;
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [pin, setPin] = useState('');

  if (!isOpen) return null;

  // 사료관리법 안내 키워드 감지
  const hasMedicalKeywords = /(치료|완치|치료약|약국|처방약)/.test(content) || /(치료|완치)/.test(title);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!author.trim() || !title.trim() || !content.trim()) {
      alert('닉네임, 제목, 내용을 모두 입력해 주세요.');
      return;
    }

    const newPost = {
      id: 'post_' + Date.now(),
      type: postType,
      author: author.trim(),
      petType,
      petInfo: petInfo.trim() || `${petType} 보호자`,
      productType,
      feedDays: postType === 'review' ? feedDays : null,
      beforeScore: postType === 'review' ? Number(beforeScore) : null,
      afterScore: postType === 'review' ? Number(afterScore) : null,
      rating: postType === 'review' ? rating : null,
      title: title.trim(),
      content: content.trim(),
      createdAt: '방금 전',
      likes: 1,
      comment: null // 박선생 답변이 달릴 공간
    };

    onAddPost(newPost);
    alert(postType === 'review' ? '소중한 급여 후기가 등록되었습니다!' : '박선생 1:1 상담 질문이 접수되었습니다. 곧 답변이 등록됩니다.');
    onClose();
  };

  return (
    <div className="fixed inset-0 z-[110] flex items-center justify-center bg-black/65 backdrop-blur-sm p-4 animate-in fade-in">
      <div className="bg-white rounded-3xl shadow-2xl max-w-xl w-full overflow-hidden border border-emerald-100 flex flex-col max-h-[92vh]">
        {/* Modal Header */}
        <div className="bg-gradient-to-r from-emerald-800 to-teal-900 px-6 py-5 text-white flex items-center justify-between">
          <div>
            <h3 className="font-black text-lg sm:text-xl tracking-tight">
              {postType === 'review' ? '✍️ 몬스멕타 분변 케어 후기 작성' : '🙋 박선생 1:1 건강 상담 질문하기'}
            </h3>
            <p className="text-xs text-emerald-200 mt-0.5">
              회원가입 없이 닉네임으로 간편하게 참여하는 몬스멕타 보호자 라운지
            </p>
          </div>
          <button
            onClick={onClose}
            className="text-white/80 hover:text-white bg-white/10 hover:bg-white/20 p-2 rounded-full transition-colors cursor-pointer"
            aria-label="닫기"
          >
            ✕
          </button>
        </div>

        {/* Modal Body */}
        <form onSubmit={handleSubmit} className="p-6 overflow-y-auto space-y-4 text-start">
          {/* Post Type Tabs */}
          <div className="flex bg-slate-100 p-1 rounded-2xl">
            <button
              type="button"
              onClick={() => setPostType('review')}
              className={`flex-1 py-2.5 rounded-xl text-xs sm:text-sm font-extrabold transition-all cursor-pointer ${
                postType === 'review'
                  ? 'bg-white text-emerald-900 shadow-sm border border-slate-200'
                  : 'text-slate-500 hover:text-slate-800'
              }`}
            >
              💩 분변 개선 급여 후기
            </button>
            <button
              type="button"
              onClick={() => setPostType('qna')}
              className={`flex-1 py-2.5 rounded-xl text-xs sm:text-sm font-extrabold transition-all cursor-pointer ${
                postType === 'qna'
                  ? 'bg-white text-teal-900 shadow-sm border border-slate-200'
                  : 'text-slate-500 hover:text-slate-800'
              }`}
            >
              💬 박선생 1:1 상담 질문
            </button>
          </div>

          {/* Author & Pet Info */}
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <div>
              <label className="block text-xs font-bold text-slate-700 mb-1">작성자 닉네임 *</label>
              <input
                type="text"
                required
                value={author}
                onChange={(e) => setAuthor(e.target.value)}
                placeholder="예) 초코맘"
                className="w-full px-3 py-2 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm focus:ring-2 focus:ring-emerald-600 focus:bg-white outline-none"
              />
            </div>
            <div>
              <label className="block text-xs font-bold text-slate-700 mb-1">반려동물 구분 *</label>
              <select
                value={petType}
                onChange={(e) => setPetType(e.target.value)}
                className="w-full px-3 py-2 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm focus:ring-2 focus:ring-emerald-600 focus:bg-white outline-none font-medium"
              >
                <option value="강아지">🐶 강아지</option>
                <option value="고양이">🐱 고양이</option>
                <option value="특수동물">🦎 특수동물/조류</option>
              </select>
            </div>
            <div>
              <label className="block text-xs font-bold text-slate-700 mb-1">품종 및 나이</label>
              <input
                type="text"
                value={petInfo}
                onChange={(e) => setPetInfo(e.target.value)}
                placeholder="예) 포메라니안, 2살"
                className="w-full px-3 py-2 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm focus:ring-2 focus:ring-emerald-600 focus:bg-white outline-none"
              />
            </div>
          </div>

          {/* Product & Feed Days */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <div>
              <label className="block text-xs font-bold text-slate-700 mb-1">급여 라인업 *</label>
              <select
                value={productType}
                onChange={(e) => setProductType(e.target.value)}
                className="w-full px-3 py-2 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm focus:ring-2 focus:ring-emerald-600 focus:bg-white outline-none font-medium"
              >
                <option value="몬스멕타 (오리지널)">몬스멕타 (오리지널 100ml)</option>
                <option value="몬스멕타 헤파맥스">몬스멕타 헤파맥스 (100ml)</option>
                <option value="몬스멕타 레날 디톡스">몬스멕타 레날 디톡스 (100ml)</option>
              </select>
            </div>
            {postType === 'review' && (
              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">급여 기간 *</label>
                <select
                  value={feedDays}
                  onChange={(e) => setFeedDays(e.target.value)}
                  className="w-full px-3 py-2 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm focus:ring-2 focus:ring-emerald-600 focus:bg-white outline-none font-medium"
                >
                  <option value="1일차 (당일 즉각 개선)">1일차 (당일 즉각 호전)</option>
                  <option value="2일차">2일차</option>
                  <option value="3일차 (추천)">3일차</option>
                  <option value="5일차">5일차</option>
                  <option value="7일차 이상 (꾸준한 관리)">7일차 이상 (꾸준한 관리)</option>
                </select>
              </div>
            )}
          </div>

          {/* Fecal Score Selector (Review Only) */}
          {postType === 'review' && (
            <div className="p-4 bg-emerald-50/50 border border-emerald-200 rounded-2xl space-y-3">
              <div className="flex items-center justify-between">
                <span className="text-xs font-black text-emerald-950 flex items-center gap-1">
                  <span>📊</span> Fecal Score (변 상태 1~7단계 점수 변화)
                </span>
                <span className="text-[11px] font-bold text-emerald-700">5단계 = 건강한 바나나변</span>
              </div>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                <div>
                  <span className="block text-slate-600 font-bold mb-1">급여 전 (Before):</span>
                  <select
                    value={beforeScore}
                    onChange={(e) => setBeforeScore(e.target.value)}
                    className="w-full p-2 bg-white border border-slate-300 rounded-xl font-medium outline-none"
                  >
                    {FECAL_SCORES.map((s) => (
                      <option key={s.score} value={s.score}>{s.label}</option>
                    ))}
                  </select>
                </div>
                <div>
                  <span className="block text-slate-600 font-bold mb-1">급여 후 (After):</span>
                  <select
                    value={afterScore}
                    onChange={(e) => setAfterScore(e.target.value)}
                    className="w-full p-2 bg-white border border-emerald-400 rounded-xl font-bold text-emerald-800 outline-none"
                  >
                    {FECAL_SCORES.map((s) => (
                      <option key={s.score} value={s.score}>{s.label}</option>
                    ))}
                  </select>
                </div>
              </div>
            </div>
          )}

          {/* Title */}
          <div>
            <label className="block text-xs font-bold text-slate-700 mb-1">
              {postType === 'review' ? '후기 제목 *' : '질문 제목 *'}
            </label>
            <input
              type="text"
              required
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder={postType === 'review' ? '예) 사료 교체 후 묽은변이었는데 2일 먹이고 잡혔어요!' : '예) 3개월 강아지 몸무게 1kg인데 하루 급여량이 어떻게 되나요?'}
              className="w-full px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm focus:ring-2 focus:ring-emerald-600 focus:bg-white outline-none font-medium"
            />
          </div>

          {/* Content */}
          <div>
            <label className="block text-xs font-bold text-slate-700 mb-1">
              {postType === 'review' ? '상세 급여 경험 내용 *' : '아이 상태 및 구체적인 질문 내용 *'}
            </label>
            <textarea
              required
              rows={4}
              value={content}
              onChange={(e) => setContent(e.target.value)}
              placeholder={
                postType === 'review'
                  ? '급여 전 아이의 상태, 급여 방법, 며칠 만에 변 상태가 어떻게 달라졌는지 솔직한 경험을 공유해 주세요.'
                  : '아이의 현재 분변 상태(색상, 묽기), 동반 증상, 복용 중인 다른 영양제나 처방약을 함께 적어주시면 박선생님께서 더욱 정확하게 상담해 드립니다.'
              }
              className="w-full p-3.5 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm focus:ring-2 focus:ring-emerald-600 focus:bg-white outline-none leading-relaxed resize-none"
            />
          </div>

          {/* 사료관리법 권장 가이드 알림창 */}
          {hasMedicalKeywords && (
            <div className="p-3 bg-amber-50 border border-amber-300 rounded-xl text-xs text-amber-900 space-y-1 animate-in fade-in">
              <span className="font-extrabold flex items-center gap-1">
                <span>🛡️</span> 사료관리법 권장 가이드 안내
              </span>
              <p className="leading-relaxed">
                몬스멕타는 의약품이 아닌 장 점막을 물리적으로 코팅·보호하는 <strong>&lsquo;보조사료&rsquo;</strong>입니다. 
                &lsquo;치료&rsquo;나 &lsquo;완치&rsquo; 대신 <strong>&lsquo;변 상태 개선&rsquo;, &lsquo;장 점막 보호&rsquo;</strong> 등의 권장 표현을 사용하시면 합법적이고 안전하게 후기가 유지됩니다.
              </p>
            </div>
          )}

          {/* Pin */}
          <div className="flex items-center justify-between gap-4 pt-1">
            <div className="flex-1">
              <label className="block text-[11px] font-bold text-slate-500 mb-1">수정/삭제용 비밀번호 4자리</label>
              <input
                type="password"
                maxLength={4}
                value={pin}
                onChange={(e) => setPin(e.target.value)}
                placeholder="숫자 4자리"
                className="w-28 px-2.5 py-1.5 bg-slate-50 border border-slate-200 rounded-lg text-xs outline-none"
              />
            </div>
            <button
              type="submit"
              className="px-6 py-3 bg-gradient-to-r from-emerald-700 to-teal-800 hover:from-emerald-800 hover:to-teal-900 text-white font-black text-sm rounded-xl shadow-md transition-all cursor-pointer active:scale-95"
            >
              {postType === 'review' ? '후기 등록하기 ✨' : '상담 질문 접수하기 🚀'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default CommunityWriteModal;

