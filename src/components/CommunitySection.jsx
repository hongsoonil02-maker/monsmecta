import { useState } from 'react';
import CommunityWriteModal from './CommunityWriteModal';

const INITIAL_REVIEWS = [
  {
    id: 'rev_1',
    type: 'review',
    author: '포미언니',
    petType: '강아지',
    petInfo: '포메라니안, 8개월 (3.1kg)',
    productType: '몬스멕타 (오리지널)',
    feedDays: '2일차',
    beforeScore: 2,
    afterScore: 5,
    rating: 5,
    title: '사료 바꾸고 3일 내내 물설사였는데, 이틀 만에 예쁜 바나나변 봤어요!',
    content: '사료를 알러지 사료로 바꾸는 과정에서 장이 뒤집어졌는지 형태도 없는 점액변을 계속 봐서 밤새 걱정했습니다. 동물병원 원장님 추천으로 몬스멕타 1ml씩 하루 두 번 먹였는데 2일 만에 변이 단단하게 뭉쳐서 감동했습니다 ㅠㅠ 억지로 지사제로 변을 굳히는 게 아니라 점막을 씌워준다는 설명이 맞네요.',
    createdAt: '2026.11.02',
    likes: 38,
    comment: {
      author: '박선생 (하남사랑동물병원)',
      text: '사료 교체 시 장내 미생물총 급변으로 장 점막 상피세포가 자극받은 케이스입니다. 몬스멕타의 고순도 나노 몬모릴로나이트가 장 점막을 즉각 피복하여 수분 과다 누출을 막아주어 빠른 호전을 보였습니다. 잘 케어해 주셨습니다!'
    }
  },
  {
    id: 'rev_2',
    type: 'review',
    author: '달콩집사',
    petType: '고양이',
    petInfo: '코리안 숏헤어, 4살 (4.5kg)',
    productType: '몬스멕타 레날 디톡스',
    feedDays: '5일차',
    beforeScore: 2,
    afterScore: 5,
    rating: 5,
    title: '신부전 초기 묽은변 보던 아이인데 변 냄새도 줄고 변도 건강해졌어요',
    content: '신장 수치가 살짝 오르면서 소화도 잘 안 되고 변이 늘 묽었는데, 레날 디톡스 급여하고 5일 만에 단단하고 촉촉한 정상변을 봅니다. 비피도박테리움 1,000억 마리가 들어있어서 그런지 특유의 심하던 변 냄새도 확연히 줄었어요. 꾸준히 먹일 생각입니다.',
    createdAt: '2026.10.29',
    likes: 45,
    comment: {
      author: '박선생 (하남사랑동물병원)',
      text: '레날 디톡스는 장-신장 축(Gut-Kidney Axis)을 기반으로 장내 유독성 질소 화합물을 흡착 배출합니다. 장 건강과 신장 여과 부담 경감을 동시에 기대할 수 있는 모범적인 급여 관리입니다.'
    }
  },
  {
    id: 'rev_3',
    type: 'review',
    author: '비숑마루맘',
    petType: '강아지',
    petInfo: '비숑 프리제, 1살 (5.2kg)',
    productType: '몬스멕타 (오리지널)',
    feedDays: '1일차 (당일 즉각 호전)',
    beforeScore: 1,
    afterScore: 4,
    rating: 5,
    title: '산책길에 뭘 잘못 주워먹고 배에서 꾸르륵 소리나며 설사했는데 즉효네요',
    content: '갑자기 배에서 천둥소리가 나더니 수양성 설사를 2번 연속 봐서 놀란 마음에 상비해둔 몬스멕타를 바로 1펌프 먹였습니다. 저녁에 바로 형태 있는 변으로 바뀌더니 다음 날 아침에는 정상변으로 돌아왔어요. 상비약으로 무조건 쟁여둬야 할 필수템입니다.',
    createdAt: '2026.10.25',
    likes: 29,
    comment: {
      author: '박선생 (하남사랑동물병원)',
      text: '이물 섭취나 세균성 외독소(Exotoxin) 유입 시, 몬스멕타의 1g당 800m² 이상의 흡착 표면적이 유해 물질을 장내에서 물리적으로 고착하여 배출시키는 강력한 응급 방어 작용을 한 결과입니다.'
    }
  }
];

