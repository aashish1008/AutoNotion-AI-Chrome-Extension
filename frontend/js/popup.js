// popup.js for RAG Note-Taking Extension

document.addEventListener('DOMContentLoaded', function() {
    const generateButton = document.getElementById('generate-note');
    const statusMessage = document.getElementById('status-message');
    const loadingIndicator = document.getElementById('loading-indicator');
    const aiSuggestion = document.getElementById('ai-suggestion');

    generateButton.addEventListener('click', generateNote);

    // Check for existing note when popup opens
    checkCurrentPageNote();

    function generateNote() {
        chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
            const url = tabs[0].url;
            if (url) {
                fetchNote(url);
            } else {
                updateStatus('Unable to get the current page URL.');
            }
        });
    }

    async function fetchNote(url) {
        try {
            updateStatus('Generating note...', true);
            aiSuggestion.textContent = '';

            const response = await fetch('http://127.0.0.1:5000/api/chat', {
                method: 'POST',
                mode: 'cors',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ url: url })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            console.log('Response data:', data);

            if (data.response) {
                updateStatus('Note generated successfully!', false);
                displayNote(data.response);
                saveNote(url, data.response);
            } else {
                throw new Error('No response data received');
            }
        } catch (error) {
            console.error('Fetch error:', error);
            updateStatus(`Error: ${error.message}. Make sure your backend is running and properly configured.`, false);
        }
    }

    function displayNote(note) {
        // Clear any previous content
        aiSuggestion.innerHTML = '';
    
        // Split the response by newline characters
        const lines = note.split('\n');
        
        let formattedNote = '';
        let currentSection = '';
    
        // Loop through each line to format it based on its content
        lines.forEach(line => {
            if (line.startsWith('**')) {
                // This is a section header, add it as an <h3>
                currentSection = `<h3>${line.replace(/\*\*/g, '')}</h3>`;
                formattedNote += currentSection;
            } else if (line.startsWith('*')) {
                // This is a list item, add it as <li> inside an unordered list
                if (!formattedNote.includes('<ul>')) {
                    formattedNote += '<ul>';
                }
                formattedNote += `<li>${line.replace('* ', '')}</li>`;
            } else if (line.trim() === '') {
                // Close the list when a blank line is encountered
                if (formattedNote.includes('<ul>')) {
                    formattedNote += '</ul>';
                }
            } else {
                // For any other text (not headers or list items), wrap it in a paragraph
                formattedNote += `<p>${line}</p>`;
            }
        });
    
        // Append any remaining open <ul> tags
        if (formattedNote.includes('<ul>') && !formattedNote.endsWith('</ul>')) {
            formattedNote += '</ul>';
        }
    
        // Insert the formatted content into the DOM
        aiSuggestion.innerHTML = formattedNote;
    }
    
    

    function saveNote(url, note) {
        chrome.storage.local.set({[url]: note}, function() {
            console.log('Note saved for URL:', url);
        });
    }

    function checkCurrentPageNote() {
        chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
            const url = tabs[0].url;
            if (url) {
                chrome.storage.local.get(url, function(result) {
                    if (result[url]) {
                        updateStatus('Existing note found for this page.');
                        displayNote(result[url]);
                    } else {
                        updateStatus('No existing note. Click "Generate AI Note" to create one.');
                    }
                });
            }
        });
    }

    function updateStatus(message, isLoading = false) {
        statusMessage.textContent = message;
        loadingIndicator.style.display = isLoading ? 'inline-block' : 'none';
    }
});