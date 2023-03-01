# Jose Galarza
# Student ID: 000930310

import datetime
from builtins import ValueError
from HashTable import HashTable
from Package import Package
from ReadCSV import *
import Truck


# Read package data from csv file and insert it into the hash table

def load_package_data(filename, package_hash_table):
    with open(filename) as package_info:
        package_data = csv.reader(package_info)
        Status = "At Hub"
        for package in package_data:
            ID, Address, City, State, Zipcode, Deadline_time, Weight, *_ = package
            ID = int(ID)
            package_hash_table.insert(ID, Package(ID, Address, City, State, Zipcode, Deadline_time, Weight, Status))


# Function for finding distance between two addresses | O(1)
def distance_in_between(x_value, y_value):
    distance = CSV_Distance[x_value][y_value]
    if distance == '':
        distance = CSV_Distance[y_value][x_value]

    return float(distance)


# Function to acquire address number | O(N)
def extract_address(address):
    for row in CSV_Address:
        if address in row[2]:
            return int(row[0])


# Create three truck objects, manually loading all packages
truck1 = Truck.Truck(16, 18, None, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=8))


truck2 = Truck.Truck(16, 18, None, [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))


truck3 = Truck.Truck(16, 18, None, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=9, minutes=5))

# Initializes the hash table
package_hash_table = HashTable()
load_package_data('packages.csv', package_hash_table)


# Function for ordering packages on a given truck by using the nearest neighbor algorithm | O(n^2)
# This also gives the total distance that the truck has traveled
def package_delivery(truck, package_hash_table):
    not_delivered = [package_hash_table.lookup(packageID) for packageID in truck.packages]
    truck.packages.clear()

    while not_delivered:
        next_package = None
        next_address = 1000
        for package in not_delivered:
            distance = distance_in_between(extract_address(truck.address), extract_address(package.address))
            if distance <= next_address:
                next_address = distance
                next_package = package

        truck.packages.append(next_package.ID)
        truck.mileage += next_address
        truck.address = next_package.address
        truck.time += datetime.timedelta(hours=next_address / 18)
        next_package.delivery_time = truck.time
        next_package.departure_time = truck.depart_time
        not_delivered.remove(next_package)


# Begin loading process for trucks one and two. Truck three is loaded at a later time to ensure it does not leave before
# a truck has returned
package_delivery(truck1, package_hash_table)
package_delivery(truck2, package_hash_table)
truck3.depart_time = min(truck1.time, truck2.time)
package_delivery(truck3, package_hash_table)


class Main:
    # Program begins by printing the total mileage of all three trucks
    print("Welcome. Total Mileage stands at:")
    print(truck1.mileage + truck2.mileage + truck3.mileage)  # Prints total mileage for all trucks
    # Next the user is prompted to input a time to check the status of the packages
    user_time = input("Please enter a time to check status of packages. Use the following format, HH:MM:SS\n")
    (h, m, s) = user_time.split(":")
    convert_timedelta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    # Packages are looked up and displayed
    try:
        for packageID in range(1, 41):
            package = package_hash_table.lookup(packageID)
            package.update_status(convert_timedelta) # Ensures package status is updated
            print(package)
    except ValueError:
        print("Entry invalid. Closing program.")