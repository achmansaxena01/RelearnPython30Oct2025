# Method 1
s = input("1 : Enter the string to reverse: ")
print(s[::-1]) #reversal using slicing

#Method 2
s = input("2 : Enter the string to reverse again: ")
i = len(s) - 1
while i >= 0:
    print(s[i], end="")
    i -= 1
print("\n")

#Method 3
s = input("3: Enter the string to reverse again: ")
result = ''
i = len(s) - 1
while i >= 0:
    result += s[i]
    i -= 1
print(result)

#Method 4
m = '-'.join(['a','b','c'])
print(m)
s = input("4: Enter the string to reverse again: ")
print(''.join(reversed(s)))
