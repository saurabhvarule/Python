
class Cric:

    format = "T20";

    def __init__(self):
        self.name = "Dhoni"
        self.jerNo = 7

    def myclassmethod(fun):

        def inner(*args):

            fun(args[0].__class__)

        return inner;

    def disp(self):
        print("Name : {} and JerNo : {}".format(self.name, self.jerNo))

    @myclassmethod
    def dispFormat(cls):
        print(cls)
        print(cls.format)


player1 = Cric()
player1.disp()

print(player1)

player1.dispFormat()
