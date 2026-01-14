# you can not add or perform/modify on bytes
# you can add or perform/modify on bytearray
list1 = [20,30,40,234]
print(type(list1))
b = bytes(list1)
print(type(b))

b1 = bytearray(list1)
print(type(b1))
b1[2] = 31
print(b1)
