# app/models.py
# Estructura simple en memoria
from typing import List, Optional

class SnapMsg:
    _id_counter = 1

    def __init__(self, message: str):
        self.id = SnapMsg._id_counter
        SnapMsg._id_counter += 1
        self.message = message

    @staticmethod
    def get_all_snaps() -> List['SnapMsg']:
        return SnapMsg._snaps

    @staticmethod
    def add_snap(message: str) -> 'SnapMsg':
        snap = SnapMsg(message)
        SnapMsg._snaps.append(snap)
        return snap

    _snaps = []
