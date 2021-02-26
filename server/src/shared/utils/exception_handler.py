import json
from werkzeug.exceptions import HTTPException
from jwt.exceptions import PyJWTError


def exception_handler(error: Exception) -> json:
    code = 500
    if isinstance(error, HTTPException):
        code = error.code
    elif isinstance(error, PyJWTError):
        code = 401
    return json.dumps({'error': error.__repr__()}), code
