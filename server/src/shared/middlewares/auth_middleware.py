from functools import wraps
from flask import request
from config import variables
import jwt
from jwt.exceptions import (
    DecodeError,
    InvalidTokenError,
    InvalidSignatureError
)


def auth_middleware(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'authorization' not in request.headers:
            raise InvalidTokenError('Invalid token')
        header_token = request.headers['authorization']
        token_parts = header_token.split(' ')
        if len(token_parts) != 2:
            raise InvalidTokenError('Invalid token')
        [scheme, token] = token_parts
        if scheme.strip() != 'Bearer':
            raise InvalidSignatureError('Invalid token signature')
        try:
            jwt.decode(token, variables.SECRET_KEY, algorithms=['HS256'])
            return func(*args, **kwargs)
        except DecodeError as err:
            print(err.__repr__())
            raise DecodeError('Token could not be decoded')
    return decorated_function
