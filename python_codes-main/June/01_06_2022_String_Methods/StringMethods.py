
str1 = "core2Web"
print(str1)

#1. capitalize()

str1 = str1.capitalize()
print(str1)

#2. casefold()

print(str1.casefold())

#3. center(width, fillcharacter = "")

print(str1.center(20, "_"))

#4. count(string)

print(str1.count('e'))

#5. endswith()

print(str1.endswith("web"))

#6. find()

print(str1.find('w'))

#7. rfind()

print(str1.rfind('e'))

#8. index()

print(str1.index('e'))  #If character not present the we have to handle the exception.

#9. join()

print('x'.join(str1))

#10. ljust()
#11. rjust()

print(str1.ljust(10, 'x'))
print(str1.rjust(10, 'x'))

#12. lower

print(str1.lower())

#13. strip()
#14. lstrip()
#15. rstrip()

str2 = "     Core2Web     "

print(str2.strip())
print(str2.lstrip())
print(str2.rstrip())

#16. partition()
#17. rpartition()

str3 = "Core2Web,Biencaps"

print(str3.partition(','))
print(str3.rpartition(','))

#18. replace()

print(str1.replace('web', 'Net'))

#19. split()
#20. rsplit()

str4 = "_Harshal_Borse_12"

print(str4.split('_'))
print(str4.rsplit('_'))
