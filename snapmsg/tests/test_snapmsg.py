from fastapi.testclient import TestClient
from app.routes import app

client = TestClient(app)

def test_create_snap():
    response = client.post("/snaps", json={"message": "Hello, SnapMsg!"})
    assert response.status_code == 201
    assert response.json()["data"]["message"] == "Hello, SnapMsg!"

def test_get_snaps():
    response = client.get("/snaps")
    assert response.status_code == 200
    assert len(response.json()["data"]) > 0
