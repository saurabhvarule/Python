
rows = int(input("Enter number of rows : "))
count = 0
i = 0
num = 1
num1 = 64
temp = 0

while(i < rows):

    for j in range(rows - i - 1):
        print(" ", end = " ")

    for k in range(i + i + 1):
        
        if(i % 2 == 0):
            print(num + i, end = " ")

        else:
            print(chr(num1 + i), end = " ")
    
#    num1 += 1

#    if(i % 2 != 0):
#         num1 += 1

    if(i == rows - 1):
        count = 1

    if(count == 1):
        i -= 1
        if(i == -1):
            break
    else:
        i += 1

    print()

print()
