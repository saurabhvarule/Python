
class Parent:

    def __init__(self):
        print("In parent constructor")
        self.x = 10

    def disp(self):
        print(self.x)

class Child(Parent):

    def __init__(self):

        super().__init__()       #To call the parent constructor so that the variable in parent class get initialize
        print("In child constructor")
        self.y = 20

    def view(self):
        print(self.y)

obj = Child()
obj.disp()
obj.view()
