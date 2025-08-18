
import array

arr = array.array('i', [])
min = 100000000
max = 0

ln = int(input("Enter length of array : "))

for i in range(ln):

    temp = int(input())
    arr.append(temp)

for i in arr:

    if(max < i):
        max = i
    if(min > i):
        min = i

print("Min :", min)
print("Max :", max)
