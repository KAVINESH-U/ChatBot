import React from "react";
import ChatBox from "./ChatBox";
import "./styles.css";

function App() {
  return (
    <div className="app-container">
      <header className="app-header">
        🤖 LangGraph Chatbot
      </header>
      <main>
        <ChatBox />
      </main>
      <footer className="app-footer">
        Built with FastAPI + Streamlit + React + Google AI
      </footer>
    </div>
  );
}

export default App;
