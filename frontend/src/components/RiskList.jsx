import { Shield } from "lucide-react";
import { explainRisk } from "../services/api";
import { useState } from "react";
function RiskList({ results, uploadedPDF, onDownload }) {
    const [explanations, setExplanations] = useState({});
    const [loadingExplanation, setLoadingExplanation] = useState({});
    async function handleExplain(clause, labels, key) {

    if (explanations[key]) return;

    setLoadingExplanation(prev => ({
        ...prev,
        [key]: true,
    }));

    try {

        const response = await explainRisk(
            clause,
            labels
        );

        setExplanations(prev => ({
            ...prev,
            [key]: response.explanation,
        }));

    } catch (error) {

        console.error(error);

    } finally {

        setLoadingExplanation(prev => ({
            ...prev,
            [key]: false,
        }));

    }
}
    if (!results.length) {
        return (
            <div className="
                rounded-2xl
                border border-white/10
                bg-white/5
                p-10
                text-center
                text-slate-400
                backdrop-blur-xl
            ">
                No analysis yet.
                <br />
                Paste a privacy policy and click Analyze.
            </div>
        );
    }

    
   return (
    <div className="space-y-4">

        {results.flatMap(result =>
            result.alerts.map((alert, index) => (

                <div
                    key={index}
                    className="
                        rounded-2xl
                        border border-white/10
                        bg-white/5
                        p-5
                        backdrop-blur-xl
                        transition-all
                        duration-300
                        hover:border-emerald-400/30
                        hover:-translate-y-1
                    "
                >
                    <div className="space-y-4">

                        <div className="flex items-start justify-between">

                            <div className="flex items-start gap-4">

                                <Shield
                                    className="mt-1 text-emerald-400"
                                    size={22}
                                />

                                <div>
                                    <h2 className="text-lg font-semibold">
                                        {alert.title}
                                    </h2>

                                    <p className="text-sm text-slate-400">
                                        {alert.message}
                                    </p>
                                </div>

                            </div>
                            
                            <span
                                className={`rounded-full px-4 py-1 text-sm font-semibold ${
                                    alert.level === "High"
                                        ? "bg-red-500/20 text-red-300"
                                        : alert.level === "Medium"
                                        ? "bg-yellow-500/20 text-yellow-300"
                                        : "bg-emerald-500/20 text-emerald-300"
                                }`}
                            >
                                {alert.level}
                            </span>

                        </div>

                        {alert.evidence && (
                            <div className="rounded-xl border border-white/5 bg-black/20 p-3">
                                <p className="mb-2 text-xs uppercase tracking-wider text-slate-500">
                                    Evidence
                                </p>

                                <p className="text-sm italic text-slate-300">
                                    "{alert.evidence}"
                                </p>
                            </div>
                        )}
                        {result.page && (
    <div className="
        rounded-xl
        border border-purple-500/20
        bg-purple-500/5
        p-3
    ">
        <p className="
            text-xs
            uppercase
            tracking-wider
            text-purple-300
        ">
            Found On
        </p>

        <p className="text-sm text-slate-300">
            Page {result.page}
        </p>
    </div>
)}
                        {result.source && (
    <div className="text-xs text-slate-500">
        Source: {result.source}
    </div>
)}

                       
                            <div className="flex justify-start">
   <button
    onClick={() =>
        handleExplain(
            result.clause,
            result.labels,
            index
        )
    }
    className="
        rounded-xl
        border border-cyan-500/30
        bg-cyan-500/10
        px-4
        py-2
        text-sm
        font-medium
        text-cyan-300
        transition-all
        hover:bg-cyan-500/20
    "
>
    {loadingExplanation[index]
        ? "Generating..."
        : explanations[index]
        ? "Regenerate Explanation"
        : "Explain with AI"}
</button>
{uploadedPDF && results.length > 0 && (
    <div className="flex justify-center">
        <button
            onClick={onDownload}
            className="
                rounded-xl
                bg-red-500
                px-6
                py-3
                font-semibold
                text-white
                hover:bg-red-400
                transition
            "
        >
            Download Highlighted PDF
        </button>
    </div>
)}
{explanations[index] && (
    <div className="
        mt-4
        rounded-xl
        border border-cyan-500/20
        bg-cyan-500/5
        p-4
    ">
        <p className="mb-2 text-xs uppercase tracking-wider text-cyan-300">
            AI Explanation
        </p>

        <p className="text-sm leading-relaxed text-slate-300">
            {explanations[index]}
        </p>
    </div>
)}
</div>

                    </div>
                </div>

            ))
        )}

    </div>
);
}

export default RiskList;