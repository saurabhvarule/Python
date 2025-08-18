
str1 = input("Enter string : ")
i = 0

while(ord(str1[i]) == 32):
    i += 1

j = len(str1) - 1
flag = 0

while(ord(str1[j]) == 32):
    j -= 1

count = 0
even = 0
odd = 0

while(i < j+1):

    if(ord(str1[i]) == 32 and count % 2 == 0 and flag == 0):
        even += 1
        count = 0
        i += 1
        flag = 1
        continue
    
    elif(ord(str1[i]) == 32 and count % 2 != 0 and flag == 0):
        odd += 1
        count = 0
        i += 1
        flag == 1
        continue
    elif(ord(str1[i]) != 32 and flag == 1):
        flag = 0
        count += 1
        i += 1
        continue

    elif(i == j):
        count += 1
        if(count % 2 == 0):
            even += 1

        elif(count % 2 != 0):
            odd += 1

    if(ord(str1[i]) != 32):
        count += 1
    i += 1

print("Even : ", even)
print("Odd : ", odd)
