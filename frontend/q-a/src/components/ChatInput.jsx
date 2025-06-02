// frontend/src/components/ChatInput.jsx

import React, { useState } from "react";

const ChatInput = ({ onSend }) => {
    const [input, setInput] = useState("");

    const handleSend = () => {
        if (!input.trim()) {
            alert("Please enter a message!");
            return;
        }
        onSend(input);
        setInput("");
    };

    return (
        <div className="mt-3">
            <textarea
                className="form-control"
                rows="3"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Type your question here..."
            />
            <button className="btn btn-primary mt-2" onClick={handleSend}>
                Send
            </button>
        </div>
    );
};

export default ChatInput;