from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_service():
    response = client.post("/services/", json={"name": "API", "status": "Operational"})
    assert response.status_code == 200
    assert response.json()["name"] == "API"