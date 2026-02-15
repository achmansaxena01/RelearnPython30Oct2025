import math

r = float(input("Please enter the radius of the circle : "))
area1 = r * r * (22/7)
area2 = math.pi * (r ** 2)
print(f"The area1 of the circle with radius {r} is {area1}")
print(f"The area2 of the circle with radius {r} is {area2}")