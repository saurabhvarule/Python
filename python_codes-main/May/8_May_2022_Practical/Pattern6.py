
rows = int(input("Enter number of rows : "))

num = 65
num1 = 1;

for i in range(rows):

    for j in range(i + 1):
     
        if(j % 2 == 0):
            print(chr(num), end = " ")
        else:
            print(num1, end = " ")

    num += 1
    num1 += 1
    print()
