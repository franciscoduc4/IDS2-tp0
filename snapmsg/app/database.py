# database.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
import uuid
from sqlalchemy.dialects.postgresql import UUID as pgUUID


DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./test.db')

if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class SnapMsg(Base):
    __tablename__ = "snapmsgs"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, index=True)
    uuid = Column(String, unique=True, default=lambda: str(uuid.uuid4()))  # Use String for SQLite

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
