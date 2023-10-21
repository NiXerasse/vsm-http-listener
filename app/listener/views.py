from aiohttp import web
import json


async def index(request: web.Request):
    return web.Response(text="This is http-listener service for FaceID system.")


async def post(request: web.Request):
    content: bytes = await request.content.read()
    json_data: dict = json.loads(content[69:-21].decode().replace('\n', '').replace('\t', ''))
    terminal_name: str = json_data['AccessControllerEvent']['deviceName']
    terminal_mac: str = json_data['macAddress']
    terminal_ip: str = json_data['ipAddress']
    print(f'Terminal: {terminal_name} -> {terminal_ip} ({terminal_mac})')
