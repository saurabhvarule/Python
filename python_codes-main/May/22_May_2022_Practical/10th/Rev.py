
import array

arr = array.array('i', [])

ln = int(input("Enter length of array : "))

for i in range(ln):

    temp = int(input())
    arr.append(temp)

k = 0

while (k < len(arr)-1):

    temp = arr[k] 
    arr[k] = arr[k + 1]
    arr[k + 1] = temp
    k += 2

print(arr)
