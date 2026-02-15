print("Enter an integer number greater than zero.")
i = int(input())
c = d = 0
print("The input int is :",i)

for j in range(1,i+1):
    if i%j==0:
        c=c+1
if c==2 :
    print("The entered number :",i,"is prime")
else:
    print("The entered number :",i,"is not prime")