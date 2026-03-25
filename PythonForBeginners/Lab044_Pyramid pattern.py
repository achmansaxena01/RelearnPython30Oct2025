n = int(input("Enter the number of rows you want to print : "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("* " * i)
print("---------------------------------")
