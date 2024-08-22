# app/schemas.py
from pydantic import BaseModel

class SnapMsgCreate(BaseModel):
    message: str
