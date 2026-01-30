
rows = int(input("Enter number of rows : "))
num = 1
for i in range(rows):
    for j in range(rows - i):
        print(" ", end = ' ')
    num = num + i
    for k in range((2*i) + 1):
        print(num, end = " ")
        if(i <= k):
            num += 1
        else:
            num -= 1
        
    print()
    num = 1
