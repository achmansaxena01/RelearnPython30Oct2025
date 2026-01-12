# List : can store any number of objects dynamically and maintain their order
# it is mutable and changing, and it can not be a key to the dictionary

lst = []  # declare empty list
print(type(lst))
print(lst)

lst1 = [10, 20, 10, 5, 6, 98, 87, 'bharat', 'achman', -10, 30.5]
print(type(lst1))
print(lst1)
print(lst1[5:9])
print(lst1 * 2)

lst1.append(100)    # add an element at the end of list
print(lst1)
lst1.insert(0,200)    # add an element at the given index in list

lst1.remove('bharat')    # remove the element from the list by value
lst1.remove('achman')    # remove the element from the list by value
print(lst1)

del(lst1[2])    # remove an element by index
print(lst1)

print(max(lst1))    #to find a maximum number in the given list
print(min(lst1))    #to find a Minimum number in the given list
lst1.sort()  # to sort the list
print(lst1)
lst1.sort(reverse=True)   # to sort the list in reverse
print(lst1)

lst1.clear()    #to clear the list
print(lst1)