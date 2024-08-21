from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from .config import Config

# Use the database URL from the configuration
engine = create_engine(Config.DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()

class SnapMsg(Base):
    __tablename__ = "snaps"
    
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, index=True)

def create_tables():
    Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
