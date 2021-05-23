from offer import Offer
from package import Package
from package_manager import PackageManager
from vehicle import Vehicle

import json 

def createOffers(offers):
    # Gets list of objects and convert them into Offer Class objects
    offers = [Offer(offer) for offer in offers]
    return offers

def createPackages(no_of_packages):
    # Gets not of packages to be created and returns them in an array
    try:
        no_of_packages = int(no_of_packages)
    except ValueError as e:
        raise e 
    packages = [Package(input().split( )) for _ in range(no_of_packages)]
    return packages

def createVehicles(no_of_vehicles,max_speed,max_weight):
    # Getting No of vehicles , Max Speed and Max Weight
    for _ in range(no_of_vehicles):
        Vehicle(max_speed,max_weight)

def readOffers():
    # Reads Offers from offers.json and returns an array of objects containing offers
    try:
        f = open('offers.json')
        offers = json.load(f)
        f.close()
        return offers
    except FileNotFoundError as e:
        raise e

def main():
    print("Courier Service")

    # Creating the offers
    offers = readOffers()
    createOffers(offers)
    
    # Getting Base Delivery Cost and No of Packages
    base_delivery_cost,no_of_packages = input().split( )

    # Creating the packages
    packages = createPackages(no_of_packages)
    
    # Getting No of vehicles , Max Speed and Max Weight
    no_of_vehicles,max_speed,max_weight = input().split( )
    
    try:
        base_delivery_cost = float(base_delivery_cost)
        no_of_vehicles = int(no_of_vehicles)
        max_speed = float(max_speed)
        max_weight = int(max_weight)

        # Checking if there are any zero values in base_delivery_cost,no_of_vehicles,max_speed,max_weight
        if 0 in [base_delivery_cost,no_of_vehicles,max_speed,max_weight] or 0.0 in [base_delivery_cost,no_of_vehicles,max_speed,max_weight]:
            raise ValueError('It Cannot Be Zero')

    except ValueError as e:
        raise e

    # Creating Vehicles
    createVehicles(no_of_vehicles,max_speed,max_weight)

    #initialize Package Manager
    manager = PackageManager(no_of_packages,base_delivery_cost,no_of_vehicles,max_speed,max_weight)
    
    # Calculate package combination, time taken and delivery cost
    manager.calculatePackages()
    
    #print the output
    print('*'*100)
    for package in packages:
        print(f'{package.name} {package.discounted_price} {package.delivery_cost} {package.delivery_time}')

if __name__ == "__main__":
    main()

