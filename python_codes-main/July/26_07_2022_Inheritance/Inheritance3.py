
class Parent(object):
    x = 10
    def __init__(self):
        print("In parent const")
        self.y = 20
    
    @classmethod
    def show(cls):
        print(cls.x)
    
    def disp(self):
        print(self.x)
        print(self.y)

class Child1(Parent):

    def __init__(self):
        super().__init__()
        #self.y = 30
        print("In child1 const")
        
    def child1disp(self):
        print(self.x)
        print(self.y)
        
class Child2(Parent):
    
    def __init__(self):
        super().__init__()
        print("In child2 const")
    
    def child2disp(self):
        print(self.x)
        print(self.y)
        print(self.z)

obj1 = Child1()
Child1.x = 100
obj1.show()
#obj1.disp()
#obj1.child1disp()

obj2 = Child2()
obj2.x = 200
obj2.show()
#obj2.disp()
#obj2.child2disp()

Parent.x = 300
obj1.show()
obj2.show()
