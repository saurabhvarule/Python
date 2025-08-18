
num = int(input("Enter the number : "))

for i in range (1,10):
    
    count = 0
    temp = num

    while(temp != 0):
        
        num1 = temp % 10

        if(i == num1):
            count += 1

        temp = temp // 10

    if(count > 0):
        print("Frequency of", i, "is", count)
