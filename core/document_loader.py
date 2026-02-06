import pdfplumber
import docx

def load_text(file):
    if file.name.endswith(".pdf"):
        return extract_pdf(file)
    elif file.name.endswith(".docx"):
        return extract_docx(file)
    else:
        return file.read().decode("utf-8")

def extract_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_docx(file):
    doc = docx.Document(file)
    return "\n".join(p.text for p in doc.paragraphs)
