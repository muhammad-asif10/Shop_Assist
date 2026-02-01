import streamlit as st
import json
import os
import random
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Data loading
def load_faq_dats(filepath):
    """Loads the FAQ data from your specific JSON structure."""
    with open(filepath, 'r') as f:
        data = json.load(f)
        return data['questions']
    
# Vector database engine
@st.cache_resource
def initialize_vector_db():
    """Converts the JSON questions into a searchable vector database."""
    # Load the dataset
    faq_list = load_faq_dats("FAQ's.json")

    #Format data for search engine
    # We combine Q and A into one string for better context matching
    documents = [f"Question: {item['question']} \nAnswer: {item['answer']}" for item in faq_list]

    #Use a high-quality local embedding model
    embiddings = HuggingFaceEmbeddings(model_name = "all-MiniLM-L6-v2")
    # Build the FAISS index (The 'Brain' of the search)
    vector_db = FAISS.from_texts(documents, embiddings)
    return vector_db

#UI
st.set_page_config(page_title="ShopAssist", page_icon='🤖')
st.title("ShopAssist")
st.markdown("Your E-commerce Assistant for answering Frequently Asked Questions (FAQs)")

#initialize the search engine
vector_db = initialize_vector_db()

#inttialize chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

    #display previous chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Helper to process input
def process_input(prompt):
    # add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    #search for most relavent answar
    # k=1 returns the single best match from your dataset
    search_results = vector_db.similarity_search(prompt, k=1)

    if search_results:
        # Extract the answer part from the document string
        raw_result = search_results[0].page_content
        answer = raw_result.split("Answer:")[1]
    else:
        answer = "I'm sorry, I couldn't find information regarding that. Please contact support."

    # display assistant response
    with st.chat_message("assistant"):
        st.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})

# Suggestions
questions = [q['question'] for q in load_faq_dats("FAQ's.json")]
if questions:
    # Pick 3 random questions
    suggestions = random.sample(questions, min(3, len(questions)))
    
    st.markdown("#### Suggested Questions:")
    cols = st.columns(len(suggestions))
    for i, suggestion in enumerate(suggestions):
        if cols[i].button(suggestion, key=f"suggestion_{i}"):
            process_input(suggestion)

# user input handling
if prompt := st.chat_input('How can I help you today?'):
    process_input(prompt)