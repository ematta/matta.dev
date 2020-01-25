from aiohttp import web
from aiohttp_security import remember, forget, authorized_userid


async def handle_index_get(request):
    data = {"success": True}
    return web.json_response(data)


routes = [
    web.get('/', handle_index_get)
]
