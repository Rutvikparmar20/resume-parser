import pdfplumber
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    text = ''
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def parse_resume(text):
    doc = nlp(text)
    name = doc.ents[0].text if doc.ents else "Unknown"
    return {
        'name': name,
        'skills': 'Python, Flask',
        'education': 'B.Tech'
    }
