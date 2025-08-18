
import array;

arr = array.array('i', [])

ln = int(input("Enter length of array : "))

for i in range(ln):

    temp = int(input())
    arr.append(temp)

for i in arr:

    if(i % 2 == 0):
        print(i, end = " ")

print()
