import streamlit as st
from src.youtube.extractor import get_video_id
from src.youtube.transcript import get_transcript
from src.processing.chunker import chunker
from src.processing.vectorstore import VectorStore
from src.chatbot.chain import build_chain

# st.set_page_config(page_title="YouTube Chatbot", page_icon="🎥", layout="wide")
# st.markdown("<style>" + open("assets/styles.css").read() + "</style>", unsafe_allow_html=True)
st.title("YouTube Video Chatbot")

if "chat_chain" not in st.session_state:
    st.session_state.chat_chain = None

url = st.text_input("Paste a YouTube URL and press Enter", placeholder="https://...", key="yt_url")
if url and st.button("Load video"):
    with st.spinner("Indexing video..."):      
        vid = get_video_id(url)
        transcript = get_transcript(url)
        chunks = chunker(transcript)
        vs = VectorStore()
        vs.add_text(chunks, metadatas=[{"source": vid}] * len(chunks))
        st.session_state.chat_chain = build_chain(vs)
        st.success("Ready! Ask anything about the video ⤵")

if st.session_state.chat_chain:
    user_q = st.chat_input("Ask a question")
    if user_q:
        with st.spinner("Thinking..."):
            resp = st.session_state.chat_chain({"question": user_q})
            st.chat_message("assistant").markdown(resp["answer"])
