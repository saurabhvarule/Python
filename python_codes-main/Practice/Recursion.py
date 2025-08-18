

def factorial(num):

    if(num == 0):
        return 1
    if(num > 0):
        fact = num * factorial(num - 1)
        return fact

num = int(input("Enter number : "))
print(factorial(num))
