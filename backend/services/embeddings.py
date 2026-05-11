import os
import warnings
from dotenv import load_dotenv

warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai

load_dotenv()

# Need aistudio.google.com api key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

EMBED_MODEL = "models/gemini-embedding-001"

def get_embeddings(text: str):
    try:
        result = genai.embed_content(
            model=EMBED_MODEL,
            content=text,
            task_type="retrieval_document"
        )
        return result["embedding"]
    except Exception as e:
        print(f"Ошибка при получении эмбеддингов: {e}")
        return None
    
def get_query_embeddings(text: str):
    try:
        result = genai.embed_content(
            model=EMBED_MODEL,
            content=text,
            task_type="retrieval_query"
        )
        return result["embedding"]
    except Exception as e:
        print(f"Ошибка при получении эмбеддингов: {e}")
        return None
    
