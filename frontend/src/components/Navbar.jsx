import { Shield } from "lucide-react";

function Navbar() {

    return (

        <nav className="border-b border-slate-800 bg-black/20 backdrop-blur-xl">

            <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-6">

                <div className="flex items-center gap-3">

                    <Shield className="h-5 w-5 text-emerald-400"/>

                    <h2 className="text-lg font-bold">

                        SentinelAI

                    </h2>

                </div>

                <p className="text-sm text-slate-400">

                    AI Privacy Analyzer

                </p>

            </div>

        </nav>

    );

}

export default Navbar;