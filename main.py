from offer import Offer
from package import Package
# from vehicle import Vehicle

import json 

def createOffers(offers):
    # Gets Array of objects and convert them into class objects
    offers = [Offer(offer) for offer in offers]
    return offers

def createPackages(no_of_packages):
    packages = [Package(input().split( )) for _ in range(no_of_packages)]
    return packages

# def createVehicles(no_of_packages):
#     no_of_vehicles,max_speed,_max_weight = input().split( )
#     vehicles = [Vehicle(max_speed,max_weight) for _ in range(no_of_vehicles)]
#     return vehicles

def main():
    print("Courier Service")
    print("Please Enter The Input")

    f = open('offers.json')
    offers = json.load(f)
    f.close()
    offers = createOffers(offers)

    base_delivery_cost,no_of_packages = input().split( )
    no_of_packages = int(no_of_packages)
    base_delivery_cost = int(base_delivery_cost)
    packages = createPackages(no_of_packages)

    # for package in packages:
    #     package.calculateDeliveryCost(base_delivery_cost)
    
    no_of_vehicles,max_speed,max_weight = input().split( )
    no_of_vehicles = float(no_of_vehicles)
    max_speed = float(max_speed)
    max_weight = float(max_weight)
    
    for package in packages:
        package.calculateTimeTaken(base_delivery_cost,no_of_vehicles,max_speed,max_weight)


    # 100 3
    # PKG1 5 5 OFR001
    # PKG2 15 5 OFR002
    # PKG3 10 100 OFR003
if __name__ == "__main__":
    main()

    