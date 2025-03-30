import os
import streamlit as st
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_mistralai.chat_models import ChatMistralAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Ensure Mistral API key is set
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
if not MISTRAL_API_KEY:
    st.error("❌ Mistral API Key is missing. Please set it in your `.env` file.")
    st.stop()

# ✅ Add full-page background image
st.markdown(
    """
    <style>
    body {
        background: url("bg.jpg") no-repeat center center fixed;
        background-size: cover;
    }
    [data-testid="stAppViewContainer"] {
        background: transparent;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Apply custom styling
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        transition: all 0.5s ease-in-out;
        background: linear-gradient(135deg, rgba(50,50,50,0.8), rgba(20,20,20,0.9));
        box-shadow: inset 0 0 15px rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }
    .main-container {
        background: url("bg.jpg") no-repeat center center/cover;
        backdrop-filter: blur(10px);
        box-shadow: 0px 4px 15px rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 15px;
        position: relative;
    }
    .stButton > button {
        background: linear-gradient(135deg, #ff416c, #ff4b2b);
        color: white;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px 20px;
        transition: 0.3s;
    }
    .stButton > button:hover {
        box-shadow: 0px 0px 15px rgba(255, 65, 108, 0.8);
        transform: scale(1.05);
    }
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.1);
        color: white;
        border: none;
        border-bottom: 2px solid rgba(255, 65, 108, 0.5);
        transition: 0.3s;
    }
    .stTextInput > div > div > input:focus {
        border-bottom: 2px solid rgba(255, 65, 108, 1);
        box-shadow: 0px 0px 10px rgba(255, 65, 108, 0.8);
    }
    .signature {
        position: fixed;
        bottom: 10px;
        right: 10px;
        font-size: 12px;
        font-family: cursive;
        color: rgba(255, 255, 255, 0.6);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📰 News Research Tool 📊")
st.sidebar.title("🔎 News Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"🌐 URL {i+1}")
    if url:
        urls.append(url)

process_clicked = st.sidebar.button("🚀 Process URLs")
query = st.text_input("❓ Ask about the articles")
vector_index_path = "faiss_index"

if process_clicked and urls:
    try:
        st.sidebar.text("📥 Loading articles...")
        loaders = UnstructuredURLLoader(urls)
        docs = loaders.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        split_docs = text_splitter.split_documents(docs)

        st.sidebar.text("🔎 Generating embeddings...")
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vector_index = FAISS.from_documents(split_docs, embeddings)
        vector_index.save_local(vector_index_path)

        st.sidebar.success("✅ Processing complete!")
    except Exception as e:
        st.sidebar.error(f"❌ Error: {e}")

if query:
    try:
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vectorstore = FAISS.load_local(vector_index_path, embeddings, allow_dangerous_deserialization=True)

        retriever = vectorstore.as_retriever()
        model = ChatMistralAI(api_key=MISTRAL_API_KEY)  # ✅ Ensure API key is passed correctly
        qa_chain = RetrievalQAWithSourcesChain.from_chain_type(llm=model, retriever=retriever)

        result = qa_chain({"question": query})
        st.subheader("Answer:")
        st.write(result["answer"])

        if result.get("sources"):
            st.subheader("Sources:")
            for source in result["sources"].split("\n"):
                st.markdown(f"[🔗 {source}]({source})")
    except Exception as e:
        st.error(f"❌ Error: {e}")

st.markdown("<p class='signature'>Made by : Priyanshu Singh</p>", unsafe_allow_html=True)
