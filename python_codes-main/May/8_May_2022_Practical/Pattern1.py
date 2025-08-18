
rows = int(input("Enter number of rows : "))
cols = int(input("Enter number of cols : "))

for i in range(rows):
    
    num = 1
    num += i

    for j in range(cols):

        print(num, end = " ")
        num += 3
    print()
