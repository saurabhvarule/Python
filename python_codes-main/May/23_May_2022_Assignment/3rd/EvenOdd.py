
import array

arr = array.array('i',[])

ln = int(input("Enter length of array :"))

for i in range(ln):

    temp = int(input())
    arr.append(temp)

ECount = 0;
OCount = 0;

for i in arr:

    if(i % 2 == 0):
        ECount += 1
    else:
        OCount += 1

print("Number of Even Numbers :", ECount)
print("Number of Odd Numbers :", OCount)
