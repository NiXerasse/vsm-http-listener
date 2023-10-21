from aiohttp import web

app = web.Application()

if __name__ == "__main__":
    from app.listener.routes import setup_routes as setup_listener_routes
    setup_listener_routes(app)
    web.run_app(app)
