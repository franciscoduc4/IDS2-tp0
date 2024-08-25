from app.repositories.repository import SnapMsgRepository  
from app.schemas.schemas import SnapMsgBase  
from sqlalchemy.orm import Session

class SnapMsgService:
    def __init__(self, db: Session):
        self.repository = SnapMsgRepository(db)

    def create_snap(self, message: str) -> SnapMsgBase:
        return self.repository.create_snap(message)

    def get_all_snaps(self) -> list[SnapMsgBase]:
        return self.repository.get_all_snaps()

    def get_snap_by_id(self, id: str) -> SnapMsgBase:
        return self.repository.get_snap_by_id(id)

    def delete_snap_by_id(self, id: int):
        self.repository.delete_snap_by_id(id)
