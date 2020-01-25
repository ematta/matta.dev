from aiohttp import web


routes = web.RouteTableDef()


@routes.post("/user/login")
async def handle_user_get(request):
    data = {"success": True, "user": request.match_info.get("name", "Anonymous")}
    return web.json_response(data)
