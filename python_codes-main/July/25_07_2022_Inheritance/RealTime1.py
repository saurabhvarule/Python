
class Car:

    carType = "Sedan"
    
    def __init__(self):

        print("Car Constructor")

    @classmethod
    def changeCarType(cls):

        cls.carType = input("Which type of car do you prefer : ")

    def accelerate(self):

        print("Funtionality of acceleration is same")

class Maruti_Suzuki(Car):

    def __init__(self, colour, sunRoof):

        super().__init__()
        self.colour = colour
        self.sunRoof = sunRoof
        print("Maruti Suzuki Constructor")

    def brake(self):

        print("Brakes of Maruti Suzuki are like this!")

    def carInfo(self):

        print("Colour : {}\nSunroof : {}\nCar Type : {}".format(self.colour,self.sunRoof,self.carType))


swift = Maruti_Suzuki("White", "Yes")
swift.changeCarType()
swift.accelerate()
swift.brake()
swift.carInfo()
