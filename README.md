![Bot Banner](banner.png)

# FAQ's Chatbot 🤖

A smart, AI-powered FAQ chatbot built with Streamlit, LangChain, and FAISS. This application allows users to query a knowledge base of Frequently Asked Questions using natural language and receive relevant answers instantly.

## 🚀 Features

-   **Natural Language Search**: Uses advanced vector embeddings (HuggingFace) to understand the semantic meaning of user queries, not just keyword matching.
-   **Interactive UI**: Built with Streamlit for a clean, chat-like interface.
-   **Smart Suggestions**: Randomly suggests questions from your dataset to help users get started.
-   **Efficient Retrieval**: Powered by FAISS (Facebook AI Similarity Search) for fast and accurate answer retrieval.
-   **Conversation History**: Maintains context within the chat session.

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
-   Python 3.8 or higher
-   pip (Python package manager)

## 🛠️ Installation

1.  **Clone the repository** (if applicable) or navigate to your project folder:
    ```bash
    cd "path/to/FAQ's Chatbot"
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    
    # On Windows:
    .\venv\Scripts\activate
    
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## 🏃 Usage

1.  **Prepare your Data**:
    Ensure you have a file named `FAQ's.json` in the root directory. It should follow this structure:
    ```json
    {
      "questions": [
        {
          "question": "What is your return policy?",
          "answer": "You can return items within 30 days of receipt."
        },
        ...
      ]
    }
    ```

2.  **Run the Application**:
    ```bash
    streamlit run ShopAssist.py
    ```

3.  **Interact**:
    -   Open your browser (usually at `http://localhost:8501`).
    -   Click on a suggested question or type your own query in the chat bar.

## 📂 Project Structure

```
FAQ's Chatbot/
├── ShopAssist.py          # Main application script
├── FAQ's.json          # Knowledge base data file
├── banner.png          # banner image
├── requirements.txt    # Python dependencies
├── LICENSE             #project license
└── README.md           # Project documentation
```

## 🔧 Technologies Used

-   [Streamlit](https://streamlit.io/) - The web framework for the UI.
-   [LangChain](https://www.langchain.com/) - Framework for developing applications powered by language models.
-   [HuggingFace Embeddings](https://huggingface.co/models) - For generating semantic vector embeddings (`all-MiniLM-L6-v2`).
-   [FAISS](https://github.com/facebookresearch/faiss) - Efficient similarity search and clustering of dense vectors.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
