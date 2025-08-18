
str1 = input("Enter string : ")
str2 = ''

i = 0
while(i < len(str1)):

    if(65 <= ord(str1[i]) and 90 >= ord(str1[i])):
        num  = ord(str1[i]) + 32
        str2 = str2 + chr(num)

    elif(97 <= ord(str1[i]) and 122 >= ord(str1[i])):
        num  = ord(str1[i]) - 32
        str2 = str2 + chr(num)
    
    i += 1

print(str2)
