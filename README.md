# 🤖 Universal AI Utility App

> **Multi-Task AI Application** | Prompt Routing | Streamlit + OpenAI and Gemini

![Python](https://img.shields.io/badge/Python-3.10+-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-blue)
![OpenAI](https://img.shields.io/badge/Google-gemini--2.5--flash-purple)

---

## 🚀 Live Demo : 

> https://universal-ai-utility.streamlit.app/

---

## 📌 About

A multi-task AI application that performs 5 different NLP tasks 
through a single unified interface — built using prompt routing architecture.

> One UI → Multiple Prompts → Different Outputs

---

## ✨ Current Features

- 5 AI Tasks — Summarize, Translate, Explain, Generate Email, Rewrite
- Two LLMs models — OpenAI, Google-Gemini 
- Prompt Routing — routes to correct prompt based on selected task
- Prompt Transparency — shows constructed prompt before output
- Input Validation — handles empty inputs gracefully
- Clean modular architecture — UI / Prompts / Backend separated

---

## 🗂️ Project Structure
```
universal_ai_app/
├── app.py            # Streamlit UI
├── backend_google.py        # Gemini API call
├── backend_openai.py        # OpenAI API call
├── prompts.py        # Prompt builder
├── README.md
└── requirements.txt
```
---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Frontend UI |
| OpenAI API (gpt-4o-mini) | LLM_1 |
| Gemini API (gemini-2.5-lflash) | LLM_2 |

---

## 🚀 Run Locally

```bash
git clone https://github.com/Abhishek-369V/universal-ai-utility.git
cd universal-ai-utility
pip install -r requirements.txt
```

Create `.streamlit/secrets.toml`:
```toml
OPENAI_API_KEY = "your-openai-key-here"
GOOGLE_API_KEY = "your-gemini-key-here"
```

```bash
streamlit run app.py
```

---

## 🔮 Upcoming Features

- [X] ~~Gemini Flash as alternative LLM~~
- [ ] Chat with PDF using RAG + LangChain
- [ ] Add chat history tracking for "chat with pdf"(using RAG)
- [X] ~~Download output button~~

---

## 👨‍💻 Author

**Abhishek** — B.Tech CSE | AI/ML Enthusiast
[GitHub](https://github.com/Abhishek-369V) | [Linkedin](https://www.linkedin.com/in/madanala-abhishek-varma/)
