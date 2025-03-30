# 📰 News Research Tool 📊

**An AI-powered research tool for analyzing news articles using advanced embeddings and intelligent search capabilities.**

---

## 🚀 Overview
The **News Research Tool** allows users to extract, analyze, and interact with online news articles using state-of-the-art AI models. Simply provide article URLs, and the tool will:

- Load and process the content
- Break it into meaningful text chunks
- Generate embeddings for efficient similarity search
- Answer user queries based on the articles using Mistral AI

With a **visually appealing Streamlit UI**, users can interact with the system seamlessly. 

---

## 🌟 Features

✅ Fetches news content from user-provided URLs 📥  
✅ Splits articles into chunks for better searchability 🔍  
✅ Uses **FAISS** for efficient vector similarity search ⚡  
✅ Generates text embeddings with **Hugging Face MiniLM** 🤖  
✅ Answers user queries using **Mistral AI’s chat model** 🧠  
✅ Sleek, responsive **Streamlit UI** with a custom background 🎨  

---

## 🏗️ How It Works

### 1️⃣ Input News URLs
- Users enter up to **three article URLs** in the sidebar.
- The tool fetches the article content and processes it.

### 2️⃣ Text Processing & Embeddings
- The content is **split into smaller, meaningful text chunks** using **RecursiveCharacterTextSplitter**.
- Each chunk is **converted into an embedding** using **Hugging Face MiniLM**.
- The embeddings are stored in a **FAISS vector database** for fast retrieval.

### 3️⃣ AI-Powered Q&A
- Users type a question related to the news articles.
- The system retrieves the most relevant text chunks using **FAISS**.
- The retrieved content is passed to **Mistral AI**, which generates a human-like response.
- The **sources** used for the answer are also displayed.

---

## 🛠️ Technologies Used

### ⚡ Backend & Processing
- **Python** 🐍 (Core programming language)
- **LangChain** 🏗️ (Framework for AI-powered search & retrieval)
- **FAISS** 🔎 (Fast Approximate Nearest Neighbors search)
- **Hugging Face MiniLM** 🤖 (For generating text embeddings)
- **Mistral AI** 🧠 (LLM for answering queries)
- **UnstructuredURLLoader** 🌐 (For fetching news articles)

### 🎨 UI & Styling
- **Streamlit** 🖥️ (Web app framework)
- **Custom CSS** 🎨 (For styling, including sidebar animations and background effects)

### 🗄️ Storage
- **FAISS Index** 🛢️ (Stores article embeddings for fast retrieval)

---

## 💻 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up API Keys
Create a `.env` file and add your **Mistral API Key**:
```env
MISTRAL_API_KEY=your_api_key_here
```

### 4️⃣ Run the Application
```bash
streamlit run app.py
```

---

## 🌍 Live Demo (Optional)
👉 **[Try it Online](https://8vxiryxuz56z2fzzxhmcie.streamlit.app/)**

---

## 📝 Example Usage
1. **Enter article URLs** in the sidebar.
2. Click **"Process URLs"** to fetch and process content.
3. Type a question in the input box.
4. View the AI-generated answer along with source links.

---

## 🤝 Contributing
Want to improve this tool? Feel free to:
- ⭐ Star the repo
- 🔧 Submit issues & feature requests
- 🛠️ Fork & contribute via PRs

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 🙌 Acknowledgments
Special thanks to:
- **LangChain** for AI-powered retrieval
- **FAISS** for fast similarity search
- **Hugging Face** for open-source embeddings
- **Streamlit** for easy UI development

💡 *Made❤️ by Priyanshu Singh*
