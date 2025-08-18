
def reverse(fun):

    print("Start : In reverse")

    def inner(*args):
        print("In inner reverse- Before")
        str2 = fun(*args)
        print("In inner reverse- After")
        return str2[-1: :-1]

    print("End : In reverse")
    return inner

def concat(fun):

    print("Start : In concat")
    
    def inner(*args):
        print("In inner concat- Before")
        retuple = fun(*args)
        print("In inner concat- After")
        str2 = ''
        for i in retuple:
            str2 = str2 + i
        return str2

    print("End : In concat")
    return inner

@reverse
@concat
def printStr(str1, str2):
    print("Start : In printStr")
    return str1, str2

str1 = input("Enter First String : ")
str2 = input("Enter First String : ")

print(printStr(str1, str2))
