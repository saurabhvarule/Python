
str1 = input("Enter first string : ")
str2 = input("Enter second string : ")
N = int(input("Enter number character you want to append : "))

str1 = str1 + str2[0 : N : 1]
print(str1)
