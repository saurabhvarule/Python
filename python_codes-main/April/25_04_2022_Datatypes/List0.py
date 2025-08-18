
lst1 = [10,20,30,'A']
lst2 = [10,20,30,'A']

x = 10

lst1[3] = 40
print(lst1[3])

print(id(lst1[0]))
print(id(lst2[0]))
print(id(x))

print(id(lst1))
print(id(lst2))

print(lst1)
print(lst2)

