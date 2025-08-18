
import array

arr = array.array('i', [])

ln = int(input("Enter length of the array : "))
print("Enter elements in the array : ")

for i in range(ln):

    temp = int(input())
    arr.append(temp)

sum = 0
fact = 1
flag = 0
print("List of strong number(s) in an array : ")
for i in range(ln):

    sum = 0
    rem = 0
    temp = arr[i]

    while(temp != 0):

        fact = 1
        rem = temp % 10

        for j in range(1, rem + 1):
            fact = fact * j

        sum = sum + fact
        temp = temp // 10
        
        if(arr[i] == sum):
           
            flag = 1
            print(arr[i], end = " ")

if(flag == 0):

    print("Array does not contain any strong number.")

print()
