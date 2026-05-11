from fastapi import APIRouter, UploadFile, File
from backend.services.file_parser import txt_parser, pdf_parser, docx_parser
from backend.services.chunker import chunk_text
from backend.services.embeddings import get_embeddings
from backend.services.vector_store import add_chunks, search
from backend.services.llm import generate_answer

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    content = await file.read()
    
    filename = file.filename.lower()
    
    if filename.endswith(".txt"):
        text = txt_parser(content)
    
    elif filename.endswith(".pdf"):
        text = pdf_parser(content)
    
    elif filename.endswith(".docx"):
        text = docx_parser(content)
    
    else:
        return {"error": "Unsupported file type"}
    
    chunks = chunk_text(text)
    
    embeddings = [get_embeddings(chunk) for chunk in chunks]
    
    add_chunks(chunks, embeddings)
    
    return {
        "filename": file.filename,
        "text_preview": text[:500],
        "first_chunk": chunks[0] if chunks else "",
        "chunks": len(chunks),
        "stored": True
    }
    
@router.post("/query")
async def query(q: str):
    result = search(q)
    return {"result": result}

@router.post("/ask")
async def ask(q: str):
    chunks = search(q)
    
    if not chunks:
        return {"answer": "no info"}
    
    answer = generate_answer(q, chunks)
    
    return {
        "answer": answer,
        "chunks_used": chunks
    }