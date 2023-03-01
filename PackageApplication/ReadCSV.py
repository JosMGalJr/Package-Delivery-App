import csv

# Opens csv files that will be manipulated within the program

with open("distance.csv") as csv_distance:
    CSV_Distance = csv.reader(csv_distance)
    CSV_Distance = list(CSV_Distance)

with open("address.csv") as csv_address:
    CSV_Address = csv.reader(csv_address)
    CSV_Address = list(CSV_Address)

with open("packages.csv") as csv_packages:
    CSV_Package = csv.reader(csv_packages)
    CSV_Package = list(CSV_Package)


