
import array

arr1 = array.array('u', [])
arr2 = array.array('u', [])

ln = int(input("Enter length of array : "))
print("Enter elements in the first array")

for i in range(ln):

    temp = input()
    arr1.append(temp)

print("Enter elements in the second array")

for i in range(ln):

    temp = input()
    arr2.append(temp)

for i in range(ln):

    if(arr1[i] > arr2[i]):
        print(arr1[i], "-", arr2[i], "=", ord(arr1[i]) - ord(arr2[i]))
    else:
        print(arr2[i], "-", arr1[i], "=", ord(arr2[i]) - ord(arr1[i]))
