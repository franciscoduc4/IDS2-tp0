from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.schemas.schemas import SnapMsgCreate, SnapMsgBase, SnapMsgList, ErrorResponse, SnapMsgResponse
from app.models.model import SnapMsg
from app.database import get_db
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/snaps", response_model=SnapMsgResponse, status_code=status.HTTP_201_CREATED)
async def create_snap(snap: SnapMsgCreate, db: Session = Depends(get_db)):
    new_snap = SnapMsg(message=snap.message)
    db.add(new_snap)
    db.commit()
    db.refresh(new_snap)
    return SnapMsgResponse(data=SnapMsgBase.model_validate(new_snap))

@router.get("/snaps", response_model=SnapMsgList)
async def get_snaps(db: Session = Depends(get_db)):
    snaps = db.query(SnapMsg).all()
    return SnapMsgList(data=[SnapMsgBase.model_validate(snap) for snap in snaps])

@router.get("/snaps/{id}", response_model=SnapMsgResponse)
async def get_snap_by_id(id: str, db: Session = Depends(get_db)):
    snap = db.query(SnapMsg).filter(SnapMsg.id == id).first()
    if snap is None:
        raise HTTPException(status_code=404, detail="Snap not found")
    return SnapMsgResponse(data=SnapMsgBase.model_validate(snap))

@router.delete("/snaps/{id}", responses={
    204: {"description": "Snap deleted successfully"},
})
async def delete_snap_by_id(id: str, db: Session = Depends(get_db)):
    snap = db.query(SnapMsg).filter(SnapMsg.id == id).first()
    if snap is None:
        raise HTTPException(status_code=404, detail="Snap not found")
    db.delete(snap)
    db.commit()
    return JSONResponse(status_code=204, content={})
