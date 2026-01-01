# 📚 EmbeddoraDoc

EmbeddoraDoc is a **Streamlit-powered, Retrieval-Augmented Generation (RAG) assistant** for your personal documents.  
Upload PDFs/JSON/TXT files, ask questions conversationally, and get precise answers grounded in your own data.

It uses a **Hybrid Retrieval Pipeline**:
FAISS (embeddings) + BM25 (keyword search) → Cross-Encoder reranking → Hallucination-checked final answer.

---

## ✨ Features

- 🗂 Per-session uploads — each chat stores its own docs & index
- 🔍 Hybrid search:
  - FAISS (OpenAI embeddings)
  - BM25 for keyword-based matching
- 🧠 Cross-encoder reranking (`ms-marco-MiniLM-L-6-v2`)
- 🛡 Hallucination guard — validates answers against context
- 🖥 Streamlit chat UI with history
- 📎 Sidebar tools:
  - Upload/manage files
  - Rename/delete/switch sessions
  - Export chat to PDF
- 🧩 Modular code structure for extendability

---

## 🏗 Project Layout

```
embeddoradoc/
│── app/main.py               # Streamlit entrypoint
│── app/components/           # Chat UI, uploader, session UI components
│── app/utility/              # File helpers, CSS injector, exporters
│── loader/loader.py          # PDF/JSON/TXT loaders + metadata tagging
│── vector_store/vector_store.py  # Chunking + FAISS + BM25 indexing
│── embeddings/embed.py       # Hybrid RAG + rerank + hallucination check
│── assets/                   # Icons, logos
│── data/                     # Sample docs for demo
│── faiss_index/              # Auto-generated FAISS DB
│── bm25_store.pkl            # BM25 cache file
│── .env                      # OpenAI key
```

---

## 🔧 Requirements

- Python **3.10+**
- Environment variable: `OPENAI_API_KEY`
- Install dependencies:

```bash
pip install streamlit langchain_openai langchain_community langchain-core rank-bm25 sentence-transformers faiss-cpu reportlab pillow python-dotenv
```

---

## 🚀 Run the App

```bash
streamlit run app/main.py
```

---

## 🧠 How It Works

### 🔹 Upload Document  
Supported: **PDF / TXT / JSON**

Documents are chunked (500 chars, overlap=50) → embedded → indexed.

### 🔹 Query Flow
1. Retrieve using **FAISS (top 10)** + **BM25 (top 10)**
2. Deduplicate & rerank using **cross-encoder**
3. Send top 3 chunks to **GPT-4o-mini**
4. Hallucination guard validates answer
5. Response returned to UI

---

## 🔥 Tips

- Delete `faiss_index/` + `bm25_store.pkl` to rebuild a clean DB
- Place sample docs inside `/data`
- Keep `.env` secret (in `.gitignore`)
- Extend support for more formats via `loader/loader.py`

---

## 📜 License
MIT — free for personal/commercial use.

---

### ❤️ Contribution Welcome

Suggest features or request enhancements!
