from aiohttp.web import json_response, post, get

from api.database.users import find_user_by_email
from api.utilities.security import check_password_hash
from api.utilities.token import generate_token, token_required

@token_required
async def handle_user_info(user, request):
    return json_response({'success': True, 'user': user })

async def handle_user_login(request):
    req_data = await request.json()
    if not req_data["email"]:
        return json_response({"success": False, "error": "Missing email"})
    if not req_data["password"]:
        return json_response({"success": False, "error": "Missing password"})
    async with request.app["db_pool"].acquire() as conn:
        user = await find_user_by_email(conn, req_data["email"])
        user_data = dict(user)
        if not check_password_hash(req_data["password"], user_data["password"]):
            return json_response({"success": False, "error": "Wrong password"})
        del user_data["password"]
        token = await generate_token(user_data["email"])
        return json_response(
            {"success": True, "user": user_data, "token": token.decode("UTF-8")}
        )


routes = [
    post("/user/login", handle_user_login),
    get("/user/info", handle_user_info),
]
