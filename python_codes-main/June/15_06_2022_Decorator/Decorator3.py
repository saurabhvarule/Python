
def sort(str1):

    lst = list(str1)
    temp = ''
    str2 = ''
    for i in range(len(lst)): 
        for j in range(len(lst)):
            
            if(lst[i] > lst[j]):
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
        
    for i in lst:
        str2 = str2 + i

    return str2

def concat(fun):
   
    def inner(*args):

        retuple = fun(*args)
        
        if(retuple == 0):
            return "Strings are not anagram"
        else:
            str2 = ''
            for i in retuple:
                str2 = str2 + i
            return str2

    return inner

def anagram(fun):

    def inner(str1, str2):

        str3 = sort(str1.lower())
        str4 = sort(str2.lower())

        if(str3 == str4):
            return str1, str2
        else:
            return 0

    return inner

@concat
@anagram
def printStr(str1, str2):
    return str1, str2

str1 = input("Enter First String : ")
str2 = input("Enter First String : ")

if(len(str1) == len(str2)):
    print(printStr(str1, str2))
else:
    print("Strings are not anagram")

