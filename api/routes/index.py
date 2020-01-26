from aiohttp import web


async def handle_index_get(request):
    data = {"success": True}
    return web.json_response(data)


routes = [
    web.get('/', handle_index_get)
]
