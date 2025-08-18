
class YouTube:

    def __init__(self):
        print("In constructor")
        self.parent = "Google"

    def disp(self):
        print("In disp")

    def __new__(self):
        print("Object creation")
        return super().__new__(self)

obj1 = YouTube()
obj1.disp()

print(dir(YouTube))
