
class Student:

    y = 50
    def __init__(self, name, rollNo):

        self.name = name
        self.rollNo = rollNo

    def fun(self):

        x = 30;
        print(x)

        print(self.name)
        print(self.rollNo)

obj = Student("Harshal", 10)
obj.fun()

class StaticDemo:

    @staticmethod
    def stat(obj1):

        obj1.name = "Prajwal"
        obj1.rollNo = 20
        obj1.y = 70


#obj1 = Student("Harshal", 10)
obj3 = StaticDemo()

obj3.stat(obj)

print(obj.name)
print(obj.rollNo)
print(obj.y)
