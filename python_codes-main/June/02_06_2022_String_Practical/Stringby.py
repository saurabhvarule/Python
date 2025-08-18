
str1 = input("Enter string : ")

i = 0

while(i < len(str1)):
    if((66 <= ord(str1[i]) and 89 >= ord(str1[i])) or (98 <= ord(str1[i]) and 121 >= ord(str1[i])) or ord(str1[i]) == 32):
            print(str1[i], end = '')
    else:
        break
    i += 1

print()
