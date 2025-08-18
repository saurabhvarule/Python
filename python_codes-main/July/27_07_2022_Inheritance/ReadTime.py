
class Company:

    #class variable

    cname = "Veritas"
    workplace = "Baner"

    #Company constructor

    def __init__(self):
        print("Company Consstructor")
        self.teamCode = "Python Code"

    @classmethod
    def facilities(cls):
        print("Provides all facilities...")
        print(cls.cname)
        print(cls.workplace)

class Employee(Company):

    #class variable
    roll = "Developer"

    #Empployee constructor

    def __init__(self, empId, lang):
        print("Employee Constructor")
        self.empId = empId
        self.lang = lang

    #Instance method

    def info(self):
        print(self.empId)
        print(self.roll)
        print(self.lang)
        print(self.workplace)
    
    @classmethod
    def skillset(cls):
        print(cls.roll)

emp1 = Employee(25,'Python')
emp2 = Employee(35,'Java')

emp1.info()
emp2.info()
