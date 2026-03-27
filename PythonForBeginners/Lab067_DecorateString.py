def decorefun(fun):
    def inner(n):
        result = fun(n)
        result += " .How are you?"
        return result
    return inner

@decorefun
def hello(name):
    return "Hello " + name

print(hello("John"))