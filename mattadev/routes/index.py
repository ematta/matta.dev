import aiohttp_jinja2

from aiohttp import web
from aiohttp_security import remember, forget, authorized_userid


@aiohttp_jinja2.template('index.html')
async def handle_index_get(request):
    return True


routes = [
    web.get('/', handle_index_get)
]
