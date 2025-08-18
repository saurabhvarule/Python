
ch = input("Enter any character : ")

if(ch >= '0' and ch <= '9'):
    print(ch, "is a digit.")

elif(ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
    print(ch, "is an alphabate")

else:
    print(ch, "is a special character")
