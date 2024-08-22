from fastapi import FastAPI
from app.routes import router
from app.logging_config import setup_logging
from app.config import Config
from app.database import init_db

setup_logging()

app = FastAPI()

init_db()

app.include_router(router)