const INITIAL_QNA = [
  {
    id: 'qna_1',
    type: 'qna',
    author: '몽이엄마',
    petType: '강아지',
    petInfo: '말티푸, 3개월 (900g)',
    productType: '몬스멕타 (오리지널)',
    title: '생후 3개월 된 900g 초소형 아기 강아지인데 급여량이 어떻게 되나요?',
    content: '분양받아 온 지 1주일 되었는데 환경 변화 때문인지 약간 무른변을 봅니다. 1kg도 안 나가는 어린 강아지에게 몬스멕타를 먹여도 안전한지, 하루에 몇 번 얼마나 펌핑해서 먹여야 하는지 알고 싶습니다.',
    createdAt: '2026.11.01',
    comment: {
      author: '박선생 (하남사랑동물병원)',
      text: '1kg 미만의 어린 자견은 1회 급여 시 펌프를 반만 살짝 눌러 약 0.5ml를 아침/저녁 식간에 단독으로 급여해 주시면 안전합니다. 몬스멕타는 체내에 흡수되지 않고 물리적으로 점막만 코팅 후 대변으로 배출되므로 어린 자견에게도 매우 안전합니다. 단, 구토나 식욕부진이 동반된다면 단순 식이성이 아닐 수 있으니 내원 진료를 권장합니다.'
    }
  },
  {
    id: 'qna_2',
    type: 'qna',
    author: '러블리냥',
    petType: '고양이',
    petInfo: '러시안블루, 5살 (4kg)',
    productType: '몬스멕타 (오리지널)',
    title: '평소 먹이는 유산균 영양제와 함께 먹여도 되나요? 시간 간격이 필요한가요?',
    content: '매일 아침 유산균 파우더를 츄르에 섞어주고 있습니다. 몬스멕타도 츄르에 함께 섞어서 먹여도 되는지, 아니면 따로 시간을 띄워서 먹여야 흡수나 효과에 방해가 안 되는지 궁금합니다.',
    createdAt: '2026.10.28',
    comment: {
      author: '박선생 (하남사랑동물병원)',
      text: '몬스멕타는 강력한 흡착력과 점막 코팅 능력이 있으므로, 유산균이나 다른 영양제, 처방약과는 최소 1~2시간 이상 시간 간격을 두고 단독 급여하시는 것이 가장 이상적입니다. 예를 들어 유산균은 아침 식사와 함께, 몬스멕타는 식간 공복이나 취침 전에 급여하시면 최상의 시너지를 얻을 수 있습니다.'
    }
  },
  {
    id: 'qna_3',
    type: 'qna',
    author: '골디파파',
    petType: '강아지',
    petInfo: '골든리트리버, 6살 (32kg)',
    productType: '몬스멕타 헤파맥스',
    title: '대형견 간수치가 경미하게 높은 편인데 헤파맥스 급여 주기와 효과가 궁금합니다.',
    content: '건강검진에서 ALT 수치가 정상 범위 상단에 걸쳐 있어 간보호제를 찾던 중 헤파맥스를 보게 되었습니다. 대형견의 경우 100ml 한 병으로 며칠이나 급여 가능한지, 장기 급여해도 간에 부담이 없는지 여쭙니다.',
    createdAt: '2026.10.22',
    comment: {
      author: '박선생 (하남사랑동물병원)',
      text: '헤파맥스는 실리마린, L-메치오닌 및 장-간 순환계 독소 흡착 성분이 복합되어 간세포 항산화와 글루타치온 생성을 돕습니다. 30kg 대형견 기준 1회 4~5ml씩 1일 2회 급여를 권장하며, 체내 대사 부산물 없이 장에서 독소만 끌고 배출되므로 간 대사 부담이 0%에 가깝습니다. 1~2개월 지속 급여 후 혈액검사 재측정을 추천드립니다.'
    }
  }
];

