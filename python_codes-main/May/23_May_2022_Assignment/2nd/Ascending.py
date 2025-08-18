
import array

arr = array.array('i',[])

ln = int(input("Enter length of array : "))

for i in range(ln):

    temp = int(input())
    arr.append(temp)

print("Original Array :", arr)

for i in range(len(arr)):

    for j in range(len(arr)):
        if(arr[i] < arr[j]):
       
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print("Sorted Array :", arr)
