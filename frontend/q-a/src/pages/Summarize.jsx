// frontend/src/pages/Summarize.jsx

import React, { useState } from "react";
import { summarizeDocument } from "../services/api";

const Summarize = () => {
    const [docName, setDocName] = useState("");
    const [summary, setSummary] = useState("");

    const handleSummarize = async () => {
        if (!docName.trim()) {
            alert("Please enter a document name!");
            return;
        }

        const result = await summarizeDocument(docName);
        setSummary(result.summary);
    };

    return (
        <div className="container mt-4">
            <h2>📝 Summarize Document</h2>

            <input
                type="text"
                className="form-control"
                value={docName}
                onChange={(e) => setDocName(e.target.value)}
                placeholder="Enter document name (e.g. HR_policy.pdf)"
            />

            <button className="btn btn-primary mt-2" onClick={handleSummarize}>
                Summarize
            </button>

            <h4 className="mt-4">Summary:</h4>
            <div className="border p-3 bg-light">
                <pre>{summary}</pre>
            </div>
        </div>
    );
};

export default Summarize;