from pydantic import BaseModel, Field, constr, ConfigDict
from typing import List, Optional, Literal
from uuid import UUID

class SnapMsgBase(BaseModel):
    """
    Base model for a snap message.

    Attributes:
        id (UUID): Unique identifier for the snap message.
        message (str): Content of the snap message.
    """
    id: UUID
    message: str

    model_config = ConfigDict(from_attributes=True)

class SnapMsgCreate(BaseModel):
    """
    Model for creating a new snap message.

    Attributes:
        message (str): Content of the snap message, limited to 280 characters.
    """
    message: str = Field(..., max_length=280)

class SnapMsgList(BaseModel):
    """
    Model for a list of snap messages.

    Attributes:
        data (List[SnapMsgBase]): List of snap messages.
    """
    data: List[SnapMsgBase]

class SnapMsgResponse(BaseModel):
    """
    Model for a single snap message response.

    Attributes:
        data (SnapMsgBase): A single snap message.
    """
    data: SnapMsgBase

class ErrorResponse(BaseModel):
    """
    Model for error responses.

    Attributes:
        type (str): Error type, always set to "about:blank".
        title (str): Brief error description.
        status (int): HTTP status code.
        detail (str): Detailed error message.
        instance (str): URI of the request that caused the error.
    """
    type: Literal["about:blank"] = Field(default="about:blank")
    title: str
    status: int
    detail: str
    instance: str
