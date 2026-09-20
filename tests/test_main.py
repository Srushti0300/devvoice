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