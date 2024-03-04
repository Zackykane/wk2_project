# Your parking garage class should have the following methods:
# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> 
#   display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

# NOTE: Use VSCode for this project starting with the following files below. 
# Also, each person in the group should list the portion of the project they 
# were responsible for inside of the python file and inside the README file.

# By the end of this project each group/student should be able to:
# - Explain and/or demostrate using Git and Github for collaboration
# - Explain and/or demostrate creating classes
# - Explain and/or demostrate creating class methods
# - Explain and/or demostrate class instantiation


# When the project is completed, commit the final changes, sync all pull requests, 
# and each member should submit their respective GitHub links(though the code in each should be the same)

class ParkingGarage():
    def __init__(self, spaces, tickets):
        self.spaces = spaces
        self.tickets = tickets
        self.current_tickets = {}

    def check_spaces(self):
        print(self.spaces)

    def removing_space(self):


garage_a = ParkingGarage(10, 10)
garage_a.check_spaces()
        
        
        