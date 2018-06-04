from bottle import request, response
from functools import wraps


VALID_TOKENS = {'testtoken', }


def is_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.query.get('token', '')
        if token.lower() in VALID_TOKENS:
            return func(*args, **kwargs)
        else:
            response.status = 401
            return response
    return wrapper
