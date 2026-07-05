
import RiskCard from "./RiskCard";

function ResultList({ results }) {
    return (
        <div>
            <h2>Detected Risks</h2>

            {results.map((result, index) => (

                <div key={index}>

                    <h4>{result.clause}</h4>

                    {result.alerts.map((alert, i) => (
                        <RiskCard
                            key={i}
                            alert={alert}
                        />
                    ))}

                </div>

            ))}
        </div>
    );
}

export default ResultList;