

class Demo :
    next = None
    age = None
    name = None

class Main:
    head = None

    def create():
        new = Demo()
        return new
    
    def add():
        new = Main.create()
        new.age = int(input("enter age :"))
        new.name = input("enter name :")
        
        if(Main.head == None):
            Main.head = new
        else:
            temp = Main.head
            while(temp.next != None):
                temp = temp.next

            temp.next = new
    
    def printData():
        temp = Main.head
        while(temp.next != None):
            print(f"| {temp.name} {temp.age} |->",end = "")
            temp = temp.next

        print(f"| {temp.name} {temp.age} |",end = "")


print("how many persons?")
count = int(input())

while(count>0):
    Main.add()
    count-=1


Main.printData()
