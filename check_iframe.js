async function checkIframe() {
  const url = 'https://t1.kakaocdn.net/postcode/cssjs/service/1782746612907/service.v2.min.js';
  const res = await fetch(url);
  const text = await res.text();
  
  // Find where iframe is created or where src is assigned
  const matches = text.match(/[a-zA-Z0-9_\.]+\s*=\s*[^;]*(\/search|\/guide)[^;]*/g) || [];
  for (const m of matches) {
    if (m.length < 500) console.log('Match:', m);
  }
}

checkIframe();
