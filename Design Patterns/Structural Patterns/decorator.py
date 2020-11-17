from functools import wraps


def make_blink(function):
    @wraps(function)
    def decorator():
        ret = function()
        return f"<blink>{ret}</blink>"

    return decorator

@make_blink
def hello_world():
    """ Original function """
    return "Hello world!"


print(hello_world())
print(hello_world.__name__)
print(hello_world.__doc__)