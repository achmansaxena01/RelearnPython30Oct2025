# Immutability : when you try to assign new values then a new memory is allocated
a = 20
b = 20
print(id(a), id(b))
b = 21
print(id(a), id(b))

f = 3.14
c = 5 + 3j
print(id(a), id(b), id(c))
print(c.real, c.imag)

s = "Achman is a good boy"
print(type(s))

lst = [1,2,3,4,5] # sequence of ordered elements
print(type(lst),lst)

b = bytes(lst)
print(type(b),b)

#print("\n---------All values till here are immutable------------")
ba = bytearray(lst)
print(type(ba),ba, "\n")

r1 = range(20)
for i in r1:
    print(i)
print("*************************************************************\n")

r2= range(1,10)
for i in r2:
    print(i)
print("*************************************************************\n")

r3 = range(1,30,3)
for i in r3:
    print(i)
print("*************************************************************\n")

t = (1,2,3,4,5)
print(type(t),t)

s = {3,1,2,9,9,4,5} # set is unordered unique values
print(type(s),s)

fs = frozenset(s)
print(type(fs),fs)

d= {1:100,2:101,3:102,4:102,5:100,6:105,7:106,8:107}
print(type(d),d)

