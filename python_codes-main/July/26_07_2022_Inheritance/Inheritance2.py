
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

class Child(Parent):

    x = 110

    def __init__(self):
        super().__init__()
        print("In child const")

    def childDisp(self):
        print(self.y)
        print(self.x)

obj = Child()
obj.show()
obj.disp()
obj.childDisp()
