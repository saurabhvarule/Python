
class Computer:

    classVar = 0;

    def __init__(self,var1, var2):

        print("Parent Constructor")
        self.var1 = var1
        self.var2 = var2

    @classmethod
    def clsMeth(cls):
        print("Class Method")
        cls.classVar = 10

    def (self):
        print("Instance Method - parent")
        print(self.var1)
        print(self.var2)
        
class Laptop(Computer):

    def __init__(self,var1, var2, var3, var4):

        super().__init__(var1, var2)

        self.var3 = var3
        self.var4 = var4

    def TDM(self):
        print("Instance Method - child")
        print(self.var3)
        print(self.var4)

obj = Child("Harshal", 23, "Prajwal", 30)
obj.instMeth1()
obj.instMeth2()
obj.clsMeth()

obj2 = Child("Aditi", 20, "Saurabh", 10)
obj2.instMeth2()
obj2.instMeth2()

print(obj2.classVar)

