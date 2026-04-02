a = [2,4,6,8,10]
b = [1,2,3,4,5]

result1 = []
for i in a:
    if i in b:
        result1.append(i)
print(result1)

result2 = [i for i in a if i in b]
print(result2)

