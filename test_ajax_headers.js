async function testAjax() {
  // Test Kakao with headers
  const kRes = await fetch('https://postcode.map.kakao.com/search?q=' + encodeURIComponent('강남대로 337'), {
    headers: {
      'Accept': 'application/json, text/javascript, */*; q=0.01',
      'X-Requested-With': 'XMLHttpRequest'
    }
  });
  const kText = await kRes.text();
  console.log('Kakao XHR response:', kText.slice(0, 500));
  
  // Test juso.go.kr with headers and POST
  const jRes = await fetch('https://www.juso.go.kr/support/AddressMainSearch.do', {
    method: 'POST',
    headers: {
      'Accept': 'application/json, text/javascript, */*; q=0.01',
      'X-Requested-With': 'XMLHttpRequest',
      'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    },
    body: `searchKeyword=${encodeURIComponent('강남대로 337')}&ajax=true`
  });
  const jText = await jRes.text();
  console.log('Juso XHR response:', jText.slice(0, 500));
}

testAjax();
