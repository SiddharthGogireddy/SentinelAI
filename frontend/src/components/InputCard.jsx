import { FileText, Upload, Globe } from "lucide-react";
import { useState } from "react";

function InputCard({
    text,
    setText,
    loading,
    onAnalyze,
    onPDFUpload,
}) {

    const [mode, setMode] = useState("text");

    return (
        <div
            className="
                rounded-2xl
                border border-white/10
                bg-white/5
                backdrop-blur-2xl
                shadow-[0_8px_40px_rgba(0,0,0,.35)]
                p-6
            "
        >

            {/* Hidden PDF Input */}

            <input
                type="file"
                accept=".pdf"
                id="pdf-upload"
                className="hidden"
                onChange={(e) => onPDFUpload(e.target.files[0])}
            />

            {/* Tabs */}

            <div className="flex gap-3 mb-6">

                <button
                    onClick={() => setMode("text")}
                    className={`flex items-center gap-2 rounded-xl px-4 py-2 transition ${
                        mode === "text"
                            ? "bg-emerald-500 text-slate-900"
                            : "bg-white/5 hover:bg-white/10"
                    }`}
                >
                    <FileText size={18} />
                    Paste Text
                </button>

                <button
                    onClick={() => setMode("pdf")}
                    className={`flex items-center gap-2 rounded-xl px-4 py-2 transition ${
                        mode === "pdf"
                            ? "bg-emerald-500 text-slate-900"
                            : "bg-white/5 hover:bg-white/10"
                    }`}
                >
                    <Upload size={18} />
                    Upload PDF
                </button>

                <button
                    onClick={() => setMode("url")}
                    className={`flex items-center gap-2 rounded-xl px-4 py-2 transition ${
                        mode === "url"
                            ? "bg-emerald-500 text-slate-900"
                            : "bg-white/5 hover:bg-white/10"
                    }`}
                >
                    <Globe size={18} />
                    Analyze URL
                </button>

            </div>

            {/* TEXT MODE */}

            {mode === "text" && (
                <textarea
                    value={text}
                    onChange={(e) => setText(e.target.value)}
                    rows={12}
                    placeholder="Paste a Privacy Policy or Terms of Service..."
                    className="
                        w-full
                        rounded-2xl
                        border border-white/10
                        bg-black/20
                        p-5
                        text-white
                        placeholder:text-slate-500
                        outline-none
                        focus:border-emerald-400
                        resize-none
                    "
                />
            )}

            {/* PDF MODE */}

            {mode === "pdf" && (
                <div
                    className="
                        flex flex-col items-center justify-center
                        rounded-2xl
                        border-2 border-dashed border-white/10
                        bg-black/20
                        p-12
                    "
                >

                    <Upload
                        size={40}
                        className="mb-4 text-emerald-400"
                    />

                    <label
                        htmlFor="pdf-upload"
                        className="
                            cursor-pointer
                            rounded-xl
                            bg-emerald-500
                            px-5 py-3
                            font-semibold
                            text-slate-900
                            hover:bg-emerald-400
                            transition
                        "
                    >
                        Select PDF
                    </label>

                </div>
            )}

            {/* URL MODE */}

            {mode === "url" && (
                <input
                    type="text"
                    placeholder="https://example.com/privacy"
                    className="
                        w-full
                        rounded-2xl
                        border border-white/10
                        bg-black/20
                        p-5
                        text-white
                        placeholder:text-slate-500
                        outline-none
                        focus:border-emerald-400
                    "
                />
            )}

            {/* Analyze Button */}

            {mode === "text" && (
                <div className="mt-6 flex justify-center">

                    <button
                        onClick={onAnalyze}
                        disabled={loading}
                        className="
                            rounded-xl
                            bg-emerald-500
                            hover:bg-emerald-400
                            disabled:opacity-50
                            text-slate-900
                            font-semibold
                            px-8 py-3
                            transition-all
                            duration-300
                            shadow-lg
                            hover:shadow-emerald-500/30
                        "
                    >
                        {loading
                            ? "Analyzing..."
                            : "Analyze Policy"}
                    </button>

                </div>
            )}

        </div>
    );
}

export default InputCard;