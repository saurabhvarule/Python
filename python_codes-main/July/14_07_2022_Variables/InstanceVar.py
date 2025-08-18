
class Railway:

    def __init__(self, ticket_No, destination):

        self.ticket_No = ticket_No
        self.destination = destination

    def dispData(self):
        
        print(self.ticket_No)
        print(self.destination)


ticket = int(input("Enter Ticket Number : "))
destination = input("Enter Destination : ")
obj = Railway(ticket, destination);
obj.dispData()
