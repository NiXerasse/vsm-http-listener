from aiohttp import web

async def index(request):
    return web.Response(text="This is a test app!")

async def post(request):
    print(f"Request: {request}")