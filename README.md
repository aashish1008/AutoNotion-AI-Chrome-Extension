# AutoNotion AI: Chrome Extension
AutoNotion AI is a Chrome extension designed to help you take smart, efficient notes from YouTube videos and web pages using advanced AI techniques like Retrieval-Augmented Generation (RAG) and the LLaMA3 model. With a focus on streamlining study workflows, this extension automates the process of generating structured and actionable notes, making learning more accessible.

https://github.com/user-attachments/assets/e32c359b-092b-4f86-9aab-e83f6c70c5b1

## Features
- **Automatic Note Generation:** Create notes from YouTube videos and web pages instantly using AI.
- **Summarization:** Get key insights and actionable items extracted and organized for quick learning.
- **Customizable Content:** AutoNotion AI generates easy-to-read notes that can be personalized and refined.
- **Intelligent Context Understanding:** Whether it's a complex research paper or a lecture video, the AI intelligently extracts the most relevant information.
- **Offline Storage:** Save and revisit notes without needing to reload the webpage or video.

## How It Works
AutoNotion AI utilizes a Retrieval-Augmented Generation (RAG) framework, incorporating agents and tools to ensure precise and relevant note-taking. Here's a breakdown:

- **RAG Framework:** This approach combines information retrieval with AI-driven note generation, ensuring that content from external sources (videos or web pages) is retrieved and summarized accurately.
  
    - **Agents and Tools:**
        - **YouTube Tool:** Extracts and summarizes transcripts from YouTube videos, highlighting key points, insights, and takeaways.
        - **Web Page Tool:** Analyzes and summarizes web pages, capturing essential information for easier study or research.
    - These tools are triggered by agents to retrieve the most relevant data from videos or web pages, ensuring efficient note generation.

## Technology Used
**Frontend:**

  - **HTML/CSS:** Provides the structure and styling for the popup interface.
  - **JavaScript:** Manages user interactions and communicates with the backend API, primarily through `popup.js`.
  - **Chrome Extensions API:** Utilizes `chrome.tabs` for managing active tabs and `chrome.storage` for local data persistence.

**Backend:**

  - **Python Flask:** Serves as the backend API for handling note generation requests.
  - **LangChain:** Supports multiple functionalities, including:
    - **Document Loaders:** For retrieving and processing web content.
    - **Agents:** Facilitates the creation of agents for automated tasks.
    - **Tool Creation:** Enables the development of tools for different data sources.
    - **FAISS:** A vector database for efficient document retrieval.
    - **Cohere Embeddings:** Embeds content into vectors.
    - **LLM Models:** Utilizes ChatGroq `(llama3 model)` for generating and structuring notes.

**RAG Techniques:**

- Implements **Retrieval-Augmented Generation (RAG)** methods by combining information retrieval and language generation, enabling the system to generate contextually relevant notes based on web pages and YouTube videos.

**Deployment:**

- The application runs locally on Flask with CORS enabled for cross-origin requests.


## Installation
- **Clone the repository:**
  ``` bash
  git clone https://github.com/aashish1008/AutoNotion-AI-Chrome-Extension.git
- **Load the extension:**
  - Go to the Chrome Extensions page (chrome://extensions/).
  - Enable Developer mode.
  - Click on Load unpacked and select the folder containing the cloned repository.
- You're all set! The AutoNotion AI extension is now installed and ready to use.
  
## How to Use
1. Navigate to any YouTube video or web page.
2. Click the AutoNotion AI extension icon in your browser toolbar.
3. Generate Note:
    - For YouTube videos: Retrieve and summarize the video transcript.
    - For web pages: Extract and summarize the page content.
4. Review the notes directly within the extension, or export them for future use.

## Contributing
We welcome contributions! If you'd like to contribute, please follow these steps:

- Fork the repository.
- Create a new branch `(git checkout -b feature-branch)`.
- Make your changes and commit them `(git commit -m "Add new feature")`.
- Push the changes to your branch `(git push origin feature-branch)`.
- Submit a pull request.
