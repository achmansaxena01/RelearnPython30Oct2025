s = input("Enter a string: ")
print(s)
temp = s.split()
print(temp,type(temp))
result = []
i = len(temp)-1
while i >= 0:
    result.append(temp[i])
    i -= 1
print(result)
print(' '.join(result))
