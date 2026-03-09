![ShopAssist Banner](banner.png)

<div align="center">

# ShopAssist 🤖

**An AI-powered e-commerce FAQ chatbot built with Streamlit, LangChain, and FAISS**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?logo=langchain&logoColor=white)](https://www.langchain.com/)
[![FAISS](https://img.shields.io/badge/FAISS-Meta%20AI-0064e0)](https://github.com/facebookresearch/faiss)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

## 📖 Overview

**ShopAssist** is an intelligent FAQ assistant designed for e-commerce platforms. It leverages semantic vector search to understand the *intent* behind customer questions — not just keywords — and returns the most relevant answer from your knowledge base instantly. No external API keys are required; the embedding model runs entirely locally.

---

## 📑 Table of Contents

- [Features](#-features)
- [Demo](#-demo)
- [Tech Stack](#-tech-stack)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Customisation](#-customisation)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

| Feature | Description |
|---|---|
| **Semantic Search** | Uses HuggingFace `all-MiniLM-L6-v2` embeddings to match questions by meaning, not just exact wording. |
| **Instant Answers** | FAISS vector index provides sub-second retrieval from your FAQ knowledge base. |
| **Smart Suggestions** | Surfaces three random FAQ suggestions on load to help users get started quickly. |
| **Conversational UI** | Clean, chat-style interface built with Streamlit's native `st.chat_message` components. |
| **Session History** | Preserves the full conversation within a browser session. |
| **Fully Local** | All embeddings are generated on-device — no OpenAI key or external API required. |
| **Easy to Extend** | Add new FAQs to a single JSON file; the vector index rebuilds automatically on next launch. |

---

## 🎬 Demo

> Start the app and navigate to **http://localhost:8501** in your browser.

```
User   ▶  What is your return policy?
Bot    ▶  You can return items within 30 days of receipt...

User   ▶  How do I track my order?
Bot    ▶  Once your order ships you will receive a tracking link...
```

---

## 🔧 Tech Stack

| Technology | Role |
|---|---|
| [Python 3.8+](https://www.python.org/) | Core language |
| [Streamlit](https://streamlit.io/) | Web UI framework |
| [LangChain](https://www.langchain.com/) | LLM application framework |
| [HuggingFace Embeddings](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) | Semantic text embeddings (`all-MiniLM-L6-v2`) |
| [FAISS](https://github.com/facebookresearch/faiss) | High-performance vector similarity search |

---

## 📋 Prerequisites

- Python **3.8** or higher
- `pip` package manager
- (Optional but recommended) a Python virtual environment tool (`venv`, `conda`, etc.)

---

## 🛠️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/muhammad-asif10/Shop_Assist.git
   cd Shop_Assist
   ```

2. **Create and activate a virtual environment** *(recommended)*

   ```bash
   python -m venv venv

   # Windows
   .\venv\Scripts\activate

   # macOS / Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🏃 Usage

1. **Prepare your knowledge base**

   Ensure `FAQ's.json` exists in the project root and follows the schema below:

   ```json
   {
     "questions": [
       {
         "question": "What is your return policy?",
         "answer": "You can return items within 30 days of receipt."
       },
       {
         "question": "How do I track my order?",
         "answer": "Once your order ships you will receive a tracking link via email."
       }
     ]
   }
   ```

2. **Launch the application**

   ```bash
   streamlit run ShopAssist.py
   ```

3. **Interact with the chatbot**

   - Open your browser at **http://localhost:8501**.
   - Click one of the suggested questions to auto-fill the input, or type your own question in the chat bar.
   - ShopAssist will return the most semantically relevant answer from your FAQ dataset.

---

## 📂 Project Structure

```
Shop_Assist/
├── ShopAssist.py       # Main Streamlit application
├── FAQ's.json          # FAQ knowledge base (questions & answers)
├── banner.png          # Header banner image
├── requirements.txt    # Python package dependencies
├── LICENSE             # MIT License
└── README.md           # Project documentation
```

---

## ⚙️ Customisation

- **Add or edit FAQs** — Modify `FAQ's.json` and restart the app. The vector index is rebuilt automatically (cached per session via `@st.cache_resource`).
- **Change the embedding model** — Swap `all-MiniLM-L6-v2` in `ShopAssist.py` for any other [Sentence Transformers](https://www.sbert.net/docs/pretrained_models.html) model to tune the trade-off between speed and accuracy.
- **Adjust retrieval depth** — Change `k=1` in the `similarity_search` call to return multiple candidate answers and implement your own ranking logic.
- **Style the UI** — Use Streamlit's [theming](https://docs.streamlit.io/library/advanced-features/theming) options (`~/.streamlit/config.toml`) to match your brand colours.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature-name`.
3. Commit your changes with clear messages: `git commit -m "feat: add your feature"`.
4. Push to your fork: `git push origin feature/your-feature-name`.
5. Open a Pull Request describing your changes.

Please ensure your code is clean and well-commented before submitting.

---

## 📝 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.
