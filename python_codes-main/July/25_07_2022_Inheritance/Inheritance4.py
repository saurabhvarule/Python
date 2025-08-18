
class Parent:

    def __init__(self, var1, var2):
        
        print("In parent constructor")
        self.var1 = var1
        self.var2 = var2

    def disp(self):

        print(self.var1)
        print(self.var2)
        print(self.var3)
        print(self.var4)

class Child(Parent):

    def __init__(self, var1, var2, var3, var4):
        
        super().__init__(var1, var2)
        print("In child constructor")
        self.var3 = var3
        self.var4 = var4

    def disp(self):
        
        super().disp()
        print(self.var3)
        print(self.var4)

obj = Child(10,20,30,40)
obj.disp()
