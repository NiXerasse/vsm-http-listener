import asyncio
from aiohttp import web
from app.listener.routes import setup_routes as setup_listener_routes
from app.settings import config
from app.store.database.accessor import InmemoryAccessor
from app.zabbix_sender.zabbix import ZabbixSender

app = web.Application()
zbx = ZabbixSender()


def setup_config(application):
    application["config"] = config


def setup_db(application):
    application["db"] = InmemoryAccessor()


def setup_zabbix(application, zabbix):
    zabbix.setup(application)


def setup_app(application):
    setup_config(application)
    setup_db(application)
    setup_listener_routes(app)


if __name__ == "__main__":
    setup_app(app)
    setup_zabbix(app, zbx)
    asyncio.ensure_future(zbx.send_to_zabbix())
    loop = asyncio.get_event_loop()
    web.run_app(app, port=app["config"]["common"]["port"], loop=loop)
