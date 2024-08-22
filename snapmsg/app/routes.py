from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from typing import List
from sqlalchemy.orm import Session
from .schemas import SnapMsgCreate, SnapMsgBase, SnapMsgList, ErrorResponse, SnapMsgResponse
from .database import SessionLocal, SnapMsg
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/snaps", response_model=SnapMsgResponse, responses={
    201: {"description": "Snap created successfully", "model": SnapMsgResponse},
    400: {"description": "Bad request error", "model": ErrorResponse},
    500: {"description": "Internal server error", "model": ErrorResponse}
})
async def create_snap(snap: SnapMsgCreate, db: Session = Depends(get_db)):
    try:
        if not snap.message:
            raise HTTPException(status_code=400, detail="Message cannot be empty")
        new_snap = SnapMsg(message=snap.message)
        db.add(new_snap)
        db.commit()
        db.refresh(new_snap)
        return SnapMsgResponse(data=SnapMsgBase.from_orm(new_snap))
    except HTTPException as e:
        return ErrorResponse(
            type="about:blank",
            title=e.detail,
            status=e.status_code,
            detail=str(e.detail),
            instance="/snaps"
        )
    except Exception as e:
        return ErrorResponse(
            type="about:blank",
            title="Internal Server Error",
            status=500,
            detail=str(e),
            instance="/snaps"
        )

@router.get("/snaps", response_model=SnapMsgList, responses={500: {"model": ErrorResponse}})
async def get_snaps(db: Session = Depends(get_db)):
    try:
        snaps = db.query(SnapMsg).all()
        return SnapMsgList(data=[SnapMsgBase.from_orm(snap) for snap in snaps])
    except Exception as e:
        return ErrorResponse(
            type="about:blank",
            title="Internal Server Error",
            status=500,
            detail=str(e),
            instance="/snaps"
        )