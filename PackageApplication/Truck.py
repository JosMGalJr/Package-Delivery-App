# Class for trucks, which will be used to load packages and also track departure times
class Truck:
    def __init__(self, capacity, speed, load, packages, mileage, address, depart_time):
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.depart_time = depart_time
        self.time = depart_time

    def __str__(self):
        return f"{self.capacity}, {self.speed}, {self.load}, {self.packages}, {self.mileage}, {self.address}, " \
               f"{self.depart_time}"