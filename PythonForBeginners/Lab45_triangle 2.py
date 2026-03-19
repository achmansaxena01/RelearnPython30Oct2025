rows = int(input("enter the number of rows: "))
for i in range(1, rows + 1):
    for j in range(5-i):
        print('_', end='')
    for k in range(i):
        print('*', end='')
    print("")
print("----------------------------------------------------------------------")
for c in range(1,rows+1):
    print('_' * (rows-c),'* ' * c)
print("----------------------------------------------------------------------")