
import array

arr = array.array('i', [])

ln = int(input("Enter length of array : "))
sum = 0

for i in range(ln):

    temp = int(input())
    arr.append(temp)

    if(i % 2 == 0):
        sum = sum + temp

print(sum)
