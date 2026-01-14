# sets : does not allow duplicates
# It does not retain the insertion order
# we can not perform indexing,slicing and repetition
# once set is frozen we can not perform the update and remove from set
Set1 = {10, 20, 30, 40, 50, 'XYZ', 'ABC', 'ABC', 10, 20}
print(Set1)
print(type(Set1))

Set1.update([23, 78, 99])  # to add an element
print(Set1)

Set1.remove(78)  # to remove an element
print(Set1)

Set1.discard(23)  # to remove an element
print(Set1)

f = frozenset(Set1)
print(f)

# f.update[2]    # can not add a value to frozen set
# f.remove[2]    # can not delete value from frozen set