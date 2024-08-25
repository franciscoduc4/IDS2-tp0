from sqlalchemy.orm import Session
from app.models.snapmsg_model import SnapMsg

class SnapMsgRepository:
    """
    Repository class for handling database operations related to SnapMsg model.
    """

    def __init__(self, db: Session):
        """
        Initialize the repository with a database session.

        Args:
            db (Session): SQLAlchemy database session.
        """
        self.db = db

    def create_snap(self, message: str) -> SnapMsg:
        """
        Create a new snap message in the database.

        Args:
            message (str): The content of the snap message.

        Returns:
            SnapMsg: The created snap message object.
        """
        new_snap = SnapMsg(message=message)
        self.db.add(new_snap)
        self.db.commit()
        self.db.refresh(new_snap)
        return new_snap

    def get_all_snaps(self):
        """
        Retrieve all snap messages from the database.

        Returns:
            List[SnapMsg]: A list of all snap message objects.
        """
        return self.db.query(SnapMsg).all()

    def get_snap_by_id(self, id: str) -> SnapMsg:
        """
        Retrieve a specific snap message by its ID.

        Args:
            id (str): The ID of the snap message to retrieve.

        Returns:
            SnapMsg: The retrieved snap message object, or None if not found.
        """
        return self.db.query(SnapMsg).filter(SnapMsg.id == id).first()

    def delete_snap_by_id(self, id: str):
        """
        Delete a specific snap message by its ID.

        Args:
            id (str): The ID of the snap message to delete.

        Note:
            This method does not return anything. If the snap message is found,
            it is deleted from the database.
        """
        snap = self.db.query(SnapMsg).filter(SnapMsg.id == id).first()
        if snap:
            self.db.delete(snap)
            self.db.commit()
