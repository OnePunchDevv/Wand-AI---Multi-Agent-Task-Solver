from fastapi.testclient import TestClient

from app.main import app


# Test the health endpoint
def test_health():
    client = TestClient(app)
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}
