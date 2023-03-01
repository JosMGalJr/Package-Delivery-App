# Class for packages, includes function to update package status depending on transport status
class Package:
    def __init__(self, ID, address, city, state, zipcode, Deadline_time, weight, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.Deadline_time = Deadline_time
        self.weight = weight
        self.status = status
        self.departure_time = None
        self.delivery_time = None

    def __str__(self):
        return f"{self.ID}, {self.address}, {self.city}, {self.state}, {self.zipcode}, {self.Deadline_time}, " \
               f"{self.weight}, {self.delivery_time}, {self.status} "

    # Updates status of package depending on whether the truck it is loaded on has left the hub and whether it has
    # reached its destination | O(1)
    def update_status(self, current_time):
        if self.delivery_time < current_time:
            self.status = "Delivered"
        elif self.departure_time > current_time:
            self.status = "En route"
        else:
            self.status = "At Hub"
