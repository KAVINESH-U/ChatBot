# ChatBot

A modern AI-powered chatbot built with FastAPI, LangGraph, Streamlit, and a React frontend with professional CSS styling.
The chatbot uses Google Generative AI (Gemini API) to generate intelligent responses, making it versatile for various use-cases like Q&A, career guidance, or general assistance.

🚀 Features

FastAPI Backend → Handles chat requests and connects with Google AI.

LangGraph Integration → Manages structured conversation flow.

React Frontend → Professional SaaS-style UI with animations, gradients, and responsive design.

Streamlit Demo App → Lightweight interface for quick testing.

Google Generative AI (Gemini API) → Powers intelligent chatbot replies.

Glassmorphism Design → Modern look with smooth transitions.

📂 Project Structure
chatbot/
│── backend/            
│   ├── main.py
│   ├── langgraph_flow.py
│   ├── requirements.txt
│
│── frontend/          
│   ├── src/
│   │   ├── App.jsx
│   │   ├── ChatBox.jsx
│   │   ├── styles.css
│   ├── package.json
│
│── streamlit_app/     
│   ├── app.py
│
│── README.md           

⚡Installations

1️⃣ Run Backend (FastAPI + LangGraph)
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000

2️⃣ Run Streamlit UI (Optional Demo)
cd streamlit_app
pip install streamlit requests
streamlit run app.py

3️⃣ Run React Frontend (Professional UI)
cd frontend
npm install
npm run dev
