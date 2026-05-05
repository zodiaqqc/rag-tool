import os
import warnings
from dotenv import load_dotenv

warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai

load_dotenv()

# Need aistudio.google.com api key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_embeddings(text: str):
    try:
        result = genai.embed_content(
            model="models/gemini-embedding-001",
            content=text,
            task_type="retrieval_document"
        )
        return result["embedding"]
    except Exception as e:
        print(f"Ошибка при получении эмбеддингов: {e}")
        return None