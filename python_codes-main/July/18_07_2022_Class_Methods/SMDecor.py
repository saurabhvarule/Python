
class StaticDemo:

    x = 10

    def __init__(self):
        self.y = 20

    def mystaticmethod(fun):

        def inner(*args):
            fun()

        return inner

    def fun(self):
        print(self)
        print(self.x)

    @classmethod
    def gun(cls):
        print(cls)

    @mystaticmethod
    def demo():
        print("Static method")

obj1 = StaticDemo()
obj1.fun()
obj1.gun()
obj1.demo()
