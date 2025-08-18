
str1 = input("Enter string : ")

capital = 0
small = 0
digits = 0

i = 0

while(i < len(str1)):

    if(65 <= ord(str1[i]) and 90 >= ord(str1[i])):
        capital += 1
    
    elif(97 <= ord(str1[i]) and 122 >= ord(str1[i])):
        small += 1
        
    elif(48 <= ord(str1[i]) and 57 >= ord(str1[i])):
        digits += 1
       
    i += 1

print("Small : ", small)
print("Capital : ", capital)
print("Digits : ", digits)

