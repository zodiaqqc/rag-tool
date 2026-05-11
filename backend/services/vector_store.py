import chromadb
import os
from backend.services.embeddings import get_query_embeddings

client = chromadb.Client()

collection = client.get_or_create_collection(name="documents")

def add_chunks(chunks, embeddings):
    valid_data = [
        (c, e) for c, e in zip(chunks, embeddings)
        if e is not None and c.strip() != "" and len(c.strip()) > 20
    ]
    if not valid_data:
        print("Добавлять нечего.")
        return
    
    for i, (chunk, emb) in enumerate(valid_data):
        collection.add(
            documents=[chunk],
            embeddings=[emb],
            ids=[f"id_{i}_{os.urandom(2).hex()}"] # Unical ID
        )
        
def search(query: str, n_result=3):
    query_embedding = get_query_embeddings(query)
    
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_result
    )
    return results["documents"][0]