async function checkKakaoBody() {
  const url = 'https://postcode.map.kakao.com/search?q=' + encodeURIComponent('강릉대로 337-5');
  const res = await fetch(url);
  const text = await res.text();
  console.log(text);
}

checkKakaoBody();
