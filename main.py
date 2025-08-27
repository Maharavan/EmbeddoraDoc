from bot.loader import load_text, load_pdf, load_json

from embeddings.embed import embed_vector

content = load_pdf('data/input.pdf')
embed_vector(content)



