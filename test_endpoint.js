async function checkEndpoint() {
  const url = 'https://www.juso.go.kr/support/AddressMainSearch.do';
  const res = await fetch(url);
  const text = await res.text();
  
  // Find all form actions and script src / ajax calls
  const forms = text.match(/<form[^>]*>/g) || [];
  console.log('Forms:', forms);
  
  // Find where search is submitted
  const searchMatch = text.match(/function\s+search\s*\([^{]*\{[^}]*\}/g) || [];
  console.log('Search function:', searchMatch);
  
  // Let's print any URL paths inside scripts
  const urls = text.match(/[\/a-zA-Z0-9_\-]+\.do\b/g) || [];
  console.log('*.do URLs found:', Array.from(new Set(urls)));
}

checkEndpoint();
