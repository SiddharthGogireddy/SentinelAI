const text = document.body.innerText;

fetch(
    "http://127.0.0.1:8000/api/analyze",
    {
        method: "POST",

        headers: {
            "Content-Type":
                "application/json"
        },

        body: JSON.stringify({
            text
        })
    }
)
.then(res => res.json())
.then(data => {
    console.log(
        "SentinelAI:",
        data
    );
});