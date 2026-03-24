def calc(a, b):
    w = a + b
    x = a - b
    y = a * b
    z = a / b
    return w, x, y, z

lst = calc(10,5)
print(f"return value from function is : {lst}" , type(lst) ,"\n")
for i in lst:
    print(i)


