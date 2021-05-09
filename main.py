from offer import Offer
from package import Package

import json 

def create_offers(offers):
    # Gets Array of objects and convert them into class objects
    offers = [Offer(offer) for offer in offers]
    return offers

def create_packages(no_of_packages):
    packages = [Package(input().split( )) for _ in range(no_of_packages)]
    return packages

def main():
    print("Courier Service")
    print("Please Enter The Input")

    f = open('offers.json')
    offers = json.load(f)
    f.close()
    offers = create_offers(offers)


    delivery_cost,no_of_packages = input().split( )
    no_of_packages = int(no_of_packages)
    packages = create_packages(no_of_packages)

    import pdb;pdb.set_trace()
    Package().calculate_total_delivery_cost()
    

    # 100 3
    # PKG1 5 5 OFR001
    # PKG2 15 5 OFR002
    # PKG3 10 100 OFR003
if __name__ == "__main__":
    main()

    