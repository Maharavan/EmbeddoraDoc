from loader.loader import load_text, load_pdf, load_json
from vector_store.vector_store import create_and_save_vector_db
from embeddings.embed import embed_vector


content = load_pdf('data/input.pdf')

create_and_save_vector_db(content)
while True:
    query = input()
    embed_vector(query)
    



