
class Cric:

    format = "T20"

    def __init__(self,name,jerNo):
        self.name = name
        self.jerNo = jerNo

    def fun(self):
        print(self)

    def myClassMethod(fun):
        def magic(cls):
            cls = cls.__class__
            fun(cls)
            return
        return magic

    @myClassMethod
    def dispData(cls):
        print(cls)
        cls.format = "Harshal"

obj = Cric("Rohit", 12)
obj2 = Cric("Kohli", 18)

obj.fun()
obj.dispData()

print(obj2.format)
print(Cric)
