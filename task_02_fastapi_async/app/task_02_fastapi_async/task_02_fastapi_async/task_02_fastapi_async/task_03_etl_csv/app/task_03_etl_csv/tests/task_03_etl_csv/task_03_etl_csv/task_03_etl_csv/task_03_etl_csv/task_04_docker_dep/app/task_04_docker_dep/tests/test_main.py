from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

def test_health_returns_200():
    # Should return 200 even if redis is down
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_count_endpoint():
    response = client.get("/count")
    assert response.status_code == 200
    assert "count" in response.json()
