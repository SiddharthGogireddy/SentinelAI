import axios from "axios";

const API = axios.create({
    baseURL: "http://127.0.0.1:8000/api",
});

export async function analyzeText(text) {
    const response = await API.post("/analyze", {
        text,
    });

    return response.data;
}
export async function analyzeURL(url) {
    const response = await API.post(
        "/url",
        { url }
    );
    return response.data;
}
export async function uploadPDF(file) {
    const formData = new FormData();

    formData.append("file", file);

    const response = await API.post(
        "/upload",
        formData,
        {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        }
    );

    return response.data;
}
export async function explainRisk(clause, labels) {
    const response = await API.post(
        "/explain",
        {
            clause,
            labels,
        }
    );

    return response.data;
}
