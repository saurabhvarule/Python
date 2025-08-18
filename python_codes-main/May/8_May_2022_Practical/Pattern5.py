
rows = int(input("Enter number of rows : "))



for i in range(rows):
    
    num1 = 64 + rows
    num2 = rows

    num1 = num1 - i
    num2 = num2 - i

    for j in range(rows - i):

        if(i % 2 == 0):
            print(num2, end = " ")
        else:
            print(chr(num1), end = " ")

        num1 -= 1
        num2 -= 1

    print()

