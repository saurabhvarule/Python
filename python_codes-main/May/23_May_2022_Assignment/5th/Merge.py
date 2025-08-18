
import array

arr1 = array.array('i', [])
arr2 = array.array('i', [])
mArr = array.array('i', [])

ln1 = int(input("Enter length of first array : "))

print("Enter elements of first array : ")

for i in range(ln1):

    temp = int(input())
    arr1.append(temp)

ln2 = int(input("Enter length of second array : "))

for i in range(ln2):

    temp = int(input())
    arr2.append(temp)

for i in range(ln1):
    mArr.append(arr1[i])

for i in range(ln2):
    mArr.append(arr2[i])

print(arr1)
print(arr2)
print(mArr)
