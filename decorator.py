# Decorator - Add extra features to existing functions

# Existing function


def div(a, b):
    print(a / b)


# Decorate it: Adding feature if a < b then we are swapping it


def smart_div(func):

    def inner_div(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner_div


div = smart_div(div)
div(2, 4)

smart_div(div)(2, 4)
