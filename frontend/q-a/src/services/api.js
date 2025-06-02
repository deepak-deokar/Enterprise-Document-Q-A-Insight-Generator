// frontend/src/services/api.js

import axios from "axios";

// 🚀 API base URL
const API_BASE = "http://localhost:8000";

// 🚀 Ask Question (used in Chat.jsx → runQA)
export const runQA = async (question) => {
    try {
        const response = await axios.post(`${API_BASE}/qa`, { question });
        return response.data;
    } catch (error) {
        console.error("runQA error:", error);
        return { answer: "Error occurred.", sources: "" };
    }
};

// 🚀 Upload document (used in Upload.jsx)
export const uploadDocument = async (file) => {
    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await axios.post(`${API_BASE}/upload`, formData, {
            headers: { "Content-Type": "multipart/form-data" },
        });
        return response.data;
    } catch (error) {
        console.error("uploadDocument error:", error);
        return { message: "Upload failed." };
    }
};

// 🚀 Summarize document (used in Summarize.jsx)
export const summarizeDocument = async (docName) => {
    const formData = new FormData();
    formData.append("doc_name", docName);

    try {
        const response = await axios.post(`${API_BASE}/summarize`, formData);
        return response.data;
    } catch (error) {
        console.error("summarizeDocument error:", error);
        return { summary: "Error occurred." };
    }
};

// 🚀 Extract insights (used in Insights.jsx)
export const extractInsights = async (text) => {
    const formData = new FormData();
    formData.append("text", text);

    try {
        const response = await axios.post(`${API_BASE}/insights`, formData);
        return response.data;
    } catch (error) {
        console.error("extractInsights error:", error);
        return { insights: "Error occurred." };
    }
};

// 🚀 Evaluate summary (used in Evaluate.jsx)
export const evaluateSummary = async (predicted, reference) => {
    const formData = new FormData();
    formData.append("predicted_summary", predicted);
    formData.append("reference_summary", reference);

    try {
        const response = await axios.post(`${API_BASE}/evaluate`, formData);
        return response.data;
    } catch (error) {
        console.error("evaluateSummary error:", error);
        return { rouge_score: "Error occurred." };
    }
};