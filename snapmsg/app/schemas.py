from pydantic import BaseModel

class SnapMsg(BaseModel):
    message: str

    class Config:
        from_attributes = True
