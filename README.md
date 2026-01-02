<p align="center">
  <img src="assets/logo.png" alt="EmbeddoraDoc Logo" width="120"/>
</p>

<h1 align="center">EmbeddoraDoc 🧠🤖</h1>
<p align="center">
  <b>Hybrid Retrieval-Augmented Document Intelligence Assistant</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/RAG-Embeddings%20%2B%20BM25-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Framework-Streamlit-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Vector%20Store-FAISS-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/LLM-GPT4o–mini-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" />
</p>

<p align="center">
  <a href="https://github.com/Maharavan/EmbeddoraDoc/stargazers">
    <img src="https://img.shields.io/github/stars/Maharavan/EmbeddoraDoc?style=social" />
  </a>
  <a href="https://github.com/Maharavan/EmbeddoraDoc/forks">
    <img src="https://img.shields.io/github/forks/Maharavan/EmbeddoraDoc?style=social" />
  </a>
</p>

---

## 🚀 Overview

**EmbeddoraDoc** is a **session-aware Retrieval-Augmented Generation (RAG) assistant** that enables users to upload documents (**PDF / TXT / JSON**) and interact with them conversationally.

Unlike basic vector-only RAG systems, EmbeddoraDoc employs a **hybrid retrieval pipeline** that combines semantic embeddings, keyword-based search, and cross-encoder reranking to deliver **accurate, context-grounded answers with reduced hallucinations**.

---

## 🧠 Why EmbeddoraDoc?

Traditional RAG implementations often:
- Miss exact terms such as IDs or error codes
- Retrieve semantically similar but irrelevant chunks
- Hallucinate when context is insufficient

**EmbeddoraDoc addresses these limitations by design.**

### 🔬 Hybrid Retrieval Pipeline

```
FAISS (Semantic Recall)
      +
BM25 (Keyword Precision)
      ↓
Cross-Encoder Reranking
      ↓
Hallucination-Guarded Answering
```

---

## ✨ Features

| Feature | Description |
|------|------------|
| 📂 Session Isolation | Independent document index per session |
| 🔍 Hybrid Retrieval | FAISS + BM25 |
| 🧠 Reranking | `ms-marco-MiniLM-L-6-v2` |
| 🛡 Hallucination Guard | Context-validated answers |
| 🗂 File Support | PDF, TXT, JSON |
| 💾 Local Cache | Persistent FAISS + BM25 |
| 🧩 Modular Codebase | Easy to extend and customize |

---

## 🏗 Architecture

```
User
 ↓
Streamlit UI
 ↓
Loader & Chunker
 ↓
Hybrid Retrieval Engine
  ├─ FAISS
  ├─ BM25
  └─ Cross-Encoder
 ↓
LLM (Answer + Validation)
```

---

## 📁 Project Structure

```
EmbeddoraDoc/
│── app/
│   ├── main.py
│   ├── components/
│   └── utility/
│── loader/
│── vector_store/
│── embeddings/
│── assets/
│   └── logo.png
│── assets/screenshots/
│── data/
│── LICENSE
│── README.md
│── requirements.txt
```

---

## ⚙️ Installation & Run (Local)

### 1️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / Mac
.venv\Scripts\activate     # Windows
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
streamlit run app/main.py
```

Open 👉 **http://localhost:8501**

---

## 📦 requirements.txt (Dependency Overview)

| Package | Purpose |
|------|--------|
| streamlit | Web UI framework |
| langchain-core | Core LangChain abstractions |
| langchain-openai | OpenAI LLM & embeddings |
| langchain-community | Community integrations |
| langchain-text-splitters | Recursive text chunking |
| rank-bm25 | Keyword-based retrieval |
| sentence-transformers | Cross-encoder reranking |
| faiss-cpu | Vector similarity search |
| python-dotenv | Environment variable loading |
| reportlab | PDF processing |
| pillow | Image handling |

---

## 🚀 Deployment (Docker-Based)

```bash
docker build -t embeddoradoc:latest .
```

```bash
docker run -p 8501:8501 \
  -e OPENAI_API_KEY=your_openai_key_here \
  embeddoradoc:latest
```

---

## ☁️ Cloud Deployment

#### 🟢 Deployed on Render using Docker
- Automatic build & deployment from GitHub
- Secrets managed via environment variables
- Public HTTPS endpoint for access

---
## UI Design

<p align="center">
<img src="assets/screenshots/home.png" width=100%>
</p>

---

## 📜 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---

⭐ **Star the repository if you find this project useful!**
