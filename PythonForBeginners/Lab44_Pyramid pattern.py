s = int(input("Enter the number of rows you want to print : "))
for i in range(1, s + 1):
    print("_" * (s - i), end="")
    print("*_" * i)
print("---------------------------------")
