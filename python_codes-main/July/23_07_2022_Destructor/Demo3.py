
# Private baher access nahi hot
# protected same folder madhe access hota 
# public kuthe pn hota access hota

class Meta:

    def __init__(self,child1, child2):

        print("In constructor")
        self.cname1 = child1
        self.cname2 = child2

    def _disp(self):

        print(self.cname1)
        print(self.cname2)

mark = Meta("FaceBook", "Instagram")
mark._disp()
