from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID as pgUUID
import uuid
from uuid import UUID
from app.database import Base

class SnapMsg(Base):
    __tablename__ = "snapmsgs"

    message = Column(String, index=True)
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
