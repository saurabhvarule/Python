
import array

arr = array.array('i', [])

ln = int(input("Enter length of the array : "))
print("Enter elements in the array : ")

for i in range(ln):

    temp = int(input())
    arr.append(temp)

flag = 0
print("List of Armstrong numbers in the array : ")

for i in arr:

    temp = i
    sum = 0;

    while(temp != 0):

        rm = temp % 10
        sum = sum + (rm * rm * rm)
        temp = temp // 10

    if(i == sum):
        flag = 1
        print(i, end = " ")

if(flag == 0):
    print("Array does not contain any Armstrong number.")

print()
