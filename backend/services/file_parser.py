from pypdf import PdfReader
import docx
from io import BytesIO

def txt_parser(content: bytes):
    return content.decode("utf-8", errors="ignore")

def pdf_parser(content: bytes):
    reader = PdfReader(BytesIO(content))
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
        
    return text

def docx_parser(content: bytes):
    doc = docx.Document(BytesIO(content))
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    text = "\n".join(full_text)
    return text