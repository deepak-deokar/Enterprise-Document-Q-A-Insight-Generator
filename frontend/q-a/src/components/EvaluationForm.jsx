// frontend/src/components/EvaluationForm.jsx

import React, { useState } from "react";

const EvaluationForm = ({ onEvaluate }) => {
    const [predicted, setPredicted] = useState("");
    const [reference, setReference] = useState("");

    const handleSubmit = () => {
        if (!predicted.trim() || !reference.trim()) {
            alert("Please fill in both summaries!");
            return;
        }
        onEvaluate(predicted, reference);
    };

    return (
        <div className="mt-4">
            <h5>Predicted Summary:</h5>
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
                placeholder="Enter reference/ground-truth summary..."
            />

            <button className="btn btn-primary mt-3" onClick={handleSubmit}>
                Evaluate
            </button>
        </div>
    );
};

export default EvaluationForm;