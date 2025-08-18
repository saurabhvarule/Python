
num = int(input("Enter the limit : "))

for i in range(1,num):

    temp = i
    temp1 = 0

    while(temp != 0):

        fact = 1
        num1 = temp % 10

        for j in range(1, num1+1):

            fact = fact * j

        temp1 = temp1 + fact
        temp = temp // 10

    if(i == temp1):
        print(i, end = " ")

print()
