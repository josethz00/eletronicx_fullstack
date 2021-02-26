from functools import wraps
from flask import request
from werkzeug.exceptions import Unauthorized

from src.modules.users.user import User


def role_middleware(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in request.headers:
            raise KeyError('Invalid id')

        user_id = request.headers['user_id']
        user = User.query.get_or_404(user_id)

        if user.role == 'admin':
            return func(*args, **kwargs)
        raise Unauthorized('Not enough permissions')
    return decorated_function
