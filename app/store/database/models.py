from dataclasses import dataclass
from app.store.database.inmemorydb import InmemoryDB


@dataclass
class TerminalData:
    name: str
    ip: str
    mac: str


db = InmemoryDB()
