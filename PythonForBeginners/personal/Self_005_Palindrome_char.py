lst1 = input("Enter the string which you want to check: ")
print(lst1,type(lst1))
lst2 = reversed(lst1)
if lst2 == lst1:
    print(f"{lst1} is palindrome")
else:
    print(f"{lst1} is not palindrome")

lst3 = lst1[::-1]
if lst3 == lst1:
    print(f"{lst1} is palindrome")
else:
    print(f"{lst1} is not palindrome")

print(lst1,type(lst1))
print(lst2,type(lst2))
print(lst3,type(lst3))
