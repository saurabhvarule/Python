

rows = int(input("Enter number of rows : "))
cols = int(input("Enter number of cols : "))

for i in range(rows):

    num1 = 64 + cols
    num2 = cols
    for j in range(cols):

        print(chr(num1), end = "")
        print(num2, end = " ")
        
        num1 -= 1
        num2 -= 1

    print()



