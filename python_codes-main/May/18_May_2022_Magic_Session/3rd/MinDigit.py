
num = int(input("Enter the number : "))
num1 = 10
temp = 0
temp1 = num

while(num != 0):
    
    temp = num % 10
    
    if(temp < num1):
        num1 = temp

    num = num // 10

print("The Min Digit from number", temp1 ,"is", num1)
