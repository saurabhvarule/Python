
str1 = input("Enter string : ")

i = 0
count = 0

while(i < len(str1)):

    if((65 <= ord(str1[i]) and 90 >= ord(str1[i])) or (97 <= ord(str1[i]) and 122>= ord(str1[i]))):
        count += 1
    
    i += 1

if(count == 0):
    print("No alphabates present in string.")
else:
    print("Number of alphabates in string ", str1, " is ", count)
