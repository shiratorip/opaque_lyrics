let lastLyrics = "";
let enabled = true;

chrome.storage.sync.get(['enabled'], (result) => {
  enabled = result.enabled !== false;
});

chrome.storage.onChanged.addListener((changes) => {
  if (changes.enabled) {
    enabled = changes.enabled.newValue;
  }
});

function getLyrics() {

const candidates = document.querySelectorAll("yt-formatted-string.description");

const lyricsEl = [...candidates].find(el => !el.querySelector("span"));
const el = lyricsEl;

  return el ? el.innerText.trim() : null;
}


setInterval(() => {
  if (!enabled) return;
  const lyrics = getLyrics();
  if (lyrics && lyrics !== lastLyrics) {
    lastLyrics = lyrics;

    chrome.runtime.sendMessage({
      type: "LYRICS",
      lyrics
    });
  }
  console
}, 500);
    
setInterval(() => {
  if (!enabled) return;
  fetchLyrics();
}, 1000);  

async function fetchLyrics() {
    try {
        const response = await fetch("http://127.0.0.1:5000/get_status");
        const data = await response.json();
        if (data.status === "force") {
            chrome.runtime.sendMessage({
              type: "LYRICS",
              lyrics: lastLyrics
            });
        }
    } catch (err) {
        console.error("Failed to fetch status:", err);
    }
}