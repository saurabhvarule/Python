
from abc import ABC, abstractmethod

class Building(ABC):

    def architecture(self):
        print('Architecture of all flats is similar.')

    def facilities(self):
        print('All facilities are provided.')

    @abstractmethod
    def interiorDesign(self):
        pass

class Flat(Building):

    def interiorDesign(self):
        print('Interior design of eacch flat depends on its owner')

owner = Flat()
owner.architecture()
owner.facilities()
owner.interiorDesign()



