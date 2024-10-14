# AutoNotion AI: Chrome Extension
AutoNotion AI is a Chrome extension designed to help you take smart, efficient notes from YouTube videos and web pages using advanced AI techniques like Retrieval-Augmented Generation (RAG) and the LLaMA3 model. With a focus on streamlining study workflows, this extension automates the process of generating structured and actionable notes, making learning more accessible.

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

## Technologies Used
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python (Flask), LangChain, FAISS, Cohere Embeddings, Groq LLM (LLaMA3)
- **AI Models:** RAG (Retrieval-Augmented Generation), LLaMA3-8B-8192

## Installation
- **Clone the repository:**
  ``` bash
  git clone https://github.com/yourusername/AutoNotionAI-Extension.git
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
