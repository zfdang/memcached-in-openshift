from functools import wraps
from flask import request, current_app
import types


def cached(timeout=300, key='view%s'):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            cache = current_app.config['cache']  # init cache client first
            cache_key = key % request.path
            # cache_key can only be string, but not unicode
            if isinstance(cache_key, types.UnicodeType):
                cache_key = cache_key.encode("UTF-8")
            rv = cache.get(cache_key)
            if rv is not None:
                current_app.logger.info("cached: find key = %s" % (cache_key))
                return rv
            rv = f(*args, **kwargs)
            cache.set(cache_key, rv, time=timeout)
            current_app.logger.info("cached: set key = %s" % (cache_key))
            return rv
        return decorated_function
    return decorator
