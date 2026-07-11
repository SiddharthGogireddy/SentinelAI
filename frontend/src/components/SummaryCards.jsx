import { AlertTriangle, ShieldAlert, ShieldCheck } from "lucide-react";

function SummaryCards({ summary }) {

    return (
        <div className="grid grid-cols-1 gap-5 md:grid-cols-3">

            <div className="
rounded-2xl
border
border-red-500/20
bg-red-500/5
backdrop-blur-xl
p-5
transition-all
duration-300
hover:-translate-y-1
hover:shadow-xl
">
                <div className="flex items-center justify-between">
                    <div>
                        <p className="text-red-300">High Risk</p>
                        <h1 className="mt-2 text-4xl font-bold">{summary.high}</h1>
                    </div>

                    <AlertTriangle className="h-10 w-10 text-red-400" />
                </div>
            </div>

            <div className="rounded-2xl border border-yellow-500/20 bg-yellow-500/5 p-6 backdrop-blur-xl transition-all
duration-300
hover:-translate-y-1
hover:shadow-xl
">
                <div className="flex items-center justify-between">
                    <div>
                        <p className="text-yellow-300">Medium Risk</p>
                        <h1 className="mt-2 text-4xl font-bold">{summary.medium}</h1>
                    </div>

                    <ShieldAlert className="h-10 w-10 text-yellow-400" />
                </div>
            </div>

            <div className="rounded-3xl border border-green-500/20 bg-emerald-500/5 p-6 backdrop-blur-xl transition-all
duration-300
hover:-translate-y-1
hover:shadow-xl
">
                <div className="flex items-center justify-between">
                    <div>
                        <p className="text-green-300">Low Risk</p>
                        <h1 className="mt-1 text-3xl font-bold">{summary.low}</h1>
                    </div>

                    <ShieldCheck className="h-8 w-8 text-emerald-300" />
                </div>
            </div>

        </div>
    );
}

export default SummaryCards;