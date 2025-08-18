
rows = int(input("Enter number of rows : "))

num = 9
count = 1;

for i in range(rows):

    for j in range(rows - i - 1):
        print("  ", end = " ")
    
    for k in range(i + 1):
        num = 9 * count
        print(num, end = " ")
        count += 1
   
    print()
