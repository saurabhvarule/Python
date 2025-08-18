
class A:

    def __init__(self):

        print("A Constructor")
        self.x = 10

class B:

    def __init__(self):

        print("B Constructor")
        self.y = 20
        #super().__init__()

class C(A):

    def __init__(self):

        print("C Constructor")
        self.z = 30
        #super().__init__()

class D(B, C):

    def __init__(self):

        print("D Constructor")
        #super().__init__()
    
    def valueX(self):
        print(self.x)
        print(self.y)
        print(self.z)

obj = D()
obj.valueX()
