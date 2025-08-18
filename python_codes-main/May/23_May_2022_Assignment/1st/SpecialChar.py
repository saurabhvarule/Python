
import array

arr = array.array('u', [])

ln = int(input("Enter length of array : "))

for i in range(ln):

    ch = input()
    arr.append(ch)

for i in arr:

    if((i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z')):
        print(i, end = " ")

print()
