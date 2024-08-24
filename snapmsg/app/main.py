from fastapi import FastAPI
from app.routes import router
from app.logging_config import setup_logging
from app.config import Config
from app.database import init_db
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

setup_logging()

app = FastAPI()

init_db()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    details = exc.errors()
    formatted_details = []
    for error in details:
        formatted_details.append({
            "loc": error["loc"],
            "msg": error["msg"],
            "type": error["type"],
            "ctx": error.get("ctx", {"max_length": 280})
        })
    
    return JSONResponse(
        status_code=400,
        content={
            "type": "about:blank",
            "title": "Bad Request",
            "status": 400,
            "detail": formatted_details,
            "instance": str(request.url)
        }
    )