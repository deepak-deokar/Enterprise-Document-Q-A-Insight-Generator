// frontend/src/pages/Upload.jsx

import React, { useState } from "react";
import { uploadDocument } from "../services/api";

const Upload = () => {
    const [file, setFile] = useState(null);
    const [status, setStatus] = useState("");

    const handleUpload = async () => {
        if (!file) {
            setStatus("⚠️ Please select a file to upload.");
            return;
        }

        setStatus("⏳ Uploading...");

        try {
            const result = await uploadDocument(file);
            setStatus(result.message || "✅ Upload complete!");
        } catch (error) {
            setStatus("❌ Upload failed. Please try again.");
            console.error("Upload error:", error);
        }
    };

    return (
        <div className="container d-flex justify-content-center py-5">
            <div className="card p-5 shadow w-75">
                <h2 className="mb-4 text-primary">📤 Upload Document</h2>

                <div className="mb-3">
                    <input
                        type="file"
                        className="form-control"
                        onChange={(e) => setFile(e.target.files[0])}
                    />
                </div>

                <button className="btn btn-primary w-100" onClick={handleUpload}>
                    Upload
                </button>

                {status && (
                    <div className="alert alert-info mt-4 text-center">
                        {status}
                    </div>
                )}
            </div>
        </div>
    );
};

export default Upload;