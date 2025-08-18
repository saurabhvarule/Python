
import array

arr = array.array('i', [])

ln = int(input("Enter length of array : "))

for i in range(ln):

    temp = int(input())
    arr.append(temp)

num = int(input("Enter the number to search : "))

if num in arr:

    print(arr.index(num))

else:
    print("Element not found")
