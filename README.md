# YouTube Chatbot
A real-time YouTube chatbot that allows users to ask questions about any YouTube video with available transcripts. Built with Streamlit for the frontend and LangChain for intelligent conversation handling.

## Features

- YouTube URL Processing: Supports various YouTube URL formats (youtube.com, youtu.be, embed links)
- Automatic Transcript Extraction: Fetches video transcripts using YouTube's API
- Intelligent Text Chunking: Breaks down long transcripts into manageable chunks for better processing
- Vector-based Search: Uses FAISS vector store for efficient similarity search
- Context-Aware Conversations: Maintains conversation history and context using LangChain memory
- Real-time Responses: Fast query processing and response generation
- Clean UI: User-friendly Streamlit interface with chat history
- Error Handling: Robust error handling for various edge cases

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Internet connection for YouTube access

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/Prateekk02/youtube-chatbot.git
cd youtube-chatbot
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  
# On Windows: . .venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
```bash
touch .env
# Edit .env and add your OpenAI API key
```

### 5. Run the application
```bash
streamlit run main.py
```

## Requirements
Create a requirements.txt file with the following dependencies:
```bash
streamlit==1.28.0
langchain==0.0.350
openai==1.3.0
faiss-cpu==1.7.4
youtube-transcript-api==0.6.1
tiktoken==0.5.1
python-dotenv==1.0.0
streamlit-chat==0.1.1
pydantic==2.5.0
numpy==1.24.3
pandas==2.0.3
```

## Configuration
```
OPENAI_API_KEY= your openai api key
PINECONE_API_KEY= your pinecode api key 
PINECONE_ENV= your pinecone environment
VECTOR_DB_INDEX= "youtube-chatbot"
GOOGLE_API_KEY= your google api key
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
```

## Project Structure
```
youtube-chatbot/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── main.py                 # Streamlit app entry 
├── config/
│   ├── __init__.py
│   └── settings.py         # Configuration 
├── src/
│   ├── __init__.py
│   ├── youtube/
│   │   ├── __init__.py
│   │   ├── extractor.py    # URL parsing and video 
│   │   └── transcript.py   # Transcript fetching and processing
│   ├── processing/
│   │   ├── __init__.py
│   │   ├── chunker.py      # Text chunking 
│   │   └── vectorstore.py  # Vector database 
│   ├── chatbot/
│   │   ├── __init__.py
│   │   ├── chain.py        # LangChain QA chain 
│   │   └── memory.py       # Conversation memory 
│   └── utils/
│       ├── __init__.py
│       ├── helpers.py      # Utility functions
│       └── exceptions.py   # Custom exception 
├── tests/
│   ├── __init__.py
│   ├── test_youtube.py
│   ├── test_processing.py
│   └── test_chatbot.py
|__docs/
    |__architecture.md

```
## How It Works

- URL Processing: Extract video ID from various YouTube URL formats
- Transcript Extraction: Fetch video transcript using YouTube Transcript API
- Text Chunking: Split transcript into overlapping chunks for better context
- Embedding Generation: Create vector embeddings using OpenAI's embedding model
- Vector Storage: Store embeddings in FAISS vector database
- Query Processing: Convert user questions to embeddings and find relevant chunks
- Response Generation: Use LangChain to generate contextual responses
- Memory Management: Maintain conversation history for context-aware responses