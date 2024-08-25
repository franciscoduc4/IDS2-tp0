# app/config.py
import os

class Config:
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', 8080))
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./app.db')  