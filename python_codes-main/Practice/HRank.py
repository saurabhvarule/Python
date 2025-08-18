
ln = int(input("Enter number of rows : "))
num = 0
count = 1
i = 0
j = 0
z = " "

while(i < ln):

    if(j < i + count):
       
       if(j == i + count - 1):
            z = "\n"
        
       if(j > i):
           num -= 1
       else:
           num += 1

       print(num, end = z)

       j += 1
       continue

    z = " "
    j = 0
    num = 0
    i += 1
    count += 1
