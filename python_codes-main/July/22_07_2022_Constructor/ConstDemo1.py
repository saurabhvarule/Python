
#Refer notebook for this code

class Movies:

    def __init__(self):

        print("In constructor")
        self.mName = "RRR"
        self.director = "SSR"

    def info(self):

        print("Movie Name : {}\nDirector : {}".format(self.mName,self.director))

#    def __new__(self):             #Here self contains name of the class whose object we are trying to create.
#        print("In new")
#        return super().__new__(self)    

#    def __new__(self):
#        print("In new")
#        var = super().__new__(self)
#        return var;

#    def __new__(self):       ~~\
#        print("In new")         \
#        self.__init__(self)      \
#        return self                == Igonre all these lines.   
#                                 /   
#movie1 = Movies()               /
#movie1.info(Movies)          __/

    def __new__(self):
        print("In new")
        var = super().__new__()
        var.__init__()
        return var

movie1 = Movies()               
movie1.info() 
