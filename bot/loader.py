from pypdf import PdfReader
import json

json_content = []

def load_text(text_file):
    with open(text_file,'r',encoding='utf-8',errors='ignore') as file:
        content = file.read()

    return content

def load_json(json_file):
    try:
        with open(json_file,'r',encoding='utf-8') as file:
            data = json.load(file)
        
            
        flatten(data,"")
        return " ".join(json_content)
    except json.JSONDecodeError as e:
        return f"Error while loading json {e}"

def flatten(data,par_key):
    
    
    if isinstance(data,dict):
        for key,val in data.items():
            new_key = f"{par_key}_{key}" if par_key else key
            flatten(val,new_key)
    elif isinstance(data,list):
        for ind,val in enumerate(data):
            new_key = f"{par_key}_{ind}" if par_key else str(ind)
            flatten(val,new_key)
    else:
        json_content.append(f"{par_key} : {data}")

def load_pdf(pdf_file):
    try:
        content = PdfReader(pdf_file)

        return "\n".join(pages.extract_text() or "" for pages in content.pages)
    except Exception as e:
        return f"Error while loading pdf {e}"
