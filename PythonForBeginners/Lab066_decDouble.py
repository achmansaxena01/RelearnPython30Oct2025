# Decorators is a function that perform additional logic on a function.
# it also returns a function as a result
#def my_decorator(func):

def decorfun(fun):
    def inner():
        result = fun()
        return result*2
    return inner

@decorfun
def num():
    return 5

print(num())
