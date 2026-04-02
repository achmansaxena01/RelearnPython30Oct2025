# use of static fields

class Students:
    major = "CSE"

    def __init__(self, rollno ,name):
        self.rollno = rollno
        self.name = name

s1 = Students(1,"John")
s2 = Students(2,"Doe")

print(s1.major)
print(s2.major)
print(s1.name)
print(s2.name)
print(Students.major)