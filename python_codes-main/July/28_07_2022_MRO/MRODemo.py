
class E: 
    def __init__(self):
        print("E")
        super().__init__()
        print("E constructor")

class F(E): 
    def __init__(self):
        print("F")
        super().__init__()
        print("F constructor")

class D: 
    def __init__(self):
        print("D")
#        super().__init__()
        print("D constructor")

class A(D):
    def __init__(self):
        print("A")
        super().__init__()
        print("A constructor")

class B(D):
    def __init__(self):
        print("B")
        super().__init__()
        print("B constructor")

class C(A,B,F):
    def __init__(self):
        print("C")
        super().__init__()
        print("C constructor")

obj = C()
