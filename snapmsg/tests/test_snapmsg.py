import pytest
from httpx import AsyncClient
from httpx import ASGITransport
from app.main import app
from app.database import SessionLocal, SnapMsg, init_db
import uuid

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


@pytest.fixture(scope="module")
async def setup_db():
    # Inicializa la base de datos antes de ejecutar las pruebas
    init_db()
    yield
    # Aquí puedes agregar cualquier limpieza después de las pruebas si es necesario

@pytest.mark.asyncio
async def test_create_snap_uuid(setup_db):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/snaps", json={"message": "Test message"})
    
    assert response.status_code == 201
    data = response.json()["data"]  # Accede a 'data' primero
    assert "uuid" in data
    assert uuid.UUID(data["uuid"])  # Verifica que el UUID es válido

@pytest.mark.asyncio
async def test_get_snap_by_uuid(setup_db):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        create_response = await ac.post("/snaps", json={"message": "Test message"})
        created_snap = create_response.json()["data"]
        uuid = created_snap["uuid"]

        get_response = await ac.get(f"/snaps/{uuid}")
        assert get_response.status_code == 200
        snap = get_response.json()["data"]
        assert snap["uuid"] == uuid

@pytest.mark.asyncio
async def test_create_snap_uuid_uniqueness(setup_db):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response1 = await ac.post("/snaps", json={"message": "First message"})
        response2 = await ac.post("/snaps", json={"message": "Second message"})

        assert response1.status_code == 201
        assert response2.status_code == 201

        data1 = response1.json()["data"]
        data2 = response2.json()["data"]

        assert data1["uuid"] != data2["uuid"]


@pytest.mark.asyncio
async def test_delete_snap_by_id(setup_db):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        create_response = await ac.post("/snaps", json={"message": "Test message"})
        created_snap = create_response.json()["data"]
        snap_id = created_snap["id"]

        delete_response = await ac.delete(f"/snaps/{snap_id}")

        assert delete_response.status_code == 204

        # Verify the snap is deleted
        get_response = await ac.get(f"/snaps/{snap_id}")
        assert get_response.status_code == 404
