lst = []
print("Enter an integer number greater than one.")
i = int(input())
count = 0
print("The prime number upto input int ", i, " is :")
j = k = 1
for j in range(1, i + 1):
    count = 0
    for k in range(1, j + 1):
        if j % k == 0:
            count = count + 1
    if count == 2:
        lst.append(j)

print(lst)
print("----------------")
