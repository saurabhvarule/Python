
class A:

    def __init__(self):
        print("A Costructor")

    def ADisp(self):
        print("Method A")

class B:

    def __init__(self):
        print("B Costructor")

    def BDisp(self):
        print("Method B")

class C(A, B):

    pass

obj = C()
obj.ADisp()
obj.BDisp()

print(C.mro())
