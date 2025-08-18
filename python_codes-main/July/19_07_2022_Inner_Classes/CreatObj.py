
# Inner classes.
# There are two types of inner classes in python.
# 1. Normal Inner Class
# 2. Method Local Inner Class
#
# There are three ways to create an object of the normal inner class among which two ways are explained in the code below.
#
#
#
#
#
#


class Outer:

    x = 10

    def __init__(self):

        print("Outer Constructor")
        self.out = 10

    class Inner:

        y = 20

        def __init__(self):

            print("Inner Constructor")
            self.inn = 20

        def disp(self):

            print(self.inn)
            print(self.y)

    def disp(self):

        print(self.out)
        print(self.x)

outObj = Outer()
outObj.disp()

innObj1 = outObj.Inner()        # Internally it goes as -> outObj.Inner(innObj1)
innObj1.disp()

# If we create an object like this we can not access the data of outer class, 
# we have to create another object for Outer class, so the prefered way is first way.

innObj2 = Outer().Inner()       
innObj2.disp()
