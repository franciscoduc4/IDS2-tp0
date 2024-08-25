from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.schemas.schemas import SnapMsgCreate, SnapMsgBase, SnapMsgList, ErrorResponse, SnapMsgResponse
from app.models.model import SnapMsg
from app.database import get_db
import logging

# Create a router instance for handling HTTP requests
router = APIRouter()

# Set up logging for this module
logger = logging.getLogger(__name__)

@router.post("/snaps", response_model=SnapMsgResponse, status_code=status.HTTP_201_CREATED)
async def create_snap(snap: SnapMsgCreate, db: Session = Depends(get_db)):
    """
    Create a new snap message.

    Args:
        snap (SnapMsgCreate): The snap message to be created.
        db (Session): The database session.

    Returns:
        SnapMsgResponse: The created snap message.
    """
    new_snap = SnapMsg(message=snap.message)
    db.add(new_snap)
    db.commit()
    db.refresh(new_snap)
    return SnapMsgResponse(data=SnapMsgBase.model_validate(new_snap))

@router.get("/snaps", response_model=SnapMsgList)
async def get_snaps(db: Session = Depends(get_db)):
    """
    Retrieve all snap messages.

    Args:
        db (Session): The database session.

    Returns:
        SnapMsgList: A list of all snap messages.
    """
    snaps = db.query(SnapMsg).all()
    return SnapMsgList(data=[SnapMsgBase.model_validate(snap) for snap in snaps])

@router.get("/snaps/{id}", response_model=SnapMsgResponse)
async def get_snap_by_id(id: str, db: Session = Depends(get_db)):
    """
    Retrieve a specific snap message by its ID.

    Args:
        id (str): The ID of the snap message to retrieve.
        db (Session): The database session.

    Returns:
        SnapMsgResponse: The requested snap message.

    Raises:
        HTTPException: If the snap message is not found.
    """
    snap = db.query(SnapMsg).filter(SnapMsg.id == id).first()
    if snap is None:
        raise HTTPException(status_code=404, detail="Snap not found")
    return SnapMsgResponse(data=SnapMsgBase.model_validate(snap))

@router.delete("/snaps/{id}", responses={
    204: {"description": "Snap deleted successfully"},
})
async def delete_snap_by_id(id: str, db: Session = Depends(get_db)):
    """
    Delete a specific snap message by its ID.

    Args:
        id (str): The ID of the snap message to delete.
        db (Session): The database session.

    Returns:
        JSONResponse: An empty response with a 204 status code.

    Raises:
        HTTPException: If the snap message is not found.
    """
    snap = db.query(SnapMsg).filter(SnapMsg.id == id).first()
    if snap is None:
        raise HTTPException(status_code=404, detail="Snap not found")
    db.delete(snap)
    db.commit()
    return JSONResponse(status_code=204, content={})
