
import array 

arr = array.array('i', [])

ln = int(input("Enter length of array : "))

for i in range(ln):

    temp = int(input())
    arr.append(temp)

num = int(input("Enter the number to check its Occurrence count : "))
count = 0

for i in arr:
    if(i == num):
        count += 1

if(count > 0):
    print("The occurrence count of number", num, "is", count)
else:
    print("No such element in an array.")
