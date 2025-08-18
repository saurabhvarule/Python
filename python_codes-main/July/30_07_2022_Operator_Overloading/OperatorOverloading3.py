
class Xyz:

    def __init__(self,x ,y):
        self.x = x
        self.y = y

    def __lshift__(self, obj):
        return self.x << obj.x

    def __mod__(self, obj):
        return self.x % obj.x

    def __floordiv__(self, obj):
        return self.x // obj.x

    def __rshift__(self, obj):
        return self.x >> obj.x

    def __sub__(self, obj):
        return self.x - obj.x
    
obj1 = Xyz(10, 20)
obj2 = Xyz(5, 15)

print(obj1 << obj2)
print(obj1 % obj2)
print(obj1 // obj2)
print(obj1 >> obj2)
print(obj1 - obj2)

