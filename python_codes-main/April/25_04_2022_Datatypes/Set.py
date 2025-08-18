
# Dictionary is the parent of set in python.
# {} are byfefault considered as dictionary.
# set does not allow duplicate data, if we give duplicate data it keeps first value and other values are ignored.
# set is immutable
# we cannot access elements by index in set

set1 = {10,20,30,10,10,10}
print(set1)

set2 = {10, "harsh", 14.5, True}
print(set2)
#print(set2[1])

set3 = {}
print(type(set3))
