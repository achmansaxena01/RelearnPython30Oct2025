class Programmer:
    def setName(self,n):
        self.name = n

    def getName(self):
        return self.name

    def setSalary(self,sal):
        self.salary = sal

    def getSalary(self):
        return self.salary

    def setTechnology(self,techs):
        self.technology = techs

    def getTechnology(self):
        return self.technology

p1= Programmer()
p1.setName("John")
p1.setSalary(10000)
p1.setTechnology(["Python","Java","Spring","Hibernate"])

print(p1.getName())
print(p1.getSalary())
print(p1.getTechnology())
