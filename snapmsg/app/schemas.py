from pydantic import BaseModel, Field, constr, ConfigDict
from typing import List, Optional, Literal
from uuid import UUID

class SnapMsgBase(BaseModel):
    id: int
    uuid: UUID
    message: str

    model_config = ConfigDict(from_attributes=True)

class SnapMsgCreate(BaseModel):
    message: str = Field(..., max_length=280)

class SnapMsgList(BaseModel):
    data: List[SnapMsgBase]

class SnapMsgResponse(BaseModel):
    data: SnapMsgBase

class ErrorResponse(BaseModel):
    type: Literal["about:blank"] = Field(default="about:blank")
    title: str
    status: int
    detail: str
    instance: str
