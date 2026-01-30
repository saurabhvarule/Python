

rows = int(input("enter no of rows: "))

for i in range(rows):
    for j in range(rows-i):
        print(" ",end=" ")
    
    for k in range((2*i)+1):
        print("*", end=" ")
    
    
    print()

for i in range(1,rows):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range(2*rows-(2*i+1)):
            print("*",end=" ")
    print()

