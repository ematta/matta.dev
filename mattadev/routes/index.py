import aiohttp_jinja2

from aiohttp import web
from aiohttp_security import remember, forget, authorized_userid


async def handle_index_get(request):
    return True


routes = [
    web.get('/', handle_index_get)
]
