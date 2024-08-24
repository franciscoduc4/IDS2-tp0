import pytest
from httpx import AsyncClient
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
