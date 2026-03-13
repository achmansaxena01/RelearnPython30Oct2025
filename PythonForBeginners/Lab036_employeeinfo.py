n = int(input("Enter the number of employees  "))
employees = {}
for i in range(n):
    name = input("Enter employee name: ")
    salary = int(input("Enter employee salary: "))
    employees[name] = salary
print("you can knows the salary of employees by giving the name")
while True:
    name = input("Enter employee name: ")
    salary = employees.get(name, -1)
    if salary == -1:
        print("Employee does not exist")
    else:
        print("The salary of the employee is", salary)
    choice = input("Do you want to know the salary of an other employee[Yes/No] : ")
    if choice == ("No" or "no"):
        break
