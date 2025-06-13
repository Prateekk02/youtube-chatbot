from __future__ import annotations

from typing import Sequence
from pathlib import Path

from dotenv import load_dotenv
load_dotenv()

from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec
from config.settings import settings
from langchain.schema import Document

class VectorStore:
    """
    Thin wrapper around PineconeVectorStore that hides connection
    boilerplate and offers helper methods add_texts() and as_retriever().
    """
        
    def __init__(self):
        if settings.VECTOR_DB_INDEX is None: 
            raise ValueError("VECTOR_DB_INDEX missing in settings.")
        self._pc = Pinecone(api_key=settings.PINECONE_API_KEY)
        
        # Creating index on first run 
        if not self._pc.list_indexes().get(settings.VECTOR_DB_INDEX):
            self._pc.create_index(
                name=settings.VECTOR_DB_INDEX,
                dimension=1536, 
                metric='cosine',
                spec=ServerlessSpec(cloud="aws", region="us-east-1")
            )  
            
            index = self._pc.Index(settings.VECTOR_DB_INDEX)
            embeddings = OpenAIEmbeddings()
            
            self._store = PineconeVectorStore(
                index=index,
                embedding=embeddings,                
            )
            
    def add_text(self, texts, metadatas= None):
        self._store.add_texts(texts, metadatas=metadatas)
        
    def as_retriever(self):
        return self._store.as_retriever()
