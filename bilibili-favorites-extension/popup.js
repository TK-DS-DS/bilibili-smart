document.getElementById('extractButton').addEventListener('click', () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      chrome.scripting.executeScript({
        target: { tabId: tabs[0].id },
        function: extractFavorites,
        args: [tabs[0].url]
      });
    });
  });
  
  function extractFavorites(url) {
    if (url.includes("bilibili.com/favlist")) {
      chrome.scripting.executeScript({
        target: { tabId: tabs[0].id },
        function: extractFavoritesFromPage
      });
    } else {
      alert("Please navigate to a Bilibili favorites page.");
    }
  }
  
  function extractFavoritesFromPage() {
    const items = document.querySelectorAll('.small-item');
    const favoriteLinks = [];
  
    for (const item of items) {
      const link = item.querySelector('.title').getAttribute('href');
      const title = item.querySelector('.title').textContent;
      favoriteLinks.push({ title, link });
    }
  
    chrome.runtime.sendMessage({ favoriteLinks: favoriteLinks });
  }
  