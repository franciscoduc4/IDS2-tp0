# tests/test_snapmsg.py

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_snap():
    response = client.post("/snaps", json={"message": "Hello, SnapMsg!"})
    assert response.status_code == 201
    response_data = response.json()
    assert "data" in response_data
    assert response_data["data"]["message"] == "Hello, SnapMsg!"

def test_get_snaps():
    client.post("/snaps", json={"message": "Hello, SnapMsg!"})
    response = client.get("/snaps")
    assert response.status_code == 200
    data = response.json().get("data", [])
    assert len(data) > 0
    assert data[0]["message"] == "Hello, SnapMsg!"  

def test_create_snap_bad_request():
    response = client.post("/snaps", json={})
    assert response.status_code == 400
    error_data = response.json()
    assert "detail" in error_data
