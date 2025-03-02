from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Add this import
from app.service import router as sentiment_analysis_router

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(sentiment_analysis_router, prefix="/api", tags=["SentimentAnalyser"])

@app.get("/")
async def root():
    return {"message": "Welcome to backend"}