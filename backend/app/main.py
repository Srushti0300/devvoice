from fastapi import FastAPI

app = FastAPI(title="DevVoice")

@app.get("/health")
def health():
    return {"status": "ok"}