
# Nested List

lst = [10, 20, [30, 40, 50], 60]
print(lst[0])
print(lst[2])
print(lst[2][2])
print(lst[3])

lst2 = [10, 20,{30, 40, 50}, (60, 70, 80), [30,100,200], 12, 13, 14]
print(lst2[0])
print(lst2[2])
print(lst2[3])
print(lst2[4][1])
print(lst2.index(30))
