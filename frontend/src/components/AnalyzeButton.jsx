function AnalyzeButton({ onClick, loading }) {
    return (
        <button
            onClick={onClick}
            disabled={loading}
        >
            {loading ? "Analyzing..." : "Analyze"}
        </button>
    );
}

export default AnalyzeButton;