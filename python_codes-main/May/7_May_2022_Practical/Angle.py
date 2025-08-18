

a = int(input("Enter first angle : "))
b = int(input("Enter second angle : "))
c = int(input("Enter three angle : "))

if(a + b + c == 180):
    print("The triangle with angles", a, b, "and", c, "is valid one")

else:
    print("The triangle with angles", a, b, "and", c, "is invalid one")
