async function investigate() {
  const epostRes = await fetch('https://www.epost.go.kr/search.RetrievePstcdInnerList.comm', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8' },
    body: 'keyword=' + encodeURIComponent('강남대로 337')
  });
  console.log('--- Epost text ---');
  console.log(await epostRes.text());

  // Check juso.go.kr search
  const jusoRes = await fetch('https://www.juso.go.kr/support/AddressMainSearch.do?searchKeyword=' + encodeURIComponent('강남대로 337'));
  const jusoText = await jusoRes.text();
  console.log('\n--- Juso text (first 1500 chars) ---');
  console.log(jusoText.slice(0, 1500));
}

investigate();
