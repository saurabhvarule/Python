
class Meta:

    def __init__(self, child1, child2 = "WhatsApp"):

        print("In constructor")
        self.cname1 = child1
        self.cname2 = child2

    def _disp(self):
        print(self.cname1)
        print(self.cname2)

obj = Meta("Instagram")
obj._disp()

obj = Meta("Instagram", "Facebook")
obj._disp()
