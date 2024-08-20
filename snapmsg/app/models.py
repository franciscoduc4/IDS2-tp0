from pydantic import BaseModel

class SnapMsg(BaseModel):
    id: int
    message: str
