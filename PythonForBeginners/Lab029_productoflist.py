lst = [1, 2, 3, 4, 5]
prod = 1
for i in lst:
    prod *= i
print(f"Product of the list is {prod}")

print("\n***************** Program for factorial********************")
fact = int(input("Enter the number whose factorial you want to get : "))
p = 1
for i in range(1, fact+1):
    p *= i
print(f"Factorial of {fact} is {p}")
print(type(p))