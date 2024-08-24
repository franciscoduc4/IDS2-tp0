from pydantic import BaseModel, Field
from typing import List, Optional, Literal

class SnapMsgBase(BaseModel):
    id: int
    message: str

    class Config:
        from_attributes = True


class SnapMsgCreate(BaseModel):
    message: str


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
