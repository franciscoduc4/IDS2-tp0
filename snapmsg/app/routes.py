from fastapi import FastAPI, HTTPException
from app.models import SnapMsg

app = FastAPI()

snaps = []

@app.post("/snaps", status_code=201)
def create_snap(snap: SnapMsg):
    snap.id = len(snaps) + 1
    snaps.append(snap)
    return {"data": snap}

@app.get("/snaps")
def get_snaps():
    return {"data": snaps}
