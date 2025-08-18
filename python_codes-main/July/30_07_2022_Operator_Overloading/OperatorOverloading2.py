
class Xyz:

    def __init__(self,x ,y):
        self.x = x
        self.y = y

    def __add__(self, obj):
        return self.x + obj.x , self.y + obj.y

    def __le__(self, obj):
        if(self.x <= obj.x):
            return True;
        else:
            return False;

    def __eq__(self, obj):
        if(self.x == obj.x):
            return True
        else:
            return False

    def __ge__(self, obj):
        if(self.x >= obj.x):
            return True

        else:
            return False

    def __gt__(self, obj):
        if(self.x > obj.x):
            return True
        else:
            return False

    def __lt__(self, obj):
        if(self.x < obj.x):
            return True
        else:
            return False

    def __ne__(self, obj):
        if(self.x != obj.x):
            return True
        else:
            return False

obj1 = Xyz(10, 20)
obj2 = Xyz(5, 15)

output = obj1 + obj2
print(output)
print(obj1 <= obj2)
print(obj1 == obj2)
print(obj1 >= obj2)
print(obj1 > obj2)
print(obj1 != obj2)

