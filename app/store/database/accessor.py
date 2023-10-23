from app.store.database.models import db


class InmemoryAccessor:
    def __init__(self):
        self.db = db
