async function testDaum() {
  const jsRes = await fetch('https://t1.daumcdn.net/mapjsapi/bundle/postcode/prod/postcode.v2.js');
  const jsText = await jsRes.text();
  
  // Find URL paths inside Daum postcode script
  const urls = jsText.match(/https?:\/\/[a-zA-Z0-9_\-\.\/\?=&]+/g) || [];
  const paths = jsText.match(/[\/a-zA-Z0-9_\-]+\/(search|postcode|addr)[a-zA-Z0-9_\-\.\/\?=&]*/g) || [];
  console.log('Daum URLs:', Array.from(new Set(urls)));
  console.log('Daum paths:', Array.from(new Set(paths)));
}

testDaum();
