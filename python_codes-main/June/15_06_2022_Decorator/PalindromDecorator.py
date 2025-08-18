
def isPalindrome(fun):
    def inner(num):
        rev = fun(num)
        if(num == rev):
            return "Number is Palindrome"
        else: 
            return "Number is not Palindrome"

    return inner

def reverse(fun):
    def inner(num):
        pNum = fun(num)
        temp = 0
        rev = 0
        temp = pNum
        while(temp > 0):
            rev = rev * 10 + (temp % 10)
            temp = temp // 10
        return rev
    return inner

@isPalindrome
@reverse
def printNum(num):
    return num

num = int(input("Enter number : "))
print(printNum(num))

