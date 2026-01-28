# Dictionary
from pickle import APPEND

Dic1 = {1:"John", 2:"Bill", 3:"Doe"}
print(Dic1)
print(type(Dic1[1]))

print(Dic1.keys())
K1 = Dic1.keys()
for i in K1: print(i)

print(Dic1.values())
V1 = Dic1.values()
for i in V1: print(i)

print(Dic1[3])

del Dic1[2] #to delete a value from Dictionary
print(Dic1)

Dic1[4] = "John"    #to add value to a dictionary
print(Dic1)
