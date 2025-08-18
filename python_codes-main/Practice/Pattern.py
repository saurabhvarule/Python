
rows = int(input("Enter number of rows : "))

priv = 0

for i in range(rows):
    
    num = rows + i
    temp = 0

    for j in range(rows-i-1):
        print(" ", end = "  ")
    
    for k in range(i + 1):
        if(k == 0):
            
            print(rows + i, end = "  ")
            temp += 2
            priv = rows + i

        else:
            
            print(rows + i - temp + priv, end = " ")
            priv = rows + i - temp + priv
            temp += 2
    
    print()
