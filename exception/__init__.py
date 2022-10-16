from functools import wraps
from logger import logger

def error_handler(func):
    @wraps(func)
    def handle_error(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            logger.error('file not found')
            return "Input file is not available"
        except ZeroDivisionError:
            return "can't division b zero"
    return handle_error,
