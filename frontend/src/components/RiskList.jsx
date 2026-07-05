import { Camera, Mic, Cookie } from "lucide-react";

const risks = [
    {
        icon: Camera,
        title: "Camera Access",
        level: "High",
        color: "red",
        description: "The application may access your camera.",
    },
    {
        icon: Mic,
        title: "Microphone Access",
        level: "High",
        color: "red",
        description: "The application may access your microphone.",
    },
    {
        icon: Cookie,
        title: "Cookies",
        level: "Low",
        color: "green",
        description: "Cookies may be used for personalization.",
    },
];

function RiskList() {
    return (
        <div className="space-y-4">

            {risks.map((risk, index) => {

                const Icon = risk.icon;

                return (

                    <div
                        key={index}
                        className="rounded-3xl border border-white/10 bg-white/5 p-6 backdrop-blur-xl transition-all
duration-300
hover:border-emerald-400/30
hover:-translate-y-1"
                    >

                        <div className="flex items-center justify-between">

                            <div className="flex items-center gap-4">

                                <Icon className="text-emerald-400" size={22} />

                                <div>

                                    <h2 className="text-lg font-semibold">
                                        {risk.title}
                                    </h2>

                                    <p className="text-slate-400">
                                        {risk.description}
                                    </p>

                                </div>

                            </div>

                            <span
                                className={`rounded-full px-4 py-1 text-sm font-semibold ${
                                    risk.level === "High"
                                        ? "bg-red-500/20 text-red-300"
                                        : "bg-green-500/20 text-green-300"
                                }`}
                            >
                                {risk.level}
                            </span>

                        </div>

                    </div>

                );
            })}
        </div>
    );
}

export default RiskList;