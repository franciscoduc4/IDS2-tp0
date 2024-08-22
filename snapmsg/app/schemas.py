from pydantic import BaseModel
from typing import List, Optional

class SnapMsgBase(BaseModel):
    id: int
    message: str

class SnapMsgCreate(BaseModel):
    message: str

class SnapMsgList(BaseModel):
    data: List[SnapMsgBase]

class SnapMsgResponse(BaseModel):
    data: SnapMsgBase


class ErrorResponse(BaseModel):
    type: str
    title: str
    status: int
    detail: str
    instance: str

