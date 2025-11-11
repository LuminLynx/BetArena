from starlette.testclient import TestClient
from app.main import app

client = TestClient(app=app)


def test_health_check():
    """Test the health check endpoint"""
    response = client.get("/healthz")
    assert response.status_code == 200
    data = response.json()
    assert data["ok"] is True
    assert data["service"] == "api"


def test_root():
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
