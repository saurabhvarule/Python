
class Movies:

    def __init__(self):

        print("In constructor")
        self.mName = "RRR"
        self.director = "SSR"

    def info(self):

        y = 20
        self.x = 10
        print("Movie Name : {}\nDirector : {}".format(self.mName, self.director))

    def __del__(self):
        print("Deleting Object")
    '''
    def __delattr__(self,mName):
        print("Delete")
        super().__delattr__(self.mName)
    '''
movie1 = Movies()
movie1.info()

#movie1.__delattr__(mName);               #error
#movie1.__delattr__(movie1.mName);        #error
movie1.__delattr__("mName");
movie1.__delattr__("x");
#movie1.__delattr__("y");                 #error
#movie1.__delattr__(movie1.info);                 #error
#print(movie1.mName)
