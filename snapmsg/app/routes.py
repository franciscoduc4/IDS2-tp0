from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.responses import JSONResponse
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

@router.post("/snaps", response_model=SnapMsgResponse, status_code=status.HTTP_201_CREATED)
async def create_snap(snap: SnapMsgCreate, db: Session = Depends(get_db)):
    new_snap = SnapMsg(message=snap.message)
    db.add(new_snap)
    db.commit()
    db.refresh(new_snap)
    return SnapMsgResponse(data=SnapMsgBase.from_orm(new_snap))

@router.get("/snaps", response_model=SnapMsgList)
async def get_snaps(db: Session = Depends(get_db)):
    snaps = db.query(SnapMsg).all()
    return SnapMsgList(data=[SnapMsgBase.from_orm(snap) for snap in snaps])

@router.get("/snaps/{uuid}", response_model=SnapMsgResponse)
async def get_snap_by_uuid(uuid: str, db: Session = Depends(get_db)):
    snap = db.query(SnapMsg).filter(SnapMsg.uuid == uuid).first()
    if snap is None:
        raise HTTPException(status_code=404, detail="Snap not found")
    return SnapMsgResponse(data=SnapMsgBase.from_orm(snap))

@router.get("/snaps/{id}", response_model=SnapMsgResponse)
async def get_snap_by_id(id: int, db: Session = Depends(get_db)):
    snap = db.query(SnapMsg).filter(SnapMsg.id == id).first()
    if snap is None:
        raise HTTPException(status_code=404, detail="Snap not found")
    return SnapMsgResponse(data=SnapMsgBase.from_orm(snap))

@router.delete("/snaps/{id}", responses={
    204: {"description": "Snap deleted successfully"},
})
async def delete_snap_by_id(id: int, db: Session = Depends(get_db)):
    snap = db.query(SnapMsg).filter(SnapMsg.id == id).first()
    if snap is None:
        raise HTTPException(status_code=404, detail="Snap not found")
    db.delete(snap)
    db.commit()
    return JSONResponse(status_code=204, content={})
