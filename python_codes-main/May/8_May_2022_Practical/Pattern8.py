
rows = int(input("Enter number of rows : "))

for i in range (rows):

    num1 = 97 + i
    num2 = i + 1

    for j in range(rows - i - 1):
        print(" ", end = " ")

    for k in range(i + 1):
        if(i % 2 == 0):
            print(chr(num1), end = " ")
        else:
            print(num2, end = " ")

        num1 -= 1
        num2 -= 1

    print()
