from bot.loader import load_text, load_pdf, load_json
# import chainlit as cl
from embeddings.embed import embed_vector, create_and_save_vector_db


content = load_pdf('data/input.pdf')

create_and_save_vector_db(content)
while True:
    query = input()
    embed_vector(query)
    



