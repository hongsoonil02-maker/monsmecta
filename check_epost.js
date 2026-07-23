async function checkEpost(query) {
  // Korea post address search
  const url = `https://www.epost.go.kr/search.RetrievePzipOfficeAddressList.comm?kwd=${encodeURIComponent(query)}`;
  try {
    const res = await fetch(url, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'ko-KR,ko;q=0.9'
      }
    });
    const text = await res.text();
    console.log('Epost status:', res.status, 'Length:', text.length);
    const zips = text.match(/\b[0-6]\d{4}\b/g) || [];
    console.log('Zips in epost:', Array.from(new Set(zips)));
  } catch(e) {
    console.log('Epost error:', e.message);
  }
}

checkEpost('밤골5길 19');
