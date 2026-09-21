from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_analyze():
    response = client.post("/analyze", json={"text": "um hello world", "seconds": 30})
    assert response.status_code == 200
    data = response.json()
    assert data["word_count"] == 3
    assert data["fillers"] == {"um": 1}


def test_analyze_audio(monkeypatch):
    monkeypatch.setattr(
        "backend.app.main.transcribe_audio",
        lambda path: ("um hello world", 30.0),
    )
    response = client.post(
        "/analyze-audio",
        files={"file": ("test.wav", b"fake audio bytes", "audio/wav")},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["transcript"] == "um hello world"
    assert data["fillers"] == {"um": 1}


def test_analyze_audio_no_speech(monkeypatch):
    monkeypatch.setattr(
        "backend.app.main.transcribe_audio",
        lambda path: ("", 5.0),
    )
    response = client.post(
        "/analyze-audio",
        files={"file": ("test.wav", b"fake audio bytes", "audio/wav")},
    )
    assert response.status_code == 422