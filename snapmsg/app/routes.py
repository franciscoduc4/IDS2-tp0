from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .models import SnapMsg as SnapMsgModel
from .schemas import SnapMsg, SnapMsgResponse, ErrorResponse
from .models import get_db

router = APIRouter()

@router.post("/snaps", status_code=201, response_model=SnapMsgResponse, responses={
    201: {"description": "Snap created successfully", "content": {"application/json": {"schema": SnapMsgResponse}}},
    400: {"description": "Bad request error", "content": {"application/json": {"schema": ErrorResponse}}},
    500: {"description": "Internal server error", "content": {"application/json": {"schema": ErrorResponse}}},
})
def create_snap(snap: SnapMsg, db: Session = Depends(get_db)):
    db_snap = SnapMsgModel(message=snap.message)
    db.add(db_snap)
    db.commit()
    db.refresh(db_snap)
    return {"id": db_snap.id, "message": db_snap.message}

@router.get("/snaps", response_model=dict, responses={
    200: {"description": "A list of snaps", "content": {"application/json": {"schema": dict}}},
    500: {"description": "Internal server error", "content": {"application/json": {"schema": ErrorResponse}}},
})
def get_snaps(db: Session = Depends(get_db)):
    snaps = db.query(SnapMsgModel).all()
    return {"data": [{"id": snap.id, "message": snap.message} for snap in snaps]}
