
def NCompare(str1, str2):
    i = 0
    num = 0
    N = int(input("Enter the number upto which you want to compare the strings : "))
    flag = 0

#if(len(str1) != len(str2)):
#    print("String lengths are not equal.")

#else:    
    while(i < N):

   
        if(str1[i] == str2[i]):
       
            i += 1
            continue
        
        else:
        
            num = i
            flag = 1
            break

    if(flag == 0):
        
        return 0

    else:
        if(ord(str1[num]) > ord(str2[num])):
            return (ord(str1[num]) - ord(str2[num]))
    
        elif(ord(str1[num]) < ord(str2[num])):
            return (ord(str2[num]) - ord(str1[num]))



str1 = input("Enter first string : ")
str2 = input("Enter second string : ")

print(NCompare(str1, str2))
