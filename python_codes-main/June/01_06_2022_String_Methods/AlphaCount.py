
str1 = input("Enter the string : ")
ch = input("Enter character to check count : ")

count = 0
i = 0;

while(i < len(str1)):

    if(ch == str1[i]):
        count += 1

    i += 1

if(count == 0):
    print("Element not found in string.")
else:
    print("Occurence of ", ch," in string ", str1," is ",count)
