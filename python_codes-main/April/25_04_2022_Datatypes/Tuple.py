
tuple1 = (10,20,"Harsh", 12.4)
tuple2 = (10,20,"Harsh", 12.4)
lst1 = [10,20,"Harsh", 12.4]

print(tuple1)
print(tuple2)
print(lst1)

print(id(tuple1[0]))
print(id(tuple2[0]))
print(id(lst1[0]))

lst1[2] = 30 
#tuple1[2] = 30         #Tuple is immutable.

print(tuple1[2])
print(lst1[2])

print(type(tuple1))
print(type(tuple1[0]))
