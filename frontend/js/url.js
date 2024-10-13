document.getElementById('generate-note').addEventListener('click', function() {
    const aiSuggestion = document.getElementById('ai-suggestion');

    // Reset previous output
    aiSuggestion.innerText = '';

    // Get the current active tab's URL
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        const activeTab = tabs[0];
        const url = activeTab.url;

        if (url) {
            aiSuggestion.innerText = `Active Tab URL: ${url}`;
        } else {
            aiSuggestion.innerText = "No active URL found.";
        }
    });
});
