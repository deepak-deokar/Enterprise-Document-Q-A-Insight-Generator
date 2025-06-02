// frontend/src/components/FileUploader.jsx

import React, { useState } from "react";
import axios from "axios";

const FileUploader = ({ onUploadSuccess }) => {
    const [file, setFile] = useState(null);
    const [uploading, setUploading] = useState(false);
    const [message, setMessage] = useState("");

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
        setMessage("");
    };

    const handleUpload = async () => {
        if (!file) {
            alert("Please select a file first!");
            return;
        }

        setUploading(true);
        setMessage("");

        const formData = new FormData();
        formData.append("file", file);

        try {
            const response = await axios.post("http://localhost:8000/upload", formData);
            setMessage("✅ Upload successful!");
            if (onUploadSuccess) onUploadSuccess(response.data);
        } catch (err) {
            console.error(err);
            setMessage("❌ Upload failed!");
        } finally {
            setUploading(false);
        }
    };

    return (
        <div className="mb-4">
            <input type="file" className="form-control" onChange={handleFileChange} />
            <button className="btn btn-success mt-2" onClick={handleUpload} disabled={uploading}>
                {uploading ? "Uploading..." : "Upload"}
            </button>
            {message && <div className="mt-2">{message}</div>}
        </div>
    );
};

export default FileUploader;