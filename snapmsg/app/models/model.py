from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID as pgUUID
import uuid
from uuid import UUID
from app.database import Base

class SnapMsg(Base):
    """
    Represents a snap message in the database.

    This model defines the structure of the 'snapmsgs' table.

    Attributes:
        message (Column): The content of the snap message. Indexed for faster queries.
        id (Column): The unique identifier for each snap message. 
                     Automatically generated as a UUID string.
    """

    __tablename__ = "snapmsgs"

    message = Column(String, index=True, doc="The content of the snap message")
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), 
                doc="Unique identifier for the snap message")
