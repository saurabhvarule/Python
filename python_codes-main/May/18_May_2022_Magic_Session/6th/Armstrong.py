
for i in range(1, 101):

    temp = 0
    num = i

    while(num != 0):

        num1 = num % 10
        temp = temp + (num1 ** 3)
        num = num // 10

    if(temp == i):
        print(i, end = " ")

print()
