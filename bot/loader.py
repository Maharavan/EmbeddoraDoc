from pypdf import PdfReader
import json
from flatten_json import flatten

def load_text(text_file):
    with open(text_file,'r',encoding='utf-8') as file:
        content = file.read()

    return content

def load_json(json_file):
    try:
        with open(json_file,'r', encoding='utf-8') as file:
            data  = json.load(file)
        content = flatten(data)
        return content
    except json.JSONDecodeError as e:
        return f"Error while loading json {e}"

def load_pdf(pdf_file):
    try:
        content = PdfReader(pdf_file)

        return "\n".join(pages.extract_text() or "" for pages in content.pages )
    except Exception as e:
        return f"Error while loading pdf {e}"
