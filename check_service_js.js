async function checkServiceJs() {
  const url = 'https://t1.kakaocdn.net/postcode/cssjs/service/1782746612907/service.v2.min.js';
  const res = await fetch(url);
  const text = await res.text();
  
  const urls = text.match(/["'](\/|https?:)[^"']*["']/g) || [];
  console.log('URLs in service.v2.min.js:', Array.from(new Set(urls)));
}

checkServiceJs();
