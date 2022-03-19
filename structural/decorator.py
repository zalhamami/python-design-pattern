""" Decorator is used to add an additional operation to existing
function without modifying the original function """

from functools import wraps

def make_blink(function):
    """ The doc of decorator """
    @wraps(function)

    def decorator():
        original_function = function()

        return '<p>{}</p>'.format(original_function)
    
    return decorator

@make_blink
def hello_world():
    """ Original function! """
    return 'Hello world.'

# Print a function with a decorator
print(hello_world())

print(hello_world.__name__)

print(hello_world.__doc__)
