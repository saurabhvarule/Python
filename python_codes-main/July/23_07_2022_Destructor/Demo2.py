
class YouTube:

    def __init__(self):
        print("In constructor")
        self.parent = "Google"

    def disp(self):
        print("In disp")

    def __new__(self):
        print("Object creation")
        return super().__new__(self)

    def __del__(self):
        print("Object delete")

obj1 = YouTube()
obj1.disp()

del obj1.parent
del obj1


obj2 = YouTube()
obj2.disp()

print(dir(YouTube))
