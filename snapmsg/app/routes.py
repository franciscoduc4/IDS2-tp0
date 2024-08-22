# app/routes.py

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from app.models import SnapMsg

router = APIRouter()

@router.post("/snaps", status_code=201)
async def create_snap(request: Request):
    body = await request.json()
    message = body.get("message")
    if not message:
        raise HTTPException(status_code=400, detail="Message is required")
    snap = SnapMsg.add_snap(message)
    return {"data": {"id": snap.id, "message": snap.message}}

@router.get("/snaps")
async def get_snaps():
    snaps = SnapMsg.get_all_snaps()
    return {"data": [{"id": snap.id, "message": snap.message} for snap in snaps]}
