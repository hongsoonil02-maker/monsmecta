async function checkEpostBody() {
  const url = `https://www.epost.go.kr/search.RetrievePzipOfficeAddressList.comm?kwd=${encodeURIComponent('밤골5길 19')}`;
  const res = await fetch(url, {
    headers: {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
  });
  console.log(await res.text());
}
checkEpostBody();