const CommunitySection = () => {
  const [activeTab, setActiveTab] = useState('review'); // 'review' | 'qna'
  const [filterPet, setFilterPet] = useState('all'); // 'all' | '강아지' | '고양이' | '특수동물'
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [posts, setPosts] = useState(() => {
    try {
      const saved = localStorage.getItem('monsmecta_community_posts_v1');
      if (saved) {
        return JSON.parse(saved);
      }
    } catch { /* ignore */ }
    return [...INITIAL_REVIEWS, ...INITIAL_QNA];
  });

  const handleAddPost = (newPost) => {
    const updated = [newPost, ...posts];
    setPosts(updated);
    try {
      localStorage.setItem('monsmecta_community_posts_v1', JSON.stringify(updated));
    } catch { /* ignore */ }
  };

  const filteredPosts = posts
    .filter((p) => p.type === activeTab)
    .filter((p) => (filterPet === 'all' ? true : p.petType === filterPet));

  return (
    <section id="community" className="py-14 sm:py-20 bg-slate-50 border-b border-slate-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Section Header */}
        <div className="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-10 pb-6 border-b border-slate-200">
          <div>
            <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-emerald-100 border border-emerald-300 text-emerald-900 text-xs font-black mb-3">
              <span>💬</span>
              <span>MONSMECTA CAFE &amp; CASE LOUNGE</span>
              <span>·</span>
              <span>보호자 소통 플랫폼</span>
            </div>
            <h2 className="text-2xl sm:text-4xl font-black text-slate-900 tracking-tight">
              몬스멕타 <span className="text-emerald-700">케이스 라운지</span> &amp; <span className="text-teal-700">박선생 상담소</span>
            </h2>
            <p className="mt-2 text-slate-600 text-sm sm:text-base leading-relaxed break-keep max-w-2xl">
              실제 보호자님들의 분변 개선 케이스(Fecal Score 일지)와 하남사랑동물병원 김동준 원장(박선생)의 1:1 맞춤 상담이 공유되는 공간입니다.
            </p>
          </div>

          <div className="flex flex-wrap items-center gap-2.5">
            <button
              onClick={() => { setActiveTab('review'); setIsModalOpen(true); }}
              className="px-5 py-3 bg-emerald-700 hover:bg-emerald-800 text-white font-black text-xs sm:text-sm rounded-xl shadow-md transition-all active:scale-95 cursor-pointer flex items-center gap-1.5"
            >
              <span>✍️</span>
              <span>내 아이 급여 후기 남기기</span>
            </button>
            <button
              onClick={() => { setActiveTab('qna'); setIsModalOpen(true); }}
              className="px-5 py-3 bg-teal-700 hover:bg-teal-800 text-white font-black text-xs sm:text-sm rounded-xl shadow-md transition-all active:scale-95 cursor-pointer flex items-center gap-1.5"
            >
              <span>🙋</span>
              <span>박선생 1:1 질문하기</span>
            </button>
          </div>
        </div>

        {/* Top Filter & Tab Controller */}
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-8">
          {/* Main 2 Tabs */}
          <div className="inline-flex bg-slate-200/80 p-1 rounded-2xl w-full sm:w-auto">
            <button
              onClick={() => setActiveTab('review')}
              className={`flex-1 sm:flex-initial px-5 py-2.5 rounded-xl text-xs sm:text-sm font-black transition-all cursor-pointer flex items-center justify-center gap-2 ${
                activeTab === 'review'
                  ? 'bg-white text-emerald-950 shadow-md'
                  : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              <span>💩</span>
              <span>리얼 급여 후기 (Fecal Score 일지)</span>
              <span className="text-[11px] px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 font-extrabold">
                {posts.filter(p => p.type === 'review').length}
              </span>
            </button>
            <button
              onClick={() => setActiveTab('qna')}
              className={`flex-1 sm:flex-initial px-5 py-2.5 rounded-xl text-xs sm:text-sm font-black transition-all cursor-pointer flex items-center justify-center gap-2 ${
                activeTab === 'qna'
                  ? 'bg-white text-teal-950 shadow-md'
                  : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              <span>💬</span>
              <span>박선생 1:1 Q&amp;A 상담실</span>
              <span className="text-[11px] px-2 py-0.5 rounded-full bg-teal-100 text-teal-800 font-extrabold">
                {posts.filter(p => p.type === 'qna').length}
              </span>
            </button>
          </div>

          {/* Pet Filter Buttons */}
          <div className="flex items-center gap-1.5 overflow-x-auto pb-1 sm:pb-0 text-xs">
            <span className="text-slate-400 font-bold mr-1 shrink-0">축종 필터:</span>
            {[
              { id: 'all', label: '전체' },
              { id: '강아지', label: '🐶 강아지' },
              { id: '고양이', label: '🐱 고양이' },
              { id: '특수동물', label: '🦎 특수동물' },
            ].map((f) => (
              <button
                key={f.id}
                onClick={() => setFilterPet(f.id)}
                className={`px-3 py-1.5 rounded-lg font-bold transition-all cursor-pointer shrink-0 ${
                  filterPet === f.id
                    ? 'bg-slate-900 text-white shadow-xs'
                    : 'bg-white border border-slate-200 text-slate-600 hover:bg-slate-100'
                }`}
              >
                {f.label}
              </button>
            ))}
          </div>
        </div>

        {/* Post Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredPosts.map((post) => (
            <div
              key={post.id}
              className="bg-white rounded-3xl p-6 border border-slate-200/90 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between text-start group hover:-translate-y-1"
            >
              <div className="space-y-3.5">
                {/* Card Top: Author & Product */}
                <div className="flex items-center justify-between text-xs">
                  <div className="flex items-center gap-2">
                    <span className="w-8 h-8 rounded-full bg-slate-100 flex items-center justify-center font-bold text-sm">
                      {post.petType === '강아지' ? '🐶' : post.petType === '고양이' ? '🐱' : '🦎'}
                    </span>
                    <div>
                      <p className="font-extrabold text-slate-900">{post.author}</p>
                      <p className="text-[11px] text-slate-400">{post.petInfo}</p>
                    </div>
                  </div>
                  <span className="text-[11px] font-bold px-2 py-0.5 rounded-md bg-emerald-50 text-emerald-800 border border-emerald-200">
                    {post.productType}
                  </span>
                </div>

                {/* Fecal Score Indicator (Reviews only) */}
                {post.type === 'review' && (
                  <div className="bg-slate-50 border border-slate-200/80 rounded-2xl p-3 space-y-1.5">
                    <div className="flex items-center justify-between text-[11px] font-extrabold">
                      <span className="text-slate-500">분변 점수 변화:</span>
                      <span className="text-amber-800 bg-amber-50 px-2 py-0.5 rounded border border-amber-200 font-bold">
                        {post.feedDays}
                      </span>
                    </div>
                    <div className="flex items-center justify-between text-xs font-black">
                      <div className="flex items-center gap-1.5">
                        <span className="text-rose-600">Before:</span>
                        <span className="px-2 py-0.5 rounded bg-rose-50 text-rose-700 border border-rose-200">
                          {post.beforeScore}단계 {post.beforeScore <= 2 ? '(설사/물변)' : '(무른변)'}
                        </span>
                      </div>
                      <span className="text-slate-400">➔</span>
                      <div className="flex items-center gap-1.5">
                        <span className="text-emerald-700">After:</span>
                        <span className="px-2 py-0.5 rounded bg-emerald-50 text-emerald-800 border border-emerald-300">
                          {post.afterScore}단계 (정상변)
                        </span>
                      </div>
                    </div>
                  </div>
                )}

                {/* Title & Content */}
                <div>
                  <h4 className="font-extrabold text-slate-900 text-sm sm:text-base leading-snug group-hover:text-emerald-700 transition-colors">
                    {post.title}
                  </h4>
                  <p className="text-xs text-slate-600 mt-2 leading-relaxed break-keep line-clamp-4">
                    {post.content}
                  </p>
                </div>

                {/* Official Expert Answer: 박선생 (하남사랑동물병원) */}
                {post.comment && (
                  <div className="bg-teal-50/70 border border-teal-200 rounded-2xl p-3.5 space-y-1.5 text-start animate-in fade-in">
                    <div className="flex items-center gap-1.5 text-[11px] font-black text-teal-900">
                      <span className="text-sm">💬</span>
                      <span className="bg-teal-700 text-white px-2 py-0.5 rounded-full text-[10px]">공식 답변</span>
                      <span>{post.comment.author}</span>
                    </div>
                    <p className="text-xs text-teal-950 leading-relaxed font-medium break-keep">
                      “{post.comment.text}”
                    </p>
                  </div>
                )}
              </div>

              {/* Card Footer */}
              <div className="mt-5 pt-3 border-t border-slate-100 flex items-center justify-between text-[11px] text-slate-400">
                <span>{post.createdAt}</span>
                <button
                  type="button"
                  className="flex items-center gap-1 text-slate-500 hover:text-emerald-700 font-bold transition-colors cursor-pointer"
                >
                  <span>👍 도움돼요</span>
                  <span>{post.likes}</span>
                </button>
              </div>
            </div>
          ))}
        </div>

        {/* Bottom Naver Cafe Sync Banner */}
        <div className="mt-12 bg-gradient-to-r from-teal-950 via-[#003828] to-slate-950 text-white rounded-3xl p-6 sm:p-8 flex flex-col md:flex-row items-center justify-between gap-6 shadow-xl border border-teal-700/60">
          <div className="flex items-center gap-4 text-center md:text-left">
            <span className="w-14 h-14 rounded-2xl bg-teal-800/80 text-white flex items-center justify-center text-3xl shrink-0 shadow-inner">
              💬
            </span>
            <div>
              <p className="font-black text-base sm:text-lg">네이버 카페 &lsquo;온라인동물병원&rsquo; 10만 반려인과 함께합니다</p>
              <p className="text-xs sm:text-sm text-teal-200 mt-1 leading-relaxed break-keep">
                카페 게시판에서 실시간 분변 상담을 신청하시거나, 전용 시크릿 코드(<code className="bg-white/20 px-1.5 py-0.5 rounded text-amber-300 font-mono">vettalk</code>)를 통해 사은품 및 무료배송 혜택을 확인하세요.
              </p>
            </div>
          </div>
          <a
            href="https://cafe.naver.com" 
            target="_blank" 
            rel="noopener noreferrer"
            className="px-6 py-3.5 bg-amber-400 hover:bg-amber-300 text-slate-950 font-black text-xs sm:text-sm rounded-xl shadow-lg transition-all shrink-0 cursor-pointer"
          >
            온라인동물병원 카페 바로가기 ↗
          </a>
        </div>

      </div>

      {/* Write Review / QnA Modal */}
      <CommunityWriteModal
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        onAddPost={handleAddPost}
        initialType={activeTab}
      />
    </section>
  );
};

export default CommunitySection;

