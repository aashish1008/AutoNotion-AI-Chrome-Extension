import os
import re
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_cohere import CohereEmbeddings
from langchain_groq import ChatGroq
from langchain.tools.retriever import create_retriever_tool
from langchain.schema import Document
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_tool_calling_agent
from langchain.agents import AgentExecutor

# Load environment variables from the correct path
load_dotenv('backend/.env')

os.environ["COHERE_API_KEY"] = os.getenv("COHERE_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")




app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})



class NoteSage:
    def __init__(self, url, inp):
        self.url = url
        self.inp = inp
        self.youtube_url = ""
        self.web_url = ""
        self.embeddings = CohereEmbeddings(model="embed-english-v3.0")

    def check_url_sources(self):
        # Define the pattern for YouTube URLs
        youtube_pattern = re.compile(r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/')

        # Check if the URL matches the YouTube pattern and assign it appropriately
        if youtube_pattern.search(self.url):
            self.youtube_url = self.url
        else:
            self.web_url = self.url

    def extract_transcript_details(self):
        try:
            video_id = self.youtube_url.split("v=")[1]
            transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

            # Use join for better performance
            transcript = " ".join([entry["text"] for entry in transcript_text]).strip()

            return transcript

        except Exception as e:
            # Optional: Handle specific exceptions for clarity
            print(f"An error occurred: {e}")
            raise e

    def extract_web_context_details(self):
        try:
            loader = WebBaseLoader(self.web_url)
            docs = loader.load()
            txt_split = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            context = txt_split.split_documents(docs)

            return context
        except Exception as e:
            raise e

    def retrieving_web_context(self):
        docs = self.extract_web_context_details()
        retriever = FAISS.from_documents(docs, self.embeddings)
        return retriever.as_retriever()

    def retrieving_youtube_context(self):
        transcript = self.extract_transcript_details()

        # Create a Document object from the transcript text
        transcript_document = [Document(page_content=transcript, metadata={"source": self.youtube_url})]

        txt_split = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

        final_docs = txt_split.split_documents(transcript_document)

        # Now pass the Document object to FAISS
        retriever = FAISS.from_documents(final_docs, self.embeddings)
        return retriever.as_retriever()

    def retriever_tools(self):
        tools = []

        # Add YouTube tool if it's a YouTube URL
        if self.youtube_url:
            youtube_source_tool = create_retriever_tool(
                self.retrieving_youtube_context(),
                "YouTube",
                "This tool helps users summarize video content for quick note-taking."
            )
            tools.append(youtube_source_tool)

        # Add Web Pages tool if it's a web URL
        elif self.web_url:
            web_source_tool = create_retriever_tool(
                self.retrieving_web_context(),
                "Web Pages",
                "This tool provides concise summaries for efficient note-taking."
            )
            tools.append(web_source_tool)

        return tools

    def setup_llm(self):
        llm = ChatGroq(model_name="llama3-8b-8192", max_tokens=8000)
        return llm

    def setup_prompt(self):
        return ChatPromptTemplate.from_messages([
            ("system",
            "You are a highly efficient note-taking assistant."),
            ("placeholder", "{chat_history}"),
            ("human", f"""
            Content Type: {'YouTube' if self.youtube_url else 'Web Page'}
            URL: {self.url}
            Create structured and detailed study notes.
            Ensure the notes are organized and clear. Use bullet points for clarity, and consider including headings or subheadings for different sections.
            """),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ])

    def run(self):
        self.check_url_sources()
        llm = self.setup_llm()
        tools = self.retriever_tools()
        prompt = self.setup_prompt()

        agent = create_tool_calling_agent(llm, tools, prompt)
        agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)

        resp = agent_executor.invoke({
                "input": self.inp
            })


        return resp['output']



# API endpoint for chatbot
@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        url = data['url']
        inp = data['question']
        sage = NoteSage(url, inp)
        response = sage.run()
        return jsonify({
               'url': url,
               'question' : inp,
               'response': response
        })
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        return jsonify({'error': str(e), 'details': error_details}), 500

# Add a basic route for testing
@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Note Sage is running'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')