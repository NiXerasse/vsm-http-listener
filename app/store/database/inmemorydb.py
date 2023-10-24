import logging
import typing

if typing.TYPE_CHECKING:
    from app.store.database.models import TerminalData


class InmemoryDB:
    def __init__(self):
        self.db = {}

    def add(self, data: "TerminalData"):
        if data.ip in self.db:
            if self.db[data.ip].name != data.name or self.db[data.ip].mac != data.mac:
                logging.info(f'Updated terminal: {data.name} {data.ip} {data.mac}')
        else:
            logging.info(f'Added terminal: {data.name} {data.ip} {data.mac}')
        self.db[data.ip] = data

    def __str__(self):
        return '\n'.join(
            f'{terminal.name.ljust(20, " ")}{terminal.ip.rjust(15, " ")}    {terminal.mac}'
            for terminal in sorted(self.db.values(), key=lambda d: d.name)
        )
