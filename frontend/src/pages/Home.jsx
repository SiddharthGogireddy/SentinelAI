import { useState } from "react";

import Navbar from "../components/Navbar";
import TextInput from "../components/TextInput";
import AnalyzeButton from "../components/AnalyzeButton";
import SummaryCard from "../components/SummaryCard";
import ResultList from "../components/ResultList";

import { analyzeText } from "../services/api";

function Home() {

    const [text, setText] = useState("");

    const [loading, setLoading] = useState(false);

    const [summary, setSummary] = useState({
        high: 0,
        medium: 0,
        low: 0,
    });

    const [results, setResults] = useState([]);

    async function handleAnalyze() {

        if (!text.trim()) return;

        setLoading(true);

        try {

            const response = await analyzeText(text);

            setSummary(response.data.summary);

            setResults(response.data.results);

        } catch (error) {

            console.error(error);

            alert("Analysis failed.");

        }

        setLoading(false);
    }

    return (

        <div className="container"> 

            <Navbar />

            <TextInput
                text={text}
                setText={setText}
            />

            <AnalyzeButton
                loading={loading}
                onClick={handleAnalyze}
            />

            <SummaryCard summary={summary} />

            <ResultList results={results} />

        </div>

    );

}

export default Home;