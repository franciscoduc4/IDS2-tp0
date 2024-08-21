from fastapi import FastAPI
from .config import DevelopmentConfig, ProductionConfig, TestingConfig
from .models import create_tables
from .routes import router

app = FastAPI()

# Initialize the database
create_tables()

app.include_router(router)
