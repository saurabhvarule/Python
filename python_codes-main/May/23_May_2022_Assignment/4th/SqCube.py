
import array

arr = array.array('i', [])
arr1 = array.array('i',[])

ln = int(input("Enter length of array : "))

for i in range(ln):

    temp = int(input())
    arr.append(temp)
    
    if(i % 2 == 0):
        arr1.append(temp * temp)

    else:

        arr1.append(temp * temp * temp)

print(arr)
print(arr1)
