from pydantic import BaseModel
from typing import Optional, List

class SnapMsg(BaseModel):
    message: str

class SnapMsgResponse(BaseModel):
    id: int
    message: str

class ErrorResponse(BaseModel):
    type: str = "about:blank"
    title: str
    status: int
    detail: Optional[str] = None
    instance: Optional[str] = None

class SnapsListResponse(BaseModel):
    data: List[SnapMsgResponse]
