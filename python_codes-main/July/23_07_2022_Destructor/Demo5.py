
class Main:

    __x = 20

    def __init__(self):
        self.name = "Harshal"
        self.age = 20

        return None 

    def disp(self):
        print(self.name)
        print(self.age)

obj = Main()
obj.disp()

print(Main._Main__x)
