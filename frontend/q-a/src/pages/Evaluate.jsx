// frontend/src/pages/Evaluate.jsx

import React, { useState } from "react";
import { evaluateSummary } from "../services/api";

const Evaluate = () => {
    const [predicted, setPredicted] = useState("");
    const [reference, setReference] = useState("");
    const [scores, setScores] = useState(null);

    const handleEvaluate = async () => {
        if (!predicted.trim() || !reference.trim()) {
            alert("Please enter both predicted and reference summaries!");
            return;
        }

        const result = await evaluateSummary(predicted, reference);
        setScores(result.scores);
    };

    return (
        <div className="container mt-4">
            <h2>📊 Evaluate Summary</h2>

            <h5 className="mt-3">Predicted Summary:</h5>
            <textarea
                className="form-control"
                rows="4"
                value={predicted}
                onChange={(e) => setPredicted(e.target.value)}
                placeholder="Enter model-generated summary..."
            />

            <h5 className="mt-3">Reference Summary:</h5>
            <textarea
                className="form-control"
                rows="4"
                value={reference}
                onChange={(e) => setReference(e.target.value)}
                placeholder="Enter ground truth / reference summary..."
            />

            <button className="btn btn-primary mt-3" onClick={handleEvaluate}>
                Evaluate
            </button>

            {scores && (
                <div className="mt-4">
                    <h4>ROUGE Scores:</h4>
                    <ul>
                        <li>ROUGE-1 F: {scores.rouge1_f.toFixed(4)}</li>
                        <li>ROUGE-2 F: {scores.rouge2_f.toFixed(4)}</li>
                        <li>ROUGE-L F: {scores.rougeL_f.toFixed(4)}</li>
                    </ul>
                </div>
            )}
        </div>
    );
};

export default Evaluate;