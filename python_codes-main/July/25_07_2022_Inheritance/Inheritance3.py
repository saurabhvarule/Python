
class Parent:

    z = 30

    def __init__(self):
        print("In parent constructor")
        self.x = 10

    @classmethod
    def demo(cls):
        print(cls.z)

    def disp(self):
        print(self.x)

    def __del__(self):
        print("Delete parent")


#obj2 = Parent()
#obj3 = Parent()

class Child(Parent):    
    def __init__(self):

    #    obj2 = obj3.__class__
    #    a = obj2()
    #    a.__init__()
        super().__init__()
        print("Here")
        print("In child constructor")
        self.y = 20

    def show(self):
        print(self.y)

    def __del__(self):
        print("Delete child")

    def objdemo(self):
        print("in demo")
        a = Child()


obj = Child()
obj.objdemo()
obj.demo()

