from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_generate():
    payload = {"topic":"productivity tools for remote teams","word_count":800}
    r = client.post("/api/v1/generate", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert "article" in data
    assert "title" in data