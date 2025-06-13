from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain   # ← missing in original
from .memory import get_memory
from ..processing.vectorstore import VectorStore


def build_chain(vstore: VectorStore):
    """Return a Conversational RAG chain wired to the supplied vector store."""
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.2,
        streaming=True,
    )
    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vstore.as_retriever(),
        memory=get_memory(),
    )
