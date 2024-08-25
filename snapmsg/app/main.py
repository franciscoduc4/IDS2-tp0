from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.controllers.controller import router  
from app.logging_config import setup_logging
from app.config.config import Config
from app.database import init_db  
from app.models.model import SnapMsg  
from app.database import get_db  

# Set up logging for the application
setup_logging()

# Initialize FastAPI application
app = FastAPI()

# Initialize the database
init_db()

# Add CORS middleware to allow all origins, methods, and headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the router for the application
app.include_router(router)

@app.middleware("http")
async def error_handling_middleware(request: Request, call_next):
    """
    Middleware to handle exceptions and return appropriate error responses.

    Args:
        request (Request): The incoming request.
        call_next (Callable): The next middleware or route handler in the chain.

    Returns:
        Response: The response from the next handler or an error response.
    """
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        # Handle unexpected errors
        return JSONResponse(
            status_code=500,
            content={
                "type": "about:blank",
                "title": "Internal Server Error",
                "status": 500,
                "detail": str(e),
                "instance": str(request.url)
            }
        )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    Exception handler for request validation errors.

    Args:
        request (Request): The incoming request.
        exc (RequestValidationError): The validation error.

    Returns:
        JSONResponse: A formatted error response.
    """
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
