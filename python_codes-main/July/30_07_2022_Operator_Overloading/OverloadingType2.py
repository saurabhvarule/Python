
from multipledispatch import dispatch

class Addition:

    @dispatch(int, int)
    def add(self, x, y):
        return x + y

    @dispatch(int, int, int)
    def add(self, x, y, z):
        return x + y + z

    @dispatch(float, float)
    def add(self, x, y):
        return x + y

    @dispatch(float, float, float)
    def add(self, x, y, z):
        return x + y + z

obj = Addition()
print(obj.add(10, 20))
print(obj.add(10, 20, 30))
print(obj.add(10.5, 20.34))
print(obj.add(10.6, 20.21, 30.123))
