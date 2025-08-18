
rows = int(input("Enter number of rows : ")) 

num = 1

for i in range(rows):

    for j in range(rows - i - 1):
        print(" ", end = " ")

    for k in range(i + 1):
        print(num * (k + 1), end = " ")
    
    num += 1
    print()
