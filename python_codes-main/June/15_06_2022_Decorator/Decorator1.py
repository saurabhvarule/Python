
# String Reverse.

def reverse(fun):

    def inner(str1):

        '''
        i = len(str1) - 1
        str2 = ''
        while(i >= 0):

            str2 = str2 + str1[i]
            i -= 1
        return str2
        '''
        return str1[-1: :-1]

    return inner

@reverse
def printStr(str1):

    return str1

str1 = input("Enter string : ")
print(printStr(str1))
