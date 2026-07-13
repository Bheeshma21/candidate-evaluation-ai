# 🧠 Candidate Evaluation AI

An AI-powered recruitment platform that helps automate candidate screening, resume evaluation, technical assessment, and recruiter decision-making using Generative AI, Retrieval-Augmented Generation (RAG), and FastAPI.

---

## 🚀 Overview

Candidate Evaluation AI streamlines the hiring process by combining Large Language Models (LLMs), semantic search, and intelligent candidate evaluation into a single platform. Recruiters can upload resumes, compare candidates against job descriptions, generate AI-powered insights, and make faster, data-driven hiring decisions.

---

## ✨ Features

- 📄 Resume Upload (PDF/DOCX)
- 🤖 AI-Powered Resume Analysis
- 🎯 Resume vs Job Description Matching
- 🧠 Gemini Embeddings for Semantic Search
- 📚 RAG-based Knowledge Retrieval
- 📊 Candidate Scoring System
- 💬 AI Recruiter Assistant
- 📑 Detailed Candidate Evaluation Reports
- 🔍 Semantic Resume Search
- 🔐 Authentication System
- 📧 Email Notifications
- ⚡ FastAPI REST APIs

---

## 🛠️ Tech Stack

### Backend

- Python
- FastAPI
- SQLAlchemy
- SQLite

### AI & Machine Learning

- Google Gemini
- Google GenAI SDK
- ChromaDB
- Retrieval-Augmented Generation (RAG)

### Frontend

- HTML
- CSS
- JavaScript

---

## 📂 Project Structure

```text
candidate-evaluation-ai/
│
├── backend/
│   ├── auth/
│   ├── rag/
│   ├── routes/
│   ├── models/
│   ├── services/
│   ├── static/
│   ├── templates/
│   ├── uploads/
│   ├── main.py
│   └── requirements.txt
│
├── README.md
├── LICENSE
└── .gitignore
```

---

## ⚙️ Installation

```bash
git clone https://github.com/<your-username>/candidate-evaluation-ai.git

cd candidate-evaluation-ai/backend

python -m venv .venv
```

### Windows

```powershell
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file inside the `backend` directory.

```env
GOOGLE_API_KEY=your_google_api_key

GROQ_API_KEY=your_groq_api_key

SECRET_KEY=your_secret_key

DATABASE_URL=sqlite:///candidate.db
```

---

## ▶️ Run the Application

```bash
python -m rag.index_documents
```

```bash
uvicorn main:app --reload
```

---

## 🌐 Deployment

The project is designed to be deployed on platforms such as:

- Render
- Railway
- Azure App Service
- AWS EC2

---

## 📌 Future Improvements

- Multi-Agent Candidate Evaluation
- Voice-Based AI Interviews
- ATS Compatibility Scoring
- Live Coding Interview Module
- Recruiter Analytics Dashboard
- Interview Scheduling
- Calendar Integration

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Open a Pull Request.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Bheeshma Reddy**

- AI Engineer
- Machine Learning Enthusiast
- Generative AI & RAG Developer

GitHub: https://github.com/<your-username>

LinkedIn: https://linkedin.com/in/<your-linkedin>

---

⭐ If you find this project useful, consider giving it a star!
