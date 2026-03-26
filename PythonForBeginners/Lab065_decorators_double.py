# Decorators is a function that perform additional logic on a function.
# it also returns a function
#def my_decorator(func):

def decor(fun):
    def inner():
        result = fun()
        return result*2
    return inner

def num():
    return 5

resultfun = decor(num)
print(resultfun())
