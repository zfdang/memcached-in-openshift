from functools import wraps
from flask import request, current_app
import types
import time


def cached(timeout=300, key='view%s'):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            stime = time.time()
            cache = current_app.config['cache']  # init cache client first
            cache_key = key % request.path
            # cache_key can only be string, but not unicode
            if isinstance(cache_key, types.UnicodeType):
                cache_key = cache_key.encode("UTF-8")
            rv = cache.get(cache_key)
            if rv is not None:
                current_app.logger.info("cached: find key = %s" % (cache_key))
                elapsed_time = time.time() - stime
                return "Elapsed Time: %f (Cached)\n" % (elapsed_time) + rv
            rv = f(*args, **kwargs)
            cache.set(cache_key, rv, time=timeout)
            current_app.logger.info("cached: set key = %s" % (cache_key))
            elapsed_time = time.time() - stime
            return "Elapsed Time: %f\n" % (elapsed_time) + rv
        return decorated_function
    return decorator
