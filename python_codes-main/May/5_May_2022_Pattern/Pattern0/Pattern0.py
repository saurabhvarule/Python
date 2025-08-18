
rows = int(input("Enter number of rows : "))
cols = int(input("Enter number of cols : "))

num = 1
sum1 = 0

for i in range(rows):

    for j in range(cols):

        print(num, end = " ")

        if(i == j or i + j == rows - 1):

            sum1 = sum1 + num
    
        num = num + 1
    print()

print(sum1)
