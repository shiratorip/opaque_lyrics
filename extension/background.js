chrome.runtime.onMessage.addListener((msg) => {
  if (msg.type !== "LYRICS") return;

  fetch("http://127.0.0.1:5000/lyrics", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ lyrics: msg.lyrics })
  }).catch(err => {
    console.error("Background fetch failed:", err);
  });
});
