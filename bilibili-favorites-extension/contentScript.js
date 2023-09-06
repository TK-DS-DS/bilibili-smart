const items = document.querySelectorAll('.small-item');
const favoriteLinks = [];

for (const item of items) {
  const link = item.querySelector('.title').getAttribute('href');
  const title = item.querySelector('.title').textContent;
  favoriteLinks.push({ title, link });
}

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.favoriteLinks) {
    const outputDiv = document.getElementById('output');
    outputDiv.innerHTML = '';

    for (const video of message.favoriteLinks) {
      const linkElement = document.createElement('a');
      linkElement.href = video.link;
      linkElement.textContent = video.title;
      linkElement.target = '_blank';

      const brElement = document.createElement('br');

      outputDiv.appendChild(linkElement);
      outputDiv.appendChild(brElement);
    }
  }
});
