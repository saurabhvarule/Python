
class RAM:

    def __init__(self, size, brand):

        self.size = size
        self.brand = brand

    class Process:

        CPUShedular = "Same for all process"

        def __init__(self):
            
            self.priority = 5
        
        def execution(self):
            print("Each process executes different task")

    
    def dataTransferRates(self):
        print("Depents on eah ram config")


ROG = RAM(8, "Kingston")
G3 = RAM(16, "XYZ")

jvm = ROG.Process()

jvm.execution()

