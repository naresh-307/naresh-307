from functools import wraps
def handle_error(f):
    @wraps(f)
    def wrapper(*args, **kwargs):

        try:
            return f(*args,**kwargs)

        except FileNotFoundError:
            print("file not found error....")

    return wrapper