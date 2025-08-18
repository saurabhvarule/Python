
import array 

arr = array.array('i', [])

ln = int(input("Enter length of array : "))

for i in range(ln):
    
    temp = int(input())
    arr.append(temp)

for i in arr:

    count = 0
    
    for j in range(1,i // 2 + 1):
        
        if(i % j == 0):
            count += 1
    
    if(count == 1):
        print(i, end = " ")

print()

    
