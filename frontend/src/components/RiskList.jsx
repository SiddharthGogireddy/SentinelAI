import { Shield } from "lucide-react";

function RiskList({ results }) {

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
                result.alerts.map((alert, index) => {

                    const Icon = Shield;

                    return (
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
                            <div className="flex items-center justify-between">

                                <div className="flex items-center gap-4">

                                    <Icon
                                        className="text-emerald-400"
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
                        </div>
                    );
                })
            )}

        </div>
    );
}

export default RiskList;