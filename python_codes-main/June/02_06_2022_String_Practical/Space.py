
str1 = input("Enter string : ")

i = 0
count = 0

while(i < len(str1)):

    if(ord(str1[i]) == 32):
       
        count += 1
    i += 1
print(count)
