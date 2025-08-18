
class Parent:
   
    a = 200
    def __init__(self):
        print("Single parameter")

    __init1 = __init__

    def __init__(self, x):
        print("Two parameters")

    __init2 = __init__

    def __init__(self, x, y):
       print("Three parameters")
    
    __init3 = __init__

    def __init__(self, x = 10, y = 20, z = 30):

        if(x,y):

            self.__init3(x,y)     
        elif(x):
            
            self.__init2(x)     
        else:

            self.__init1()

        print("Four parameters")

obj = Parent(10)

