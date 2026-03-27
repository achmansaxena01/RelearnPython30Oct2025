# generators are the function which return sequence of values
# it use yield statements : storing each generated value and then return at the end

def customgen(x,y):
    while x<y:
        yield x
        x+=1

result = customgen(10,18)
'''
print(''.join(result)) expects strings,
but your generator is yielding integers.
join() can only join an iterable of str, not int, so you get a TypeError.'''

for i in result:
    print(i)
