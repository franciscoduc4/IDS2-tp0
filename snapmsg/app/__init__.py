from fastapi import FastAPI
from .config import DevelopmentConfig, ProductionConfig, TestingConfig
from .models import create_tables, SessionLocal
from .routes import router

app = FastAPI()

# Initialize the database
create_tables()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(router)
