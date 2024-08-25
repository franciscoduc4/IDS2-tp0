from app.repositories.repository import SnapMsgRepository  
from app.schemas.schemas import SnapMsgBase  
from sqlalchemy.orm import Session

class SnapMsgService:
    """
    Service class for handling SnapMsg-related operations.
    
    This class acts as an intermediary between the controller and the repository,
    providing an abstraction layer for business logic related to SnapMsg entities.
    """

    def __init__(self, db: Session):
        """
        Initialize the SnapMsgService with a database session.

        Args:
            db (Session): SQLAlchemy database session.
        """
        self.repository = SnapMsgRepository(db)

    def create_snap(self, message: str) -> SnapMsgBase:
        """
        Create a new snap message.

        Args:
            message (str): The content of the snap message.

        Returns:
            SnapMsgBase: The created snap message.
        """
        return self.repository.create_snap(message)

    def get_all_snaps(self) -> list[SnapMsgBase]:
        """
        Retrieve all snap messages.

        Returns:
            list[SnapMsgBase]: A list of all snap messages.
        """
        return self.repository.get_all_snaps()

    def get_snap_by_id(self, id: str) -> SnapMsgBase:
        """
        Retrieve a specific snap message by its ID.

        Args:
            id (str): The ID of the snap message to retrieve.

        Returns:
            SnapMsgBase: The requested snap message.
        """
        return self.repository.get_snap_by_id(id)

    def delete_snap_by_id(self, id: int):
        """
        Delete a specific snap message by its ID.

        Args:
            id (int): The ID of the snap message to delete.
        """
        self.repository.delete_snap_by_id(id)
