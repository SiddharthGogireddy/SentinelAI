from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.upload import router as upload_router


from backend.api.analyze import router as analyze_router

app = FastAPI(
    title="SentinelAI API",
    version="1.0.0"
)

# Allow frontend/browser extension
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analyze_router, prefix="/api")
app.include_router(upload_router, prefix="/api")


@app.get("/")
def home():
    return {
        "message": "SentinelAI Backend Running"
    }