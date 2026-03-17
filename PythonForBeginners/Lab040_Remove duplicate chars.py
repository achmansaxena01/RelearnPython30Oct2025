s = 'abcbbbbcccZZZZZIIII'
print(s)
temp = []
for c in s:
    if c not in temp:
        temp.append(c)
print(temp,type(temp))
print(''.join(temp))