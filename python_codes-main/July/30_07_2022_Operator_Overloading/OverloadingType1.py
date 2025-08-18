
class Addition:

    def add(self, x = None, y = None, z = None):

        if(x != None and y != None and z != None):
            return x + y + z
        elif(x != None and y != None):
            return x + y

obj = Addition()
print(obj.add(10,20,30))
print(obj.add(10,20))
