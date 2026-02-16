students = { "john" : ["python","Django","DRF"],
             "Bob" : ["Java","Spring"],
             "Jim" : ["Js","node","react"]}

keys = students.keys()
print(keys)

for eachkeys in keys:
    print("Courses attended by " , eachkeys ," are :")
    for eachcourse in students[eachkeys]:
        print(eachcourse)
    print("---------------")

