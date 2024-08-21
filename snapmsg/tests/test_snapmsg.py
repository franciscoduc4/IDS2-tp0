import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, SnapMsg, get_db
from app import app

DATABASE_URL = "sqlite:///./test_snapmsg.db"

engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_and_teardown():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_create_snap():
    response = client.post("/snaps", json={"message": "Hello, SnapMsg!"})
    assert response.status_code == 201
    assert response.json()["message"] == "Hello, SnapMsg!"

def test_get_snaps():
    # Create a snap message
    client.post("/snaps", json={"message": "Hello, SnapMsg!"})
    
    # Get all snap messages
    response = client.get("/snaps")
    assert response.status_code == 200
    
    # Check if there is at least one snap message
    data = response.json().get("data", [])
    assert len(data) > 0
    assert data[0]["message"] == "Hello, SnapMsg!"  
