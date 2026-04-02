class Course:
    def __init__(self,name,ratings): #This is parameterised constructor
        self.name = name
        self.ratings = ratings

    def average_rating(self):
        numberOfRatings = len(self.ratings)
        average = sum(self.ratings)/numberOfRatings
        print(f"The average rating of the Course {self.name} is : {average} \n")

C1 = Course("Java",[1,2,3,4,5])
print(C1.name)
print(C1.ratings)
for rating in C1.ratings:
    print(rating)
C1.average_rating()

C2 = Course("Java Web Services",[5,5,5,5])
print(C2.name)
print(C2.ratings)
for rating in C2.ratings:
    print(rating)
C2.average_rating()