
rows = int(input("Enter number of rows : "))
cols = int(input("Enter number of cols : "))

num1 = 65
num2 = 97
count = 0

for i in range(rows):

    for j in range(cols):

        if(count % 2 == 0):
            print(chr(num1), end = " ")
        else:
            print(chr(num2), end = " ")

        num1 += 1
        num2 += 1
        count += 1

    print()
