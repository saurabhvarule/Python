
def outer():

    print("In outer")

    def inner1():
        
        return "In inner1"
    
    def inner2():
        
        return "In inner2"

    return inner1, inner2

Rinner = outer()

for x in Rinner:
    print(x())
