
#Object la jaga ani constructor la call he doghi funtion ekach veli hota.

class Movies:

    def __init__(self):

        self.mName = "RRR"
        self.director = "SSR"

    def info(self):

        print("Movie Name : {}\nDirector : {}".format(self.mName, self.director))

movie1 = Movies()
movie1.info()
