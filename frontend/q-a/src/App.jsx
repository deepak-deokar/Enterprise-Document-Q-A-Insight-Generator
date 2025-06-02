// frontend/src/App.jsx

import React from "react";
import { BrowserRouter as Router, Routes, Route, NavLink } from "react-router-dom";
import Chat from "./pages/Chat";
import Summarize from "./pages/Summarize";
import Insights from "./pages/Insights";
import Evaluate from "./pages/Evaluate";
import Upload from "./pages/Upload"; // 🚀 Upload Page

const App = () => {
    return (
        <Router>
            {/* 🚀 Top Header */}
            <header className="bg-primary text-white py-3 mb-4">
                <div className="container text-center">
                    <h2>🚀 Enterprise Document Q&A AI</h2>
                    <p className="lead mb-0">Transform your documents into insights with LangGraph + RAG + LLMs</p>
                </div>
            </header>

            {/* 🚀 Navbar */}
            <nav className="navbar navbar-expand-lg navbar-dark bg-dark mb-4">
                <div className="container justify-content-center">
                    <div className="navbar-nav">
                        <NavLink exact="true" to="/" className="nav-link mx-2" activeclassname="active">
                            Chat
                        </NavLink>
                        <NavLink to="/summarize" className="nav-link mx-2" activeclassname="active">
                            Summarize
                        </NavLink>
                        <NavLink to="/insights" className="nav-link mx-2" activeclassname="active">
                            Insights
                        </NavLink>
                        <NavLink to="/evaluate" className="nav-link mx-2" activeclassname="active">
                            Evaluate
                        </NavLink>
                        <NavLink to="/upload" className="nav-link mx-2" activeclassname="active">
                            Upload
                        </NavLink>
                    </div>
                </div>
            </nav>

            {/* 🚀 Page Content */}
            <main className="container mb-5">
                <Routes>
                    <Route path="/" element={<Chat />} />
                    <Route path="/summarize" element={<Summarize />} />
                    <Route path="/insights" element={<Insights />} />
                    <Route path="/evaluate" element={<Evaluate />} />
                    <Route path="/upload" element={<Upload />} />
                </Routes>
            </main>

            {/* 🚀 Footer */}
            <footer className="bg-light text-center text-muted py-3 border-top">
                <div className="container">
                    Built with ❤️ using LangGraph, LangChain, Ollama, React
                </div>
            </footer>
        </Router>
    );
};

export default App;