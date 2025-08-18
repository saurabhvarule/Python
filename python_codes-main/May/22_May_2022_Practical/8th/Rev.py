
import array

arr = array.array('i', [])

ln = int(input("Enter length of array :"))

for i in range(ln):

    temp = int(input())
    arr.append(temp)

print(arr)

arr.reverse()
print(arr)
