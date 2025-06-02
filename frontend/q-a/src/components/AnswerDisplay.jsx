// frontend/src/components/AnswerDisplay.jsx

import React from "react";
import ReactMarkdown from "react-markdown";

const AnswerDisplay = ({ answer, sources }) => {
    return (
        <div className="mt-4">
            <h4>Answer:</h4>
            <div className="border p-3 bg-light">
                <ReactMarkdown>{answer}</ReactMarkdown>
            </div>

            <h5 className="mt-3">Sources:</h5>
            <div className="border p-2 bg-white">
                <pre>{sources}</pre>
            </div>
        </div>
    );
};

export default AnswerDisplay;