x = int(input("Enter a minimum number  : "))
y = int(input("Enter a maximum number  : "))
i=x
if(i % 2 == 0):
    i=x+1
while i<=y:         #while loop testing
    print(i)
    i=i+2
