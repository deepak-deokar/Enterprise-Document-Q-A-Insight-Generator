// frontend/src/pages/Insights.jsx

import React, { useState } from "react";
import { extractInsights } from "../services/api";

const Insights = () => {
    const [inputText, setInputText] = useState("");
    const [insights, setInsights] = useState("");

    const handleExtract = async () => {
        if (!inputText.trim()) {
            alert("Please enter text to analyze!");
            return;
        }

        const result = await extractInsights(inputText);
        setInsights(result.insights);
    };

    return (
        <div className="container mt-4">
            <h2>💡 Extract Insights</h2>

            <textarea
                className="form-control"
                rows="6"
                value={inputText}
                onChange={(e) => setInputText(e.target.value)}
                placeholder="Enter text or document content..."
            />

            <button className="btn btn-primary mt-2" onClick={handleExtract}>
                Extract Insights
            </button>

            <h4 className="mt-4">Insights:</h4>
            <div className="border p-3 bg-light">
                <pre>{insights}</pre>
            </div>
        </div>
    );
};

export default Insights;