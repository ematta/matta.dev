from aiohttp.web import json_response, post

from api.database.users import find_user_by_email
from api.utilities.security import check_password_hash


async def handle_user_login(request):
    form = await request.post()
    if not form['email']:
        return json_response({ 'success': False, 'error': 'Missing email' })
    if not form['password']:
        return json_response({ 'success': False, 'error': 'Missing password' })
    async with request.app['db_pool'].acquire() as conn:
        user = await find_user_by_email(conn, form['email'])
        user_data = dict(user)
        if not check_password_hash(form['password'], user_data['password']):
            return json_response({ 'success': False, 'error': 'Wrong password' })
        del user_data['password']
        return json_response({"success": True, "user": user_data})


routes = [
    post('/user/login', handle_user_login)
]
