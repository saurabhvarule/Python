
class X:
    
    def __init__(self):
        self.x = 10
        self.y = 20

    def show(self):
        print(self.x)
        print(self.y)

    def __add__(self, obj):
        return self.x + obj.x

obj1 = X()
obj2 = X()

obj1.show()
obj2.show()

a = 50
b = 60

print(a + b)

#TypeError: unsupported operand type(s) for +: 'X' and 'X'
#If I write my own __add__ method then there will be no error.

print(obj1+obj2)
