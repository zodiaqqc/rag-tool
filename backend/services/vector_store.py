import chromadb
import os

client = chromadb.Client()

collection = client.get_or_create_collection(name="documents")

def add_chunks(chunks, embeddings):
    valid_data = [(c, e) for c, e in zip(chunks, embeddings) if e is not None]
    if not valid_data:
        print("Добавлять нечего.")
        return
    
    for i, (chunk, emb) in enumerate(zip(chunks, embeddings)):
        collection.add(
            documents=[chunk],
            embeddings=[emb],
            ids=[f"id_{i}_{os.urandom(2).hex()}"] # Unical ID
        )
        
def search(query_embeddings, n_result=3):
    results = collection.query(
        query_embeddings=[query_embeddings],
        n_results=n_result
    )
    return results["documents"][0]