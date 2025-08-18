
str1 = input('Enter string : ')
str2 = ''
N = int(input('Enter the number last character you want to copy to the string : '))
i = -1
count = 1

while(i >= -N):

    str2 = str2 + str1[i]
    i -= 1

i = len(str2) - 1

while(i > -1):
    print(str2[i], end = '')
    i -= 1

print()
