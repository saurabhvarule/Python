
str1 = input("Enter string : ")

i = len(str1) - 1

while(ord(str1[i]) == 32):
    i -= 1

str2 = ''
while(i > -1):
    if(ord(str1[i]) == 32):
        break
    else:
        str2 = str2 + str1[i]
    i -= 1

j = len(str2) - 1

while(j > -1):
    print(str2[j], end = '')
    j -= 1
    
