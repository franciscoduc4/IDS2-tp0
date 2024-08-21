from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .models import SnapMsg as SnapMsgModel, get_db
from .schemas import SnapMsg as SnapMsgSchema

router = APIRouter()

@router.post("/snaps", status_code=201)
def create_snap(snap: SnapMsgSchema, db: Session = Depends(get_db)):
    db_snap = SnapMsgModel(message=snap.message)
    db.add(db_snap)
    db.commit()
    db.refresh(db_snap)
    return {"data": db_snap}

@router.get("/snaps")
def get_snaps(db: Session = Depends(get_db)):
    snaps = db.query(SnapMsgModel).all()
    return {"data": snaps}
