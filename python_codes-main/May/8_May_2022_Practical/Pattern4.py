
rows = int(input("Enter number of rows : "))

for i in range(rows):

    num = 96 + rows 
    num = num - i
  
    for j in range(rows - i):
        print(chr(num), end = " ")
        num -= 1
    print()

