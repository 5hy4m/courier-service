from offer import Offer
from package import Package
from package_manager import PackageManager
from vehicle import Vehicle

import json 

def createOffers(offers):
    # Gets list of objects and convert them into class objects
    offers = [Offer(offer) for offer in offers]
    return offers

def createPackages(no_of_packages):
    try:
        no_of_packages = int(no_of_packages)
    except ValueError as e:
        raise e 
    packages = [Package(input().split( )) for _ in range(no_of_packages)]
    return packages

def readOffers():
    try:
        f = open('offers.json')
        offers = json.load(f)
        f.close()
        return offers
    except FileNotFoundError as e:
        raise e

def main():
    print("Courier Service")
    print("Please Enter The Input")

    offers = readOffers()
    createOffers(offers)
    # Getting Base Delivery Cost and No of Packages
    base_delivery_cost,no_of_packages = input().split( )

    packages = createPackages(no_of_packages)
    
    # Getting No of vehicles and Max Speed
    no_of_vehicles,max_speed,max_weight = input().split( )
    
    try:
        base_delivery_cost = float(base_delivery_cost)
        no_of_vehicles = int(no_of_vehicles)
        max_speed = float(max_speed)
        max_weight = float(max_weight)
    except ValueError as e:
        raise e

    for _ in range(no_of_vehicles):
        Vehicle(max_speed,max_weight)

    manager = PackageManager(base_delivery_cost,no_of_vehicles,max_speed,max_weight)

    for package in packages:
        manager.calculatePackages(base_delivery_cost,max_weight)

if __name__ == "__main__":
    main()

    