import pytest
from httpx import AsyncClient
from httpx import ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_create_snap():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/snaps", json={"message": "Hello!"})
    assert response.status_code == 201
    assert response.json()["data"]["message"] == "Hello!"

@pytest.mark.asyncio
async def test_get_snaps():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/snaps")
    assert response.status_code == 200
    assert isinstance(response.json()["data"], list)

@pytest.mark.asyncio
async def test_create_snap_length_validation():
    async with AsyncClient(app=app, base_url="http://test") as client:
        long_message = "a" * 281  
        response = await client.post("/snaps", json={"message": long_message})
        assert response.status_code == 400  
        assert response.json() == {
            "type": "about:blank",
            "title": "Bad Request",
            "status": 400,
            "detail": [
                {
                    "loc": ["body", "message"],
                    "msg": "String should have at most 280 characters",
                    "type": "string_too_long",
                    "ctx": {"max_length": 280}
                }
            ],
            "instance": "http://test/snaps"
        }