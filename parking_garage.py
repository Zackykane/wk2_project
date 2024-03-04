class ParkingGarage:
    def __init__(self, total_tickets, total_parking_spaces):
        self.tickets = list(range(1, total_tickets + 1))
        self.parkingSpaces = list(range(1, total_parking_spaces + 1))
        self.currentTicket = {}

    def takeTicket(self):
        if self.tickets and self.parkingSpaces:
            ticket_number = self.tickets.pop(0)
            parking_space = self.parkingSpaces.pop(0)
            self.currentTicket = {
                                    "ticket_number": ticket_number, 
                                    "parking_space": parking_space, 
                                    "paid": False
                                    }
            print(f"Your ticket number is {ticket_number}. Please park in space #{parking_space}.")

    def payForParking(self):
        if "ticket_number" in self.currentTicket:
            payment = input("Enter the payment amount: ")
            if payment:
                print("Ticket has been paid. You have 15 minutes to leave.")
                self.currentTicket["paid"] = True
            else:
                print("Payment not received.")

    def checkAvailability(self):
        print(f"Available parking spaces: {len(self.parkingSpaces)}")

    def leaveGarage(self):
        if "ticket_number" in self.currentTicket:
            if self.currentTicket["paid"]:
                print("Thank you, have a nice day!")
            else:
                payment = input("Please pay for your ticket: ")
                if payment:
                    print("Thank you, have a nice day!")
                    self.currentTicket["paid"] = True
                    self.parkingSpaces.append(self.currentTicket["parking_space"])
                    self.tickets.append(self.currentTicket["ticket_number"])
                else:
                    print("Payment not received. You must pay before leaving.")
# Our Example Input 
total_tickets = 10
total_parking_spaces = 10

garage = ParkingGarage(total_tickets, total_parking_spaces)

while True:
    print("Options:")
    print("1. Take Ticket")
    print("2. Pay for Parking")
    print("3. Check Availability")
    print("4. Leave Garage")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        garage.takeTicket()
    elif choice == "2":
        garage.payForParking()
    elif choice == "3":
        garage.checkAvailability()
    elif choice == "4":
        garage.leaveGarage()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please choose a valid option.")
