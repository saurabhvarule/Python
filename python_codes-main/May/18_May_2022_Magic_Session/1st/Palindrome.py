
num1 = 0

for i in range(300,601):
    
    num = i
    
    while(num != 0):

        num1 = (num1 * 10) + (num % 10)
        num = num // 10
    
    if(i == num1):
        print(i, end = " ")
    
    num1 = 0
print()
