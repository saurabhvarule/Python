
str1 = input("Enter string : ")

i = 0
 
#Count starting spaces.
while(ord(str1[i]) == 32):

    i += 1

j = len(str1) - 1

#Count ending spaces.
while(ord(str1[j]) == 32):
    
    j -= 1

num = 1
flag = 0

#Count number of words.
while(i < j):
    
    if(ord(str1[i]) == 32) and flag == 0:
        num += 1
        flag = 1
    
    if(ord(str1[i]) != 32):
        flag = 0

    i += 1

print(num)

