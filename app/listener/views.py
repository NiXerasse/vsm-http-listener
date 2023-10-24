import logging

from aiohttp import web
from app.store.database.models import TerminalData
import json


async def index(request: web.Request):
    return web.Response(text="This is http-listener service for FaceID system.")


async def post(request: web.Request):
    content: bytes = await request.content.read()
    json_data: dict = json.loads(content[69:-21].decode().replace('\n', '').replace('\t', ''))
    try:
        terminal_name: str = json_data['AccessControllerEvent']['deviceName']
        terminal_mac: str = json_data['macAddress']
        terminal_ip: str = json_data['ipAddress']
        request.app["db"].db.add(TerminalData(terminal_name, terminal_ip, terminal_mac))
    except KeyError:
        logging.error("Failed to collect all data from json")
        logging.error(json_data)
