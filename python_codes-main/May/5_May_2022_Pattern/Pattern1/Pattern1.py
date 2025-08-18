
rows = int(input("Enter number of rows : "))
cols = int(input("Enter number of cols : "))

a = 0
num1 = 65;
num2 = 1;

for i in range(rows):    

    for j in range(cols):

        if(a == 0):
            print("*", end = " ")

        elif(a == 1):
            print(chr(num1), end = " ")
            num1 = num1 + 1

        elif(a == 2):
            print(num2, end = " ")
            num2 = num2 + 1
    
    a = a + 1
    if(a == 3):
         a = 0
    
    print()
