import logging
import re

from aiohttp import web
from app.store.database.models import TerminalData
import json


async def index(request: web.Request):
    return web.Response(text="This is http-listener service for FaceID system.")


async def post(request: web.Request):
    content: bytes = await request.content.read()
    json_str = re.findall(r'(?s)MIME.*?(\{.*}).*MIME', content[:1100].decode())[0]
    json_data: dict = json.loads(json_str)
    terminal_name: str = json_data['AccessControllerEvent']['deviceName']
    terminal_ip: str = json_data['ipAddress']
    terminal_mac: str = json_data.get('macAddress', '')
    request.app["db"].db.add(TerminalData(terminal_name, terminal_ip, terminal_mac))
