import { FileText, Upload, Globe } from "lucide-react";

function InputCard({
    text,
    setText,
    loading,
    onAnalyze,
}) {
    return (
        <div className="rounded-2xl
border
border-white/10
bg-white/5
backdrop-blur-2xl
shadow-[0_8px_40px_rgba(0,0,0,.35)]
p-6">

            {/* Tabs */}

            <div className="flex gap-3 mb-6">

                <button className="flex items-center gap-2 rounded-xl bg-emerald-500 text-slate-900 px-4 py-2 text-white">
                    <FileText size={18} />
                    Paste Text
                </button>

                <button className="flex items-center gap-2 rounded-xl bg-white/5 px-4 py-2 hover:bg-white/10 transition">
                    <Upload size={18} />
                    Upload PDF
                </button>

                <button className="flex items-center gap-2 rounded-xl bg-white/5 px-4 py-2 hover:bg-white/10 transition">
                    <Globe size={18} />
                    Analyze URL
                </button>

            </div>

            {/* Text Area */}

            <textarea
                 value={text}
    onChange={(e) => setText(e.target.value)}
                rows={12}
                placeholder="Paste a Privacy Policy or Terms of Service..."
                className="
                    w-full
                    rounded-2xl
                    border
                    border-white/10
                    bg-black/20
                    p-5
                    text-white
                    placeholder:text-slate-500
                    outline-none
                    focus:border-emerald-400
                    resize-none
                "
            />

            {/* Analyze Button */}

            <div className="mt-6 flex justify-center">

                <button
                    onClick={onAnalyze}
                    
                    className="
rounded-xl
bg-emerald-500
hover:bg-emerald-400
text-slate-900
font-semibold
px-8
py-3
transition-all
duration-300
shadow-lg
hover:shadow-emerald-500/30
"                >
                {loading ? "Analyzing..." : "Analyze Policy"}
                    Analyze
                </button>

            </div>

        </div>
    );
}

export default InputCard;