
class Node :
    def __init__(self, age=None, name=None):
        self.age = age
        self.name = name
        self.next = None

class MY_LinkedList :
    def __init__(self):
        self.head = None
    
    
    def createNode(self):
        newNode = Node()
        newNode.age = int(input("enter age :"))
        newNode.name = input("enter name :")

        return newNode
    
    def addNode(self):

        newNode = self.createNode()
        
        if(self.head == None):
            self.head = newNode
        else:
            temp = self.head
            while(temp.next != None) :
                temp = temp.next
            
            temp.next = newNode
    
    def printLinkedList(self):
        temp = self.head
        while(temp.next != None):
            print(f"| {temp.name},{temp.age} |", end = "->")
            temp = temp.next

        print(f"| {temp.name},{temp.age} |", end = "")



ll = MY_LinkedList()
ll.addNode()
ll.addNode()
ll.addNode()
ll.addNode()
ll.printLinkedList()
