from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document     
from config.settings import settings                                                     

if settings.CHUNK_SIZE is None or settings.CHUNK_OVERLAP is None:
    raise ValueError("CHUNK_SIZE or CHUNK_OVERLAP missing from settings.") 

def chunker(
    transcript: str,
    chunk_size: int = int(settings.CHUNK_SIZE),
    chunk_overlap: int = int(settings.CHUNK_OVERLAP),
) -> List[Document]:
    """
    Split a full transcript into overlapping character-level chunks.

    Returns a list of `langchain.docstore.document.Document` objects so they
    can be ingested directly by the vector store.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    
    return splitter.create_documents([transcript])
