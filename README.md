# 🤖 Universal AI Utility App

> **Multi-Task AI Application** | Prompt Routing | Streamlit + OpenAI

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-green)

---

## 📌 About

A multi-task AI application that performs 5 different NLP tasks 
through a single unified interface — built using prompt routing architecture.

> One UI → Multiple Prompts → One Model → Different Outputs

---

## ✨ Current Features

- 5 AI Tasks — Summarize, Translate, Explain, Generate Email, Rewrite
- Prompt Routing — routes to correct prompt based on selected task
- Prompt Transparency — shows constructed prompt before output
- Input Validation — handles empty inputs gracefully
- Clean modular architecture — UI / Prompts / Backend separated

---

## 🗂️ Project Structure
```
universal_ai_app/
├── app.py            # Streamlit UI
├── backend.py        # OpenAI API call
├── prompts.py        # Prompt builder
├── requirements.txt
└── README.md
```
---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Frontend UI |
| OpenAI API (GPT-4o-mini) | LLM |

---

## 🚀 Run Locally

```bash
git clone https://github.com/Abhishek-369V/universal-ai-utility.git
cd universal-ai-utility
pip install -r requirements.txt
```

Create `.streamlit/secrets.toml`:
```toml
OPENAI_API_KEY = "your-key-here"
```

```bash
streamlit run app.py
```

---

## 🔮 Upcoming Features

- [X] Gemini Flash as alternative LLM
- [ ] Prompt history tracking
- [ ] Chat with PDF using RAG + LangChain
- [X] Download output button

---

## 👨‍💻 Author

**Abhishek** — B.Tech CSE | AI/ML Enthusiast
[GitHub](https://github.com/Abhishek-369V) | [Linkedin](https://www.linkedin.com/in/madanala-abhishek-varma/)
