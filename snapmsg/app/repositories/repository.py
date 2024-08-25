from sqlalchemy.orm import Session
from app.models.snapmsg_model import SnapMsg

class SnapMsgRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_snap(self, message: str) -> SnapMsg:
        new_snap = SnapMsg(message=message)
        self.db.add(new_snap)
        self.db.commit()
        self.db.refresh(new_snap)
        return new_snap

    def get_all_snaps(self):
        return self.db.query(SnapMsg).all()

    def get_snap_by_id(self, id: str) -> SnapMsg:
        return self.db.query(SnapMsg).filter(SnapMsg.id == id).first()

    def delete_snap_by_id(self, id: str):
        snap = self.db.query(SnapMsg).filter(SnapMsg.id == id).first()
        if snap:
            self.db.delete(snap)
            self.db.commit()
