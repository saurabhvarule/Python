
# Python madhe class ch ani constructor ch nav same rahat nahi. Constructor __init__(self) ne define kela jato.
# Python madhe constructor overloading chalat nahi, kelyas interpreter most recently lihilelya constructor la consider karto.
# Just like in all other languages, in python constructor is use for initialization of instance variable.
# Constructor cha first parameter ha nehami object cha address asto just like this pointer pn ethe aplyala variable lihayala lagto, hidden nasto.
# To hidden parameter self ne denote karaych convention ahe python madhe.

class PoliParty:

    def __init__(self,abc, xyz):

        print("In Constructor")
        self.pName = "NCP"
        self.symbol = "Alarm Clock"        

#    def __init__(self, xyz):
#        self.xyz = xyz                     # Constrcutor overloading error.
#        self.abc = 21

    def dispParty(self):

        print("Party Name : {}\nSymbol : {}".format(self.pName,self.symbol))

obj1 = PoliParty(10,20)
obj1.dispParty()

print(obj1.dispParty)
print(type(obj1.dispParty))
