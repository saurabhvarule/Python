
str1 = input("Enter string : ")
ch = input("Enter the character to search : ")

flag = 0;
i = len(str1) - 1

while(i > -1):
    if(str1[i] == ch):
        print("Last index of ", ch, " in ", str1, " is ", i)
        flag = 1
        break
    i -= 1

if(flag == 0):
    print("Element not present in String")
