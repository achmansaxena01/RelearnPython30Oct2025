print("Enter the number")
j = int(input())
k = j
e=0
while j > 0:
    e= j%10+e*10
    j = int(j/10)
print(e)
if e == k:
    print("It is a palindrome")
else:
    print("No , its not a palindrome")

lst = j
print(lst)