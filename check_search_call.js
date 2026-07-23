async function checkSearchCall() {
  const url = 'https://t1.kakaocdn.net/postcode/cssjs/service/1782746612907/service.v2.min.js';
  const res = await fetch(url);
  const text = await res.text();
  
  const idx = text.indexOf('"/search"');
  if (idx !== -1) {
    console.log('Snippet around /search:\n', text.slice(idx - 300, idx + 500));
  }
}

checkSearchCall();
