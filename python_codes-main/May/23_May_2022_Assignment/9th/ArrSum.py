
import array

arr1 = array.array('i', [])
arr2 = array.array('i', [])
sumarr = array.array('i', [])

ln = int(input("Enter length of array : "))

print("Enter elements in the first array :")

for i in range(ln):

    temp = int(input())
    arr1.append(temp)

print("Enter elements in the second array :")

for i in range(ln):

    temp = int(input())
    arr2.append(temp)

for i in range(len(arr1)):

    sum = arr1[i] + arr2[i]
    sumarr.append(sum)

print(arr1)
print(arr2)
print(sumarr)
