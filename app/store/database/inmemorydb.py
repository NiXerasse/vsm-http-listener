import typing

if typing.TYPE_CHECKING:
    from app.store.database.models import TerminalData


class InmemoryDB:
    def __init__(self):
        self.db = {}

    def add(self, data: "TerminalData"):
        self.db[data.name] = data

    def __str__(self):
        return '\n'.join(
            f'{terminal.name}: {terminal.ip} {terminal.mac}'
            for terminal in sorted(self.db.values(), key=lambda d: d.name)
        )
