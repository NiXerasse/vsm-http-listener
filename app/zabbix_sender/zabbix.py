import asyncio
from aiohttp import web
from pyzabbix import ZabbixSender as ZbxSender, ZabbixMetric as ZbxMetric


class ZabbixSender:
    def __init__(self):
        self.db = None
        self.server = None
        self.interval = None
        self.port = None

    def setup(self, app: web.Application):
        self.db = app["db"].db
        self.server = ZbxSender(app["config"]["zabbix"]["server"], app["config"]["zabbix"]["port"])
        self.interval = app["config"]["zabbix"]["interval"]

    async def send_to_zabbix(self):
        while True:
            data = str(self.db)
            if data:
                packet = [ZbxMetric('1602-NB', 'FaceID.Terminals.Info', data)]
                self.server.send(packet)
                print('---Sending to zabbix---')
                print(data)
                print('---Sent to zabbix!---')
            await asyncio.sleep(self.interval)
