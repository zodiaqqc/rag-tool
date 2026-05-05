from fastapi import APIRouter, UploadFile, File
from backend.services.file_parser import txt_parser, pdf_parser, docx_parser
from backend.services.chunker import chunk_text

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
        return {"error": "unsupported file type"}
    
    chunks = chunk_text(text)
    
    return {
        "filename": file.filename,
        "text_preview": text[:500],
        "first_chunk": chunks[0] if chunks else ""
    }
