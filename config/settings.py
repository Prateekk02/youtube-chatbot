# config/settings.py

import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env file
BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_path = BASE_DIR / ".env"
load_dotenv(dotenv_path)

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    PINECONE_ENV = os.getenv("PINECONE_ENV")
    VECTOR_DB_INDEX = os.getenv("VECTOR_DB_INDEX")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    # Optional fallback/defaults
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

settings = Settings()
