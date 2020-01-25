from aiohttp import web


async def handle_user_get(request):
    data = {"success": True, "user": request.match_info.get("name", "Anonymous")}
    return web.json_response(data)


routes = [
    web.post('/user/login', handle_user_get)
]
