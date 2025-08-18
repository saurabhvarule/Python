
def outer():

    print("In outer")
    def inner():
        
        print("In inner")
        # return "In inner"
    return inner

Rinner = outer()
Rinner()
