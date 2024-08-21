import uvicorn
from app import app  # Import app from __init__.py

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
