# This file is an exercise on decorators

def add_tags(*tags):
    def decorator(old_function):
        def inside(*args, **kwargs):
            code = old_function(*args, **kwargs)
            for tag in reversed(tags):
                code = "<{0}><{1}></{0}>".format(tag, code)
            return code
        return inside
    return decorator

@add_tags("p", "i", "b")
def my_web_welcome(name):
    return "Welcome " + name + " to my blog!"

print(my_web_welcome("Steven"))