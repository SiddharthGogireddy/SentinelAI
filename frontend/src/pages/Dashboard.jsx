import { useState } from "react";
import { analyzeText,uploadPDF,analyzeURL,downloadHighlightedPDF } from "../services/api";
import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import InputCard from "../components/InputCard";
import SummaryCards from "../components/SummaryCards";
import RiskList from "../components/RiskList";

function Dashboard() {
    const [url, setUrl] = useState("");
    const [text, setText] = useState("");
    const [loading, setLoading] = useState(false);
    const [results, setResults] = useState([]);
    const [summary, setSummary] = useState({
        high: 0,
        medium: 0,
        low: 0,
    });
    const [uploadedPDF, setUploadedPDF] = useState(null);
    
    
    async function handleAnalyze() {
    if (!text.trim()) return;

    setLoading(true);

    try {
        const response = await analyzeText(text);
        console.log(response);
        setResults(response.data.results);
        setSummary(response.data.summary);

    } catch (error) {
        console.error(error);
    } finally {
        setLoading(false);
    }
}
    async function handlePDF(file) {

        if (!file) return;

        setLoading(true);
        setUploadedPDF(file);
        try {
            console.log("Uploading file:", file);
            const response = await uploadPDF(file);
            console.log(JSON.stringify(response, null, 2));
            setResults(response.data.results);
            setSummary(response.data.summary);
            

        } catch (error) {

            console.error(error);

        } finally {

            setLoading(false);

        }
    }
    async function handleDownload() {

    if (!uploadedPDF) return;

    const blob =
        await downloadHighlightedPDF(
            uploadedPDF
        );

    const url =
        window.URL.createObjectURL(blob);

    const link =
        document.createElement("a");

    link.href = url;
    link.download =
        "highlighted_policy.pdf";

    link.click();
}
    async function handleURL() {

    if (!url.trim()) return;

    setLoading(true);

    try {

        const response = await analyzeURL(url);

        setResults(response.data.results);
        setSummary(response.data.summary);

    } catch (error) {

        console.error(error);

    } finally {

        setLoading(false);

    }
}

    return (
        <div className="min-h-screen bg-gradient-to-br from-[#07130F] via-[#0B1D18] to-[#111827] text-white relative overflow-hidden">

            <div className="absolute -top-40 -left-40 h-96 w-96 rounded-full bg-emerald-500/10 blur-3xl" />

            <div className="absolute bottom-0 right-0 h-96 w-96 rounded-full bg-emerald-400/10 blur-3xl" />

            <Navbar />

            <main className="mx-auto max-w-7xl px-6 py-10">

                <div
                    className="
                        rounded-3xl
                        border border-white/10
                        bg-white/[0.03]
                        backdrop-blur-3xl
                        shadow-[0_25px_80px_rgba(0,0,0,.45)]
                        p-8
                        space-y-10
                    "
                >
                    <Hero />
                    <InputCard
    text={text}
    setText={setText}
    loading={loading}
    onAnalyze={handleAnalyze}
    onPDFUpload={handlePDF}
    url={url}
    setUrl={setUrl}
    onURLAnalyze={handleURL}
    uploadedPDF={uploadedPDF}
    onDownload={handleDownload}
/>

                    <SummaryCards summary={summary} />

                    <RiskList results={results} />

                </div>

            </main>

        </div>
    );
}

export default Dashboard;