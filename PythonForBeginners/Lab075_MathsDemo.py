import math
from math import *

print(sqrt(9))
print(ceil(8.2))
print(floor(7.9))
print(pow(2,3))
print(fabs(-2.2))

print(dir())
for i in dir(math):
    print(i, getattr(math, i))

help(math)