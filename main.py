from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from Sentiment import run_sentiment_model

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Request(BaseModel):
    ticker: str

@app.post("/sentiment")
def sentiment(req: Request):
    score = run_sentiment_model(req.ticker.upper())

    if score is None:
        return {"error": "No data found"}

    label = (
        "Bullish" if score > 0.2 else
        "Bearish" if score < -0.2 else
        "Neutral"
    )

    return {
        "ticker": req.ticker.upper(),
        "score": score,
        "label": label
    }
