# database.py

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
import uuid
from sqlalchemy.dialects.postgresql import UUID as pgUUID

# Get the database URL from environment variables, defaulting to a SQLite database if not set
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./test.db')

# Create the database engine, with special configuration for SQLite
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(DATABASE_URL)

# Create a sessionmaker, which will be used to create database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models
Base = declarative_base()

def init_db():
    """
    Initialize the database by dropping all existing tables and creating new ones.
    This function should be used with caution as it will erase all data in the database.
    """
    Base.metadata.drop_all(bind=engine)  
    Base.metadata.create_all(bind=engine)

def get_db():
    """
    Generator function to get a database session.
    This function creates a new SessionLocal instance, yields it, and then closes it when done.
    It's designed to be used with FastAPI's dependency injection system.

    Yields:
        SessionLocal: A SQLAlchemy database session

    Example:
        @app.get("/")
        def read_root(db: Session = Depends(get_db)):
            # Use the db session here
            pass
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
