import asyncio
import logging
import sys

from aiohttp import web
from pyzabbix import ZabbixSender as ZbxSender, ZabbixMetric as ZbxMetric


logger = logging.getLogger(__name__)


class ZabbixSender:
    def __init__(self):
        self.db = None
        self.server = None
        self.interval = None
        self.port = None
        self.host = None
        self.key = None

    def setup(self, app: web.Application):
        self.db = app["db"].db
        self.server = ZbxSender(app["config"]["zabbix"]["server"], app["config"]["zabbix"]["port"])
        self.interval = app["config"]["zabbix"]["interval"]
        self.host = app["config"]["zabbix"]["host"]
        self.key = app["config"]["zabbix"]["key"]

    async def send_to_zabbix(self):
        while True:
            data = str(self.db)
            if data:
                packet = [ZbxMetric(self.host, self.key, data)]
                logger.info(self.server.send(packet))
            await asyncio.sleep(self.interval)
