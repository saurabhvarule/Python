
class A:

    def __init__(self):
        super().__init__()
        print("A constructor")
class B:

    def __init__(self):
        #super().__init__()
        print("B constructor")

class D:

    def __init__(self):
        #super().__init__()
        print("D constructor")

class C(A, B, D):

    def __init__(self):
        super().__init__()
        print("C constructor")

obj = C()
