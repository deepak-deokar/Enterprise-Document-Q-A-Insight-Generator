// frontend/src/pages/Chat.jsx

import React, { useState } from "react";
import { runQA } from "../services/api";
import ChatInput from "../components/ChatInput";
import AnswerDisplay from "../components/AnswerDisplay";

const Chat = () => {
    const [answer, setAnswer] = useState("");
    const [sources, setSources] = useState("");

    const handleAsk = async (question) => {
        const result = await runQA(question);
        setAnswer(result.answer);
        setSources(result.sources);
    };

    return (
        <div className="container d-flex justify-content-center py-5">
            <div className="card p-5 shadow w-75">
                <h2 className="mb-4 text-primary">📚 Document Q&A</h2>

                <ChatInput onSend={handleAsk} />

                {answer && (
                    <div className="mt-4">
                        <h4>Answer:</h4>
                        <div className="alert alert-success">
                            {answer}
                        </div>
                    </div>
                )}

                {sources && (
                    <div className="mt-4">
                        <h5>Sources:</h5>
                        <div className="alert alert-secondary">
                            <pre>{sources}</pre>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default Chat;