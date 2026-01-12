tpl = (20,30,40,20,50,'xyz')
print(type(tpl))
print(tpl*3)
print(tpl.count(20))    # to count the number of times the element is present in the tuple
print(tpl.index(20))   # to find the index of the element present in the tuple

lst = [67,34,'XYZ']
print(type(lst))
tpl1=tuple(lst) # to convert list to a tuple
print(tpl1)
print(type(tpl1))