
rows = int(input("Enter number of rows : "));
count = 0

for i in range(rows):

    for j in range(i):

        print(" ", end = "\t")
        count += 1
    
    for k in range(rows - i):
        print(i * count, end = "\t")
        count += 1
    count = 0
    print()
