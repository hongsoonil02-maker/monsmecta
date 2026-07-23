async function testFindby() {
  const url = `https://findby.co.kr/search?q=${encodeURIComponent('강릉대로 337-5')}`;
  try {
    const res = await fetch(url);
    console.log('Status:', res.status);
    const text = await res.text();
    console.log('Snippet:\n', text.slice(0, 1000));
  } catch(e) {
    console.log('Error:', e.message);
  }
}

testFindby();
