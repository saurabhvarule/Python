
str1 = input("Enter first string : ")
str2 = input("Enter second string : ")
i = 0
num = 0
flag = 0

if(len(str1) != len(str2)):
    print("String lengths are not equal.")

else:    
    while(i < len(str1)):
        if(str1[i] == str2[i]):
            i += 1
            continue
        else:
            num = i
            flag = 1
            break

if(flag == 0):
    print("Both strings are equal.")
else:
    if(ord(str1[num]) > ord(str2[num])):
            print(ord(str1[num]) - ord(str2[num]))
    
    elif(ord(str1[num]) < ord(str2[num])):
            print(ord(str2[num]) - ord(str1[num]))
