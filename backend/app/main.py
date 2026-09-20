from fastapi import FastAPI
from pydantic import BaseModel

from backend.app.analyzer import analyze_speech

app = FastAPI(title="DevVoice")


class SpeechInput(BaseModel):
    text: str
    seconds: float


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/analyze")
def analyze(data: SpeechInput):
    return analyze_speech(data.text, data.seconds)