"""
Conversation memory helpers.

The module exposes a single factory function `get_memory()` so the rest of the
application (Streamlit UI, tests, background jobs) can obtain a ready-to-use
LangChain memory object without importing LangChain internals everywhere.
"""

from __future__ import annotations
from langchain.memory import ConversationBufferMemory


def get_memory() -> ConversationBufferMemory:
    """
    Return a `ConversationBufferMemory` that stores the full chat history and
    hands it back to the LLM on every call.

    • return_messages=True  → provides structured `AIMessage` / `HumanMessage`
                              objects rather than raw strings.
    • memory_key="chat_history"  → matches the default expected by
      `ConversationalRetrievalChain`.
    • input_key="question"  → the key your Streamlit app sends to the chain.

    You can swap this implementation for a more advanced one (e.g. Redis,
    PGVector, or summarising memory) without touching the Streamlit layer.
    """
    return ConversationBufferMemory(
        return_messages=True,
        memory_key="chat_history",
        input_key="question",
    )
