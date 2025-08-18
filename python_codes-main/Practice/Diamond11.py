
rows = int(input("Enter number of rows : "))

flag = 0
i = 0
while(i < rows):
    for j in range(rows - 1 - i):
        print(" ", end = " ")

    for k in range(2*i + 1):
        
        print("*", end = " ")
        
    if(i == rows - 1):
        flag = 1
    if(flag == 1):
        i -= 1
        if(i == -1):       
            break
    else:
        i += 1

    print()
print()
