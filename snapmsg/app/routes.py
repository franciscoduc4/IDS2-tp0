from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .schemas import SnapMsgCreate, SnapMsgBase, SnapMsgList, ErrorResponse, SnapMsgResponse
from .database import SessionLocal, SnapMsg
import logging
from pydantic import ValidationError

router = APIRouter()
logger = logging.getLogger(__name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/snaps", response_model=SnapMsgResponse, status_code=status.HTTP_201_CREATED, responses={ 
    201: {"description": "Snap created successfully", "model": SnapMsgResponse},
    400: {"description": "Bad request error", "model": ErrorResponse},
    500: {"description": "Internal server error", "model": ErrorResponse}
})
async def create_snap(snap: SnapMsgCreate, db: Session = Depends(get_db)):
    try:
        new_snap = SnapMsg(message=snap.message)
        db.add(new_snap)
        db.commit()
        db.refresh(new_snap)
        return SnapMsgResponse(data=SnapMsgBase.from_orm(new_snap))
    
    except ValidationError as e:
        logger.error(f"Validation error: {e}")
        return JSONResponse(
            status_code=400,
            content=ErrorResponse(
                type="about:blank",
                title="Bad Request",
                status=400,
                detail=str(e),
                instance="/snaps"
            ).dict()
        )
    
    except HTTPException as e:
        return JSONResponse(
            status_code=e.status_code,
            content=ErrorResponse(
                type="about:blank",
                title=e.detail,
                status=e.status_code,
                detail=str(e.detail),
                instance="/snaps"
            ).dict()
        )
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return JSONResponse(
            status_code=500,
            content=ErrorResponse(
                type="about:blank",
                title="Internal Server Error",
                status=500,
                detail=str(e),
                instance="/snaps"
            ).dict()
        )

@router.get("/snaps", response_model=SnapMsgList, responses={500: {"model": ErrorResponse}})
async def get_snaps(db: Session = Depends(get_db)):
    logger.info("Received request to get all snaps")
    try:
        snaps = db.query(SnapMsg).all()
        logger.info(f"Retrieved {len(snaps)} snaps from database")
        return SnapMsgList(data=[SnapMsgBase.from_orm(snap) for snap in snaps])
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return JSONResponse(
            status_code=500,
            content=ErrorResponse(
                type="about:blank",
                title="Internal Server Error",
                status=500,
                detail=str(e),
                instance="/snaps"
            ).dict()
        )


@router.get("/snaps/{uuid}", response_model=SnapMsgResponse, responses={
    404: {"description": "Snap not found", "model": ErrorResponse},
    500: {"description": "Internal server error", "model": ErrorResponse}
})
async def get_snap_by_uuid(uuid: str, db: Session = Depends(get_db)):
    logger.info(f"Received request to get snap with UUID: {uuid}")
    try:
        snap = db.query(SnapMsg).filter(SnapMsg.uuid == uuid).first()
        if snap is None:
            logger.warning(f"Snap with UUID {uuid} not found")
            raise HTTPException(status_code=404, detail="Snap not found")
        return SnapMsgResponse(data=SnapMsgBase.from_orm(snap))
    
    except HTTPException as e:
        return JSONResponse(
            status_code=e.status_code,
            content=ErrorResponse(
                type="about:blank",
                title=e.detail,
                status=e.status_code,
                detail=str(e.detail),
                instance=f"/snaps/{uuid}"
            ).dict()
        )
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return JSONResponse(
            status_code=500,
            content=ErrorResponse(
                type="about:blank",
                title="Internal Server Error",
                status=500,
                detail=str(e),
                instance=f"/snaps/{uuid}"
            ).dict()
        )
