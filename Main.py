# WGUPS ROUTING PROGRAM Author : Shane O'Hara  Student ID: 010044820

import csv
import datetime
from typing import Any

from Package import Package
from Hashmap import *
from Truck import Truck

# creates hash table for packages
myHash = Hashmap()

# reads address csv to adjacency list
with open("addresses.csv") as csvfile:
    Address = csv.reader(csvfile)
    Address = list(Address)
# reads distance csv to adjacency list
with open("distance.csv") as csvfilez:
    Distance = csv.reader(csvfilez)
    Distance = list(Distance)

#reads package csv to create package objects and load packages to myHash
def load_package(filename):

    with open(filename) as package_content:
        package_data = csv.reader(package_content)
        for package in package_data:
            mID = int(package[0])
            maddress = (package[1])
            mcity = (package[2])
            mstate = (package[3])
            mzip = (package[4])
            mstatus = "At HUB"
            mDeadline = (package[5])
            mweight = (package[6])


            pack = Package(mID,maddress,mcity,mstate, mzip, mweight, mDeadline, mstatus)
            myHash.update(mID,pack)

load_package("package.csv")

# returns address ID from address string
def return_addresses(address):
    for data in Address:
        if address in data[2]:
            return int(data[0])

#finds the distance between two places, if distance is not found, order of terms is reversed to search again. returns float of distance
def find_distance(first_place, second_place):
     dist = Distance[first_place][second_place]
     if dist == '':
         dist = Distance[second_place][first_place]

     return float(dist)

# creates truck objects, manually loads packages on to trucks, and sets departure time for trucks
Truck1 = Truck(16,[1,13,14,15,16,19,20,21,24,29,30,31,34,37,40] ,18, 0.0, "4001 South 700 East",datetime.timedelta(hours= 8))
Truck2 = Truck(16,[3,18,36,9,38,17,27,33,35,39] ,18,  0.0, "4001 South 700 East",datetime.timedelta(hours=10, minutes=21))
Truck3 = Truck(16,[25,28,32,2,4,5,7,8,10,11,12,6,22,23,26] , 18, 0.0, "4001 South 700 East", datetime.timedelta(hours=9, minutes=6))


#sorts packages on truck with nearest neighbor algorithm for optimized delivery
def sort_and_deliver(truck):
    #creates sorting bay array
    sorting_bay = []
    #puts packages from truck into sorting bay, empties trucks
    for packid in truck.package:
        pack = myHash.search(packid)
        sorting_bay.append(pack)

    truck.package.clear()
    # finds the nearest package for delivery in the sorting bay, and adds it to the truck. Finds next nearest package to previous package destination and adds to the truck
    # continues until sorting bay is empty, and truck is loaded in order
    while len(sorting_bay) > 0:
        next_stop = 4000
        next_package = None
        for pack in sorting_bay:
            if find_distance(return_addresses(truck.address), return_addresses(pack.address)) <= next_stop:
                    next_stop = find_distance(return_addresses(truck.address),return_addresses(pack.address))
                    next_package = pack


        truck.package.append(next_package.ID)
        sorting_bay.remove(next_package)
        # adds distance driven to deliver package to truck mileage
        truck.mileage += next_stop
        #updates truck address to the delivery address
        truck.address = next_package.address
        #updates time by dividing distance travelled by the 18mph speed of truck
        truck.time += datetime.timedelta(hours= next_stop/18)
        next_package.arrival_time = truck.time
        next_package.departure_time = truck.departure_time

# sorts the packages on each truck with Nearest neighbor and delivers packages
sort_and_deliver(Truck1), sort_and_deliver(Truck2), sort_and_deliver(Truck3)

# class Main creates UI, displays messages and prompts to user upon running including daily mileage total
class Main:
    print("Welcome to WGUPS!"), print("The daily total mileage is " ,Truck1.mileage + Truck2.mileage +Truck3.mileage)
    # Prompts users to input a time in HH:MM:SS format, in order to check the delivery status of any and all packages at that time
    display_time = input("Enter a time in order to check delivery status, using format HH:MM:SS")
    (hour, minute, second) = display_time.split(":")
    time_update = datetime.timedelta(hours=int(hour), minutes=int(minute), seconds=int(second))
    yes_no = input("Would you like to search for an individual package? Please enter Y for Yes, N for No")
    if yes_no == "N" or yes_no == "n":
        for packID in range(1,41):
            pack = myHash.search(packID)
            pack.delivery_status(time_update)
            print(str(pack))
    elif yes_no == "Y" or yes_no == "y":
         id_number = input("Please enter a package ID number to search")
         p = myHash.search(int(id_number))
         p.delivery_status(time_update)
         print(str(p))
    else:
        exit()
