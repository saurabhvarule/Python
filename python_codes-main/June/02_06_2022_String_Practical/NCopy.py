
str1 = input('Enter string : ')
str2 = ''
N = int(input('Enter the number upto which you want to copy the string : '))
i = 0

while(i < N):
    str2 = str2 + str1[i]
    i += 1

print(str2)
