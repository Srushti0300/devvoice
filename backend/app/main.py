import os
import tempfile

from fastapi import FastAPI, File, HTTPException, UploadFile
from pydantic import BaseModel

from backend.app.analyzer import analyze_speech
from backend.app.transcriber import transcribe_audio

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


@app.post("/analyze-audio")
async def analyze_audio(file: UploadFile = File(...)):
    suffix = os.path.splitext(file.filename or "")[1] or ".wav"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name
    try:
        text, seconds = transcribe_audio(tmp_path)
    finally:
        os.remove(tmp_path)
    if not text:
        raise HTTPException(status_code=422, detail="No speech found in the audio")
    return {"transcript": text, **analyze_speech(text, seconds)}