# app/main.py

from fastapi import FastAPI
from app.routes import router
from app.logging_config import setup_logging
from app.config import Config

setup_logging()

app = FastAPI()

app.include_router(router)

@app.on_event("startup")
async def startup_event():
    # Perform startup actions if necessary
    pass

@app.on_event("shutdown")
async def shutdown_event():
    # Perform shutdown actions if necessary
    pass
