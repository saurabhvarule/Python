
import array

arr = array.array('i', [])

ln = int(input("Enter length of array : "))

for i in range(ln):

    temp = int(input())
    arr.append(temp)

for i in range(len(arr)):
    
    count = 0

    for j in range(len(arr)):

        if(arr[i] == arr[j]):
            count += 1
    
    flag = 0
    
    for j in range(i):
        if(arr[i] == arr[j]):
            flag += 1

    if(count > 1 and flag == 0 ):
        print(arr[i], end = " ")

print()
        

